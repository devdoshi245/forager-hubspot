"""
main.py
-------
Flask webhook + manual-trigger server for the Forager x HubSpot enrichment automation.

Webhook events are authenticated, ACKed immediately, and processed on a background
worker — so a slow enrichment (the LLM logo web-search can take tens of seconds) can't
trip HubSpot's delivery timeout and trigger retries / double Forager-credit spend. The
manual /enrich/* endpoints run synchronously and return the result to the caller.

Sensitive endpoints (webhooks, /enrich/*, /debug/*) require APP_SECRET when it is set
(send it as header `X-App-Secret` or query `?token=`). `/` and `/health` stay public.

Endpoints:
  GET  /                       Service info / build
  GET  /health                 Health check + queue depth
  GET  /debug/config           Which integrations are configured (no secrets)   [auth]
  GET/POST /debug/alert-test    Send a test error email                          [auth]
  POST /webhook                 HubSpot single Target URL (routes all events)    [auth]
  POST /webhook/company         Company-created handler                          [auth]
  POST /webhook/contact         Contact-created handler                          [auth]
  POST /enrich/company          Manual {"company_id"} (forces a refresh)         [auth]
  POST /enrich/contact          Manual {"contact_id"}                            [auth]
  POST /enrich/find-contacts    Manual {"company_id","company_domain",...}       [auth]
  POST /enrich/demo             Full company pipeline {"company_id"}             [auth]
"""

import logging
import os
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

load_dotenv()

import alerts       # noqa: E402  (import after load_dotenv so env vars are set)
import auth         # noqa: E402
import background   # noqa: E402
import deepline     # noqa: E402
import enrichment   # noqa: E402
import forager      # noqa: E402
import hubspot      # noqa: E402
import scoring      # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

BUILD = "v3.40 (Email extraction now PREFERS the target-company email when a provider returns several — ContactOut returned [jsconf.eu, vercel.com] and we were grabbing jsconf (first) and rejecting it, throwing away the usable vercel.com address; now we pick the domain-matching one. +?raw=1 on the test endpoints surfaces each provider's full JSON, to verify extraction picks the RIGHT value (e.g. the target-domain email when a tool returns several). +/debug/email-tools + /debug/phone-tools: run EACH tool's real adapter through real extraction + validation, no first-success stop, no HubSpot write, ?tools= filter to test only specific tools. Upcell payload fixed to FLAT camelCase top-level fields (the `contact` nesting was wrong; live 422 confirmed it wants linkedinUrl/firstName/lastName/companyDomain/email flat). +/debug/phone-waterfall: runs the full region-aware phone waterfall + Trestle for a person without writing to HubSpot or skipping when a phone exists — lets us confirm the phone tools even when Forager always supplies a phone. Fixed the phone-provider adapters that returned nothing: Upcell now nests identity in a `contact` object (was flat -> empty); Wiza requests enrichment_level=full to actually return phones (DEEPLINE_WIZA_LEVEL); phone extractor now prefers INTERNATIONAL/E.164 format so a bare national number (Datagma's 1718659901) keeps its +country code (+491718659901); +Wiza phone_number1/mobile_phone1 keys. Findymail/Datagma confirmed working (needed the LinkedIn URL). + full per-provider logging + extractor hardening + domain guard + seeded 422 + Trestle/ZeroBounce verdict fixes. Tier 1/2; funding via Crustdata; region-aware phone waterfalls. Deepline dormant unless DEEPLINE_API_KEY)"

_REQUIRED_ENV = ("FORAGER_API_KEY", "FORAGER_ACCOUNT_ID", "HUBSPOT_TOKEN")


def _missing_required_env() -> list:
    return [name for name in _REQUIRED_ENV if not os.environ.get(name)]


# Fail LOUD at startup if the must-have credentials are absent (instead of a silent
# 500 on the first request). The service still boots so /health and /debug/config work.
_missing = _missing_required_env()
if _missing:
    logger.critical("MISSING REQUIRED ENV VARS: %s — enrichment will fail until these are set.",
                    ", ".join(_missing))
if not auth.is_enabled():
    logger.warning("APP_SECRET is not set — sensitive endpoints are OPEN. Set it before going live.")

app = Flask(__name__)

# Create custom HubSpot properties up front, and start the background worker that
# drains the webhook queue.
try:
    hubspot.ensure_custom_properties()
except Exception as exc:  # noqa: BLE001
    logger.warning("ensure_custom_properties() at startup failed: %s", exc)
background.start_worker()


def require_secret(fn):
    """Gate a sensitive endpoint behind the shared secret (enforced only when
    APP_SECRET is configured — see auth.py)."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not auth.authorize(request):
            return jsonify({"error": "unauthorized"}), 401
        return fn(*args, **kwargs)
    return wrapper


def _int_arg(value, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


@app.errorhandler(Exception)
def handle_uncaught(error):
    """Return clean JSON instead of a 500 HTML page for unhandled errors, and surface
    upstream issues clearly — notably Forager returning HTTP 402 (out of credits)."""
    if isinstance(error, HTTPException):
        return error  # let Flask render 404/405/etc. normally
    logger.exception("Unhandled error while handling request")
    response = getattr(error, "response", None)
    upstream_status = getattr(response, "status_code", None)
    summary = ("Forager out of credits" if upstream_status == 402
               else f"Unhandled error on {request.method} {request.path}")
    alerts.send_error_alert(summary, error=error,
                            context={"method": request.method, "path": request.path,
                                     "upstream_status": upstream_status})
    if upstream_status == 402:
        return jsonify({
            "error": "forager_out_of_credits",
            "message": "Forager reports insufficient credits. Add credits in the Forager dashboard, then retry.",
        }), 402
    if upstream_status is not None:
        return jsonify({"error": "upstream_error", "upstream_status": upstream_status,
                        "message": str(error)}), 502
    return jsonify({"error": "internal_error", "message": str(error)}), 500


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "Forager x HubSpot Enrichment Automation",
        "status": "running",
        "build": BUILD,
        "auth_enabled": auth.is_enabled(),
        "endpoints": [
            "GET  /health",
            "GET  /debug/config          [auth]",
            "GET/POST /debug/alert-test  [auth]",
            "POST /webhook               [auth]  (HubSpot single Target URL)",
            "POST /webhook/company       [auth]",
            "POST /webhook/contact       [auth]",
            "POST /enrich/company        [auth]",
            "POST /enrich/contact        [auth]",
            "POST /enrich/find-contacts  [auth]",
            "POST /enrich/demo           [auth]",
        ],
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "queue_depth": background.queue_size()}), 200


@app.route("/debug/config", methods=["GET"])
@require_secret
def debug_config():
    """Readiness check — what's configured, without secrets and without spending any
    Forager credits. Useful to confirm you're ready before creating a company."""
    return jsonify({
        "build": BUILD,
        "required_env_ok": not _missing_required_env(),
        "missing_required_env": _missing_required_env(),
        "auth_enabled": auth.is_enabled(),
        "scoring_provider": scoring.provider(),   # "gemini" | "anthropic" | null
        "deepline_enabled": deepline.is_enabled(),
        "alerts_configured": alerts.is_configured(),
        "queue_depth": background.queue_size(),
    }), 200


@app.route("/debug/alert-test", methods=["GET", "POST"])
@require_secret
def alert_test():
    """Send a harmless test alert; returns the ACTUAL SMTP error + non-secret config
    when the send fails, so 'email_sent: false' is self-diagnosing."""
    return jsonify(alerts.test_send()), 200


@app.route("/debug/score-test", methods=["GET", "POST"])
@require_secret
def score_test():
    """Fast Claude key/health check: runs ONLY the ICP prompt (no web search), so it
    returns in a few seconds. A 401 here means a bad key; real JSON means the key
    works. The logo step is skipped on purpose — its live web search is too slow for
    a synchronous request, but runs fine on the background worker during real
    enrichment. No Forager credits (LLM account only)."""
    sample = {
        "name": "Stripe", "domain": "stripe.com",
        "description": "Payments infrastructure and financial APIs for internet businesses.",
        "industry": "Financial Services", "numberofemployees": 8000,
    }
    return jsonify(scoring.icp_only(sample)), 200


@app.route("/debug/owners", methods=["GET"])
@require_secret
def debug_owners():
    """List HubSpot owners (id, email, name) and show what CONTACT_OWNER resolves to —
    use it to find/verify the value for the auto-created Contact Owner."""
    return jsonify({
        "configured_contact_owner": hubspot.CONTACT_OWNER,
        "resolved_owner_id": hubspot.auto_create_owner_id(),
        "owners": hubspot.list_owners(),
    }), 200


@app.route("/debug/person-test", methods=["GET", "POST"])
@require_secret
def person_test():
    """Diagnostic: does Forager return a person's full profile from a LinkedIn handle
    ALONE (no company)? Pass ?slug=<linkedin-handle>. It's a search, not a reveal, so
    ~0 Forager credits. 'found': true with a title/company means the LinkedIn-only
    full-profile path works."""
    slug = request.args.get("slug") or "ankurbansal177"
    return jsonify(forager.probe_person_by_linkedin(slug)), 200


@app.route("/debug/company-test", methods=["GET", "POST"])
@require_secret
def company_test():
    """Diagnostic: for ?company=&first=&last=, report whether the company name resolves
    to a domain and whether the person is findable by name. A search, ~0 credits."""
    company = request.args.get("company") or "Apollo.io"
    first = request.args.get("first") or "Ankur"
    last = request.args.get("last") or "Bansal"
    return jsonify(forager.probe_company_person(company, first, last)), 200


# ---------------------------------------------------------------------------
# Webhooks: authenticate, enqueue, ACK 200 immediately. The slow pipeline runs
# on the background worker (background.py) so HubSpot never waits / retries.
# ---------------------------------------------------------------------------
def _process_company_event(object_id: str, job_title_filter, max_contacts: int) -> None:
    try:
        enrichment.handle_company_webhook(object_id, job_title_filter, max_contacts)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Background company enrichment failed for %s", object_id)
        alerts.send_error_alert(f"Company enrichment failed: {object_id}", error=exc,
                                context={"objectId": object_id, "type": "company"})


def _process_contact_event(object_id: str) -> None:
    try:
        enrichment.handle_contact_webhook(object_id)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Background contact enrichment failed for %s", object_id)
        alerts.send_error_alert(f"Contact enrichment failed: {object_id}", error=exc,
                                context={"objectId": object_id, "type": "contact"})


@app.route("/webhook", methods=["POST"])
@require_secret
def webhook():
    """Unified HubSpot webhook Target URL — routes company + contact events by their
    subscriptionType. Authenticated, enqueued, ACKed immediately."""
    payload = request.get_json(force=True, silent=True) or []
    logger.info("/webhook received %d event(s)", len(payload))
    job_title_filter = request.args.get("job_title_filter")
    max_contacts = _int_arg(request.args.get("max_contacts"), 10)
    accepted = 0
    for event in payload:
        object_id = str(event.get("objectId", ""))
        subscription = (event.get("subscriptionType") or "").lower()
        if not object_id:
            continue
        if subscription.startswith("company"):
            background.enqueue(_process_company_event, object_id, job_title_filter, max_contacts)
            accepted += 1
        elif subscription.startswith("contact"):
            background.enqueue(_process_contact_event, object_id)
            accepted += 1
        else:
            logger.info("/webhook ignoring event with subscriptionType=%r", subscription)
    return jsonify({"accepted": accepted, "queue_depth": background.queue_size()}), 200


@app.route("/webhook/company", methods=["POST"])
@require_secret
def webhook_company():
    payload = request.get_json(force=True, silent=True) or []
    logger.info("/webhook/company received %d event(s)", len(payload))
    job_title_filter = request.args.get("job_title_filter")
    max_contacts = _int_arg(request.args.get("max_contacts"), 10)
    accepted = 0
    for event in payload:
        company_id = str(event.get("objectId", ""))
        if not company_id:
            continue
        background.enqueue(_process_company_event, company_id, job_title_filter, max_contacts)
        accepted += 1
    return jsonify({"accepted": accepted, "queue_depth": background.queue_size()}), 200


@app.route("/webhook/contact", methods=["POST"])
@require_secret
def webhook_contact():
    payload = request.get_json(force=True, silent=True) or []
    logger.info("/webhook/contact received %d event(s)", len(payload))
    accepted = 0
    for event in payload:
        contact_id = str(event.get("objectId", ""))
        if not contact_id:
            continue
        background.enqueue(_process_contact_event, contact_id)
        accepted += 1
    return jsonify({"accepted": accepted, "queue_depth": background.queue_size()}), 200


# ---------------------------------------------------------------------------
# Manual triggers: synchronous — the caller wants the result inline.
# ---------------------------------------------------------------------------
@app.route("/enrich/company", methods=["POST"])
@require_secret
def manual_enrich_company():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    if not company_id:
        return jsonify({"error": "company_id required"}), 400
    # Manual trigger forces a refresh even if already enriched.
    return jsonify(enrichment.enrich_company(str(company_id), force=True)), 200


@app.route("/enrich/contact", methods=["POST"])
@require_secret
def manual_enrich_contact():
    body = request.get_json(force=True, silent=True) or {}
    contact_id = body.get("contact_id")
    if not contact_id:
        return jsonify({"error": "contact_id required"}), 400
    return jsonify(enrichment.enrich_contact(str(contact_id))), 200


@app.route("/enrich/deepline", methods=["POST"])
@require_secret
def manual_deepline():
    """Manually run Workflow 3 (Deepline) on one contact — for controlled testing
    once the Deepline key + credits are in place. {"contact_id": "123"}."""
    body = request.get_json(force=True, silent=True) or {}
    contact_id = body.get("contact_id")
    if not contact_id:
        return jsonify({"error": "contact_id required"}), 400
    return jsonify(enrichment.workflow3_deepline(str(contact_id))), 200


@app.route("/debug/deepline", methods=["GET", "POST"])
@require_secret
def debug_deepline():
    """Dormant-safe Deepline check: confirms the key is set and (optionally) runs one
    tool. Pass ?tool=zerobounce_validate&email=test@stripe.com to probe a single tool.
    Spends provider credits only if you pass a tool to run."""
    out = {"deepline_enabled": deepline.is_enabled()}
    tool = request.args.get("tool")
    if tool and deepline.is_enabled():
        payload = {k: v for k, v in request.args.items() if k != "tool" and k != "token"}
        out["tool"] = tool
        out["result"] = deepline.execute_tool(tool, payload)
    return jsonify(out), 200


@app.route("/debug/phone-waterfall", methods=["GET", "POST"])
@require_secret
def debug_phone_waterfall():
    """Run the FULL region-aware phone waterfall for a person — every provider in order
    + Trestle name-match — WITHOUT writing to HubSpot and WITHOUT the 'already has a
    phone' skip. Lets us confirm the phone tools end-to-end even when Forager always
    supplies a phone. The full per-provider trail prints to the logs.
    Example: ?first_name=Malte&last_name=Ubl&domain=vercel.com&country=United States
             &linkedin_url=https://www.linkedin.com/in/malteubl&email=malte@vercel.com
    Spends provider credits (it actually runs the waterfall)."""
    inp = _person_inp({**(request.get_json(silent=True) or {}), **request.args.to_dict()})
    result = deepline.run_phone_waterfall(inp) if deepline.is_enabled() else {}
    return jsonify({"deepline_enabled": deepline.is_enabled(), "input": inp, "result": result}), 200


def _person_inp(a: dict) -> dict:
    """Build the enrichment input dict from request args (shared by the debug endpoints)."""
    first, last = a.get("first_name", ""), a.get("last_name", "")
    return {
        "first_name": first, "last_name": last,
        "full_name": a.get("full_name") or f"{first} {last}".strip(),
        "domain": forager.normalize_domain(a.get("domain", "")),
        "company_name": a.get("company_name", ""),
        "linkedin_url": a.get("linkedin_url", ""),
        "email": a.get("email", ""),
        "country": a.get("country", ""),
    }


def _only_tools(a: dict):
    """Optional ?tools=a,b,c filter — limits which tools run (to save credits)."""
    raw = (a.get("tools") or "").strip()
    return [t.strip() for t in raw.split(",") if t.strip()] or None


@app.route("/debug/email-tools", methods=["GET", "POST"])
@require_secret
def debug_email_tools():
    """Run EACH email tool's real adapter (with its correct reveal flags) through the
    real extraction + ZeroBounce + domain check — without stopping at the first success
    and without writing to HubSpot. Confirms every tool individually. Use ?tools=a,b to
    test only specific tools (saves credits). Spends provider credits.
    Example: ?first_name=Malte&last_name=Ubl&domain=vercel.com
             &linkedin_url=https://www.linkedin.com/in/malteubl&tools=contactout,crustdata"""
    a = {**(request.get_json(silent=True) or {}), **request.args.to_dict()}
    inp = _person_inp(a)
    raw = str(a.get("raw", "")).lower() in ("1", "true", "yes", "on")
    return jsonify({"deepline_enabled": deepline.is_enabled(), "input": inp,
                    "tools": deepline.test_email_tools(inp, _only_tools(a), include_raw=raw)}), 200


@app.route("/debug/phone-tools", methods=["GET", "POST"])
@require_secret
def debug_phone_tools():
    """Run EACH phone tool's real adapter (with its correct reveal flags) through real
    extraction + Trestle (region-based) — without stopping at the first success and
    without writing to HubSpot. Use ?tools=a,b to test only specific tools (saves
    credits). Spends provider credits.
    Example: ?first_name=Malte&last_name=Ubl&domain=vercel.com&country=United States
             &linkedin_url=https://www.linkedin.com/in/malteubl&email=malte@vercel.com
             &tools=wiza,prospeo,contactout,upcell,findymail"""
    a = {**(request.get_json(silent=True) or {}), **request.args.to_dict()}
    inp = _person_inp(a)
    raw = str(a.get("raw", "")).lower() in ("1", "true", "yes", "on")
    return jsonify({"deepline_enabled": deepline.is_enabled(), "input": inp,
                    "phone": deepline.test_phone_tools(inp, _only_tools(a), include_raw=raw)}), 200


@app.route("/enrich/find-contacts", methods=["POST"])
@require_secret
def manual_find_contacts():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    company_domain = body.get("company_domain")
    job_title = body.get("job_title_filter")
    max_contacts = _int_arg(body.get("max_contacts"), 10)
    if not company_id or not company_domain:
        return jsonify({"error": "company_id and company_domain required"}), 400
    results = enrichment.discover_and_create_contacts(
        hubspot_company_id=str(company_id),
        company_domain=company_domain,
        job_title_filter=job_title,
        max_contacts=max_contacts,
    )
    return jsonify(results), 200


@app.route("/enrich/demo", methods=["POST"])
@require_secret
def demo():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    if not company_id:
        return jsonify({"error": "company_id required"}), 400
    job_title_filter = request.args.get("job_title_filter")
    max_contacts = _int_arg(request.args.get("max_contacts", body.get("max_contacts")), 10)
    # Demo runs the full pipeline synchronously and forces a refresh so you always see results.
    return jsonify(enrichment.handle_company_webhook(
        str(company_id), job_title_filter, max_contacts, force=True)), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
