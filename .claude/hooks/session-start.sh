#!/bin/bash
# SessionStart hook. Injects current active state from the global CLAUDE.md
# Current state snapshot section as additionalContext for the new session.
# Read-only, no external calls, falls back gracefully if grep fails.

claude_md="$HOME/.claude/CLAUDE.md"

if [ ! -f "$claude_md" ]; then
  exit 0
fi

# Pull the four lines under "Current state snapshot:" — fitness phase, language, content priority, business priority.
state=$(awk '
  /^\*\*Current state snapshot:\*\*$/ { capturing=1; next }
  capturing && /^---$/ { exit }
  capturing && /^- / { print }
' "$claude_md")

if [ -z "$state" ]; then
  exit 0
fi

context="Active state at session start:
$state"

jq -n --arg ctx "$context" '{hookSpecificOutput: {hookEventName: "SessionStart", additionalContext: $ctx}}'
