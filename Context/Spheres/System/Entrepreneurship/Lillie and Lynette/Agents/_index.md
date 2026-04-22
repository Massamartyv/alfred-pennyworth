---
file_type: agent_governance
venture: Lillie and Lynette
methodology: The Manor Protocol
status: active
last_updated: 2026-04-22
---

# The Manor Protocol – Lillie and Lynette

The proprietary methodology governing all work at Lillie and Lynette. Every studio is a room in the manor where craft happens. Creative excellence is the governing standard across all studios – the hospitality a guest experiences is the product of craft held to the same bar in Creative, Operations, Production, Finance and Administration alike.

---

## Philosophy

Hospitality is the art of being remembered well. The Manor Protocol does not treat warmth as a soft value. It holds it to a standard. A welcome is craft. A menu narrative is craft. A service moment is craft. A vendor relationship is craft. The methodology treats every output as an expression of the standard, regardless of which studio produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, context. Cultural sensing. Guest behaviour. Venue reconnaissance. The output is not answers – it is a landscape of possibility.

**Primary crews:** Explorer, Strategist

### 2. Direction

The hospitality call. A point of view crystallises from the reconnaissance – what the guest should feel, what the space should say, what the service should mean. This is the brief. Everything downstream is measured against it.

**Primary crews:** Strategist, Maestro

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Design the service flow. Write the menu. Source the vendor. Fabricate the experience. The brief is the guardrail. Craft is the standard.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Does it feel like Lillie and Lynette? Does the guest experience warmth and refinement in equal measure? Is every detail considered? This is not review for approval – it is review for quality.

**Primary crews:** Evaluator, Validator

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Open the doors. Serve the guest. Send the menu. Hand off the venue. Clean, complete, with nothing left undone.

**Primary crews:** Maestro

---

## Governance Model

**Hybrid architecture.** Shared governance lives here at the venture root (`Agents/`). Studio-specific agents, workflows and criteria live inside each studio local `Agents/` subfolder.

### Shared governance files (this folder)

| File | Purpose |
|---|---|
| `_index.md` | This file. The Manor Protocol definition. |
| `agent-guidelines.md` | Execution tiers, red lines, approval gates |
| `department-heads.md` | Role definitions and specialist seats |

Note: `integrations.md` is not yet created. Plugin scope for Lillie and Lynette is TBD and will be documented when tooling is selected.

### Studio-level agentic layer

Every studio contains an `Agents/` subfolder with a standard structure:

```
{Studio}/Agents/
  _index.md           -- Specialist roster and workflow registry
  Workflows/          -- Named Manor Protocol sequences for common tasks
  Criteria/           -- Quality rubrics and evaluation standards
  {agent-name}.md     -- Individual agent definitions as needed
```

---

## The Seven Studios

| Studio | Craft | Scope |
|---|---|---|
| **Creative** | Brand identity, guest experience design, visual language, interior direction, menu and offering narrative | What Lillie and Lynette looks like, feels like, sounds like |
| **Strategy** | Hospitality research, competitive intelligence, venue and market positioning, guest behaviour | The thinking behind the hospitality |
| **Production** | Service delivery production, event production, experience fabrication, content production | The execution engine |
| **Growth** | Sales, partnerships, venue sourcing, distribution pipeline, guest acquisition | Reach, revenue and pipeline |
| **Operations** | Day-to-day service, SOPs, tools, guest and vendor clientele | The engine room |
| **Finance** | Revenue, cost of service, expenses, projections, tax, metrics | The numbers |
| **Administration** | Legal, licensing, food and beverage compliance, insurance, HR | The structure |

### Shared Resources

| Resource | Purpose |
|---|---|
| **Knowledge Base** | Industry research, case studies, methodologies |
| **Foundation** | Community, philanthropy, hospitality-driven giving |

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

Not every task requires all five phases. A routine vendor confirmation does not need Reconnaissance. A template-based guest email does not need Direction approval. Use judgement. The lifecycle is a standard, not a ceremony.

### Multi-phase workflows

Complex deliverables – a new experience design, a venue launch, a menu development, a signature event – may cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before the guest ever sees it.

### Cross-studio work

When work spans multiple studios (Creative sets the guest experience direction, Production builds the service choreography, Operations runs the shift, Growth sells the experience), each studio runs its own lifecycle on its portion. The Maestro crew coordinates handoffs between studios.

---

*This is a living document. It evolves as the practice evolves.*
