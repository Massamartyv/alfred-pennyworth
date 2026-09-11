---
file_type: agent_governance
venture: Five Points Digital Studio
last_updated: 2026-09-10
---

# The Manor Protocol

The proprietary methodology governing all work at Five Points Digital Studio. Every department is a room in the manor where craft happens. Creative excellence is the governing standard across all departments, not a privilege reserved for one.

---

## Philosophy

The Manor Protocol does not separate "creative" from "operational." It holds all work to the same standard of taste and precision. A proposal is craft. An onboarding experience is craft. A financial report is craft. The methodology treats every output as an expression of the standard, regardless of which department produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, context. Instinct-led exploration. The output is not answers – it is a landscape of possibility.

**Primary crews:** Researcher

### 2. Direction

The creative call. A point of view crystallises from the reconnaissance. This is the brief – the decision that everything downstream is measured against.

**Primary crews:** Researcher, Creator

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Write the copy. Design the system. Structure the proposal. The brief is the guardrail. Craft is the standard. Speed serves the work, not the other way round.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Is it excellent? Is it honest? Does it meet the bar? This is not review for approval – it is review for quality. The evaluator's eye, not the manager's clipboard.

**Primary crews:** Reviewer:Scrutiny, Reviewer:Behavioural

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Hand it off. Deliver it to the world or to the next person in the chain. Clean, complete, with nothing left undone.

**Primary crews:** Broadcaster

---

## Governance Model

**Hybrid architecture.** Shared governance lives here at the venture root (`Agents/`). Department-specific agents, workflows and criteria live inside each department's local `Agents/` subfolder.

### Shared governance files (this folder)

| File | Purpose |
|---|---|
| `_index.md` | This file. The Manor Protocol definition. |
| `agent-guidelines.md` | Execution tiers, red lines, approval gates |
| `department-heads.md` | Role definitions and specialist seats |
| `token-budget-framework.md` | Task complexity tiers and budget ceilings |
| `integrations.md` | Plugin and tool connections scoped to Five Points |
| `operating-loop.md` | The client flywheel – nine stages across the departments, the venture operating loop |

### Department-level agentic layer

Every department contains an `Agents/` subfolder with a standard structure:

```
{Department}/Agents/
  _index.md           – Agent roster and workflow registry for this department
  Workflows/          – Named Manor Protocol sequences for common tasks
  Criteria/           – Quality rubrics and evaluation standards
  {agent-name}.md     – Individual agent definitions as needed
```

---

## The Nine Departments

| Department | Craft | Scope |
|---|---|---|
| **Foundation** | Brand fingerprint, standing doctrine, venture mission, community, philanthropy, pro bono | The constitutional layer |
| **Administration** | Legal, compliance, contracts, brand protection, governance | The structure |
| **Finances** | Revenue, expenses, projections, tax, metrics | The numbers |
| **Business Development** | ICP, prospecting and outreach, partnerships, pipeline, channels, positioning and market strategy | Who we sell to |
| **Marketing & Sales** | Brand identity and creative direction, visual and content standards, marketing, sales process, discovery, proposals, pricing | The look, feel and voice of everything, and how a prospect becomes a client |
| **Operations** | SOPs, client delivery, quality control of delivery, clientele, deliverable builds | The engine room and the execution arm |
| **Product Development** | Offers, tiers, bundles, offer strategy and audits, the venture's own products and builds | What we sell |
| **Human Resources** | Team, contractors, hiring, culture | The people |
| **Knowledge Base** | Research, case studies, industry and competitive intelligence, methodologies | Institutional memory |

---

## Crew Mapping

The five universal crews classify the type of work, not who does it. Full definitions in `~/Alfred Pennyworth/Agents/crews.md`.

| Crew | Role | Lifecycle Affinity |
|---|---|---|
| Researcher | Research, analyse, synthesise | Reconnaissance, Direction |
| Creator | Build, write, design, produce | Execution |
| Reviewer:Scrutiny | Mechanical compliance | Critique |
| Reviewer:Behavioural | End-user verification | Critique |
| Mediator | Resolve contention, surface tradeoffs | Direction |
| Broadcaster | Distribute context, status and signal | Release |

---

## Applying the Protocol

### Lightweight tasks

Not every task requires all five phases. A routine status update does not need Reconnaissance. A template-based email does not need Direction approval. Use judgement. The lifecycle is a standard, not a ceremony.

### Multi-phase workflows

Complex deliverables may cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before the world sees it – but internal iterations within a department can flow freely.

### Cross-department work

When work spans multiple departments (e.g. Marketing & Sales sets the brand direction, Operations builds the website, Business Development writes the proposal), each department runs its own lifecycle on its portion. The Broadcaster crew distributes handoff context and signals between departments; the Mediator crew resolves contention when departments have competing inputs.

---

*This is a living document. It evolves as the practice evolves.*
