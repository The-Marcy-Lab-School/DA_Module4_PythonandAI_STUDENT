"""
Preview -- code given, you don't need to write this yourself.

Compares pandas vs. polars reading and querying the same CSV -- the file
you're already using in starter/analysis.ipynb's Part 2. This module's own
tools notes flag polars as a real, faster modern alternative worth knowing
exists (unlike Module 2, where it was deliberately left out) -- this is
that awareness, hands-on.

Setup (one-time):
    uv add polars

Usage:
    python3 above_and_beyond/polars_comparison.py path/to/your_file.csv
"""
import sys
import time

import pandas as pd
import polars as pl


def time_pandas(path: str) -> float:
    start = time.perf_counter()
    df = pd.read_csv(path)
    df.groupby(df.columns[0]).size()
    return time.perf_counter() - start


def time_polars(path: str) -> float:
    start = time.perf_counter()
    df = pl.read_csv(path)
    df.group_by(df.columns[0]).len()
    return time.perf_counter() - start


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python3 above_and_beyond/polars_comparison.py path/to/file.csv")
    path = sys.argv[1]

    pandas_time = time_pandas(path)
    polars_time = time_polars(path)

    print(f"pandas: {pandas_time:.4f}s")
    print(f"polars: {polars_time:.4f}s")
    print(
        "\nRun this a few times -- timing results for small files vary "
        "run-to-run (process warm-up, caching, etc.). Don't trust a single "
        "run's numbers; look for a consistent pattern across several."
    )
