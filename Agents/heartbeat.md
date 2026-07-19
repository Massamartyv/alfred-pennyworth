# Heartbeat

The standing rhythm of Alfred operating system. Cadenced maintenance and opportunistic upkeep that keep the system aligned with the present moment without prompting.

---

## Standing autonomous tasks

| Cadence | Task | Details |
|---|---|---|
| Daily, evening | Watchtower sweep | Personal Notion sweep for overdue tasks, stale priorities, missed deadlines and stagnating projects. Alerts via iMessage. Agent: `Agents/Orchestration/watchtower.md`. |
| Weekly, Monday morning | Portfolio briefing | Aggregates tasks, projects, content pipeline and Five Points revenue into one briefing. Delivered via iMessage. Scheduled task: `penny-one` -- distinct from the on-demand syndication agent `pennyone` at `Agents/Orchestration/pennyone.md`. |
| First of every month | Media and Library scan | Query Notion Media and Literature for new five-star entries. Write thematic DNA onto each new entry's Notion page -- no local file writes. `culture.md` points at the live query. |
| First of every month | Context file audit | Review all sphere files for stale information. Flag anything that needs updating. |
| First of every month | Pattern memo | Synthesise three patterns from the prior month's Notion activity -- Reflections, Tasks, Projects, Content, Achievements, Alfred Logs -- plus session memory. Stage as the opening section of the new Monthly Review entry in Reflections. Agent: `Agents/Orchestration/pattern-memo.md`. |
| First of each quarter | Sphere Index review | Review every entry in the Sphere Index. Flag any state that may have shifted. Surface the question rather than assuming the answer. |
| First of each quarter | Sphere Manager alignment check | Verify that the sphere file structure still mirrors the active spheres. Flag any sphere that has become active enough to graduate to its own file. |
| First of each quarter | Restore drill | Fire-drill the Genesis Protocol per `Manual/restore-drill.md`. Score each step, file the report as an Alfred Logs entry (Log Type Audit/Analysis) related to the Alfred operating system project, fix the Manual the same day. |
| First of every month | Scheduler audit | Compare the scheduled-task registry against this table. Re-register anything missing; reconcile anything drifted. Watchtower also checks handoff receipts daily. |
| First of every month | Working directory sweep | Review the dry-run of `Automations/Guards/working-sweep.sh`, then run with `--execute`. 30-day rule; `session-buffer/` always held; open handoffs held. |
| First of each quarter | Memory consolidation | Run the consolidate-memory pass – merge duplicate memories, fix stale facts, prune the index. |
| First of each quarter | Appraisal review | Via the prospect-appraiser skill: surface active-pipeline CRM cards (Prospect, Lead, Discovery Session) whose Appraised date predates the quarter and propose a sweep; reconcile any Clientele conversion still carrying its pre-signing appraisal against actuals. Propose, then run on approval -- never unbidden. |
| First of every month | Drift audit | Scan tracked markdown for state-shaped blocks outside allowed paths (shared pattern file `Automations/Guards/state-patterns.grep`). Verify cache stamp and buffer hygiene. Confirm Alfred Logs continuity for the prior month. Agent: `Agents/System/drift-audit.md`. |
| First of every month | Credential expiry sweep | Read every `*_EXPIRES` variable in `.env`. Any credential inside 21 days of expiry is flagged to the operator via iMessage with its rotation path. Any credential whose matching `*_ACCOUNT` reads `personal` while sitting in a venture section is flagged as a provenance mismatch awaiting rotation to the venture account. |

Month-rollover detection: the first session of each month is detected by the SessionStart hook, which injects the heartbeat reminder on month rollover. After the run completes, write the current `YYYY-MM` to `.claude/cache/last-heartbeat`.

---

## Opportunistic maintenance

These run during any session where the trigger surfaces.

- When a conversation reveals outdated information in a sphere file, flag it immediately and offer to update in the same session.
- When a conversation introduces a new domain or priority not yet reflected, flag the gap and offer to create or update the relevant file.
- When a pattern of repeated clarifications suggests a sphere file is incomplete, flag the pattern and suggest what should be added.
- When a decision changes active state, update the Sphere Index immediately and create any new files needed.

---

*Last updated: 2026-07-11 – Appraisal review row added: quarterly staleness sweep and actuals reconciliation via prospect-appraiser.*
