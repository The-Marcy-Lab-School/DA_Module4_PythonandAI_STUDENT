# psycopg2 vs. SQLAlchemy: Your Real Comparison

You just connected to your own database both ways in `db_connect.py`.
Now compare them for real — not a textbook definition of each, reasoning
about *this actual script and this actual query*.

## The comparison framework

For each dimension below, answer based on what you actually experienced
running both, not what you'd expect in the abstract:

| Dimension | psycopg2 | SQLAlchemy |
|---|---|---|
| Lines of code to get a connection open | TODO | TODO |
| What happens if your query has a typo — how clear was the error? | TODO | TODO |
| How much would change if your database engine (SQL flavor) changed? | TODO | TODO |
| Would you trust this in a script someone else has to maintain later? | TODO | TODO |

## Your recommendation

For **your actual script** — a one-off analyst pulling a query result into
pandas, not a production application — which one would you genuinely
reach for by default, and why? Be specific about *this* scenario, not a
general "SQLAlchemy is more powerful" statement that could apply to any
script.

> TODO

Is there a *different* scenario (not this one) where the other tool would
clearly be the better call? Name a real one.

> TODO
