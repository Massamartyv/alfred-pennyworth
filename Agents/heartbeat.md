# Heartbeat

The standing rhythm of Alfred operating system. Cadenced maintenance and opportunistic upkeep that keep the system aligned with the present moment without prompting.

---

## Standing autonomous tasks

| Cadence | Task | Details |
|---|---|---|
| Daily, evening | Watchtower sweep | Personal Notion sweep for overdue tasks, stale priorities, missed deadlines and stagnating projects. Alerts via iMessage. Agent: `Agents/Orchestration/watchtower.md`. |
| Weekly, Monday morning | Portfolio briefing | **Retired 2026-08-12 by operator ruling.** Designed 2026-04-23, never built, deferred twice. The Observatory replaces it: a living surface that is always current answers the need better than a document generated weekly and read once. Do not re-register `penny-one` and do not schedule a briefing under any name. See the mission record, The Observatory, in personal Projects. |
| First of every month | Media and Library scan | Query Notion Media and Literature for new five-star entries. Write thematic DNA onto each new entry's Notion page -- no local file writes. `culture.md` points at the live query. |
| First of every month | Context file audit | Review all sphere files for stale information. Flag anything that needs updating. |
| First of each quarter | Sphere Index review | Review every entry in the Sphere Index. Flag any state that may have shifted. Surface the question rather than assuming the answer. |
| First of each quarter | Sphere Manager alignment check | Verify that the sphere file structure still mirrors the active spheres. Flag any sphere that has become active enough to graduate to its own file. |
| First of each quarter | Restore drill | Fire-drill the Genesis Protocol per `Manual/restore-drill.md`. Score each step, file the report as an Alfred Logs entry (Log Type Audit/Analysis) related to the Alfred operating system project, fix the Manual the same day. |
| First of every month | Scheduler audit | Compare the scheduled-task registry against this table. Re-register anything missing; reconcile anything drifted. Watchtower also checks handoff receipts daily. **Exception, set 2026-07-23:** `context-audit`, `media-scanner` and `sphere-review` are deliberately absent from the registry -- interactive report-and-ask agents that run inside heartbeat sessions only, per each definition's Execution Model section; do not re-register them. `penny-one` is also deliberately absent -- gated on the briefing redesign; do not re-register it until that gate clears. `pattern-memo` was retired outright 2026-08-11 by Domesday ruling -- agent definition deleted; its scheduled-task directory survives as a recovery blueprint only. |
| First of every month | Capability matrix regeneration | Dump the live scheduler first: call the `mcp__scheduled-tasks__list_scheduled_tasks` tool and save its verbatim JSON output to `.working/capability-matrix/live-tasks.json`. Then from the project root run `python3 "Automations/Capability Matrix/capability-matrix.py" --live-tasks .working/capability-matrix/live-tasks.json --write`. The dump lets the Scheduled-Task Registrations table in `Agents/_index.md` distinguish live scheduler entries from deregistered SKILL.md recovery artifacts (`--live-tasks` added 2026-07-23); without it every row is marked unverified. |
| First of every month | Working directory sweep | Review the dry-run of `Automations/Guards/working-sweep.sh`, then run with `--execute`. 30-day rule; `session-buffer/` always held; open handoffs held. |
| First of each quarter | Memory consolidation | Run the consolidate-memory pass – merge duplicate memories, fix stale facts, prune the index. |
| First of each quarter | Appraisal review | Via the prospect-appraiser skill: surface active-pipeline CRM cards (Prospect, Lead, Discovery Session) whose Appraised date predates the quarter and propose a sweep; reconcile any Clientele conversion still carrying its pre-signing appraisal against actuals. Propose, then run on approval -- never unbidden. |
| First of every month | Achievements current-value sync | Refresh Current Value on Achievements entries whose source is another database: films from Media, books from Literature, bucket-list count from Bucket List, lift totals from the Fitness Journal, monthly revenue from the venture ledgers. Values move toward Notion-derived truth only; targets and wagers never change in this pass. |
| First of each quarter | Achievements quarterly triage | Advance the This Quarter view's date filter to the new quarter end. Review every goal whose Achieve By has passed: retime with the operator, mark Done or archive with a reason in the Wager. Confirm every open goal still has an Achieve By and a Wager -- the specificity gate applied on cadence. |
| First of every month | Drift audit | Scan tracked markdown for state-shaped blocks outside allowed paths (shared pattern file `Automations/Guards/state-patterns.grep`). Verify cache stamp and buffer hygiene. Confirm Alfred Logs continuity for the prior month. Agent: `Agents/System/drift-audit.md`. |
| First of every month | Credential expiry sweep | Read every `*_EXPIRES` variable in `.env`. Any credential inside 21 days of expiry is flagged to the operator via iMessage with its rotation path. Any credential whose matching `*_ACCOUNT` reads `personal` while sitting in a venture section is flagged as a provenance mismatch awaiting rotation to the venture account. |
| First of each quarter | Robyn trademark watch | Check USPTO TSDR status of Serial 98514837 (Feazel ROBYN, voice AI for sales in home services) and Serial 79387123 (Robin AI, Classes 9 and 42). Flag registration issuance, ownership transfer, or any enforcement signal to the operator via iMessage. Set 2026-08-13 by the retain-Robyn ruling on The Answering Machine; the ruling reopens if either mark moves. |
| Weekly, Sunday 09:00 | Weekly review instantiation | Scheduled task `weekly-review-open` creates the week's Weekly Review entry in personal Reflections from the New Weekly Review template, writes the ONE Thing handoff at the top and nudges via iMessage. The operator works the review Sunday night, 90 minutes, before midnight. Ruled 2026-09-02; Decision Log "Adopt Alfred-Instantiated Review Cadence". |
| Weekly, Sunday 10:00 | Whetstone retrospective | Scheduled task `whetstone-retrospective`. Runs `Automations/Whetstone/monitor-check.sh`, then the full Assay (`Automations/The Assay/the-assay.sh`), alerts via iMessage on any monitor FAIL or failed or unscoreable suite, then sends the weekly ship-or-report note with the Assay pass-rate curve. Receipt via `Automations/Guards/agent-receipt.sh`. Ratified 2026-09-08; the Assay added 2026-09-10. Read-only on Notion; Tier 0 on everything it measures. |
| First of every month, 08:00 | Monthly review instantiation | Scheduled task `monthly-review-open` creates the Monthly Review entry from its template with the pattern memo drafted inline into Movement 0 -- no standing pattern-memo agent, per the 2026-08-11 retirement. On 1 January, 1 April, 1 July and 1 October it also creates the Quarterly Review entry with its handoff; monthly then quarterly run as one sitting. Ruled 2026-09-02. |

Month-rollover detection: the first session of each month is detected by the SessionStart hook, which injects the heartbeat reminder on month rollover. After the run completes, write the current `YYYY-MM` to `.claude/cache/last-heartbeat`.

---

## Opportunistic maintenance

These run during any session where the trigger surfaces.

- When a conversation reveals outdated information in a sphere file, flag it immediately and offer to update in the same session.
- When a conversation introduces a new domain or priority not yet reflected, flag the gap and offer to create or update the relevant file.
- When a pattern of repeated clarifications suggests a sphere file is incomplete, flag the pattern and suggest what should be added.
- When a decision changes active state, update the Sphere Index immediately and create any new files needed.

---

*Last updated: 2026-09-10 – The Assay: the Whetstone retrospective row added, carrying the weekly Assay run. Previously 2026-09-02 – Review cadence: weekly and monthly review instantiation registered as scheduled tasks; the monthly pattern memo drafts inline, the quarterly joins the monthly on quarter starts. Prior: 2026-08-11 Domesday.*
