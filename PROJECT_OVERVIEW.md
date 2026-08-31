# Project Overview: Python for Data Analysis & Database Connectivity

## The objective

Reconnect to the real PostgreSQL database you built in Module 3, and
write a Python script that queries it two different ways — directly via
`psycopg2`, and separately via `SQLAlchemy` — pulling the result into a
real pandas DataFrame each time. Write up a genuine comparison of the two
approaches based on what you actually experienced, not a textbook
definition. Use a free-tier AI coding assistant to draft a connection
function, then find and document a real bug or inefficiency in its
suggestion before trusting it — the first formally graded AI-assisted-
coding work in the program. Finally, independently clean a genuinely
unseen dataset (a domain you didn't work with in Module 2/3): find and
resolve at least 2 real data-quality issues, justify each decision in
writing, and output a clean, analysis-ready CSV.

## Why it matters

Every prior project lived in one tool at a time — a notebook, or a
database. Real analyst work constantly crosses that boundary: pulling a
live query result into Python to actually do something with it. This is
also the first time an AI coding assistant is a *graded* part of your
work, not just something you might personally use — verifying an AI's
suggestion before trusting it is a real, permanent habit, not a one-time
exercise. It gets used immediately: this connects directly to **Module 5**
(Business Analytics), and real Python fluency keeps compounding through
Modules 8, 9, 11, 12, 13, and the Capstone.

## Deliverables at a glance

- A **public GitHub repo** (your own, from "Use this template"), with
  real `.gitignore`/`LICENSE` you set up yourself.
- A working connection to your Module 3 database via **both** psycopg2
  and SQLAlchemy, pulling a real query result into pandas.
- A written psycopg2-vs-SQLAlchemy comparison, reasoned from your own
  actual script.
- A real AI-drafted connection function, plus your own written
  correction log documenting a real bug/inefficiency you found and fixed.
- An independently cleaned, genuinely unseen dataset: ≥2 real
  data-quality issues found and resolved, each justified in writing, a
  clean output CSV.
- Real, incremental commits — no hardcoded credentials anywhere.

## Skills you'll practice

- **Python** — connecting to a live database two different ways and
  working with the results in pandas.
- **Data Analysis** — independently finding and resolving real
  data-quality issues, with real written justification.
- **AI-Assisted Coding** — using an AI assistant as a first draft, then
  verifying it before trusting it — not accepting suggestions blind.
- **Git & Version Control** — real, independent environment setup and
  atomic commit hygiene, a full rep past Module 0's first-ever pass.
- **General Programming & Coding** — clear variable names and a logical
  script structure, without a template.

## Timeline

See `CHECKLIST_TIMELINE.md` for the day-by-day sprint pace and the full
submission checklist — 5 build days, plus a required share-out session
scheduled after.

## Where to start

Go to `README.md`, then `GETTING_STARTED.md`.
