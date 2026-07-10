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

## Step 7 – Secrets

1. Recreate `/Users/martyspicer/Alfred Pennyworth/.env` from `secrets-inventory.md` – every key name is listed there with its re-issue procedure. Values come from the password manager or by re-issuing at the provider.
2. Run `direnv allow` at the repo root.
3. By design, Alfred is denied read access to `.env` and `.envrc` (see `~/.claude/settings.json` deny list). Populate the file by hand.

## Step 8 – Python integrations

Each custom MCP server rebuilds its own virtual environment:

```bash
cd "/Users/martyspicer/Alfred Pennyworth/Integrations"
for d in fivepoints-mail strava pennyone instantly fullscript-mcp; do
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

The vault restores the six task definitions at `~/.claude/scheduled-tasks/`, but **restoring files does not re-register schedules**. Recreate each registration per the heartbeat table (`Agents/heartbeat.md`):

| Task | Cadence |
|---|---|
| watchtower | Daily, evening |
| penny-one (portfolio briefing) | Weekly, Monday morning |
| context-audit | First of month |
| media-scanner | First of month |
| pattern-memo | First of month |
| sphere-review | First of quarter |

Ask Alfred to re-register them (the scheduled-task tools handle creation), then verify the scheduler list matches the table above.

## Step 15 – Plugins

`~/.claude/settings.json` (restored by the vault) carries the enabled plugins and both marketplaces (claude-plugins-official, knowledge-work-plugins). Launch Claude Code and run `/plugin` to confirm installs completed; install anything missing from the listed marketplaces.

## Step 16 – Apps

```bash
git clone https://github.com/Massamartyv/catalogue.git "/Users/martyspicer/Alfred Pennyworth/Apps/catalogue"
cd "/Users/martyspicer/Alfred Pennyworth/Apps/catalogue" && npm install
```

`.env.local` from its `.env.example` (ANTHROPIC_API_KEY optional – enables the didactic panel).

## Step 17 – Voice mode

No external dependencies – the Stop hook uses the native macOS `say` command, and both the hook script and its registration arrived with the repo in Step 4. Toggle: tell Alfred "voice on" or run `Automations/Voice/voice on`. Flag file: `.working/voice/enabled`.

---

## Step 18 – Verification checklist

Run after rebuild; every line must pass before declaring the system restored.

| Probe | Expected |
|---|---|
| `claude doctor` | No errors |
| `claude mcp list` | All servers connected |
| `health_check` on pennyone, instantly, fivepoints-mail | Healthy responses |
| Ask Alfred: "What fitness phase am I in?" | Correct answer from memory/state (proves memory restored) |
| Ask Alfred to draft (not send) an iMessage | Draft produced; send prompts for confirmation (proves gating intact) |
| Scheduled-task list vs heartbeat table | All six registered with correct cadences |
| Statusline visible with scope and phase | Hook layer working |
| Voice toggle on, say one response, toggle off | Voice automation working |
| `git -C ~/.claude status` and repo `git status` | Clean, tracking remotes |

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
