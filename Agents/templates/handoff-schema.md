---
name: handoff-schema
type: template
schema_version: 1
---

# Handoff Schema Template

The canonical handoff document. Every dispatched agent writes this as the last action of its run. Replaces the loose Report Format that previously lived in `Agents/_index.md`.

## When this template applies

Required output for every agent run. No exceptions. Whether the agent succeeded, partially completed or was blocked, the handoff is the artefact that closes the run.

## Authoring rules

- Mandatory for every agent run, regardless of outcome
- Written as the agent's final action before exit
- Stored at `.working/{agent-name}/handoff.md` for the active run
- Persisted into the mission record on completion for portfolio-tracked missions
- Status field is one of: `complete`, `partial`, `blocked`
- Severity values are one of: `blocking`, `follow-up`, `observation`
- Procedural compliance values are one of: `followed`, `deviated`, `not applicable`
- Assertion outcomes are one of: `satisfied`, `partially-satisfied`, `not-attempted`

If the agent deviated from a procedure, the deviation must include the reason inline.

## Consumption

- Alfred reads the handoff before dispatching the next agent
- Reviewers read the handoff as input to their review
- The orchestrator reads the handoff at every milestone boundary
- The operator reads the handoff at the Critique gate

## Retroactivity

Existing agents – `context-audit`, `media-scanner`, `sphere-review`, `penny-one`, `watchtower` – are retrofitted during each agent's next definition update. No stop-the-world rewrite.

---

## Template

Copy the block below into `.working/{agent-name}/handoff.md` and fill in.

```markdown
---
agent: {agent-name}
mission: {mission-name or 'standalone'}
started: {ISO 8601 timestamp}
completed: {ISO 8601 timestamp}
status: complete | partial | blocked
---

## Completed
- {what was actually done, with evidence}

## Undone
- {what was scoped but not finished, with reason}

## Commands Run
- `{command}` – exit {code} – {one-line outcome}

## Issues Discovered
- {issue} – severity: blocking | follow-up | observation

## Procedural Compliance
- {procedure name} – followed | deviated | not applicable
- if deviated: {why}

## Assertions Touched
- {assertion-id} – satisfied | partially-satisfied | not-attempted
```

If a section has no content, write a single line: `None.` Do not omit the section header.

---

## Worked example

A successful run of the `context-audit` agent against a single venture:

```markdown
---
agent: context-audit
mission: standalone
started: 2026-06-01T14:00:00Z
completed: 2026-06-01T14:18:00Z
status: complete
---

## Completed
- Scanned 47 context files under Context/Spheres/. Findings written to .working/context-audit/findings.md.
- Surfaced three stale entries: fitness phase date in body.md, content priority in global CLAUDE.md, ZERNIO key status in pennyone references.

## Undone
- None.

## Commands Run
- `find Context/Spheres -name "*.md" -type f` – exit 0 – 47 files
- `grep -rn "fitness phase" Context/` – exit 0 – 3 matches
- `grep -rn "ZERNIO" Integrations/` – exit 0 – 8 matches

## Issues Discovered
- fitness phase date references "April 1 – September 30" but current state snapshot is dated 2026-05-05; verify still accurate – severity: follow-up
- ZERNIO scaffold references "awaiting key" in two places, may be stale if account is now provisioned – severity: follow-up

## Procedural Compliance
- 24-hour pre-check on .working/context-audit/ – followed
- Scope limited to Context/ directory – followed

## Assertions Touched
- None. Standalone run.
```

---

*Schema version 1. Manor Protocol Phase 1 deliverable. 2026-05-10.*
