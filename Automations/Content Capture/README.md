# Content Capture

Act 0 of the Martywood content pipeline (SOP MW-000). Bridges the three local
capture rails into the Notion Content Calendar.

## Design

The sweep is read-only and holds no credentials. It reports what is sitting on
the rails as JSON; the agent reads that report, shows the haul for approval and
writes the Idea rows through the Notion MCP. This keeps a single credential path
and keeps the operator in the loop, per the on-command sweep ruling.

## Rails

| Rail | Source | Queue state |
|---|---|---|
| Voice | Apple Voice Memos, `CloudRecordings.db` metadata store | Watermark file |
| Notes | Apple Notes, folder `Capture` | The folder itself |
| Paper | Photographed into the `Capture` folder in Notes | The folder itself |

Apple Notes needs no watermark: landed notes move to the `Captured` folder, so an
empty `Capture` folder means the rail is clear. Voice Memos is not scriptable, so
recordings are tracked by a watermark at
`.working/capture-sweep/watermark.json`.

## Usage

```bash
python3 capture-sweep.py                 # both rails, since the last sweep
python3 capture-sweep.py --since 14      # last 14 days, ignoring the watermark
python3 capture-sweep.py --rail notes    # one rail only
python3 capture-sweep.py --mark          # stamp the watermark after landing rows
python3 capture-sweep.py --file-note ID  # move a landed note to Captured
```

Trigger phrase: "empty the notebook".

## Transcription

Voice memos are transcribed locally. The script auto-detects, in order:

1. `whisper-cli` or `whisper-cpp` on PATH, converting via ffmpeg (installed)
2. `mlx_whisper` importable by the running Python

With neither present, recordings are still reported with title, timestamp,
duration and path, and each carries `"error": "no transcriber installed"`.

To install the Apple Silicon build:

```bash
brew install whisper-cpp
```

Nothing leaves the machine. No audio is sent to any API.

## Permissions

First run prompts for macOS Automation access to Notes. Voice Memos is read
directly from disk and needs no permission grant.
