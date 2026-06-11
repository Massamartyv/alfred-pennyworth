# Capability Matrix

Generates a markdown capability matrix for the Alfred operating system agent stack. Scans three layers and prints three tables showing tool grants, models and cadence per agent.

## What it scans

| Layer | Source | Table produced |
|---|---|---|
| Scheduled agents | `Agents/System/*.md`, `Agents/Orchestration/*.md` | Scheduled Agents |
| Native crew subagents | `~/.claude/agents/*.md` | Native Crew Subagents |
| Scheduled-task registrations | `~/.claude/scheduled-tasks/*/SKILL.md` | Scheduled-Task Registrations |

Frontmatter is parsed with simple line parsing. No third-party dependencies.

## How to run

Print to stdout:

```
python3 "Automations/Capability Matrix/capability-matrix.py"
```

Write directly into `Agents/_index.md` (replaces content between the two HTML markers):

```
python3 "Automations/Capability Matrix/capability-matrix.py" --write
```

Run from the Alfred Pennyworth project root (`~/Alfred Pennyworth/`). Relative paths in the script resolve from that root.

## When to run

The heartbeat agent regenerates the matrix on the first of each month as part of the monthly maintenance pass. It is also safe to run manually at any time -- the `--write` flag is idempotent.

## Markers in _index.md

The `--write` flag looks for these two HTML comment markers in `Agents/_index.md`:

```
<!-- capability-matrix:start -->
<!-- capability-matrix:end -->
```

Everything between them is replaced. Everything outside them is untouched. If either marker is missing the script exits with an error rather than corrupting the file.
