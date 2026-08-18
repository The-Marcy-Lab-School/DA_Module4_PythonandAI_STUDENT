"""
Given connection template -- the connection mechanics themselves (opening,
closing, reading credentials from the environment) are given so you're not
reinventing driver boilerplate. What you write yourself: the actual query,
and everything you do with the result once it's a DataFrame -- in
`analysis.ipynb`, which imports these two functions directly.

Before running anything, set your Module 3 database's connection info as
an environment variable (never hardcode it in this file -- see this
module's own common_project_mistakes):
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
