---
file_type: reference
document_type: department_heads
venture: Martywood
status: active
last_updated: 2026-09-10
---

# Department Heads – Martywood

The organisational structure of AI-assisted roles within Martywood. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

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

### Head of Foundation

| Field | Value |
|---|---|
| Department | Foundation |
| Domain | Master brand fingerprint stewardship, community initiatives, cultural philanthropy, mentorship |
| Primary files | `Foundation/_index.md`, `Foundation/brand-fingerprint.md` |
| Reports to | You (Creative Director) directly through Alfred |

---

### Head of Administration

| Field | Value |
|---|---|
| Department | Administration |
| Domain | Legal, licensing, brand protection, platform compliance, policies |
| Primary files | `Administration/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Content licensing, IP filings, contracts, sponsorship agreements |
| Compliance Officer | Platform terms, privacy policies, music licensing, rights clearance |
| Brand Protection Lead | Trademark monitoring, brand misuse response, reputation management |

---

### Head of Finances

| Field | Value |
|---|---|
| Department | Finances |
| Domain | Revenue (subscriptions, sponsorships, merchandise, speaking, consulting), expenses, projections |
| Primary files | `Finances/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finances:**

| Role | Scope |
|---|---|
| Revenue Analyst | Subscription MRR, sponsorship revenue, cohort analysis |
| Financial Reporter | P&L, cash flow statements, monthly and quarterly reports |
| Compliance Validator | Tax readiness, platform compliance, audit trails |

---

### Head of Business Development

| Field | Value |
|---|---|
| Department | Business Development |
| Domain | Audience growth, partnerships, sponsorships, collaborations, guest booking, positioning and market strategy |
| Primary files | `Business Development/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Business Development:**

| Role | Scope |
|---|---|
| Audience Growth Lead | Subscriber growth tactics, cross-platform expansion, referral loops |
| Partnership Scout | Identifying collaboration opportunities, aligned creators, brand partners |
| Sponsorship Lead | Sponsor outreach, qualification, proposal terms, negotiation |
| Guest Coordinator | Conversation guest identification, outreach, booking, preparation |

---

### Head of Marketing & Sales

| Field | Value |
|---|---|
| Department | Marketing & Sales |
| Domain | Brand voice, editorial direction, aesthetic standards, cultural perspective, content product definitions, sponsorship sales process once a pipeline reaches proposal stage |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `brand-fingerprint.md`, `Marketing & Sales/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Marketing & Sales:**

| Role | Scope |
|---|---|
| Editorial Director | Epiphany voice, Conversation themes, content pillars, editorial calendar |
| Cultural Curator | Trend sensing, cultural references, curation of ideas and influences |
| Brand Voice Guardian | Consistency across platforms, tone calibration per channel |
| Visual Director | Social aesthetics, cover art, visual storytelling standards |

---

### Head of Operations

| Field | Value |
|---|---|
| Department | Operations |
| Domain | Content pipeline, scheduling, distribution, tool administration, sponsor and collaborator management |
| Primary files | `Operations/_index.md`, `Operations/SOPs/_sop-registry.md`, `Operations/Clientele/_clients-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Pipeline Manager | Content pipeline tracking – ideation through publication |
| Distribution Coordinator | Syndication scheduling via Pennyone, cross-platform publishing, Epiphany delivery |
| Systems Administrator | Tool configuration, integration management, workflow automation |
| Clientele Coordinator | Sponsor, collaborator and featured guest relationship management |

---

### Head of Product Development

| Field | Value |
|---|---|
| Department | Product Development |
| Domain | Conversation production, Epiphany production, music production, social and video production, physical products and merchandise |
| Primary files | `Product Development/_index.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Product Development:**

| Role | Scope |
|---|---|
| Conversation Producer | Conversation planning, recording prep, show notes, audio post-production via ElevenLabs |
| Epiphany Producer | Epiphany drafting, formatting, Substack publishing workflow |
| Social Content Producer | Platform-native content creation, asset preparation, caption writing |
| Quality Assurance | Pre-publish review for all content types – voice, accuracy, formatting |

---

### Head of Human Resources

| Field | Value |
|---|---|
| Department | Human Resources |
| Domain | Team and contractor onboarding, hiring plans, culture documentation |
| Primary files | `Human Resources/_index.md` |
| Reports to | Alfred |

---

### Head of Knowledge Base

| Field | Value |
|---|---|
| Department | Knowledge Base |
| Domain | Audience research, platform intelligence, cultural trend sensing, competitive analysis |
| Primary files | `Knowledge Base/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Knowledge Base:**

| Role | Scope |
|---|---|
| Audience Researcher | Subscriber demographics, engagement behaviour, segment mapping |
| Platform Strategist | Channel-specific performance, algorithm awareness, format fit |
| Cultural Analyst | Emerging movements, audience zeitgeist, trend timing |
| Competitive Intelligence | Adjacent creators, category shifts, reference brands |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Martywood – Department Heads v3.0 – 2026-09-10 – The Restoration: nine departments restored, replacing the seven-studio model. Previously v2.1 – 2026-06-11 – crew taxonomy migrated to five-crew model*
