# Voice

Reads Alfred's responses aloud through the macOS `say` command, so a session can
be heard rather than read. Speech is gated behind an on-demand toggle and runs
entirely offline.

## How it works

A `Stop` hook fires when the assistant finishes a response. The hook gate at
`.claude/hooks/stop-speak.sh` checks the voice flag; if voice is off it exits at
once. If voice is on, it pipes the hook payload to `speak.py`, which:

1. Reads the just-completed assistant message from the session transcript.
2. Strips markdown, code blocks and links down to clean spoken prose.
3. Reads it aloud with the `say` command, launched detached so the prompt is
   never blocked. Each new response interrupts any speech still in progress.

Nothing leaves the machine. The transcript is local and `say` is the built-in
offline macOS synthesiser.

## Switching it on and off

Voice is off by default. Two ways to toggle it:

- **Tell Alfred** "voice on" or "voice off" in conversation.
- **Run the command** from this directory:

  ```bash
  ./voice on       # switch on
  ./voice off      # switch off and stop any speech
  ./voice          # toggle
  ./voice status   # report current state
  ./voice stop     # cut off speech in progress, leave the toggle as is
  ```

State lives in `.working/voice/enabled` - the file existing means on.

The `Stop` hook is registered in `.claude/settings.json`. A change to that file
takes effect from the next session start, so the very first activation may need
a fresh session; the toggle and `speak.py` work immediately.

## Configuration

Set these environment variables before the session to change the voice:

| Variable            | Default  | Meaning                          |
|---------------------|----------|----------------------------------|
| `ALFRED_VOICE`      | `Jamie (Premium)` | macOS voice name (en_GB)         |
| `ALFRED_VOICE_RATE` | `180`    | speaking rate in words per minute |

List installed voices with `say -v '?'`. `Jamie (Premium)` is the default, a
downloaded premium en-GB voice. `Daniel` is the always-present built-in
fallback. Other premium or enhanced voices can be downloaded in System
Settings, Accessibility, Spoken Content, System Voice, Manage Voices, then
named in `ALFRED_VOICE`.

Responses longer than 8000 characters are truncated for speech with a spoken
note that the rest is on screen. Adjust `MAX_CHARS` in `speak.py` to change it.

## Files

| File                          | Tracked | Role                                  |
|-------------------------------|---------|---------------------------------------|
| `Automations/Voice/speak.py`  | yes     | transcript read, sanitise, speak      |
| `Automations/Voice/voice`     | yes     | on/off/toggle/status/stop             |
| `Automations/Voice/README.md` | yes     | this file                             |
| `.claude/hooks/stop-speak.sh` | no      | local hook gate (`.claude` gitignored) |
| `.working/voice/enabled`      | no      | transient on/off flag                 |
