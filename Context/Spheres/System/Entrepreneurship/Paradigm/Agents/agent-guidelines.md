---
file_type: reference
document_type: agent_guidelines
venture: Paradigm
status: active
last_updated: 2026-09-10
---

# Agent Guidelines – Paradigm

Rules for AI agent behaviour within Paradigm. Read this before executing any task scoped to this venture.

---

## Execution Tiers

### Tier 1 – Full Autonomy

Execute without approval:
- Drafting internal documents – briefs, research summaries, formulation notes
- Generating templates and variations
- Creating content drafts – social, email, educational copy
- Extracting and summarising data from Notion
- Updating registries and indexes
- Gathering ingredient science and competitive intelligence

### Tier 2 – Execute Then Notify

Act within defined parameters, then notify for review:
- Populating product launch templates
- Generating proposals and wholesale pitch drafts – must be reviewed before sending
- Creating performance reports from data
- Updating SOPs with improvements
- Drafting supplier and manufacturer outreach – must be reviewed before sending

### Tier 3 – Approval Required Before Execution

Do not proceed without explicit approval:
- Publishing any health claim, label copy or supplement facts panel
- Committing to manufacturing runs, ingredient orders or packaging orders
- Sending anything customer-facing, retailer-facing or regulator-facing
- Registering products with FDA or entering any regulatory submission
- Signing supplier, manufacturer, distribution or wholesale agreements
- Modifying formulations or product specifications
- Making financial decisions or commitments
- Publishing brand content externally on any platform

---

## Red Lines

1. Never publish any health or structure-function claim that has not been reviewed against FDA and FTC guidance.
2. Never commit to a product delivery timeline without verifying manufacturing capacity and regulatory status.
3. Never deviate from documented brand voice, positioning or visual system.
4. Never modify a formulation without approval – formulations are source documents.
5. Never send anything customer-facing, wholesale-facing or regulator-facing without human review.
6. Never share proprietary formulation data, supplier terms or manufacturer details outside authorised channels.
7. Never guess at pricing, dosage, ingredient concentrations or regulatory status – always reference the source file.
8. Never use unapproved ingredients, unverified suppliers or uncleared marketing claims in any draft that could be copied to a live channel by accident.
9. Never cross personal and business data boundaries.

---

## File Interaction Rules

- **Read freely.** Any file in this venture is accessible for context.
- **Write to drafts.** Create new files in appropriate locations freely.
- **Update registries.** Keep `_clients-registry.md` and `_sop-registry.md` current.
- **Never delete.** Move to Archive, never delete. If something is wrong, flag it.
- **Always use frontmatter.** Every new file gets the standard YAML frontmatter.
- **Treat formulations as source documents.** Files in `Product Development/Formulations/` and product spec files are read-only to agents. Propose changes as a draft in a separate file for human review.

---

## Plugin Scope

Paradigm does not yet have a defined plugin registry. When plugin access is configured, an `Agents/integrations.md` file will be added here. Until then, operate on file-level context only and escalate any task that requires live platform access.

---

## Brand Voice Loading

Any task that produces audience-facing or customer-facing content must load:

1. `Context/personal-brand-identity.md` – the voice foundation
2. `Context/creative-director.md` – aesthetic sensibility
3. `Marketing & Sales/_index.md` – Paradigm creative scope (and the brand fingerprint when one is created)

These files govern everything the audience sees, reads or receives.

---

## Context Loading

When starting a task:

1. Read `_index.md` at the venture root – orient to the venture
2. Read this file – know the rules
3. Read `Agents/_index.md` – know the Manor Protocol
4. Read `Agents/department-heads.md` – identify the relevant department head and specialist roles
5. Read the relevant department `_index.md` – find the right files
6. Read the department-level `Agents/_index.md` – know the specialist roster and workflows
7. Read the specific files needed for the task
8. Do not load everything. Be surgical.

---

## Regulatory Awareness

### FDA and FTC context

Paradigm operates in a regulated category. Dietary supplements, cosmetics and wellness products all sit under FDA jurisdiction for labelling, manufacturing and claims – and under FTC jurisdiction for marketing truthfulness. The Administration department owns compliance. Every output that references ingredients, dosages, benefits or outcomes must be checked against that framework before Release.

### Structure-function vs. disease claims

Structure-function claims (e.g. "supports healthy immune response") require an FDA disclaimer. Disease claims (e.g. "treats flu") require drug approval. Agents draft in the safer structure-function space by default and flag any draft that edges into disease-claim territory for Administration review.

### Third-party verification

Ingredient sourcing, manufacturing facilities and testing results are verified source documents. Never generate an ingredient claim, origin story or testing result that is not backed by a verified document in the Knowledge Base or Product Development department.

---

## Escalation

When uncertain, ask rather than improvise. The cost of a question is always lower than the cost of a wrong action taken with confidence. In a regulated industry the cost of a wrong action can include recall, fines or brand damage.
