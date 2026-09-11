# Genesis Protocol – Rebuilding Alfred from Zero

This is the disaster-recovery runbook for the Alfred operating system. It assumes total machine loss: a new or wiped Mac, no local files, no installed tools. Followed in order, it restores the full system – identity, memory, skills, agents, integrations and scheduled automation.

Scope: rebuild on replacement hardware with existing accounts. It does not cover re-creating the accounts themselves; see `accounts-inventory.md` for that layer.

**Read this first:** Steps are ordered by dependency. Do not skip ahead – later steps assume earlier state. Estimated time for a full rebuild: 2 to 4 hours, dominated by account re-authentication.

---

## Step 0 – Standing prerequisites (maintain these BEFORE any disaster)

The rebuild is only possible if these survive the machine:

1. **Password manager access** from a non-Mac device (phone). Contains all account credentials referenced in `accounts-inventory.md`.
2. **GitHub credentials and 2FA recovery codes** for `Massamartyv` and `studio-fivepoints` – escrowed in the password manager. The entire rebuild flows through GitHub; losing both accounts is the only unrecoverable failure mode.
3. **Apple ID credentials and recovery key** – iCloud holds the Alfred-os archive and syncs the off-device manual copy.
4. **An off-device copy of this manual** – the `alfred-pennyworth` repo is private but reachable from any browser at github.com once signed in. A standalone copy of the Manual directory lives in iCloud Drive under `Alfred Archives/Manual/`, refreshed whenever the Manual changes.
5. **2FA devices** – phone number portability matters more than the phone itself.

Quarterly restore drills (see `restore-drill.md`) keep this document honest.

---

## Step 1 – macOS base

1. Complete macOS setup. **Create the user account with short name `martyspicer`.** This is load-bearing: the memory layer keys off the absolute path `/Users/martyspicer/Alfred Pennyworth` (the project slug `-Users-martyspicer-Alfred-Pennyworth` derives from it). A different short name orphans every memory file until paths are migrated.
2. Sign into Apple ID. Let iCloud Drive settle before relying on its contents.
3. Install Xcode Command Line Tools: `xcode-select --install` (provides git).
4. Install Homebrew: instructions at brew.sh.
5. Install the toolchain from the committed Brewfile (after Step 4 clone, or download the raw file from GitHub first):
   ```bash
   brew bundle --file="/Users/martyspicer/Alfred Pennyworth/Manual/Brewfile"
   ```
   The Brewfile's `uv` and `npm` stanzas are part of the same run: they install `mcp-apple-mail` (landing at `~/.local/bin/mcp-apple-mail`, needed in Step 10) and the global `vercel` CLI.

## Step 2 – Shell layer

The repo expects direnv to load `.env` into any shell rooted in the project.

1. Add to `~/.zshrc`:
   ```bash
   eval "$(direnv hook zsh)"
   export PATH="$HOME/.local/bin:$PATH"
   ```
2. Restart the shell or `source ~/.zshrc`.

## Step 3 – GitHub authentication

```bash
gh auth login          # Massamartyv (personal) – primary
gh auth login          # studio-fivepoints (Five Points) – second account
gh auth switch --user Massamartyv
gh auth setup-git
git config --global user.name "Martavious Spicer"
git config --global user.email "20412262+Massamartyv@users.noreply.github.com"
```

Five Points repos override email per-repo to `martavious@fivepoints.studio`.

**Two accounts, one active.** `gh auth setup-git` makes gh the credential helper for every GitHub push, and gh only ever lends git its *active* account. Whichever account is not active cannot reach its own private repos – the failure reads `Repository not found`, which is misleading, since the repo exists and git is presenting the wrong account. Each clone is therefore pinned to its owning account once cloned, at the end of Step 16, and after that the active account no longer matters. Never fix a failed push by switching accounts; rerun the pin.

## Step 4 – Clone the estate

```bash
git clone https://github.com/Massamartyv/alfred-pennyworth.git "/Users/martyspicer/Alfred Pennyworth"
cd "/Users/martyspicer/Alfred Pennyworth" && git config core.hooksPath .githooks
```

The path, including the space, is exact. Do not rename. The second command wires the tracked git hooks (pre-commit state tripwire); it is per-clone configuration and must be rerun on every fresh clone.

## Step 5 – Restore the vault (BEFORE first Claude Code launch)

The durable global layer lives in the private `alfred-vault` repo and must be in place before Claude Code first runs. The vault tracks the restore-critical set – identity file, memory, skills, output style, scheduled-task definitions, settings – and Claude Code will grow untracked runtime directories (sessions, telemetry and similar) around it as it runs; that is expected, not drift:

```bash
git clone https://github.com/Massamartyv/alfred-vault.git /Users/martyspicer/.claude
```

If `~/.claude` already exists (Claude Code installed first), clone elsewhere and copy the contents in, keeping the vault's `.git/`.

## Step 6 – Claude Code

1. Install Claude Code (current instructions at code.claude.com; historically `npm install -g @anthropic-ai/claude-code`).
2. `claude login` with the Anthropic account (see accounts inventory).
3. Run `claude doctor` – resolve anything red.
4. Launch `claude` inside `/Users/martyspicer/Alfred Pennyworth`: trust the folder when prompted and approve the project MCP servers from `.mcp.json`.
5. Confirm the output style is active – responses should arrive in Alfred's voice. The vault's settings.json already selects it; `/output-style alfred-voice` is the fallback only if that setting did not take effect.
6. Confirm the three project hooks fired. All three are tracked files (`.claude/hooks/` and `.claude/settings.json` are un-ignored via the negation lines in `.gitignore`) and arrived with the Step 4 clone – nothing further to configure:
   - **SessionStart** (`session-start.sh`) – injects the state-cache summary, flags an unsynced offline buffer, and raises the monthly heartbeat reminder on month rollover. Confirm its output appeared at this session's start.
   - **Stop** (`stop-speak.sh`) – the voice-mode gate; silent unless voice is toggled on (Step 17).
   - **statusLine** (`statusline.sh`) – renders `model | scope | phase | cost` in the terminal status line. Confirm it is visible and non-blank.

## Step 7 – Secrets

1. Recreate `/Users/martyspicer/Alfred Pennyworth/.env` from `secrets-inventory.md` – every key name is listed there with its re-issue procedure. Values come from the password manager or by re-issuing at the provider.
2. Run `direnv allow` at the repo root.
3. By design, Alfred is denied read access to `.env` and `.envrc` (see `~/.claude/settings.json` deny list). Populate the file by hand.

## Step 8 – Python integrations

Each custom MCP server rebuilds its own virtual environment. As of 2026-07-23 there are seven – `instantly` is gone (see `mcp-registry.md`); `discord-setup-mcp` is Node-based and rebuilds via `npm install` per Step 9, not this loop:

```bash
cd "/Users/martyspicer/Alfred Pennyworth/Integrations"
for d in fivepoints-mail strava pennyone fullscript-mcp calcom fivepoints-calendar apple-calendar; do
  (cd "$d" && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt)
done
```

## Step 9 – Integration-specific authentication

These hold state outside both repos and must be re-established:

- **fivepoints-mail** – Google Cloud service account with domain-wide delegation. The JSON key is NOT in git: re-download from the GCP console (or create fresh per `Integrations/fivepoints-mail/README.md` – GCP service account, Gmail API enabled, DWD scopes added at admin.google.com as hello@fivepoints.studio) and place at `Integrations/fivepoints-mail/credentials/service-account.json` – the filename is exact; the server resolves that path by default.
- **strava** – tokens live at `~/.config/alfred/strava-tokens.json`. Re-mint: export `STRAVA_CLIENT_ID` and `STRAVA_CLIENT_SECRET`, run `Integrations/strava/.venv/bin/python Integrations/strava/bootstrap.py`, approve in the browser.
- **discord-setup-mcp** – lives in its own repository (gitignored here). Clone it back to `Integrations/discord-setup-mcp/`, `npm install`, and ensure `DISCORD_BOT_TOKEN` is provisioned per its README.
- **apple-mail** – `uv tool install` of `mcp-apple-mail` (patrickfreyer, GitHub) provides `~/.local/bin/mcp-apple-mail`. Covered by the Brewfile uv line; verify the binary exists.
- **fullscript** – no auth file; the four `FULLSCRIPT_*` variables in `.env` (Step 7) are the entire credential set. The server registers from the committed `.mcp.json` alongside the other project servers.

## Step 10 – MCP registration

**Project scope** – `.mcp.json` is committed to the repo and self-sources `.env`. Nothing to recreate; approve the servers on first launch (Step 6.4).

**User scope** – `~/.claude.json` is not in the vault (it carries machine and session state). Re-register:

```bash
claude mcp add --scope user apple-mail /Users/martyspicer/.local/bin/mcp-apple-mail
claude mcp add --scope user fivepoints-mail "/Users/martyspicer/Alfred Pennyworth/Integrations/fivepoints-mail/.venv/bin/python" "/Users/martyspicer/Alfred Pennyworth/Integrations/fivepoints-mail/server.py"
claude mcp add --scope user discord-setup "/Users/martyspicer/Alfred Pennyworth/Integrations/discord-setup-mcp/run.sh"
```

Verify with `claude mcp list` – every server green. Full registry and routing: `mcp-registry.md`.

## Step 11 – Claude Desktop layer

1. Install the Claude desktop app.
2. Re-grant the claude.ai connectors in app settings: Notion (personal workspace), Supabase (personal), Vercel, Google Drive. These live server-side on no disk and carry new internal IDs after re-granting.
3. **Connector IDs change on re-grant.** The permission ask-list in `~/.claude/settings.json` gates several connector tools by their old IDs (`mcp__fae54ad8-…`, `mcp__3cad28e2-…`). Update those entries to the new IDs – `mcp-registry.md` documents which tools must stay gated.
4. Desktop built-ins (iMessage, Apple Notes, computer use, preview, Chrome) arrive with the app; they need only macOS permissions (Step 12).

## Step 12 – macOS permissions (TCC)

Each prompts on first use; grant deliberately:

- Automation: terminal and Claude → Mail, Messages, Notes (AppleScript bridges)
- Full Disk Access: for Messages database reads (chat.db)
- Accessibility and Screen Recording: computer use
- Contacts: iMessage contact resolution

Sign Mail.app and Messages into the relevant accounts at the OS level first.

## Step 13 – CLI authentications

```bash
vercel login        # personal account; Five Points work uses the second Vercel account
supabase login      # personal; Five Points Supabase is token-based via .env
```

`vercel link` inside each app repo as needed.

## Step 14 – Scheduled agents

**Verified live 2026-07-23: exactly four tasks are registered with the scheduler.** The vault restores SKILL.md definitions at `~/.claude/scheduled-tasks/` for these four plus six retired ones, but **restoring files does not re-register schedules** – re-create each of the four below per its SKILL.md and the heartbeat table (`Agents/heartbeat.md`):

| Task | Cadence | Cron |
|---|---|---|
| `watchtower` | Daily, evening | `0 20 * * *` |
| `oracle-platform` | Daily, morning | `0 8 * * *` |
| `contact-card-sync` | Monthly, day 5 | `0 9 5 * *` |
| `wealth-benchmark-refresh` | Annual, 20 September | `0 9 20 9 *` |

**Six further SKILL.md directories survive on disk but are deliberately NOT registered** – recovery artefacts only, do not re-register them without first clearing the gate named against each:

| Directory | Status |
|---|---|
| `catalogue-likes` | Superseded – renamed to `oracle-platform` when the app renamed from Catalogue to Oracle |
| `context-audit` | Deliberately absent – interactive report-and-ask agent, runs inside heartbeat sessions only |
| `media-scanner` | Deliberately absent – same reason |
| `sphere-review` | Deliberately absent – same reason |
| `penny-one` | Deregistered 2026-07-23 (The Lamplighter) – portfolio-briefing ownership collapsed to Watchtower; gated on a redesign session before reactivation |
| `pattern-memo` | Headless scheduling paused 2026-07-23 – gated on a Notion API quota / plan decision; runs on demand inside a live session until reactivated |

Ask Alfred to re-register the four live tasks (the scheduled-task tools handle creation), then verify the scheduler list matches the four-row table above exactly – not ten, not six.

## Step 15 – Plugins

`~/.claude/settings.json` (restored by the vault) carries the enabled plugins and both marketplaces (claude-plugins-official, knowledge-work-plugins). Launch Claude Code and run `/plugin` to confirm installs completed; install anything missing from the listed marketplaces.

## Step 16 – Apps

Oracle (built as "Catalogue", renamed since): the app's own remote is still named `catalogue` as of 2026-07-23 – **a rename to `oracle` is pending operator action** – but it clones into the `Apps/oracle` directory per the standard Apps/ layout:

```bash
git clone https://github.com/Massamartyv/catalogue.git "/Users/martyspicer/Alfred Pennyworth/Apps/oracle"
cd "/Users/martyspicer/Alfred Pennyworth/Apps/oracle" && npm install
```

Build `.env.local` from its `.env.example` – every variable is optional at the code level, but `ANTHROPIC_API_KEY` and `NOTION_TOKEN` are required for the `oracle-platform` scheduled task (Step 14) to file complete Media entries, and the `YT_OAUTH_*` trio needs its own one-time browser authorisation (`npm run yt:auth`). Full variable set and re-issue procedures: `secrets-inventory.md`.

### Pin every clone to its owning account

Run once every repo above is cloned, and again after any later clone:

```bash
"/Users/martyspicer/Alfred Pennyworth/Manual/pin-github-accounts.sh"
gh auth switch --user studio-fivepoints
```

The script finds every clone in the estate and gives each one a local credential helper that asks gh for the owning account's token by name – `Massamartyv` for the estate, vault, oracle and templates, `studio-fivepoints` for the Five Points apps. No token is written to disk. Repos owned by anyone else, client repos among them, are skipped. It must be rerun on every fresh clone because the pin lives in each clone's `.git/config`. The switch back to `studio-fivepoints` is optional once pinned; it is simply the account the Five Points tooling expects to find active.

## Step 17 – Voice mode

No external dependencies – the Stop hook uses the native macOS `say` command, and both the hook script and its registration arrived with the repo in Step 4. Toggle: tell Alfred "voice on" or run `Automations/Voice/voice on`. Flag file: `.working/voice/enabled`.

---

## Step 18 – Verification checklist

Run after rebuild; every line must pass before declaring the system restored.

| Probe | Expected |
|---|---|
| `claude doctor` | No errors |
| `claude mcp list` | All ten project-scope servers connected, no `instantly` |
| `health_check` on pennyone, fivepoints-mail | Healthy responses |
| Ask Alfred: "What fitness phase am I in?" | Correct answer from memory/state (proves memory restored) |
| Ask Alfred to draft (not send) an iMessage | Draft produced; send prompts for confirmation (proves gating intact) |
| Scheduled-task list vs Step 14 table | Exactly four registered (`watchtower`, `oracle-platform`, `contact-card-sync`, `wealth-benchmark-refresh`) with correct cadences; the six retired SKILL.md directories present but NOT in the live list |
| Statusline visible with scope and phase | Hook layer working (see Step 6.6 for all three hooks) |
| Voice toggle on, say one response, toggle off | Voice automation working |
| `git -C ~/.claude status` and repo `git status` | Clean, tracking remotes |
| `Manual/pin-github-accounts.sh` | `0 failed` – every personal and Five Points clone reachable whichever gh account is active |

---

## Appendix – Load-bearing paths

| Path | Why it matters |
|---|---|
| `/Users/martyspicer/Alfred Pennyworth` | Project root; memory slug derives from it; exact spelling and space required |
| `/Users/martyspicer/.claude` | The vault: identity, memory, skills, settings, scheduled tasks |
| `~/.claude/projects/-Users-martyspicer-Alfred-Pennyworth/memory/` | All persistent memory; inside the vault repo |
| `~/.config/alfred/strava-tokens.json` | Strava OAuth state; outside both repos; re-minted by bootstrap |
| `Integrations/fivepoints-mail/credentials/` | Google service-account key; outside git; re-downloaded from GCP |
| `~/.claude.json` | User-scope MCP registrations and session state; recreated, never restored |
| iCloud Drive `Alfred Archives/` | Cold archives (retired Alfred-os source, manual PDF) |

---

*Last updated: 2026-09-11 – GitHub account pinning: Step 3 explains why gh lends git only its active account, Step 16 gains the pin step and `Manual/pin-github-accounts.sh`, Step 18 gains its probe. Previously 2026-07-23 – The Lamplighter, registries lane: hooks wiring made explicit (Step 6.6), the venv rebuild loop corrected to the live seven-server set with `instantly` removed, Step 14 rewritten to the four live scheduled tasks plus the six retired SKILL.md directories, Step 16 corrected to clone into `Apps/oracle` from the still-named `catalogue` remote, Step 18 checklist trued up to match.*
