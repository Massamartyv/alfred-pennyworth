---
file_type: agent_governance
venture: "{Venture Name}"
status: template
methodology: The Manor Protocol
last_updated: 2026-05-14
---

# The Manor Protocol – {Venture Name}

The proprietary methodology governing all work at {Venture Name}. Every studio is a room in the manor where craft happens. Creative excellence is the governing standard across all studios.

---

## Philosophy

{Venture Name} operates in {Industry}. The Manor Protocol does not treat any output lightly. A brief is craft. A product is craft. A piece of copy is craft. The methodology holds every output to the same standard regardless of which studio produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, competitive intelligence and market context. The output is not answers – it is a landscape of possibility.

**Primary crews:** Researcher

### 2. Direction

The point of view crystallises from the reconnaissance. This is the brief – the decision that everything downstream is measured against.

**Primary crews:** Researcher → Creator (handoff)

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Develop the product. Design the assets. Draft the plan. Write the copy. The brief is the guardrail. Craft is the standard.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Is it excellent? Is it compliant? Does it meet the bar? This is review for quality, not approval.

**Primary crews:** Reviewer:Scrutiny, Reviewer:Behavioural

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Launch the product. Publish the campaign. Send the deliverable. Clean, complete, on standard.

**Primary crews:** Creator (release-mode), Broadcaster

---

## Governance Model

**Hybrid architecture.** Shared governance lives here at the venture root (`Agents/`). Studio-specific agents, workflows and criteria live inside each studio local `Agents/` subfolder.

### Shared governance files (this folder)

| File | Purpose |
|---|---|
| `_index.md` | This file. The Manor Protocol definition. |
| `agent-guidelines.md` | Execution tiers, red lines, approval gates |
| `department-heads.md` | Role definitions and specialist seats |

Plugin scope to be determined on copy. No `integrations.md` exists until configured.

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
| **Creative** | Brand identity, visual direction, aesthetics, content standards | The look, feel and voice of the venture |
| **Strategy** | Industry research, competitive intelligence, positioning, market behaviour | The thinking behind the work |
| **Production** | Product and content development, manufacturing coordination, build quality | The execution engine |
| **Growth** | Sales, partnerships, distribution, channel architecture | Revenue generation and channel architecture |
| **Operations** | Delivery, supply chain, quality control, SOPs, clientele management | The engine room |
| **Finance** | Revenue, costs, expenses, projections, tax, metrics | The numbers |
| **Administration** | Legal, compliance, brand protection, governance, HR | The structure |

### Shared Resources

| Resource | Purpose |
|---|---|
| **Knowledge Base** | Research, case studies, industry intelligence, methodologies |
| **Foundation** | Community initiatives, philanthropy, education |

---

## Crew Mapping

The five universal crews classify the type of work, not who does it. Full definitions in `~/Alfred Pennyworth/Agents/crews.md`.

| Crew | Role | Lifecycle Affinity |
|---|---|---|
| Researcher | Investigator and sensor | Reconnaissance, Direction |
| Creator | Builder | Execution, Release |
| Reviewer | Auditor and gate | Critique |
| Mediator | Tradeoff resolver | Direction, Execution |
| Broadcaster | Signal distributor and coherence keeper | Direction, Release |

Reviewer carries two tiers dispatched as distinct subtypes – `Reviewer:Scrutiny` for mechanical compliance and `Reviewer:Behavioural` for end-user verification. Mission planning declares which tier each Critique milestone requires.

---

## Applying the Protocol

### Lightweight tasks

Not every task requires all five phases. Use judgement. A routine admin update does not need Reconnaissance. A template-based communication does not need a Direction gate.

### Multi-phase workflows

Complex deliverables cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before anything reaches an audience, a client or a partner.

### Cross-studio work

When work spans multiple studios, each studio runs its own lifecycle on its portion. Alfred coordinates handoffs across studios. The Broadcaster crew carries shared context and milestone signals between them.

---

*This is a living document. It evolves as the practice evolves.*
