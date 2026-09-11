---
file_type: agent_governance
venture: Paradigm
status: active
methodology: The Manor Protocol
last_updated: 2026-09-10
---

# The Manor Protocol – Paradigm

The proprietary methodology governing all work at Paradigm. Every department is a room in the manor where craft happens. Creative excellence is the governing standard across all departments – formulation, packaging, marketing, compliance alike.

---

## Philosophy

Paradigm is a health and wellness brand. The stakes of "craft" are felt on a customer's body and felt in their daily ritual. Products go inside people. Labels make claims that regulators read. Packaging sits on shelves next to incumbents with decades of equity. The Manor Protocol does not treat any of this lightly. A formula is craft. A compliance label is craft. A supplement facts panel is craft. A customer email is craft. The methodology holds every output to the same standard regardless of which department produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, ingredient science, consumer insight, regulatory context. The output is not answers – it is a landscape of possibility.

**Primary crews:** Researcher

### 2. Direction

The brand call. A point of view crystallises from the reconnaissance – on formula, positioning, packaging, channel. This is the brief – the decision that everything downstream is measured against.

**Primary crews:** Researcher, Mediator

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Develop the formula. Design the label. Draft the launch plan. Write the claims. The brief is the guardrail. Craft is the standard.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Is it excellent? Is it compliant? Does it meet the bar? This is not review for approval – it is review for quality. In a regulated industry, this gate is non-negotiable.

**Primary crews:** Reviewer

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Launch the product. Publish the campaign. Send the order to fulfilment. Clean, complete, compliant.

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

Plugin scope for Paradigm is still to be determined. No `integrations.md` exists yet.

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
| **Foundation** | Community wellness initiatives, philanthropy, education, giving – plus the brand fingerprint and venture mission | Where the brand invests in the health of the communities it serves |
| **Administration** | Legal, FDA and FTC compliance, labelling, brand protection, governance | The structure |
| **Finances** | Revenue, COGS, expenses, projections, tax, metrics | The numbers |
| **Business Development** | Wholesale, distribution, partnerships, affiliates and ambassadors, sales pipeline, positioning, consumer insight | Revenue generation and channel architecture |
| **Marketing & Sales** | Brand identity, visual direction, packaging aesthetics, content standards, DTC channel, sales process | The look, feel and voice of the brand, and the path from that voice to a sale |
| **Operations** | Fulfilment, supply chain, quality control, SOPs, clientele management | The engine room |
| **Product Development** | Product formulation, manufacturing workflows, packaging production, content production, offer architecture | The execution engine, and the venture's own products and builds |
| **Human Resources** | Team, contractors, advisors, culture, hiring plans | The people |
| **Knowledge Base** | Ingredient science, case studies, industry research, methodologies | Institutional memory |

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

Not every task requires all five phases. A routine restock order does not need Reconnaissance. A template-based customer service reply does not need Direction approval. Use judgement.

### Multi-phase workflows

Complex deliverables – a new product formulation, a packaging redesign, a wholesale pitch deck – cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before the product, the label or the campaign reaches a customer or a regulator.

### Cross-department work

When work spans multiple departments (Marketing & Sales sets packaging direction, Product Development manufactures the product, Administration clears the claims, Business Development pitches the distributor), each department runs its own lifecycle on its portion. The Mediator and Broadcaster crews coordinate handoffs and distribute state.

### Regulated-industry discipline

Paradigm operates under FDA and FTC oversight. Critique is not an optional polish step – it is a compliance checkpoint. Labels, claims, marketing copy and ingredient representations all pass through Critique with Administration in the loop before Release.

---

*This is a living document. It evolves as the practice evolves.*
