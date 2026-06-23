"""
enrichment.py
-------------
Business logic: orchestrates Forager lookups and HubSpot writes.

Five capabilities:
  enrich_company           - fill a HubSpot company from Forager
  enrich_contact           - fill a HubSpot contact's email/phone from Forager
  find_and_create_contacts - discover people at a company, create + associate
  handle_company_webhook   - company-created pipeline (enrich + find people)
  handle_contact_webhook   - contact-created pipeline (enrich the contact)
"""

import logging

import buyer_committee
import forager
import hubspot
import scoring

logger = logging.getLogger(__name__)


def _linkedin_slug(url: str) -> str | None:
    """Extract the slug from a LinkedIn personal URL (.../in/<slug>)."""
    if url and "linkedin.com/in/" in url:
        return url.rstrip("/").split("/in/")[-1].split("?")[0]
    return None


# A contact's LinkedIn URL can live in several HubSpot fields depending on how it
# was entered: HubSpot's built-in "LinkedIn URL" (hs_linkedin_url) when typed into
# the standard field, our custom "LinkedIn Profile URL" (linkedin_url) when we write
# it back, or the built-in "LinkedIn Profile" (linkedin_profile). Check them all.
_CONTACT_LINKEDIN_FIELDS = ("linkedin_url", "hs_linkedin_url", "linkedin_profile")


def _contact_linkedin_slug(props: dict) -> str | None:
    for field in _CONTACT_LINKEDIN_FIELDS:
        slug = _linkedin_slug(props.get(field) or "")
        if slug:
            return slug
    return None


def _company_linkedin_slug(url: str) -> str | None:
    """Extract the company slug from a LinkedIn company URL (.../company/<slug>)."""
    if url and "linkedin.com/company/" in url:
        slug = url.rstrip("/").split("/company/")[-1].split("?")[0].split("/")[0]
        return slug or None
    return None


def _find_person_role(slug: str | None, firstname: str, lastname: str,
                      company_name: str, max_pages: int = 5) -> dict | None:
    """Find a person's Forager role record (full profile) by resolving their company
    and matching them among its current people — by LinkedIn slug when we have one,
    otherwise by first+last name. Returns the role dict, or None if not found.

    Needs a company to scope the people search; name-matching is best-effort."""
    if not company_name:
        return None
    org = forager.search_organization(name=company_name)
    domain = (org or {}).get("domain")
    if not domain:
        return None
    want_slug = (slug or "").lower()
    want_name = f"{firstname} {lastname}".strip().lower()
    for page in range(max_pages):
        roles = forager.find_contacts_at_company(domain, page=page)
        if not roles:
            break
        for role in roles:
            person = role.get("person") or {}
            p_slug = ((person.get("linkedin_info") or {}).get("public_identifier") or "").lower()
            p_name = f"{person.get('first_name', '')} {person.get('last_name', '')}".strip().lower()
            if want_slug and p_slug and p_slug == want_slug:
                return role
            if want_name and p_name and p_name == want_name:
                return role
    return None


def enrich_company(hubspot_company_id: str, force: bool = False) -> dict:
    """Fetch a company from HubSpot, find it in Forager, write enriched fields back.

    Idempotent by default: if the company already carries a forager_org_id (we have
    enriched it before), it is skipped unless force=True. This stops a duplicate
    webhook delivery from re-running the Forager search + LLM scoring and re-spending."""
    hubspot.ensure_custom_properties()
    company = hubspot.get_company(hubspot_company_id)
    if not company:
        return {"error": f"Company {hubspot_company_id} not found in HubSpot"}

    props = company.get("properties", {})
    domain = (props.get("domain") or "").strip()
    name = (props.get("name") or "").strip()
    # Also accept a company LinkedIn URL as a resolver: when no domain is set,
    # resolve the company by its LinkedIn handle (exact) — that fills in the
    # website/domain + all other fields. When a domain IS set, the existing
    # domain flow runs unchanged.
    li_slug = _company_linkedin_slug(props.get("linkedin_company_page") or "")

    # Skip only if the company is BOTH enriched (forager_org_id) AND scored
    # (icp_match_score) — so a company that missed scoring (e.g. a transient LLM
    # 503/429 blip) is completed on the next run instead of being skipped forever.
    # If scoring isn't configured at all, there's nothing to backfill, so skip too.
    already_enriched = bool((props.get("forager_org_id") or "").strip())
    already_scored = bool((props.get("icp_match_score") or "").strip())
    if not force and already_enriched and (already_scored or scoring.provider() is None):
        return {"hubspot_company_id": hubspot_company_id, "status": "skipped",
                "reason": "already enriched + scored (or scoring disabled); use /enrich/company to force a refresh",
                "domain": domain}

    org = forager.search_organization(
        domain=domain or None, name=name or None,
        linkedin_identifier=(li_slug if not domain else None),
    )
    if not org:
        return {"error": f"No Forager match for domain='{domain}' name='{name}' linkedin='{li_slug or ''}'"}

    fields = forager.parse_company_fields(org)

    # Score the company in parallel to enrichment (diagram: ICP fit + logo
    # recognizability via Claude). Skips gracefully if scoring isn't configured,
    # and never blocks the Forager write-back on a scoring failure.
    scores = scoring.score_company(fields.get("name") or name, fields)

    hubspot.update_company(hubspot_company_id, {**fields, **scores.get("hubspot_fields", {})})
    return {
        "hubspot_company_id": hubspot_company_id,
        "forager_org_id": fields.get("forager_org_id"),
        "name": fields.get("name"),
        "domain": fields.get("domain"),
        "employees": fields.get("numberofemployees"),
        "revenue": fields.get("annualrevenue"),
        "icp": scores.get("icp"),
        "logo": scores.get("logo"),
        "scoring_status": scores.get("status"),
        "status": "enriched",
    }


def enrich_contact(hubspot_contact_id: str) -> dict:
    """Enrich a single contact (manual add or company-discovered): pull the full
    Forager field set via the person's LinkedIn URL, or first+last name + company."""
    hubspot.ensure_custom_properties()
    contact = hubspot.get_contact(hubspot_contact_id)
    if not contact:
        return {"error": f"Contact {hubspot_contact_id} not found in HubSpot"}

    props = contact.get("properties", {})

    # Idempotency guard: contacts our pipeline created/enriched carry a Forager
    # person id. Both webhooks (company-created and contact-created) are active,
    # so without this the contact-created webhook would re-enrich every contact
    # the company pipeline just created (each already has a LinkedIn URL),
    # doubling Forager credit spend. Skip anything already stamped by us.
    if (props.get("forager_person_id") or "").strip():
        return {
            "hubspot_contact_id": hubspot_contact_id,
            "status": "skipped",
            "reason": "already enriched (forager_person_id present)",
        }

    slug = _contact_linkedin_slug(props)
    firstname = (props.get("firstname") or "").strip()
    lastname = (props.get("lastname") or "").strip()
    company_name = (props.get("company") or "").strip()

    # Resolve the person's full Forager profile so we can fill ALL the fields
    # (job title, location, company links, personal email -> Email Home, phone),
    # not just email/phone. We match them among their company's people by LinkedIn
    # slug when we have one, else by first+last name.
    role = _find_person_role(slug, firstname, lastname, company_name)
    if role:
        person = role.get("person") or {}
        person_id = person.get("id")
        person_slug = slug or (person.get("linkedin_info") or {}).get("public_identifier")
        emails = forager.get_person_emails(person_id=person_id, linkedin_identifier=person_slug)
        phones = forager.get_person_phones(person_id=person_id, linkedin_identifier=person_slug)
        fields = forager.parse_person_fields(role, emails, phones)
        hubspot.update_contact(hubspot_contact_id, fields)
        return {
            "hubspot_contact_id": hubspot_contact_id,
            "status": "enriched",
            "matched_by": "linkedin" if slug else "name+company",
            "email_home": fields.get("email_home"),
            "phone": fields.get("phone"),
            "title": fields.get("jobtitle"),
        }

    # No resolvable company for the full profile — but if we have a LinkedIn URL,
    # still pull the personal email + phone directly by slug.
    if slug:
        emails = forager.get_person_emails(linkedin_identifier=slug)
        phones = forager.get_person_phones(linkedin_identifier=slug)
        update: dict = {}
        if emails:
            update["email_home"] = emails[0]
            update["all_emails"] = ", ".join(emails)
        if phones:
            update["phone"] = phones[0]
            update["all_phones"] = ", ".join(phones)
        if update:
            hubspot.update_contact(hubspot_contact_id, update)
        return {
            "hubspot_contact_id": hubspot_contact_id,
            "status": "enriched" if update else "no_data_found",
            "matched_by": "linkedin (email/phone only — add a Company for full enrichment)",
            "emails_found": emails,
            "phones_found": phones,
        }

    return {
        "hubspot_contact_id": hubspot_contact_id,
        "status": "skipped",
        "reason": "need a LinkedIn URL, or first+last name + company, to enrich",
    }


def find_and_create_contacts(
    hubspot_company_id: str,
    company_domain: str,
    job_title_filter: str | None = None,
    max_contacts: int = 5,
) -> list[dict]:
    """Discover people at a company, enrich them, create/update + associate in HubSpot.

    Only people whose job title is on the TAM buyer-committee list
    (``buyer_committee.matches_buyer_committee``) are created — everyone else is
    skipped *before* any (credit-spending) Forager contact lookup. ``job_title_filter``,
    if given, is an additional narrowing applied on top of the committee list.

    Of the buyer-committee matches, only people for whom Forager returns an email
    are created — emailless records can't be de-duplicated, so they're skipped.
    The function is idempotent: contacts the company already has count toward
    ``max_contacts``, so a re-delivered webhook neither creates extra rows nor
    re-spends Forager credits.
    """
    hubspot.ensure_custom_properties()

    # What does the company already have? Count enriched (email-bearing) contacts
    # and remember their Forager person ids so we never re-process / re-pay for them.
    seen_person_ids: set[str] = set()
    already = 0
    for existing_contact in hubspot.get_contacts_for_company(hubspot_company_id):
        cp = existing_contact.get("properties", {})
        pid = (cp.get("forager_person_id") or "").strip()
        if pid:
            seen_person_ids.add(pid)
            already += 1

    needed = max_contacts - already
    results: list[dict] = []
    if needed <= 0:
        return [{"status": "skipped",
                 "reason": f"company already has {already} enriched contact(s); max is {max_contacts}"}]

    # Scan candidates until we've created `needed` email-having contacts. Bound the
    # scan (candidate_budget / MAX_PAGES) so a low email hit-rate can't run away
    # with credits — each email lookup costs Forager credits.
    candidate_budget = needed * 2
    scanned = 0
    page = 0
    # Scan deeper: the buyer-committee filter is narrow, so for large / non-SaaS
    # companies the qualifying titles can be sparse on the first pages. People who
    # don't match are skipped for free, and credits are still only spent on matches
    # (up to max_contacts), so a deeper scan costs nothing extra in Forager credits.
    MAX_PAGES = 10
    while needed > 0 and page < MAX_PAGES and scanned < candidate_budget:
        # Fetch the broad set of current people (no Forager-side title filter) so
        # we can apply the full buyer-committee list locally.
        roles = forager.find_contacts_at_company(
            company_domain, job_title_filter=None, page=page
        )
        page += 1
        if not roles:
            break
        for role in roles:
            if needed <= 0 or scanned >= candidate_budget:
                break
            role_title = role.get("role_title") or ""
            # Title gate (free, local): only buyer-committee titles are created.
            if not buyer_committee.matches_buyer_committee(role_title):
                continue
            if job_title_filter and job_title_filter.lower() not in role_title.lower():
                continue
            person = role.get("person") or {}
            person_id = person.get("id")
            pid = str(person_id) if person_id else ""
            if pid and pid in seen_person_ids:
                continue  # already handled (this run or a previous delivery)
            if pid:
                seen_person_ids.add(pid)
            scanned += 1
            slug = (person.get("linkedin_info") or {}).get("public_identifier")

            # The buyer-committee title match is now the ONLY gate. Pull email +
            # phone if Forager has them (email lands in Email Home), but do NOT
            # require an email — every title-matched contact is dumped regardless.
            emails = forager.get_person_emails(person_id=person_id, linkedin_identifier=slug)
            phones = forager.get_person_phones(person_id=person_id, linkedin_identifier=slug)
            fields = forager.parse_person_fields(role, emails, phones)

            existing = hubspot.find_contact_by_email_home(fields["email_home"])
            if existing:
                contact_id = existing["id"]
                hubspot.update_contact(contact_id, fields)
                action = "updated"
            else:
                created = hubspot.create_contact(fields)
                contact_id = created["id"]
                action = "created"

            try:
                hubspot.associate_contact_to_company(contact_id, hubspot_company_id)
            except Exception as exc:  # noqa: BLE001
                logger.warning("Association failed for contact %s: %s", contact_id, exc)

            needed -= 1
            results.append({
                "contact_id": contact_id,
                "name": f"{fields.get('firstname', '')} {fields.get('lastname', '')}".strip(),
                "email_home": fields.get("email_home"),
                "phone": fields.get("phone"),
                "title": fields.get("jobtitle"),
                "action": action,
            })
    return results


def handle_company_webhook(hubspot_company_id: str, job_title_filter: str | None = None,
                           max_contacts: int = 5, force: bool = False) -> dict:
    """Company-created pipeline: enrich company -> enrich existing contacts -> find new ones."""
    company_result = enrich_company(hubspot_company_id, force=force)
    if "error" in company_result:
        return company_result

    company_domain = company_result.get("domain", "") or ""
    existing_contacts = hubspot.get_contacts_for_company(hubspot_company_id)
    enriched_existing = [enrich_contact(c["id"]) for c in existing_contacts]

    new_contacts = []
    if company_domain:
        new_contacts = find_and_create_contacts(
            hubspot_company_id=hubspot_company_id,
            company_domain=company_domain,
            job_title_filter=job_title_filter,
            max_contacts=max_contacts,
        )

    return {
        "company": company_result,
        "enriched_existing": enriched_existing,
        "new_contacts": new_contacts,
    }


def handle_contact_webhook(hubspot_contact_id: str) -> dict:
    """Contact-created pipeline: enrich the contact."""
    return enrich_contact(hubspot_contact_id)
