#!/usr/bin/env python3
"""
Outreach -> contacts bridge (Forager-Signals  ->  Forager-HubSpot)
------------------------------------------------------------------
Connects the two projects. For every company the signals system flagged
`outreach = 'Yes'` in Supabase (total_score >= 80), this checks HubSpot to see
whether that company already has any contacts. If it has none, it runs the
EXISTING buyer-discovery + enrichment (`enrichment.discover_and_create_contacts`)
- the same process a company webhook triggers. Nothing about that process changes.

Companies that already have >=1 contact are skipped (nothing to do).

SAFE BY DEFAULT: this is a DRY RUN unless you pass --live. Dry run reads the
outreach list and checks contacts but spends NO credits - it just prints what it
WOULD do. Add --live only when you actually want to discover + enrich people.

Reads Supabase (add SUPABASE_URL / SUPABASE_KEY / SUPABASE_TABLE to .env); the
HubSpot + Forager + Deepline keys this project already uses do the rest.

Usage:
  python outreach_to_contacts.py                 # dry run (no credits) - preview
  python outreach_to_contacts.py --live          # actually discover + enrich
  python outreach_to_contacts.py --live --limit 1   # only the first company (test)
  python outreach_to_contacts.py --live --max-contacts 5
"""

import argparse
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

import enrichment   # noqa: E402  (import after load_dotenv so env is set)
import hubspot      # noqa: E402

SUPABASE_URL   = os.environ.get("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY   = os.environ.get("SUPABASE_KEY", "")
SUPABASE_TABLE = os.environ.get("SUPABASE_TABLE", "t1_tam_companies")


def _outreach_companies():
    """Companies the signals system marked outreach='Yes' (total_score >= 80)."""
    if not (SUPABASE_URL and SUPABASE_KEY):
        sys.exit("Missing SUPABASE_URL / SUPABASE_KEY in .env "
                 "(needed to read the outreach list from Supabase).")
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
        headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"},
        params={"select": "record_id,company_name,domain",
                "outreach": "eq.Yes",
                "order": "total_score.desc.nullslast"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def _contact_count(company_id: str) -> int:
    try:
        return len(hubspot.get_contacts_for_company(str(company_id)) or [])
    except Exception as e:  # noqa: BLE001
        print(f"    ! could not read HubSpot contacts: {e}")
        return -1   # unknown -> treat as "do not touch" (never enrich blindly)


def main():
    ap = argparse.ArgumentParser(description="Enrich contacts for outreach=Yes companies with no contacts.")
    ap.add_argument("--live", action="store_true",
                    help="actually run discovery + enrichment (spends credits). Default is a dry run.")
    ap.add_argument("--limit", type=int, default=0, help="process at most N companies (0 = all).")
    ap.add_argument("--max-contacts", type=int, default=5, help="max people to create per company (default 5).")
    ap.add_argument("--job-title-filter", default=None, help="optional exact title filter.")
    args = ap.parse_args()

    companies = _outreach_companies()
    if args.limit:
        companies = companies[: args.limit]

    mode = "LIVE (will spend credits)" if args.live else "DRY RUN (no credits)"
    print(f"outreach=Yes companies in {SUPABASE_TABLE}: {len(companies)}   mode: {mode}\n")

    to_enrich = skipped = errored = triggered = 0
    for c in companies:
        cid, name, domain = str(c["record_id"]), c.get("company_name") or "", c.get("domain") or ""
        n = _contact_count(cid)
        if n < 0:
            errored += 1
            print(f"-> {name}: SKIP (couldn't read HubSpot)")
            continue
        if n >= 1:
            skipped += 1
            print(f"-> {name}: already has {n} contact(s) - skip")
            continue
        # no contacts -> needs enrichment
        to_enrich += 1
        if not domain:
            print(f"-> {name}: 0 contacts, but NO domain on record - cannot discover, skip")
            continue
        if not args.live:
            print(f"-> {name}: 0 contacts -> WOULD discover + enrich people (dry run)")
            continue
        print(f"-> {name}: 0 contacts -> discovering + enriching people ...")
        try:
            results = enrichment.discover_and_create_contacts(
                hubspot_company_id=cid,
                company_domain=domain,
                job_title_filter=args.job_title_filter,
                max_contacts=args.max_contacts,
            )
            triggered += 1
            print(f"     created/updated {len(results)} contact(s)")
        except Exception as e:  # noqa: BLE001
            errored += 1
            print(f"     ERROR: {e}")

    print(f"\nSummary: {len(companies)} outreach=Yes | already had contacts: {skipped} | "
          f"needed enrichment: {to_enrich} | "
          + ("triggered: %d" % triggered if args.live else "would trigger: %d (dry run)" % to_enrich)
          + f" | errors: {errored}")
    if not args.live and to_enrich:
        print("Re-run with --live to actually discover + enrich those companies.")


if __name__ == "__main__":
    main()
