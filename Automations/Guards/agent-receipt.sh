#!/bin/bash
# Deterministic receipt writer for scheduled agents.
#
# A receipt written by model judgment is not a receipt: it depends on the run
# reaching its final step and on a Write permission that a headless scheduled
# run has no channel to approve. This script makes the receipt a Bash call
# instead, matching the mechanism that keeps oracle-platform's receipt fresh.
#
# Usage:
#   agent-receipt.sh <agent> <status> [detail ...]
#
#   agent   scheduled-agent name; becomes .working/<agent>/handoff.md
#   status  ok | alert | partial | blocked | failed
#   detail  free text appended as the Detail line (optional)
#
# Exit codes: 0 written, 1 bad arguments.

set -euo pipefail

project_dir="${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}"

agent="${1:-}"
status="${2:-}"
shift 2 2>/dev/null || true
detail="${*:-none recorded}"

if [ -z "$agent" ] || [ -z "$status" ]; then
  echo "usage: agent-receipt.sh <agent> <status> [detail ...]" >&2
  exit 1
fi

case "$status" in
  ok|alert|partial|blocked|failed) ;;
  *) echo "status must be one of: ok alert partial blocked failed" >&2; exit 1 ;;
esac

dir="$project_dir/.working/$agent"
mkdir -p "$dir"

stamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
local_stamp=$(date +%Y-%m-%d\ %H:%M\ %Z)

cat > "$dir/handoff.md" <<RECEIPT
---
agent: $agent
status: $status
run_completed: $stamp
written_by: Automations/Guards/agent-receipt.sh
---

# $agent receipt

- Run completed: $local_stamp
- Status: $status
- Detail: $detail

This receipt is written deterministically by the agent-receipt script, not by
the agent's own judgment. Its presence proves the run reached completion; its
timestamp is the liveness signal the next sweep reads.
RECEIPT

echo "receipt written: .working/$agent/handoff.md ($status)"
