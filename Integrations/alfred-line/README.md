# Alfred line

A dedicated iMessage address for Alfred, so correspondence with the operator is
a two-way thread between two parties rather than the operator texting himself.

Status: built, not yet provisioned. The three provisioning steps below require
the operator's hands and have not been run.

## Why it is shaped this way

Messages.app signs into exactly one iMessage account per macOS login session.
For Alfred to send from his own address, Messages must be signed in as him,
which means a second login session on this Mac. AppleScript cannot cross
between login sessions, so the two sides talk through a spool directory under
`/Users/Shared/alfred-line`.

```
operator session                     alfred session
  enqueue.py  ── outbox/ ──────────►  send_daemon.py ──► Messages.app
  wake.py     ◄──── inbox/ ─────────  receive_daemon.py ◄── chat.db
    │
    └─► claude -p ──► conversation.md ──► enqueue.py
```

Conversation state is not stored here. A review conversation lives in its Notion
Reflections entry: the movement checkboxes are the thread, and the first
unticked box is the current position. See `conversation.md`.

## Provisioning – operator only

These three steps cannot be automated. Account creation and password entry are
the operator's alone.

1. **Create Alfred's Apple ID.** Address `alfred.pennyworth@icloud.com`,
   created as a new iCloud address during Apple ID signup. If that address is
   taken, pick another and update `ALFRED_ADDRESS` in `config.py`. Recovery
   contact is the operator's own iCloud account.

2. **Create the macOS account.** System Settings, Users and Groups, add a
   Standard user with full name "Alfred Pennyworth" and account name `alfred`.
   Enable fast user switching. The session must stay logged in for the line to
   work, so log into it and switch back rather than logging out.

3. **Sign Messages in.** In the `alfred` session, open Messages, sign into the
   new Apple ID, and confirm the iMessage address is enabled under Settings,
   iMessage.

Then, in the `alfred` session:

```bash
"/Users/Shared/alfred-line/install.sh" --alfred
```

and in the operator session:

```bash
"/Users/martyspicer/Alfred Pennyworth/Integrations/alfred-line/install.sh" --operator
```

The install script stages the daemons into `/Users/Shared/alfred-line/bin`
because the Alfred session cannot read the operator home directory.

## Permissions

Two macOS grants are needed in the `alfred` session, both prompted on first use:

- **Automation → Messages.app**, for the send daemon. Triggered by the first
  outbound message.
- **Full Disk Access → /usr/bin/python3**, for the receive daemon, because
  `~/Library/Messages/chat.db` is protected. This one must be granted manually
  in System Settings, Privacy and Security; the daemon logs a permission error
  until it is.

## Verifying

From the operator session:

```bash
"/Users/martyspicer/Alfred Pennyworth/Integrations/alfred-line/enqueue.py" "Line test."
```

The message should arrive from Alfred's address within a few seconds. Reply to
it; `/Users/Shared/alfred-line/logs/wake.log` should show a session starting.

## Known tradeoffs

- **Spool permissions.** The spool directories are mode 777 because two users
  write to them and creating a shared group needs administrator rights. This is
  a single-operator machine, so the exposure is other processes running as the
  operator, which already have his privileges.
- **Both sessions must stay logged in.** A reboot leaves the Alfred session
  logged out and the line dead until someone logs into it. There is no way
  around this short of a dedicated machine.
- **Apple may break this.** AppleScript access to Messages and the schema of
  `chat.db` are both undocumented and have changed before. Expect repair after
  major macOS releases. This was accepted as a known cost when the transport
  was chosen.
- **Inbound is polled, not pushed.** Three-second interval. A reply is picked up
  within roughly ten seconds including the debounce.

## Not yet done

The weekly and monthly review scheduled tasks still send through the operator's
own iMessage account. They should be rewired to open the conversation on this
line once it is verified live – deliberately deferred, so a working nudge is not
broken on an unprovisioned dependency.
