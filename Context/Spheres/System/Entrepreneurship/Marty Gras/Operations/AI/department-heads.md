---
file_type: reference
document_type: department_heads
venture: Marty Gras
status: active
last_updated: 2026-04-05
---

# Department Heads -- Marty Gras

The organisational structure of AI-assisted roles within Marty Gras. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models -- they are role definitions that shape context loading and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head's primary files for context
3. Applies the execution tier from `agent-guidelines.md`
4. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Domain | Brand voice, editorial direction, aesthetic standards, cultural perspective |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `martyv-identity.md` |
| Reports to | You -- Creative Director -- directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope |
|---|---|
| Editorial Director | Newsletter voice, podcast themes, content pillars, editorial calendar |
| Cultural Curator | Trend sensing, cultural references, curation of ideas and influences |
| Brand Voice Guardian | Consistency across platforms, tone calibration per channel |
| Visual Director | Social aesthetics, cover art, visual storytelling standards |

---

### Head of Production

| Field | Value |
|---|---|
| Domain | Podcast production, newsletter production, social content creation |
| Primary files | Product Development/_index.md, Operations/_index.md |
| Reports to | Alfred |

**Specialist roles under Head of Production:**

| Role | Scope |
|---|---|
| Podcast Producer | Episode planning, recording prep, show notes, audio post-production via ElevenLabs |
| Newsletter Producer | Epiphany edition drafting, formatting, Substack publishing workflow |
| Social Content Producer | Platform-native content creation, asset preparation, caption writing |
| Quality Assurance | Pre-publish review for all content types -- voice, accuracy, formatting |

---

### Head of Operations

| Field | Value |
|---|---|
| Domain | Scheduling, pipeline management, distribution, tool administration |
| Primary files | Operations/_index.md, Operations/SOPs/_sop-registry.md |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Pipeline Manager | Content pipeline tracking -- ideation through publication |
| Distribution Coordinator | Buffer scheduling, cross-platform publishing, newsletter delivery |
| Systems Administrator | Tool configuration, integration management, workflow automation |
| Guest Coordinator | Podcast guest scheduling, prep materials, follow-up |

---

### Head of Growth

| Field | Value |
|---|---|
| Domain | Audience analytics, trend sensing, platform strategy, partnership development |
| Primary files | Business Development/_index.md, Marketing & Sales/_index.md |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Audience Analyst | Subscriber growth, engagement metrics, demographic insights |
| Platform Strategist | Channel-specific growth tactics, algorithm awareness, format optimisation |
| Partnership Scout | Identifying collaboration opportunities, sponsor alignment, guest prospects |
| Trend Researcher | Cultural movements, emerging platforms, audience behaviour shifts |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as active -- automated
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Marty Gras -- Department Heads v1.0 -- April 2026*
