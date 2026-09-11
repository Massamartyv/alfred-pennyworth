---
file_type: department_index
department: Operations
venture: Martywood
last_updated: 2026-09-10
---

# Operations – Martywood

The engine room of Martywood. Content pipeline, scheduling, tool stack and the Clientele directory for sponsors, collaborators and featured guests.

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
└── Tools/
    ├── software-stack.md           -- To be created
    └── automation-workflows.md     -- To be created
```

### What Belongs Here

- Content pipeline tracking (ideation through publication)
- Publishing schedules and deadlines
- Tool configurations and integrations
- Sponsor, collaborator and featured guest management
- Standard operating procedures
- Quality assurance processes at the operational level
- Client and content delivery workflow and delivery quality

### What Does Not Belong Here

- Agent guidelines and department heads – those now live at `Agents/` (venture root)
- Content strategy, editorial direction and voice – Marketing & Sales
- Audience growth strategy, partnerships and positioning – Business Development
- Financial tracking – Finances
- Content and product builds themselves – Product Development

### Subdirectories

| Folder | Contents |
|---|---|
| Clientele/ | Master roster of sponsors, collaborators and featured guests, split into Active, Archived and Churned |
| SOPs/ | SOP registry and individual standard operating procedures |

## Content Pipeline Overview

Four acts, preceded by a capture layer that sits outside Notion. Full definition in `SOPs/content-pipeline.md` (MW-000).

0. **Capture** – voice memo, Apple Notes, pen and paper. Held locally until the sweep lands it
1. **Ideation** – the standing pool of options. Most ideas die here, cheaply
2. **Pre-Production** – Research then Planned. Reference set, format shell, outline, booked shoot date
3. **Production** – Recording then Editing. Execution only, no new structural decisions
4. **Post-Production** – Scheduled, Published, Reviewed. Syndication via Pennyone, Substack for Epiphany, the audio host for the Conversation, then metrics reconciled and a verdict written

Each act owns a defined set of Content Calendar fields and its exit gate is checkable rather than judged. The `Phase` property derives the act from Status by formula.

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

## Active State

Live state: Notion Projects and Tasks, personal workspace.
