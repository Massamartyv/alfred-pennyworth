---
file_type: build_brief
department: Growth
venture: Five Points Digital Studio
status: ready-for-build
owner: Claude Code
last_updated: 2026-07-07
---

# Build Brief — Five Points Sales Pipeline on Notion

Instructions for Claude Code. Mission: promote the Prospect Pipeline from a self-contained Cowork artifact into a full sales pipeline system whose **database of record is the Five Points Notion workspace**, mirroring the Supabase pattern — Notion stores, everything else reads and writes through it.

## Context — read first

1. `Growth/Prospecting/lookalike-engine.md` — the outreach engine, two-stage funnel (Connect → Convert), run log through Pulse 6.
2. `Growth/Prospecting/outreach-log.md` — touch-1 sends (70 on 2026-06-30) and Stage-A connection requests (19 on 2026-07-01).
3. `Agents/integrations.md` (this venture) — the `notion-fivepoints` MCP server, `NOTION_FIVEPOINTS_TOKEN` in `.env`. **All writes go to this workspace, never the personal one.** Data never crosses the boundary.
4. The current Cowork artifact at `~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html` — the canonical current state. It contains three machine-readable regions:
   - `const SEED = [...]` — 100 prospect records (id, names, company, position, city, segment, offer, linkedin, touch1, warmth, relationshipContext)
   - `PULSE-SYNC-START … END` — versioned outreach ground truth (stages, dates, appointment-ready flags, notes; `SENT_JUN30` array of the 70 contacted)
   - `CONNECT-START … END` — 20 Stage-A connection-request rows with statuses

## Architecture

```
Notion (Five Points workspace)        ← system of record
  └── Contacts DB (single database)
        Type: Connection Request → Prospect → Client
              (acceptance graduates a request into a prospect)
Sync layer (repo scripts, notion-fivepoints MCP or Notion SDK)
  ├── seed script      — one-time import from artifact SEED/PULSE/CONNECT
  ├── pulse writer     — daily pulse writes replies/stages/accepts to Notion
  └── artifact export  — regenerates the Cowork artifact FROM Notion
Dashboard(s)
  ├── Cowork artifact  — interim daily surface (already live)
  └── Apps/pipeline    — future venture app if/when a richer dashboard is wanted
```

## Contacts DB — schema (one database, Type + Stage)

| Property | Type | Notes |
|---|---|---|
| Name | Title | Full name |
| Type | Select | `Connection Request`, `Prospect`, `Client`, `Held`, `Closed` |
| Stage | Status | `Not contacted`, `Touch 1 sent`, `Replied`, `In conversation`, `Qualified`, `Proposal`, `Won`, `Lost`, `Nurture` |
| Appt Ready | Checkbox | The priority flag — appointment → lead → Marty closes |
| Warmth | Select | `Cold`, `Warm`, `Close` — sync only ever raises it |
| Segment | Select | From artifact segments + `Dental — aesthetics` |
| Company / Position / City | Text | From SEED / connect queue |
| Best-Fit Offer | Select | From SEED `offer` |
| LinkedIn | URL | Search-style URLs acceptable; upgrade to profile URLs opportunistically |
| Touch 1 / Touch 2 / Touch 3 | Text | Openers and follow-ups |
| Relationship Context | Text | How Marty knows them |
| Last Contacted / Next Action Date / Request Sent | Date | |
| Next Action / Notes | Text | Pulse intel appends to Notes, tagged `[Pulse N · date]` |
| Owner | Select | Default `Marty` |
| Source | Select | `Network 100`, `Stage A — dental`, `Lookalike batch`, `Inbound` |
| External ID | Text | **Stable sync key** — the artifact `id` slug. All upserts match on this, never on Name. Idempotency is non-negotiable. |

## Missions (each ≤ one pomodoro; sequence strictly)

1. **Scaffold.** Create `Growth/Prospecting/pipeline-sync/` in the venture folder: `README.md`, `schema.json` (the table above as code), `.env` reference (`NOTION_FIVEPOINTS_TOKEN` — never hardcode).
2. **Create the database.** In the Five Points workspace, page `CRM` → Contacts database per schema. Record database + data-source IDs in `schema.json`.
3. **Extractor.** Script that parses the artifact HTML and emits `contacts.json`: 100 SEED prospects (Type per state: contacted → `Prospect`; Taruna/Elizma/Megan → `Held`), PULSE overlays applied (stage, dates, apptReady, notes), 20 CONNECT rows (Type `Connection Request`, Stage `Not contacted`, Request Sent 2026-07-01).
4. **Seed.** Upsert `contacts.json` into Notion keyed on External ID. Run twice; second run must be a no-op (prove idempotency).
5. **Pulse writer.** Function the daily pulse calls: given reply/accept/send events, upsert Notion. Acceptance flips Type `Connection Request` → `Prospect` — the graduation. New sends append Stage/date.
6. **Artifact regenerator.** Script that queries Notion and re-emits the artifact regions (SEED, PULSE, CONNECT) so the Cowork dashboard mirrors Notion, not the other way round. Notion wins conflicts; localStorage becomes scratch only.
7. **Rewire the scheduled task.** Update `five-points-lookalike-pulse` step 5: write to Notion first (missions 5), regenerate + ship the artifact second (mission 6).
8. **Reviewer pass.** Behavioural: open the Notion DB, verify counts (100 + 20), spot-check Shar Caesar Douglas (Appt Ready ✓, Stage Replied), Beatrice Sibblies (Warm), Soroush Liaghat (Needs-fix note). Scrutiny: schema matches this brief exactly.

## Red lines

- Nothing sends on LinkedIn without Marty's explicit greenlight — this system stores and surfaces; it does not message.
- Five Points data only in the Five Points workspace. The personal Contacts CRM (family/relationships) is untouchable.
- Upserts by External ID only. No duplicate people, ever.
- The Cowork artifact keeps working throughout — no dark window on the daily pulse surface.

## Later (out of scope now)

- Cowork connector to the Five Points Notion workspace, so the artifact reads Notion live via `callMcpTool` instead of regeneration.
- `Apps/pipeline` venture app (Next.js on `vercel-fivepoints`) if the dashboard outgrows the artifact.
- Deals database split once proposals start flowing; Clients relate to `Operations/Clientele`.
