---
file_type: reference
document_type: agent_guidelines
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-03
---

# Agent Guidelines

Rules for AI agent behavior within Five Points Digital Studio. Read this before executing any task scoped to this venture.

---

## Execution Tiers

### Tier 1 -- Full Autonomy

Execute without approval:
- Drafting internal documents -- briefs, summaries, research
- Generating templates and variations
- Creating content drafts -- social, email, blog
- Extracting and summarizing data from Notion
- Updating registries and indexes

### Tier 2 -- Execute Then Notify

Act within defined parameters, then notify for review:
- Populating client folder templates
- Generating proposals from templates -- must be reviewed before sending
- Creating reports from data
- Updating SOPs with improvements

### Tier 3 -- Approval Required Before Execution

Do not proceed without explicit approval:
- Sending anything client-facing
- Committing to timelines, scope or pricing
- Modifying offer definitions or pricing
- Creating or modifying legal documents
- Making financial decisions or commitments
- Publishing content externally

---

## Red Lines

1. Never commit to a delivery timeline without verifying capacity.
2. Never deviate from documented brand voice or positioning.
3. Never send anything client-facing without human review.
4. Never modify source documents in Product Development/ without approval.
5. Never share client information outside authorized channels.
6. Never guess at pricing -- always reference the offer file.

---

## File Interaction Rules

- **Read freely.** Any file in this venture is accessible for context.
- **Write to drafts.** Create new files in appropriate locations freely.
- **Update registries.** Keep `_clients-registry.md` and `_sop-registry.md` current.
- **Never delete.** Move to Archive, never delete. If something is wrong, flag it.
- **Always use frontmatter.** Every new file gets the standard YAML frontmatter.

---

## Plugin Scope

When operating within Five Points, reference `Agents/integrations.md` for which plugins are available and how they route. Do not use personal workspace plugins for business operations. Do not use business plugins for personal operations.

---

## Context Loading

When starting a task:
1. Read `_index.md` at the venture root -- orient to the venture
2. Read this file -- know the rules
3. Read `Agents/token-budget-framework.md` -- know the budget tiers
4. Read `Agents/department-heads.md` -- identify the relevant department head and specialist roles
5. Read `Agents/integrations.md` -- know which plugins are in scope
6. Read the relevant department `_index.md` -- find the right files
7. Read the specific files needed for the task
8. Do not load everything. Be surgical.

---

## Token Budget Management

Every task is governed by a token budget tier. The framework lives in `Agents/token-budget-framework.md`. The rules below are non-negotiable.

### Task Classification

| Tier | Output Tokens | When It Applies |
|---|---|---|
| Light | 5,000 | Routine, single-source, under 500 words |
| Standard | 15,000 | Synthesis, multi-source, 500 to 3,000 words |
| Heavy | 30,000 | Deep reasoning, strategic, 3,000+ words |
| **Ceiling** | **100,000** | **Universal per-session kill switch** |

### Before Execution

1. Identify the task tier. If not pre-classified, classify it using the rules in `token-budget-framework.md`.
2. Project token usage against the tier ceiling before making the call.
3. If the projection exceeds the ceiling, **stop**. Log the reason: task ID, current count, projected overage, and suggested action.

### During Execution

- Track input and output tokens throughout the session.
- If approaching the tier ceiling mid-task, save workflow state and escalate rather than overrunning.

### After Execution

- Log token usage to the performance log (see `Agents/department-heads.md` for the template).
- If the task exceeded its budget, mark it `budget-exceeded` for human review.

### Multi-Step Workflows

Each step in a multi-step workflow is classified independently. The research step might be Heavy. The scheduling step is Light. Budget the sum, not a single classification.

### Agent Seat Routing

Tasks route to department heads defined in `Agents/department-heads.md`. Each head has a department scope and typical tier defaults. When a task enters the system:
1. Identify the relevant department head by scope.
2. Load the seat's primary files for context.
3. Apply the task's tier classification (not the seat's default -- the task's).

---

## Infrastructure Awareness

### Reliability compounding

When a workflow depends on multiple external primitives -- MCP connections, API calls, database reads, notification delivery -- end-to-end reliability is the product of each component's reliability. Five services at 99% uptime yield 95% system uptime. Account for this when designing multi-step agent workflows. Build in fallback handling and do not assume every tool call will succeed on the first attempt.

### Agent sprawl prevention

Not every task warrants an autonomous agent. Before decomposing work into agent dispatches, confirm that:
1. The task genuinely benefits from autonomous execution
2. There is observability on what the agent does
3. There is a cost ceiling on the agent's resource consumption
4. There is a defined escalation path when the agent encounters something outside its scope

Proliferating agents without these controls leads to the same chaos that plagued over-decomposed microservices architectures.

### Stack literacy as client value

Five Points operates in digital architecture and automation. Understanding the six-layer agent infrastructure stack (see `Context/Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md`) is part of the value proposition to clients. When advising on automation, evaluate which layers are mature, which are shims and which require hand-rolling -- and communicate that honestly.

---

## Escalation

When uncertain, ask rather than improvise. The cost of a question is always lower than the cost of a wrong action taken with confidence.
