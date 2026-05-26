# Notion Touch-Point Audit – Personal and Five Points

**Date:** 2026-05-26
**Trigger:** Operator request to inventory every Notion interaction across all cadences and harden each against Notion 3.5's agentic capabilities.
**Methodology:** Local recon across Automations, Integrations, Agents, Skills, Spheres, CLAUDE.md. Notion-side search and known MEMORY IDs. Cross-checked against Dashboard structure.

---

## Ironclad rating definition

Each touch point is rated on five axes, 0 to 2 each, maximum 10:

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| Capture friction | High – operator has to remember and click through several surfaces | Some friction, but ritualised | Single tap or automatic |
| Retrieval value | Data goes in, nothing comes out | Useful when manually queried | Surfaces itself when needed |
| Automation | Pure manual | Partly scripted | Scheduled or event-triggered |
| Interconnection | Isolated entries | Some relations | Fully wired to Sphere Manager and adjacent databases |
| 3.5 readiness | No agentic features apply | Some apply if built | Already on a 3.5-native path |

**Targets:** 8+ ironclad, 5-7 healthy, below 5 needs work.

---

## Daily

| # | Touch point | Surface | Cadence | Rating | Notes |
|---|---|---|---|---|---|
| D1 | Inbox capture | Inbox database `bdfa49b5-...` | Constant | 6 | iMessage → Inbox path is documented; AI Autofill could auto-suggest Sphere and Type |
| D2 | Tasks status updates | Tasks `bdfa49b5-...` | Continuous | 6 | GTD next-action discipline exists; no automatic stale-detection sweep |
| D3 | Habits log | Habits `098c6a57-...` | Daily | 5 | Manual entry. Strava partially closes movement; nothing closes stillness, journal, keystone |
| D4 | Strava → Fitness Journal | Fitness Journal `9084eeda-...` | Per activity | 8 | strava MCP `strava_sync_activity_to_notion`. Already event-triggered, well-wired |
| D5 | Reflections – Morning Pages | Reflections `f0025f83-...` | Daily | 7 | Now categorised post-rename. Template exists. No scheduled trigger; relies on operator |
| D6 | Reflections – Dream Journal | Reflections `f0025f83-...` | When dreamed | 6 | New category as of 2026-05-23. Template exists |
| D7 | Currently Reading | Currently Reading `c59b6a29...` | Daily glance | 7 | Wired to Literature, surfaced on Dashboard |
| D8 | Content Calendar draft / status | Content Calendar `ad36d098-...` | Daily | 7 | Pennyone publisher updates status on publish. Drafting still manual |
| D9 | Watchtower threshold sweep | Cross-database | Continuous + 20:00 sweep | 6 | Personal scope only. Five Points pending |
| D10 | Decision Log entries | Decision Log `238912a8-...` | Event | 7 | Standard format documented. Manual write |

## Weekly

| # | Touch point | Surface | Cadence | Rating | Notes |
|---|---|---|---|---|---|
| W1 | Weekly Review | Reflections, template `33218961-...` | Sunday 90 min | 7 | Just rebuilt. Six-movement ritual, 11 inline deck views. Custom Agent build sheet handed off; not yet scheduled |
| W2 | Watchtower Monday 09:00 briefing | Cross-database | Weekly | 7 | Live for personal. Briefing crew Broadcaster |
| W3 | Pennyone weekly content batch | Content Calendar | Weekly | 6 | Manual batch creation. Publish is automated |
| W4 | Reach Out / Reconnection pass | Reconnection `7b46ab48...` | Weekly inside Weekly Review | 6 | Inline view present, manual triage |
| W5 | Content Calendar week-ahead | Content Calendar | Sunday into the week | 5 | No automated digest of what is scheduled vs. what is missing |

## Monthly

| # | Touch point | Surface | Cadence | Rating | Notes |
|---|---|---|---|---|---|
| M1 | Monthly Review | Reflections, template `33218961-65cf-80b9...` | First Sunday of month | 5 | Template exists. No content yet, no scheduled trigger |
| M2 | media-scanner agent | Media `a2368097-...`, Literature `1995c30b-...` → Culture cluster | 1st of month | 7 | Claude Code subagent, fires from heartbeat |
| M3 | Sphere Achievements review | Achievements `bfd6a3ba-...` | Monthly | 4 | Surfaced on Dashboard, no ritual binding it to action |
| M4 | Finances reconciliation | Finances database | Monthly | 3 | Pending Finance Dashboard automation. Manual today |
| M5 | Content retrospective | Content Calendar | Monthly | 4 | No regular retrospective ritual |

## Quarterly

| # | Touch point | Surface | Cadence | Rating | Notes |
|---|---|---|---|---|---|
| Q1 | Quarterly Review | Reflections, template `33218961-65cf-8012...` | Quarter end | 5 | Template exists, content blank |
| Q2 | sphere-review agent | Sphere Manager, Spheres files | Quarterly | 7 | Reviewer:Scrutiny crew. Validates alignment |
| Q3 | Quarterly Business Review – Five Points | FP workspace | Quarterly | 6 | Template exists in personal workspace search results; FP execution discipline TBD |
| Q4 | Fitness phase transitions | Body sphere file + Fitness Journal | Quarterly-ish | 7 | Current Cut Apr 1 → Sep 30; phase tracked in global CLAUDE.md and Body sphere |

## Annual

| # | Touch point | Surface | Cadence | Rating | Notes |
|---|---|---|---|---|---|
| A1 | Annual Review | Reflections, template `33218961-65cf-800f...` | Year end | 4 | Template exists, content blank |
| A2 | Annual Achievements | Achievements `bfd6a3ba-...` | Year end | 5 | Dashboard view exists. No ritual yet |
| A3 | Sphere prioritisation reset | Sphere Manager + global CLAUDE.md | Annual | 5 | Implicit; no formal ritual |
| A4 | Year-in-Review content | Content Calendar + Marty Gras | Annual | 4 | No system; opportunity for the cultural side |

## Anniversary / Birthday

| # | Touch point | Surface | Cadence | Rating | Notes |
|---|---|---|---|---|---|
| AB1 | Birthday surfacing | Birthday Calendar `b1a86e6c...` | Per person | 7 | Surfaced on Dashboard; reconnection trigger |
| AB2 | Anniversary surfacing | Anniversary Calendar `ce1740ac...` | Per person | 6 | Same pattern, less used |
| AB3 | Gift baskets via gift-shopper | Contacts Giftshop section | On occasion | 8 | Skill writes back to Contact's Giftshop with bookmark embeds. Well-wired |

## Ad-hoc and event-triggered

| # | Touch point | Surface | Trigger | Rating | Notes |
|---|---|---|---|---|---|
| X1 | Permanent Notes | Permanent Notes `7b032882...` | When an idea crystallises | 6 | Surfaced on Dashboard |
| X2 | Topics / Resources | Topics, Resources | New learning area | 5 | Less used; could benefit from AI Autofill enrichment |
| X3 | Recipes via michelin-chef | Notion recipe DB (per skill description) | Cooking session | 7 | Skill-driven write-back |
| X4 | Workouts via personal-trainer | Fitness Journal | Live session | 8 | Conversational logging skill, PR detection |
| X5 | Discovery via discovery-architect | Five Points CRM | New FP lead | 7 | Venture-scoped, well-defined |
| X6 | Travel Journal entries | Reflections, Travel Journal category | Per trip | 7 | Wired post-rename, linked to Cities |
| X7 | Cities updates | Cities `73c32463-...` | Post-trip | 6 | Two-signal convention documented |
| X8 | Performance Calendar | Performance Calendar `bc26ce85...` | Event ahead | 6 | Surfaced on Dashboard |
| X9 | Supermarket | Supermarket `2cd1fd81...` | Before shopping | 5 | Surfaced on Dashboard |
| X10 | Five Points Tasks/Projects/Decisions | FP workspace | Per work | 7 | Discipline established 2026-05-05 |
| X11 | session-audit skill writes | Memory + Notion Inbox if relevant | Session end | 6 | Optional; operator-confirmed |

## Continuous and threshold-triggered

| # | Touch point | Surface | Trigger | Rating | Notes |
|---|---|---|---|---|---|
| C1 | Watchtower threshold alerts | Cross-database | Threshold | 6 | Personal scope only |
| C2 | Pennyone status updates | Content Calendar | On publish | 8 | Bridge handles status transitions |
| C3 | Strava activity sync | Fitness Journal | On activity | 8 | Working pipeline |

---

## Patterns across the matrix

**Strengths (8+ rated).** D4 Strava sync, AB3 gift-shopper, X4 personal-trainer, C2 Pennyone status, C3 Strava activity. All share the same DNA: event-triggered, single-purpose pipelines with the skill or integration owning the write-back.

**Mid-tier (5-7 rated).** Most operational rituals. Templates exist; triggers do not. Capture is fine; retrieval is on-demand only.

**Weak points (below 5).** M3 Sphere Achievements, M4 Finances reconciliation, M5 Content retrospective, A1 Annual Review, A4 Year-in-Review, W5 Content week-ahead. Pattern: longer-cadence rituals where no automation closes the loop and operator memory is the only trigger.

---

## Notion 3.5 capability mapping

For each capability, the touch points it would lift:

### Custom Agents with schedules
- **Sunday 21:00 ET Weekly Review trigger** – W1 (already in V8 build sheet)
- **Monday 09:00 ET Briefing dispatcher** – W2 (Watchtower's existing routine; consider migrating from Claude Code scheduled task to Notion-native Custom Agent)
- **First Sunday of month Monthly Review** – M1 (new)
- **First day of quarter Quarterly Review** – Q1 (new)
- **31 December Annual Review** – A1 (new)
- **First of month media scan** – M2 (consider migration from Claude Code subagent)
- **First of quarter sphere review** – Q2 (consider migration)
- **Mid-week Content Calendar gap check** – W5 (new)
- **Monthly finance reconciliation prompt** – M4 (until Finance Dashboard ships)
- **Sphere Achievements monthly prompt** – M3 (new)

### AI Autofill on databases
- **Inbox auto-tagging** – D1. Sphere and Type predicted from title and content
- **Tasks effort estimation** – D2. Suggest pomodoro count
- **Permanent Notes auto-link to Topics and Spheres** – X1
- **Topics / Resources enrichment** – X2. Summary, related Spheres
- **Cities post-visit enrichment** – X7. Auto-fill insights from a Travel Journal entry that referenced the city

### External Agents API (Claude Code as agent)
- **Weekly Review Phase 2** – W1. Pre-population from data sources, swap in once waitlist clears
- **Discovery dispatch for FP leads** – X5. From inside FP Notion, dispatch Claude Code with the discovery-architect skill
- **Recipe logging from cooking session** – X3. From a recipe page, dispatch michelin-chef
- **Workout logging from gym** – X4. From Fitness Journal, dispatch personal-trainer

### Workers
- **Weekly Review data pull** – W1, the rich pre-population (covered in v9 memo)
- **Decision Log weekly digest** – consumer of Decision Log writing to Alfred OS Project
- **Sphere Manager pulse rollup** – computed properties

### Database Sync
- **Strava → Fitness Journal** – D4. Could move from FastMCP to native Database Sync if Strava is supported. Cuts a layer
- **Stripe → Five Points revenue** – M4, FP scope. Native sync would replace pending Finance Dashboard script
- **Gmail / Apple Mail → Reach Out** – W4. Auto-create reach-out cards from sender history

### n8n MCP integration
- Cross-app automations between Notion and platforms without a dedicated MCP. Likely not a priority over Custom Agents

---

## Prioritised optimisation roadmap

Ordered by impact-to-effort ratio. Items 1-3 are the high-leverage moves.

### 1. Cadence triggers cluster – ship five Custom Agents at once
Build the full set of recurring triggers as one operator task in the Notion UI:
- Sunday 21:00 ET Weekly Review
- First Sunday of month Monthly Review at 21:00 ET
- First day of quarter Quarterly Review at 09:00 ET
- 31 December 21:00 ET Annual Review (or first Sunday of new year)
- Mid-week Wednesday 09:00 ET Content Calendar gap check

Each agent creates a new entry from the existing template, sets properties, and notifies the operator. Phase 1 uses Notion AI; Phase 2 swap to Claude Code once V7 waitlist clears.

**Lift:** turns five mid-rated rituals into 8+ ironclad triggers. **Effort:** 20 to 30 minutes operator UI work, batched. Already has the build-sheet pattern from V8.

### 2. AI Autofill on Inbox and Permanent Notes
Switch on AI Autofill for Sphere prediction on Inbox capture, and for Topics/Spheres auto-link on Permanent Notes. The operator captures; Notion auto-classifies; sphere context is preserved without manual tagging.

**Lift:** drops D1 capture friction; raises X1 retrieval value. **Effort:** UI configuration, 10 minutes.

### 3. Watchtower Five Points scope completion
The watchtower agent is documented as personal-scope only. Extending to FP closes the venture parity gap. Could ship as a Notion Custom Agent that reads FP databases natively rather than via Claude Code dispatch.

**Lift:** raises FP operational hygiene; closes a known pending in MEMORY. **Effort:** medium; depends on whether to migrate Watchtower to Notion-native or keep as Claude Code.

### 4. Finance Dashboard automation
Long-standing pending. Should this still be a Python script in Automations/, or does Notion 3.5 Database Sync from Stripe make it native? Worth the audit before code is written.

**Lift:** unlocks M4 monthly reconciliation. **Effort:** scoping first, build second.

### 5. Annual rituals get definition
A1, A4, A2 are sitting at 4-5. Year-in-Review especially is a Marty Gras opportunity. Define the ritual, define the deliverable, then schedule the trigger. Could anchor to 31 December or first Sunday of the new year.

**Lift:** turns four annual touch points into ironclad. **Effort:** half a session for the ritual design, plus the Custom Agent build.

### 6. Decision Log weekly digest Worker
A small Notion Worker that reads the past seven days of Decision Log entries and writes a digest under the Alfred OS Project. Becomes a free experimentation target before the 2026-08-11 paid Workers transition.

**Lift:** raises Decision Log retrieval value; tests Workers before they cost money. **Effort:** small.

### 7. Codex / Skills inventory page
Confirm whether the "Codex" referenced in skill descriptions (prompt-creator, others) is a Notion database. If not, build it. The skills inventory deserves a Notion home.

**Lift:** completes the system's self-documentation in Notion. **Effort:** small if no DB exists yet.

---

## Open questions before Direction

1. Notion-native versus Claude Code dispatch for each Custom Agent. Which is the default? Notion AI is less powerful but no waitlist; Claude Code is richer but waitlist.
2. Five Points scope in this audit – do the FP touch points get the same Custom Agent treatment as personal?
3. Marty Gras subset – does it get its own touch-point map, or does it inherit personal patterns?

---

## Inventory totals

**Personal databases touched:** 27 distinct surfaces across daily/weekly/monthly/quarterly/annual/ad-hoc/continuous cadences.

**Average rating:** approximately 6.0 across all touch points. Healthy baseline; strong head room.

**Touch points already at 8+:** D4 Strava sync, AB3 gift-shopper, X4 personal-trainer, C2 Pennyone status, C3 Strava activity.

**Touch points below 5:** M3 Sphere Achievements, M4 Finances, M5 Content retrospective, A1 Annual Review, A4 Year-in-Review, W5 Content week-ahead.
