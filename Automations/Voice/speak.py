#!/usr/bin/env python3
"""
Alfred voice mode - Stop hook handler.

Reads the Claude Code Stop-hook JSON from stdin, extracts the text of the
assistant message that just completed, reduces it to clean spoken prose, and
reads it aloud with the macOS `say` command in a British voice.

Invoked by .claude/hooks/stop-speak.sh, which gates on the voice flag file so
this script only runs when voice mode is switched on. Speech is launched
detached so the hook returns immediately and never blocks the prompt. Each new
turn interrupts any speech still running from the previous one.

Fully offline: it reads the local transcript and calls the system `say`
binary. No text leaves the machine.

Configuration via environment variables:
  ALFRED_VOICE       macOS voice name        (default: Daniel, en_GB)
  ALFRED_VOICE_RATE  speaking rate, wpm      (default: 180)
"""

import json
import os
import re
import subprocess
import sys

VOICE = os.environ.get("ALFRED_VOICE", "Jamie (Premium)")
RATE = os.environ.get("ALFRED_VOICE_RATE", "180")
MAX_CHARS = 8000  # safety cap so an oversized response is not an endless monologue


def read_last_assistant_text(transcript_path):
    """Return the text of the most recent main-thread assistant message."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""
    last_text = ""
    with open(transcript_path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("type") != "assistant":
                continue
            if entry.get("isSidechain"):
                continue  # skip subagent output; only the main thread speaks
            content = entry.get("message", {}).get("content", [])
            if not isinstance(content, list):
                continue
            parts = [
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            ]
            text = "".join(parts).strip()
            if text:
                last_text = text  # keep overwriting so the final message wins
    return last_text


def sanitise(text):
    """Reduce markdown to clean prose suitable for text-to-speech."""
    # Fenced code blocks - drop entirely, leave a pause.
    text = re.sub(r"```.*?```", ". ", text, flags=re.DOTALL)
    # Images - drop.
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    # Links - keep the visible text, drop the URL.
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    # Bare URLs - drop.
    text = re.sub(r"https?://\S+", "", text)
    # Inline code - keep the content, drop the backticks.
    text = text.replace("`", "")
    # Table separator rows - drop.
    text = re.sub(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", "", text, flags=re.MULTILINE)
    # Remaining table pipes - turn into pauses.
    text = text.replace("|", ", ")
    # Headers, blockquotes and list markers at the start of a line.
    text = re.sub(r"^\s{0,3}#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    # Horizontal rules.
    text = re.sub(r"^\s*([-*_])\1{2,}\s*$", "", text, flags=re.MULTILINE)
    # Emphasis and strikethrough markers.
    text = text.replace("**", "").replace("__", "").replace("~~", "")
    text = re.sub(r"(?<!\w)[*_](\S)", r"\1", text)
    text = re.sub(r"(\S)[*_](?!\w)", r"\1", text)
    # En dash used as an aside - read it as a pause.
    text = text.replace(" - ", ", ").replace(" – ", ", ").replace("–", ", ")
    # Collapse whitespace; paragraph breaks become sentence boundaries.
    text = re.sub(r"\n{2,}", ". ", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"(?:\.\s*){2,}", ". ", text)  # tidy doubled periods
    return text.strip()


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    spoken = sanitise(read_last_assistant_text(payload.get("transcript_path", "")))
    if not spoken:
        return 0
    if len(spoken) > MAX_CHARS:
        spoken = spoken[:MAX_CHARS].rsplit(" ", 1)[0] + ". The rest is on screen."

    # Interrupt any speech still running from the previous turn.
    subprocess.run(
        ["killall", "say"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    # Launch detached, feeding text on stdin so a leading dash is never read as a flag.
    proc = subprocess.Popen(
        ["say", "-v", VOICE, "-r", str(RATE)],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    try:
        proc.stdin.write(spoken.encode("utf-8"))
        proc.stdin.close()
    except (BrokenPipeError, OSError):
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
