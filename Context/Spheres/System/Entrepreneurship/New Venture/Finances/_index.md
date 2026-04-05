---
file_type: department_index
department: Finances
last_updated: "{YYYY-MM-DD}"
---

# Finances

Revenue models, financial projections, tax compliance, cost management, and performance metrics. Reference frameworks that agents use for pricing decisions, financial reporting, and planning.

## Structure

```
Finances/
├── Revenue/
│   ├── pricing-framework.md        -- Value-based pricing principles and tier logic
│   ├── revenue-model.md            -- Revenue streams and mix targets
│   └── client-mix-scenarios.md     -- Models for hitting MRR targets
├── Planning/
│   ├── cash-flow-model.md          -- Monthly cash flow template
│   ├── financial-projections.md    -- Quarterly and annual projections
│   └── capacity-planning.md        -- Client capacity vs. team size
├── Tax/
│   ├── compliance-calendar.md      -- Filing deadlines
│   ├── deductible-categories.md    -- Agency-specific deductions
│   └── entity-structure.md         -- Business structure and election info
├── Cost Management/
│   ├── software-subscriptions.md   -- Tool costs and renewal dates
│   └── vendor-contracts.md         -- Active vendor agreements
└── Metrics/
    ├── key-financial-metrics.md    -- MRR, CAC, LTV, churn, margins
    ├── monthly-review-template.md  -- Monthly financial review format
    └── quarterly-planning.md       -- OKRs and capacity review
```

## Agent Instructions

- Reference `Revenue/pricing-framework.md` when generating proposals or quoting prices.
- Use `Planning/` templates when asked to project revenue or model scenarios.
- Check `Tax/compliance-calendar.md` when approaching end of quarter.
- Never modify pricing without explicit approval.

## What Belongs Here

- Pricing frameworks and revenue models
- Financial planning templates and projections
- Tax compliance references
- Cost tracking and optimization
- Financial metric definitions

## What Does Not Belong Here

- Live financial data (lives in banking and accounting systems)
- Invoices (generated from Stripe)
- Client billing details (Operations/Clientele/{Client}/Administrative/)
