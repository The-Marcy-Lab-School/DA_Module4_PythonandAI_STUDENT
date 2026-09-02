"""
Preview of Module 6 -- code given, you don't need to write this yourself.

Module 6 (the very next module) is Business Analytics: Excel & KPI
Development. A real, working look at one thing that connects directly:
exporting a cleaned pandas DataFrame to a real Excel file, not just a CSV.

Setup (one-time):
    uv add openpyxl

Usage:
    python3 above_and_beyond/excel_export_preview.py clean_analysis_output.csv
"""
import sys

import pandas as pd


def export_to_excel(csv_path: str, xlsx_path: str = "cleaned_output.xlsx") -> None:
    df = pd.read_csv(csv_path)

    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Cleaned Data", index=False)

        # A real second sheet -- a quick summary, the kind of thing Module 6
        # builds much further into a real KPI workbook.
        summary = pd.DataFrame(
            {
                "metric": ["row_count", "column_count"],
                "value": [len(df), len(df.columns)],
            }
        )
        summary.to_excel(writer, sheet_name="Summary", index=False)

    print(f"Wrote {xlsx_path} with 2 sheets: 'Cleaned Data' and 'Summary'.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python3 above_and_beyond/excel_export_preview.py "
            "clean_analysis_output.csv"
        )
    export_to_excel(sys.argv[1])
