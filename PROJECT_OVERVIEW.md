# Project Overview: Python for Data Analysis & Database Connectivity

## The objective

Reconnect to your real Module 3 PostgreSQL database, then:

- **Connect to it two different ways** — directly via `psycopg2`, and
  separately via `SQLAlchemy` — pulling the result into a real pandas
  DataFrame each time, and write up a genuine comparison of the two based
  on what you actually experienced, not a textbook definition.
- **Pull at least two of your own tables** into pandas as raw,
  unaggregated data — no `JOIN`, no `GROUP BY` in the SQL this time.
- **Do the relational work yourself, in pandas** — join your tables with
  `pd.merge()` and answer a real business question with `.groupby()`,
  instead of writing another SQL query to do it for you. This is the
  actual point of the module: Module 3 already proved you can join and
  aggregate in SQL — this time it happens as real Python objects.
- **Find and resolve at least 2 real data-quality issues** in your own
  data along the way — justify each decision in writing, and output a
  clean, analysis-ready CSV.
- **Use a free-tier AI coding assistant** to draft a connection function,
  then find and document a real bug or inefficiency in its suggestion
  before trusting it — the first formally graded AI-assisted-coding work
  in the program.

## Why it matters

Every prior project lived in one tool at a time — a notebook, or a
database. Real analyst work constantly crosses that boundary: pulling a
live query result into Python and actually doing something with it there,
not just asking the database to hand back an already-finished answer.
This is also the first time an AI coding assistant is a *graded* part of
your work, not just something you might personally use — verifying an
AI's suggestion before trusting it is a real, permanent habit, not a
one-time exercise. It gets used immediately: this connects directly to
**Module 6** (Business Analytics), and real Python fluency keeps
compounding through every module from here to the Capstone.

## Deliverables at a glance

- A **public GitHub repo** (your own, from "Use this template"), with
  real `.gitignore`/`LICENSE` you set up yourself.
- A working connection to your Module 3 database via **both** psycopg2
  and SQLAlchemy, pulling a real query result into pandas.
- A written psycopg2-vs-SQLAlchemy comparison, reasoned from your own
  actual script.
- A real AI-drafted connection function, plus your own written
  correction log documenting a real bug/inefficiency you found and fixed.
- At least two of your own Module 3 tables, joined and aggregated in
  pandas (not SQL) to answer a real question about your own data — with
  ≥2 real data-quality issues found and resolved along the way, each
  justified in writing, and a clean output CSV.
- Real, incremental commits — no hardcoded credentials anywhere.

## Skills you'll practice

- **Python** — connecting to a live database two different ways, and
  doing real relational work (joining, grouping, aggregating) on the
  result as pandas objects instead of more SQL.
- **Data Analysis** — independently finding and resolving real
  data-quality issues in your own data, with real written justification.
- **AI-Assisted Coding** — using an AI assistant as a first draft, then
  verifying it before trusting it — not accepting suggestions blind.
- **Git & Version Control** — real, independent environment setup and
  atomic commit hygiene, a full rep past Module 0's first-ever pass.
- **General Programming & Coding** — clear variable names and a logical
  script structure, without a template.

## Timeline

See [`CHECKLIST_TIMELINE.md`](CHECKLIST_TIMELINE.md) for the day-by-day
sprint pace and the full submission checklist — 5 build days, plus a
required share-out session scheduled after.

## Where to start

Go to [`README.md`](README.md), then [`GETTING_STARTED.md`](GETTING_STARTED.md).
