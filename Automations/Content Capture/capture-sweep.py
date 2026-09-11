#!/usr/bin/env python3
"""
Capture sweep for the Martywood content pipeline (SOP MW-000, Act 0).

Reads the local capture rails and emits a JSON report on stdout. Read-only:
it holds no credentials, touches no network and writes nothing to Notion.
The agent reads this report, shows the haul and lands the rows on approval.

Rails:
  voice   Apple Voice Memos, read from the CloudRecordings metadata store.
          Transcribed locally when a transcriber is installed.
  notes   Apple Notes, folder "Capture". Landed notes move to "Captured".

Usage:
  capture-sweep.py                 report both rails since the last watermark
  capture-sweep.py --since 14      report the last 14 days, ignoring watermark
  capture-sweep.py --rail notes    report one rail only
  capture-sweep.py --mark          stamp the watermark after a successful land
  capture-sweep.py --file-note ID  move one note to "Captured" after landing
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sqlite3
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

VOICE_DB = (
    Path.home()
    / "Library/Group Containers/group.com.apple.VoiceMemos.shared"
    / "Recordings/CloudRecordings.db"
)
WATERMARK = Path.home() / "Alfred Pennyworth/.working/capture-sweep/watermark.json"
CAPTURE_FOLDER = "Capture"
FILED_FOLDER = "Captured"

# Core Data reference date: 2001-01-01 UTC.
CORE_DATA_EPOCH = 978307200


def run_osascript(script):
    result = subprocess.run(
        ["osascript", "-e", script], capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "osascript failed")
    return result.stdout


def read_watermark():
    if not WATERMARK.exists():
        return None
    try:
        return json.loads(WATERMARK.read_text()).get("last_sweep")
    except (json.JSONDecodeError, OSError):
        return None


def write_watermark():
    WATERMARK.parent.mkdir(parents=True, exist_ok=True)
    WATERMARK.write_text(
        json.dumps({"last_sweep": datetime.now(timezone.utc).isoformat()}, indent=2)
    )


def find_transcriber():
    """Return a callable that transcribes a file, or None if nothing is installed."""
    if shutil.which("whisper-cli"):
        return "whisper-cli"
    if shutil.which("whisper-cpp"):
        return "whisper-cpp"
    try:
        subprocess.run(
            [sys.executable, "-c", "import mlx_whisper"],
            capture_output=True,
            check=True,
            timeout=30,
        )
        return "mlx_whisper"
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        return None


def transcribe(path, engine):
    if engine == "mlx_whisper":
        script = (
            "import mlx_whisper, json, sys; "
            "print(json.dumps(mlx_whisper.transcribe(sys.argv[1], "
            "path_or_hf_repo='mlx-community/whisper-medium-mlx')['text']))"
        )
        result = subprocess.run(
            [sys.executable, "-c", script, str(path)],
            capture_output=True,
            text=True,
            timeout=900,
        )
        if result.returncode != 0:
            return None, result.stderr.strip()[:300]
        return json.loads(result.stdout.strip()).strip(), None

    # whisper.cpp needs 16 kHz mono WAV.
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio.wav"
        conv = subprocess.run(
            ["ffmpeg", "-nostdin", "-loglevel", "error", "-i", str(path),
             "-ar", "16000", "-ac", "1", str(wav)],
            capture_output=True, text=True, timeout=300,
        )
        if conv.returncode != 0:
            return None, "ffmpeg conversion failed"
        result = subprocess.run(
            [engine, "-f", str(wav), "-nt", "-np"],
            capture_output=True, text=True, timeout=900,
        )
        if result.returncode != 0:
            return None, result.stderr.strip()[:300]
        return " ".join(result.stdout.split()), None


def sweep_voice(cutoff, engine):
    if not VOICE_DB.exists():
        return {"available": False, "reason": "Voice Memos store not found", "items": []}

    cutoff_cd = cutoff.timestamp() - CORE_DATA_EPOCH
    con = sqlite3.connect(f"file:{VOICE_DB}?mode=ro", uri=True)
    try:
        rows = con.execute(
            "SELECT ZUNIQUEID, ZCUSTOMLABEL, ZPATH, ZDATE, ZDURATION "
            "FROM ZCLOUDRECORDING WHERE ZDATE > ? AND ZPATH IS NOT NULL "
            "ORDER BY ZDATE DESC",
            (cutoff_cd,),
        ).fetchall()
    finally:
        con.close()

    items = []
    for uid, label, path, zdate, duration in rows:
        audio = VOICE_DB.parent / path
        recorded = datetime.fromtimestamp(zdate + CORE_DATA_EPOCH).astimezone()
        item = {
            "rail": "voice",
            "id": uid,
            "title": label or path,
            "recorded_at": recorded.isoformat(),
            "duration_seconds": round(duration or 0, 1),
            "path": str(audio),
            "exists": audio.exists(),
            "transcript": None,
            "error": None,
        }
        if audio.exists() and engine:
            item["transcript"], item["error"] = transcribe(audio, engine)
        elif not engine:
            item["error"] = "no transcriber installed"
        items.append(item)

    return {"available": True, "engine": engine, "items": items}


def sweep_notes():
    script = f'''
    tell application "Notes"
        if not (exists folder "{CAPTURE_FOLDER}") then return ""
        set out to ""
        repeat with n in notes of folder "{CAPTURE_FOLDER}"
            set out to out & "<<<REC>>>" & (id of n as string) & "<<<F>>>" ¬
                & (name of n as string) & "<<<F>>>" ¬
                & ((creation date of n) as string) & "<<<F>>>" ¬
                & (body of n as string)
        end repeat
        return out
    end tell
    '''
    try:
        raw = run_osascript(script)
    except RuntimeError as exc:
        return {"available": False, "reason": str(exc), "items": []}

    items = []
    for chunk in raw.split("<<<REC>>>")[1:]:
        parts = chunk.split("<<<F>>>")
        if len(parts) < 4:
            continue
        note_id, name, created, body = parts[0], parts[1], parts[2], "<<<F>>>".join(parts[3:])
        title = name.strip()
        text = html_to_text(body)
        # Notes carries the title as the body's first line, and repeats it
        # when the note was created programmatically. Strip every leading copy.
        while title:
            first, sep, rest = text.partition("\n")
            if first.strip() != title:
                break
            text = rest.strip() if sep else ""
        items.append({
            "rail": "notes",
            "id": note_id.strip(),
            "title": title,
            "created_at": created.strip(),
            "body": text,
        })
    return {"available": True, "items": items}


def html_to_text(html):
    text = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    text = re.sub(r"</(div|p|li|h[1-6])>", "\n", text, flags=re.I)
    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    replacements = {
        "&nbsp;": " ", "&amp;": "&", "&lt;": "<",
        "&gt;": ">", "&quot;": '"', "&#39;": "'",
    }
    for entity, char in replacements.items():
        text = text.replace(entity, char)
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line.strip()).strip()


def file_note(note_id):
    script = f'''
    tell application "Notes"
        set n to note id "{note_id}"
        move n to folder "{FILED_FOLDER}"
    end tell
    '''
    run_osascript(script)


def main():
    parser = argparse.ArgumentParser(description="Sweep the local capture rails.")
    parser.add_argument("--since", type=float, metavar="DAYS",
                        help="look back this many days, ignoring the watermark")
    parser.add_argument("--rail", choices=["voice", "notes"],
                        help="sweep a single rail")
    parser.add_argument("--mark", action="store_true",
                        help="stamp the watermark and exit")
    parser.add_argument("--file-note", metavar="ID",
                        help="move a landed note to the Captured folder")
    args = parser.parse_args()

    if args.mark:
        write_watermark()
        print(json.dumps({"watermark": read_watermark()}))
        return

    if args.file_note:
        file_note(args.file_note)
        print(json.dumps({"filed": args.file_note}))
        return

    if args.since is not None:
        cutoff = datetime.now().astimezone() - timedelta(days=args.since)
        window = f"last {args.since:g} days"
    else:
        mark = read_watermark()
        if mark:
            cutoff = datetime.fromisoformat(mark).astimezone()
            window = f"since last sweep, {mark}"
        else:
            cutoff = datetime.now().astimezone() - timedelta(days=14)
            window = "last 14 days, no prior sweep"

    report = {
        "swept_at": datetime.now().astimezone().isoformat(),
        "window": window,
        "rails": {},
    }
    if args.rail in (None, "voice"):
        report["rails"]["voice"] = sweep_voice(cutoff, find_transcriber())
    if args.rail in (None, "notes"):
        report["rails"]["notes"] = sweep_notes()

    report["total"] = sum(
        len(rail.get("items", [])) for rail in report["rails"].values()
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
