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

Your script connects to the **same PostgreSQL database you built in
Module 3** — not a new one.

1. Confirm it's still reachable: `psql <your Module 3 connection string>`
   (or however you connected it there). If you get a real prompt, you're
   done — set `DATABASE_URL` as an environment variable and move on:
   ```bash
   export DATABASE_URL="postgresql://user:password@host:port/dbname"
   ```
2. **If it's gone** (an expired free hosted project, a reformatted
   laptop, etc.): pull your own `schema.sql` from your Module 3 GitHub
   repo, recreate the database, and reload it via `\copy` from
   `data/<your-domain>/` in **this** repo (identical files — see
   `data/SOURCE.md`). You already know how to do every step here; you did
   it once already.

**Never hardcode `DATABASE_URL` (or any credential) directly in a `.py`
file** — read it from the environment, every time. This is named
explicitly in this module's own `common_project_mistakes` for a reason.

## What's next

Once `DATABASE_URL` is set and you've confirmed it connects, open
`starter/db_connect.py` and start there.
