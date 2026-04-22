---
file_type: agent_governance
venture: Five Points Digital Studio
last_updated: 2026-04-07
---

# The Manor Protocol

The proprietary methodology governing all work at Five Points Digital Studio. Every department is a studio – a room in the manor where craft happens. Creative excellence is the governing standard across all departments, not a privilege reserved for one.

---

## Philosophy

The Manor Protocol does not separate "creative" from "operational." It holds all work to the same standard of taste and precision. A proposal is craft. An onboarding experience is craft. A financial report is craft. The methodology treats every output as an expression of the standard, regardless of which studio produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, context. Instinct-led exploration. The output is not answers – it is a landscape of possibility.

**Primary crews:** Explorer, Strategist

### 2. Direction

The creative call. A point of view crystallises from the reconnaissance. This is the brief – the decision that everything downstream is measured against.

**Primary crews:** Strategist, Maestro

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Write the copy. Design the system. Structure the proposal. The brief is the guardrail. Craft is the standard. Speed serves the work, not the other way round.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Is it excellent? Is it honest? Does it meet the bar? This is not review for approval – it is review for quality. The evaluator's eye, not the manager's clipboard.

**Primary crews:** Evaluator, Validator

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Hand it off. Deliver it to the world or to the next person in the chain. Clean, complete, with nothing left undone.

**Primary crews:** Maestro

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

## The Seven Studios

| Studio | Craft | Scope |
|---|---|---|
| **Creative** | Brand, visual direction, design, content, aesthetic standard | The look, feel and voice of everything |
| **Strategy** | Market intelligence, competitive analysis, positioning, research | The thinking behind the work |
| **Production** | Web development, media production, deliverable builds | The execution engine |
| **Growth** | Sales, BD, partnerships, pipeline, offer suite | Revenue generation and offer architecture |
| **Operations** | Client delivery, SOPs, tools, clientele management | The engine room |
| **Finance** | Revenue, expenses, projections, tax, metrics | The numbers |
| **Administration** | Legal, policies, compliance, HR, governance | The structure |

### Shared Resources

| Resource | Purpose |
|---|---|
| **Knowledge Base** | Institutional memory – case studies, methodologies, learnings |
| **Foundation** | Community, philanthropy, pro bono |

---

## Crew Mapping

The six universal crews classify the type of work, not who does it. Full definitions in `~/Alfred Pennyworth/Agents/crews.md`.

| Crew | Role | Lifecycle Affinity |
|---|---|---|
| Explorer | Market Sensor | Reconnaissance |
| Strategist | Researcher | Reconnaissance, Direction |
| Creator | Builder | Execution |
| Evaluator | Grader | Critique |
| Validator | Approver | Critique |
| Maestro | Orchestrator | Direction, Release |

---

## Applying the Protocol

### Lightweight tasks

Not every task requires all five phases. A routine status update does not need Reconnaissance. A template-based email does not need Direction approval. Use judgement. The lifecycle is a standard, not a ceremony.

### Multi-phase workflows

Complex deliverables may cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before the world sees it – but internal iterations within a studio can flow freely.

### Cross-studio work

When work spans multiple studios (e.g. Creative sets the brand direction, Production builds the website, Growth writes the proposal), each studio runs its own lifecycle on its portion. The Maestro crew coordinates handoffs between studios.

---

*This is a living document. It evolves as the practice evolves.*
