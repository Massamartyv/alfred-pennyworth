---
name: validation-contract
type: template
schema_version: 1
---

# Validation Contract Template

A validation contract is a pre-execution assertion list that defines "done" independently of implementation. Each assertion is a binary check evaluable without inspecting the work that satisfies it. The sum of assertions covers the mission.

## When this template applies

Required for any Manor Protocol mission that meets either trigger:

- Two or more Creator dispatches inside the mission
- The work is irreversible at the Critique gate (sends, publishes, payments, force-pushes, deploys)

For missions below the threshold, a validation contract is optional but recommended for anything novel.

## Authoring rules

- Each assertion is a single binary statement that can be answered yes or no
- Each assertion is evaluable without reading the implementation
- Each assertion has exactly one owner – the feature, milestone or worker that satisfies it
- Each assertion declares its evidence – the artefact that proves satisfaction
- Each assertion declares its review tier – `scrutiny` for mechanical compliance, `behavioural` for end-user verification
- The template is the schema and stays local; instances live in `.working/{mission-name}/` and, after Critique, on the mission record as an H3 section

Assertions are written as outcomes, not steps. "The dispatched agent writes a handoff document" is an assertion. "Run the handoff write step" is not.

## Lifecycle

1. Alfred drafts the contract during Reconnaissance
2. Alfred surfaces the draft at Direction
3. Operator approves before the Direction gate clears
4. The contract is stored at `.working/{mission-name}/validation-contract.md` during execution
5. Every Reviewer dispatch reads the contract before reviewing
6. The orchestrator reads the contract at every milestone boundary
7. The contract is copied onto the mission record – the scoped Notion Projects entry, defined in `Agents/_index.md` – once Critique clears

## Relationship to Manor Protocol gates

When a validation contract is in play, the Direction gate is promoted from optional to required for that mission. The contract itself is the artefact gating Direction. The Critique gate clears only when every assertion is satisfied with declared evidence.

---

## Template

Copy the block below into `.working/{mission-name}/validation-contract.md` and fill in.

```markdown
---
mission: {mission-name}
created: {YYYY-MM-DD}
contract_version: 1
---

## Assertions

A1. {Binary statement evaluable without inspecting implementation}
    - Owner: {feature-id or worker that satisfies this assertion}
    - Evidence: {what proves this is satisfied}
    - Tier: scrutiny | behavioural

A2. {Next assertion}
    - Owner:
    - Evidence:
    - Tier:

## Coverage Map

| Feature | Assertions Owned |
|---|---|
| F1     | A1, A3           |
| F2     | A2, A4, A5       |
```

---

## Worked example

A mission to retrofit five existing agents with the handoff schema:

```markdown
---
mission: agent-handoff-retrofit
created: 2026-06-01
contract_version: 1
---

## Assertions

A1. Each retrofitted agent writes a handoff document conforming to handoff-schema.md as its final action.
    - Owner: F1 retrofit pass on each agent file
    - Evidence: handoff.md exists in .working/{agent-name}/ after a test run
    - Tier: scrutiny

A2. Each retrofitted agent's handoff includes every required section (Completed, Undone, Commands Run, Issues Discovered, Procedural Compliance, Assertions Touched).
    - Owner: F1 retrofit pass on each agent file
    - Evidence: section presence check against handoff-schema.md
    - Tier: scrutiny

A3. Each retrofitted agent's definition file references the handoff schema in its After the Mission section.
    - Owner: F1 retrofit pass on each agent file
    - Evidence: grep for "handoff-schema" in each agent file
    - Tier: scrutiny

A4. The retrofit does not change any agent's mission scope or tool set.
    - Owner: F2 reviewer pass
    - Evidence: diff comparison of frontmatter before and after
    - Tier: scrutiny

## Coverage Map

| Feature | Assertions Owned |
|---|---|
| F1      | A1, A2, A3       |
| F2      | A4               |
```

---

*Schema version 1. Manor Protocol Phase 1 deliverable. 2026-05-10. Updated 2026-07-10 – mission record made concrete; authoring rule on template vs instance location added.*
