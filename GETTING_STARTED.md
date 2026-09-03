# Getting Started

## "Use this template" vs. Fork vs. Clone

Same rule as every project: **"Use this template"** on this repo's GitHub
page (not Fork — Fork keeps a visible link back to this template) creates
your own independent copy. Clone *that* copy, not this template directly.

## Set up git yourself — this module tests it again

Unlike Module 1/3, this repo does **not** come with `.gitignore` or
`LICENSE` already made — `git-version-control` is being tested again this
module, this time expecting more independence than Module 0's first-ever
rep (`competency_assessments` literally asks for "at least 3 atomic,
well-messaged commits... up from the single first commit in Module 0").

- **Create a `.gitignore`.** Think about what this specific project
  shouldn't track — `.env` (your real database credentials go here, never
  committed — see below), Python's `__pycache__`/`.venv`, OS files like
  `.DS_Store`. Write the lines yourself; you did this once already in
  Module 0.
- **Choose a `LICENSE`.** Same call as every prior project — MIT is a
  common default; see https://choosealicense.com if you want the
  reasoning.
- **Commit both, then keep committing atomically as you go** — one commit
  per real milestone (connection working, cleaning done, etc.), not
  everything bundled into one commit at the end.

### What your repo should look like once this step is done

```
your-repo-name/
├── .gitignore          ← you create this
├── LICENSE             ← you create this
├── README.md           ← already here
├── PROJECT_OVERVIEW.md ← already here
├── GETTING_STARTED.md  ← already here
├── CHECKLIST_TIMELINE.md ← already here
├── data/               ← already here (4 real domains, pick one)
└── starter/
    ├── db_connect.py           ← already here (given connection functions)
    ├── analysis.ipynb          ← already here (this is what you run)
    └── reflections.md          ← already here (fill in both sections)
```

## Set up your Python environment with `uv`

`uv` is a modern, fast Python package/environment manager — new this
module, worth using instead of bare `pip` for a reproducible setup:

```bash
# install uv if you don't have it (see https://docs.astral.sh/uv/ for your OS)
uv init
uv add pandas psycopg2-binary sqlalchemy
```

## Reconnect to your Module 3 database

**What actually connects:** [`starter/analysis.ipynb`](starter/analysis.ipynb)
is where the real connecting happens — it's the notebook you'll open and
run. [`db_connect.py`](starter/db_connect.py) is not something you run on
its own; it's a given module of connection *functions*
(`query_with_psycopg2`, `query_with_sqlalchemy`) that the notebook imports
and calls. Same database either way — just one file holds the reusable
connection logic, the other is where you actually use it.

**The database name itself doesn't matter, and doesn't need to match
anything.** Whatever you named your database in Module 3 — an
auto-generated name from a hosted Supabase/Neon project, or a name you
picked yourself with a local install — is fine exactly as-is.
`DATABASE_URL` is a full connection string (host, port, database name,
username, password, all bundled into one string); as long as it's the
**same one** you used in Module 3 (or a real equivalent, if you rebuild
below), it already points at the right database regardless of what it's
called. There's no "correct" name to match — only "does this connection
string point at your actual data."

**You won't use `psql` for this, same as Module 3** — every check runs
through Python instead, using this module's own given `db_connect.py`:

1. Confirm it's still reachable — set `DATABASE_URL` to your exact
   Module 3 connection string, then run one real query through Python:
   ```bash
   export DATABASE_URL="postgresql://user:password@host:port/dbname"
   cd starter
   python3 -c "from db_connect import query_with_psycopg2; print(query_with_psycopg2('SELECT 1;'))"
   ```
   If that prints back a real result, you're done — move on.
2. **If it's gone** (an expired free hosted project, a reformatted
   laptop, etc.): you need a database to point at again first — see
   your own Module 3 repo's own `GETTING_STARTED.md` for the hosted-vs-
   local install steps (same choice you already made once). Once you
   have a fresh database, rebuild it the same
   Python-only way Module 3 did — pull your own `starter/schema.sql` and
   `starter/db.py` from your **Module 3** GitHub repo, then from that
   repo run:
   ```bash
   python3 starter/db.py starter/schema.sql    # recreates your tables
   ```
   and use `db.py`'s own `load_csv()` function to reload each table from
   `data/<your-domain>/` in **this** repo (identical files — see
   [`data/SOURCE.md`](data/SOURCE.md)). No `\copy`, no `psql` — you
   already know how to do every step here; you did it once already. Then
   set `DATABASE_URL` to point at *that* new database.

**Never hardcode `DATABASE_URL` (or any credential) directly in
`db_connect.py`, `analysis.ipynb`, or anywhere else** — read it from the
environment, every time. This is named explicitly in this module's own
`common_project_mistakes` for a reason.

## What's next

Once `DATABASE_URL` is set and you've confirmed it connects, open
[`starter/analysis.ipynb`](starter/analysis.ipynb) and start there — it
imports `db_connect.py`'s given connection functions directly.
