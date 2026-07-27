---
file_type: reference
venture: Atlas
status: active
last_updated: 2026-07-27
---

# Finance – Atlas

Revenue, costs, unit economics and the financial health of the venture. Finance tracks the SaaS metrics that matter at each stage – pre-revenue cost discipline, MRR / NRR / churn at scale, per-clinic unit economics throughout.

---

## What Belongs Here

- Revenue tracking by pilot, paid clinic, channel
- Cost tracking – AI inference per note, infrastructure, support, sales
- Operating expenses by category
- Per-clinic unit economics – CAC, LTV, payback period, margin
- SaaS metrics – MRR, ARR, NRR, churn, expansion rate
- Financial projections and scenario modelling
- Tax preparation, filings, compliance
- Monthly and quarterly P&L, cash flow and management reports

## What Does Not Belong Here

- Personal finances – those live in the personal Notion workspace
- Other venture financial data – each venture is isolated
- Supplier contracts and legal terms – those go in Administration
- Pricing strategy and packaging – that goes in Growth/Offers

## Subdirectories

| Folder | Contents | Status |
|---|---|---|
| Agents/ | Specialist roster, workflow registry, quality criteria | Scaffold |
| Revenue/ | Revenue tracking by pilot, clinic, channel | Empty – pre-revenue |
| Cost Management/ | Inference cost, infrastructure cost, operating expenses | Empty |
| Metrics/ | Unit economics, SaaS metrics, cohort behaviour | Empty |
| Planning/ | Budgets, projections, scenario models | Empty – Phase 1 priority |
| Reports/ | Monthly, quarterly, annual reports | Empty |
| Tax/ | Federal, state, sales tax filings | Empty – post-entity formation |

## Unit Economics Framework

The core financial model for Atlas tracks per-clinic economics across three axes:

### Per-note cost

Inference cost per generated SOAP note plus codes plus plan. This is the unit of consumption. Composed of:

- LLM API cost (Creator crew, Reviewer:Behavioural crew)
- Transcription cost (voice ingest)
- Storage cost (audit log, generated artefacts)
- EHR API call cost (if vendor charges per call)

The benchmark target: per-note cost remains below 10% of per-note pricing.

### Per-clinic margin

Monthly margin per active clinic:

- Revenue (subscription + per-note transaction if hybrid)
- Less inference cost at projected volume
- Less infrastructure allocation
- Less support cost allocation

Target: 70% gross margin per clinic at maturity.

### Cohort behaviour

Monthly cohort retention, expansion within cohort, churn drivers. Healthcare SaaS in chiropractic should retain at >95% annually if the product fits.

## SaaS Metric Targets (forward-looking)

| Metric | Phase 2 target | Phase 4 target |
|---|---|---|
| MRR | $50K | $1M+ |
| Active clinics | 50 | 1,000+ |
| Per-clinic ARPU | $1,000 / month | $1,000 / month |
| Gross margin | 60% | 75%+ |
| Net Revenue Retention | 100% | 115%+ |
| CAC payback | < 12 months | < 6 months |
| Annual churn | < 10% | < 5% |

These targets are aspirational and refined post-pilot. They exist to anchor the scale ambition – billion-dollar trajectory requires the path from $50K MRR to $50M+ ARR within five years, which means the unit economics need to support a path to $50M ARR with healthy margins, not just the first $1M.

## Active State

Live state: Notion Projects and Tasks, Five Points workspace.

## Key Registries

- Unit economics model: `Metrics/_unit-economics.md` (to be created)
- Revenue dashboard: `Revenue/_revenue-dashboard.md` (to be created)
- Projection model: `Planning/_projection-model.md` (to be created)
