#!/bin/bash
# SessionStart hook. Injects the one-way Notion state cache, warns on an
# unsynced offline buffer, and raises the monthly heartbeat reminder on
# month rollover. Local reads only; no network calls. Read-only: the
# last-heartbeat marker is written by the heartbeat run itself, not here.

project_dir="${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}"
cache="$project_dir/.claude/cache/state-cache.md"
buffer_dir="$project_dir/.working/session-buffer"
marker="$project_dir/.claude/cache/last-heartbeat"

parts=""

if [ -f "$cache" ]; then
  mtime=$(stat -f %m "$cache" 2>/dev/null || echo 0)
  now=$(date +%s)
  days=$(( (now - mtime) / 86400 ))
  header="State cache, refreshed $days day(s) ago:"
  if [ "$days" -ge 7 ]; then
    header="STALE state cache ($days days old) - a session-end bookend was likely missed. Refresh from Notion early this session."
  fi
  parts="$header
$(cat "$cache")"
else
  parts="No state cache present. Render one from Notion at this session's end bookend."
fi

if [ -d "$buffer_dir" ] && [ -n "$(ls -A "$buffer_dir" 2>/dev/null)" ]; then
  parts="$parts

Unsynced state buffer present at .working/session-buffer/ - sync it to Notion before any other state work."
fi

current_month=$(date +%Y-%m)
last_month=$(cat "$marker" 2>/dev/null || echo "")
if [ "$current_month" != "$last_month" ]; then
  parts="$parts

Month rollover: run the monthly heartbeat cadences in Agents/heartbeat.md, then write $current_month to .claude/cache/last-heartbeat."
fi

parts="$parts

Standing doctrine: state reads and writes go to Notion in the correct scope; never write Status, Stage or Pending blocks to local files. Close the session with the bookend - Alfred Logs entry, leftovers filed as Tasks, state cache refreshed."

jq -n --arg ctx "$parts" '{hookSpecificOutput: {hookEventName: "SessionStart", additionalContext: $ctx}}'
