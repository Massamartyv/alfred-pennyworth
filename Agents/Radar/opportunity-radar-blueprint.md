---
file_type: design_blueprint
directory: Agents/Radar
status: ready to build – thesis complete
last_updated: 2026-07-07
---

# Opportunity Radar – Fleet Blueprint

A standing reconnaissance system that scans the external landscape for opportunities worth pursuing – fellowships, programs, contracts, jobs, sports-industry roles, international experiences – and lands qualified finds in the existing task and project pipeline for triage.

This document is the fleet doctrine. When the fleet ships, it graduates to `_index.md` for this directory. The application process is explicitly out of scope – it belongs to a future Application Suite (see Handoff Boundary).

---

## Philosophy

Inherited from the Scout methodology and the Researcher crew mandate ("scout trends, sense shifts, surface opportunities"):

1. **Map before you move.** A radar never applies, contacts or commits. It surveys the territory, scores what it finds against a fixed thesis, and reports. Action is a human decision made at triage.
2. **Standing observation, not one-off searches.** Like Watchtower, the radar fleet derives two outputs from one continuous act of observation: a scheduled digest and threshold-triggered alerts.
3. **The thesis is the filter.** Radars do not guess what is interesting. Every find is scored against `Context/opportunity-thesis.md` – the single source of truth for who the candidate is and what a hell-yes looks like. A poorly tuned thesis produces noise; the fix is always to sharpen the thesis, never to let radars freelance.
4. **Travel-aware.** The radar fleet reads current and upcoming locations from the thesis (and, later, travel state) so "cool opportunities where I am or where I'm going" outranks generic remote listings.

---

## Architecture – Three Layers

```
LAYER 1  THE THESIS      Context/opportunity-thesis.md
         Who the candidate is, target domains, geography,
         constraints, scoring rubric. Built by intake interview.
              |
LAYER 2  THE FLEET       Agents/Radar/{domain}-radar.md  x4
         Researcher-crew agents on weekly cadence.
         Each walks its own beat, scores finds against the thesis.
              |
LAYER 3  THE PIPELINE    Existing Notion Tasks + Projects databases
         Finds land as Automated tasks under standing radar
         projects. Triage promotes them toward application.
```

---

## The Fleet

All four radars are Researcher crew, outward-facing (`-radar` suffix per the naming convention in `Agents/_index.md`), model `sonnet`, weekly cadence, working directory `.working/{radar-name}/`.

Radars are typed by **opportunity shape**, not by industry. The industries live in the thesis as a Target Industry Map (below) that every radar weights when scoring – so a fellowship radar find in music production and a contract radar find in sports medicine are both scored against the same industry gravity.

| Radar | Beat | Example sources |
|---|---|---|
| `fellowship-radar` | Fellowships, residencies, accelerators, funded programs with published deadlines | Fellowship aggregators, foundation sites, university program pages, ProFellow-class directories, artist-residency directories |
| `industry-radar` | Insider pipelines of the target industries – roles, contracts and programs published where the industry itself hires | Team/league career boards (TeamWork Online et al.), studio/label/agency career pages, healthtech and sports-science networks, culinary/hospitality placement boards, design-industry boards |
| `contract-radar` | Freelance contracts, consulting engagements and salaried roles matching the skill profile | Contract marketplaces, agency networks, niche job boards matched to thesis skills |
| `international-radar` | Work-abroad programs, cultural exchanges, visa-plus-job pathways, one-off international experiences | Exchange program directories, working-holiday visa programs, embassy cultural programs, international volunteer/paid hybrids |

Beats overlap deliberately (an international sports fellowship could surface on three radars); the pipeline dedupe rule resolves collisions.

### Rollout order

All four are approved. Build all four definitions, but tune in waves: `fellowship-radar` first (highest signal-to-noise – structured opportunities with published deadlines make scoring calibration measurable), then `international-radar`, then `industry-radar`, then `contract-radar` (noisiest; benefits from a thesis already sharpened by the first three).

First two sweeps of each radar run in **calibration mode**: every find in the digest carries its fit rationale so the thesis can be corrected against real output before alerts go live.

---

## The Pipeline – Existing Databases, Zero Schema Changes

Decision: the pipeline lives inside the existing personal Notion **Tasks** and **Projects** databases. No new database. The Tasks schema already carries everything a radar find needs.

### Standing structure (one-time setup)

Project names follow the house register observed in the live Projects database: two-to-three words, Title Case, no punctuation, no plural category labels. Passion projects carry evocative titles; infrastructure carries plain, dignified names. The radar pipeline sits between the two – an evocative parent, plain children that map one-to-one to the agents.

- One parent project: **Open Horizon** (Status: In progress, pinned as desired) – the line the radars watch; everything worth pursuing appears there first
- Four child projects via `Parent Project`: **Fellowship Radar**, **Industry Radar**, **Contract Radar**, **International Radar** – one per radar agent, same name as the agent that feeds it, so each radar writes to exactly one project and triage views stay clean

### How a find lands

Each qualified find becomes a **Task**:

| Task property | Radar writes |
|---|---|
| Name | `{Opportunity title} – {organisation}` |
| Status | `Automated` (the existing agent-created status) |
| Link | Canonical source URL – also the dedupe key |
| Due Date | Application deadline (omit if rolling) |
| Priority | Fit tier: High = hell-yes (fit 5), Medium = strong (fit 4), Low = worth a look (fit 3). Below 3 is digest-only, never written to Notion |
| Project | The radar's child project |
| Sphere | Matched sphere where obvious (e.g. Travel, Martial Arts) |
| Page body | Structured brief: summary, why it fits (thesis criteria cited), requirements with each skill marked ✓ held / ◌ developing per the Skill Ledger, visa-path note for non-U.S. finds, effort estimate, deadline, source links, radar name and sweep date |

### Lifecycle stages

Stages map onto existing Status values – no new fields:

| Stage | Where it shows |
|---|---|
| Surfaced | Task, Status `Automated` |
| Interested | Task, Status `In progress` (set by Marty at triage) |
| Passed | Task, Status `Archived` |
| Applying | Task promoted: a new project is created under the radar's child project carrying the full brief; application work becomes tasks under it. **This promotion is the handoff boundary to the Application Suite.** |
| Submitted / Outcome | Application project Status: `Paused` (awaiting result), then `Done` / `Terminated` |

### Rules

- **Dedupe:** before writing, a radar searches its child project's tasks for the find's Link URL (and near-duplicate names). Collisions across radars resolve to whichever landed first; the later radar appends a note to the existing task instead of duplicating. This extends the Pre-Action Checks duplicate rule.
- **Expiry:** during each sweep, a radar archives its own `Automated` tasks whose Due Date has passed without triage, noting them in the digest as expired-unreviewed (a thesis-tuning signal).
- **Red lines:** radars never apply, register, message anyone, or submit any form. Web access is read-only. Notion writes are limited to the four radar child projects and their tasks. No personal data beyond what the thesis marks as shareable ever appears in search queries.

---

## Cadence and Delivery

Decision: **weekly digest + deadline alerts.**

| Output | Cadence | Content |
|---|---|---|
| Sweep | Weekly, staggered across the fleet (e.g. Sunday evening) | Radars scan sources, score, write qualified finds to the pipeline |
| Digest | Monday morning, alongside the existing portfolio-briefing rhythm | One synthesized digest across all four radars: new finds by fit tier, approaching deadlines, expired-unreviewed, calibration notes. Delivered via iMessage summary, full digest on the Open Horizon project page |
| Deadline alert | Immediate, threshold-triggered | Fit ≥ 4 **and** deadline within 14 days → Watchtower-style iMessage alert. Everything else waits for the digest |

Each radar writes a handoff to `.working/{radar-name}/handoff.md` per `Agents/templates/handoff-schema.md` at the end of every sweep. Heartbeat gains one row per radar plus the digest when the fleet ships.

---

## Layer 1 – The Opportunity Thesis

`Context/opportunity-thesis.md` (cross-cutting file, per convention). **Drafted 2026-07-07** from the intake interview and hell-yes calibration; maintained like a sphere file – updated the moment reality changes, `Last updated` stamped. The thesis is now the authority on scoring; this blueprint keeps only the architecture. One gap remains: the Credentials section.

The thesis includes a **Skill Ledger** – held skills (✓) versus developing skills (◌, the "grayed" state) – added at Marty's direction. Radars read the requirements out of every opportunity's documentation, mark each required skill against the ledger in the find's brief, and the weekly digest aggregates which developing skills recur across strong finds. The fleet is thereby a skills-demand sensor as well as an opportunity sensor: it surfaces what to apply for and what to sharpen.

### Target Industry Map – inferred v0, pending confirmation

Drawn from the spheres, ventures, creative-director file and identity files. Every radar weights finds by industry gravity; sports is one row, not the whole map. The intake interview confirms, re-ranks and prunes this list.

| Industry | Evidence in the system |
|---|---|
| Sports & human performance | Body cluster (martial arts, combat sports, Ironman base-building, strength training), Human Anatomy sphere, Atlas venture, health-and-performance reading |
| Health & wellness innovation | Atlas (chiropractic intelligence), Medicine sphere, nutritional-science philosophy in the creative-director file |
| Media, storytelling & culture | Marty Gras – podcast, Epiphany newsletter, YouTube; "Cultural Facilitator" identity; film and visual storytelling active; Cinema and Photography spheres |
| Music & sound | Music production active discipline, Music Theory sphere, deep genre map in creative-director |
| Design & creative industries | Creative-director sensory operating system, Fashion and Architecture reference-library depth, Interior Design sphere, fragrance/sensory work, Five Points design practice |
| Culinary & hospitality | Full culinary philosophy in creative-director – experimental fusion cooking, restaurant curation, hosting ethos |
| Technology & AI | Artificial Intelligence sphere with graduated infrastructure file, Five Points Digital Studio, JS/Python/Swift spheres, agent systems built in-house |
| Language, culture & education | Spanish active plus five language spheres, Education and Public Speaking spheres, culture-and-anthropology reading – doubles as the international radar's fabric |

### Location Podium

Three cities stand on a podium above all other locations: **New York, Tokyo, Miami** (listed order is the default first/second/third, but the placing is a soft tiebreaker only – membership on the podium is what matters).

How the podium enters scoring:

- An opportunity located in (or relocating to) a podium city gains **+1 fit tier**, capped at 5. A fit-3 find in Tokyo becomes fit 4 – which also makes it eligible for deadline alerts.
- Podium order breaks ties only when two otherwise-equal finds compete for attention in the digest; it never suppresses a find.
- The digest leads with podium-city finds as their own section before everything else.
- Remote/location-agnostic opportunities take no podium boost, but the thesis geography section governs how they rank against placed ones.
- The podium is thesis state – Marty can reorder or swap cities at any time and the change propagates to every radar on its next sweep.

### Intake interview – question set

1. **Candidate profile.** Education, credentials, certifications, languages and levels. What does the strongest version of your CV say?
2. **Skills inventory.** What can you be hired to do today – and what do you want to be hired to do in two years?
3. **Industry map.** Review the inferred Target Industry Map above: confirm, re-rank, prune, add. Within each kept industry, which functions (e.g. for sports: performance/medical, operations, media, tech)? Does the Atlas venture connect to the health/performance rows?
4. **Fellowships and programs.** Fully funded only, or partial? Academic, artistic, entrepreneurial, civic? Duration appetite – weeks, months, a year?
5. **Geography.** The Location Podium is set: New York, Tokyo, Miami. Beyond the podium – where are you now, where are you headed, which regions excite you, which are off the table? Visa/passport situation?
6. **Timing and capacity.** Earliest start date, hours per week available for applications, and how the ventures constrain (or bend for) a big opportunity.
7. **Compensation floor.** Minimum viable pay for contracts/jobs; whether unpaid-but-prestigious ever clears the bar, and under what conditions.
8. **Deal-breakers.** Hard nos – industries, org types, locations, commitments.
9. **Hell-yes calibration.** Three real or hypothetical opportunities you would drop things for, and *why* – this seeds the scoring rubric.
10. **Privacy boundary.** What personal information radars may use in queries, and what stays out of any external search.

Answers become the thesis; the thesis defines the 1–5 fit rubric every radar cites when scoring.

---

## Handoff Boundary – The Application Suite (future build)

Out of scope for the radar fleet, designed against now so the interface is stable:

- **Input contract:** a task promoted to Applying – a project carrying the structured brief (summary, requirements, deadline, links, thesis-fit rationale).
- The suite will own: requirement decomposition into tasks, material drafting (CV tailoring, essays, portfolios – Creator crew, gated by Reviewer per the fresh-context rule), submission checklists, and outcome tracking.
- Anything external-facing (a submission, an email) is irreversible and takes the Critique gate per Manor Protocol rules.

---

## Open Items

| # | Item | Owner |
|---|---|---|
| 1 | ~~Thesis intake interview~~ Done 2026-07-07 – thesis at `Context/opportunity-thesis.md` | – |
| 2 | ~~Credentials section of the thesis~~ Done 2026-07-07 – sourced from the Notion Master Résumé and LinkedIn export | – |
| 3 | Source list per radar – seeded from the thesis, refined every sweep | Alfred drafts, Marty prunes |
| 4 | Create the standing Notion structure (Open Horizon + 4 radar child projects) | Alfred, at fleet build |
| 5 | Write the four radar agent definitions in `Agents/Radar/` + heartbeat entries | Alfred, at fleet build |
| 6 | Digest delivery detail – standalone Monday iMessage vs. folded into the portfolio briefing once that ships | Decide at fleet build |
| 7 | Whether the local Scout skill file carries doctrine beyond what this blueprint inherits – paste it in if so | Marty |

---

*Last updated: 2026-07-07 – v0.6: intake interview and hell-yes calibration complete; thesis drafted at `Context/opportunity-thesis.md` with Skill Ledger (held ✓ / developing ◌); scoring authority moves to the thesis. Remaining gap: credentials.*
