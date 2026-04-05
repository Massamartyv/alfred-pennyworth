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
| media-scan | System/ | Explorer | Monthly | Surface new five-star entries from Notion databases |
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
tools: {what tools it needs}
---
```

Followed by: Mission, Scope, Criteria, Report Format, After the Mission.

---

## Naming Convention

Files use lowercase kebab-case: `{domain}-{function}.md`

---

## Directory Structure

```
Agents/
+-- _index.md          -- This file
+-- crews.md           -- Universal crew definitions
+-- System/            -- Infrastructure and maintenance agents
|   +-- context-audit.md
|   +-- media-scan.md
|   +-- sphere-review.md
+-- Orchestration/     -- Portfolio-level agents
    +-- penny-one.md
    +-- watchtower.md
```

---

*Last updated: April 2026*
