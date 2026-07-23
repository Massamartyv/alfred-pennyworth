# Capability Matrix

Generates a markdown capability matrix for the Alfred operating system agent stack. Scans three layers and prints three tables showing tool grants, models and cadence per agent.

## What it scans

| Layer | Source | Table produced |
|---|---|---|
| Scheduled agents | `Agents/System/*.md`, `Agents/Orchestration/*.md` | Scheduled Agents |
| Native crew subagents | `~/.claude/agents/*.md` | Native Crew Subagents |
| Scheduled-task registrations | `~/.claude/scheduled-tasks/*/SKILL.md`, cross-checked against a live scheduler dump | Scheduled-Task Registrations |

Frontmatter is parsed with simple line parsing. No third-party dependencies.

## Live scheduler cross-check

A SKILL.md directory on disk is not proof of a live registration: deleting a task via the scheduled-tasks MCP (`delete_scheduled_task`) removes the scheduler entry but deliberately leaves SKILL.md on disk so the prompt can be recovered. The script therefore never trusts filesystem presence alone.

The script cannot call MCP tools itself. Save the verbatim JSON output of the `mcp__scheduled-tasks__list_scheduled_tasks` tool to a file (`.working/capability-matrix/live-tasks.json` by convention) and pass it with `--live-tasks`. Each row's Status column is then marked:

| Status | Meaning |
|---|---|
| `live` | Registered with the scheduler and enabled |
| `live (disabled)` | Registered with the scheduler but disabled |
| `deregistered` | SKILL.md on disk only; no scheduler entry (recovery artifact) |
| `unverified` | No `--live-tasks` dump supplied to this run |

If the dump lists a task with no SKILL.md directory on disk, the script appends a note naming it below the table. A missing or malformed dump file is a hard error -- a bad dump would mislabel every row.

## How to run

Print to stdout:

```
python3 "Automations/Capability Matrix/capability-matrix.py" --live-tasks .working/capability-matrix/live-tasks.json
```

Write directly into `Agents/_index.md` (replaces content between the two HTML markers):

```
python3 "Automations/Capability Matrix/capability-matrix.py" --live-tasks .working/capability-matrix/live-tasks.json --write
```

Run from the Alfred Pennyworth project root (`~/Alfred Pennyworth/`). The `--live-tasks` path may be relative to wherever the script is invoked; the scanned sources and `Agents/_index.md` resolve to absolute paths under `~/Alfred Pennyworth/` regardless.

## When to run

The heartbeat agent regenerates the matrix on the first of each month as part of the monthly maintenance pass, dumping the live scheduler first so the cross-check stays current. It is also safe to run manually at any time -- the `--write` flag is idempotent.

## Markers in _index.md

The `--write` flag looks for these two HTML comment markers in `Agents/_index.md`:

```
<!-- capability-matrix:start -->
<!-- capability-matrix:end -->
```

Everything between them is replaced. Everything outside them is untouched. If either marker is missing the script exits with an error rather than corrupting the file.
