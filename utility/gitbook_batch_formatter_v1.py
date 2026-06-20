#!/usr/bin/env python3
"""
GitBook Batch Formatter
========================
Transforms a Google Drive export CSV (columns: Folder Path, Name, Original Link,
Downloadable Link) into a nested folder/markdown structure ready to be committed
to a GitBook-synced GitHub repository.

USAGE:
    python3 gitbook_batch_formatter_v1.py

The script will interactively ask for:
    1. The path to the source .csv file
    2. The output formatting style to apply (numbered choice)

OUTPUT STRUCTURE:
    A new directory named after the CSV file (without extension) is created
    next to the CSV. Inside it, one folder per ROOT folder-path segment is
    created, each containing a single <ROOT>.md file. Nested folder-path
    segments become incrementing markdown headings inside that one file:

        BCU641                    -> BCU641/BCU641.md            (no heading, flat list)
        CSE603/CSE603-M1          -> CSE603/CSE603.md   -> "# CSE603-M1"
        CSE604/CSE604-M4/SCALER-TOPICS
                                   -> CSE604/CSE604.md   -> "# CSE604-M4" -> "## SCALER-TOPICS"

    Heading level = (path depth - 1), heading text = literal folder segment
    name (hyphens preserved, per user confirmation).
"""

import csv
import os
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

# Fields each format strictly requires to render correctly.
FORMAT_REQUIRED_FIELDS = {
    FORMAT_TABLE: ["Original Link", "Downloadable Link"],
    FORMAT_PLAIN_ORIGINAL: ["Original Link"],
    FORMAT_PLAIN_DOWNLOAD: ["Downloadable Link"],
}


# --------------------------------------------------------------------------- #
# Tree node representing one folder-path segment
# --------------------------------------------------------------------------- #
class Node:
    __slots__ = ("name", "entries", "children")

    def __init__(self, name):
        self.name = name            # literal folder segment name (heading text)
        self.entries = []           # list of row dicts attached directly at this path
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
        # strip accidental surrounding quotes (common when paths are dragged in)
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
        for raw_row in reader:
            row = {k.strip(): (v or "").strip() for k, v in raw_row.items()}
            if not row.get("Folder Path") and not row.get("Name"):
                continue  # skip fully blank lines
            rows.append(row)
        return rows


# --------------------------------------------------------------------------- #
# Step 2: Format choice
# --------------------------------------------------------------------------- #
def prompt_format_choice():
    print("\nSelect the output formatting style:")
    for key, label in FORMAT_LABELS.items():
        print(f"  {key}. {label}")
    while True:
        raw = input("Enter choice number: ").strip()
        if raw in ("1", "2", "3"):
            return int(raw)
        print("  ✗ Please enter 1, 2, or 3.")


# --------------------------------------------------------------------------- #
# Step 3: Missing-link scan, debug log, confirm/abort
# --------------------------------------------------------------------------- #
def scan_missing_links(rows, format_choice):
    required_fields = FORMAT_REQUIRED_FIELDS[format_choice]
    missing_report = []
    for idx, row in enumerate(rows, start=1):
        missing_fields = [f for f in required_fields if not row.get(f)]
        if missing_fields:
            missing_report.append((idx, row["Folder Path"], row["Name"], missing_fields))
    return missing_report


def print_missing_report(missing_report):
    print(f"\n⚠ {len(missing_report)} entr{'y is' if len(missing_report) == 1 else 'ies are'} "
          f"missing a required link for the selected format:\n")
    header = f'{"#":>4}  {"Folder Path":<35} {"Name":<45} {"Missing"}'
    print(header)
    print("-" * len(header))
    for idx, folder, name, missing_fields in missing_report:
        folder_disp = (folder[:32] + "...") if len(folder) > 35 else folder
        name_disp = (name[:42] + "...") if len(name) > 45 else name
        print(f"{idx:>4}  {folder_disp:<35} {name_disp:<45} {', '.join(missing_fields)}")


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
    """Mutates a copy of rows, filling missing required fields with placeholder URLs."""
    missing_by_idx = {idx: missing_fields for idx, _, _, missing_fields in missing_report}
    patched = []
    for idx, row in enumerate(rows, start=1):
        row = dict(row)  # copy
        for field in missing_by_idx.get(idx, []):
            if field == "Original Link":
                row["Original Link"] = PLACEHOLDER_ORIGINAL_LINK
            elif field == "Downloadable Link":
                row["Downloadable Link"] = PLACEHOLDER_DOWNLOAD_LINK
        patched.append(row)
    return patched


# --------------------------------------------------------------------------- #
# Step 4: Build the folder-path tree
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
# Step 5: Markdown / HTML rendering per entry format
# --------------------------------------------------------------------------- #
def escape_md(text: str) -> str:
    """Light escaping so names containing [ ] | don't break markdown links/tables."""
    return text.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def render_entries(entries, format_choice):
    if not entries:
        return []

    if format_choice == FORMAT_TABLE:
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

    if format_choice == FORMAT_PLAIN_ORIGINAL:
        return [
            f'\\[⤓] [{escape_md(row["Name"])}]({row["Original Link"]})'
            for row in entries
        ]

    if format_choice == FORMAT_PLAIN_DOWNLOAD:
        return [
            f'\\[⤓] [{escape_md(row["Name"])}]({row["Downloadable Link"]})'
            for row in entries
        ]

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
# Step 6: Write output files
# --------------------------------------------------------------------------- #
def write_output(roots: "OrderedDict[str, Node]", csv_path: Path, format_choice: int):
    parent_dir = csv_path.parent / csv_path.stem
    parent_dir.mkdir(parents=True, exist_ok=True)

    written_files = []
    for root_name, root_node in roots.items():
        folder = parent_dir / root_name
        folder.mkdir(parents=True, exist_ok=True)
        md_path = folder / f"{root_name}.md"

        body_lines = render_node(root_node, depth=1, format_choice=format_choice)
        content = "\n".join(body_lines).rstrip() + "\n"

        md_path.write_text(content, encoding="utf-8")
        written_files.append(md_path)

    return parent_dir, written_files


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

    format_choice = prompt_format_choice()
    print(f"\n✓ Selected format: {FORMAT_LABELS[format_choice]}")

    missing_report = scan_missing_links(rows, format_choice)
    if missing_report:
        print_missing_report(missing_report)
        if not confirm_continue_with_placeholders():
            print("\n✗ Aborted by user. No files were written.")
            sys.exit(0)
        rows = apply_placeholders(rows, missing_report)
        print(f"\n✓ Placeholder links inserted for {len(missing_report)} entr"
              f"{'y' if len(missing_report) == 1 else 'ies'}.")
    else:
        print("\n✓ All entries have the required link(s) for the selected format.")

    roots = build_tree(rows)
    parent_dir, written_files = write_output(roots, csv_path, format_choice)

    print(f"\n✓ Done. Output written to: {parent_dir}")
    print(f"  {len(written_files)} markdown file(s) created:")
    for f in written_files:
        print(f"    - {f.relative_to(parent_dir.parent)}")

    if missing_report:
        print(
            f"\n⚠ Reminder: {len(missing_report)} entries contain PLACEHOLDER links "
            f"(grep for 'PLACEHOLDER' or 'placeholder.invalid') — update these "
            f"before pushing to GitHub/GitBook."
        )


if __name__ == "__main__":
    main()
