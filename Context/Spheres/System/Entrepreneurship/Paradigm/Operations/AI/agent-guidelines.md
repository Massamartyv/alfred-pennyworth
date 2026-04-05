---
file_type: reference
document_type: agent_guidelines
venture: Paradigm
status: active
last_updated: 2026-04-05
---

# Agent Guidelines -- Paradigm

Rules for AI agent behaviour within Paradigm. Read this before executing any task scoped to this venture.

---

## Execution Tiers

### Tier 1 -- Full Autonomy

Execute without approval:
- Research -- ingredient sourcing, competitor analysis, market trends, regulatory requirements
- Data extraction -- industry reports, pricing benchmarks, consumer insights
- Drafting internal documents -- briefs, summaries, meeting notes
- Generating templates and document variations
- Updating registries and indexes

### Tier 2 -- Execute Then Notify

Act within defined parameters, then notify for review:
- Drafting product descriptions, marketing copy or educational content
- Creating supplier outreach drafts -- must be reviewed before sending
- Populating financial models with researched data
- Updating SOPs with improvements
- Creating performance reports from analytics data

### Tier 3 -- Approval Required Before Execution

Do not proceed without explicit approval:
- Publishing any content externally -- website, social, email
- Sending messages to suppliers, manufacturers or partners
- Committing to partnerships, supplier terms or distribution agreements
- Making health or wellness claims in any external-facing material
- Modifying product formulations or ingredient lists
- Making financial decisions or commitments
- Placing orders with suppliers or manufacturers
- Registering for new platforms or services

---

## Red Lines

1. Never make health claims without verified regulatory compliance.
2. Never publish product information without human review.
3. Never send outreach to suppliers, partners or retailers without approval.
4. Never modify formulation or ingredient documents without approval.
5. Never commit to any partnership, supply agreement or distribution terms.
6. Never cross personal and business data boundaries.
7. Never use copyrighted images, formulations or proprietary processes.

---

## File Interaction Rules

- **Read freely.** Any file in this venture is accessible for context.
- **Write to drafts.** Create new files in appropriate locations freely.
- **Update registries.** Keep `_clients-registry.md` and `_sop-registry.md` current.
- **Never delete.** Move to Archive, never delete. If something is wrong, flag it.
- **Always use frontmatter.** Every new file gets the standard YAML frontmatter.

---

## Context Loading

When starting a task:
1. Read `_index.md` at the venture root -- orient to the venture
2. Read this file -- know the rules
3. Read the relevant department `_index.md` -- find the right files
4. Read the specific files needed for the task
5. Do not load everything. Be surgical.

---

## Health and Wellness Compliance

Any task that produces customer-facing content must consider:
1. FDA regulations on supplement and wellness product claims
2. FTC guidelines on advertising and endorsements
3. State-level regulations where applicable
4. Internal health claims policy -- to be developed in Administration/Policies/

This is a non-negotiable layer. Health and wellness is a regulated space. Every external claim must be defensible.

---

## Plugin Scope

When MCP connections are established for Paradigm, they will be documented in `Operations/AI/integrations.md`. Until then, all operations use personal workspace plugins scoped to this venture's content.

---

## Escalation

When uncertain, ask rather than improvise. The cost of a question is always lower than the cost of a wrong action taken with confidence.
