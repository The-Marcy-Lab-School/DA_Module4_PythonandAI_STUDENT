# Checklist & Timeline — 5 Days

This project runs as **one sprint**, 5 days long. Every item below is also
the actual submission checklist — work through it in order, top to bottom.
This is your 4th rep of sprint pacing — same rules as before: `MVP.md`'s
bar is fixed once you start, a quick daily check-in (what did I finish,
what am I doing today, what's blocking me), and `ABOVE_AND_BEYOND.md` is
this sprint's backlog — real work, deliberately not in scope this week.

## Day 1 — Setup

- [ ] Repo created from the template via **"Use this template"** (not
  Fork), cloned locally.
- [ ] `.gitignore`/`LICENSE` created **yourself** this time (see
  [`GETTING_STARTED.md`](GETTING_STARTED.md)) and committed.
- [ ] `uv`-managed environment set up; `pandas`/`psycopg2-binary`/
  `sqlalchemy` installed.
- [ ] `DATABASE_URL` confirmed connecting to your **Module 3** database —
  or, if it's gone, the real fallback rebuild done (see
  [`GETTING_STARTED.md`](GETTING_STARTED.md)/[`data/SOURCE.md`](data/SOURCE.md)).
- [ ] `starter/analysis.ipynb`'s Part 2 intro read in full — you'll need
  at least 2 of your **own** Module 3 tables, so know which two before
  Day 4.
- [ ] Commit: a real, descriptive message you write yourself.

## Day 2 — Connect both ways, compare them

- [ ] `starter/analysis.ipynb` Part 1: a real query written, run
  successfully via **both** `query_with_psycopg2` and
  `query_with_sqlalchemy` (imported from `db_connect.py`), both confirmed
  to return the same real result, and at least 2 real summary statistics
  produced from it.
  > ⚠️ Common mistake: hardcoding your database credentials directly in
  > the notebook instead of reading `DATABASE_URL` from the environment.
  > ⚠️ Common mistake: never closing/releasing the connection — confirm
  > `db_connect.py`'s given `finally: conn.close()` is actually still
  > there and you haven't removed it while editing.
- [ ] [`starter/tradeoff_comparison.md`](starter/tradeoff_comparison.md)
  completed — reasoned from what you actually saw running both, not a
  general definition of either.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 3 — AI-assisted coding exercise

- [ ] [`starter/ai_assisted_coding.md`](starter/ai_assisted_coding.md)
  completed: a real AI-drafted connection function pasted in full, a real
  bug or inefficiency actually found by tracing through it, a written fix.
  > ⚠️ Common mistake: accepting AI-suggested connection code without
  > actually tracing through what it does — a function that runs without
  > an error isn't the same as a function that's actually safe/correct.
- [ ] Commit: a real, descriptive message you write yourself.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
3 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 4 — Deepen & clean your own data, in pandas

- [ ] `starter/analysis.ipynb` Part 2 completed: **≥2 of your own Module
  3 tables** pulled in raw (no `JOIN`/`GROUP BY` in the SQL), ≥2 real
  data-quality issues found and resolved in them, each justified in
  writing with a specific reason.
  > ⚠️ Common mistake: a silent `.dropna()` with no check on how much data
  > that actually discarded, or why — always confirm with a real
  > `.isna().sum()` before and after, and say what you found.
- [ ] Your cleaned tables **joined with `pd.merge()` and aggregated with
  `.groupby()`, in pandas** — a real business question about your own
  data, answered by writing Python, not another SQL query.
- [ ] `clean_analysis_output.csv` produced.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 5 — Finish, verify, submit

- [ ] Final pass: no hardcoded credentials anywhere in the repo (grep your
  own files for your actual password/connection string before pushing).
- [ ] Clean sweep of your script: no leftover debug `print()` calls,
  commented-out dead code, or scratch experiments left in — only the
  real, working script.
- [ ] **Delete `PROJECT_OVERVIEW.md`** — it explains the assignment, not
  your project; a real portfolio repo shouldn't have "here's what you
  were asked to build" sitting in it.
- [ ] **Replace `README.md`'s content with your own real project README**
  — write it for someone who's never seen this assignment:
  - **Business Problem** — what question your analysis answers.
  - **Methodology** — psycopg2 vs. SQLAlchemy, and how you joined,
    cleaned, and aggregated your own tables in pandas.
  - **Key Findings** — your real summary statistics, the result of your
    pandas join/aggregation, and your cleaning decisions.
  - **AI Integration/Validation** — the real bug/inefficiency you caught
    in the AI-drafted connection function.
- [ ] Final push to GitHub — confirm the repo is actually **public** (open
  it in a private/incognito browser window to check).
- [ ] Final self-check against this checklist before calling it done.
- [ ] Commit(s) pushed — `git log --oneline` should show real,
  incremental history (3+ commits), not one giant final commit.

**Exit criterion:** everything above is done and pushed. That's the whole
sprint. Backlog items (`ABOVE_AND_BEYOND.md`) are exactly that — backlog.

## Day 6 — Share-out

Your instructor schedules this once every submission is in — usually a
few days after Day 5, not necessarily the next calendar day. Real
session, not optional: an anonymized peer review of classmates'
data-quality-cleaning logs (`analysis.ipynb`'s Part 2), reviewed in
groups of 3 against real specificity/verification/duplicate-judgment
questions in a shared doc, then a share-out of trends across logs. No
extra prep needed — just have your repo pushed and public before the
session — see your instructor for the exact date.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. Details in `ABOVE_AND_BEYOND.md`.

- [ ] Run the given-code `above_and_beyond/polars_comparison.py` and write
  a short reflection comparing it to your own pandas workflow.
- [ ] Run the given-code `above_and_beyond/excel_export_preview.py`
  (Module 6 preview) and write a short reflection.
- [ ] Commit a `uv.lock` file and confirm a clean re-install from it.
- [ ] Define a real SQLAlchemy ORM model class for one of your tables and
  use it for one query, instead of raw SQL strings.
