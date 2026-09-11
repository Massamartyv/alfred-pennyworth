#!/bin/bash
# The monitor of the monitors - Whetstone Layer 2, first duty.
#
# Deterministic liveness check over the estate's own instrumentation. It makes
# no judgment and calls no model: every assertion is a file, a timestamp or a
# count. That is the point. The alarms that failed between July and September
# 2026 all failed silently, and every one of them would have tripped a check
# in this file.
#
# Usage:
#   monitor-check.sh              human-readable report, exit 1 on any failure
#   monitor-check.sh --quiet      print only failures
#
# Exit codes: 0 all checks pass, 1 one or more failures.

set -uo pipefail

project_dir="${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}"
working="$project_dir/.working"
cache="$project_dir/.claude/cache"
now=$(date +%s)
quiet=false
[ "${1:-}" = "--quiet" ] && quiet=true

failures=0
lines=""

report() {  # status, name, detail
  local status="$1" name="$2" detail="$3"
  if [ "$status" = "FAIL" ]; then
    failures=$((failures + 1))
    lines+="FAIL  $name - $detail"$'\n'
  elif [ "$quiet" = false ]; then
    lines+="ok    $name - $detail"$'\n'
  fi
}

age_days() {  # path -> whole days since mtime, or -1 if missing
  [ -e "$1" ] || { echo -1; return; }
  local m; m=$(stat -f %m "$1" 2>/dev/null) || { echo -1; return; }
  echo $(( (now - m) / 86400 ))
}

# 1. Heartbeat marker matches the current month
marker_file="$cache/last-heartbeat"
if [ -f "$marker_file" ]; then
  marker=$(tr -d '[:space:]' < "$marker_file")
  current=$(date +%Y-%m)
  if [ "$marker" = "$current" ]; then
    report ok "heartbeat" "marker $marker is current"
  else
    report FAIL "heartbeat" "marker $marker, current month $current - heartbeat unrun"
  fi
else
  report FAIL "heartbeat" "no marker at .claude/cache/last-heartbeat"
fi

# 2. State cache younger than 7 days
cache_age=$(age_days "$cache/state-cache.md")
if [ "$cache_age" -lt 0 ]; then
  report FAIL "state-cache" "missing"
elif [ "$cache_age" -le 7 ]; then
  report ok "state-cache" "${cache_age}d old, allowance 7d"
else
  report FAIL "state-cache" "${cache_age}d old, allowance 7d - session-end bookend not closing"
fi

# 3. Offline buffer drained
buffer="$working/session-buffer"
if [ -d "$buffer" ]; then
  pending=$(find "$buffer" -type f -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
  if [ "$pending" -eq 0 ]; then
    report ok "buffer" "empty"
  else
    oldest=$(find "$buffer" -type f -name '*.md' -exec stat -f %m {} + 2>/dev/null | sort -n | head -1)
    odays=$(( (now - ${oldest:-$now}) / 86400 ))
    report FAIL "buffer" "$pending entries unsynced, oldest ${odays}d - sync to Notion before other state work"
  fi
else
  report ok "buffer" "no buffer directory"
fi

# 4. Scheduled-agent receipts inside their allowances.
#    name:allowance_days. A receipt older than its allowance means the agent
#    has not completed a run in its window, whatever the scheduler claims.
for entry in watchtower:2 oracle-platform:2 weekly-review:8 monthly-review:32 contact-card-sync:32; do
  name="${entry%%:*}"
  allowance="${entry##*:}"
  rdays=$(age_days "$working/$name/handoff.md")
  if [ "$rdays" -lt 0 ]; then
    report FAIL "receipt/$name" "missing, allowance ${allowance}d"
  elif [ "$rdays" -le "$allowance" ]; then
    report ok "receipt/$name" "${rdays}d old, allowance ${allowance}d"
  else
    report FAIL "receipt/$name" "${rdays}d old, allowance ${allowance}d - runs are not completing"
  fi
done

# 5. Receipts must be script-written. A receipt the model wrote by hand is a
#    claim; one the script wrote is evidence. Flag the difference.
for name in watchtower oracle-platform; do
  r="$working/$name/handoff.md"
  if [ -f "$r" ] && ! grep -q "written_by:\|Agent: \|handoff$" "$r" 2>/dev/null; then
    report FAIL "provenance/$name" "receipt carries no writer stamp"
  fi
done

printf '%s' "$lines"

if [ "$failures" -gt 0 ]; then
  echo "MONITOR ALERT: $failures check(s) failed"
  exit 1
fi
[ "$quiet" = false ] && echo "all checks pass"
exit 0
