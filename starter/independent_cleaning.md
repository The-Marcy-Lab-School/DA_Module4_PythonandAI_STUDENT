# Independent Data-Quality Cleaning

No template for this one — this is meant to be a real, independent
exercise, on data you haven't already spent two modules with.

## Step 1: Pick your file

Choose **one file from a domain you did NOT work with in Module 2/3** —
see `data/SOURCE.md` for the 4 real starting points. Not your own
domain's data, even if it would be more familiar.

Domain/file chosen: _______________

## Step 2: Inspect it for real

Before fixing anything, actually look: `df.info()`, `df.head()`,
`df.isna().sum()`, and — since this file may have real duplicate-content
rows — a real duplicate check (`df.duplicated()`, and separately, a check
that drops the ID column first, since two rows can be identical in
every real way except an arbitrary ID).

## Step 3: Find and resolve at least 2 real issues

For **each** issue: name it specifically, decide how you're handling it
(`dropna`, `fillna`, `drop_duplicates`, something else), and justify the
choice in writing — a specific reason tied to *this* data, not "cleaned
the data."

### Issue 1

- What's wrong, specifically (column, and how many rows affected):

  > TODO

- Your fix (`dropna`/`fillna`/`drop_duplicates`/other) and the exact
  reasoning:

  > TODO

### Issue 2

- What's wrong, specifically:

  > TODO

- Your fix and reasoning:

  > TODO

**If you found rows that look like duplicates except for an ID column**
(a real possibility in a couple of these files) — that's a genuine
judgment call, not an automatic drop. Are they actually the same event
recorded twice, or a real coincidence given the data? Say which you
concluded and why, specifically, before deciding whether to drop them.

## Step 4: Output

- Save the cleaned result as `independent_cleaning_output.csv`.
- Confirm your before/after row counts and null counts really changed the
  way you expected — paste the real `.isna().sum()` output before and
  after, not a description of it.

```
TODO — real before/after output
```
