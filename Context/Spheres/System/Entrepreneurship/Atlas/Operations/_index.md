---
file_type: reference
venture: Atlas
status: active
last_updated: 2026-05-14
---

# Operations – Atlas

Pilot management, clinical advisor liaison, clinic onboarding, support and the systems that keep deployed Atlas instances running cleanly. Operations is the engine room – it does not decide what gets built, it makes sure what gets built actually serves the clinic.

---

## What Belongs Here

- Pilot clinic management – Arlando Parker Jr. first, then subsequent pilot clinics
- Clinical advisor relationships – cadence, communications, scope tracking
- Customer support workflows – bug triage, escalation paths, ticket management
- Clinic onboarding – EHR connection, staff training, baseline note benchmarking
- Standard operating procedures
- Tool configurations and integrations (operational layer, not product layer)
- Performance monitoring against the validation contract

## What Does Not Belong Here

- Product development and architecture – that goes in Production
- Brand marketing and acquisition campaigns – those go in Growth
- Financial tracking – that goes in Finance
- Agent governance and guidelines – those live at venture root in `Agents/`

## Subdirectories

| Folder | Contents | Status |
|---|---|---|
| Agents/ | Specialist roster, workflow registry, quality criteria | Scaffold |
| Clientele/ | Pilot clinic and clinical advisor folders | Arlando Parker Jr. active |
| SOPs/ | Standard operating procedures | Empty |
| Tools/ | Tool configuration and integration documentation | Empty |
| Templates/ | Reusable templates for recurring operations | Empty |
| Support/ | Support workflows, escalation paths, ticket management | Empty |

## Operations Stack

| Tool | Purpose | Status |
|---|---|---|
| HIPAA-compliant infrastructure | Hosting, storage, audit log persistence | Not yet selected |
| EHR API credentials | Sandbox and production access per pilot | Not yet provisioned |
| Communications channel with Arlando | Cadenced clinical advisor communications | Not yet selected |
| Support ticket system | In-product support for pilot users | Not required pre-pilot |

## Clientele Structure

The Clientele folder follows the venture filing standard with one modification for Atlas: clinical advisors and pilot sites are filed separately from paying clients.

```
Operations/Clientele/
├── Active/
│   ├── Arlando Parker Jr./              – Clinical Advisor (not paying, equity-adjacent terms)
│   └── {future pilot clinics}/ – Pilot sites under pilot agreement
├── Paid/
│   └── {paying clinics}/       – Once Phase 2 paid expansion begins
└── Archive/                    – Past advisors and clinics
```

The Clinical Advisor role at Atlas carries a specific obligation: Arlando is the Reviewer:Behavioural authority for clinical knowledge curation during Phase 1. His clinic is also the pilot site for product validation. Both relationships are documented in his dossier at `Clientele/Active/Arlando Parker Jr./`.

## Current State

Pre-operational. Arlando Parker Jr. dossier in place. Onboarding workflow design pending Direction-gate approval of pilot commercial terms.

## Key Registries

- Clinical advisors and pilot clinics: `Clientele/_clients-registry.md` (to be created)
- SOP catalogue: `SOPs/_sop-registry.md` (to be created)
