---
file_type: department_agent_index
department: Operations
venture: Five Points Digital Studio
methodology: The Manor Protocol
last_updated: 2026-09-10
---

# Operations – Agent Roster and Workflow Registry

The Operations department is the engine room and the execution arm. Client delivery, SOPs, tools, the Clientele directory, and every deliverable build – websites, templates, integrations, media assets – that ships to a client. Operations absorbs the former Production department's build roster in full: every piece of work that enters or exits the build side of this department is held to the technical quality rubric defined in `Criteria/technical-quality-rubric.md`.

See venture-level `Agents/department-heads.md` for the Head of Operations role definition and specialist seats.

---

## Specialist Roles

| Role | Function | Primary Phase | Primary Crew |
|---|---|---|---|
| **Head of Operations** | Department head. Owns delivery throughput, SOP integrity, build quality and deployment standards. | All | – |
| **Client Success Lead** | Onboarding, account management, retention, offboarding. | Execution, Release | Broadcaster, Creator |
| **SOP Architect** | Standard operating procedure design, maintenance, rollout. | Direction, Execution | Creator, Reviewer:Scrutiny |
| **Systems and Tools Lead** | Tool stack, automation workflows, integration management. | Reconnaissance, Execution | Researcher, Creator |
| **Technical Scout** | Audits the client's existing digital footprint, competitor site performance and technical constraints. Maps the landscape. | Reconnaissance | Researcher |
| **Solutions Architect** | Writes the Vibe Coding PRD. Translates Marketing & Sales's brand direction into a build specification – stack decisions, component architecture, engineering mandates, performance budgets. | Direction | Creator |
| **Engineer** | The hands. Builds the site to the PRD specification. Clones the starter template, writes components, implements animations, integrates data sources. | Execution | Creator |
| **QA Engineer** | Runs the build against the technical quality rubric. Does not fix – evaluates with precise notes. | Critique | Reviewer:Scrutiny |
| **Release Engineer** | Deploys to production, configures DNS, runs smoke tests, hands off for client delivery. | Release | Broadcaster |

### Role activation

Client onboarding activates the full delivery-management roster. SOP revisions activate SOP Architect. Tool evaluations activate Systems and Tools Lead. A copy swap may only need the Engineer. A component hotfix may need the Engineer and QA Engineer. A full website build activates Technical Scout, Solutions Architect, Engineer, QA Engineer and Release Engineer.

---

## Workflow Registry

| Workflow | Description | File |
|---|---|---|
| Website Development | Full website build for a new or existing client | `Workflows/website-development.md` |

Planned (not yet built):
- Component Library Build
- Template Build
- Site Maintenance

---

## Quality Gate

All build output passes through Critique before Release. The evaluation criteria live in `Criteria/technical-quality-rubric.md`. The six non-negotiable technical standards:

1. **Code quality** – Is it clean, maintainable and faithful to the PRD?
2. **Performance** – Does it meet Lighthouse and Core Web Vitals targets?
3. **Accessibility** – Does it meet WCAG 2.1 AA?
4. **SEO completeness** – Are metadata, schema, sitemap and canonical URLs correct?
5. **Security** – Are headers, environment variables and authentication patterns correct?
6. **Responsiveness** – Does it work at every viewport?

Work that fails any one of the six does not release. It returns to Execution with specific notes on what must improve.

Additionally, for website builds, Marketing & Sales's quality rubric (`Marketing & Sales/Agents/Criteria/quality-rubric.md`) is applied to the visual output by Marketing & Sales's Editor. Both the technical gate here and the visual gate at Marketing & Sales must pass before Release.

---

## Cross-Department Dependencies

### Receives from

| Department | What Operations receives |
|---|---|
| **Marketing & Sales** | Brand direction, colour palette, typography system, content, imagery direction |
| **Business Development** | Market research, competitive analysis, audience definition |
| **Product Development** | Engagement scope, offer tier (Rapid / Custom / Platform) |

### Hands off to

| Department | What Operations delivers |
|---|---|
| **Marketing & Sales** | Preview URL for visual quality evaluation during Critique |
| **Knowledge Base** | Case study material after Release |

---

## Context Loading

When operating within Operations:

1. Read venture-root `Agents/_index.md` – Manor Protocol definition
2. Read `Agents/agent-guidelines.md` – execution tiers and red lines
3. Read `Agents/department-heads.md` – role definitions
4. Read `Agents/token-budget-framework.md` – budget tiers
5. Read `Agents/integrations.md` – Vercel, Supabase, Notion connections
6. Read this file – Operations-specific workflows and criteria
7. Read `Operations/_index.md` – department scope
8. Read `Operations/Clientele/_clients-registry.md` – active client roster
9. Read `Operations/SOPs/_sop-registry.md` – SOP catalogue
10. Read `Operations/Templates/New Client/` for onboarding, `Operations/Templates/Standardized Document Library/03-workflow-operations-intake.md` and `06-client-onboarding-packet.md` for onboarding, `07-post-engagement-feedback.md` for offboarding, and `Operations/Templates/client-brand-asset-requirements.md` when onboarding a brand-heavy engagement
11. The relevant workflow file
12. `Criteria/technical-quality-rubric.md` (for Critique phase)
13. Client-specific PRD and brand assets if applicable

---

## Working Directory

Agent scratch space: `.working/five-points-operations/` (create on first use).
