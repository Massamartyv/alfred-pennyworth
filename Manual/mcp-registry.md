# MCP Registry – Canonical Server and Routing Table

The single source of truth for every MCP surface Alfred touches: what is registered, where, under which account, and which tools are permission-gated. Venture `Agents/integrations.md` files describe usage within their venture; this registry describes the wiring.

Last verified: 2026-07-23 (The Lamplighter, registries lane) – cross-checked directly against the repo-root `.mcp.json` and the `mcpServers` block of `~/.claude.json` on disk.

---

## Project scope – committed `.mcp.json` at the repo root

The file is secret-free: each entry sources `.env` at launch and passes keys by reference. It is committed to git and restores with the repo. Ten servers are currently registered.

| Server | Backing | Scope | Env keys consumed |
|---|---|---|---|
| `notion-fivepoints` | `@notionhq/notion-mcp-server` (npx) | Five Points Notion workspace | `NOTION_FIVEPOINTS_TOKEN` |
| `supabase-fivepoints` | `@supabase/mcp-server-supabase` (npx) | Five Points Supabase | `SUPABASE_FIVEPOINTS_TOKEN` |
| `stripe-fivepoints` | `@stripe/mcp` (npx) | Five Points Stripe | `STRIPE_FIVEPOINTS_SECRET_KEY` |
| `pennyone` | local FastMCP, `Integrations/pennyone/` | Cross-venture syndication; pipeline key selects account | `ZERNIO_PERSONAL_API_KEY`, `ZERNIO_FIVEPOINTS_API_KEY` (+ future pipelines) |
| `strava` | local FastMCP, `Integrations/strava/` | Personal fitness | `STRAVA_CLIENT_ID`, `STRAVA_CLIENT_SECRET` (tokens at `~/.config/alfred/strava-tokens.json`) |
| `fullscript` | local FastMCP, `Integrations/fullscript-mcp/` | Personal wellness -- intentionally resting, unauthenticated by design until supplement-protocol work resumes (operator ruling 2026-07-23) | `FULLSCRIPT_CLIENT_ID`, `FULLSCRIPT_CLIENT_SECRET`, `FULLSCRIPT_ENV`, `FULLSCRIPT_BASE_URL` |
| `elevenlabs` | `elevenlabs-mcp` (uvx, official) | Personal – voice production for the Marty Gras podcast lane. **Registered 2026-07-10; awaiting key** | `ELEVENLABS_API_KEY` (wrapper also sets non-secret `ELEVENLABS_MCP_BASE_PATH` to `.working/elevenlabs/`) |
| `calcom` | local FastMCP, `Integrations/calcom/` | Five Points booking layer (Cal.com API v2). **Registered 2026-07-10; the pipeline key is absent from `.env` as of 2026-07-23 – server registers but the Five Points pipeline has no working key** | `CALCOM_FIVEPOINTS_API_KEY` |
| `fivepoints-calendar` | local FastMCP, `Integrations/fivepoints-calendar/` | Five Points Workspace calendars, user-routed (Calendar API v3). **Registered 2026-07-10; awaiting shared key + Calendar delegation scope** | none – service-account file shared with fivepoints-mail; optional `FIVEPOINTS_CALENDAR_SERVICE_ACCOUNT` override |
| `apple-calendar` | local FastMCP (PyObjC/EventKit), `Integrations/apple-calendar/` | Personal – iCloud and every macOS-configured calendar | none – TCC authorization, no credentials |

**`instantly` is absent.** The server previously registered here was torn down 2026-07-23 (The Lamplighter, registries lane): `Integrations/instantly/` (`README.md`, `requirements.txt`, `server.py`) was deleted from the working tree and the `instantly` block was removed from `.mcp.json`. Two operator actions remain outstanding and are not something this pass could execute: (1) delete `INSTANTLY_FIVEPOINTS_API_KEY` from `.env` by hand, and (2) cancel the Instantly account. See `secrets-inventory.md` and `accounts-inventory.md` for the tracking rows.

## User scope – `~/.claude.json` (recreated by hand on rebuild; never in git)

Confirmed against the live `mcpServers` block: three servers, unchanged since last verification.

| Server | Backing | Scope | Notes |
|---|---|---|---|
| `apple-mail` | `~/.local/bin/mcp-apple-mail` (patrickfreyer, via uv) | Personal iCloud mail | AppleScript bridge to Mail.app; sends gated |
| `fivepoints-mail` | local FastMCP, `Integrations/fivepoints-mail/` | All five `@fivepoints.studio` inboxes | Service account + domain-wide delegation; explicit `mailbox` parameter on every call; sends gated |
| `discord-setup` | retired 2026-07-23 (operator ruling, The Lamplighter) -- deregistered from user scope via `claude mcp remove`; bot token cleanup pending in accounts inventory | -- | -- |

Re-registration commands live in `genesis.md` Step 10.

## Claude Desktop connectors – claude.ai, browser-side, no disk presence

Not independently re-verified this pass (no filesystem or config surface to check against); carried forward from the last verification.

| Connector | Current internal ID prefix | Scope |
|---|---|---|
| Notion (enhanced) | `mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__` | Personal Notion workspace |
| Supabase | `mcp__fae54ad8-4f7a-4a10-b1d6-a95427baee20__` | Personal Supabase |
| Vercel | `mcp__3cad28e2-8f9c-40ed-9a3a-04ac8503fc0e__` | Personal Vercel |
| Google Drive | `mcp__34aed90a-ebfd-4a55-bda5-65132d78b122__` | Five Points Google Drive (read) |
| Google Calendar | `mcp__0bb634c3-a56c-44e9-8183-aa3c0016a566__` | Personal Gmail calendar |
| Gmail | `mcp__3f878845-ed12-433d-947f-a8f854eaa8d7__` | Personal Gmail inbox, the life-admin buffer |
| Uber Rides / Uber Eats | `mcp__12a30f57-a85a-4692-88a2-9e053702ed91__` / `mcp__46049b74-3f61-41c5-8e30-efeb73fc2266__` | Personal convenience connectors |

**These IDs are install-specific.** Re-granting a connector mints a new ID; the ask-list entries in `~/.claude/settings.json` and the scheduled-task `allowed-tools` lines that reference these prefixes must be updated to match. This is a known rebuild step (genesis Step 11.3).

## Desktop built-ins (ship with the Claude app)

iMessage (`Read_and_Send_iMessages`), Apple Notes (`Read_and_Write_Apple_Notes`), computer use, preview (`Claude_Preview`), Chrome bridge (`Claude_in_Chrome`), scheduled tasks. No registration; they need macOS TCC permissions only.

**Scheduled tasks – live registry, verified 2026-07-23.** Four tasks are actually registered with the scheduler: `watchtower`, `oracle-platform`, `wealth-benchmark-refresh`, `contact-card-sync`. Six further SKILL.md directories survive on disk at `~/.claude/scheduled-tasks/` as deregistered recovery artefacts – `catalogue-likes` (superseded by the `oracle-platform` rename), `context-audit`, `media-scanner`, `pattern-memo`, `penny-one`, `sphere-review` – per the exception list in `Agents/heartbeat.md`'s Scheduler audit row. A SKILL.md on disk is not proof of a live registration; cross-check with `mcp__scheduled-tasks__list_scheduled_tasks` (or the `Capability Matrix` automation's `--live-tasks` cross-check) before trusting the filesystem. Full rebuild sequence: `genesis.md` Step 14.

---

## The Notion routing rule (four paths, one rule)

1. **Personal context** → the enhanced Notion connector (`mcp__a42a278a…` prefix). Sphere Manager, Tasks, Fitness Journal, Reflections, all personal databases.
2. **Five Points context** → `notion-fivepoints` server. CRM, client workspaces, venture operations.
3. `mcp__notion__API-*` and `mcp__claude_ai_Notion__*` are **legacy prefixes** from prior registrations. Stale allow-entries referencing them survive in `settings.local.json`; they match nothing and are harmless. Do not reintroduce.
4. Data never crosses: personal pages are never written from the Five Points server and vice versa.

## Permission gates (the mechanical layer of Navigation Rule 3)

The ask list in `~/.claude/settings.json` gates every outward-facing tool:

| Class | Gated tools |
|---|---|
| Email sends | `fivepoints-mail` send_message and send_draft; `apple-mail` compose, reply, forward |
| Messages | iMessage send_imessage |
| Social publishing | `pennyone` publish |
| Financial writes | `stripe-fivepoints` stripe_api_write, create_refund |
| Data and deploy | Supabase apply_migration, execute_sql, deploy_edge_function, create_project, pause_project, delete_branch, reset_branch (both Supabase servers); Vercel deploy_to_vercel |
| Bookings | `calcom` create_booking, reschedule_booking, cancel_booking |
| Calendar writes | `fivepoints-calendar` create_event, update_event, delete_event; `apple-calendar` create_event, update_event, delete_event |
| Community infrastructure | the whole `discord-setup` server |
| Git | `git push` |

Scheduled (headless) agents cannot answer an ask: each scheduled task carries an `allowed-tools` allowlist instead, granting at most one outward tool – iMessage delivery to the operator – and nothing else. See `~/.claude/scheduled-tasks/*/SKILL.md`.

**The former "Outbound campaigns" row (`instantly` reply_to_email, add_leads_bulk, pause_campaign) is retired along with the server.** No replacement gate exists yet for Clay – it has no MCP surface as of this pass and is dashboard-managed only (monitor but do not act without instruction, per the global CLAUDE.md ecosystem entry).

## Intentional denies (do not re-flag in audits)

- `Skill(anthropic-skills:michelin-chef)` and `Skill(anthropic-skills:frontend-design)` – plugin duplicates of locally maintained skills; the local versions win.
- `Read(./.env*)`, `Read(./.envrc)` – Alfred never reads the secrets file, including key names, in this project or in any nested app directory (confirmed 2026-07-23: the deny also catches `Apps/oracle/.env.example`, a values-free template). The secrets inventory is maintained by hand.
- Blanket `python3 -c`, `pip3 install` and bare `osascript` approvals were removed 2026-06-11; script execution approvals are scoped to `Automations/` and `Integrations/` paths.

## Decisions of record

- **Instantly server torn down 2026-07-23 (The Lamplighter, registries lane).** `Integrations/instantly/` deleted from the working tree; `.mcp.json` no longer registers it. This completes the code-level half of the 2026-07-10 Clay-replaces-Instantly decision below. Remaining: remove `INSTANTLY_FIVEPOINTS_API_KEY` from `.env`, cancel the Instantly account.
- **Calendar lane built 2026-07-10.** Two servers registered at project scope: `fivepoints-calendar` (Calendar API v3, service-account impersonation shared with fivepoints-mail, user-routed with no implicit default) and `apple-calendar` (EventKit via PyObjC – chosen over an AppleScript bridge for speed, structured CRUD and no app dependency). Found in passing: the fivepoints-mail service-account key was never dropped, so the mail server has been unauthenticated since April – one key drop now lights both Google servers.
- **calcom MCP scaffolded and registered 2026-07-10.** Booking layer for the agent-first scheduling lane (Cal.com API v2, 10 tools, writes gated on the ask list). Offline smoke test passing; the pipeline key was still absent from `.env` as of 2026-07-23.
- **ElevenLabs restored to the wiring 2026-07-10.** Broken since April 2026 – the connection predated the secret-free architecture and was never migrated; no server existed at any scope. Official `elevenlabs-mcp` registered at project scope in `.mcp.json`; launch verified end to end, with the server halting on a missing `ELEVENLABS_API_KEY`. Operator step staged to mint a key at elevenlabs.io/app/settings/api-keys and add the line to `.env` by hand; the server connects automatically at the next session after that.
- **Instantly deprecated 2026-07-10.** Clay owns the Five Points outbound lane (enrichment, sequencing, sending; no MCP yet). Decision made this date; the server unregistration and account cancellation followed on 2026-07-23 above.
- **Desktop connector registry trued up 2026-07-10.** Google Calendar, Gmail and Uber connectors added; both Google connectors serve the personal Gmail account.
- **fullscript-mcp registered at project scope, 2026-06-11.** Personal wellness tooling; built April 2026, credentials rotated 2026-04-22, previously unregistered by oversight.
- **Buffer deprecated ecosystem-wide April 2026**; Pennyone is the syndication layer. Account confirmed cancelled by the operator 2026-07-23.
- **Stripe is venture-scoped only** – no personal Stripe exists.
- **Oracle (`Apps/oracle`) has no MCP surface.** It is driven headlessly by the `oracle-platform` scheduled task (`npm run watch-likes`) and interactively by its own Next.js dev server; nothing in `.mcp.json` or `~/.claude.json` references it. Its environment surface lives in its own `.env.local`, catalogued for the first time in `secrets-inventory.md` this pass.

---

*Last updated: 2026-07-23.*
