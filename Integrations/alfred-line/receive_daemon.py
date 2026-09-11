#!/usr/bin/env python3
"""Inbound half of the Alfred line. Runs in Alfred's login session.

Polls Alfred's own Messages database for messages received from the operator
and writes each one into the spool inbox. The operator session picks them up
and wakes a Claude session.

Requires Full Disk Access for the process running this daemon, because
~/Library/Messages/chat.db is protected. Grant it to /usr/bin/python3 (or to
the interpreter named in the LaunchAgent) in the `alfred` login session.
"""

import json
import logging
import plistlib
import re
import shutil
import sqlite3
import tempfile
import time
from pathlib import Path

from config import INBOX, OPERATOR_ADDRESSES, ensure_dirs

POLL_SECONDS = 3
CHAT_DB = Path.home() / "Library" / "Messages" / "chat.db"
CURSOR = Path.home() / "Library" / "Application Support" / "alfred-line" / "cursor"

# Messages stores dates as nanoseconds since 2001-01-01.
APPLE_EPOCH_OFFSET = 978307200

QUERY = """
SELECT m.ROWID, m.text, m.attributedBody, m.date, h.id
FROM message m
LEFT JOIN handle h ON m.handle_id = h.ROWID
WHERE m.is_from_me = 0 AND m.ROWID > ?
ORDER BY m.ROWID ASC
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s receive_daemon %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)


def read_cursor() -> int:
    try:
        return int(CURSOR.read_text().strip())
    except (OSError, ValueError):
        return 0


def write_cursor(rowid: int):
    CURSOR.parent.mkdir(parents=True, exist_ok=True)
    CURSOR.write_text(str(rowid))


def extract_text(text, attributed_body) -> str:
    """Return the message body.

    Recent macOS often leaves `text` NULL and stores the body in
    `attributedBody`, an NSAttributedString archive. The typed-stream format is
    not worth a full parser here, so pull the readable run out of it.
    """
    if text:
        return text
    if not attributed_body:
        return ""
    try:
        decoded = plistlib.loads(attributed_body)
        if isinstance(decoded, dict):
            for key in ("NSString", "NSAttributedString"):
                if key in decoded:
                    return str(decoded[key])
    except Exception:
        pass
    # Fall back to the longest printable run in the archive.
    blob = attributed_body.decode("utf-8", errors="ignore")
    runs = re.findall(r"[ -~\n\t]{4,}", blob)
    return max(runs, key=len).strip() if runs else ""


def snapshot_db() -> Path:
    """Copy the database before reading it.

    Messages holds chat.db open in WAL mode and writes to it constantly.
    Reading the live file produces locking errors, so work on a copy.
    """
    tmpdir = Path(tempfile.mkdtemp(prefix="alfred-line-"))
    for suffix in ("", "-wal", "-shm"):
        src = Path(str(CHAT_DB) + suffix)
        if src.exists():
            shutil.copy2(src, tmpdir / src.name)
    return tmpdir / CHAT_DB.name


def poll_once():
    last = read_cursor()
    snapshot = snapshot_db()
    try:
        conn = sqlite3.connect(f"file:{snapshot}?mode=ro", uri=True)
        rows = conn.execute(QUERY, (last,)).fetchall()
        conn.close()
    finally:
        shutil.rmtree(snapshot.parent, ignore_errors=True)

    highest = last
    for rowid, text, attributed_body, date, sender in rows:
        highest = max(highest, rowid)

        if sender not in OPERATOR_ADDRESSES:
            # Ignore anything not from the operator. A wrong number must never
            # be able to start a session.
            log.info("ignoring message %s from %s", rowid, sender)
            continue

        body = extract_text(text, attributed_body).strip()
        if not body:
            continue

        payload = {
            "rowid": rowid,
            "from": sender,
            "text": body,
            "received_at": date / 1e9 + APPLE_EPOCH_OFFSET,
            "spooled_at": time.time(),
        }
        path = INBOX / f"{rowid}.json"
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, indent=2))
        tmp.rename(path)
        log.info("spooled inbound %s from %s", rowid, sender)

    if highest > last:
        write_cursor(highest)


def main():
    ensure_dirs()
    if read_cursor() == 0:
        # First run: start from the current end of the database rather than
        # replaying the entire message history into the inbox.
        snapshot = snapshot_db()
        try:
            conn = sqlite3.connect(f"file:{snapshot}?mode=ro", uri=True)
            row = conn.execute("SELECT COALESCE(MAX(ROWID), 0) FROM message").fetchone()
            conn.close()
            write_cursor(row[0])
            log.info("initialised cursor at rowid %s", row[0])
        finally:
            shutil.rmtree(snapshot.parent, ignore_errors=True)

    log.info("watching %s", CHAT_DB)
    while True:
        try:
            poll_once()
        except Exception:
            log.exception("poll cycle failed")
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
