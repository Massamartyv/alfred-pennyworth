# MCP Registry – Canonical Server and Routing Table

The single source of truth for every MCP surface Alfred touches: what is registered, where, under which account, and which tools are permission-gated. Venture `Agents/integrations.md` files describe usage within their venture; this registry describes the wiring.

Last verified: 2026-06-11.

---

## Project scope – committed `.mcp.json` at the repo root

The file is secret-free: each entry sources `.env` at launch and passes keys by reference. It is committed to git and restores with the repo.

| Server | Backing | Scope | Env keys consumed |
|---|---|---|---|
| `notion-fivepoints` | `@notionhq/notion-mcp-server` (npx) | Five Points Notion workspace | `NOTION_FIVEPOINTS_TOKEN` |
| `supabase-fivepoints` | `@supabase/mcp-server-supabase` (npx) | Five Points Supabase | `SUPABASE_FIVEPOINTS_TOKEN` |
| `stripe-fivepoints` | `@stripe/mcp` (npx) | Five Points Stripe | `STRIPE_FIVEPOINTS_SECRET_KEY` |
| `pennyone` | local FastMCP, `Integrations/pennyone/` | Cross-venture syndication; pipeline key selects account | `ZERNIO_PERSONAL_API_KEY`, `ZERNIO_FIVEPOINTS_API_KEY` (+ future pipelines) |
| `instantly` | local FastMCP, `Integrations/instantly/` | Five Points outbound leads | `INSTANTLY_FIVEPOINTS_API_KEY` |
| `strava` | local FastMCP, `Integrations/strava/` | Personal fitness | `STRAVA_CLIENT_ID`, `STRAVA_CLIENT_SECRET` (tokens at `~/.config/alfred/strava-tokens.json`) |
| `fullscript` | local FastMCP, `Integrations/fullscript-mcp/` | Personal wellness | `FULLSCRIPT_CLIENT_ID`, `FULLSCRIPT_CLIENT_SECRET`, `FULLSCRIPT_ENV`, `FULLSCRIPT_BASE_URL` |

## User scope – `~/.claude.json` (recreated by hand on rebuild; never in git)

| Server | Backing | Scope | Notes |
|---|---|---|---|
| `apple-mail` | `~/.local/bin/mcp-apple-mail` (patrickfreyer, via uv) | Personal iCloud mail | AppleScript bridge to Mail.app; sends gated |
| `fivepoints-mail` | local FastMCP, `Integrations/fivepoints-mail/` | All five `@fivepoints.studio` inboxes | Service account + domain-wide delegation; explicit `mailbox` parameter on every call; sends gated |
| `discord-setup` | `Integrations/discord-setup-mcp/run.sh` (own repo) | Server setup tooling | Whole server on the ask list |

Re-registration commands live in `genesis.md` Step 10.

## Claude Desktop connectors – claude.ai, browser-side, no disk presence

| Connector | Current internal ID prefix | Scope |
|---|---|---|
| Notion (enhanced) | `mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__` | Personal Notion workspace |
| Supabase | `mcp__fae54ad8-4f7a-4a10-b1d6-a95427baee20__` | Personal Supabase |
| Vercel | `mcp__3cad28e2-8f9c-40ed-9a3a-04ac8503fc0e__` | Personal Vercel |
| Google Drive | `mcp__34aed90a-ebfd-4a55-bda5-65132d78b122__` | Five Points Google Drive (read) |

**These IDs are install-specific.** Re-granting a connector mints a new ID; the ask-list entries in `~/.claude/settings.json` and the scheduled-task `allowed-tools` lines that reference these prefixes must be updated to match. This is a known rebuild step (genesis Step 11.3).

## Desktop built-ins (ship with the Claude app)

iMessage (`Read_and_Send_iMessages`), Apple Notes (`Read_and_Write_Apple_Notes`), computer use, preview (`Claude_Preview`), Chrome bridge (`Claude_in_Chrome`), scheduled tasks. No registration; they need macOS TCC permissions only.

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
| Outbound campaigns | `instantly` reply_to_email, add_leads_bulk, pause_campaign |
| Community infrastructure | the whole `discord-setup` server |
| Git | `git push` |

Scheduled (headless) agents cannot answer an ask: each scheduled task carries an `allowed-tools` allowlist instead, granting at most one outward tool – iMessage delivery to the operator – and nothing else. See `~/.claude/scheduled-tasks/*/SKILL.md`.

## Intentional denies (do not re-flag in audits)

- `Skill(anthropic-skills:michelin-chef)` and `Skill(anthropic-skills:frontend-design)` – plugin duplicates of locally maintained skills; the local versions win.
- `Read(./.env*)`, `Read(./.envrc)` – Alfred never reads the secrets file, including key names. The secrets inventory is maintained by hand.
- Blanket `python3 -c`, `pip3 install` and bare `osascript` approvals were removed 2026-06-11; script execution approvals are scoped to `Automations/` and `Integrations/` paths.

## Decisions of record

- **fullscript-mcp registered at project scope, 2026-06-11.** Personal wellness tooling; built April 2026, credentials rotated 2026-04-22, previously unregistered by oversight.
- **Buffer deprecated ecosystem-wide April 2026**; Pennyone is the syndication layer.
- **Stripe is venture-scoped only** – no personal Stripe exists.
