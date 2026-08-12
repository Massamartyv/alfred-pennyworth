---
file_type: department_index
department: Operations
venture: Marty Gras
last_updated: 2026-08-04
---

# Operations

The engine room of Marty Gras. Content pipeline, scheduling, tool stack and the Clientele directory for sponsors, collaborators and featured guests.

## Structure

```
Operations/
├── Clientele/
│   ├── _clients-registry.md       -- Master roster of sponsors, collaborators, featured guests
│   ├── Active/                    -- Current relationships
│   ├── Archived/                  -- Completed or paused
│   └── Churned/                   -- Ended relationships (kept for reference)
├── SOPs/
│   ├── _sop-registry.md
│   └── {SOPs as created}
├── Delivery Playbooks/            -- Step-by-step production guides
├── Templates/
│   └── New Engagement/            -- Copy for each new sponsor or collaborator
├── Tools/
│   ├── software-stack.md           -- To be created
│   └── automation-workflows.md     -- To be created
└── Agents/                        -- Studio-specific agents, workflows, criteria
```

## Scope

### What belongs here

- Content pipeline tracking (ideation through publication)
- Publishing schedules and deadlines
- Tool configurations and integrations
- Sponsor, collaborator and featured guest management
- Standard operating procedures
- Quality assurance processes at the operational level

### What does not belong here

- Agent guidelines and department heads – those now live at `Agents/` (venture root)
- Content strategy and ideation – Creative
- Audience growth strategy – Growth
- Financial tracking – Finance

## Content Pipeline Overview

Three stages:

1. **Ideation** – captured in Notion Content database, tagged by sphere and platform
2. **Production** – drafted, reviewed, refined per the relevant Production SOP
3. **Distribution** – scheduled via Pennyone for social syndication, Substack for Epiphany, the audio host for the Conversation

Detailed SOPs for each content type live in `Operations/SOPs/`.

## Production Stack

| Tool | Purpose | Status |
|---|---|---|
| Pennyone | Social syndication (Zernio under the hood for IG, TikTok, Threads, X, Reddit, Snap) | Scaffold ready; awaiting Zernio key |
| ElevenLabs | Conversation audio production and voice work | Active |
| Substack | Epiphany publishing | To be configured |
| Audio host | Audio distribution | To be selected |
| Notion | Content calendar, editorial planning, production tracking | Active (personal workspace) |

Note: Buffer is deprecated ecosystem-wide as of April 2026. Pennyone replaces it for social syndication.

## Current State

Pipeline structure defined. SOPs and playbooks to be written as production cadence stabilises. Pennyone integration pending.
