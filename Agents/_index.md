---
file_type: directory_index
directory: Agents
last_updated: 2026-04-29
---

# Agents

Reusable mission briefs for autonomous subprocesses. Each file defines a specific agent that Alfred can dispatch during a session. Agents do not carry the Alfred character. They carry a directive, execute and report back.

---

## The Agentic Framework

### Hierarchy

```
YOU -- CEO / Creative Director / Founder
  |
  ALFRED -- COO / Orchestrator
    |
    +-- [Department Heads] -- Venture-specific leadership roles
    |     +-- [Specialist Roles] -- Functional positions under each head
    |
    +-- [Crews] -- The five types of work any role dispatches
```

**You** set the vision, strategy and creative direction. **Alfred** translates strategy into actionable plans, manages day-to-day operations, maintains infrastructure and systems and tracks performance. **Department Heads** own specific functional areas within each venture. **Crews** classify the type of work being performed.

### The Five Crews

Crews are not agents. They are classifications of work. See `crews.md` for full definitions.

| Crew | What They Do |
|---|---|
| Researcher | Research, analyse, synthesise, scout trends, sense shifts, surface opportunities. Combines what was previously Strategist and Explorer. |
| Creator | Build, write, design, produce. |
| Reviewer | Review, audit, grade, validate, gate output. Combines what was previously Evaluator and Validator. |
| Mediator | Resolve contention over shared resources, surface tradeoffs, optimise across stakeholders, find win-wins. Promoted from coordination pattern 2026-05-14. |
| Broadcaster | Distribute shared context, status and signal, keep coherence across multi-agent missions and multi-channel output. Promoted from coordination pattern 2026-05-14. |

Maestro retired. Alfred is the orchestrator – multi-step coordination is what the orchestrator already does, not a separate crew.

### Venture Department Heads

Each venture defines its own department head structure in `Operations/AI/department-heads.md`. Department heads provide vertical structure. Crews provide horizontal capability. The two systems are orthogonal.

---

## Coordination Patterns

How dispatches relate to each other inside a mission. Crews say what the work is. Patterns say how dispatches link up.

Sourced from Factory's multi-agent strategies (AI Engineer, 2026), cross-referenced against the Alfred operating system on 2026-05-10.

### The five patterns

| Pattern | What it is | Alfred state |
|---|---|---|
| Delegation | One agent spawns another for a subtask | Active – the spine of every mission. Hardened by the handoff schema |
| Creator-Verifier | One agent builds, a different agent checks | Active – Creator crew followed by Reviewer crew. Fresh-context rule below |
| Direct Communication | Peer agents coordinate without an orchestrator | Skipped deliberately – Alfred-as-coordinator is the safer pattern |
| Negotiation | Two agents resolve contention over a shared resource | Promoted to crew 2026-05-14 – see Mediator in `crews.md` |
| Broadcast | One agent distributes shared context or status to many | Promoted to crew 2026-05-14 – see Broadcaster in `crews.md` |

### Creator fresh-context rule

Every dispatched Reviewer agent runs in fresh context with no memory of the Creator it audits. Both tiers, no exceptions:

- Reviewer:Scrutiny – mechanical audit in fresh context
- Reviewer:Behavioural – end-user pass in fresh context

The rule exists to eliminate sunk-cost bias on the work being audited. A Reviewer that carries memory of the Creator's work is no longer auditing – it is the Creator extending its own work.

Alfred reviewing in his own main thread is a different pattern – the orchestrator running a quality check on output that passed through him – not a Reviewer dispatch. The fresh-context rule applies only to dispatched Reviewer agents.

### What we deliberately skip

**Direct Communication.** Peer-to-peer coordination without an orchestrator. Factory itself flagged the failure mode: state fragments across agents that cannot reconcile without a coordinator. Alfred-as-coordinator is the chosen pattern for the foreseeable future. Any future temptation to let dispatched agents talk to each other directly should reread this note first.

### Future phases

- **Mission Control** – the dynamic in-mission status surface. Phase 2. Until it exists, the handoff schema and validation contract serve as passive Broadcaster work – the same shared truth read by every dispatch at every milestone.

---

## When to Use an Agent vs. a Skill

| | Skill | Agent |
|---|---|---|
| Who acts | Alfred himself -- first person | A dispatched worker -- third person |
| Activation | User invokes with a slash command or trigger word | Alfred dispatches when the mission calls for it |
| Persistence | Active for the duration of the task | Executes and disappears |
| Character | Carries persona, philosophy, standards | Carries a directive, tools and success criteria |
| Output | Interactive conversation | Structured report |
| Example | `/personal-trainer` -- Alfred becomes the Sensei | context-audit -- agent scans files and returns findings |

---

## Agent Types

### System Agents

Operate across the entire ecosystem. Infrastructure-level maintenance.

| Agent | Location | Crew | Cadence | Purpose |
|---|---|---|---|---|
| context-audit | System/ | Reviewer:Scrutiny | Monthly | Scan context files for stale or inconsistent information |
| media-scanner | System/ | Researcher | Monthly | Surface new five-star entries from Notion databases |
| sphere-review | System/ | Reviewer:Scrutiny | Quarterly | Verify Sphere Index alignment |

### Orchestration Agents

Portfolio-level systems that aggregate intelligence and surface alerts across all ventures.

| Agent | Location | Crew | Cadence | Purpose |
|---|---|---|---|---|
| pattern-memo | Orchestration/ | Researcher, Creator | Monthly | Three patterns from the prior month, staged into the new Monthly Review entry in Reflections |
| penny-one | Orchestration/ | Creator, Broadcaster | Weekly and on-demand | Portfolio briefing production and multi-platform syndication |
| watchtower | Orchestration/ | Reviewer:Scrutiny, Broadcaster | Continuous | Threshold monitoring and alert broadcasting |

### Venture Agents

Venture-specific agent configurations live at `Operations/AI/` within each venture. See each venture's `department-heads.md` for role definitions and `agent-guidelines.md` for execution rules.

---

## Stack Awareness

Alfred operating system operates within a six-layer agent infrastructure stack. Every agent, crew dispatch and architectural decision should be evaluated against this model. Full reference: `Context/Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md`.

| Layer | What It Is | Alfred operating system Position |
|---|---|---|
| 1. Compute and sandboxing | Safe, isolated execution environments | Local Mac. `.working/` for transient files. Cloud sandboxes needed for deployed agents. |
| 2. Identity and communication | How agents exist and communicate on the internet | Email Directory, iMessage, MCP auth. Shim-heavy -- functional but not agent-native. |
| 3. Memory and state | Persistent recall across sessions and tasks | `.claude/` memory system with active curation. Notion as durable portable layer. |
| 4. Tools and integration | Connecting agents to external services | MCP connections. Per-venture `integrations.md` files. Strong but MCP-dependent. |
| 5. Provisioning and billing | Agents acquiring and paying for services | Token budget framework, execution tiers. Needs formal billing protocol at scale. |
| 6. Orchestration and coordination | Multi-agent reliability at scale | Pennyone, Watchtower, six-crew system. **This is where we are building.** |

### Reliability rule

End-to-end reliability is the product of every layer's reliability. Five layers at 99% uptime yield 95% system uptime. Every primitive composed by hand stacks its liabilities. When dispatching multi-step agent workflows, account for compounding failure risk and build in fallback handling.

### Agent sprawl guardrail

Not every task needs an agent. The same disease that plagued microservices -- decomposing everything into agents because it is fashionable rather than because it is needed -- leads to proliferation without observability or cost control. Before dispatching an agent, confirm that the task genuinely benefits from autonomous execution rather than direct handling.

---

## How Agents Work

1. Alfred reads the agent definition file to understand the mission scope, tools and success criteria
2. If the agent operates within a venture, Alfred also reads that venture's `Operations/AI/agent-guidelines.md`
3. Alfred dispatches an autonomous subprocess with the mission brief
4. The agent executes independently
5. The agent returns a structured report
6. Alfred presents the findings and acts on approved recommendations

---

## Agent Definition Format

Each agent file uses this structure:

```yaml
---
name: {agent-name}
description: {one-line description focused on when to invoke, not what it is}
model: {haiku, sonnet, opus}
type: {maintenance, research, build, audit, orchestration, monitoring}
crew: {one or more of: researcher, creator, reviewer, mediator, broadcaster}
tier: {scrutiny, behavioural}    # required when crew is reviewer
cadence: {when it runs}
scope: {what files/systems it operates on}
working_dir: .working/{agent-name}/
tools: {what tools it needs}
---
```

Followed by: Mission, Scope, Criteria, Working Directory, After the Mission.

### Handoff is the closing artefact

Every agent run ends with a handoff document written to `.working/{agent-name}/handoff.md`. The canonical schema lives at `templates/handoff-schema.md` and is required output – no exceptions. The handoff replaces the loose Report Format that previously sat under this section.

Existing agents (`context-audit`, `media-scanner`, `sphere-review`, `penny-one`, `watchtower`) retrofit to the schema on their next definition update – no stop-the-world rewrite.

### Manor Protocol gates – reversibility-based

Gates fire on irreversibility, not category.

| Action class | Direction gate | Critique gate |
|---|---|---|
| Reversible work (drafts, internal writes, research output, scratch artefacts) | – | – |
| External-facing or irreversible (sends, publishes, payments, force-pushes, deploys) | – | Required |

The Direction gate is retired as a structural requirement. Agents may still produce a direction artefact for their own planning. The Critique gate is the load-bearing one – it is the last opportunity to catch a compounding error before the work leaves the system.

### Model defaults

- System maintenance agents (`context-audit`, `media-scanner`, `sphere-review`): `haiku`. Mechanical scans, low judgment, high frequency.
- Orchestration agents (`penny-one`, `watchtower`): `sonnet`. Mid-judgment, mid-frequency, content production and threshold logic.
- Department heads doing strategic or creative judgment work: `opus`. Taste, synthesis and direction calls.

### Working directory convention

Every agent gets a named subdirectory under `.working/` at the project root. The path is `.working/{agent-name}/`. This is where the agent writes all intermediate output -- raw data, comparison diffs, draft sections, temporary exports. The directory is cleared at the end of each run.

When creating a new agent, create its working directory: `mkdir -p .working/{agent-name}/`.

---

## Naming Convention

Files use lowercase kebab-case: `{domain}-{function}.md`

Explorer agents carry a directional suffix that signals where they look:

| Suffix | Direction | What It Means | Example |
|---|---|---|---|
| `-scanner` | Inward | Scans internal systems -- Notion databases, file structures, internal data | `media-scanner`, `sphere-scanner` |
| `-radar` | Outward | Scans external landscape -- platforms, markets, competitors, trends | `tiktok-radar`, `competitor-radar` |

---

## Directory Structure

```
Agents/
+-- _index.md          -- This file
+-- crews.md           -- Universal crew definitions
+-- System/            -- Infrastructure and maintenance agents
|   +-- context-audit.md
|   +-- media-scanner.md
|   +-- sphere-review.md
+-- Orchestration/     -- Portfolio-level agents
    +-- pattern-memo.md
    +-- penny-one.md
    +-- watchtower.md
```

---

*Last updated: 2026-05-26 – pattern-memo added under Orchestration; runs first of every month, drafts the Monthly Review entry in Reflections.*
