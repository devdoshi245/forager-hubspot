"""
scoring.py
----------
Claude-powered company scoring used in the company pipeline (diagram: "ICP fit
scoring" + "Logo recognizability", parallel to Forager enrichment):

  1. ICP fit scoring      - is this company a good fit for Forager.ai? (text only)
  2. Logo recognizability - how known is the brand in its B2B category? (web search)

Both call the Claude API (Anthropic). The exact scoring prompts are product-owned
and live verbatim in _ICP_SYSTEM / _LOGO_SYSTEM below. Each returns strict JSON,
which we flatten into HubSpot company properties.

Configuration (env):
  ANTHROPIC_API_KEY   required to enable scoring. If unset (or the `anthropic`
                      package is missing) scoring is skipped gracefully and
                      company enrichment still runs.
  ANTHROPIC_MODEL     optional; defaults to claude-opus-4-8.

Web search incurs Anthropic web-search usage (billed to the Anthropic account),
not Forager credits.
"""

import json
import logging
import os
import re

logger = logging.getLogger(__name__)

_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")
# Server-side web search tool (Claude runs the searches; results never touch our code).
_WEB_SEARCH_TOOL = {"type": "web_search_20260209", "name": "web_search", "max_uses": 5}

# ---------------------------------------------------------------------------
# Product-owned scoring prompts (verbatim). Model must return ONLY JSON.
# ---------------------------------------------------------------------------
_ICP_SYSTEM = """Return ONLY valid JSON. No prose. No markdown. No code fences.

You are scoring ICP fit for Forager.ai.

Forager.ai provides: LinkedIn people + company profile data + verified contact details (mobile numbers, personal emails, business emails). Delivered via API and datasets/feeds. ICP = platforms where data is core to their product: enrichment/waterfalls, GTM tools, AI SDRs, CRMs/dialers, sales engagement, ABM/intent/data platforms, recruiting platforms that enrich candidates, data vendors that resell/serve datasets. ATS is generally considered a strong fit. The best fits is where people/company/contact details are core to platform functionality itself, However where people/company/contact details could greatly improve the product's offering (for example: automatically updating a person's information when added to a CRM... a CRM core functionality is not people/company data yet people/company data can greatly improve the CRM's value) We should also consider such products a reasonably strong fit for Forager's data.

Input fields:
product_name:
g2_description:
forager_description:
company_keywords(optional, may be blank):
g2_categories:
employee_range:
employee_count:
Evidence rule:
If company_keywords is blank, do NOT skip. Use g2_description + forager_description + g2_categories to score.


Score rules:
- 0-10 match_score
- Favor products that: enrich contacts, provide data/APIs, prospecting/list building, AI SDR/outreach automation needing contact data, CRMs/dialers needing mobile numbers, data platforms selling/embedding data.
- Penalize products that are: internal-only HR/payroll, generic project management, design tools, unrelated vertical software, pure services/agency, non-data core products.
- If unclear, score mid (4-6) and lower confidence.
- If product is a GTM platform, outbound platform, dialer, sales engagement, lead generation, sales intelligence, recruiting platform, or any tool that could embed enrichment, do not score below 4 unless evidence clearly shows it is unrelated.
Missing data rule:
If g2_description and forager_description are both empty (or combined length < 20), output:
 match_score=4, decision="MAYBE", confidence=10,
 reasoning_short="Missing descriptions; needs research.",
 positives=[], negatives=[], red_flags=["Missing descriptions"],
 best_fit_use_case="other", suggested_next_step="research_needed".


Output JSON schema:
{
 "match_score": <integer 0-10>,
 "decision": "<ICP|MAYBE|REMOVE>",
 "confidence": <integer 0-100>,
 "reasoning_short": "<max 220 chars>",
 "positives": ["<bullet 1>", "<bullet 2>", "<bullet 3>"],
 "negatives": ["<bullet 1>", "<bullet 2>", "<bullet 3>"],
 "red_flags": ["<bullet 1>", "<bullet 2>"],
 "best_fit_use_case": "<one of: waterfall_enrichment | contact_data_provider | sales_engagement_or_dialer | ai_sdr_outreach | abm_intent_data | recruiting_enrichment | other>",
 "suggested_next_step": "<one of: prioritize_outreach | research_needed | deprioritize>"
}

Decisions:
- ICP: match_score 7-10
- MAYBE: match_score 4-6
- REMOVE: match_score 0-3"""

_LOGO_SYSTEM = """Return ONLY valid JSON. No prose. No markdown. No code fences.

Task:
Use web search to (1) score company recognizability (B2B ecosystem, not consumers) and (2) rate Forager.ai ICP fit.

Forager ICP reminder:
Platforms where data is core to the product and they embed people/company data + contact enrichment (mobile, personal/business emails) via API/feed: enrichment/waterfall, prospecting/sales intelligence, AI SDR/outbound automation, dialers, ABM/intent, recruiting enrichment, data resellers.

Recognizability scale:
1 unknown/low footprint
5 real company, moderate footprint
8 widely known in its B2B category
10 category-defining B2B platform brand

Rules:
- Include >=2 evidence items (URLs). If you cannot find them: logo_score=4, tier_recommendation="T3", confidence=20, forager_fit="MEDIUM", forager_fit_reason="Insufficient public footprint to confirm."
- If official domain is parked/for sale/inactive: logo_score=1, tier_recommendation="T3", confidence=90, forager_fit="LOW", forager_fit_reason="Inactive/parked domain."
Tier mapping (logo only):
T1 if logo_score >= 8
T2 if logo_score 6-7
T3 if logo_score <= 5

Output JSON (always include all keys):
{
 "logo_score": <integer 1-10>,
 "tier_recommendation": "<T1|T2|T3>",
 "confidence": <integer 0-100>,
 "why": "<max 160 chars; include 1 clause on why it may/may not want Forager data>",
 "forager_fit": "<HIGH|MEDIUM|LOW>",
 "forager_fit_reason": "<max 160 chars>",
 "evidence": [
  {"source":"official_site|wikipedia|linkedin|g2|crunchbase|press","url":"<url>","note":"<max 60 chars>"},
  {"source":"...","url":"...","note":"..."}
 ]
}
Input:
company_name:"""


def _client():
    """Return an Anthropic client, or None if scoring is not configured."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic
    except ImportError:
        logger.warning("`anthropic` package not installed; company scoring disabled")
        return None
    return anthropic.Anthropic()


def _response_text(response) -> str:
    """Concatenate the text content blocks of a Messages API response."""
    parts = []
    for block in getattr(response, "content", []) or []:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)
    return "".join(parts)


def _extract_json(text: str | None) -> dict | None:
    """Parse the model's JSON output, tolerating stray code fences / surrounding prose."""
    if not text:
        return None
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```[a-zA-Z]*\n?", "", cleaned)
        cleaned = re.sub(r"\n?```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except (ValueError, TypeError):
        pass
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)  # first/widest JSON object
    if match:
        try:
            return json.loads(match.group(0))
        except (ValueError, TypeError):
            return None
    return None


def _employee_range(count) -> str:
    """Map a headcount to a coarse band for the ICP prompt's employee_range field."""
    try:
        n = int(count)
    except (TypeError, ValueError):
        return ""
    bands = [
        (10, "1-10"), (50, "11-50"), (200, "51-200"), (500, "201-500"),
        (1000, "501-1000"), (5000, "1001-5000"), (10000, "5001-10000"),
    ]
    for ceiling, label in bands:
        if n <= ceiling:
            return label
    return "10000+"


def _score_icp(client, fields: dict) -> dict | None:
    count = fields.get("numberofemployees")
    user = "\n".join([
        f"product_name: {fields.get('name', '') or ''}",
        "g2_description: ",  # no G2 integration; forager_description carries the weight
        f"forager_description: {fields.get('description', '') or ''}",
        "company_keywords: ",
        f"g2_categories: {fields.get('industry', '') or ''}",  # industry as a category proxy
        f"employee_range: {_employee_range(count)}",
        f"employee_count: {count if count is not None else ''}",
    ])
    response = client.messages.create(
        model=_MODEL, max_tokens=1024, system=_ICP_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    return _extract_json(_response_text(response))


def _score_logo(client, name: str, domain: str = "") -> dict | None:
    user = f"company_name: {name}"
    if domain:
        user += f"\ndomain: {domain}"  # helps disambiguate + detect parked domains
    messages = [{"role": "user", "content": user}]
    response = None
    # Server runs web search; if it pauses after the 10-iteration tool loop, resume.
    for _ in range(6):
        response = client.messages.create(
            model=_MODEL, max_tokens=2048, system=_LOGO_SYSTEM,
            messages=messages, tools=[_WEB_SEARCH_TOOL],
        )
        if getattr(response, "stop_reason", None) != "pause_turn":
            break
        messages.append({"role": "assistant", "content": response.content})
    return _extract_json(_response_text(response))


def _icp_to_hubspot(data: dict) -> dict:
    return {
        "icp_match_score": data.get("match_score"),
        "icp_decision": data.get("decision"),
        "icp_confidence": data.get("confidence"),
        "icp_reasoning": data.get("reasoning_short"),
        "icp_positives": "; ".join(data.get("positives") or []),
        "icp_negatives": "; ".join(data.get("negatives") or []),
        "icp_red_flags": "; ".join(data.get("red_flags") or []),
        "icp_best_fit_use_case": data.get("best_fit_use_case"),
        "icp_suggested_next_step": data.get("suggested_next_step"),
    }


def _logo_to_hubspot(data: dict) -> dict:
    evidence = data.get("evidence") or []
    evidence_str = "; ".join(
        f"{e.get('source', '')}: {e.get('url', '')}".strip(": ")
        for e in evidence if isinstance(e, dict) and e.get("url")
    )
    return {
        "logo_score": data.get("logo_score"),
        "logo_tier": data.get("tier_recommendation"),
        "logo_confidence": data.get("confidence"),
        "logo_why": data.get("why"),
        "logo_forager_fit": data.get("forager_fit"),
        "logo_forager_fit_reason": data.get("forager_fit_reason"),
        "logo_evidence": evidence_str,
    }


def score_company(name: str, fields: dict) -> dict:
    """Run ICP + logo scoring for a company.

    Returns {"icp": <raw|error>, "logo": <raw|error>, "hubspot_fields": {...}}.
    Never raises: a failure in either score is logged and reported, and company
    enrichment continues. If scoring isn't configured, returns a "skipped" status.
    """
    out: dict = {"icp": None, "logo": None, "hubspot_fields": {}}
    client = _client()
    if client is None:
        out["status"] = "skipped"
        out["reason"] = "ANTHROPIC_API_KEY not set (or `anthropic` missing); scoring disabled"
        return out

    fields = fields or {}
    domain = fields.get("domain", "") or ""

    try:
        icp_raw = _score_icp(client, fields)
        out["icp"] = icp_raw
        if icp_raw:
            out["hubspot_fields"].update(_icp_to_hubspot(icp_raw))
    except Exception as exc:  # noqa: BLE001 - never let scoring break enrichment
        logger.warning("ICP scoring failed for '%s': %s", name, exc)
        out["icp"] = {"error": str(exc)}

    try:
        logo_raw = _score_logo(client, name, domain)
        out["logo"] = logo_raw
        if logo_raw:
            out["hubspot_fields"].update(_logo_to_hubspot(logo_raw))
    except Exception as exc:  # noqa: BLE001
        logger.warning("Logo scoring failed for '%s': %s", name, exc)
        out["logo"] = {"error": str(exc)}

    out["status"] = "scored"
    return out
