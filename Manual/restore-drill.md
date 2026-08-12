# Restore Drill – Quarterly Fire-Drill Protocol

**Purpose:** a backup that has never been restored is a hypothesis. This drill converts `genesis.md` from hypothesis to a tested procedure each quarter. The goal is not to rebuild the system – it is to discover drift before a real emergency forces the discovery under pressure.

---

## Protocol

1. **Create the drill account.** In System Settings > Users and Groups, create a new standard macOS user named `drill` on the current machine. Do not use the primary account for any drill step. The isolation is the point.

2. **Execute genesis.md from Step 1.** Inside the drill account, follow `genesis.md` in sequence as far as reality allows. Complete the following layers where they do not touch the primary account or require irreversible external actions:
   - Homebrew installation and package layer
   - Shell configuration layer (`.zshrc`, prompt, aliases)
   - `gh auth login` using existing credentials
   - Clone both repos (`alfred-pennyworth`, `alfred-vault`) to the drill-account canonical paths
   - Vault restore into `~/.claude` in the drill account
   - Python venv rebuilds for all integrations
   - Record every step where the documented procedure is wrong, ambiguous, or out of date. These are findings, not failures to note later – capture them in real time.

3. **Skip with a dry-read.** The following steps cannot be safely executed in a drill account without disturbing the primary account or external state. For each, read the documented procedure and verify it still matches the provider's current UI or flow:
   - Account re-creation at any external provider
   - TCC permission re-grants that would affect primary account settings
   - Scheduled-task registration (heartbeat, watchtower, pattern-memo) in cron or launchd
   - claude.ai connector re-grants in the Claude web app
   - Any Stripe, Notion, or banking configuration steps
   - Mark each skipped step explicitly in the drill report with the reason and whether the documentation appears current.

4. **Run the genesis verification checklist.** Execute every verification check in `genesis.md` that is feasible inside the drill account. Each check should return a pass. If it does not, capture the failure and the exact error.

5. **Score the drill.** Assign one of three outcomes to each `genesis.md` step:
   - **Pass** – executed without issue, documentation was accurate
   - **Fail** – execution errored or blocked and the document did not prevent it
   - **Drifted** – the procedure worked but the document no longer describes what was done (UI changed, path changed, command changed)
   File the full scored report as an Alfred Logs entry – Log Type Audit/Analysis, related to the Alfred operating system project – matching the heartbeat's instruction for the same artefact.

6. **Fix the manuals the same day.** Update `genesis.md`, `accounts-inventory.md`, and `secrets-inventory.md` to match what the drill revealed. Do not carry forward known drift. Drift compounds between drills and is unacceptable in a life-insurance document.

7. **Delete the drill user account.** System Settings > Users and Groups > select drill account > delete. Remove the home directory when prompted. Leave no residual state on the primary machine.

---

## Cadence

Quarterly. Register the recurrence in `Agents/heartbeat.md` alongside the other cadenced maintenance tasks. Suggested months: January, April, July, October – the first week of the quarter.

**Time budget:** approximately 90 minutes.

---

## Failure rule

If any step fails hard – not drifted, but genuinely broken to the point where a real restore would stall – that fix is the highest-priority item of the week. Not the next drill cycle. This week.

The manual is the system's life insurance. A known gap in life insurance is not an acceptable open item.

---

*Last updated: 2026-08-11 – Domesday truth pass: drill-report destination corrected from the retired Logs/ directory to Notion Alfred Logs, resolving the contradiction with Agents/heartbeat.md.*
