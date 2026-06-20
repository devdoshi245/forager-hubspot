# Forager × HubSpot Enrichment Automation

A small Flask service that enriches HubSpot CRM records using the
[Forager](https://www.forager.ai/) data API.

It can:

1. **Enrich a company** — look it up in Forager and write back description,
   revenue, headcount, LinkedIn, location, industry, etc.
2. **Enrich a contact** — use a contact's LinkedIn URL to find emails + phone
   numbers and write them back.
3. **Find contacts at a company** — discover current employees (optionally
   filtered by job title), create them in HubSpot, and associate them to the
   company.
4. **Company webhook** — on "company created", auto-run: enrich company →
   enrich existing contacts → find & create new contacts.
5. **Contact webhook** — on "contact created", auto-enrich that contact.

## Architecture

| File | Responsibility |
|------|----------------|
| `forager.py` | All Forager API calls + response → field mapping |
| `hubspot.py` | All HubSpot CRM calls (+ custom-property bootstrap, resilient writes) |
| `enrichment.py` | Business logic tying Forager and HubSpot together |
| `main.py` | Flask server (webhooks + manual triggers) |

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

Job-title filtering is supported on `/webhook/company` and `/enrich/demo` via a
`?job_title_filter=engineer` query parameter, and on `/enrich/find-contacts` via
the `job_title_filter` body field.

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

The `Procfile` runs `gunicorn main:app`. Set the three environment variables in
the Railway dashboard, deploy, then point your HubSpot Private App's single
webhook **Target URL** at `https://<your-app>.up.railway.app/webhook` — it routes
company and contact events automatically (HubSpot only allows one Target URL
per app).
