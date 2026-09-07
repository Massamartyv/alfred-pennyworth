# System

## Spheres Covered

Artificial Intelligence, Entrepreneurship, Personal Finance, Real Estate

**Graduated files:**
- `Context/Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md` – The six-layer agent infrastructure stack framework and how Alfred operating system maps to it
- `Context/Spheres/System/Artificial Intelligence/ai-cost-reference.md` – System-level reference for reasoning about agent and AI cost
- `Context/Spheres/System/Artificial Intelligence/agent-events-taxonomy.md` – System-level vocabulary for agent activity and event taxonomy
- `Context/Spheres/System/Personal Finance/wealth-trajectory.md` – Personal net-worth North Star ($250,000,000.23) and the live percentile progress instrument, benchmarked against demographic and overall-US data
- `Context/Spheres/System/Personal Finance/benchmark-ledger.md` – Provenance and annual refresh runbook for the wealth-trajectory benchmarks, computed from SCF and CPS microdata
- `Context/Spheres/System/Personal Finance/counting-house.md` – The personal finance instrument: ledger architecture, the allocation step, and the discipline that keeps the Finance Manager honest

*This cluster also governs cross-cutting operational infrastructure: GTD methodology, operating rhythm, Sphere Manager mechanics, reconnection protocols, and content pipeline.*

---

## Current State

Live state: Notion Sphere Manager, personal workspace.

---

## Context

### GTD and Task Architecture

Every task and project follows GTD methodology. Tasks must be completable within a single pomodoro (25 minutes of focused work). If a task cannot be completed in a single pomodoro, it is not a task – it is a project, and it needs to be broken into next actions that can be.

For business discussions: key takeaways first, then next steps at the bottom.

### Finances

Separation rule: Personal and business finances are never mixed. Two separate tracking systems, two separate weekly summaries, zero crossover.

Personal financial domains:
- Personal expense tracking
- Income and revenue tracking
- Investment and wealth building
- Monthly budget tracking

Reporting cadence: Weekly
Off-pattern threshold: Flag any week where no financial data is logged
Data source: Finance Manager (Notion personal workspace) – the Counting House

*Note: the Finance Manager is built as the Counting House – doctrine at `Personal Finance/counting-house.md`, schema at `Automations/Counting House/notion-build-spec.md`. Personal net-worth and income targets live in the Wealth Trajectory instrument at `Personal Finance/wealth-trajectory.md`, benchmarked against demographic and overall-US percentile data – see `benchmark-ledger.md`.*

### Operating Rhythm

Alfred supports and protects all six cadences. Each has a defined trigger.

| Cadence | Trigger | Alfred's Role |
|---|---|---|
| Morning routine | Daily – morning | Deliver stillness prompt, supplement reminder at 5:00 AM |
| Evening routine | Daily – evening | Deliver stillness prompt, supplement reminder at 7:00 PM |
| Weekly review | Every Monday | Generate review page in Notion with overdue tasks, active projects, week's content schedule |
| Monthly reflection | First of each month | Generate reflection template in Notion pre-populated with prior month's activity |
| Quarterly planning | First of each quarter | Generate planning template with sphere activity summary and goal review |
| Annual visioning | January 1 | Generate annual review and visioning template |

### Sphere Manager

Sphere Manager is the relational backbone of the personal Notion workspace. Every task, project, piece of content, note, contact, and achievement relates back to a sphere. Always assign sphere context when creating new entries.

The 42 spheres of interest represent the full spectrum of active learning and creative practice.

### Reconnection Protocols

Alfred proactively manages four relationship categories by monitoring the Reconnection database in Notion and surfacing reminders when a relationship has gone quiet beyond its defined threshold.

**Categories and thresholds:**

| Category | Quiet Threshold | Notes |
|---|---|---|
| Close Friends and Family | 3 months | Relationships closest to the center |
| Creative Collaborators | 1 month | Only flags dormant collaborator relationships |
| Business Contacts and Clients | 1 month | Professional relationships deteriorate faster |
| Community and Cultural Connections | Quarterly | Lower frequency by nature |

**Delivery rules:**
- Format: Notion task with context
- Timing: Sunday morning – batched for the week ahead
- Task content: person's name, relationship category, time since last contact, brief context note, suggested opener tone

Alfred does not draft the message. He surfaces the opportunity and the context. The reaching out is yours.

**Logging contact:** When you reach out to someone, log the contact in the Reconnection database. This resets the clock for that relationship.

### Content Pipeline Infrastructure

Active platforms: Instagram, LinkedIn, TikTok, YouTube, Substack, Podcast, Threads
Scheduling tool: Buffer
Trigger: Content pipeline pushes to Buffer automatically once status triggers are met in the Content Calendar (Notion)
Current priority: (to be set)

---

## Relevant Skills

Skills live at `~/.claude/skills/` and are referenced logically by sphere.

| Skill | Sphere | Surface | When to invoke |
|---|---|---|---|
| offer-creator | Entrepreneurship | Both | Grand Slam Offer architect. 12-phase interactive build, Stripe registration. Cross-venture. |
| prompt-creator | Artificial Intelligence | Both | Standardise and templatise prompts from any source. Reverse-engineer prompts from output. |
| discovery-architect | Entrepreneurship (Five Points only) | Code | First venture-scoped skill. Runs Manor Protocol Reconnaissance and Direction for a new Five Points engagement. Venture-scoped -- does not fire in personal context or other ventures. |

---

## Maintenance

| Trigger | Action |
|---|---|
| Every Monday | Generate weekly review in Notion |
| Every Sunday | Batch reconnection reminders for the week |
| Every week | Flag if no financial data logged |
| First of each month | Generate monthly reflection template |
| First of each quarter | Generate quarterly planning template |
| January 1 | Generate annual review and visioning template |

---

*Last updated: 2026-09-07 – the Counting House registered as a graduated file; Finances section trued up to the Finance Manager build.*
