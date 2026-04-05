---
file_type: department_index
department: Product Development
last_updated: "{YYYY-MM-DD}"
---

# Product Development

The offer suite. All products, services, tiers, bundles, and their definitions. This is the catalog that every other department references.

## Structure

Organize by pillar, then by offer, then by tier:

```
Product Development/
├── _index.md                          -- This file (offer registry)
├── {Pillar Name}/
│   ├── {Offer Category}/
│   │   ├── offer-overview.md          -- Parent overview with all tiers
│   │   └── {Tier Name}/
│   │       └── offer.md               -- Full tier definition
│   └── {Offer Category}/
└── Bundles/
    └── {Bundle Name}/
        └── offer.md                   -- Bundle definition
```

## Offer Registry

| Offer ID | Name | Pillar | Tiers | Status |
|---|---|---|---|---|
| {1.1} | {Offer Name} | {Pillar} | {Bronze, Silver, Gold, Platinum} | {active} |

(Populate as offers are built.)

## Agent Instructions

- This is the source of truth for what the venture sells. Never quote pricing or scope from memory -- always reference the offer file.
- Each `offer-overview.md` contains: pillar, offer number, description, tiers, dream outcome.
- Each `offer.md` within a tier folder contains: full pricing, deliverables, timeline, guarantee.
- When generating proposals, pull scope and pricing from the relevant offer file.
- Never modify offer files without explicit approval.

## What Belongs Here

- Offer definitions and tier structures
- Bundle configurations
- Pricing per offer (source of truth)
- Deliverable specifications

## What Does Not Belong Here

- Sales process or proposals (Marketing & Sales/)
- Client-specific scoping (Operations/Clientele/)
- Delivery SOPs (Operations/SOPs/ and Operations/Delivery Playbooks/)
