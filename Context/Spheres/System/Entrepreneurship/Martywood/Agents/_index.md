---
file_type: agent_governance
venture: Marty Gras
methodology: The Manor Protocol
last_updated: 2026-08-04
---

# The Manor Protocol – Marty Gras

The proprietary methodology governing all work at Marty Gras. Every studio is a room in the manor where craft happens. Creative excellence is the governing standard across all studios – editorial, production, distribution, operations alike.

---

## Philosophy

Marty Gras is a media company. The stakes of "craft" are visible to an audience every time content ships. The Manor Protocol does not treat this lightly. An Epiphany is craft. A Conversation is craft. A mix is craft. A social fragment is craft. A sponsorship negotiation is craft. The methodology holds every output to the same standard regardless of which studio produced it.

## The Lifecycle

All work moves through five phases. The phases are sequential but not rigid – lightweight tasks may compress multiple phases into a single action. The lifecycle scales to the complexity of the work.

### 1. Reconnaissance

Wide scan. Gather raw material, references, signals, context. Cultural sensing. Audience insight. The output is not answers – it is a landscape of possibility.

**Primary crews:** Researcher

### 2. Direction

The editorial call. A point of view crystallises from the reconnaissance. This is the brief – the thesis that everything downstream is measured against.

**Primary crews:** Researcher, Mediator

**Hard gate: human approval required before proceeding to Execution.**

### 3. Execution

Build the thing. Write the Epiphany. Record the Conversation. Cut the mix. Craft the social fragment. Design the asset. The brief is the guardrail. Craft is the standard.

**Primary crews:** Creator

### 4. Critique

Hold the output against the brief and the standard. Is it excellent? Does it sound like Marty Gras? Does it meet the bar? This is not review for approval – it is review for quality.

**Primary crews:** Reviewer

**Hard gate: human approval required before proceeding to Release.**

### 5. Release

Ship it. Publish the Epiphany. Release the Conversation. Post the fragment. Clean, complete, delivered.

**Primary crews:** Broadcaster

---

## Governance Model

**Hybrid architecture.** Shared governance lives here at the venture root (`Agents/`). Studio-specific agents, workflows and criteria live inside each studio local `Agents/` subfolder.

### Shared governance files (this folder)

| File | Purpose |
|---|---|
| `_index.md` | This file. The Manor Protocol definition. |
| `agent-guidelines.md` | Execution tiers, red lines, approval gates |
| `department-heads.md` | Role definitions and specialist seats |
| `integrations.md` | Plugin and tool connections scoped to Marty Gras |

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
| **Creative** | Editorial direction, voice, brand system, content product definitions | What Marty Gras sounds like, looks like, feels like |
| **Strategy** | Audience research, platform intelligence, cultural positioning | The thinking behind the work |
| **Production** | Conversation production, Epiphany production, music and social production | The execution engine for content |
| **Growth** | Audience growth, partnerships, sponsorships, collaborations | Reach expansion and revenue relationships |
| **Operations** | Content pipeline, scheduling, tool stack, clientele management | The engine room |
| **Finance** | Revenue, expenses, projections, tax, metrics | The numbers |
| **Administration** | Legal, licensing, brand protection, policies, HR | The structure |

### Shared Resources

| Resource | Purpose |
|---|---|
| **Knowledge Base** | Cultural references, audience insights, research library |
| **Foundation** | Community initiatives, cultural philanthropy, mentorship |

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

Not every task requires all five phases. A template-based social post does not need Reconnaissance. A routine Epiphany send does not need Direction approval if it is already in the pipeline. Use judgement.

### Multi-phase workflows

Complex deliverables – a Conversation, a major Epiphany, a sponsorship pitch – may cycle through Execution and Critique multiple times before Release. The hard gate after Critique means human eyes before the audience sees it.

### Cross-studio work

When work spans multiple studios (Creative sets the editorial direction, Production builds the Conversation, Growth sells the sponsorship, Operations schedules the release), each studio runs its own lifecycle on its portion. The Mediator and Broadcaster crews coordinate handoffs and distribute state.

---

*This is a living document. It evolves as the practice evolves.*
