---
file_type: department_index
department: Operations
venture: Five Points Digital Studio
last_updated: 2026-04-07
---

# Operations

The engine room of Five Points. Client delivery, SOPs, tools, and the Clientele directory.

## Structure

```
Operations/
├── Clientele/
│   ├── _clients-registry.md       – Master roster
│   ├── Active/                    – Current engagements
│   │   └── Nomad Express/         – First organized client folder
│   ├── Archived/                  – Completed or paused
│   └── Churned/                   – Lost clients (kept for reference)
├── SOPs/
│   ├── _sop-registry.md
│   └── {SOPs as created}
├── Delivery Playbooks/            – Step-by-step by service type
├── Templates/
│   └── New Client/                – Copy for each new client
├── Tools/
│   ├── software-stack.md           – To be created
│   └── automation-workflows.md     – To be created
└── Agents/                        – Department-specific agents, workflows, criteria
```

## Key Ops Context

- Current delivery ratio: 80% delivery, 20% systems (target: flip this)
- Primary delivery tool: Notion (Five Points workspace)
- Client communication: Slack channels per client
- Quality gate: every deliverable reviewed before client handoff

## Agent Instructions

- **New client:** Copy Templates/New Client/ into Clientele/Active/{Client Name}/.
- **Client work:** Check _clients-registry.md first to understand the engagement.
- **Status change:** Move entire folder between Active/Archived/Churned. Update the registry.
- **Delivery:** Load the relevant SOP and delivery playbook before executing.

### Token Budget Defaults (per `Agents/token-budget-framework.md`)

| Task | Tier |
|---|---|
| Task creation, reminders, deadline flags, health checks | Light |
| Weekly status reports, meeting briefs, automation docs | Standard |
| SOPs, project post-mortems, infrastructure architecture | Heavy |

**Agent seats operating here:** Project Manager, Systems Engineer.
