---
file_type: department_index
department: Operations
last_updated: "{YYYY-MM-DD}"
---

# Operations

The engine room. Client delivery, standard operating procedures, delivery playbooks, tools, and the Clientele directory where all active client work lives.

## Structure

```
Operations/
├── Clientele/
│   ├── _clients-registry.md       -- Master roster of all clients
│   ├── Active/                    -- Current engagements
│   │   └── {Client Name}/
│   │       ├── Onboarding/        -- Brief, terms, resources
│   │       ├── Strategy/          -- Positioning, goals, quarterly strategy
│   │       ├── Brand Assets/      -- Guidelines, templates, assets
│   │       ├── Deliverables/      -- Organized by service type
│   │       └── Administrative/    -- SOW, billing, meeting notes
│   ├── Archived/                  -- Completed or paused engagements
│   └── Churned/                   -- Lost clients (kept for reference)
├── SOPs/
│   ├── _sop-registry.md           -- Catalog of all SOPs
│   ├── client-onboarding.md       -- New client launch process
│   ├── project-delivery.md        -- Standard delivery workflow
│   ├── quality-assurance.md       -- QA checklist before any delivery
│   └── client-offboarding.md      -- Graceful exit process
├── Delivery Playbooks/            -- Step-by-step execution by service type
├── Templates/
│   ├── New Client/                -- Copy this folder for each new client
│   ├── monthly-report-template.md
│   ├── meeting-agenda-template.md
│   └── deliverables-checklist.md
└── Tools/
    ├── software-stack.md           -- All tools, access, purpose
    ├── automation-workflows.md     -- Active automations and what they do
    └── integration-docs.md         -- API connections and data flows
```

## Agent Instructions

- **New client onboarding:** Copy `Templates/New Client/` into `Clientele/Active/{Client Name}/`. Fill in Onboarding/ files first.
- **Client work:** Always check `_clients-registry.md` to understand the engagement before starting.
- **Delivery:** Load the relevant SOP from `SOPs/` and the service-specific playbook from `Delivery Playbooks/`.
- **Quality gate:** Run `SOPs/quality-assurance.md` before delivering anything to a client.
- **Client transitions:** Move folder from Active/ to Archived/ or Churned/ -- do not delete.

## What Belongs Here

- All client-facing work and context
- Standard operating procedures
- Delivery playbooks by service type
- Reusable templates
- Tool and infrastructure documentation

## What Does Not Belong Here

- Offer definitions (Product Development/)
- Sales process (Marketing & Sales/)
- Lead generation (Business Development/)
- Financial frameworks (Finances/)
