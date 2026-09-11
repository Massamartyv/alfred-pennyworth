---
file_type: department_index
department: Operations
venture: Five Points Digital Studio
last_updated: 2026-09-10
---

# Operations – Five Points Digital Studio

The engine room of Five Points. Client delivery, deliverable builds, SOPs, tools, quality control of delivery and the Clientele directory. Operations absorbs the former Production department's build execution – website development, media production and technical implementation are delivery work, and delivery is Operations' charter.

## Structure

```
Operations/
├── Clientele/
│   ├── _clients-registry.md       – Master roster
│   ├── Active/                    – Current engagements
│   ├── Archived/                  – Completed or paused
│   └── Churned/                   – Lost clients (kept for reference)
├── SOPs/
│   ├── _sop-registry.md
│   └── {SOPs as created}
├── Templates/
│   ├── New Client/                – Copy for each new client
│   └── Standardized Document Library/  – Master intake forms, MSA, SOW, onboarding packet, feedback form and the operational standards reference
└── Agents/                        – Department-specific agents, workflows, criteria
    _index.md                      – Agent roster and workflow registry
    Workflows/                     – Named Manor Protocol sequences
    Criteria/                      – Quality rubrics and evaluation standards
```

## Scope

### What belongs here
- Client onboarding, delivery tracking and offboarding
- SOP creation, maintenance and delivery playbooks
- Website development, media production and deliverable builds
- Quality control of delivery – technical and process
- Tool stack, automation workflows and integration management
- The Clientele directory

### What does not belong here
- Brand direction and creative decisions (Marketing & Sales)
- Offer scoping and pricing (Product Development)
- Prospecting and deal closing (Business Development, Marketing & Sales)
- Financial reporting (Finances)

## Subdirectories

| Folder | Purpose |
|---|---|
| Clientele/ | Client roster and folders – Active, Archived, Churned |
| SOPs/ | Standard operating procedures and the SOP registry |
| Templates/ | New client copy set and the standardized document library |
| Agents/ | Department-specific agent roster and workflows |

## Key Registries

- Web template repo: `studio-fivepoints/fp-starter-template` (GitHub)
- Production stack: Next.js, Vercel, Supabase, Adobe Creative Suite

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
- **Standards and forms:** Master client-facing documents – intake forms, MSA, SOW, onboarding packet and feedback form – plus the operational standards reference live in `Templates/Standardized Document Library/`. Update `00-operational-standards-reference.md` first when any standard changes, then propagate across the library.
- Load the relevant creative brief from Marketing & Sales before building – never build without direction
- All client-facing deliverables pass through Critique before Release
- Code commits follow conventional commit standards (no character)

### Token Budget Defaults (per `Agents/token-budget-framework.md`)

| Task | Tier |
|---|---|
| Task creation, reminders, deadline flags, health checks, component updates, copy swaps | Light |
| Weekly status reports, meeting briefs, automation docs, page builds, template creation | Standard |
| SOPs, project post-mortems, infrastructure architecture, full site builds, complex integrations | Heavy |

**Agent seats operating here:** Project Manager, Systems Engineer.
