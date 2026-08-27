# Python for Data Analysis & Database Connectivity Project

Start with `PROJECT_OVERVIEW.md` for what you're building and why. This
file is where the step-by-step setup lives.

**Due:** 1 week, run as a sprint — 5 build days. See `CHECKLIST_TIMELINE.md`
for the day-by-day pace and the full submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

**Before you do anything else**: click **"Use this template"** on this
repo's GitHub page (not "Fork") to create your own copy. See
`GETTING_STARTED.md` — git setup (tested again this module, less
hand-holding than Module 0), `uv` environment setup, and reconnecting to
your Module 3 database (with a real fallback if it doesn't exist anymore).

## What to do

See `starter/` for everything you'll fill in:

- **`db_connect.py`** — given connection mechanics for both psycopg2 and
  SQLAlchemy; imported directly into `analysis.ipynb`, not run on its own.
- **`analysis.ipynb`** — the graded hands-on notebook, in two parts: (1)
  connect both ways, load into pandas, produce real summary statistics;
  (2) independently clean a file from a domain you didn't work with in
  Module 2/3 (see `data/SOURCE.md`) — find and resolve at least 2 real
  data-quality issues, justify each choice, output a clean CSV.
- **`tradeoff_comparison.md`** — your real psycopg2-vs-SQLAlchemy
  comparison, based on what you actually experienced running both.
- **`ai_assisted_coding.md`** — draft a connection function with a
  free-tier AI assistant, then find and document a real bug or
  inefficiency before trusting it. First formally graded AI-assisted-
  coding work in the program — see the file for exactly what's expected.

`CHECKLIST_TIMELINE.md` has the suggested day-by-day pace and the full
sequenced checklist. Commit incrementally — after your connection works,
again after the AI-review exercise, again after the independent cleaning
— not one commit at the end.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your **M**inimum **V**iable **P**roduct —
the required baseline) or `ABOVE_AND_BEYOND.md` on purpose. Ask your instructor for the link to
this template's `project-scope` branch, or check the checklist your
instructor shares through the classroom.
