# MCP Registry – Canonical Server and Routing Table

The single source of truth for every MCP surface Alfred touches: what is registered, where, under which account, and which tools are permission-gated. Venture `Agents/integrations.md` files describe usage within their venture; this registry describes the wiring.

Last verified: 2026-08-11 (Domesday) – full live sweep of every reachable surface, one probe per server. Prior pass: 2026-08-08 (The Junction), the first against live health checks rather than config files alone.

**The verification standard changed this pass.** Previous passes confirmed that a server was registered. Registration is not connection: a server can be registered, start cleanly and fail every call, and three did. Worse, two entries in the Five Points venture registry claimed servers that had never existed at any scope. From this pass forward, a row claims "live" only on the strength of a call that returned, and it carries the date of that call.

---

## Project scope – committed `.mcp.json` at the repo root

The file is secret-free: each entry sources `.env` at launch and passes keys by reference. It is committed to git and restores with the repo. Eleven servers are currently registered.

| Server | Backing | Scope | Env keys consumed |
|---|---|---|---|
| `notion-fivepoints` | `@notionhq/notion-mcp-server` (npx) | Five Points Notion workspace | `NOTION_FIVEPOINTS_TOKEN` |
| `notion-personal` | `@notionhq/notion-mcp-server` (npx) | Personal Notion workspace – the working route since the OAuth enhanced connector died 12 July; also serves the Marty Gras standing exception. **First recorded in this registry 2026-08-11** – it was registered in `.mcp.json` but undocumented here | `NOTION_PERSONAL_TOKEN` |
| `supabase-fivepoints` | `@supabase/mcp-server-supabase` (npx) | Five Points Supabase | `SUPABASE_FIVEPOINTS_TOKEN` |
| `stripe-fivepoints` | `@stripe/mcp` (npx) | Five Points Stripe | `STRIPE_FIVEPOINTS_SECRET_KEY` |
| `pennyone` | local FastMCP, `Integrations/pennyone/` | Cross-venture syndication; pipeline key selects account | `ZERNIO_PERSONAL_API_KEY`, `ZERNIO_FIVEPOINTS_API_KEY` (+ future pipelines) |
| `strava` | local FastMCP, `Integrations/strava/` | Personal fitness | `STRAVA_CLIENT_ID`, `STRAVA_CLIENT_SECRET` (tokens at `~/.config/alfred/strava-tokens.json`) |
| `fullscript` | local FastMCP, `Integrations/fullscript-mcp/` | Personal wellness – intentionally resting, unauthenticated by design until supplement-protocol work resumes (operator ruling 2026-07-23) | `FULLSCRIPT_CLIENT_ID`, `FULLSCRIPT_CLIENT_SECRET`, `FULLSCRIPT_ENV`, `FULLSCRIPT_BASE_URL` |
| `elevenlabs` | `elevenlabs-mcp` (uvx, official) | Personal – voice production for the Marty Gras podcast lane. **Registered 2026-07-10; awaiting key** | `ELEVENLABS_API_KEY` (wrapper also sets non-secret `ELEVENLABS_MCP_BASE_PATH` to `.working/elevenlabs/`) |
| `calcom` | local FastMCP, `Integrations/calcom/` | Five Points booking layer (Cal.com API v2). **Registered 2026-07-10; the pipeline key is absent from `.env` as of 2026-07-23 – server registers but the Five Points pipeline has no working key** | `CALCOM_FIVEPOINTS_API_KEY` |
| `fivepoints-calendar` | local FastMCP, `Integrations/fivepoints-calendar/` | Five Points Workspace calendars, user-routed (Calendar API v3). **Registered 2026-07-10; awaiting shared key + Calendar delegation scope** | none – service-account file shared with fivepoints-mail; optional `FIVEPOINTS_CALENDAR_SERVICE_ACCOUNT` override |
| `apple-calendar` | local FastMCP (PyObjC/EventKit), `Integrations/apple-calendar/` | Personal – iCloud and every macOS-configured calendar | none – TCC authorization, no credentials |

### Live results, 2026-08-08

| Server | Call | Result |
|---|---|---|
| `notion-fivepoints` | `API-get-self` | **Live.** Workspace "Five Points Digital Studio", bot "Alfred Pennyworth", owner `systems@fivepoints.studio` |
| `stripe-fivepoints` | `get_stripe_account_info` | **Live.** `acct_1PfTxpDH3f10EsHc`, "Five Points Digital Studio" |
| `supabase-fivepoints` | `list_projects` | **Live.** Three projects – `fivepoints-site` healthy, `strong-tower-christian-ministry` and `Nomad Express` inactive |
| `pennyone` | `health_check` (all pipelines) | **Partly live.** `personal` ok with seven accounts; `five_points` ok with one (Instagram); `marty_gras`, `paradigm`, `lillie_and_lynette` all `no_key` |
| `calcom` | `health_check` | **Fails.** `Pipeline 'five_points' not provisioned. Set CALCOM_FIVEPOINTS_API_KEY` |
| `fivepoints-calendar` | `health_check` (martavious) | **Fails.** Service account key not found at the shared path |
| `elevenlabs` | – | **Halting.** Registered in `.mcp.json` but surfaces zero tools, consistent with the server exiting on the missing `ELEVENLABS_API_KEY` |
| `strava`, `fullscript`, `apple-calendar` | – | Registered and surfacing tools; not exercised this pass. Fullscript is intentionally resting per the 2026-07-23 ruling. |

### Live results, 2026-08-11 (Domesday)

| Server | Call | Result |
|---|---|---|
| `notion-personal` | `API-get-self` | **Live.** Workspace "Personal Notion", bot "Alfred Pennyworth" – overturns the estate-wide "personal Notion dark" claim, which was true only of the retired OAuth connector |
| `notion-fivepoints` | `API-get-self` | **Live.** Unchanged |
| `stripe-fivepoints` | `get_stripe_account_info` | **Live.** Unchanged |
| `supabase-fivepoints` | `list_projects` | **Live call; all three projects INACTIVE** including `fivepoints-site`, which was healthy 2026-08-08. Site-impact check pending |
| `pennyone` | `health_check` | Unchanged – `personal` ok/7, `five_points` ok/1, three pipelines `no_key` |
| `strava` | `strava_auth_status` | **Fails. 403 Forbidden** on the athlete endpoint despite a token file refreshed the same day – app credentials or scopes revoked |
| `calcom`, `fivepoints-calendar` | `health_check` | **Fail.** Identical errors to 2026-08-08 |
| `elevenlabs` | – | Still surfaces zero tools – key absent |
| `apple-calendar` | `authorization_status` | Call OK; **TCC `not_determined`, read and write both false** – macOS Calendar access has never been granted |
| `fivepoints-mail` (user scope) | `health_check` | **Dark.** `no_credentials` on all five mailboxes, unchanged |

Four of the eleven project-scope servers cannot complete a call – `calcom`, `fivepoints-calendar`, `elevenlabs` and `strava` – with `fivepoints-mail` dark at user scope beside them. The mail–calendar–booking trio is the Five Points communications layer, and two operator actions clear all three.

**`instantly` is absent.** The server previously registered here was torn down 2026-07-23 (The Lamplighter, registries lane): `Integrations/instantly/` (`README.md`, `requirements.txt`, `server.py`) was deleted from the working tree and the `instantly` block was removed from `.mcp.json`. Two operator actions remain outstanding and are not something this pass could execute: (1) delete `INSTANTLY_FIVEPOINTS_API_KEY` from `.env` by hand, and (2) cancel the Instantly account. See `secrets-inventory.md` and `accounts-inventory.md` for the tracking rows.

## User scope – `~/.claude.json` (recreated by hand on rebuild; never in git)

Confirmed against the live `mcpServers` block: three servers, unchanged since last verification.

| Server | Backing | Scope | Notes |
|---|---|---|---|
| `apple-mail` | `~/.local/bin/mcp-apple-mail` (patrickfreyer, via uv) | Personal iCloud mail | AppleScript bridge to Mail.app; sends gated. **2026-08-11:** `list_accounts` also returns an undocumented second account, "Studio Administration" – confirmation of what it is and why it sits in the personal Mail.app pending with the operator |
| `fivepoints-mail` | local FastMCP, `Integrations/fivepoints-mail/` | All five `@fivepoints.studio` inboxes | **Dark. `health_check` returns `no_credentials` on all five mailboxes, verified 2026-08-08.** The service-account JSON has never been dropped at `Integrations/fivepoints-mail/credentials/service-account.json`. Scaffolded April 2026; unauthenticated ever since. Sends gated when it works. |
| `discord-setup` | retired 2026-07-23 (operator ruling, The Lamplighter) – deregistered from user scope via `claude mcp remove`; bot token cleanup pending in accounts inventory | – | – |

Re-registration commands live in `genesis.md` Step 10.

## Claude Desktop connectors – claude.ai, browser-side, no disk presence

Not independently re-verified this pass (no filesystem or config surface to check against); carried forward from the last verification.

Re-verified 2026-08-08 against the session tool surface, which is the only observable evidence available for this class.

| Connector | Current internal ID prefix | Scope | Present 2026-08-08 |
|---|---|---|---|
| Notion (enhanced) | `mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__` | Personal Notion workspace | **ABSENT and superseded.** The personal workspace is served by the project-scoped `notion-personal` server, live-verified 2026-08-11. This connector stays retired; its dead allow-entries were removed from settings the same day. |
| Supabase | `mcp__fae54ad8-4f7a-4a10-b1d6-a95427baee20__` | Personal Supabase | Present |
| Vercel | `mcp__3cad28e2-8f9c-40ed-9a3a-04ac8503fc0e__` | Personal Vercel | Present. `list_teams` returns one team – `lavender-stingray`, "Headquarters". **This is the only Vercel surface in the estate; the Five Points team `studio-fivepoints` is unreachable.** |
| Google Drive | `mcp__34aed90a-ebfd-4a55-bda5-65132d78b122__` | Five Points Google Drive (read) – **label disputed** | Present. **Scope flag 2026-08-11:** sampled files belong to personal and family accounts, nothing from fivepoints.studio – either the label is wrong or the connector reaches wider than documented. Operator confirmation pending; the data-never-crosses rule is the stake |
| Google Calendar | `mcp__0bb634c3-a56c-44e9-8183-aa3c0016a566__` | Personal Gmail calendar | Present |
| Gmail | `mcp__3f878845-ed12-433d-947f-a8f854eaa8d7__` | Personal Gmail inbox, the life-admin buffer | Present |
| Uber Rides / Uber Eats | `mcp__12a30f57-…__` / `mcp__46049b74-…__` | Personal convenience connectors | Absent this session |

### Unregistered connectors found 2026-08-08

Present in the session tool surface, absent from every registry until this pass. Recorded so they are governed rather than merely available.

| Connector | Prefix | What it is | Disposition |
|---|---|---|---|
| Media generation | `mcp__02edb1a9-a1b7-4aa1-8d77-f34a218271b6__` | Image, video, audio, 3D and website generation, plus a TikTok publishing lane. Private workspace, free tier, **zero credits**, workspace not selected. | **Gated by operator ruling 2026-08-11.** `tiktok_publish`, `tiktok_connect` and `tiktok_prepare_publish` sit on the ask list beside the Pennyone gate; generation tools stay open. The install-specific ID caveat below applies – re-granting the connector mints a new prefix and the three ask entries must be updated to match. |
| Connector discovery | `mcp__mcp-registry__` | Searches the MCP connector registry and suggests connectors | Benign, read-only. Useful to the skill-scout lane. No gate needed. |
| Context7 | `mcp__plugin_context7_context7__` | Library and framework documentation lookup | Benign, read-only. Useful to any build lane. No gate needed. |
| PDF viewer | `mcp__pdf-viewer__` | Displays and interacts with local PDFs | Benign, local, read-only. No gate needed. |

The lesson generalises beyond these four: connectors accrete silently between passes. The registry cannot be a snapshot taken once a quarter and trusted in between.

**These IDs are install-specific.** Re-granting a connector mints a new ID; the ask-list entries in `~/.claude/settings.json` and the scheduled-task `allowed-tools` lines that reference these prefixes must be updated to match. This is a known rebuild step (genesis Step 11.3).

## Desktop built-ins (ship with the Claude app)

iMessage (`Read_and_Send_iMessages`), Apple Notes (`Read_and_Write_Apple_Notes`), computer use, preview (`Claude_Preview`), Chrome bridge (`Claude_in_Chrome`), scheduled tasks. No registration; they need macOS TCC permissions only.

**Scheduled tasks – live registry, verified 2026-07-23.** Four tasks are actually registered with the scheduler: `watchtower`, `oracle-platform`, `wealth-benchmark-refresh`, `contact-card-sync`. Five further SKILL.md directories survive on disk at `~/.claude/scheduled-tasks/` as deregistered recovery artefacts – `context-audit`, `media-scanner`, `pattern-memo`, `penny-one`, `sphere-review` – kept deliberately as blueprints per the 2026-08-11 Domesday ruling; `catalogue-likes` is gone with the Oracle rename. The `pattern-memo` agent definition itself is retired – the blueprint outlives the agent. A SKILL.md on disk is not proof of a live registration; cross-check with `mcp__scheduled-tasks__list_scheduled_tasks` (or the `Capability Matrix` automation's `--live-tasks` cross-check) before trusting the filesystem. Full rebuild sequence: `genesis.md` Step 14.

---

## The Notion routing rule – one workspace per sovereign venture

**Amended 2026-08-08 by operator ruling.** The rule previously described two paths, personal and Five Points, and had done since the second venture arrived. The portfolio has since grown to five active ventures plus one dormant, and three of them were sharing the personal workspace while a fourth sat inside the Five Points workspace. The rule now scales with the portfolio rather than lagging it.

**Every sovereign venture holds its own Notion workspace and its own integration token.** One standing exception: Marty Gras is the personal media identity and routes to the personal workspace permanently, by ruling rather than deferral. Sub-brands inherit the workspace of the parent venture – Paradigm Farms does not provision its own.

| Context | Target | Server | Status |
|---|---|---|---|
| Personal | Personal workspace | `notion-personal` (project scope) | **Live, verified 2026-08-11** |
| Five Points | Five Points workspace | `notion-fivepoints` | Live, verified 2026-08-11 |
| Marty Gras | Personal workspace, by standing exception | `notion-personal` | Live with the personal server |
| Paradigm | Paradigm workspace | `notion-paradigm` | Not provisioned |
| Lillie and Lynette | Lillie and Lynette workspace | `notion-lillieandlynette` | Not provisioned – **provision first, the only one with live revenue** |
| Atlas | Atlas workspace | `notion-atlas` | Not provisioned – state currently misfiled in the Five Points workspace and migrates out |
| Athena | Athena workspace | `notion-athena` | Held while dormant |

Standing rules that survive the amendment:

1. `mcp__notion__API-*`, `mcp__claude_ai_Notion__*` and `mcp__a42a278a…__*` are **legacy prefixes** from prior registrations. The last surviving allow-entries – seven `a42a278a` rows across both settings.local.json files and one `discord-setup` ask row – were removed 2026-08-11 (Domesday). Do not reintroduce.
2. **Data never crosses.** No venture page is written from another venture server. Personal pages are never written from a venture server and vice versa.
3. **Never substitute a reachable workspace for an unreachable one.** While a venture workspace is unprovisioned or dark, its state buffers to `.working/session-buffer/` under the buffer rule and syncs when the workspace exists. It does not get written somewhere convenient in the meantime – that is how Atlas ended up inside the Five Points workspace.

## Permission gates (the mechanical layer of Navigation Rule 3)

The ask list in `~/.claude/settings.json` gates every outward-facing tool:

| Class | Gated tools |
|---|---|
| Email sends | `fivepoints-mail` send_message and send_draft; `apple-mail` compose, reply, forward |
| Messages | iMessage send_imessage |
| Social publishing | `pennyone` publish; media-generation connector `tiktok_publish`, `tiktok_connect`, `tiktok_prepare_publish` (gated 2026-08-11) |
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

- **Two phantom servers corrected 2026-08-08 (The Junction).** The Five Points venture registry recorded `vercel-fivepoints` and `apify-fivepoints` as "Live – connected via `.mcp.json`". Neither existed at any scope and neither ever had. The consequence for Vercel is material: the only reachable Vercel MCP is the **personal** account, so every Five Points client deployment has run outside the wiring or through a personal-scoped connector. Apify is less severe – the capability is real over REST, only the MCP surface was fictional. Both rows now read NOT CONNECTED with the evidence attached. **This is the failure the verification standard at the head of this file exists to prevent: a registry that lies stops you looking.**
- **One Notion workspace per sovereign venture, ruled 2026-08-08 (The Junction).** Replaces the two-path personal/Five Points rule. Marty Gras is the single standing exception. Full table above. The project CLAUDE.md already carried the principle – "Venture A's Notion workspace is not Venture B's Notion workspace" – so this is execution catching up with doctrine rather than new policy.
- **Four venture integration registries created 2026-08-08 (The Junction).** Paradigm, Lillie and Lynette, Atlas and Athena had none; only Five Points and Marty Gras did. The root cause was the `New Venture/` template, which shipped the sentence "No `Agents/integrations.md` exists until configured" in three separate files instead of shipping a registry to fill in. Every venture copied from it inherited an absence. The template now ships a blank registry carrying a three-row provisioning checklist – Notion workspace, Pennyone pipeline, payment rail – and the three deferral sentences are gone.
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

*Last updated: 2026-08-11 – Domesday. Full live sweep: notion-personal documented for the first time and verified live, the broken count corrected to four project-scope servers plus dark mail, Strava's 403 recorded, the Drive connector scope disputed, the Studio Administration mailbox flagged, dead legacy permission entries removed, discord-setup directory deletion staged under the walked purge.*
