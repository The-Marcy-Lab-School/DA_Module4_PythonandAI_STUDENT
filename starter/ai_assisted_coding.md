# AI-Assisted Coding: Draft, Then Verify

This is the first module where using an AI coding assistant is itself a
graded skill — not "did you use AI," but "did you verify what it gave
you before trusting it." You did a rehearsal of this with a partner in
lecture; this is your own, solo pass on your own script.

## Step 1: Get a real AI draft

Using a free-tier AI coding assistant (Claude.ai's free tier, or another
free-tier tool you already have), ask it to draft a Python function that
connects to a PostgreSQL database and runs a query — psycopg2 or
SQLAlchemy, your choice. Use a real prompt, not a leading one that
basically writes the function for it in the prompt itself.

**Paste the AI's raw, unedited draft here:**

```python
TODO — the actual AI output, not a cleaned-up version
```

## Step 2: Trace through it for real

Before accepting any of it, actually trace through the AI's code line by
line. Real things worth checking (not a checklist to satisfy — actually
look):

- Does it hardcode a password/connection string anywhere, instead of
  reading from the environment?
- Does it actually close/release the connection, including if the query
  raises an error partway through?
- Does it build the SQL query by directly formatting a string (a real
  injection risk) instead of using parameters?
- Does it do what it claims, or does it just *look* plausible?

## Step 3: Document what you found

**The real bug or inefficiency you found:**

> TODO — be specific: which line, what's actually wrong with it, not
> "it could be improved"

**Why it matters** (what would actually go wrong if this shipped as-is):

> TODO

**Your fix** (the corrected version of just the part you changed):

```python
TODO
```

**If you genuinely found nothing wrong after really tracing through it** —
that's an acceptable outcome, but it needs the same rigor: document
*specifically* what you checked and confirmed was actually correct (not
"looks fine to me"), the same way you'd document a real code review that
happened to pass.
