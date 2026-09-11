"""Shared configuration for the Alfred line.

The line is a two-user iMessage bridge. Messages.app permits one iMessage
account per macOS login session, so Alfred runs in his own login session
under his own Apple ID. The two sessions cannot drive each other's
AppleScript, so they communicate through a spool directory that both users
can read and write.

Nothing here is secret. The Apple ID password lives in Keychain, entered by
the operator when signing Messages in.
"""

import os
from pathlib import Path

# The address Alfred sends from. Owned by the Apple ID signed into Messages
# in the `alfred` login session.
ALFRED_ADDRESS = "alfred.pennyworth@icloud.com"

# Addresses Alfred will accept inbound messages from. Anything else is
# ignored rather than woken on, so a wrong number cannot start a session.
OPERATOR_ADDRESSES = [
    "martavious.spicer@icloud.com",
]

# Spool root. Readable and writable by both login sessions.
SPOOL = Path(os.environ.get("ALFRED_LINE_SPOOL", "/Users/Shared/alfred-line"))

OUTBOX = SPOOL / "outbox"   # written by the operator session, drained by Alfred
SENT = SPOOL / "sent"       # outbound archive
FAILED = SPOOL / "failed"   # outbound that could not be delivered
INBOX = SPOOL / "inbox"     # written by Alfred, drained by the operator session
HANDLED = SPOOL / "handled"  # inbound archive

ALL_DIRS = [OUTBOX, SENT, FAILED, INBOX, HANDLED]

# Repository root, used by the wake handler to start sessions in the right place.
PROJECT_DIR = Path.home() / "Alfred Pennyworth"


def ensure_dirs():
    """Create the spool tree. Mode 0777 because two different users own files here.

    This is a single-operator machine; the tradeoff is documented in README.md.
    """
    for d in [SPOOL] + ALL_DIRS:
        d.mkdir(parents=True, exist_ok=True)
        try:
            os.chmod(d, 0o777)
        except PermissionError:
            # Directory already exists and is owned by the other user. If it is
            # already group-writable this is harmless.
            pass
