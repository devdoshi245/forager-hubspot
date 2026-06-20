"""
main.py
-------
Flask webhook + manual-trigger server for the Forager x HubSpot enrichment automation.

Endpoints:
  GET  /                      Service info
  GET  /health                Health check -> {"status": "ok"}
  POST /webhook/company       HubSpot "company created" (body: [{"objectId": ...}])
  POST /webhook/contact       HubSpot "contact created" (body: [{"objectId": ...}])
  POST /enrich/company        Manual: {"company_id": "123"}
  POST /enrich/contact        Manual: {"contact_id": "123"}
  POST /enrich/find-contacts  Manual: {"company_id","company_domain","job_title_filter","max_contacts"}
  POST /enrich/demo           Demo: {"company_id": "123"} -> full company pipeline
"""

import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

load_dotenv()

import enrichment  # noqa: E402  (must import after load_dotenv so env vars are set)
import hubspot     # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Make sure the custom HubSpot fields exist as soon as the server boots, so a
# user can populate (e.g.) linkedin_url on a contact before the first webhook.
try:
    hubspot.ensure_custom_properties()
except Exception as exc:  # noqa: BLE001
    logger.warning("ensure_custom_properties() at startup failed: %s", exc)


@app.errorhandler(Exception)
def handle_uncaught(error):
    """Return clean JSON instead of a 500 HTML page for unhandled errors, and
    surface upstream issues clearly — notably Forager returning HTTP 402 when the
    account is out of credits."""
    if isinstance(error, HTTPException):
        return error  # let Flask render 404/405/etc. normally
    logger.exception("Unhandled error while handling request")
    response = getattr(error, "response", None)
    upstream_status = getattr(response, "status_code", None)
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
        "endpoints": [
            "GET  /health",
            "POST /webhook  (HubSpot single target URL - routes all events)",
            "POST /webhook/company",
            "POST /webhook/contact",
            "POST /enrich/company",
            "POST /enrich/contact",
            "POST /enrich/find-contacts",
            "POST /enrich/demo",
        ],
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/webhook", methods=["POST"])
def webhook():
    """Unified HubSpot webhook endpoint.

    A HubSpot Private App posts EVERY event subscription to a single Target URL,
    so we route each event to the right handler by its subscriptionType
    (e.g. 'company.creation' vs 'contact.creation')."""
    payload = request.get_json(force=True, silent=True) or []
    logger.info("/webhook received %d event(s): %s", len(payload), payload)
    job_title_filter = request.args.get("job_title_filter")
    max_contacts = int(request.args.get("max_contacts", 5))
    results = []
    for event in payload:
        object_id = str(event.get("objectId", ""))
        subscription = (event.get("subscriptionType") or "").lower()
        if not object_id:
            continue
        try:
            if subscription.startswith("company"):
                results.append({"type": "company", "objectId": object_id,
                                "result": enrichment.handle_company_webhook(object_id, job_title_filter, max_contacts)})
            elif subscription.startswith("contact"):
                results.append({"type": "contact", "objectId": object_id,
                                "result": enrichment.handle_contact_webhook(object_id)})
            else:
                results.append({"type": "unknown", "objectId": object_id,
                                "subscriptionType": subscription, "skipped": True})
        except Exception as exc:  # noqa: BLE001 - never fail the batch / trigger HubSpot retries
            logger.exception("Webhook processing failed for %s %s", subscription, object_id)
            results.append({"type": subscription or "unknown", "objectId": object_id, "error": str(exc)})
    # Always 200 so HubSpot doesn't retry a permanent failure (e.g. out of credits).
    return jsonify(results), 200


@app.route("/webhook/company", methods=["POST"])
def webhook_company():
    payload = request.get_json(force=True, silent=True) or []
    logger.info("/webhook/company received: %s", payload)
    job_title_filter = request.args.get("job_title_filter")
    results = []
    for event in payload:
        company_id = str(event.get("objectId", ""))
        if not company_id:
            continue
        results.append(enrichment.handle_company_webhook(company_id, job_title_filter))
    return jsonify(results), 200


@app.route("/webhook/contact", methods=["POST"])
def webhook_contact():
    payload = request.get_json(force=True, silent=True) or []
    logger.info("/webhook/contact received: %s", payload)
    results = []
    for event in payload:
        contact_id = str(event.get("objectId", ""))
        if not contact_id:
            continue
        results.append(enrichment.handle_contact_webhook(contact_id))
    return jsonify(results), 200


@app.route("/enrich/company", methods=["POST"])
def manual_enrich_company():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    if not company_id:
        return jsonify({"error": "company_id required"}), 400
    return jsonify(enrichment.enrich_company(str(company_id))), 200


@app.route("/enrich/contact", methods=["POST"])
def manual_enrich_contact():
    body = request.get_json(force=True, silent=True) or {}
    contact_id = body.get("contact_id")
    if not contact_id:
        return jsonify({"error": "contact_id required"}), 400
    return jsonify(enrichment.enrich_contact(str(contact_id))), 200


@app.route("/enrich/find-contacts", methods=["POST"])
def manual_find_contacts():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    company_domain = body.get("company_domain")
    job_title = body.get("job_title_filter")
    max_contacts = int(body.get("max_contacts", 5))
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
def demo():
    body = request.get_json(force=True, silent=True) or {}
    company_id = body.get("company_id")
    if not company_id:
        return jsonify({"error": "company_id required"}), 400
    job_title_filter = request.args.get("job_title_filter")
    max_contacts = int(request.args.get("max_contacts", body.get("max_contacts", 5)))
    return jsonify(enrichment.handle_company_webhook(str(company_id), job_title_filter, max_contacts)), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
