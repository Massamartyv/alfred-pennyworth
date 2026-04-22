---
file_type: reference
document_type: agent_guidelines
venture: "{Venture Name}"
status: template
last_updated: 2026-04-22
---

# Agent Guidelines – {Venture Name}

Rules for AI agent behaviour within {Venture Name}. Read this before executing any task scoped to this venture.

---

## Execution Tiers

### Tier 1 – Full Autonomy

Execute without approval:
- Drafting internal documents – briefs, research summaries, notes
- Generating templates and variations
- Creating content drafts – social, email, editorial copy
- Extracting and summarising data from Notion
- Updating registries and indexes
- Gathering competitive intelligence and market research

### Tier 2 – Execute Then Notify

Act within defined parameters, then notify for review:
- Populating launch and project templates
- Generating proposals and pitch drafts – must be reviewed before sending
- Creating performance reports from data
- Updating SOPs with improvements
- Drafting outreach communications – must be reviewed before sending

### Tier 3 – Approval Required Before Execution

Do not proceed without explicit approval:
- Sending anything external – client-facing, partner-facing or audience-facing
- Committing to orders, contracts or production runs
- Publishing content externally on any platform
- Making financial decisions or commitments
- Signing agreements of any kind
- Modifying core product, offer or brand specifications

---

## Red Lines

1. Never deviate from documented brand voice, positioning or visual system.
2. Never send anything client-facing, partner-facing or audience-facing without human review.
3. Never commit to a delivery timeline without verifying capacity and dependencies.
4. Never share proprietary pricing, supplier terms or internal specifications outside authorised channels.
5. Never modify source documents – formulas, offer specs, brand assets – without approval. Propose changes as a draft.
6. Never guess at pricing, specifications or compliance status – always reference the source file.
7. Never cross personal and business data boundaries.

---

## File Interaction Rules

- **Read freely.** Any file in this venture is accessible for context.
- **Write to drafts.** Create new files in appropriate locations freely.
- **Update registries.** Keep `_clients-registry.md` and `_sop-registry.md` current.
- **Never delete.** Move to Archive, never delete. If something is wrong, flag it.
- **Always use frontmatter.** Every new file gets the standard YAML frontmatter.

---

## Plugin Scope

Plugin scope to be determined on copy. When plugin access is configured, an `Agents/integrations.md` file will be added here. Until then, operate on file-level context only and escalate any task requiring live platform access.

---

## Brand Voice Loading

Any task that produces audience-facing or client-facing content must load:

1. `Context/personal-brand-identity.md` – the voice foundation
2. `Context/creative-director.md` – aesthetic sensibility
3. `Creative/_index.md` – venture creative scope

These files govern everything the audience sees, reads or receives.

---

## Context Loading

When starting a task:

1. Read `_index.md` at the venture root – orient to the venture
2. Read this file – know the rules
3. Read `Agents/_index.md` – know the Manor Protocol
4. Read `Agents/department-heads.md` – identify the relevant studio head and specialist roles
5. Read the relevant studio `_index.md` – find the right files
6. Read the studio-level `Agents/_index.md` – know the specialist roster and workflows
7. Read the specific files needed for the task
8. Do not load everything. Be surgical.

---

## Escalation

When uncertain, ask rather than improvise. The cost of a question is always lower than the cost of a wrong action taken with confidence.
