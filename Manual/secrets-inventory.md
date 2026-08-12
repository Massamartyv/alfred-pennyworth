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
| `ZERNIO_MARTYGRAS_API_KEY` | retired – the `marty_gras` pipeline was removed from the Pennyone router 2026-08-11 by operator ruling, executing the 2026-07-23 decision; Marty Gras publishes through `ZERNIO_PERSONAL_API_KEY`. No key will exist. Delete any resident line from `.env` during the escrow pass | n/a – retired |
| `ZERNIO_PARADIGM_API_KEY` | Pennyone Paradigm pipeline – pipeline registered in code, `no_key` verified 2026-08-08 | Zernio dashboard for the Paradigm account when provisioned |
| `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Pennyone Lillie and Lynette pipeline – pipeline registered in code, `no_key` verified 2026-08-08 | Zernio dashboard for the L&L account when provisioned |
| `INSTANTLY_FIVEPOINTS_API_KEY` | nothing – Clay replaced Instantly as the outbound lead engine 2026-07-10; the `instantly` MCP server code (`Integrations/instantly/`) and its `.mcp.json` entry were torn down 2026-07-23 (The Lamplighter, registries lane) | **pending, operator action:** delete this line from `.env` by hand; the account itself also awaits cancellation – see `accounts-inventory.md` |
| `CALCOM_FIVEPOINTS_API_KEY` | calcom MCP, Five Points pipeline | **absent from `.env` as of 2026-07-23** – the server registers and starts but every call fails until this key is dropped in; Cal.com dashboard > Settings > Developer > API keys; scope to the `martavious-spicer` event-type owner used by the Five Points pipeline |
| `STRAVA_CLIENT_ID` | strava MCP bootstrap | strava.com/settings/api > My API Application; the Client ID is shown in plain text and does not rotate unless the app is deleted and recreated |
| `STRAVA_CLIENT_SECRET` | strava MCP bootstrap | same location as Client ID; reset via "Reset Secret" button; callback domain must remain localhost |
| `FULLSCRIPT_CLIENT_ID` | fullscript MCP | Fullscript practitioner portal > Developer settings > OAuth application; Client ID is static unless the app is deleted |
| `FULLSCRIPT_CLIENT_SECRET` | fullscript MCP | Same app; delete and recreate the app to rotate the secret; update `FULLSCRIPT_ENV` and `FULLSCRIPT_BASE_URL` to match the environment (sandbox vs. production) |
| `FULLSCRIPT_ENV` | fullscript MCP | Set to `production` for live use; `sandbox` for testing; determined by which Fullscript app is registered |
| `FULLSCRIPT_BASE_URL` | fullscript MCP | Fullscript API base URL for the environment; confirm in Fullscript developer documentation at time of re-issue |
| `APIFY_PERSONAL_TOKEN` | scraping – personal scope | Apify console (personal account) > Settings > Integrations > Personal API tokens |
| `DISCORD_BOT_TOKEN` | discord-setup MCP | Discord developer portal > Applications > select the bot > Bot tab > Reset Token; update permissions and re-invite if the bot was removed during the reset |
| `ELEVENLABS_API_KEY` | elevenlabs MCP (`uvx elevenlabs-mcp`, project scope) | elevenlabs.io/app/settings/api-keys > create API key; add the line to `.env` by hand. **Pending 2026-07-10:** launch check confirms the variable is not yet present in `.env` – the server halts demanding it. While in the dashboard, confirm the account login email against `accounts-inventory.md` |
| `NOTION_PERSONAL_TOKEN` | **the `notion-personal` MCP server** – the working route to the entire personal workspace, live-verified 2026-08-11 – plus the icon helper (`Integrations/notion-personal/upload_icon.py`) | Notion personal workspace settings > Connections > Develop or manage integrations > internal integration with read, update and insert capabilities; copy the secret; grant the integration to each database it serves. **Provisioned and live as of 2026-08-11** – the 2026-07-10 pending note is resolved |
| Perplexity API key | Perplexity integrations (if wired) | confirm against `.env` by hand; same caveat as above |
| `VERCEL_FIVEPOINTS_TOKEN` | **nothing.** No `vercel-fivepoints` server exists at any scope – the venture registry claimed one for an extended period and the claim was false (corrected 2026-08-08, The Junction). Presence of this line in `.env` is unconfirmed. | Vercel dashboard for the `studio-fivepoints` team, login `systems-9970` > Account Settings > Tokens. Needed when the server is actually built. |
| `APIFY_FIVEPOINTS_TOKEN` | Apify Five Points scope over the **REST API**, not MCP. No `apify-fivepoints` server exists; the venture registry claimed one and the claim was false (corrected 2026-08-08). The scraping capability is real, the MCP surface never was. | Apify console (Five Points account) > Settings > Integrations > Personal API tokens |

---

## Venture Provisioning Variables – ruled 2026-08-08, not yet minted

The 2026-08-08 one-workspace-per-venture ruling requires a Notion token per sovereign venture. None of the below exists yet. Listed here at the moment of the ruling rather than at the moment of minting, so that the inventory reflects the target state and the gap between target and actual stays visible.

| Variable | Consumed by | Re-issue procedure | Priority |
|---|---|---|---|
| `NOTION_LILLIEANDLYNETTE_TOKEN` | `notion-lillieandlynette` MCP (to be registered) | Create the Lillie and Lynette Notion workspace; Settings > Connections > new internal integration; grant it to each database | **First.** The only unprovisioned venture with live revenue. |
| `STRIPE_LILLIEANDLYNETTE_SECRET_KEY` | `stripe-lillieandlynette` MCP (to be registered) | Create the Lillie and Lynette Stripe account; Developers > API keys; prefer a restricted key | **First.** Stewardship is taking money with no rail. |
| `NOTION_PARADIGM_TOKEN` | `notion-paradigm` MCP (to be registered) | As above, against the Paradigm workspace | Second |
| `STRIPE_PARADIGM_SECRET_KEY` | `stripe-paradigm` MCP (to be registered) | As above, against a Paradigm Stripe account | On first product run |
| `ANTHROPIC_PARADIGM_API_KEY` | Paradigm Farms AI layer | Anthropic console > API keys. The app manages its own key independently of the Claude Code session, on the Oracle precedent. | With the Farms build |
| `NOTION_ATLAS_TOKEN` | `notion-atlas` MCP (to be registered) | As above, against the Atlas workspace. Migrate the Arlando Parker Jr. pilot records out of the Five Points workspace on provisioning. | Third |
| `ANTHROPIC_ATLAS_API_KEY` | Atlas clinical documentation layer | Anthropic console. **A Business Associate Agreement must be executed before any real patient encounter reaches this key.** | Gated on the BAA |
| `NOTION_ATHENA_TOKEN` | `notion-athena` MCP (to be registered) | As above | Held while dormant |

Marty Gras takes no venture token – it routes to the personal workspace by standing exception.

---

## Environment Variables in `Apps/oracle/.env.local` (Oracle's own repo, gitignored – separate from the repo-root `.env`)

**Catalogued here for the first time 2026-07-23 (The Lamplighter, registries lane) – to-be-provisioned/verified as part of any restore.** Oracle (`Apps/oracle`) is a standalone Next.js app, not an MCP server; nothing in this table registers with `.mcp.json` or `~/.claude.json`. It reads its own `.env.local`, templated by its own `.env.example` (which Alfred is equally denied from reading, by the same `.env*` deny pattern). It is driven interactively by its own dev server and headlessly by the `oracle-platform` scheduled task (`npm run watch-likes`). Names and purposes below are sourced from the app's own `README.md` and its source (`lib/ai/`, `lib/notion/`, `lib/youtube/`) – every variable is optional at the code level, but the rows marked required are load-bearing for the `oracle-platform` scheduled task specifically.

| Variable | Consumed by | Re-issue procedure |
|---|---|---|
| `ANTHROPIC_API_KEY` | Oracle's AI layer – didactic panel (abstract, key points, chapters) and the classification/sphere-assignment step of Save to Media; **required** for `oracle-platform` to file full entries | Anthropic console > API keys; Oracle manages its own key independently of the Claude Code session's credentials |
| `ORACLE_MODEL` | Which Claude model writes the panel | Config flag, not a secret; defaults to `claude-sonnet-4-5` if unset |
| `ORACLE_MAX_ITEMS` | Cap on videos pulled from a playlist or channel in the interactive UI | Config flag, not a secret; defaults to `25` |
| `ORACLE_WATCH_MAX_PER_RUN` | Cap on new likes filed per `oracle-platform` run | Config flag, not a secret; defaults to `10` |
| `ORACLE_NOTIFY_IMESSAGE` | Operator's iMessage handle for watcher per-item notices | Config value, not a secret; unset means the watcher stays silent on success |
| `NOTION_TOKEN` | Connects Save to Media; **required** for `oracle-platform` to file anything | Create an internal integration at notion.com/my-integrations; copy its token; add the integration to both the Media and Sphere Manager databases via each database's `•••` menu > Connections |
| `NOTION_MEDIA_DATA_SOURCE_ID` | Personal workspace Media database data-source id | Cross-check the "Notion database IDs" reference memory, or read it from the Notion API against the Media database |
| `NOTION_SPHERE_DATA_SOURCE_ID` | Personal workspace Sphere Manager data-source id, for auto-sphere assignment | Same path as above, against the Sphere Manager database |
| `YT_OAUTH_CLIENT_ID` | Liked-video watcher's Google OAuth client id | Google Cloud console > new project > enable YouTube Data API v3 > create an OAuth client of type Desktop app |
| `YT_OAUTH_CLIENT_SECRET` | Liked-video watcher's Google OAuth client secret | Same app as above; same console screen |
| `YT_OAUTH_REFRESH_TOKEN` | Liked-video watcher's long-lived Google auth | Run `npm run yt:auth` from `Apps/oracle` (wraps `scripts/authorize.mjs`), open the printed URL, grant read-only access, paste the printed refresh token into `.env.local` |
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

*Last updated: 2026-08-11 – Domesday: NOTION_PERSONAL_TOKEN row corrected to name its true consumer, the notion-personal server, and marked live; the duplicate APIFY_FIVEPOINTS_TOKEN row collapsed into the corrected one. Standing operator actions unchanged: delete the INSTANTLY line by hand, drop the Calcom and ElevenLabs keys, drop the mail service-account JSON. Secrets-architecture ruling of the same date, refined the same evening: keys stay in .env, hardened – chmod 600 plus a complete escrow of every variable in the password manager – and local-only by explicit ruling: nothing key-shaped enters git in any form, encrypted or otherwise. The escrow is the sole off-machine copy, so its non-Mac reachability check is load-bearing.*
