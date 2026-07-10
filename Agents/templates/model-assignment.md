---
name: model-assignment
type: template
schema_version: 1
---

# Model Assignment Template

A planning deliverable that assigns a model to each role within a mission. Made conscious, not implicit. Overrides the global Model Selection Protocol defaults for the duration of the mission.

## When this template applies

Required for any Manor Protocol mission with two or more roles active. Optional for single-role missions, where the global default applies.

A role is active if at least one dispatch will be made under that role inside the mission.

## Authoring rules

- One row per active role
- Each row declares the model and a one-line reasoning
- Defaults shown below are starting points, not mandates – override per mission when the work warrants it
- Reasoning is required for every row, including rows that use the default

## Lifecycle

1. Alfred proposes the assignment during Direction
2. Operator approves at the Direction gate
3. Every dispatch inside the mission reads the assignment and selects its model accordingly
4. The assignment overrides global model defaults for the duration of the mission
5. The assignment is stored on the mission record – the scoped Projects entry – for tracked missions

## Relationship to global Model Selection Protocol

The global protocol in `~/.claude/CLAUDE.md` defines the default mapping of task type to model. The per-mission assignment is the exception – it makes the choice conscious for high-stakes or multi-role missions where the default might quietly under- or over-spend.

---

## Defaults

| Role                  | Model  | Reasoning                                       |
|-----------------------|--------|-------------------------------------------------|
| Orchestrator (Alfred) | opus   | Strategic judgement, plan revision              |
| Researcher            | sonnet | Volume work, synthesis at acceptable depth     |
| Creator               | sonnet | Code fluency, content production speed         |
| Reviewer:Scrutiny     | haiku  | High-frequency mechanical checks               |
| Reviewer:Behavioural  | sonnet | Reasoning about user experience                |

---

## Template

Copy the block below into the mission brief under the Direction section, or into `.working/{mission-name}/model-assignment.md` if maintained separately.

```markdown
## Model Assignment

| Role                  | Model  | Reasoning                                       |
|-----------------------|--------|-------------------------------------------------|
| Orchestrator (Alfred) | {model} | {one-line reasoning}                           |
| Researcher            | {model} | {one-line reasoning}                           |
| Creator               | {model} | {one-line reasoning}                           |
| Reviewer:Scrutiny     | {model} | {one-line reasoning}                           |
| Reviewer:Behavioural  | {model} | {one-line reasoning}                           |
```

Remove rows for roles that are not active in the mission.

---

## Worked example

A mission to author and ship a Marty Gras newsletter issue with brand-fingerprint review:

```markdown
## Model Assignment

| Role                  | Model  | Reasoning                                                       |
|-----------------------|--------|-----------------------------------------------------------------|
| Orchestrator (Alfred) | opus   | Editorial judgement and voice direction                         |
| Researcher            | sonnet | Source synthesis for the issue's argument                       |
| Creator               | opus   | Override: voice-led prose where taste outweighs throughput      |
| Reviewer:Scrutiny     | haiku  | Grammar, link integrity, brand-fingerprint mechanical pass     |
| Reviewer:Behavioural  | sonnet | Fresh read as a subscriber – does the hook land, is the CTA clear |
```

The Creator override to Opus is the kind of conscious upgrade this template forces into the open. Without the template the work would have defaulted to Sonnet by virtue of being content production, and the taste call would have been silently downgraded.

---

*Schema version 1. Manor Protocol Phase 1 deliverable. 2026-05-10. Updated 2026-07-10 – mission record made concrete.*
