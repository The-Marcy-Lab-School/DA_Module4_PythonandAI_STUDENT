"""
Given connection template -- the connection mechanics themselves (opening,
closing, reading credentials from the environment) are given so you're not
reinventing driver boilerplate. What you write yourself: the actual query,
and everything you do with the result once it's a DataFrame.

Before running anything here, set your Module 3 database's connection
info as an environment variable (never hardcode it in this file -- see
this module's own common_project_mistakes):
    export DATABASE_URL="postgresql://user:password@host:port/dbname"

Setup (one-time):
    uv add psycopg2-binary sqlalchemy pandas
"""
import os

import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text


def get_database_url() -> str:
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise SystemExit(
            "Set DATABASE_URL first, e.g.:\n"
            '  export DATABASE_URL="postgresql://user:password@host:port/dbname"'
        )
    return dsn


def query_with_psycopg2(sql: str) -> pd.DataFrame:
    """Connect via psycopg2 directly, run one query, return a DataFrame.

    Given: the connect/cursor/close mechanics. Not given: what SQL you
    actually run -- that's yours, from your own Module 3 schema.
    """
    conn = psycopg2.connect(get_database_url())
    try:
        return pd.read_sql(sql, conn)
    finally:
        conn.close()  # always release the connection -- see common_project_mistakes


def query_with_sqlalchemy(sql: str) -> pd.DataFrame:
    """Connect via SQLAlchemy, run the same query, return a DataFrame.

    Given: the engine/connection mechanics. Not given: the query itself.
    """
    engine = create_engine(get_database_url())
    with engine.connect() as conn:
        return pd.read_sql(text(sql), conn)


if __name__ == "__main__":
    # TODO: write a real query against your own Module 3 schema -- one
    # that pulls the rows you'll actually clean and analyze below.
    my_query = "TODO"

    df_psycopg2 = query_with_psycopg2(my_query)
    df_sqlalchemy = query_with_sqlalchemy(my_query)

    # TODO: confirm both DataFrames actually match (same shape, same
    # values) -- don't just assume both connection methods returned the
    # same thing.

    # TODO: your real analysis/cleaning work starts here.
