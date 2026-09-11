---
file_type: agent_governance
venture: Lillie and Lynette
methodology: The Manor Protocol
status: active
last_updated: 2026-09-10
---

# The Manor Protocol – Lillie and Lynette

The proprietary methodology governing all work at Lillie and Lynette. Every department is a room in the manor where craft happens. Creative excellence is the governing standard across all departments – the hospitality a guest experiences is the product of craft held to the same bar in Marketing & Sales, Operations, Finances and Administration alike.

---

## Philosophy

Hospitality is the art of being remembered well. The Manor Protocol does not treat warmth as a soft value. It holds it to a standard. A welcome is craft. A menu narrative is craft. A service moment is craft. A vendor relationship is craft. The methodology treats every output as an expression of the standard, regardless of which department produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, context. Cultural sensing. Guest behaviour. Venue reconnaissance. The output is not answers – it is a landscape of possibility.

**Primary crews:** Researcher

### 2. Direction

The hospitality call. A point of view crystallises from the reconnaissance – what the guest should feel, what the space should say, what the service should mean. This is the brief. Everything downstream is measured against it.

**Primary crews:** Researcher, Mediator

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Design the service flow. Write the menu. Source the vendor. Fabricate the experience. The brief is the guardrail. Craft is the standard.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Does it feel like Lillie and Lynette? Does the guest experience warmth and refinement in equal measure? Is every detail considered? This is not review for approval – it is review for quality.

**Primary crews:** Reviewer

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Open the doors. Serve the guest. Send the menu. Hand off the venue. Clean, complete, with nothing left undone.

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
| `integrations.md` | Plugin and tool connections; the provisioning checklist |

### Department-level agentic layer

Every department contains an `Agents/` subfolder with a standard structure:

```
{Department}/Agents/
  _index.md           -- Specialist roster and workflow registry
  Workflows/          -- Named Manor Protocol sequences for common tasks
  Criteria/           -- Quality rubrics and evaluation standards
  {agent-name}.md     -- Individual agent definitions as needed
```

---

## The Nine Departments

| Department | Craft | Scope |
|---|---|---|
| **Foundation** | Community initiatives, philanthropy, education, giving – plus the brand fingerprint and venture mission | The world the other pillars answer to |
| **Administration** | Legal, licensing, food and beverage compliance, insurance | The structure |
| **Finances** | Revenue, cost of service, expenses, projections, tax, metrics | The numbers |
| **Business Development** | ICP, prospecting and outreach, venue and partnership pipeline, positioning and market strategy | The thinking and the pipeline behind the hospitality |
| **Marketing & Sales** | Brand identity, guest experience design, visual language, content, sales process, guest acquisition, distribution | What Lillie and Lynette looks like, feels like, sounds like, and how a prospect becomes a guest |
| **Operations** | Day-to-day service, SOPs, event and experience production, tools, guest and vendor clientele | The engine room |
| **Product Development** | Offer tiers, pricing rungs, offer strategy and audits, the Objects retail line | The offer ladder |
| **Human Resources** | Team, contractors, hiring plans, culture | The people |
| **Knowledge Base** | Industry research, case studies, methodologies, competitive intelligence | The intellectual fuel |

---

## Crew Mapping

The five universal crews classify the type of work, not who does it. Full definitions in `~/Alfred Pennyworth/Agents/crews.md`.

| Crew | Role | Lifecycle Affinity |
|---|---|---|
| Researcher | Market Sensor, Analyst | Reconnaissance, Direction |
| Creator | Builder | Execution |
| Reviewer | Grader, Approver | Critique |
| Mediator | Orchestrator, Tradeoff Resolver | Direction |
| Broadcaster | Distributor | Release |

---

## Applying the Protocol

### Lightweight tasks

Not every task requires all five phases. A routine vendor confirmation does not need Reconnaissance. A template-based guest email does not need Direction approval. Use judgement. The lifecycle is a standard, not a ceremony.

### Multi-phase workflows

Complex deliverables – a new experience design, a venue launch, a menu development, a signature event – may cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before the guest ever sees it.

### Cross-department work

When work spans multiple departments (Marketing & Sales sets the guest experience direction and sells it, Operations builds the service choreography and runs the shift, Business Development sources the venue or partner), each department runs its own lifecycle on its portion. The Mediator and Broadcaster crews coordinate handoffs and distribute state between departments.

---

*This is a living document. It evolves as the practice evolves.*
