"""
hubspot.py
----------
All interactions with the HubSpot CRM API (v3 + v4 associations).
Auth: Bearer token (Private App).

Robustness features:
  * ensure_custom_properties() creates the custom text fields Forager fills in
    (founded_year, forager_org_id, linkedin_url, etc.) so writes don't 400 on
    unknown properties. Idempotent — safe to call repeatedly.
  * update_*/create_* stringify values, strip blanks, and on a 400 will drop the
    offending property and retry, so a single bad field (e.g. an "industry"
    value HubSpot's dropdown doesn't recognise) never blocks the whole record.
"""

import json
import logging
import os
import re

import requests

import httpclient

logger = logging.getLogger(__name__)

_SESSION = httpclient.make_session()

HUBSPOT_BASE = "https://api.hubapi.com"
HUBSPOT_TOKEN = os.environ.get("HUBSPOT_TOKEN")

# Custom properties we create on first use: (name, human label[, type]).
# type is "string" (free text, default) or "number".
_COMPANY_CUSTOM_PROPS = [
    ("founded_year", "Founded Year"),
    ("forager_org_id", "Forager Org ID"),
    ("industry_forager", "Industry (Forager)"),
    ("funding", "Funding"),  # filled from Deepline (Phase 2)
    # ICP fit scoring (Claude) — see scoring.py
    ("icp_match_score", "ICP Match Score", "number"),
    ("icp_decision", "ICP Decision"),                       # ICP | MAYBE | REMOVE
    ("icp_confidence", "ICP Confidence", "number"),
    ("icp_reasoning", "ICP Reasoning"),
    ("icp_positives", "ICP Positives"),
    ("icp_negatives", "ICP Negatives"),
    ("icp_red_flags", "ICP Red Flags"),
    ("icp_best_fit_use_case", "ICP Best-Fit Use Case"),
    ("icp_suggested_next_step", "ICP Suggested Next Step"),
    # Logo recognizability (Claude + web search) — see scoring.py
    ("logo_score", "Logo Recognizability Score", "number"),
    ("logo_tier", "Logo Tier"),                             # T1 | T2 | T3
    ("logo_confidence", "Logo Confidence", "number"),
    ("logo_why", "Logo Why"),
    ("logo_forager_fit", "Logo Forager Fit"),               # HIGH | MEDIUM | LOW
    ("logo_forager_fit_reason", "Logo Forager Fit Reason"),
    ("logo_evidence", "Logo Evidence"),
]
_CONTACT_CUSTOM_PROPS = [
    ("email_home", "Email Home"),
    ("linkedin_url", "LinkedIn Profile URL"),
    ("company_domain", "Company Domain"),
    ("company_linkedin_url", "Company LinkedIn URL"),
    ("person_description", "Person Description"),
    ("person_headline", "Person Headline"),
    ("person_skills", "Person Skills"),
    ("forager_person_id", "Forager Person ID"),
    ("all_emails", "All Emails"),
    ("all_phones", "All Phones"),
]

_COMPANY_PROPS_TO_READ = (
    "name,domain,description,linkedin_company_page,numberofemployees,"
    "annualrevenue,founded_year,city,state,country,industry,industry_forager,funding,website,forager_org_id,"
    "icp_match_score"
)
_CONTACT_PROPS_TO_READ = (
    "firstname,lastname,email,email_home,phone,jobtitle,city,state,country,"
    "linkedin_url,hs_linkedin_url,linkedin_profile,"
    "company,company_domain,company_linkedin_url,all_emails,all_phones,forager_person_id"
)

_ensured = False


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {HUBSPOT_TOKEN}",
        "Content-Type": "application/json",
    }


def _clean(properties: dict) -> dict:
    """Drop None/empty values and stringify the rest (HubSpot wants strings)."""
    clean = {}
    for key, value in properties.items():
        if value in (None, "", []):
            continue
        clean[key] = value if isinstance(value, str) else str(value)
    return clean


def _invalid_property_names(error_json: dict, candidates: dict) -> list[str]:
    """Which of our properties did HubSpot reject?

    HubSpot embeds per-property errors as a JSON-ish string inside the top-level
    "message", e.g.  ..."name":"industry"...  — so we extract the *values* of
    those "name" keys (plus any  Property "x"  / properties.x  mentions), never
    the literal key text (which would false-match a property called 'name')."""
    texts: list[str] = []
    if isinstance(error_json, dict):
        if error_json.get("message"):
            texts.append(str(error_json["message"]))
        for err in error_json.get("errors") or []:
            if isinstance(err, dict):
                if err.get("message"):
                    texts.append(str(err["message"]))
                for key in ("name", "in", "propertyName"):
                    if err.get(key):
                        texts.append(f'"name":"{err[key]}"')
    text = " ".join(texts)
    flagged: set[str] = set()
    for pattern in (r'"name"\s*:\s*"([^"]+)"', r'[Pp]roperty\s+"([^"]+)"', r'properties\.([A-Za-z0-9_]+)'):
        flagged.update(re.findall(pattern, text))
    return [c for c in candidates if c in flagged]


def _write_with_retry(method: str, url: str, properties: dict) -> dict:
    """PATCH/POST properties, dropping any property HubSpot rejects, then retry."""
    clean = _clean(properties)
    func = getattr(_SESSION, method)
    for _ in range(len(clean) + 1):
        resp = func(url, json={"properties": clean}, headers=_headers(), timeout=30)
        if resp.status_code == 400 and clean:
            offending = _invalid_property_names(resp.json() if resp.content else {}, clean)
            if offending:
                for name in offending:
                    clean.pop(name, None)
                logger.warning("HubSpot rejected properties %s; retrying without them", offending)
                if clean:
                    continue
        resp.raise_for_status()
        return resp.json()
    return {}


# ---------------------------------------------------------------------------
# Custom property bootstrapping
# ---------------------------------------------------------------------------
def ensure_custom_properties() -> None:
    """Create the custom text properties we depend on (idempotent)."""
    global _ensured
    if _ensured:
        return
    _create_properties("companies", "companyinformation", _COMPANY_CUSTOM_PROPS)
    _create_properties("contacts", "contactinformation", _CONTACT_CUSTOM_PROPS)
    _ensured = True


def _existing_property_names(object_type: str) -> set[str]:
    """Names of properties that already exist on this object, so we create only the
    missing ones — this avoids the noisy (harmless) 409 'already exists' calls."""
    try:
        resp = _SESSION.get(
            f"{HUBSPOT_BASE}/crm/v3/properties/{object_type}",
            headers=_headers(), timeout=30,
        )
        resp.raise_for_status()
        return {p.get("name") for p in resp.json().get("results", []) if p.get("name")}
    except Exception as exc:  # noqa: BLE001 - fall back to create-and-tolerate-409
        logger.warning("Could not list %s properties: %s", object_type, exc)
        return set()


def _create_properties(object_type: str, group: str, props: list[tuple]) -> None:
    existing = _existing_property_names(object_type)
    for entry in props:
        name, label = entry[0], entry[1]
        if name in existing:
            continue  # already present — skip the POST (no 409)
        prop_type = entry[2] if len(entry) > 2 else "string"
        field_type = "number" if prop_type == "number" else "text"
        body = {
            "name": name,
            "label": label,
            "type": prop_type,
            "fieldType": field_type,
            "groupName": group,
        }
        try:
            resp = _SESSION.post(
                f"{HUBSPOT_BASE}/crm/v3/properties/{object_type}",
                json=body, headers=_headers(), timeout=30,
            )
            if resp.status_code in (200, 201):
                logger.info("Created %s property '%s'", object_type, name)
            elif resp.status_code == 409:
                pass  # already exists (created between our list call and this POST)
            else:
                logger.warning(
                    "Create property %s/%s -> %s: %s",
                    object_type, name, resp.status_code, resp.text[:200],
                )
        except Exception as exc:  # noqa: BLE001
            logger.warning("Create property %s/%s failed: %s", object_type, name, exc)


# ---------------------------------------------------------------------------
# Companies
# ---------------------------------------------------------------------------
def get_company(company_id: str) -> dict | None:
    resp = _SESSION.get(
        f"{HUBSPOT_BASE}/crm/v3/objects/companies/{company_id}",
        headers=_headers(), params={"properties": _COMPANY_PROPS_TO_READ}, timeout=30,
    )
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def find_company_by_domain(domain: str) -> dict | None:
    body = {
        "filterGroups": [{"filters": [{"propertyName": "domain", "operator": "EQ", "value": domain}]}],
        "properties": ["name", "domain"],
        "limit": 1,
    }
    resp = _SESSION.post(
        f"{HUBSPOT_BASE}/crm/v3/objects/companies/search", json=body, headers=_headers(), timeout=30,
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return results[0] if results else None


def update_company(company_id: str, properties: dict) -> dict:
    return _write_with_retry("patch", f"{HUBSPOT_BASE}/crm/v3/objects/companies/{company_id}", properties)


def create_company(properties: dict) -> dict:
    return _write_with_retry("post", f"{HUBSPOT_BASE}/crm/v3/objects/companies", properties)


def get_contacts_for_company(company_id: str) -> list[dict]:
    """Return full contact records associated with a company (via v4 associations)."""
    resp = _SESSION.get(
        f"{HUBSPOT_BASE}/crm/v4/objects/companies/{company_id}/associations/contacts",
        headers=_headers(), timeout=30,
    )
    resp.raise_for_status()
    refs = resp.json().get("results", [])
    contacts = []
    for ref in refs:
        contact_id = str(ref.get("toObjectId") or ref.get("id") or "")
        if not contact_id:
            continue
        contact = get_contact(contact_id)
        if contact:
            contacts.append(contact)
    return contacts


# ---------------------------------------------------------------------------
# Contacts
# ---------------------------------------------------------------------------
def get_contact(contact_id: str) -> dict | None:
    resp = _SESSION.get(
        f"{HUBSPOT_BASE}/crm/v3/objects/contacts/{contact_id}",
        headers=_headers(), params={"properties": _CONTACT_PROPS_TO_READ}, timeout=30,
    )
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def find_contact_by_email(email: str) -> dict | None:
    body = {
        "filterGroups": [{"filters": [{"propertyName": "email", "operator": "EQ", "value": email}]}],
        "properties": ["firstname", "lastname", "email"],
        "limit": 1,
    }
    resp = _SESSION.post(
        f"{HUBSPOT_BASE}/crm/v3/objects/contacts/search", json=body, headers=_headers(), timeout=30,
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return results[0] if results else None


def find_contact_by_email_home(email: str) -> dict | None:
    """Dedup lookup on our custom Email Home property. The built-in email field is
    left empty on purpose, so HubSpot's native email uniqueness can't be relied on."""
    if not email:
        return None
    body = {
        "filterGroups": [{"filters": [{"propertyName": "email_home", "operator": "EQ", "value": email}]}],
        "properties": ["firstname", "lastname", "email_home"],
        "limit": 1,
    }
    resp = _SESSION.post(
        f"{HUBSPOT_BASE}/crm/v3/objects/contacts/search", json=body, headers=_headers(), timeout=30,
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return results[0] if results else None


def update_contact(contact_id: str, properties: dict) -> dict:
    return _write_with_retry("patch", f"{HUBSPOT_BASE}/crm/v3/objects/contacts/{contact_id}", properties)


def create_contact(properties: dict) -> dict:
    return _write_with_retry("post", f"{HUBSPOT_BASE}/crm/v3/objects/contacts", properties)


# ---------------------------------------------------------------------------
# Associations (v4 default association)
# ---------------------------------------------------------------------------
def associate_contact_to_company(contact_id: str, company_id: str) -> None:
    resp = _SESSION.put(
        f"{HUBSPOT_BASE}/crm/v4/objects/contacts/{contact_id}/associations/default/companies/{company_id}",
        headers=_headers(), timeout=30,
    )
    resp.raise_for_status()
