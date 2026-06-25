"""
test_deepline_offline.py
------------------------
Offline verification of the Deepline Workflow 3 logic against Shirish's spec.
NO API keys, NO credits, NO network, NO HubSpot — we stub the single network
call (deepline.execute_tool) with canned provider responses and assert the code
behaves exactly as specified.

Run:  python test_deepline_offline.py
"""
import os
os.environ["DEEPLINE_API_KEY"] = "dlp_test"  # flip is_enabled() on; no real calls are made

import types
import deepline
import enrichment

PASS, FAIL = 0, 0
def check(label, cond):
    global PASS, FAIL
    print(("  PASS  " if cond else "  FAIL  ") + label)
    PASS += 1 if cond else 0
    FAIL += 0 if cond else 1

def stub(responses_by_tool):
    """Install a fake execute_tool. responses_by_tool maps tool_id -> value or
    callable(payload)->value. Also records how many times each tool was called."""
    calls = {}
    def fake(tool_id, payload, timeout=60):
        calls[tool_id] = calls.get(tool_id, 0) + 1
        r = responses_by_tool.get(tool_id)
        return r(payload) if callable(r) else r
    deepline.execute_tool = fake
    return calls

PERSON = {"first_name": "Pat", "last_name": "Lee", "full_name": "Pat Lee",
          "domain": "acme.com", "linkedin_url": "https://linkedin.com/in/patlee"}

print("\n=== EMAIL WATERFALL (Shirish: tool->ZeroBounce; VALID only; INVALID/CATCH-ALL fail) ===")

# E1: first tool VALID -> accept immediately, record SMTP provider, do NOT call tool 2.
calls = stub({
    "hunter_email_finder": {"email": "a@acme.com"},
    "leadmagic_email_finder": {"email": "should-not-be-used@acme.com"},
    "zerobounce_validate": lambda p: {"status": "valid", "smtp_provider": "Microsoft"},
})
r = deepline.run_email_waterfall(PERSON)
check("first valid email is accepted", r.get("value") == "a@acme.com")
check("SMTP provider recorded", (r.get("meta") or {}).get("smtp_provider") == "Microsoft")
check("stops at provider 1 (provider 2 NOT called)", "leadmagic_email_finder" not in calls)

# E2: tool 1 returns nothing -> tool 2 returns VALID -> accept.
stub({
    "hunter_email_finder": None,
    "leadmagic_email_finder": {"email": "b@acme.com"},
    "zerobounce_validate": lambda p: {"status": "valid", "smtp_provider": "Google"},
})
r = deepline.run_email_waterfall(PERSON)
check("falls through empty provider to next, accepts valid", r.get("value") == "b@acme.com" and r.get("winner") == "leadmagic")

# E3: tool 1 INVALID -> tool 2 VALID.
stub({
    "hunter_email_finder": {"email": "bad@acme.com"},
    "leadmagic_email_finder": {"email": "good@acme.com"},
    "zerobounce_validate": lambda p: {"status": "valid"} if p["email"] == "good@acme.com" else {"status": "invalid"},
})
r = deepline.run_email_waterfall(PERSON)
check("INVALID email rejected, next valid accepted", r.get("value") == "good@acme.com")

# E4: CATCH-ALL must be treated as fail.
stub({
    "hunter_email_finder": {"email": "catch@acme.com"},
    "leadmagic_email_finder": {"email": "good@acme.com"},
    "zerobounce_validate": lambda p: {"status": "valid"} if p["email"] == "good@acme.com" else {"status": "catch-all"},
})
r = deepline.run_email_waterfall(PERSON)
check("CATCH-ALL rejected (only VALID passes)", r.get("value") == "good@acme.com")

# E5: Shirish's exact boundary example — tool1 emailX(fail), tool2 nothing, tool3 emailX again -> STOP, blank,
#     and ZeroBounce is NOT called a second time on the repeat.
calls = stub({
    "hunter_email_finder": {"email": "dupe@acme.com"},
    "leadmagic_email_finder": None,
    "prospeo_enrich_person": {"email": "dupe@acme.com"},   # same failed email from a 2nd provider
    "contactout_enrich_person": {"email": "later@acme.com"},
    "zerobounce_validate": lambda p: {"status": "invalid"},
})
r = deepline.run_email_waterfall(PERSON)
check("boundary: same failed email from 2 providers -> blank output", r == {})
check("boundary: ZeroBounce NOT re-run on the repeated email (1 call only)", calls.get("zerobounce_validate") == 1)
check("boundary: later providers are NOT called (stopped early)", "contactout_enrich_person" not in calls)

# E6: nobody finds anything -> blank.
stub({"zerobounce_validate": lambda p: {"status": "valid"}})
check("no email found anywhere -> blank", deepline.run_email_waterfall(PERSON) == {})

print("\n=== PHONE WATERFALL (Shirish: tool->Trestle; VALID AND activity>=50; record fields) ===")

# P1: valid + high activity -> accept + record all fields.
stub({
    "leadmagic_mobile_finder": {"phone": "+14155550100"},
    "trestle_real_contact": lambda p: {"phone_status": "valid", "activity_score": 82,
                                       "line_type": "Mobile", "country_name": "United States",
                                       "country_calling_code": "+1"},
})
r = deepline.run_phone_waterfall(PERSON)
m = r.get("meta") or {}
check("valid phone w/ activity>=50 accepted", bool(r.get("value")))
check("records activity score", m.get("activity_score") == 82)
check("records line type / country / calling code",
      m.get("line_type") == "Mobile" and m.get("country") == "United States" and m.get("calling_code") == "+1")

# P2: activity < 50 must fail, next provider passes.
stub({
    "leadmagic_mobile_finder": {"phone": "+14155550100"},
    "contactout_enrich_person": {"phone": "+14155550200"},
    "trestle_real_contact": lambda p: {"phone_status": "valid", "activity_score": 30} if "0100" in p["phone"]
                                      else {"phone_status": "valid", "activity_score": 65},
})
r = deepline.run_phone_waterfall(PERSON)
check("activity_score < 50 rejected, next accepted", (r.get("meta") or {}).get("activity_score") == 65)

# P3: boundary — same failed phone from 2 providers -> blank.
stub({
    "leadmagic_mobile_finder": {"phone": "+14155550999"},
    "contactout_enrich_person": {"phone": "+1 415-555-0999"},  # same number, different formatting
    "trestle_real_contact": lambda p: {"phone_status": "invalid"},
})
r = deepline.run_phone_waterfall(PERSON)
check("boundary: same failed phone from 2 providers -> blank", r == {})

print("\n=== WORKFLOW 3 ORCHESTRATION (after WF2; parallel; phone only if none exists; field mapping) ===")

# Mock HubSpot so we can run the full workflow3 offline and inspect what it writes.
written = {}
def mock_get_contact(cid):
    return {"id": cid, "properties": MOCK_PROPS}
def mock_update_contact(cid, props):
    written.update(props)
def mock_find_dupe(pid, exclude_id=None):
    return None
enrichment.hubspot = types.SimpleNamespace(
    get_contact=mock_get_contact, update_contact=mock_update_contact,
    find_deepline_contact_by_person_id=mock_find_dupe, ensure_custom_properties=lambda: None,
)
# Make the waterfalls deterministic without network.
deepline.run_email_waterfall = lambda inp: {"value": "work@acme.com", "meta": {"smtp_provider": "Microsoft"}}
deepline.run_phone_waterfall = lambda inp: {"value": "+14155551234", "meta": {"activity_score": 90, "line_type": "Mobile", "country": "United States", "calling_code": "+1"}}

# W1: contact has NO phone -> phone waterfall runs; work email -> Email; phone -> Phone.
written = {}
MOCK_PROPS = {"firstname": "Pat", "lastname": "Lee", "company_domain": "acme.com", "phone": ""}
deepline.run_phone_waterfall = lambda inp: {"value": "+14155551234", "meta": {"activity_score": 90, "line_type": "Mobile", "country": "United States", "calling_code": "+1"}}
res = enrichment.workflow3_deepline("111")
check("work email written to built-in Email field", written.get("email") == "work@acme.com")
check("SMTP provider written", written.get("email_smtp_provider") == "Microsoft")
check("phone written (no existing phone)", written.get("phone") == "+14155551234")
check("phone metadata written (score/line/country/code)",
      written.get("phone_activity_score") == 90 and written.get("phone_calling_code") == "+1")
check("deepline_enriched flag set", written.get("deepline_enriched") == "true")

# W2: contact ALREADY has a phone -> phone waterfall must NOT run (Deepline = fallback after Forager).
written = {}
MOCK_PROPS = {"firstname": "Pat", "lastname": "Lee", "company_domain": "acme.com", "phone": "+19998887777"}
ran = {"phone": False}
def phone_spy(inp):
    ran["phone"] = True
    return {"value": "x"}
deepline.run_phone_waterfall = phone_spy
enrichment.workflow3_deepline("222")
check("phone waterfall SKIPPED when phone already present", ran["phone"] is False)

# W3: idempotency -> already deepline_enriched -> skip entirely.
written = {}
MOCK_PROPS = {"firstname": "Pat", "deepline_enriched": "true"}
res = enrichment.workflow3_deepline("333")
check("idempotent: already deepline-enriched -> skipped", res.get("status") == "skipped" and written == {})

# W4: dormant -> no key -> no-op.
deepline.DEEPLINE_API_KEY = None
res = enrichment.workflow3_deepline("444")
check("dormant: no key -> skipped", res.get("status") == "skipped")
deepline.DEEPLINE_API_KEY = "dlp_test"

print("\n=== INPUT GUARDS (Shirish: work email needs name+domain; phone needs name) ===")
# Restore the REAL functions (the Workflow-3 section above stubbed them for orchestration tests).
import importlib
importlib.reload(deepline)
check("email waterfall needs a domain", deepline.run_email_waterfall({"first_name": "Pat", "domain": ""}) == {})
check("email waterfall needs a name", deepline.run_email_waterfall({"first_name": "", "domain": "acme.com"}) == {})

print("\n=== COMPANY FUNDING (Deepline) ===")
deepline.execute_tool = lambda t, p, timeout=60: {"total_funding": "$120M", "last_funding_type": "Series C"}
f = deepline.get_company_funding("acme.com", "Acme")
check("funding summary built from provider response", "120M" in (f or "") and "Series C" in (f or ""))

print(f"\n================  RESULT: {PASS} passed, {FAIL} failed  ================")
raise SystemExit(1 if FAIL else 0)
