# Data Sources

This folder is the same real (or clearly-labeled synthetic) data from
Module 3 — reused here for reconnecting to your own database. See
Module 3's own `data/SOURCE.md` for the full origin/license detail per
file; this note just covers what it's *for* in this module.

## Reconnecting to your own database

Your Python script connects to the **same PostgreSQL database you built in
Module 3** — the one matching whichever domain you chose there. You don't
need anything from this folder for that if your database still exists (a
hosted Supabase/Neon project, or a still-installed local Postgres).

**If it doesn't exist anymore** (a free hosted project expired, a
reformatted laptop, etc.): rebuild it the Python-only way Module 3 uses —
pull your own `schema.sql` and `db.py` from your Module 3 GitHub repo, run
`db.py` against your schema to recreate your tables, then use `db.py`'s
own `load_csv()` to reload from **your domain's folder here** (identical
files — nothing new to source or trust). See
[`GETTING_STARTED.md`](../GETTING_STARTED.md) for the exact steps.

## What's actually messy in your own domain

This module's Part 2 (in `starter/analysis.ipynb`) has you find and clean
real data-quality issues **in your own domain's tables** — not a domain
you didn't choose. Every domain genuinely has at least 2 real, cleanable
issues once you actually inspect it (`.info()`, `.isna().sum()`, a real
duplicate check that drops the ID column first) — don't just take this
list's word for it, confirm it yourself against your own live data:

- **`finance_insurance`** — `claims`: real missing
  `amount_paid_building`/`amount_paid_contents` on several hundred rows,
  and **175 rows that are duplicate-content claims** (identical except
  for `claim_id`) — a real question, not resolved for you: genuine
  duplicate submissions, or coincidentally identical claims? Investigate
  before deciding.
- **`public_sector`** — `service_requests`: real missing `descriptor` on
  110 rows, and **36 duplicate-content rows** (identical except for
  `request_id`) — same real duplicate-or-coincidence question.
  (`closed_date` missing is a genuinely valid state — a still-open
  case — not an issue to fix.)
- **`healthcare_operations`** — this domain looks clean at a glance in
  Module 3's own docs, but a direct inspection turns up two real issues
  that aren't documented anywhere else: `patients`: 304 rows missing
  `marital_status` (mostly, but not entirely, patients too young to have
  been married — there's at least one 109-year-old exception, so it's a
  real judgment call, not a clean age cutoff); `facilities`: **3
  duplicate-content rows** (identical except for `facility_id`).
  (`deathdate` missing is a genuinely valid state — the patient is
  still alive — not an issue to fix.)
- **`professional_services`** — `time_entries`: real missing `hours` on
  ~4% of rows, and **6 rows with a genuine negative `hours` value** — a
  planted data-entry-error pattern in an otherwise-synthetic file.
  (`end_date` missing on ongoing engagements is a genuinely valid state —
  not an issue to fix.)

You need to find and resolve **at least 2 real issues** in your own
domain's tables — the list above is a real starting point for *your*
domain, not necessarily the only 2 things you'll find once you inspect it
yourself.
