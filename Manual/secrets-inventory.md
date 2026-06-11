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
| `ZERNIO_MARTYGRAS_API_KEY` | Pennyone Marty Gras pipeline (future) | Zernio dashboard for the Marty Gras account when provisioned |
| `ZERNIO_PARADIGM_API_KEY` | Pennyone Paradigm pipeline (future) | Zernio dashboard for the Paradigm account when provisioned |
| `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Pennyone Lillie and Lynette pipeline (future) | Zernio dashboard for the L&L account when provisioned |
| `INSTANTLY_FIVEPOINTS_API_KEY` | instantly MCP | Instantly workspace settings > API; generate a v2 API key (v1 keys are not compatible with the MCP) |
| `STRAVA_CLIENT_ID` | strava MCP bootstrap | strava.com/settings/api > My API Application; the Client ID is shown in plain text and does not rotate unless the app is deleted and recreated |
| `STRAVA_CLIENT_SECRET` | strava MCP bootstrap | same location as Client ID; reset via "Reset Secret" button; callback domain must remain localhost |
| `FULLSCRIPT_CLIENT_ID` | fullscript MCP | Fullscript practitioner portal > Developer settings > OAuth application; Client ID is static unless the app is deleted |
| `FULLSCRIPT_CLIENT_SECRET` | fullscript MCP | Same app; delete and recreate the app to rotate the secret; update `FULLSCRIPT_ENV` and `FULLSCRIPT_BASE_URL` to match the environment (sandbox vs. production) |
| `FULLSCRIPT_ENV` | fullscript MCP | Set to `production` for live use; `sandbox` for testing; determined by which Fullscript app is registered |
| `FULLSCRIPT_BASE_URL` | fullscript MCP | Fullscript API base URL for the environment; confirm in Fullscript developer documentation at time of re-issue |
| `APIFY_PERSONAL_TOKEN` | scraping – personal scope | Apify console (personal account) > Settings > Integrations > Personal API tokens |
| `APIFY_FIVEPOINTS_TOKEN` | scraping – Five Points scope | Apify console (Five Points account) > same path as above |
| `ANTHROPIC_API_KEY` | Catalogue app didactic panel (its own `.env.local`, not the repo root `.env`) | Anthropic console > API keys; the Catalogue app manages this separately from the Claude Code session |
| `DISCORD_BOT_TOKEN` | discord-setup MCP | Discord developer portal > Applications > select the bot > Bot tab > Reset Token; update permissions and re-invite if the bot was removed during the reset |
| ElevenLabs API key | ElevenLabs integrations (if wired) | confirm against `.env` by hand; this inventory was assembled from integration documentation because `.env` is read-denied |
| Perplexity API key | Perplexity integrations (if wired) | confirm against `.env` by hand; same caveat as above |

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

*Last updated: 2026-06-11*
