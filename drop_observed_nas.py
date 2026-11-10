"""
Drop rows with a missing observed value from the weekly-summaries
observed data files. Companion to report_observed_nas.py, which
finds them without changing anything. Run from the HAH directory:

python3 cfa-forecast-hub-reports/drop_observed_nas.py \
    --hub rsv-forecast-hub --folder 2026-11-07
python3 cfa-forecast-hub-reports/drop_observed_nas.py \
    --hub rsv-forecast-hub --folder 2026-11-07 --write

The hubs share reference dates, so --folder on its own can match more
than one hub; pass --hub as well to act on a single file.

Rows are filtered as text rather than read and rewritten by a parser,
so every retained line keeps its original bytes and the diff shows
deletions only.
"""

import argparse
import csv
import io
from pathlib import Path

REPORTS_ROOT = Path("cfa-forecast-hub-reports") / "weekly-summaries"
TARGET_DATA_GLOB = "*/*/*_target_data.csv"
NA_TOKENS = ("NA", "NaN", "")
VALUE_COLUMN = "value"


def find_observed_files(
    root: Path, folder: str | None, hub: str | None
) -> list[Path]:
    """
    Collect the observed target data files to consider.

    A folder name alone does not identify a file, because the hubs
    share reference dates, so the hub is a separate filter rather
    than something inferred from the date.

    Parameters
    ----------
    root : Path
        The weekly-summaries directory holding per-hub report folders.
    folder : str | None
        Keep only files inside a folder of this name, such as a
        reference date; None considers every folder.
    hub : str | None
        Keep only files under this hub directory; None considers all.

    Returns
    -------
    list[Path]
        Sorted paths to the `*_target_data.csv` files.
    """
    files = sorted(root.glob(TARGET_DATA_GLOB))
    if hub is not None:
        files = [path for path in files if path.parent.parent.name == hub]
    if folder is not None:
        files = [path for path in files if path.parent.name == folder]
    return files


def is_missing(field: str) -> bool:
    """
    Decide whether an observed value counts as missing.

    Parameters
    ----------
    field : str
        The raw text of the value column.

    Returns
    -------
    bool
        True when the field is empty or a literal missing marker.
    """
    return field.strip() in NA_TOKENS


def split_rows(path: Path) -> tuple[list[str], list[str], int]:
    """
    Read a file into its header, body lines and value column index.

    Parameters
    ----------
    path : Path
        Path to a `*_target_data.csv` file.

    Returns
    -------
    tuple[list[str], list[str], int]
        The header lines, the body lines and the index of the value
        column, which is -1 when the file has no such column.
    """
    lines = path.read_text().splitlines(keepends=True)
    if not lines:
        return [], [], -1
    header = next(csv.reader(io.StringIO(lines[0])))
    index = header.index(VALUE_COLUMN) if VALUE_COLUMN in header else -1
    return lines[:1], lines[1:], index


def partition(body: list[str], index: int) -> tuple[list[str], list[str]]:
    """
    Separate the lines to keep from the lines with a missing value.

    Parameters
    ----------
    body : list[str]
        The file's lines, excluding the header.
    index : int
        Position of the value column.

    Returns
    -------
    tuple[list[str], list[str]]
        The kept lines and the dropped lines, in original order.
    """
    kept, dropped = [], []
    for line in body:
        if not line.strip():
            kept.append(line)
            continue
        fields = next(csv.reader(io.StringIO(line)))
        missing = index < len(fields) and is_missing(fields[index])
        (dropped if missing else kept).append(line)
    return kept, dropped


def main() -> None:
    """
    Report, and optionally remove, rows with a missing observed value.

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPORTS_ROOT)
    parser.add_argument(
        "--folder",
        default=None,
        help="restrict to one folder name, such as 2026-11-07",
    )
    parser.add_argument(
        "--hub",
        default=None,
        help="restrict to one hub, such as covid19-forecast-hub",
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    files = find_observed_files(args.root, args.folder, args.hub)
    if not files:
        print(f"no observed data files found under {args.root}")
        return

    total = 0
    touched = 0
    for path in files:
        header, body, index = split_rows(path)
        if index < 0:
            print(f"{path}: no {VALUE_COLUMN} column, skipped")
            continue
        kept, dropped = partition(body, index)
        if not dropped:
            continue
        touched += 1
        total += len(dropped)
        print(
            f"{path.relative_to(args.root)}: "
            f"{len(dropped)} of {len(body)} rows missing, "
            f"{len(kept)} kept"
        )
        if args.write:
            path.write_text("".join(header + kept))

    verb = "removed" if args.write else "would remove"
    print(f"\n{verb} {total} row(s) across {touched} of {len(files)} file(s)")
    if not args.write:
        print("dry run; pass --write to apply")


if __name__ == "__main__":
    main()
