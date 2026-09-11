#!/usr/bin/env python3
"""Wake handler for the Alfred line. Runs in the operator session.

Watches the spool inbox and starts a headless Claude session for each inbound
message. The session decides what to do and replies by calling enqueue.py.

Messages are handled strictly one at a time. A review conversation edits a
single Notion entry, so two concurrent sessions would race each other.
"""

import json
import logging
import subprocess
import time

from config import HANDLED, INBOX, PROJECT_DIR, ensure_dirs

POLL_SECONDS = 2

# Wait briefly before handling, so a burst of texts arrives as one turn
# rather than three sessions talking over each other.
DEBOUNCE_SECONDS = 6

SESSION_TIMEOUT = 600

INSTRUCTIONS = PROJECT_DIR / "Integrations" / "alfred-line" / "conversation.md"

PROMPT = """A message has arrived on Alfred's line, the dedicated iMessage \
address the operator uses to correspond with you.

From: {sender}
Message: {body}

Read {instructions} and follow it. Reply by running enqueue.py from \
Integrations/alfred-line. Do not reply by any other channel."""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s wake %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)


def handle(message: dict):
    prompt = PROMPT.format(
        sender=message["from"],
        body=message["text"],
        instructions=INSTRUCTIONS,
    )
    log.info("starting session for inbound %s", message["rowid"])
    result = subprocess.run(
        ["claude", "-p", prompt],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        timeout=SESSION_TIMEOUT,
    )
    if result.returncode != 0:
        log.error("session failed: %s", result.stderr.strip()[:500])
    else:
        log.info("session finished for %s", message["rowid"])


def pending():
    """Return spooled messages that have settled past the debounce window."""
    now = time.time()
    ready = []
    for path in sorted(INBOX.glob("*.json"), key=lambda p: int(p.stem)):
        try:
            message = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if now - message.get("spooled_at", 0) >= DEBOUNCE_SECONDS:
            ready.append((path, message))
    return ready


def main():
    ensure_dirs()
    log.info("watching %s", INBOX)
    while True:
        try:
            for path, message in pending():
                try:
                    handle(message)
                except subprocess.TimeoutExpired:
                    log.error("session timed out for %s", message["rowid"])
                except Exception:
                    log.exception("handler failed for %s", message["rowid"])
                finally:
                    # Archive either way. A message that crashed a session must
                    # not be retried forever.
                    path.rename(HANDLED / path.name)
        except Exception:
            log.exception("watch cycle failed")
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
