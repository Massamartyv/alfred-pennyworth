---
file_type: agent_governance
venture: Atlas
status: active
methodology: The Manor Protocol
last_updated: 2026-06-11
---

# The Manor Protocol – Atlas

The proprietary methodology governing all work at Atlas. Every studio is a room in the manor where craft happens. Creative excellence is the governing standard across all studios.

Healthcare AI carries irreversibility risk that elevates the Critique gate to load-bearing status. No clinical output may ship without binary validation against the per-mission contract in `validation-contract.md`.

---

## Philosophy

Atlas operates in healthcare AI – specifically the chiropractic intelligence layer. The Manor Protocol does not treat any output lightly. A brief is craft. An EHR adapter is craft. A generated SOAP note is craft. A line of patient-facing copy is craft. The methodology holds every output to the same standard regardless of which studio produced it.

In a clinical domain, craft has a second meaning: the output must be defensible. Documentation that does not survive an audit, a board complaint, a malpractice review or a HIPAA enquiry is not craft – it is liability. The Critique gate is where that defensibility is verified.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. Clinical output never compresses Critique.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, competitive intelligence and clinical context. For Atlas this includes EHR API documentation, payer rules, technique-specific terminology and competitor moves.

**Primary crews:** Researcher

### 2. Direction

The point of view crystallises. The brief is decided. The validation contract is drafted and gated through operator approval.

**Primary crews:** Researcher → Creator (briefing handoff)

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Develop the adapter. Curate the clinical knowledge file. Generate the note. The brief is the guardrail. The validation contract is the standard.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief, the standard and the validation contract. Reviewer:Scrutiny runs the mechanical compliance pass – schema validity, code-set membership, log integrity, HIPAA boundary. Reviewer:Behavioural runs the clinician read – does this note read like a competent chiropractor wrote it.

**Primary crews:** Reviewer:Scrutiny, Reviewer:Behavioural

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Post the note. Deploy the adapter. Send the deliverable. Clean, complete, on standard.

**Primary crews:** Creator (release-mode)

---

## Governance Model

**Hybrid architecture.** Shared governance lives at the venture root (`Agents/`). Studio-specific agents, workflows and criteria live inside each studio local `Agents/` subfolder.

### Shared governance files (this folder)

| File | Purpose |
|---|---|
| `_index.md` | This file. The Manor Protocol definition scoped to Atlas. |
| `agent-guidelines.md` | Execution tiers, red lines, HIPAA boundaries |
| `department-heads.md` | Role definitions and specialist seats |
| `validation-contract.md` | Phase 1 binary assertions and evidence |
| `model-assignment.md` | Per-mission model allocation |

Plugin scope to be determined. `integrations.md` will be added once HIPAA-compliant infrastructure and the first EHR API key are configured.

### Studio-level agentic layer

Every studio contains an `Agents/` subfolder with a standard structure:

```
{Studio}/Agents/
  _index.md           – Specialist roster and workflow registry
  Workflows/          – Named Manor Protocol sequences for common tasks
  Criteria/           – Quality rubrics and evaluation standards
  {agent-name}.md     – Individual agent definitions as needed
```

---

## The Seven Studios

| Studio | Craft | Scope |
|---|---|---|
| **Creative** | Brand identity, voice, clinical communication standards | The look, feel and voice of Atlas |
| **Strategy** | EHR landscape, competitive intelligence, chiropractic market behaviour | The thinking behind the work |
| **Production** | AI architecture, FastMCP service, EHR adapters, clinical knowledge curation | The execution engine |
| **Growth** | Pilot expansion, channel architecture, partnerships | Revenue generation and adoption |
| **Operations** | Pilot management, clinical advisor liaison, support | The engine room |
| **Finance** | SaaS metrics, unit economics, inference cost | The numbers |
| **Administration** | HIPAA, BAAs, regulatory, entity, IP | The structural backbone |

### Shared Resources

| Resource | Purpose |
|---|---|
| **Knowledge Base** | Clinical knowledge, EHR intelligence, coding references, competitive landscape |
| **Foundation** | Community initiatives, chiropractic education contribution |

---

## Crew Mapping

The five universal crews classify the type of work, not who does it. Full definitions in `~/Alfred Pennyworth/Agents/crews.md`.

| Crew | Role | Lifecycle Affinity |
|---|---|---|
| Researcher | Research, analyse, synthesise | Reconnaissance, Direction |
| Creator | Build, write, design, produce | Execution, Release |
| Reviewer:Scrutiny | Mechanical compliance | Critique |
| Reviewer:Behavioural | End-user verification | Critique |
| Mediator | Resolve contention, surface tradeoffs | Direction, Critique |
| Broadcaster | Distribute context, status and signal | Release |

---

## Applying the Protocol

### Lightweight tasks

Not every task requires all five phases. Use judgement. Curating a single clinical knowledge file does not need a Direction gate. Generating a single SOAP note in production absolutely needs Critique.

### Multi-phase workflows

Complex deliverables cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before anything reaches a patient chart, a payer, the EHR or any audit surface.

### Cross-studio work

When work spans multiple studios, each studio runs its own lifecycle on its portion. The Creator crew in release-mode coordinates handoffs.

### Clinical work is irreversible

Every mission that touches patient data, generates clinical documentation or posts to an EHR carries a validation contract. The contract is a pre-execution assertion list, approved at Direction, read by every Reviewer dispatch and re-read at every milestone. Critique clears only when every assertion is satisfied with declared evidence.

---

*This is a living document. It evolves as the practice evolves.*
