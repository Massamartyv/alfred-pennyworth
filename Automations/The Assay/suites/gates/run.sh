#!/bin/bash
# The Assay - suite one: gates and monitors.
#
# Seeded-fault drills against the real gate layer - Automations/Guards/ and
# Automations/Whetstone/monitor-check.sh. Every drill seeds a known fault
# into a fixture (never into the live estate), calls the real gate script
# against that fixture, and asserts the gate catches it. Deterministic, no
# model call. Scalar is pass rate across drills.
#
# --prove-red is a standing self-check, not a one-off manual act: it
# temporarily renames one live gate script aside, re-runs the drill that
# depends on it, asserts the drill goes red, then restores the script via a
# trap that fires on any exit path. This is the literal proof the operation
# brief asks for, made repeatable rather than performed once by hand.
#
# Exit 0 pass, 1 fail, 3 unscoreable (not used by this suite - the gate
# layer always has a clean verifier: file presence, exit code, or a count).

set -uo pipefail

ASSAY_PROJECT_DIR="${ASSAY_PROJECT_DIR:-${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}}"
guards="$ASSAY_PROJECT_DIR/Automations/Guards"
whetstone="$ASSAY_PROJECT_DIR/Automations/Whetstone"
fixture_root=$(mktemp -d "${TMPDIR:-/tmp}/assay-gates.XXXXXX")
trap 'rm -rf "$fixture_root"' EXIT

drills_total=0
drills_pass=0
report=""

record() {  # status(PASS|FAIL) name detail
  drills_total=$((drills_total + 1))
  if [ "$1" = "PASS" ]; then
    drills_pass=$((drills_pass + 1))
  fi
  report+="$1  $2 - $3"$'\n'
}

# ---------------------------------------------------------------------
# Drill 1 - state-patterns.grep tripwire
# ---------------------------------------------------------------------
pattern_file="$guards/state-patterns.grep"

clean_fixture="$fixture_root/clean.md"
cat > "$clean_fixture" <<'EOF'
# A durable context file

This file carries only durable knowledge, no live state. See the sphere
principles and nothing that reads as a status or pipeline block.
EOF

seeded_fixture="$fixture_root/seeded.md"
cat > "$seeded_fixture" <<'EOF'
# A file that should never pass the tripwire

- Status: In Progress
- Pending: awaiting operator ruling

This is exactly the shape of block the Drift Audit is meant to catch.
EOF

if [ -f "$pattern_file" ]; then
  # Match the exact invocation the live tripwire uses (.githooks/pre-commit:
  # grep -E -i -f). A drill that omits -i tests a gate that does not exist -
  # the pattern file's entries are lowercase and the real hook relies on
  # case-insensitive matching to catch "Status:" as well as "status:".
  if grep -qE -i -f "$pattern_file" "$clean_fixture"; then
    record FAIL "state-patterns/clean-silent" "clean fixture false-positived against $pattern_file"
  else
    record PASS "state-patterns/clean-silent" "clean fixture correctly untouched"
  fi

  if grep -qE -i -f "$pattern_file" "$seeded_fixture"; then
    record PASS "state-patterns/seeded-caught" "seeded Status/Pending block caught"
  else
    record FAIL "state-patterns/seeded-caught" "seeded Status/Pending block NOT caught - tripwire is not live"
  fi
else
  record FAIL "state-patterns/exists" "pattern file missing at $pattern_file"
fi

# ---------------------------------------------------------------------
# Drill 2 - agent-receipt.sh: correctness and rejection
# ---------------------------------------------------------------------
receipt_script="$guards/agent-receipt.sh"
receipt_project="$fixture_root/receipt-project"
mkdir -p "$receipt_project"

if CLAUDE_PROJECT_DIR="$receipt_project" "$receipt_script" fixture-agent ok "drill run" >/dev/null 2>&1; then
  receipt_file="$receipt_project/.working/fixture-agent/handoff.md"
  if [ -f "$receipt_file" ] && grep -q '^written_by: Automations/Guards/agent-receipt.sh' "$receipt_file"; then
    record PASS "agent-receipt/writes-stamped-receipt" "receipt written with provenance stamp"
  else
    record FAIL "agent-receipt/writes-stamped-receipt" "receipt missing or unstamped at $receipt_file"
  fi
else
  record FAIL "agent-receipt/writes-stamped-receipt" "script exited nonzero on a valid call"
fi

if CLAUDE_PROJECT_DIR="$receipt_project" "$receipt_script" fixture-agent bogus-status >/dev/null 2>&1; then
  record FAIL "agent-receipt/rejects-bad-status" "script accepted an invalid status - should have exited 1"
else
  record PASS "agent-receipt/rejects-bad-status" "invalid status correctly rejected"
fi

# ---------------------------------------------------------------------
# Drill 3 - working-sweep.sh hold rules
# ---------------------------------------------------------------------
sweep_script="$guards/working-sweep.sh"
sweep_project="$fixture_root/sweep-project"
sweep_working="$sweep_project/.working"
mkdir -p "$sweep_working"
old_mtime=$(( $(date +%s) - 40*86400 ))  # 40 days old, past the 30-day cutoff
new_mtime=$(date +%s)

mk_dir_at_mtime() {  # dir mtime
  # working-sweep.sh ages a directory by the mtime of the files inside it
  # (find -type f), not the directory entry itself - an empty directory
  # always reads as infinitely old. Guarantee a file exists before retiming.
  mkdir -p "$1"
  if [ -z "$(find "$1" -type f 2>/dev/null)" ]; then
    touch "$1/.assay-marker"
  fi
  local ts; ts=$(date -r "$2" +%Y%m%d%H%M.%S)
  touch -t "$ts" "$1"
  find "$1" -exec touch -t "$ts" {} \;
}

# A: session-buffer/ - always held, even stale
mk_dir_at_mtime "$sweep_working/session-buffer" "$old_mtime"
# B: watchtower/ - scheduled-agent receipt dir, always held, even stale
mk_dir_at_mtime "$sweep_working/watchtower" "$old_mtime"
# C: open mission with a partial handoff - held until the mission closes
mkdir -p "$sweep_working/open-mission"
cat > "$sweep_working/open-mission/handoff.md" <<'EOF'
---
status: partial
---
EOF
mk_dir_at_mtime "$sweep_working/open-mission" "$old_mtime"
# D: closed mission, stale - eligible for archive
mkdir -p "$sweep_working/closed-mission"
cat > "$sweep_working/closed-mission/handoff.md" <<'EOF'
---
status: complete
---
EOF
mk_dir_at_mtime "$sweep_working/closed-mission" "$old_mtime"
# E: touched recently - active, not eligible regardless of contents
mk_dir_at_mtime "$sweep_working/recent-mission" "$new_mtime"

dry_run_out=$(CLAUDE_PROJECT_DIR="$sweep_project" "$sweep_script" 2>&1)

check_line() {  # expected_prefix dirname
  if printf '%s\n' "$dry_run_out" | grep -qE "^$1[[:space:]]+$2 "; then
    record PASS "working-sweep/$2" "correctly reported $1"
  else
    record FAIL "working-sweep/$2" "expected $1 for $2, got: $(printf '%s' "$dry_run_out" | grep "$2" || echo 'no matching line')"
  fi
}

check_line "HELD" "session-buffer"
check_line "HELD" "watchtower"
check_line "HELD" "open-mission"
check_line "ELIGIBLE" "closed-mission"
check_line "ACTIVE" "recent-mission"

# --execute: closed-mission should actually move, the three held dirs stay
CLAUDE_PROJECT_DIR="$sweep_project" "$sweep_script" --execute >/dev/null 2>&1
month=$(date +%Y-%m)
if [ -d "$sweep_project/Context/Archive/working-$month/closed-mission" ] && [ ! -d "$sweep_working/closed-mission" ]; then
  record PASS "working-sweep/execute-moves-eligible" "closed-mission archived on --execute"
else
  record FAIL "working-sweep/execute-moves-eligible" "closed-mission was not archived on --execute"
fi
if [ -d "$sweep_working/session-buffer" ] && [ -d "$sweep_working/watchtower" ] && [ -d "$sweep_working/open-mission" ]; then
  record PASS "working-sweep/execute-respects-holds" "held directories survived --execute"
else
  record FAIL "working-sweep/execute-respects-holds" "a held directory was archived - hold rule broken"
fi

# ---------------------------------------------------------------------
# Drill 4 - monitor-check.sh: pass fixture and fail fixture
# ---------------------------------------------------------------------
monitor_script="$whetstone/monitor-check.sh"

pass_project="$fixture_root/monitor-pass"
mkdir -p "$pass_project/.claude/cache" "$pass_project/.working"
date +%Y-%m > "$pass_project/.claude/cache/last-heartbeat"
: > "$pass_project/.claude/cache/state-cache.md"  # fresh mtime = now
for agent in watchtower:2 oracle-platform:2 weekly-review:8 monthly-review:32 contact-card-sync:32; do
  name="${agent%%:*}"
  mkdir -p "$pass_project/.working/$name"
  cat > "$pass_project/.working/$name/handoff.md" <<EOF
---
written_by: Automations/Guards/agent-receipt.sh
---
EOF
done

if CLAUDE_PROJECT_DIR="$pass_project" "$monitor_script" --quiet >/dev/null 2>&1; then
  record PASS "monitor-check/pass-fixture" "clean fixture reports all checks passing"
else
  record FAIL "monitor-check/pass-fixture" "clean fixture unexpectedly failed monitor-check"
fi

fail_project="$fixture_root/monitor-fail"
mkdir -p "$fail_project/.claude/cache" "$fail_project/.working/session-buffer"
echo "2020-01" > "$fail_project/.claude/cache/last-heartbeat"      # stale month
: > "$fail_project/.claude/cache/state-cache.md"
touch -t "$(date -r $(( $(date +%s) - 20*86400 )) +%Y%m%d%H%M.%S)" "$fail_project/.claude/cache/state-cache.md"  # 20d old, >7d allowance
echo "unsynced" > "$fail_project/.working/session-buffer/stale-entry.md"  # nonempty buffer
# no scheduled-agent receipts at all -> all five FAIL missing

fail_out=$(CLAUDE_PROJECT_DIR="$fail_project" "$monitor_script" --quiet 2>&1)
fail_status=$?
fail_count=$(printf '%s\n' "$fail_out" | grep -c '^FAIL')

if [ "$fail_status" -ne 0 ] && [ "$fail_count" -ge 5 ]; then
  record PASS "monitor-check/fail-fixture" "seeded fixture correctly failed ($fail_count FAIL lines, exit $fail_status)"
else
  record FAIL "monitor-check/fail-fixture" "seeded fixture did not fail as expected (exit $fail_status, $fail_count FAIL lines)"
fi

# ---------------------------------------------------------------------
# --prove-red: temporarily remove one live gate, show the drill goes red
# ---------------------------------------------------------------------
prove_red_report=""
if [ "${1:-}" = "--prove-red" ]; then
  receipt_backup="${receipt_script}.assay-backup"
  mv "$receipt_script" "$receipt_backup"
  trap 'mv "$receipt_backup" "$receipt_script" 2>/dev/null; rm -rf "$fixture_root"' EXIT

  if CLAUDE_PROJECT_DIR="$receipt_project" "$receipt_script" fixture-agent ok "post-removal" >/dev/null 2>&1; then
    prove_red_report="FAIL  prove-red/agent-receipt - drill still passed with the gate removed, coupling is fake"
  else
    prove_red_report="PASS  prove-red/agent-receipt - drill correctly went red with agent-receipt.sh removed"
  fi

  mv "$receipt_backup" "$receipt_script"
  trap 'rm -rf "$fixture_root"' EXIT
  report+="$prove_red_report"$'\n'
fi

# ---------------------------------------------------------------------
printf '%s' "$report"

pass_rate=$(awk -v p="$drills_pass" -v t="$drills_total" 'BEGIN { if (t==0) print "n/a"; else printf "%.2f", p/t }')
echo "SCALAR: ${drills_pass}/${drills_total} (${pass_rate})"

if [ "$drills_pass" -eq "$drills_total" ]; then
  exit 0
fi
exit 1
