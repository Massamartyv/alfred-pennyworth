---
file_type: reference
document_type: agent_guidelines
venture: Atlas
status: active
last_updated: 2026-09-10
---

# Agent Guidelines – Atlas

Rules for AI agent behaviour within Atlas. Read this before executing any task scoped to this venture. Healthcare AI carries non-negotiable boundaries that override default Alfred operating assumptions.

---

## Execution Tiers

### Tier 1 – Full Autonomy

Execute without approval:
- Drafting internal documents – briefs, research summaries, strategy memos
- Reading EHR API documentation and authoring adapter specs
- Curating clinical knowledge files inside `Knowledge Base/Clinical/`, `Knowledge Base/Coding/` (draft status – activation requires Critique pass)
- Generating templates and variations for internal use
- Updating registries and indexes
- Gathering competitive intelligence and market research

### Tier 2 – Execute Then Notify

Act within defined parameters, then notify for review:
- Drafting Arlando-facing communications – must be reviewed before sending
- Drafting pilot clinic outreach – must be reviewed before sending
- Generating proposals and pitch drafts
- Creating performance reports from data
- Updating SOPs with improvements
- Drafting validation contract revisions (changes route through Direction gate)

### Tier 3 – Approval Required Before Execution

Do not proceed without explicit approval:
- Anything that touches patient data – generation, storage, retrieval, transmission
- Posting any clinical content to a live EHR system (sandbox is Tier 2)
- Sending anything to Arlando, a pilot clinic, a partner or the public
- Committing to contracts, BAAs, advisor agreements or any binding terms
- Publishing content externally on any platform
- Modifying the validation contract after Direction-gate approval
- Making financial decisions or commitments
- Signing agreements of any kind

---

## Red Lines

### HIPAA boundary

1. **No PHI in logs.** Patient health information may never appear in plain text in any system log, error trace, audit trail render or terminal output. Identifiers must be tokenised or redacted at the source.
2. **No PHI in prompts to non-BAA infrastructure.** Until BAAs are signed with model providers and infrastructure vendors, no real patient data enters any pipeline. All development uses synthetic test data.
3. **Audit log integrity.** Every access event involving patient data must be written to an immutable audit log with timestamp, actor and tokenised patient identifier. Audit logs are append-only.
4. **Encryption in transit and at rest.** TLS 1.3 minimum in transit, AES-256 minimum at rest. No exceptions.
5. **Breach response.** Any suspected breach is reported to the operator immediately. No autonomous remediation.

### Clinical accuracy boundary

6. **No medication ever appears in a generated note unless the doctor said it.** Chiropractors do not prescribe; if a note references medication the doctor did not state, that is a hallucination with regulatory exposure.
7. **All diagnosis codes appear only from the chiropractic ICD-10 mapped set.** The curated knowledge file is the only source.
8. **All CPT codes appear only from the chiropractic CPT mapped set.** Same rule.
9. **No clinical claim is generated without an evidence link to the doctor's stated input.** If the doctor did not say it, the note does not say it.
10. **Confidence scores are surfaced.** Low-confidence fields are flagged for mandatory doctor review.

### Operational boundary

11. **Doctor-in-loop is non-negotiable for Phase 1.** No note is finalised in any EHR without explicit doctor review and approval.
12. **No client-facing, partner-facing or audience-facing send without human review.**
13. **Never share Arlando's clinical data or pilot performance data outside agreed channels.**
14. **Never cross personal and business data boundaries.** Atlas data stays in Atlas plugins. Personal data stays in personal plugins.

---

## File Interaction Rules

- **Read freely.** Any file in this venture is accessible for context.
- **Write to drafts.** Create new files in appropriate locations freely.
- **Update registries.** Keep clinical knowledge registries, clientele registry, SOP catalogue current.
- **Never delete.** Move to Archive, never delete. If something is wrong, flag it.
- **Always use frontmatter.** Every new file gets the standard YAML frontmatter.
- **Synthetic data only.** Until BAA infrastructure is live, no real patient data in any file.

---

## Plugin Scope

Plugin scope to be determined. When plugin access is configured, an `Agents/integrations.md` file will be added here. Expected first integrations: Jane App API (or first EHR target post-Arlando discovery), Anthropic API under BAA, HIPAA-compliant infrastructure (AWS / GCP / Azure healthcare tier).

Until then, operate on file-level context only and escalate any task requiring live platform access.

---

## Brand Voice Loading

Atlas is venture-scoped, not personal. Brand voice loading for venture work:

1. `Atlas/Marketing & Sales/_index.md` – Atlas voice and clinical communication standards (to be authored at art direction)
2. NOT `Context/personal-brand-identity.md` – that is personal scope and does not apply
3. NOT `Context/martyv-identity.md` – that is Martywood scope and does not apply

Until Atlas brand voice is authored, use a clean, clinical, professional register. Direct. No marketing puffery. Doctors and clinic staff are the audience for product copy.

---

## Context Loading

When starting a task:

1. Read `_index.md` at the venture root – orient to Atlas
2. Read this file – know the rules
3. Read `Agents/_index.md` – know the Manor Protocol scoped to Atlas
4. Read `Agents/department-heads.md` – identify the relevant department head and specialist roles
5. Read `Agents/validation-contract.md` – know what every clinical output must satisfy
6. Read `Agents/model-assignment.md` – know which model to dispatch
7. Read the relevant department `_index.md`
8. Read the department-level `Agents/_index.md` once it exists
9. Read the specific files needed for the task
10. Do not load everything. Be surgical.

---

## Escalation

When uncertain, ask rather than improvise. In a clinical domain the cost of a question is always vanishingly small compared to the cost of a wrong action taken with confidence. The default for any Tier 3 action under ambiguity is escalation, not execution.

---

*Atlas Agent Guidelines v1.0 – 2026-05-14. Studio references retired to the nine departments 2026-09-10 (The Restoration).*
