#!/usr/bin/env python3
"""
GitBook Batch Formatter
========================
Transforms a Google Drive export CSV (columns: Folder Path, Name, Original Link,
Downloadable Link) into a nested folder/markdown structure ready to be committed
to a GitBook-synced GitHub repository.

USAGE:
    python3 gitbook_batch_formatter_v2.py

The script interactively asks for:
    1. The path to the source .csv file
    2. The output formatting style(s) to apply (numbered choice, comma-separated
       for multiple formats run simultaneously, e.g. "1,2")

CORE RULES
----------
1. EMBEDS (formats 2 & 3 only — never format 1/table):
   Immediately after a row's link line, a GitBook embed block is inserted when
   either is true:
     a. The row's Original Link is a native Google Slides / Docs / Sheets URL
        (docs.google.com/presentation|document|spreadsheets) — these are
        typically duplicate representations of the same content as an actual
        uploaded file elsewhere in the data, and need a working "open it
        in-place" option since they can't be downloaded as a generic file.
     b. The row's Name contains "PYQ" (case-insensitive).
   The embed always uses the Original Link:
        {% embed url="{ORIGINAL-LINK}" %}

2. TABLE-FORMAT FILTERING (format 1 only):
   The Downloadable Link only reliably works for genuine uploaded files whose
   Original Link matches the pattern drive.google.com/file/d/{ID}/view — i.e.
   NOT Google-native Slides/Docs/Sheets. Since the table format's only
   interactive element per row besides the name is the download button (no
   embed fallback is used here), any row that isn't a genuine file link is
   excluded entirely from table-format output (and logged to the terminal).

3. FOLDER FLATTENING (single-format runs only):
   A root folder that has no nested subfolders (i.e. all its rows sit directly
   under it, no deeper "/" segments) no longer gets wrapped in its own
   directory — its content is written directly as "<ROOT>.md" next to the
   other root folders, instead of "<ROOT>/<ROOT>.md".
   Root folders that DO have nested subfolders keep the wrapping folder, since
   it has somewhere to live.

4. MULTI-FORMAT MODE:
   When more than one format is selected at once, flattening (rule 3) is
   disabled — every root folder always gets its own wrapping directory, since
   that directory is now needed to hold multiple sibling files (one per
   format), e.g.:
        BCU641/BCU641-table.md
        BCU641/BCU641-original-link.md
   This keeps same-course outputs "clubbed" together under one folder.
"""

import csv
import os
import re
import sys
from pathlib import Path
from collections import OrderedDict

REQUIRED_COLUMNS = ["Folder Path", "Name", "Original Link", "Downloadable Link"]

PLACEHOLDER_ORIGINAL_LINK = "https://placeholder.invalid/UPDATE-ORIGINAL-LINK"
PLACEHOLDER_DOWNLOAD_LINK = "https://placeholder.invalid/UPDATE-DOWNLOAD-LINK"

FORMAT_TABLE = 1
FORMAT_PLAIN_ORIGINAL = 2
FORMAT_PLAIN_DOWNLOAD = 3

FORMAT_LABELS = {
    FORMAT_TABLE: "Table with download button (dual link: original + downloadable)",
    FORMAT_PLAIN_ORIGINAL: "Plain markdown link using the ORIGINAL link",
    FORMAT_PLAIN_DOWNLOAD: "Plain markdown link using the DOWNLOADABLE link",
}

FORMAT_SLUGS = {
    FORMAT_TABLE: "table",
    FORMAT_PLAIN_ORIGINAL: "original-link",
    FORMAT_PLAIN_DOWNLOAD: "download-link",
}

# Fields each format strictly requires to render correctly.
FORMAT_REQUIRED_FIELDS = {
    FORMAT_TABLE: ["Original Link", "Downloadable Link"],
    FORMAT_PLAIN_ORIGINAL: ["Original Link"],
    FORMAT_PLAIN_DOWNLOAD: ["Downloadable Link"],
}

# Native Google Workspace document types — never genuinely "downloadable" as a
# plain file the way an uploaded PDF/DOCX/etc. is.
NATIVE_DOC_URL_PATTERNS = [
    "docs.google.com/presentation",
    "docs.google.com/document",
    "docs.google.com/spreadsheets",
]

# Only links matching this pattern are treated as a genuine downloadable file.
REAL_FILE_PATTERN = re.compile(r"drive\.google\.com/file/d/", re.IGNORECASE)


# --------------------------------------------------------------------------- #
# Tree node representing one folder-path segment
# --------------------------------------------------------------------------- #
class Node:
    __slots__ = ("name", "entries", "children")

    def __init__(self, name):
        self.name = name               # literal folder segment name (heading text)
        self.entries = []              # list of row dicts attached directly at this path
        self.children = OrderedDict()  # subfolder_name -> Node (insertion order preserved)

    def get_or_create_child(self, name):
        if name not in self.children:
            self.children[name] = Node(name)
        return self.children[name]


# --------------------------------------------------------------------------- #
# Step 1: CSV loading & validation
# --------------------------------------------------------------------------- #
def prompt_csv_path():
    while True:
        raw = input("\nEnter the full path to the source .csv file: ").strip()
        cleaned = raw.strip('"').strip("'")
        path = Path(cleaned).expanduser()
        if not path.is_file():
            print(f"  ✗ File not found: {path}")
            continue
        if path.suffix.lower() != ".csv":
            confirm = input("  ⚠ File does not have a .csv extension. Continue anyway? (y/n): ").strip().lower()
            if confirm != "y":
                continue
        return path


def load_rows(csv_path: Path):
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = [h.strip() for h in (reader.fieldnames or [])]
        missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
        if missing:
            print(f"\n✗ The CSV is missing required column(s): {', '.join(missing)}")
            print(f"  Columns found: {fieldnames}")
            sys.exit(1)

        rows = []
        idx = 0
        for raw_row in reader:
            row = {k.strip(): (v or "").strip() for k, v in raw_row.items()}
            if not row.get("Folder Path") and not row.get("Name"):
                continue  # skip fully blank lines
            idx += 1
            row["_idx"] = idx
            rows.append(row)
        return rows


# --------------------------------------------------------------------------- #
# Step 2: Format choice (multi-select)
# --------------------------------------------------------------------------- #
def prompt_format_choices():
    print("\nSelect the output formatting style(s):")
    for key, label in FORMAT_LABELS.items():
        print(f"  {key}. {label}")
    print("  (For multiple formats at once, separate with commas, e.g. 1,2 or 1,2,3)")
    while True:
        raw = input("Enter choice number(s): ").strip()
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        if not parts:
            print("  ✗ Please enter at least one number (1-3).")
            continue
        try:
            nums = sorted(set(int(p) for p in parts))
        except ValueError:
            print("  ✗ Invalid input — use digits only, comma-separated.")
            continue
        if not all(n in (1, 2, 3) for n in nums):
            print("  ✗ Choices must be 1, 2, and/or 3.")
            continue
        return nums


# --------------------------------------------------------------------------- #
# Step 3: Missing-link scan, debug log, confirm/abort, placeholder fill
# --------------------------------------------------------------------------- #
def scan_missing_links(rows, required_fields):
    missing_report = []
    for row in rows:
        missing_fields = [f for f in required_fields if not row.get(f)]
        if missing_fields:
            missing_report.append((row["_idx"], row["Folder Path"], row["Name"], missing_fields))
    return missing_report


def print_report_table(title, report_rows, reason_label="Missing"):
    print(f"\n{title}\n")
    header = f'{"#":>4}  {"Folder Path":<35} {"Name":<45} {reason_label}'
    print(header)
    print("-" * len(header))
    for idx, folder, name, detail in report_rows:
        folder_disp = (folder[:32] + "...") if len(folder) > 35 else folder
        name_disp = (name[:42] + "...") if len(name) > 45 else name
        detail_disp = ", ".join(detail) if isinstance(detail, list) else detail
        print(f"{idx:>4}  {folder_disp:<35} {name_disp:<45} {detail_disp}")


def confirm_continue_with_placeholders():
    while True:
        raw = input(
            "\nContinue and insert PLACEHOLDER links for these entries? "
            "(y = continue with placeholders / n = abort): "
        ).strip().lower()
        if raw in ("y", "n"):
            return raw == "y"
        print("  Please enter 'y' or 'n'.")


def apply_placeholders(rows, missing_report):
    """Returns a new list of rows with missing required fields filled with placeholders."""
    missing_by_idx = {idx: missing_fields for idx, _, _, missing_fields in missing_report}
    patched = []
    for row in rows:
        row = dict(row)
        for field in missing_by_idx.get(row["_idx"], []):
            if field == "Original Link":
                row["Original Link"] = PLACEHOLDER_ORIGINAL_LINK
            elif field == "Downloadable Link":
                row["Downloadable Link"] = PLACEHOLDER_DOWNLOAD_LINK
        patched.append(row)
    return patched


# --------------------------------------------------------------------------- #
# Step 4: Table-format genuine-file filtering
# --------------------------------------------------------------------------- #
def is_real_file(row) -> bool:
    return bool(REAL_FILE_PATTERN.search(row.get("Original Link", "") or ""))


def filter_for_table_format(rows):
    kept, excluded = [], []
    for row in rows:
        if is_real_file(row):
            kept.append(row)
        else:
            excluded.append(row)
    return kept, excluded


def excluded_reason(row) -> str:
    original = row.get("Original Link", "") or ""
    if any(p in original for p in NATIVE_DOC_URL_PATTERNS):
        return "Native Google Slides/Docs/Sheets link"
    if not original or original == PLACEHOLDER_ORIGINAL_LINK:
        return "No genuine file link available"
    return "Original Link is not a drive.google.com/file/d/ link"


# --------------------------------------------------------------------------- #
# Step 5: Embed-insertion triggers (formats 2 & 3 only)
# --------------------------------------------------------------------------- #
def needs_embed(row) -> bool:
    original = row.get("Original Link", "") or ""
    name = row.get("Name", "") or ""
    is_native_doc = any(p in original for p in NATIVE_DOC_URL_PATTERNS)
    is_pyq = "pyq" in name.lower()
    return is_native_doc or is_pyq


# --------------------------------------------------------------------------- #
# Step 6: Build the folder-path tree
# --------------------------------------------------------------------------- #
def build_tree(rows):
    """Returns OrderedDict[root_name -> Node] preserving first-seen order."""
    roots = OrderedDict()
    for row in rows:
        segments = [s.strip() for s in row["Folder Path"].split("/") if s.strip()]
        if not segments:
            continue
        root_name = segments[0]
        if root_name not in roots:
            roots[root_name] = Node(root_name)
        node = roots[root_name]
        for seg in segments[1:]:
            node = node.get_or_create_child(seg)
        node.entries.append(row)
    return roots


# --------------------------------------------------------------------------- #
# Step 7: Markdown / HTML rendering per entry format
# --------------------------------------------------------------------------- #
def escape_md(text: str) -> str:
    """Light escaping so names containing [ ] | don't break markdown links/tables."""
    return text.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def render_entries(entries, format_choice):
    if not entries:
        return []

    if format_choice == FORMAT_TABLE:
        # Entries reaching here have already been filtered to genuine file links
        # (see filter_for_table_format) — no embeds apply to this format.
        lines = [
            "<table>",
            "    <thead>",
            "        <tr>",
            '            <th width="80">[⤓]</th>',
            "            <th>Content Preview</th>",
            "        </tr>",
            "    </thead>",
            "    <tbody>",
        ]
        for row in entries:
            name = escape_md(row["Name"])
            original = row["Original Link"]
            download = row["Downloadable Link"]
            lines.append("        <tr>")
            lines.append(
                f'            <td><a href="{download}" class="button primary" '
                f'data-icon="arrow-down-to-square"></a></td>'
            )
            lines.append(f'            <td><a href="{original}">{name}</a></td>')
            lines.append("        </tr>")
        lines.append("    </tbody>")
        lines.append("</table>")
        return lines

    if format_choice in (FORMAT_PLAIN_ORIGINAL, FORMAT_PLAIN_DOWNLOAD):
        lines = []
        for row in entries:
            name = escape_md(row["Name"])
            link = row["Original Link"] if format_choice == FORMAT_PLAIN_ORIGINAL else row["Downloadable Link"]
            lines.append(f'\\[⤓] [{name}]({link})')
            if needs_embed(row):
                lines.append("")
                lines.append(f'{{% embed url="{row["Original Link"]}" %}}')
                lines.append("")
        return lines

    raise ValueError(f"Unknown format choice: {format_choice}")


def render_node(node: Node, depth: int, format_choice: int) -> list:
    """Recursively renders a node's entries + headings for child nodes.
    depth=1 is the root node (no heading emitted for it)."""
    lines = []

    if depth > 1:
        heading_level = depth - 1
        lines.append(f'{"#" * heading_level} {node.name}')
        lines.append("")

    entry_lines = render_entries(node.entries, format_choice)
    if entry_lines:
        lines.extend(entry_lines)
        lines.append("")

    for child in node.children.values():
        child_lines = render_node(child, depth + 1, format_choice)
        if child_lines:
            lines.extend(child_lines)

    return lines


# --------------------------------------------------------------------------- #
# Step 8: Write output files
# --------------------------------------------------------------------------- #
def write_format_output(roots: "OrderedDict[str, Node]", parent_dir: Path,
                         format_choice: int, multi_mode: bool):
    written_files = []
    for root_name, root_node in roots.items():
        has_children = bool(root_node.children)
        flatten = (not multi_mode) and (not has_children)

        if flatten:
            md_path = parent_dir / f"{root_name}.md"
        else:
            folder = parent_dir / root_name
            folder.mkdir(parents=True, exist_ok=True)
            if multi_mode:
                md_path = folder / f"{root_name}-{FORMAT_SLUGS[format_choice]}.md"
            else:
                md_path = folder / f"{root_name}.md"

        body_lines = render_node(root_node, depth=1, format_choice=format_choice)
        content = "\n".join(body_lines).rstrip() + "\n"
        md_path.write_text(content, encoding="utf-8")
        written_files.append(md_path)

    return written_files


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    print("=" * 70)
    print(" GitBook Batch Formatter — Drive CSV -> Nested Markdown Structure")
    print("=" * 70)

    csv_path = prompt_csv_path()
    rows = load_rows(csv_path)
    print(f"\n✓ Loaded {len(rows)} row(s) from {csv_path.name}")

    format_choices = prompt_format_choices()
    multi_mode = len(format_choices) > 1
    chosen_labels = ", ".join(f"{n} ({FORMAT_LABELS[n]})" for n in format_choices)
    print(f"\n✓ Selected format(s): {chosen_labels}")
    if multi_mode:
        print("  Multi-format mode: each root folder will always get its own "
              "directory holding one file per format.")

    # Union of required fields across all selected formats.
    required_fields = sorted(set(f for n in format_choices for f in FORMAT_REQUIRED_FIELDS[n]))
    missing_report = scan_missing_links(rows, required_fields)
    if missing_report:
        print_report_table(
            f"⚠ {len(missing_report)} entr{'y is' if len(missing_report) == 1 else 'ies are'} "
            f"missing a link required by the selected format(s):",
            missing_report,
        )
        if not confirm_continue_with_placeholders():
            print("\n✗ Aborted by user. No files were written.")
            sys.exit(0)
        rows = apply_placeholders(rows, missing_report)
        print(f"\n✓ Placeholder links inserted for {len(missing_report)} entr"
              f"{'y' if len(missing_report) == 1 else 'ies'}.")
    else:
        print("\n✓ All entries have the required link(s) for the selected format(s).")

    parent_dir = csv_path.parent / csv_path.stem
    parent_dir.mkdir(parents=True, exist_ok=True)

    all_written = []
    table_excluded_total = 0

    for format_choice in format_choices:
        print(f"\n{'-' * 70}\nBuilding format {format_choice}: {FORMAT_LABELS[format_choice]}")

        if format_choice == FORMAT_TABLE:
            rows_for_format, excluded = filter_for_table_format(rows)
            if excluded:
                report_rows = [
                    (r["_idx"], r["Folder Path"], r["Name"], excluded_reason(r))
                    for r in excluded
                ]
                print_report_table(
                    f"⚠ {len(excluded)} entr{'y' if len(excluded) == 1 else 'ies'} excluded from "
                    f"the Table format (no genuine downloadable file link):",
                    report_rows,
                    reason_label="Reason",
                )
                table_excluded_total += len(excluded)
        else:
            rows_for_format = rows

        roots = build_tree(rows_for_format)
        written = write_format_output(roots, parent_dir, format_choice, multi_mode)
        all_written.extend(written)
        print(f"✓ {len(written)} file(s) written for this format.")

    print(f"\n{'=' * 70}")
    print(f"✓ Done. Output written to: {parent_dir}")
    print(f"  {len(all_written)} markdown file(s) total:")
    for f in sorted(set(all_written)):
        print(f"    - {f.relative_to(parent_dir.parent)}")

    if missing_report:
        print(
            f"\n⚠ Reminder: entries with PLACEHOLDER links need updating "
            f"(grep for 'PLACEHOLDER' or 'placeholder.invalid') before pushing."
        )
    if table_excluded_total:
        print(
            f"⚠ Reminder: {table_excluded_total} entrie(s) were excluded from the "
            f"Table format because they aren't genuine downloadable files — they "
            f"may still appear in any plain-format output you generated, with an "
            f"embed block in their place."
        )


if __name__ == "__main__":
    main()
