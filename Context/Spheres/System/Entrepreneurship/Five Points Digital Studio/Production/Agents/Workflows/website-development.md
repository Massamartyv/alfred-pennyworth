---
file_type: workflow
department: Production
workflow_name: Website Development
venture: Five Points Digital Studio
methodology: The Manor Protocol
last_updated: 2026-04-08
---

# Website Development

Full website build for a new or existing client. Production's most complex workflow -- activates all five specialist roles and runs the complete Manor Protocol lifecycle. Cross-studio workflow that receives direction from Creative and Strategy and hands off to Operations for delivery.

---

## Token Budget

Full site builds are Heavy. The workflow chains multiple steps -- budget the sum per `token-budget-framework.md` multi-step rules.

| Phase | Classification | Budget |
|---|---|---|
| Reconnaissance | Standard | 15,000 |
| Direction (PRD authoring) | Heavy | 30,000 |
| Execution (per page or feature) | Heavy | 30,000 each |
| Critique | Standard | 15,000 |
| Release | Light | 5,000 |

---

## Prerequisites

Before this workflow begins, the following must exist:

- Client folder in `Operations/Clientele/Active/{Client}/` with completed `Onboarding/client-brief.md`
- Engagement scope defined by Growth -- which Website Engineering tier: Rapid, Custom or Platform
- Brand direction from Creative -- either completed brand-identity-build workflow output or existing client brand assets in `Brand Assets/`

---

## Reconnaissance

**Role:** Technical Scout
**Crew:** Explorer

- Load the client brief from `Operations/Clientele/Active/{Client}/Onboarding/client-brief.md`
- Audit the client's existing website if one exists -- tech stack, performance scores, SEO health, accessibility issues
- Competitor technical analysis via Apify MCP -- stack detection, performance benchmarks, feature inventory
- Identify technical constraints: existing integrations, data sources, third-party services to preserve
- Review Creative's brand direction output for technical implications -- animation requirements, custom fonts, image-heavy layouts, video needs
- Surface infrastructure requirements: forms, databases, authentication, CMS, e-commerce, third-party APIs

**Output:** Technical reconnaissance brief saved to `Operations/Clientele/Active/{Client}/Deliverables/Website/technical-recon.md`

**Cross-studio input:** Strategy provides market research. Creative provides brand direction if ready. Operations provides client brief.

---

## Direction

**Role:** Solutions Architect
**Crew:** Strategist

- Clone the PRD template from `Context/vibe-coding-prd-template.md`
- Fill all seven sections by synthesising Creative's brand direction, the technical reconnaissance and Growth's engagement scope:
  1. **Project Grounding and Objective** -- from client brief and engagement scope
  2. **The Vision and "The Vibe"** -- from Creative's brand direction (aesthetic thesis, the tension, animation philosophy, visual references)
  3. **Global Architecture and the Stack** -- Next.js App Router, Tailwind v4 (or vanilla CSS per project), TypeScript strict, animation engine selection, data architecture (Notion as CMS where applicable)
  4. **Universal Engineering Mandates** -- layout rules, typography scale, responsive strategy, component design, spacing system
  5. **Scope and Mechanics** -- sitemap with per-page goals, sections, technical specs, image art direction
  6. **Performance and SEO Requirements** -- Lighthouse targets per project tier, SEO rules, AEO implementation, accessibility mandates
  7. **AI Mega-Prompt Injection** -- synthesised system prompt for vibe coding sessions
- Define the Vercel project structure and Supabase requirements if any
- Identify which Website Engineering tier governs the build (Rapid, Custom or Platform) -- this affects depth of every section

**Output:** Completed Vibe Coding PRD saved to `Operations/Clientele/Active/{Client}/Deliverables/Website/prd.md`

**Hard gate: human approval required before proceeding.**

The PRD is the most consequential gate. It is the constitution for the entire build. Everything downstream is measured against it. Creative's brand direction feeds in, but the PRD is Production's document -- it translates aesthetic intent into engineering specifications.

---

## Execution

**Role:** Engineer
**Crew:** Creator

- Clone the Next.js starter template from `Templates/Website/nextjs-starter/` into `Operations/Clientele/Active/{Client}/Deliverables/Website/{project-slug}/`
- Initialise the git repository
- Create a Vercel project via Vercel MCP (Five Points team account)
- Create a Supabase project via Supabase MCP if database is required
- Configure environment variables in Vercel
- Load the AI Mega-Prompt from Section 7 of the PRD at the start of every coding session
- Build to the PRD specification, page by page per Section 5's sitemap:
  - Global layout: root layout.tsx, globals.css, design tokens, navigation, footer
  - Per-page components following the PRD's section-by-section specs
  - Animation implementation per the PRD's interaction philosophy
  - Form handling, data integration, CMS connection as specified
  - SEO implementation: metadata, JSON-LD schema, sitemap.ts, robots.ts per the PRD
  - Responsive implementation per the PRD's responsive strategy
- Follow conventional commit standards
- Deploy preview builds to Vercel for iterative review

**Output:** Functional website deployed to a Vercel preview URL, matching the PRD specification.

Execution may span multiple sessions. Each session loads the PRD's Mega-Prompt. The Engineer builds incrementally -- global shell first, then page by page, then polish and integration. Complex builds (Platform tier) may require multiple Execution-Critique cycles before the final Critique gate.

**Cross-studio hand-off:** Once the preview URL is live, Creative's Editor receives it for visual quality evaluation.

---

## Critique

**Role:** QA Engineer
**Crew:** Evaluator

This phase runs two parallel evaluations. Both must pass for Release.

### Production evaluation (QA Engineer)

Run the build against the six criteria in `Criteria/technical-quality-rubric.md`:

1. **Code quality** -- review against PRD engineering mandates
2. **Performance** -- Lighthouse audit targeting scores from PRD Section 6
3. **Accessibility** -- WCAG AA automated scan plus manual keyboard and screen reader check
4. **SEO completeness** -- verify metadata, schema markup, sitemap, robots, canonical URLs
5. **Security** -- verify headers, environment variable hygiene, no exposed secrets
6. **Responsiveness** -- test at mobile (375px), tablet (768px), desktop (1280px+)

### Creative evaluation (Editor, Creative studio)

Creative's Editor evaluates the preview URL against Creative's four criteria (`Creative/Agents/Criteria/quality-rubric.md`):

1. **Brand alignment** -- does the built site feel like the brand direction specified?
2. **Originality** -- is it distinctive in the client's market?
3. **Craft and finish** -- are visual details precise?
4. **Emotional resonance** -- does it connect?

### Output

Two critique reports:
- Technical critique report from QA Engineer -- pass or fail per criterion with specific findings
- Visual critique report from Creative's Editor -- pass or fail per criterion with revision notes

Any Failing criterion on either report sends the work back to Execution with specific notes on what must improve.

**Hard gate: human approval required before proceeding.**

---

## Release

**Role:** Release Engineer
**Crew:** Maestro

- Promote the Vercel deployment from preview to production
- Configure the custom domain in Vercel
- Run production smoke test: all pages load, forms submit, analytics fire, schema validates
- Generate a project summary for client delivery -- what was built, where it lives, how to access it
- Hand off to Operations:
  - Production URL and Vercel dashboard access details
  - Operations executes `SOPs/project-handoff.md` for client ownership transfer
  - Client folder updated: archive the PRD and technical recon as project history
- Hand off to Knowledge Base: case study material for the institutional archive

**Output:** Live production website, delivered to Operations for client handoff.

---

## Cross-Studio Flow

The end-to-end chain for a website engagement:

1. **Growth** closes the deal. Defines engagement scope and tier (Rapid, Custom or Platform). Hands off to Operations.
2. **Operations** onboards the client. Creates the client folder from template. Populates `Onboarding/client-brief.md`. Hands off to Strategy and Creative in parallel.
3. **Strategy** runs competitive research and market positioning. Output goes to Creative (for brand direction) and Production (for technical reconnaissance).
4. **Creative** runs the brand-identity-build or client-brand-direction workflow. Produces brand direction -- visual identity, voice, content. Hands off to Production.
5. **Production** receives all of the above. Runs this workflow.
6. During Critique, **Creative** receives the preview URL and runs its quality rubric evaluation. Returns visual critique report to Production.
7. **Production** runs its technical quality rubric evaluation. Both critique reports go to the human gate.
8. After Release, **Operations** receives the production URL and executes client delivery. Operations runs the project-handoff SOP when the client takes ownership.
