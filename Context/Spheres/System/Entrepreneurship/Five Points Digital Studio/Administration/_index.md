---
file_type: department_index
department: Administration
venture: Five Points Digital Studio
last_updated: 2026-04-03
---

# Administration

Legal templates, compliance checklists, company policies, and brand identity for Five Points.

## Structure

```
Administration/
├── Legal/
│   ├── service-agreement-template.md    -- To be created
│   ├── nda-template.md                  -- To be created
│   ├── sow-template.md                  -- To be created
│   ├── contractor-agreement-template.md -- To be created
│   └── ip-ownership-addendum.md         -- To be created
├── Compliance/
│   ├── business-registration.md         -- To be created
│   ├── insurance-requirements.md        -- To be created
│   └── data-protection-policy.md        -- To be created
├── Policies/
│   ├── communication-standards.md       -- To be created
│   ├── confidentiality-policy.md        -- To be created
│   └── quality-standards.md             -- To be created
└── Identity/
    ├── brand-voice.md                   -- To be created
    ├── company-positioning.md           -- To be created
    ├── values-and-principles.md         -- To be created
    ├── business-model.md                -- To be created
    └── service-scope.md                 -- To be created
```

## Agent Instructions

- Use Legal/ templates when drafting any client-facing agreement.
- Client-specific legal documents live in Operations/Clientele/{Client}/Legal/.
- Administrative templates here are the source of truth -- client legal folders reference these.
- `Identity/brand-voice.md` must be loaded before generating any external-facing content.

### Token Budget Defaults (per `Operations/AI/token-budget-framework.md`)

| Task | Tier |
|---|---|
| Filing, scheduling, reminders, policy lookups | Light |
| Onboarding packets, compliance checklists | Standard |
| Compliance audits, legal template drafting | Heavy |

**Agent seat operating here:** HR/Admin Coordinator.
