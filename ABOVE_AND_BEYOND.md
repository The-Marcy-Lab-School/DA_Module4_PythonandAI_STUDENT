# Above & Beyond — Backlog

Only the additional items — everything in `MVP.md` still applies and isn't
repeated here. Pick these up only after MVP is genuinely done and pushed;
this is a bonus sprint, not part of this one.

- [ ] **Preview of Module 6 — code given, you don't need to write this
  yourself.** Run `above_and_beyond/excel_export_preview.py` against your
  `clean_analysis_output.csv`. Module 6 (the very next module) is
  Business Analytics & Data Visualization — this is a real, working
  look at exactly what that module builds on. Write a short reflection on
  what a second Excel sheet (a real summary, however small) starts to
  hint at that a single CSV can't do.

- [ ] **Do Part 2 in the library you didn't pick, and compare.** If you
  used pandas for Part 2, run `above_and_beyond/polars_comparison.py`
  against your `clean_analysis_output.csv` (or vice versa — redo Part 2's
  join/aggregation in the other library). Write a short comparison of
  what you actually saw (remember: small-file timing genuinely varies
  run to run — look for a real pattern across a few runs, don't trust
  one number) and which library's syntax you'd reach for again, and why.

- [ ] **Commit a `uv.lock` file** and confirm a teammate (or you, in a
  fresh clone) gets an identical environment from it — real reproducible-
  environment practice that Module 8's CI/CD-adjacent work assumes later.

- [ ] **Define a real SQLAlchemy ORM model class** for one of your Module
  3 tables, and use it for one query instead of a raw SQL string. Previews
  the deeper SQLAlchemy usage Modules 7/8 assume you're comfortable with.
