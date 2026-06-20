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

import requests

logger = logging.getLogger(__name__)

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
    resp = requests.post(_url(path), json=payload, headers=_headers(), timeout=60)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# ORGANIZATION SEARCH
# POST /datastorage/organization_search/
# Response: {"search_results": [...], "total_search_results": int}
# ---------------------------------------------------------------------------
def _domain_matches(org: dict, domain: str) -> bool:
    return (org.get("domain") or "").lower().strip() == (domain or "").lower().strip()


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

    # 2) Domain — paginate and rank.
    if domain:
        candidates: list[dict] = []
        for page in range(max_pages):
            data = _post("datastorage/organization_search/", {"page": page, "domains": [domain]})
            batch = (data or {}).get("search_results", [])
            candidates.extend(batch)
            total = (data or {}).get("total_search_results") or 0
            if not batch or len(candidates) >= total:
                break
        exact = [o for o in candidates if _domain_matches(o, domain)]
        pool = exact or candidates
        if pool:
            return sorted(pool, key=_org_score)[0]

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


def parse_company_fields(org: dict) -> dict:
    """Flatten a Forager org record into HubSpot company properties."""
    if not org:
        return {}
    li = org.get("linkedin_info") or {}
    industry = (li.get("industry") or {}).get("name", "")
    finance = org.get("finance_info") or {}
    addresses = org.get("addresses") or []
    addr = addresses[0] if addresses else {}
    founded = org.get("founded_date") or ""
    return {
        "name": org.get("name", "") or "",
        "domain": org.get("domain", "") or "",
        "description": org.get("description", "") or "",
        "linkedin_company_page": li.get("public_profile_url", "") or "",
        "numberofemployees": org.get("employees_amount"),
        "annualrevenue": finance.get("revenue"),
        "founded_year": founded[:4] if founded else "",
        "city": addr.get("city", "") or "",
        "state": addr.get("state", "") or "",
        "country": addr.get("country", "") or "",
        "industry": industry,
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
        "email": emails[0] if emails else "",
        "phone": phones[0] if phones else "",
        "city": location["city"],
        "state": location["state"],
        "country": location["country"],
        "linkedin_url": person_li.get("public_profile_url", "") or "",
        "company": org.get("name", "") or "",
        "company_domain": org.get("domain", "") or "",
        "company_linkedin_url": org_li.get("public_profile_url", "") or "",
        # Nice-to-haves (stored in custom properties)
        "person_description": person.get("description", "") or "",
        "person_headline": person.get("headline", "") or "",
        "person_skills": ", ".join(skills[:10]),
        "forager_person_id": str(person.get("id", "")),
        "all_emails": ", ".join(emails),
        "all_phones": ", ".join(phones),
    }
