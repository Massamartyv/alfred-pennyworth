#!/usr/bin/env python3
"""Outbound half of the Alfred line. Runs in Alfred's login session.

Drains the spool outbox and delivers each message through Messages.app under
Alfred's own Apple ID. Requires Automation permission for Messages.app in this
login session, granted on first send.
"""

import json
import logging
import subprocess
import time

from config import FAILED, OUTBOX, SENT, ensure_dirs

POLL_SECONDS = 2

# Arguments are passed to osascript rather than interpolated into the source,
# so message bodies containing quotes or newlines cannot break the script.
APPLESCRIPT = """
on run argv
    set targetAddr to item 1 of argv
    set msgText to item 2 of argv
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to participant targetAddr of targetService
        send msgText to targetBuddy
    end tell
end run
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s send_daemon %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)


def deliver(to: str, text: str):
    result = subprocess.run(
        ["osascript", "-", to, text],
        input=APPLESCRIPT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "osascript failed")


def drain_once():
    for path in sorted(OUTBOX.glob("*.json")):
        try:
            job = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            log.error("unreadable job %s: %s", path.name, exc)
            path.rename(FAILED / path.name)
            continue

        try:
            deliver(job["to"], job["text"])
        except Exception as exc:
            log.error("delivery failed for %s: %s", path.name, exc)
            job["error"] = str(exc)
            job["failed_at"] = time.time()
            (FAILED / path.name).write_text(json.dumps(job, indent=2))
            path.unlink()
            continue

        job["sent_at"] = time.time()
        (SENT / path.name).write_text(json.dumps(job, indent=2))
        path.unlink()
        log.info("sent %s to %s", job["id"], job["to"])


def main():
    ensure_dirs()
    log.info("watching %s", OUTBOX)
    while True:
        try:
            drain_once()
        except Exception:
            log.exception("drain cycle failed")
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
