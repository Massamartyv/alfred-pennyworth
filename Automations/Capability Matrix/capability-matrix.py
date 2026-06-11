#!/usr/bin/env python3
"""
capability-matrix.py

Scans three agent layers in the Alfred operating system and prints a capability
matrix as a single markdown document with three tables:

  1. Scheduled agents        (Agents/System/*.md, Agents/Orchestration/*.md)
  2. Native crew subagents   (.claude/agents/*.md)
  3. Scheduled-task registrations (~/.claude/scheduled-tasks/*/SKILL.md)

Accepts an optional --write flag that replaces the content between
  <!-- capability-matrix:start -->
and
  <!-- capability-matrix:end -->
in Agents/_index.md with the current output.

No third-party dependencies. Requires Python 3.6+.
"""

import argparse
import glob
import os
import sys
import textwrap


# ---------------------------------------------------------------------------
# Path constants
# ---------------------------------------------------------------------------

ALFRED_ROOT = os.path.expanduser("~/Alfred Pennyworth")
AGENTS_ROOT = os.path.join(ALFRED_ROOT, "Agents")
CLAUDE_AGENTS = os.path.join(ALFRED_ROOT, ".claude", "agents")
SCHEDULED_TASKS = os.path.expanduser("~/.claude/scheduled-tasks")
INDEX_FILE = os.path.join(AGENTS_ROOT, "_index.md")

MARKER_START = "<!-- capability-matrix:start -->"
MARKER_END = "<!-- capability-matrix:end -->"


# ---------------------------------------------------------------------------
# Frontmatter parser
# ---------------------------------------------------------------------------

def parse_frontmatter(path):
    """
    Parse YAML-style frontmatter delimited by --- lines.
    Returns a dict of key: value strings. Multi-word values are stripped of
    surrounding quotes. Does not depend on PyYAML.
    """
    data = {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        return data

    if not lines or lines[0].strip() != "---":
        return data

    in_front = False
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            if not in_front:
                in_front = True
                break
        # parse key: value
        if ":" in stripped:
            key, _, rest = stripped.partition(":")
            value = rest.strip().strip('"').strip("'")
            data[key.strip()] = value
    return data


# ---------------------------------------------------------------------------
# Tool summary helper
# ---------------------------------------------------------------------------

def tool_summary(tools_str, max_names=3):
    """
    Given a comma-separated tools string, return 'N tools (a, b, c…)'.
    """
    if not tools_str:
        return "none"
    parts = [t.strip() for t in tools_str.split(",") if t.strip()]
    count = len(parts)
    if count == 0:
        return "none"
    preview = parts[:max_names]
    label = ", ".join(preview)
    if count > max_names:
        label += "…"
    return f"{count} ({label})"


# ---------------------------------------------------------------------------
# Scanners
# ---------------------------------------------------------------------------

def scan_scheduled_agents():
    """
    Scan Agents/System/*.md and Agents/Orchestration/*.md.
    Returns a list of dicts with keys: name, crew, model, cadence, tool_summary.
    """
    rows = []
    patterns = [
        os.path.join(AGENTS_ROOT, "System", "*.md"),
        os.path.join(AGENTS_ROOT, "Orchestration", "*.md"),
    ]
    paths = []
    for pattern in patterns:
        paths.extend(sorted(glob.glob(pattern)))

    for path in paths:
        filename = os.path.basename(path)
        if filename.startswith("_"):
            continue
        fm = parse_frontmatter(path)
        if not fm:
            continue
        rows.append({
            "name": fm.get("name", filename),
            "crew": fm.get("crew", "–"),
            "model": fm.get("model", "–"),
            "cadence": fm.get("cadence", "–"),
            "tools": tool_summary(fm.get("tools", "")),
            "type": fm.get("type", "–"),
        })
    return rows


def scan_native_subagents():
    """
    Scan .claude/agents/*.md.
    Returns a list of dicts with keys: name, model, tools, disallowed.
    """
    rows = []
    if not os.path.isdir(CLAUDE_AGENTS):
        return rows
    for path in sorted(glob.glob(os.path.join(CLAUDE_AGENTS, "*.md"))):
        filename = os.path.basename(path)
        if filename.startswith("_"):
            continue
        fm = parse_frontmatter(path)
        if not fm:
            continue
        rows.append({
            "name": fm.get("name", filename),
            "model": fm.get("model", "–"),
            "tools": tool_summary(fm.get("tools", "")),
            "disallowed": fm.get("disallowed-tools", "none") or "none",
        })
    return rows


def scan_scheduled_tasks():
    """
    Scan ~/.claude/scheduled-tasks/*/SKILL.md.
    Returns a list of dicts with keys: name, allowed_tools.
    """
    rows = []
    if not os.path.isdir(SCHEDULED_TASKS):
        return rows
    for task_dir in sorted(os.listdir(SCHEDULED_TASKS)):
        skill_path = os.path.join(SCHEDULED_TASKS, task_dir, "SKILL.md")
        if not os.path.isfile(skill_path):
            continue
        fm = parse_frontmatter(skill_path)
        rows.append({
            "name": fm.get("name", task_dir),
            "allowed_tools": tool_summary(fm.get("allowed-tools", "")),
            "description": fm.get("description", ""),
        })
    return rows


# ---------------------------------------------------------------------------
# Table renderer
# ---------------------------------------------------------------------------

def md_table(headers, rows):
    """
    Render a markdown table from a list of headers and a list of row dicts.
    Each row dict must have a key matching each header (lowercased, spaces to _).
    Rows is a list of lists aligned to headers.
    """
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def fmt_row(cells):
        return "| " + " | ".join(str(c).ljust(col_widths[i]) for i, c in enumerate(cells)) + " |"

    separator = "| " + " | ".join("-" * w for w in col_widths) + " |"

    lines = [fmt_row(headers), separator]
    for row in rows:
        lines.append(fmt_row(row))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Matrix builder
# ---------------------------------------------------------------------------

def build_matrix():
    scheduled = scan_scheduled_agents()
    native = scan_native_subagents()
    tasks = scan_scheduled_tasks()

    sections = []

    # Table 1: Scheduled agents
    sections.append("### Scheduled Agents\n")
    sections.append("Defined under `Agents/System/` and `Agents/Orchestration/`.\n")
    if scheduled:
        headers = ["Name", "Type", "Crew", "Model", "Cadence", "Tools"]
        table_rows = [
            [r["name"], r["type"], r["crew"], r["model"], r["cadence"], r["tools"]]
            for r in scheduled
        ]
        sections.append(md_table(headers, table_rows))
    else:
        sections.append("_No scheduled agent definitions found._")
    sections.append("")

    # Table 2: Native crew subagents
    sections.append("### Native Crew Subagents\n")
    sections.append("Defined under `.claude/agents/` at the project root. Dispatched in-session via the Task tool.\n")
    if native:
        headers = ["Name", "Model", "Tools", "Disallowed Tools"]
        table_rows = [
            [r["name"], r["model"], r["tools"], r["disallowed"]]
            for r in native
        ]
        sections.append(md_table(headers, table_rows))
    else:
        sections.append("_No native subagent definitions found._")
    sections.append("")

    # Table 3: Scheduled-task registrations
    sections.append("### Scheduled-Task Registrations\n")
    sections.append("Registered under `~/.claude/scheduled-tasks/`. These are the live scheduler entries.\n")
    if tasks:
        headers = ["Name", "Allowed Tools", "Description"]
        table_rows = [
            [r["name"], r["allowed_tools"], textwrap.shorten(r["description"], width=72, placeholder="…")]
            for r in tasks
        ]
        sections.append(md_table(headers, table_rows))
    else:
        sections.append("_No scheduled-task registrations found._")
    sections.append("")

    # Row counts note
    sections.append(
        f"_Generated automatically. "
        f"Scheduled agents: {len(scheduled)}. "
        f"Native subagents: {len(native)}. "
        f"Scheduled-task registrations: {len(tasks)}._"
    )

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# --write flag handler
# ---------------------------------------------------------------------------

def write_to_index(matrix_content):
    """
    Replace content between MARKER_START and MARKER_END in _index.md
    with the generated matrix. Raises on any file error.
    """
    if not os.path.isfile(INDEX_FILE):
        print(f"ERROR: index file not found at {INDEX_FILE}", file=sys.stderr)
        sys.exit(1)

    with open(INDEX_FILE, "r", encoding="utf-8") as fh:
        original = fh.read()

    if MARKER_START not in original:
        print(
            f"ERROR: marker '{MARKER_START}' not found in _index.md. "
            "Add the ## Capability Matrix section with start/end markers first.",
            file=sys.stderr,
        )
        sys.exit(1)

    if MARKER_END not in original:
        print(
            f"ERROR: marker '{MARKER_END}' not found in _index.md.",
            file=sys.stderr,
        )
        sys.exit(1)

    before = original[: original.index(MARKER_START) + len(MARKER_START)]
    after = original[original.index(MARKER_END):]

    replacement = f"\n\n{matrix_content}\n\n"
    updated = before + replacement + after

    with open(INDEX_FILE, "w", encoding="utf-8") as fh:
        fh.write(updated)

    print(f"Wrote capability matrix to {INDEX_FILE}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate the Alfred operating system capability matrix."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Replace the capability-matrix block in Agents/_index.md with current output.",
    )
    args = parser.parse_args()

    matrix = build_matrix()

    if args.write:
        write_to_index(matrix)
    else:
        print(matrix)


if __name__ == "__main__":
    main()
