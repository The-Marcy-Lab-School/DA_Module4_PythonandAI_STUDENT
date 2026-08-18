# Data Sources

This folder is the same real (or clearly-labeled synthetic) data from
Module 3 — reused here for two different reasons, not duplicated by
accident. See Module 3's own `data/SOURCE.md` for the full origin/license
detail per file; this note just covers what each one is *for* in this
module.

## 1. Reconnecting to your own database

Your Python script connects to the **same PostgreSQL database you built in
Module 3** — the one matching whichever domain you chose there. You don't
need anything from this folder for that part if your database still
exists (a hosted Supabase/Neon project, or a still-installed local
Postgres).

**If it doesn't exist anymore** (a free hosted project expired, a
reformatted laptop, etc.): pull your own `schema.sql` from your Module 3
GitHub repo, recreate the database, and reload it from **your domain's
folder here** using the same `\copy` commands you used the first time.
This folder has the identical files — nothing new to source or trust.

## 2. The independent data-quality cleaning exercise

For this module's independent cleaning exercise (see
`starter/independent_cleaning.md`), you'll work with **one file from a
domain you did NOT choose in Module 2/3** — genuinely unseen data to you,
even though it's not new to the project. Real, documented starting points
per domain (full detail in each file's own real messiness, see Module 3's
`SOURCE.md` for the complete picture):

- **`finance_insurance/claims.csv`** — real missing payment amounts and
  `cause_of_damage` codes on several hundred rows; **175 rows that are
  identical to another row except for `claim_id`** — a real question,
  not resolved for you: are these genuine duplicate submissions, or
  coincidentally identical claims? Investigate before deciding.
- **`public_sector/service_requests.csv`** — real missing `closed_date`
  (still-open cases) and `descriptor`; **36 rows identical except for
  `request_id`** — same real duplicate-or-coincidence question.
- **`healthcare_operations/patients.csv`** — real missing `deathdate`
  (patients still living) — a genuine null, not an error.
- **`professional_services/time_entries.csv`** — real missing `hours`
  (~4% of rows) and **6 rows with a negative `hours` value** — a planted
  data-entry-error pattern in an otherwise-synthetic file.

Pick **one file** from **one domain you didn't already work with**. You
need to find and resolve **at least 2 real issues** in it — the list
above is a real starting point, not necessarily the only 2 things you'll
find once you actually inspect the file yourself.
