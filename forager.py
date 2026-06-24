"""
forager.py
----------
All interactions with the Forager API.

Base URL : https://api-v2.forager.ai/api/{account_id}/
Auth     : X-API-KEY header

IMPORTANT NOTES (discovered by probing the live API, the docs were inaccurate):
  * The Forager edge sits behind Cloudflare, which blocks the default
    Python/requests User-Agent with HTTP 403 ("error code: 1010"). We therefore
    send a browser-like User-Agent on every request.
  * Search endpoints return results under the "search_results" key (NOT
    "results"), alongside a "total_search_results" count.
  * Company records use "domain" (a single string), "employees_amount",
    "finance_info.revenue", and "linkedin_info.public_profile_url".
  * The contact-lookup endpoints return a BARE JSON ARRAY, e.g.
    [{"email": "...", "email_type": "personal", "validation_status": "valid"}].
"""

import logging
import os
import re

import requests

import httpclient

logger = logging.getLogger(__name__)

_SESSION = httpclient.make_session()

FORAGER_BASE = "https://api-v2.forager.ai/api"
FORAGER_API_KEY = os.environ.get("FORAGER_API_KEY")
FORAGER_ACCOUNT_ID = os.environ.get("FORAGER_ACCOUNT_ID")

# Cloudflare blocks the default requests User-Agent; pretend to be a browser.
_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)


def _headers() -> dict:
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": _BROWSER_UA,
        "X-API-KEY": FORAGER_API_KEY or "",
    }


def _url(path: str) -> str:
    return f"{FORAGER_BASE}/{FORAGER_ACCOUNT_ID}/{path}"


def _post(path: str, payload: dict) -> dict | list:
    resp = _SESSION.post(_url(path), json=payload, headers=_headers(), timeout=60)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# ORGANIZATION SEARCH
# POST /datastorage/organization_search/
# Response: {"search_results": [...], "total_search_results": int}
# ---------------------------------------------------------------------------
def _normalize_domain(value: str | None) -> str:
    """Lower-case and strip scheme / path / leading 'www.' so domain comparison is
    robust ('https://www.OpenAI.com/' -> 'openai.com')."""
    d = (value or "").lower().strip()
    for scheme in ("https://", "http://"):
        if d.startswith(scheme):
            d = d[len(scheme):]
    d = d.split("/")[0].strip()
    if d.startswith("www."):
        d = d[4:]
    return d


def _domain_matches(org: dict, domain: str) -> bool:
    return _normalize_domain(org.get("domain")) == _normalize_domain(domain)


def _org_score(org: dict) -> tuple:
    """Sort key: lower domain_rank is more canonical (None ranks worst);
    break ties by larger headcount."""
    rank = org.get("domain_rank")
    rank_key = rank if isinstance(rank, int) else float("inf")
    employees = org.get("employees_amount") or 0
    return (rank_key, -employees)


def search_organization(
    domain: str | None = None,
    name: str | None = None,
    linkedin_identifier: str | None = None,
    max_pages: int = 3,
) -> dict | None:
    """
    Find the single best-matching company.

    Strategy (in priority order):
      1. linkedin_identifier  -> exact, most reliable.
      2. domain               -> domain search returns lots of noise (personal
                                 pages that merely list the domain), so we
                                 paginate and pick the best exact-domain match
                                 by (domain_rank, headcount).
      3. name                 -> fuzzy text search; only trusted on an exact
                                 name match, as a last resort.
    Returns the chosen org dict, or None.
    """
    # 1) LinkedIn identifier — most precise.
    if linkedin_identifier:
        data = _post(
            "datastorage/organization_search/",
            {"page": 0, "linkedin_public_identifiers": [linkedin_identifier]},
        )
        results = (data or {}).get("search_results", [])
        if results:
            return results[0]

    # 2) Domain — the plain domain search is extremely noisy: a search for
    #    openai.com returns 37 unrelated projects (Wordwise, ChatGPT, SORA AI...)
    #    that all list openai.com as their own domain, and the real OpenAI isn't
    #    even on the first page. So we resolve by LinkedIn handle FIRST.
    if domain:
        # (a) The handle guessed from the domain root (openai.com -> "openai")
        #     returns the one canonical company. Validate it owns the domain,
        #     then trust it over the noisy domain results.
        root = _normalize_domain(domain).split(".")[0]
        if root:
            slug_data = _post(
                "datastorage/organization_search/",
                {"page": 0, "linkedin_public_identifiers": [root]},
            )
            for org in (slug_data or {}).get("search_results", []):
                if _domain_matches(org, domain):
                    return org
        # (b) Fall back to the domain search, keeping ONLY orgs that actually own
        #     the domain and preferring the most canonical (a real domain_rank
        #     beats None, then larger headcount). Never pick from the noise.
        candidates: list[dict] = []
        for page in range(max_pages):
            data = _post("datastorage/organization_search/", {"page": page, "domains": [domain]})
            batch = (data or {}).get("search_results", [])
            candidates.extend(batch)
            total = (data or {}).get("total_search_results") or 0
            if not batch or len(candidates) >= total:
                break
        exact = [o for o in candidates if _domain_matches(o, domain)]
        if exact:
            return sorted(exact, key=_org_score)[0]

    # 3) Name — fuzzy; require an exact name match to avoid garbage.
    if name:
        data = _post("datastorage/organization_search/", {"page": 0, "description": name})
        for org in (data or {}).get("search_results", []):
            if (org.get("name") or "").strip().lower() == name.strip().lower():
                return org

    return None


def get_organization_by_linkedin(linkedin_identifier: str) -> dict | None:
    """Fetch an org by its LinkedIn slug, e.g. 'openai'."""
    return search_organization(linkedin_identifier=linkedin_identifier)


# LinkedIn stores a merged/duplicate company page as
# ".../company/duplicate__<id>_<slug>" — a dead shell left over when it merges
# duplicate listings (e.g. apify.com's record carries
# ".../company/duplicate__10608457_apify/" instead of ".../company/apify/").
# Forager passes that stale URL straight through, so rewrite it to the canonical
# ".../company/<slug>" before it reaches HubSpot.
_DUP_LINKEDIN_RE = re.compile(r"(/company/)duplicate__\d+_([^/?#]+)", re.IGNORECASE)


def _clean_linkedin_url(url: str) -> str:
    if not url:
        return url
    return _DUP_LINKEDIN_RE.sub(r"\1\2", url)


def _company_location(org: dict) -> dict:
    """City / state / country for a company, robust to Forager's varying shapes.

    Forager's flat company address often carries city + country but an EMPTY state,
    while the richer ``osm_locations`` structure (the same one used for people) does
    include the state/region. So we read the flat address first, then backfill any
    missing piece from osm_locations on the address or the org."""
    addresses = org.get("addresses") or []
    addr = addresses[0] if isinstance(addresses, list) and addresses else {}
    city = (addr.get("city") or "").strip()
    state = (addr.get("state") or addr.get("region") or addr.get("state_name") or "").strip()
    country = (addr.get("country") or "").strip()
    if not (city and state and country):
        for loc in (addr, addr.get("location"), org.get("location")):
            if isinstance(loc, dict) and loc.get("osm_locations"):
                parts = _location_parts(loc)
                city = city or parts["city"]
                state = state or parts["state"]
                country = country or parts["country"]
                break
    return {"city": city, "state": state, "country": country}


def parse_company_fields(org: dict) -> dict:
    """Flatten a Forager org record into HubSpot company properties."""
    if not org:
        return {}
    li = org.get("linkedin_info") or {}
    industry = (li.get("industry") or {}).get("name", "")
    finance = org.get("finance_info") or {}
    founded = org.get("founded_date") or ""
    loc = _company_location(org)
    return {
        "name": org.get("name", "") or "",
        "domain": org.get("domain", "") or "",
        "description": org.get("description", "") or "",
        "linkedin_company_page": _clean_linkedin_url(li.get("public_profile_url", "") or ""),
        "numberofemployees": org.get("employees_amount"),
        "annualrevenue": finance.get("revenue"),
        "founded_year": founded[:4] if founded else "",
        "city": loc["city"],
        "state": loc["state"],
        "country": loc["country"],
        "industry_forager": industry,
        "website": org.get("website", "") or "",
        "forager_org_id": str(org.get("id", "")),
    }


# ---------------------------------------------------------------------------
# PEOPLE SEARCH
# POST /datastorage/person_role_search/
# Each result is a ROLE object holding nested "person" and "organization".
# ---------------------------------------------------------------------------
def find_contacts_at_company(
    organization_domain: str,
    job_title_filter: str | None = None,
    page: int = 0,
) -> list[dict]:
    """Find current people at a company domain (optionally filtered by title).
    Returns a list of role records (each with nested person + organization)."""
    payload = {
        "page": page,
        "organization_domains": [organization_domain],
        "role_is_current": True,
    }
    if job_title_filter:
        payload["role_title"] = job_title_filter
    data = _post("datastorage/person_role_search/", payload)
    return (data or {}).get("search_results", [])


def find_contacts_at_company_with_total(organization_domain: str, page: int = 0) -> tuple[list[dict], int | None]:
    """Like find_contacts_at_company, but also returns Forager's TOTAL count of
    current people it has for the domain (``total_search_results``). Used by the
    discovery diagnostic so we can tell 'ran out of people' from 'hit the page cap'."""
    payload = {
        "page": page,
        "organization_domains": [organization_domain],
        "role_is_current": True,
    }
    data = _post("datastorage/person_role_search/", payload)
    return (data or {}).get("search_results", []), (data or {}).get("total_search_results")


def _role_person_slug(role: dict) -> str:
    return (((role.get("person") or {}).get("linkedin_info") or {}).get("public_identifier") or "").lower()


def find_person_by_linkedin(linkedin_identifier: str) -> dict | None:
    """Look up one person's role record (full profile) DIRECTLY by LinkedIn id.

    Uses person_role_search's ``person_linkedin_public_identifiers`` filter (confirmed
    by probing the live API; the plain ``linkedin_public_identifiers`` is ignored and
    returns an arbitrary person). We still VALIDATE the returned person's slug matches
    before trusting it, and return None on no match so the caller falls back to the
    email/phone-only lookup — never wrong-person data."""
    if not linkedin_identifier:
        return None
    want = linkedin_identifier.lower().strip()
    try:
        data = _post("datastorage/person_role_search/",
                     {"page": 0, "person_linkedin_public_identifiers": [linkedin_identifier]})
    except Exception as exc:  # noqa: BLE001
        logger.warning("person_role_search by linkedin (%s) failed: %s", linkedin_identifier, exc)
        return None
    for role in (data or {}).get("search_results", []):
        if _role_person_slug(role) == want:
            return role
    return None


def probe_person_by_linkedin(linkedin_identifier: str) -> dict:
    """Diagnostic only (/debug/person-test): try several Forager calls to fetch a
    person by LinkedIn id and report which — if any — returns the MATCHING person."""
    want = (linkedin_identifier or "").lower().strip()
    attempts = [
        ("person_role_search: linkedin_public_identifiers", "datastorage/person_role_search/",
         {"page": 0, "linkedin_public_identifiers": [linkedin_identifier]}),
        ("person_role_search: linkedin_public_identifier", "datastorage/person_role_search/",
         {"page": 0, "linkedin_public_identifier": linkedin_identifier}),
        ("person_role_search: person_linkedin_public_identifiers", "datastorage/person_role_search/",
         {"page": 0, "person_linkedin_public_identifiers": [linkedin_identifier]}),
        ("person_search: linkedin_public_identifiers", "datastorage/person_search/",
         {"page": 0, "linkedin_public_identifiers": [linkedin_identifier]}),
        ("person_search: linkedin_public_identifier", "datastorage/person_search/",
         {"page": 0, "linkedin_public_identifier": linkedin_identifier}),
    ]
    report = []
    for name, path, payload in attempts:
        item = {"attempt": name}
        try:
            data = _post(path, payload)
        except Exception as exc:  # noqa: BLE001
            item["error"] = str(exc)[:140]
            report.append(item)
            continue
        results = data if isinstance(data, list) else (data or {}).get("search_results", [])
        item["count"] = len(results) if isinstance(results, list) else "?"
        match = next((r for r in (results if isinstance(results, list) else [])
                      if isinstance(r, dict) and _role_person_slug(r) == want), None)
        item["matched"] = bool(match)
        if match:
            item["title"] = match.get("role_title")
            item["company"] = (match.get("organization") or {}).get("name")
        report.append(item)
    return {"slug": linkedin_identifier, "attempts": report}


def probe_company_person(company_name: str, firstname: str, lastname: str) -> dict:
    """Diagnostic only (/debug/company-test): for a name + company, report (1) whether
    the company resolves to a domain, (2) whether the person is findable by name — via
    a direct person-name filter, and via paging the company's people (current method)."""
    want = f"{firstname} {lastname}".strip().lower()
    org = search_organization(name=company_name)
    domain = (org or {}).get("domain")
    out = {"input": {"company": company_name, "name": f"{firstname} {lastname}"},
           "company_resolved": {"name": (org or {}).get("name"), "domain": domain}}

    name_attempts = []
    for param, val in (
        ("full_name", f"{firstname} {lastname}"),
        ("person_full_names", [f"{firstname} {lastname}"]),
        ("full_names", [f"{firstname} {lastname}"]),
        ("names", [f"{firstname} {lastname}"]),
    ):
        payload = {"page": 0, param: val}
        if domain:
            payload["organization_domains"] = [domain]
        try:
            data = _post("datastorage/person_role_search/", payload)
            res = (data or {}).get("search_results", [])
            m = next((r for r in res if f"{(r.get('person') or {}).get('first_name', '')} "
                      f"{(r.get('person') or {}).get('last_name', '')}".strip().lower() == want), None)
            name_attempts.append({"param": param, "count": len(res), "matched": bool(m)})
        except Exception as exc:  # noqa: BLE001
            name_attempts.append({"param": param, "error": str(exc)[:100]})
    out["name_filter_attempts"] = name_attempts

    if domain:
        seen, found = [], None
        for page in range(5):
            roles = find_contacts_at_company(domain, page=page)
            if not roles:
                break
            for r in roles:
                p = r.get("person") or {}
                nm = f"{p.get('first_name', '')} {p.get('last_name', '')}".strip().lower()
                if len(seen) < 10:
                    seen.append(nm)
                if nm == want:
                    found = page
            if found is not None:
                break
        out["paged_search"] = {"found_on_page": found, "sample_names_seen": seen}
    return out


# ---------------------------------------------------------------------------
# CONTACT ENRICHMENT (emails + phones)
# These endpoints return a bare JSON array. Accepts {"person_id": int} or
# {"linkedin_public_identifier": str}.
# ---------------------------------------------------------------------------
def _lookup_body(person_id: int | None, linkedin_identifier: str | None) -> dict | None:
    if person_id:
        return {"person_id": person_id}
    if linkedin_identifier:
        return {"linkedin_public_identifier": linkedin_identifier}
    return None


def get_person_emails(person_id: int | None = None, linkedin_identifier: str | None = None) -> list[str]:
    """Look up personal + work emails. Prefers person_id when available."""
    body = _lookup_body(person_id, linkedin_identifier)
    if body is None:
        return []
    emails: list[str] = []
    for endpoint in ("personal_emails", "work_emails"):
        try:
            data = _post(f"datastorage/person_contacts_lookup/{endpoint}/", body)
            emails += [e.get("email") for e in (data or []) if isinstance(e, dict) and e.get("email")]
        except Exception as exc:  # noqa: BLE001 - one bad lookup shouldn't kill the rest
            logger.warning("email lookup (%s) failed: %s", endpoint, exc)
    return list(dict.fromkeys(emails))  # de-duplicate, preserve order


def get_person_phones(person_id: int | None = None, linkedin_identifier: str | None = None) -> list[str]:
    """Look up phone numbers. Prefers person_id when available."""
    body = _lookup_body(person_id, linkedin_identifier)
    if body is None:
        return []
    try:
        data = _post("datastorage/person_contacts_lookup/phone_numbers/", body)
        phones = [p.get("phone_number") for p in (data or []) if isinstance(p, dict) and p.get("phone_number")]
        return list(dict.fromkeys(phones))
    except Exception as exc:  # noqa: BLE001
        logger.warning("phone lookup failed: %s", exc)
        return []


def _location_parts(location: dict | None) -> dict:
    """Extract city / state / country from a Forager location's osm_locations."""
    location = location or {}
    parts = {"city": "", "state": "", "country": ""}
    for entry in location.get("osm_locations") or []:
        place_type = entry.get("place_type")
        value = (entry.get("name") or "").split(",")[0].strip()
        if place_type == "country" and not parts["country"]:
            parts["country"] = value
        elif place_type in ("state", "region") and not parts["state"]:
            parts["state"] = value
        elif place_type in ("city", "town", "municipality", "village") and not parts["city"]:
            parts["city"] = value
    if not parts["city"] and location.get("name"):
        candidate = location["name"].split(",")[0].strip()
        if candidate.lower() != (parts["country"] or "").lower():
            parts["city"] = candidate
    return parts


def parse_person_fields(role: dict, emails: list, phones: list) -> dict:
    """Flatten a Forager role record (+ contacts) into HubSpot contact properties."""
    if not role:
        return {}
    person = role.get("person") or {}
    org = role.get("organization") or {}
    person_li = person.get("linkedin_info") or {}
    org_li = org.get("linkedin_info") or {}
    location = _location_parts(person.get("location"))
    skills = [s.get("name", "") for s in (person.get("skills") or []) if s.get("name")]
    return {
        "firstname": person.get("first_name", "") or "",
        "lastname": person.get("last_name", "") or "",
        "jobtitle": role.get("role_title", "") or "",
        # Personal email -> HubSpot's migrated "Email (home)" field (internal name
        # migrated_emails_home). The built-in `email` stays empty (reserved).
        "migrated_emails_home": emails[0] if emails else "",
        "phone": phones[0] if phones else "",
        "city": location["city"],
        "state": location["state"],
        "country": location["country"],
        "linkedin_url": _clean_linkedin_url(person_li.get("public_profile_url", "") or ""),
        "company": org.get("name", "") or "",
        "company_domain": org.get("domain", "") or "",
        "company_linkedin_url": _clean_linkedin_url(org_li.get("public_profile_url", "") or ""),
        # Nice-to-haves (stored in custom properties)
        "person_description": person.get("description", "") or "",
        "person_headline": person.get("headline", "") or "",
        "person_skills": ", ".join(skills[:10]),
        "forager_person_id": str(person.get("id", "")),
        "all_emails": ", ".join(emails),
        "all_phones": ", ".join(phones),
    }
