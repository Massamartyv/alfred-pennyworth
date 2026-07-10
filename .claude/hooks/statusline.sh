#!/bin/bash
# Alfred OS status line.
# Reads JSON session state from stdin and renders: model | scope | active phase | cost.
# Falls back to defaults if any field is missing.

input=$(cat)

model=$(echo "$input" | jq -r '.model.display_name // "Opus 4.7"' 2>/dev/null)
output_style=$(echo "$input" | jq -r '.output_style.name // "default"' 2>/dev/null)
total_cost=$(echo "$input" | jq -r '.cost.total_cost_usd // 0' 2>/dev/null)
cwd=$(echo "$input" | jq -r '.workspace.current_dir // ""' 2>/dev/null)

# Determine scope from current working directory.
scope="personal"
case "$cwd" in
  *"Five Points Digital Studio"*) scope="five points" ;;
  *"Marty Gras"*) scope="marty gras" ;;
  *"Paradigm"*) scope="paradigm" ;;
  *"Lillie and Lynette"*) scope="lillie & lynette" ;;
  *"Athena"*) scope="athena (dormant)" ;;
esac

# Pull active fitness phase from the Notion state cache.
phase=$(grep -E "^- Fitness phase:" "${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}/.claude/cache/state-cache.md" 2>/dev/null | sed -E 's/^- Fitness phase: *([A-Za-z]+).*/\1/' | head -n 1)
[ -z "$phase" ] && phase="—"

# Cost rendering.
if [ -n "$total_cost" ] && [ "$total_cost" != "null" ] && [ "$total_cost" != "0" ]; then
  cost=$(printf '$%.2f' "$total_cost")
else
  cost="—"
fi

printf '%s | %s | %s | %s' "$model" "$scope" "$phase" "$cost"
