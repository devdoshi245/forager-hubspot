# Forager × HubSpot Enrichment Automation

A small Flask service that enriches HubSpot CRM records using the
[Forager](https://www.forager.ai/) data API.

It can:

1. **Enrich a company** — look it up in Forager and write back description,
   revenue, headcount, LinkedIn, location, industry, etc.
2. **Enrich a contact** — use a contact's LinkedIn URL to find emails + phone
   numbers and write them back.
3. **Find contacts at a company** — discover current employees, keep only those
   whose **job title is on the TAM buyer-committee list**, create them in HubSpot,
   and associate them to the company.
4. **Score the company (Claude)** — alongside enrichment, compute **ICP fit**
   (is this a good Forager prospect?) and **logo recognizability** (brand
   notability, via web search) and write both score sets back to the company.
5. **Company webhook** — on "company created", auto-run: enrich + score company →
   enrich existing contacts → find & create new buyer-committee contacts.
6. **Contact webhook** — on "contact created", auto-enrich that contact.

## Architecture

| File | Responsibility |
|------|----------------|
| `forager.py` | All Forager API calls + response → field mapping |
| `hubspot.py` | All HubSpot CRM calls (+ custom-property bootstrap, resilient writes) |
| `buyer_committee.py` | TAM buyer-committee title list + the title matcher |
| `scoring.py` | Claude-powered ICP fit + logo recognizability scoring |
| `enrichment.py` | Business logic tying Forager, Claude, and HubSpot together |
| `main.py` | Flask server (webhooks + manual triggers) |

## Buyer-committee title filtering

When the pipeline auto-discovers people at a company, it only creates + enriches
contacts whose job title matches the **TAM buyer-committee list** (Decision Maker
/ Champion / Influencer — Product, Eng/Platform, Data/AI, Partnerships, Exec, …)
in `buyer_committee.py`. Everyone else is skipped **before** any credit-spending
Forager contact lookup. Matching is normalization-tolerant (abbreviations, comma
variants, seniority prefixes). The optional `job_title_filter` still works as an
extra narrowing on top of the committee list. `max_contacts` defaults to **5**.

## Scoring (Claude)

Two company-level scores are computed via the Claude API and written to HubSpot
custom properties:

- **ICP fit** → `icp_match_score`, `icp_decision` (ICP/MAYBE/REMOVE),
  `icp_confidence`, `icp_reasoning`, `icp_positives`, `icp_negatives`,
  `icp_red_flags`, `icp_best_fit_use_case`, `icp_suggested_next_step`.
- **Logo recognizability** (uses Claude web search) → `logo_score`, `logo_tier`
  (T1/T2/T3), `logo_confidence`, `logo_why`, `logo_forager_fit`,
  `logo_forager_fit_reason`, `logo_evidence`.

Scoring is gated on `ANTHROPIC_API_KEY` — if it's unset, enrichment still runs and
the scores are simply skipped. Web search is billed to the Anthropic account
(not Forager credits).

## Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/health` | Health check |
| POST | `/webhook` | **HubSpot webhook Target URL** — routes company + contact events |
| POST | `/webhook/company` | Company-created handler (also callable directly) |
| POST | `/webhook/contact` | Contact-created handler (also callable directly) |
| POST | `/enrich/company` | Manual: `{"company_id": "123"}` |
| POST | `/enrich/contact` | Manual: `{"contact_id": "123"}` |
| POST | `/enrich/find-contacts` | Manual: `{"company_id","company_domain","job_title_filter","max_contacts"}` |
| POST | `/enrich/demo` | Full company pipeline: `{"company_id": "123"}` |

Buyer-committee filtering is always applied to auto-discovered contacts. The
optional `job_title_filter` narrows further: on `/webhook/company` and
`/enrich/demo` via a `?job_title_filter=engineer` query parameter, and on
`/enrich/find-contacts` via the `job_title_filter` body field. `/enrich/company`
and `/enrich/demo` responses include the computed `icp` and `logo` scores.

## Setup

```bash
python -m venv .venv
. .venv/Scripts/activate      # Windows;  use .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
cp .env.example .env          # then fill in real values
python main.py                # http://localhost:5000
```

### Environment variables

```
FORAGER_API_KEY       Forager API key
FORAGER_ACCOUNT_ID    Forager account id (integer, part of every API path)
HUBSPOT_TOKEN         HubSpot Private App token
ANTHROPIC_API_KEY     Claude API key — enables ICP + logo scoring (optional)
ANTHROPIC_MODEL       optional; scoring model (defaults to claude-opus-4-8)
```

The HubSpot Private App needs these scopes:
`crm.objects.companies.read/write`, `crm.objects.contacts.read/write`,
and `crm.schemas.companies.write` + `crm.schemas.contacts.write`
(so the app can create its custom properties).

## Implementation notes (Forager API specifics)

These were verified against the live API and differ from a naive reading of the
docs:

- Forager is fronted by **Cloudflare, which blocks the default Python
  user-agent** — every request sends a browser-like `User-Agent`.
- Search responses are under **`search_results`** (with `total_search_results`),
  not `results`. Company fields: `domain` (string), `employees_amount`,
  `finance_info.revenue`, `linkedin_info.public_profile_url`.
- A domain search returns many low-quality matches; the **best company is chosen
  by `domain_rank` then headcount**, not just the first result.
- Contact-lookup endpoints return a **bare JSON array**, e.g.
  `[{"email": "...", "email_type": "personal"}]`.

## Deployment (Railway)

The `Procfile` runs `gunicorn main:app`. Set the environment variables in
the Railway dashboard (the three Forager/HubSpot ones are required; add
`ANTHROPIC_API_KEY` to turn on scoring), deploy, then point your HubSpot Private
App's single
webhook **Target URL** at `https://<your-app>.up.railway.app/webhook` — it routes
company and contact events automatically (HubSpot only allows one Target URL
per app).
