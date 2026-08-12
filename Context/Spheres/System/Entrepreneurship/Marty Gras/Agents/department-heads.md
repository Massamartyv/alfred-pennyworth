---
file_type: reference
document_type: department_heads
venture: Marty Gras
status: active
last_updated: 2026-08-04
---

# Department Heads – Marty Gras

The organisational structure of AI-assisted roles within Marty Gras. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that studio scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Researcher, Creator, Reviewer, Mediator, Broadcaster)
4. Applies the execution tier from `agent-guidelines.md`
5. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Studio | Creative |
| Domain | Brand voice, editorial direction, aesthetic standards, cultural perspective, content product definitions |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `martyv-identity.md`, `brand-fingerprint.md`, `Creative/_index.md`, `Creative/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope |
|---|---|
| Editorial Director | Epiphany voice, Conversation themes, content pillars, editorial calendar |
| Cultural Curator | Trend sensing, cultural references, curation of ideas and influences |
| Brand Voice Guardian | Consistency across platforms, tone calibration per channel |
| Visual Director | Social aesthetics, cover art, visual storytelling standards |

---

### Head of Strategy

| Field | Value |
|---|---|
| Studio | Strategy |
| Domain | Audience research, platform intelligence, cultural positioning, competitive analysis |
| Primary files | `Strategy/_index.md`, `Strategy/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Strategy:**

| Role | Scope |
|---|---|
| Audience Researcher | Subscriber demographics, engagement behaviour, segment mapping |
| Platform Strategist | Channel-specific performance, algorithm awareness, format fit |
| Cultural Analyst | Emerging movements, audience zeitgeist, trend timing |
| Competitive Intelligence | Adjacent creators, category shifts, reference brands |

---

### Head of Production

| Field | Value |
|---|---|
| Studio | Production |
| Domain | Conversation production, Epiphany production, music production, social and video production |
| Primary files | `Production/_index.md`, `Production/Agents/_index.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Production:**

| Role | Scope |
|---|---|
| Conversation Producer | Conversation planning, recording prep, show notes, audio post-production via ElevenLabs |
| Epiphany Producer | Epiphany drafting, formatting, Substack publishing workflow |
| Social Content Producer | Platform-native content creation, asset preparation, caption writing |
| Quality Assurance | Pre-publish review for all content types – voice, accuracy, formatting |

---

### Head of Growth

| Field | Value |
|---|---|
| Studio | Growth |
| Domain | Audience growth, partnerships, sponsorships, collaborations, guest booking |
| Primary files | `Growth/_index.md`, `Growth/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Audience Growth Lead | Subscriber growth tactics, cross-platform expansion, referral loops |
| Partnership Scout | Identifying collaboration opportunities, aligned creators, brand partners |
| Sponsorship Lead | Sponsor outreach, qualification, proposal, negotiation |
| Guest Coordinator | Conversation guest identification, outreach, booking, preparation |

---

### Head of Operations

| Field | Value |
|---|---|
| Studio | Operations |
| Domain | Content pipeline, scheduling, distribution, tool administration, sponsor and collaborator management |
| Primary files | `Operations/_index.md`, `Operations/Agents/_index.md`, `Operations/SOPs/_sop-registry.md`, `Operations/Clientele/_clients-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Pipeline Manager | Content pipeline tracking – ideation through publication |
| Distribution Coordinator | Syndication scheduling via Pennyone, cross-platform publishing, Epiphany delivery |
| Systems Administrator | Tool configuration, integration management, workflow automation |
| Clientele Coordinator | Sponsor, collaborator and featured guest relationship management |

---

### Head of Finance

| Field | Value |
|---|---|
| Studio | Finance |
| Domain | Revenue (subscriptions, sponsorships, merchandise, speaking, consulting), expenses, projections |
| Primary files | `Finance/_index.md`, `Finance/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finance:**

| Role | Scope |
|---|---|
| Revenue Analyst | Subscription MRR, sponsorship revenue, cohort analysis |
| Financial Reporter | P&L, cash flow statements, monthly and quarterly reports |
| Compliance Validator | Tax readiness, platform compliance, audit trails |

---

### Head of Administration

| Field | Value |
|---|---|
| Studio | Administration |
| Domain | Legal, licensing, brand protection, platform compliance, policies, HR |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md`, `Administration/HR/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Content licensing, IP filings, contracts, sponsorship agreements |
| Compliance Officer | Platform terms, privacy policies, music licensing, rights clearance |
| Brand Protection Lead | Trademark monitoring, brand misuse response, reputation management |
| People Lead | Team and contractor onboarding, hiring plans, culture documentation |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Marty Gras – Department Heads v2.1 – 2026-06-11 – crew taxonomy migrated to five-crew model*
