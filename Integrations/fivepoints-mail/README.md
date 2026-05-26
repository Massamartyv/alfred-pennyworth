# Five Points Mail MCP

Venture-scoped Gmail access for Five Points Digital Studio. Exposes the five
inboxes of the `fivepoints.studio` Google Workspace to Alfred and its agents
via a unified MCP with `mailbox` routing.

## Mailboxes

| Mailbox key | Address | Purpose |
|---|---|---|
| `hello` | `hello@fivepoints.studio` | Workspace admin. General engagements and admin. |
| `martavious` | `martavious@fivepoints.studio` | Owner-direct. Personal studio communications. |
| `systems` | `systems@fivepoints.studio` | Technical infrastructure and dev tooling. |
| `opportunities` | `opportunities@fivepoints.studio` | Sponsors, press, hiring and vendor inquiries. |
| `finance` | `finance@fivepoints.studio` | Business banking, invoicing, financial platforms. |

Every tool takes a `mailbox` parameter. There is no implicit default so
nothing can be read or written without an explicit mailbox selection.

## Architecture

One Google Cloud service account with domain-wide delegation impersonates
each user per request. Single credential, five inboxes, no per-mailbox OAuth
flows. Future inboxes added to the domain are reachable without any new
authentication work -- add them to the `MAILBOX_REGISTRY` in `server.py` and
redeploy.

```
┌──────────────────────────────────────────────────┐
│ fivepoints-mail MCP                              │
│ ┌──────────────────────────────────────────────┐ │
│ │ service-account.json (domain-wide delegation)│ │
│ └──────────────────────────────────────────────┘ │
│            │              │             │        │
│     hello@       martavious@      systems@ ...   │
└──────────────────────────────────────────────────┘
```

## Setup

### Google Cloud

1. Create a project or reuse an existing Five Points GCP project.
2. Enable the Gmail API (APIs & Services > Library > Gmail API > Enable).
3. Create a service account (IAM & Admin > Service Accounts).
4. On the service account's Keys tab, create a JSON key and download it.
5. Note the service account's Unique ID from the Details tab.

### Workspace Admin

1. Sign into https://admin.google.com as `hello@fivepoints.studio`.
2. Security > Access and data control > API controls > Manage Domain-wide
   Delegation > Add new.
3. Paste the service account Unique ID as the OAuth Client ID.
4. Add the scopes:

   ```
   https://www.googleapis.com/auth/gmail.modify,
   https://www.googleapis.com/auth/gmail.send,
   https://www.googleapis.com/auth/gmail.readonly,
   https://www.googleapis.com/auth/gmail.compose
   ```

### Local

1. Drop the downloaded JSON key at
   `Integrations/fivepoints-mail/credentials/service-account.json`.
   (Gitignored -- never commit.)
2. Create the venv and install dependencies:

   ```bash
   cd "Integrations/fivepoints-mail"
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Register the MCP with Claude Code:

   ```bash
   claude mcp add fivepoints-mail -- \
     "/Users/martyspicer/Alfred Pennyworth/Integrations/fivepoints-mail/.venv/bin/python" \
     "/Users/martyspicer/Alfred Pennyworth/Integrations/fivepoints-mail/server.py"
   ```

4. In a fresh Claude Code session, run `health_check` against each mailbox
   to verify impersonation works end to end.

## Environment variables

- `FIVEPOINTS_MAIL_SERVICE_ACCOUNT` (optional) -- override the default
  credentials path. Defaults to `./credentials/service-account.json`.

## Tools

### Read

- `list_mailboxes()` -- the registry.
- `health_check(mailbox?)` -- verify Gmail API access per mailbox.
- `list_messages(mailbox, query?, max_results?, label_ids?, include_spam_trash?)`
- `search(mailbox, query, max_results?)`
- `read_message(mailbox, message_id, format?)`
- `list_threads(mailbox, query?, max_results?, label_ids?)`
- `get_thread(mailbox, thread_id)`
- `list_labels(mailbox)`
- `list_drafts(mailbox, max_results?)`

### Write -- Navigation Rule 3 applies

Every write tool documents `writes: True` so the calling agent asks for
confirmation before dispatch.

- `create_draft(request)` -- compose a draft. Does not send.
- `update_draft(mailbox, draft_id, to, subject, body, ...)`
- `delete_draft(mailbox, draft_id)`
- `send_draft(mailbox, draft_id)` -- requires explicit confirmation.
- `send_message(request)` -- compose and send in one step. Prefer draft-first.
- `create_reply_draft(request)` -- reply with thread preservation.
- `modify_labels(update)` -- archive, star, mark read, etc.
- `trash_message(mailbox, message_id)` / `untrash_message(...)`

## Gmail search syntax quick reference

- `is:unread`, `is:read`, `is:starred`
- `from:name@domain.com`, `to:name@domain.com`
- `subject:"exact phrase"`
- `newer_than:7d`, `older_than:30d`, `after:2026/04/01`
- `has:attachment`, `filename:pdf`
- `label:inbox`, `-label:inbox` (archived)
- Combine with `AND` / `OR` / `()` as needed.

## Scope boundary

This MCP is venture-scoped to Five Points. Personal email routes through the
Apple Mail MCP (`mcp-apple-mail`), never through this server. Never cross the
boundary.
