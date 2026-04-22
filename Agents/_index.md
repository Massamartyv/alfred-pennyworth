---
file_type: directory_index
directory: Agents
last_updated: 2026-04-05
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
    +-- [Crews] -- The six types of work any role dispatches
```

**You** set the vision, strategy and creative direction. **Alfred** translates strategy into actionable plans, manages day-to-day operations, maintains infrastructure and systems and tracks performance. **Department Heads** own specific functional areas within each venture. **Crews** classify the type of work being performed.

### The Six Crews

Crews are not agents. They are classifications of work. See `crews.md` for full definitions.

| Crew | Role | What They Do |
|---|---|---|
| Strategist | Researcher | Research, analyse, synthesise, recommend |
| Creator | Builder | Build, write, design, produce |
| Evaluator | Grader | Review, audit, grade against criteria |
| Maestro | Orchestrator | Coordinate multi-step workflows |
| Validator | Approver | Check compliance, gate output |
| Explorer | Market Sensor | Scout trends, sense shifts, surface opportunities |

### Venture Department Heads

Each venture defines its own department head structure in `Operations/AI/department-heads.md`. Department heads provide vertical structure. Crews provide horizontal capability. The two systems are orthogonal.

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
| context-audit | System/ | Evaluator | Monthly | Scan context files for stale or inconsistent information |
| media-scanner | System/ | Explorer | Monthly | Surface new five-star entries from Notion databases |
| sphere-review | System/ | Evaluator | Quarterly | Verify Sphere Index alignment |

### Orchestration Agents

Portfolio-level systems that aggregate intelligence and surface alerts across all ventures.

| Agent | Location | Crew | Cadence | Purpose |
|---|---|---|---|---|
| penny-one | Orchestration/ | Maestro | Weekly and on-demand | Portfolio-level briefing |
| watchtower | Orchestration/ | Validator | Continuous | Threshold monitoring and alerts |

### Venture Agents

Venture-specific agent configurations live at `Operations/AI/` within each venture. See each venture's `department-heads.md` for role definitions and `agent-guidelines.md` for execution rules.

---

## Stack Awareness

Alfred OS operates within a six-layer agent infrastructure stack. Every agent, crew dispatch and architectural decision should be evaluated against this model. Full reference: `Context/Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md`.

| Layer | What It Is | Alfred OS Position |
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
description: {one-line description}
type: {maintenance, research, build, audit, orchestration, monitoring}
crew: {strategist, creator, evaluator, maestro, validator, explorer}
cadence: {when it runs}
scope: {what files/systems it operates on}
working_dir: .working/{agent-name}/
tools: {what tools it needs}
---
```

Followed by: Mission, Scope, Criteria, Report Format, Working Directory, After the Mission.

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
    +-- penny-one.md
    +-- watchtower.md
```

---

*Last updated: April 2026*
