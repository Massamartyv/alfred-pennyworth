---
file_type: department_agent_index
department: Production
venture: Five Points Digital Studio
methodology: The Manor Protocol
last_updated: 2026-06-11
---

# Production – Agent Roster and Workflow Registry

The Production studio is the execution engine for Five Points. Every deliverable that ships – websites, templates, integrations, media assets – passes through Production's hands. Every piece of work that enters or exits this studio is held to the technical quality rubric defined in `Criteria/technical-quality-rubric.md`.

---

## Specialist Roles

| Role | Function | Primary Phase | Primary Crew |
|---|---|---|---|
| **Head of Production** | Department head. Owns build quality, deployment standards and technical excellence across all output. | All | – |
| **Technical Scout** | Audits the client's existing digital footprint, competitor site performance and technical constraints. Maps the landscape. | Reconnaissance | Researcher |
| **Solutions Architect** | Writes the Vibe Coding PRD. Translates Creative's brand direction into a build specification – stack decisions, component architecture, engineering mandates, performance budgets. | Direction | Creator |
| **Engineer** | The hands. Builds the site to the PRD specification. Clones the starter template, writes components, implements animations, integrates data sources. | Execution | Creator |
| **QA Engineer** | Runs the build against the technical quality rubric. Does not fix – evaluates with precise notes. | Critique | Reviewer:Scrutiny |
| **Release Engineer** | Deploys to production, configures DNS, runs smoke tests, hands off to Operations for client delivery. | Release | Broadcaster |

### Role activation

Not every build activates every role. A copy swap may only need the Engineer. A component hotfix may need the Engineer and QA Engineer. A full website build activates all five. Match the roles to the complexity of the work.

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

All Production output passes through Critique before Release. The evaluation criteria live in `Criteria/technical-quality-rubric.md`. The six non-negotiable technical standards:

1. **Code quality** – Is it clean, maintainable and faithful to the PRD?
2. **Performance** – Does it meet Lighthouse and Core Web Vitals targets?
3. **Accessibility** – Does it meet WCAG 2.1 AA?
4. **SEO completeness** – Are metadata, schema, sitemap and canonical URLs correct?
5. **Security** – Are headers, environment variables and authentication patterns correct?
6. **Responsiveness** – Does it work at every viewport?

Work that fails any one of the six does not release. It returns to Execution with specific notes on what must improve.

Additionally, for website builds, Creative's quality rubric (`Creative/Agents/Criteria/quality-rubric.md`) is applied to the visual output by Creative's Editor. Both Production's technical gate and Creative's visual gate must pass before Release.

---

## Cross-Studio Dependencies

### Receives from

| Studio | What Production receives |
|---|---|
| **Creative** | Brand direction, colour palette, typography system, content, imagery direction |
| **Strategy** | Market research, competitive analysis, audience definition |
| **Growth** | Engagement scope, offer tier (Rapid / Custom / Platform) |
| **Operations** | Client brief, client folder structure, communication preferences |

### Hands off to

| Studio | What Production delivers |
|---|---|
| **Creative** | Preview URL for visual quality evaluation during Critique |
| **Operations** | Production URL for client delivery, project-handoff SOP execution |
| **Knowledge Base** | Case study material after Release |

---

## Context Loading

Before any Production task, load in this order:

1. This file (`Production/Agents/_index.md`)
2. `Agents/agent-guidelines.md` (shared governance)
3. `Agents/token-budget-framework.md` (budget tiers)
4. `Agents/integrations.md` (Vercel, Supabase, Notion connections)
5. The relevant workflow file
6. `Criteria/technical-quality-rubric.md` (for Critique phase)
7. Client-specific PRD and brand assets if applicable
