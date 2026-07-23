# Secrets Inventory – Key Names and Re-issue Procedures

**Purpose:** maps every credential the system consumes to where it lives and how to regenerate it after a credential loss, rotation event, or full restore. Values never appear in this file. Alfred is denied direct reads of `.env` by design, so this inventory is maintained by hand whenever `.env` changes.

**Rule:** if a variable appears in `.env` but is absent from this table, add it immediately. Drift here is a restore liability.

---

## Environment Variables in `.env` (repo root, gitignored)

| Variable | Consumed by | Re-issue procedure |
|---|---|---|
| `NOTION_FIVEPOINTS_TOKEN` | notion-fivepoints MCP | Notion Five Points workspace settings > Connections > internal integration; copy the integration secret; re-grant each database connection that the integration requires |
| `SUPABASE_FIVEPOINTS_TOKEN` | supabase-fivepoints MCP | Supabase dashboard (business account) > Account > Access tokens; create a new personal access token; revoke the old one |
| `STRIPE_FIVEPOINTS_SECRET_KEY` | stripe-fivepoints MCP | Stripe dashboard > Developers > API keys; prefer a restricted key scoped to required resources over the full secret key; revoke the old key after rotation |
| `ZERNIO_PERSONAL_API_KEY` | Pennyone personal pipeline | Zernio dashboard for the personal account; API keys or credentials section; generates per pipeline |
| `ZERNIO_FIVEPOINTS_API_KEY` | Pennyone Five Points pipeline | Zernio dashboard for the Five Points account; same flow as above |
| `ZERNIO_MARTYGRAS_API_KEY` | not needed -- operator ruling 2026-07-23: Marty Gras is the personal media identity and its content routes through the personal Zernio pipeline (`ZERNIO_PERSONAL_API_KEY`); no separate account is planned |
| `ZERNIO_PARADIGM_API_KEY` | Pennyone Paradigm pipeline (future) | Zernio dashboard for the Paradigm account when provisioned |
| `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Pennyone Lillie and Lynette pipeline (future) | Zernio dashboard for the L&L account when provisioned |
| `INSTANTLY_FIVEPOINTS_API_KEY` | nothing – Clay replaced Instantly as the outbound lead engine 2026-07-10; the `instantly` MCP server code (`Integrations/instantly/`) and its `.mcp.json` entry were torn down 2026-07-23 (The Lamplighter, registries lane) | **pending, operator action:** delete this line from `.env` by hand; the account itself also awaits cancellation – see `accounts-inventory.md` |
| `CALCOM_FIVEPOINTS_API_KEY` | calcom MCP, Five Points pipeline | **absent from `.env` as of 2026-07-23** – the server registers and starts but every call fails until this key is dropped in; Cal.com dashboard > Settings > Developer > API keys; scope to the `martavious-spicer` event-type owner used by the Five Points pipeline |
| `STRAVA_CLIENT_ID` | strava MCP bootstrap | strava.com/settings/api > My API Application; the Client ID is shown in plain text and does not rotate unless the app is deleted and recreated |
| `STRAVA_CLIENT_SECRET` | strava MCP bootstrap | same location as Client ID; reset via "Reset Secret" button; callback domain must remain localhost |
| `FULLSCRIPT_CLIENT_ID` | fullscript MCP | Fullscript practitioner portal > Developer settings > OAuth application; Client ID is static unless the app is deleted |
| `FULLSCRIPT_CLIENT_SECRET` | fullscript MCP | Same app; delete and recreate the app to rotate the secret; update `FULLSCRIPT_ENV` and `FULLSCRIPT_BASE_URL` to match the environment (sandbox vs. production) |
| `FULLSCRIPT_ENV` | fullscript MCP | Set to `production` for live use; `sandbox` for testing; determined by which Fullscript app is registered |
| `FULLSCRIPT_BASE_URL` | fullscript MCP | Fullscript API base URL for the environment; confirm in Fullscript developer documentation at time of re-issue |
| `APIFY_PERSONAL_TOKEN` | scraping – personal scope | Apify console (personal account) > Settings > Integrations > Personal API tokens |
| `APIFY_FIVEPOINTS_TOKEN` | scraping – Five Points scope | Apify console (Five Points account) > same path as above |
| `DISCORD_BOT_TOKEN` | discord-setup MCP | Discord developer portal > Applications > select the bot > Bot tab > Reset Token; update permissions and re-invite if the bot was removed during the reset |
| `ELEVENLABS_API_KEY` | elevenlabs MCP (`uvx elevenlabs-mcp`, project scope) | elevenlabs.io/app/settings/api-keys > create API key; add the line to `.env` by hand. **Pending 2026-07-10:** launch check confirms the variable is not yet present in `.env` – the server halts demanding it. While in the dashboard, confirm the account login email against `accounts-inventory.md` |
| `NOTION_PERSONAL_TOKEN` | notion-personal icon helper (`Integrations/notion-personal/upload_icon.py`) | Notion personal workspace settings > Connections > Develop or manage integrations > new internal integration with content read, update and insert capabilities; copy the secret; connect the integration to the Projects database. **Pending 2026-07-10:** variable not yet in `.env` – the helper halts demanding it |
| Perplexity API key | Perplexity integrations (if wired) | confirm against `.env` by hand; same caveat as above |

---

## Environment Variables in `Apps/nabu/.env.local` (Nabu's own repo, gitignored – separate from the repo-root `.env`)

**Catalogued here for the first time 2026-07-23 (The Lamplighter, registries lane) – to-be-provisioned/verified as part of any restore.** Nabu (`Apps/nabu`) is a standalone Next.js app, not an MCP server; nothing in this table registers with `.mcp.json` or `~/.claude.json`. It reads its own `.env.local`, templated by its own `.env.example` (which Alfred is equally denied from reading, by the same `.env*` deny pattern). It is driven interactively by its own dev server and headlessly by the `nabu-likes` scheduled task (`npm run watch-likes`). Names and purposes below are sourced from the app's own `README.md` and its source (`lib/ai/`, `lib/notion/`, `lib/youtube/`) – every variable is optional at the code level, but the rows marked required are load-bearing for the `nabu-likes` scheduled task specifically.

| Variable | Consumed by | Re-issue procedure |
|---|---|---|
| `ANTHROPIC_API_KEY` | Nabu's AI layer – didactic panel (abstract, key points, chapters) and the classification/sphere-assignment step of Save to Media; **required** for `nabu-likes` to file full entries | Anthropic console > API keys; Nabu manages its own key independently of the Claude Code session's credentials |
| `NABU_MODEL` | Which Claude model writes the panel | Config flag, not a secret; defaults to `claude-sonnet-4-5` if unset |
| `NABU_MAX_ITEMS` | Cap on videos pulled from a playlist or channel in the interactive UI | Config flag, not a secret; defaults to `25` |
| `NABU_WATCH_MAX_PER_RUN` | Cap on new likes filed per `nabu-likes` run | Config flag, not a secret; defaults to `10` |
| `NABU_NOTIFY_IMESSAGE` | Operator's iMessage handle for watcher per-item notices | Config value, not a secret; unset means the watcher stays silent on success |
| `NOTION_TOKEN` | Connects Save to Media; **required** for `nabu-likes` to file anything | Create an internal integration at notion.com/my-integrations; copy its token; add the integration to both the Media and Sphere Manager databases via each database's `•••` menu > Connections |
| `NOTION_MEDIA_DATA_SOURCE_ID` | Personal workspace Media database data-source id | Cross-check the "Notion database IDs" reference memory, or read it from the Notion API against the Media database |
| `NOTION_SPHERE_DATA_SOURCE_ID` | Personal workspace Sphere Manager data-source id, for auto-sphere assignment | Same path as above, against the Sphere Manager database |
| `YT_OAUTH_CLIENT_ID` | Liked-video watcher's Google OAuth client id | Google Cloud console > new project > enable YouTube Data API v3 > create an OAuth client of type Desktop app |
| `YT_OAUTH_CLIENT_SECRET` | Liked-video watcher's Google OAuth client secret | Same app as above; same console screen |
| `YT_OAUTH_REFRESH_TOKEN` | Liked-video watcher's long-lived Google auth | Run `npm run yt:auth` from `Apps/nabu` (wraps `scripts/authorize.mjs`), open the printed URL, grant read-only access, paste the printed refresh token into `.env.local` |
| `YT_TRANSCRIPT_IO_TOKEN` | Optional paid fallback transcript fetch via the youtube-transcript.io API, used only when the free InnerTube/`youtube-transcript-plus` paths fail | youtube-transcript.io account dashboard |

---

## File-based Credentials (outside git)

| Path | What it holds | Restore procedure |
|---|---|---|
| `Integrations/fivepoints-mail/credentials/*.json` | Google service-account key with domain-wide delegation (Gmail API, fivepoints.studio tenant) | GCP console > IAM & Admin > Service Accounts; download a new JSON key for the existing service account, or full recreate per the integration README: enable Gmail API, create service account, configure domain-wide delegation in Google Workspace admin at admin.google.com (required scopes documented in the README) |
| `~/.config/alfred/strava-tokens.json` | Strava OAuth access and refresh tokens | Re-run `Integrations/strava/bootstrap.py`; the script opens a browser authorisation flow against the strava.com OAuth endpoint and writes fresh tokens to this path on completion |
| `~/.claude.json` | User-scope MCP server registrations and Claude Code session state | Do not restore from backup; this file is recreated by running `claude mcp add` commands in the sequence documented in `genesis.md` Step 10; restoring a stale copy causes version and path mismatches |

---

## Escrow

All credential values and two-factor authentication recovery codes are stored in the operator's password manager.

Items that must be present and verified in the password manager before any restore drill proceeds:

- GitHub recovery codes for Massamartyv account
- GitHub recovery codes for studio-fivepoints account
- Apple ID recovery key
- Stripe restricted key and the full secret key (business account)
- All 2FA backup codes for accounts where 2FA is active

**The password manager must be reachable from a non-Mac device.** If it is not, that is a blocking gap to resolve before the next drill.

---

*Last updated: 2026-07-23 – The Lamplighter, registries lane: Instantly key marked pending removal (teardown 2026-07-23, decision 2026-07-10), Cal.com key added as absent, Nabu's own environment surface catalogued for the first time.*
