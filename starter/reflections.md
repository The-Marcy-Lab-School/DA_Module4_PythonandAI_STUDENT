# Reflections

Two required sections. Both graded, both real — see `rubric.md` (ask
your instructor) for exactly what each is checked against.

## Part 1: psycopg2 vs. SQLAlchemy — Your Real Comparison

You just connected to your own database both ways in `analysis.ipynb`.
Now compare them for real — not a textbook definition of each, reasoning
about *this actual notebook and this actual query*.

### The comparison framework

For each dimension below, answer based on what you actually experienced
running both, not what you'd expect in the abstract:

| Dimension | psycopg2 | SQLAlchemy |
|---|---|---|
| Lines of code to get a connection open | TODO | TODO |
| What happens if your query has a typo — how clear was the error? | TODO | TODO |
| How much would change if your database engine (SQL flavor) changed? | TODO | TODO |
| Would you trust this in a script someone else has to maintain later? | TODO | TODO |

### Your recommendation

For **your actual notebook** — a one-off analyst pulling a query result into
pandas, not a production application — which one would you genuinely
reach for by default, and why? Be specific about *this* scenario, not a
general "SQLAlchemy is more powerful" statement that could apply to any
script.

> TODO

Is there a *different* scenario (not this one) where the other tool would
clearly be the better call? Name a real one.

> TODO

## Part 2: AI-Assisted Coding — Draft, Then Verify

This is the first module where using an AI coding assistant is itself a
graded skill — not "did you use AI," but "did you verify what it gave
you before trusting it." You did a rehearsal of this with a partner in
lecture; this is your own, solo pass on your own script.

### Step 1: Get a real AI draft

Using a free-tier AI coding assistant (Claude.ai's free tier, or another
free-tier tool you already have), ask it to draft a Python function that
connects to a PostgreSQL database and runs a query — psycopg2 or
SQLAlchemy, your choice. Use a real prompt, not a leading one that
basically writes the function for it in the prompt itself.

**Paste the AI's raw, unedited draft here:**

```python
TODO — the actual AI output, not a cleaned-up version
```

### Step 2: Trace through it for real

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

### Step 3: Document what you found

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
