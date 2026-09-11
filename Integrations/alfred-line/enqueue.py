#!/usr/bin/env python3
"""Queue an outbound message on the Alfred line.

Runs in the operator session. Writes a job to the spool; the send daemon in
Alfred's login session picks it up and delivers it through Messages.app.

Usage:
    ./enqueue.py "Message body"
    ./enqueue.py --to someone@example.com "Message body"
    echo "Message body" | ./enqueue.py
"""

import argparse
import json
import sys
import time
import uuid

from config import OPERATOR_ADDRESSES, OUTBOX, ensure_dirs


def enqueue(text: str, to: str) -> str:
    ensure_dirs()
    job_id = f"{time.time():.6f}-{uuid.uuid4().hex[:8]}"
    path = OUTBOX / f"{job_id}.json"
    payload = {"id": job_id, "to": to, "text": text, "queued_at": time.time()}

    # Write to a temporary name first so the daemon never reads a partial file.
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, indent=2))
    tmp.rename(path)
    return job_id


def main():
    parser = argparse.ArgumentParser(description="Send a message on the Alfred line.")
    parser.add_argument("text", nargs="?", help="message body; read from stdin if omitted")
    parser.add_argument("--to", default=OPERATOR_ADDRESSES[0], help="recipient address")
    args = parser.parse_args()

    text = args.text if args.text is not None else sys.stdin.read()
    text = text.strip()
    if not text:
        parser.error("refusing to send an empty message")

    job_id = enqueue(text, args.to)
    print(f"queued {job_id} -> {args.to}")


if __name__ == "__main__":
    main()
