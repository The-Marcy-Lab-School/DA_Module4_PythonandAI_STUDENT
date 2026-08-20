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

## Set up your Python environment with `uv`

`uv` is a modern, fast Python package/environment manager — new this
module, worth using instead of bare `pip` for a reproducible setup:

```bash
# install uv if you don't have it (see https://docs.astral.sh/uv/ for your OS)
uv init
uv add pandas psycopg2-binary sqlalchemy
```

## Reconnect to your Module 3 database

**What actually connects:** `starter/analysis.ipynb` is where the real
connecting happens — it's the notebook you'll open and run. `db_connect.py`
is not something you run on its own; it's a given module of connection
*functions* (`query_with_psycopg2`, `query_with_sqlalchemy`) that the
notebook imports and calls. Same database either way — just one file
holds the reusable connection logic, the other is where you actually use
it.

**The database name itself doesn't matter, and doesn't need to match
anything.** Whatever you named your database in Module 3 — an
auto-generated name from a hosted Supabase/Neon project, or a name you
picked yourself with a local `createdb` — is fine exactly as-is.
`DATABASE_URL` is a full connection string (host, port, database name,
username, password, all bundled into one string); as long as it's the
**same one** you used in Module 3 (or a real equivalent, if you rebuild
below), it already points at the right database regardless of what it's
called. There's no "correct" name to match — only "does this connection
string point at your actual data."

1. Confirm it's still reachable: `psql <your Module 3 connection string>`
   (whatever you used there — the exact same string, name and all). If
   you get a real prompt, you're done — set `DATABASE_URL` to that same
   string as an environment variable and move on:
   ```bash
   export DATABASE_URL="postgresql://user:password@host:port/dbname"
   ```
2. **If it's gone** (an expired free hosted project, a reformatted
   laptop, etc.): pull your own `schema.sql` from your Module 3 GitHub
   repo, recreate a database (any name — a new hosted project will
   generate one for you; locally, `createdb <any-name-you-want>` works
   fine), and reload it via `\copy` from `data/<your-domain>/` in
   **this** repo (identical files — see `data/SOURCE.md`). Then set
   `DATABASE_URL` to point at *that* new database. You already know how
   to do every step here; you did it once already.

**Never hardcode `DATABASE_URL` (or any credential) directly in
`db_connect.py`, `analysis.ipynb`, or anywhere else** — read it from the
environment, every time. This is named explicitly in this module's own
`common_project_mistakes` for a reason.

## What's next

Once `DATABASE_URL` is set and you've confirmed it connects, open
`starter/analysis.ipynb` and start there — it imports `db_connect.py`'s
given connection functions directly.
