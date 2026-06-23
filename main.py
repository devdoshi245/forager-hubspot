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
import enrichment   # noqa: E402
import hubspot      # noqa: E402
import scoring      # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

BUILD = "v3.4 (create only missing custom properties - no 409 log noise)"

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
        "alerts_configured": alerts.is_configured(),
        "queue_depth": background.queue_size(),
    }), 200


@app.route("/debug/alert-test", methods=["GET", "POST"])
@require_secret
def alert_test():
    """Send a harmless test alert; returns the ACTUAL SMTP error + non-secret config
    when the send fails, so 'email_sent: false' is self-diagnosing."""
    return jsonify(alerts.test_send()), 200


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
    max_contacts = _int_arg(request.args.get("max_contacts"), 5)
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
    max_contacts = _int_arg(request.args.get("max_contacts"), 5)
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


@app.route("/enrich/find-contacts", methods=["POST"])
@require_secret
def manual_find_contacts():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    company_domain = body.get("company_domain")
    job_title = body.get("job_title_filter")
    max_contacts = _int_arg(body.get("max_contacts"), 5)
    if not company_id or not company_domain:
        return jsonify({"error": "company_id and company_domain required"}), 400
    results = enrichment.find_and_create_contacts(
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
    max_contacts = _int_arg(request.args.get("max_contacts", body.get("max_contacts")), 5)
    # Demo runs the full pipeline synchronously and forces a refresh so you always see results.
    return jsonify(enrichment.handle_company_webhook(
        str(company_id), job_title_filter, max_contacts, force=True)), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
