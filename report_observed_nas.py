"""
Print any missing values found in the observed data files
across every weekly-summaries folder. Read-only; nothing is
written. Run from the HAH directory:

python3 report_observed_nas.py
python3 report_observed_nas.py --root some/other/weekly-summaries
"""

import argparse
from pathlib import Path

import polars as pl

REPORTS_ROOT = Path("cfa-forecast-hub-reports") / "weekly-summaries"
TARGET_DATA_GLOB = "*/*/*_target_data.csv"
NA_TOKENS = ("NA", "NaN", "")
VALUE_COLUMN = "value"
DETAIL_COLUMNS = ("week_ending_date", "location", "location_name", "target")


def find_observed_files(root: Path) -> list[Path]:
    """
    Collect every observed target data file under the reports root.

    Parameters
    ----------
    root : Path
        The weekly-summaries directory holding per-hub report folders.

    Returns
    -------
    list[Path]
        Sorted paths to the `*_target_data.csv` files.
    """
    return sorted(root.glob(TARGET_DATA_GLOB))


def na_mask() -> pl.Expr:
    """
    Build the expression selecting rows whose observed value is missing.

    Returns
    -------
    pl.Expr
        Boolean expression that is true for null or literal NA values.
    """
    value = pl.col(VALUE_COLUMN)
    return value.is_null() | value.str.strip_chars().is_in(list(NA_TOKENS))


def find_na_rows(path: Path) -> pl.DataFrame:
    """
    Read one observed data file and return only its missing-value rows.

    Every column is read as a string so that literal "NA" entries stay
    intact rather than being coerced to nulls or breaking type inference.

    Parameters
    ----------
    path : Path
        Path to a `*_target_data.csv` file.

    Returns
    -------
    pl.DataFrame
        The missing-value rows, limited to the identifying columns.
    """
    frame = pl.read_csv(path, infer_schema_length=0)
    columns = [c for c in DETAIL_COLUMNS if c in frame.columns]
    return frame.filter(na_mask()).select(columns)


def summarize(rows: pl.DataFrame, column: str) -> pl.DataFrame:
    """
    Count missing-value rows grouped by one column, most frequent first.

    Parameters
    ----------
    rows : pl.DataFrame
        The combined missing-value rows across all files.
    column : str
        Column to group by.

    Returns
    -------
    pl.DataFrame
        The group counts, sorted descending.
    """
    return rows.group_by(column).len().sort("len", descending=True)


def main() -> None:
    """
    Print the missing observed values found under the reports root.

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=REPORTS_ROOT,
        help="weekly-summaries directory to scan",
    )
    args = parser.parse_args()

    files = find_observed_files(args.root)
    if not files:
        print(f"no observed data files found under {args.root}")
        return

    print(f"scanning {len(files)} observed data files under {args.root}\n")

    found = []
    for path in files:
        rows = find_na_rows(path)
        if rows.height == 0:
            continue
        found.append(rows)
        print(f"{path.relative_to(args.root)}: {rows.height} missing")
        with pl.Config(tbl_rows=-1):
            print(rows)

    if not found:
        print("no missing observed values found")
        return

    combined = pl.concat(found)
    print(
        f"\n{combined.height} missing values across "
        f"{len(found)} of {len(files)} files"
    )
    for column in ("target", "location_name", "week_ending_date"):
        if column in combined.columns:
            print(f"\nby {column}:")
            print(summarize(combined, column))


if __name__ == "__main__":
    main()
