# MVP — Minimum Bar

One line per requirement. Full grading detail lives in `rubric.md` (ask
your instructor) — this is the scannable bar, not the explanation.

- [ ] `.gitignore`/`LICENSE` created yourself, committed.
- [ ] `starter/analysis.ipynb` Part 1: a real query run successfully via
  **both** psycopg2 and SQLAlchemy (imported from `db_connect.py`)
  against your own Module 3 database, both confirmed to return the same
  real result, and at least 2 real summary statistics produced.
- [ ] `starter/reflections.md`'s tool-comparison section completed,
  reasoned from your own actual notebook — not a generic definition of
  either tool.
- [ ] `starter/reflections.md`'s AI-assisted-coding section completed: a
  real AI-drafted connection function pasted in full, a real
  bug/inefficiency found by actually tracing through it, a written fix.
- [ ] `starter/analysis.ipynb` Part 2: at least 2 of your **own** Module
  3 tables pulled raw (no `JOIN`/`GROUP BY` in the SQL), at least 2 real
  data-quality issues found and resolved, each justified in writing with
  a specific reason — not "cleaned the data" — then joined and
  aggregated with a real group-level comparison across a categorical
  variable, in pandas or polars (your choice), to answer a real question
  different from Part 1's.
- [ ] `clean_analysis_output.csv` produced.
- [ ] No hardcoded credentials anywhere in the repo; connections closed/
  released properly.
- [ ] Public GitHub repo, real incremental commits (3+, not one at the
  end).

**Don't soften this bar** — but don't add to it either. Everything past
this line is `ABOVE_AND_BEYOND.md`, not part of MVP.
