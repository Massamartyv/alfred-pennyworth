#!/bin/bash
# The Assay - the measurement layer this estate did not have.
#
# FROZEN. This file is the harness. No agent, including the one that built
# it, edits this file during a run. Suites are the editable surface; this
# dispatcher is not. If a suite needs new behaviour, change the suite's own
# run.sh, not this file.
#
# One harness, three registered suites: gates, skills, notion. Each suite
# is surface-agnostic machinery wired to one editable target - the gate
# layer, the skill roster, a Notion payload fixture set. Every suite
# declares a fixed-cost budget (wall-clock seconds), reports exactly one
# scalar, and appends one line to the verdict ledger. A suite that exceeds
# its budget fails on time, not on content - that is what makes runs
# comparable across suites and across dates.
#
# Refusal is a valid outcome. A suite with no clean verifier for the thing
# it is asked to check reports "unscoreable" rather than inventing a number.
# Autonomy Tier 0: this harness proposes and measures. It never applies a
# change, never writes to Notion, never sends or publishes, never commits.
#
# Usage:
#   the-assay.sh                    run every registered suite
#   the-assay.sh <suite>             run one suite: gates | skills | notion
#   the-assay.sh --quiet [<suite>]   print only the scalar line and failures
#   the-assay.sh --list              list registered suites and their budgets
#
# Exit codes: 0 all run suites pass, 1 one or more suites fail or are
# unscoreable, 2 bad usage.

set -uo pipefail

export ASSAY_HOME
ASSAY_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_dir="${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}"
export ASSAY_PROJECT_DIR="$project_dir"

# shellcheck source=lib/ledger.sh
source "$ASSAY_HOME/lib/ledger.sh"

quiet=false
target=""
list_only=false

for arg in "$@"; do
  case "$arg" in
    --quiet) quiet=true ;;
    --list) list_only=true ;;
    gates|skills|notion) target="$arg" ;;
    *) echo "usage: the-assay.sh [--quiet] [--list] [gates|skills|notion]" >&2; exit 2 ;;
  esac
done

# Registry: suite_name:budget_seconds:runner_path
# This is the one place a new suite is wired in. Adding a suite means
# adding a row here and a suites/<name>/run.sh that honours the contract
# below - it does not mean editing the loop that calls it.
registry="gates:120:$ASSAY_HOME/suites/gates/run.sh
skills:1200:$ASSAY_HOME/suites/skills/run.sh
notion:60:$ASSAY_HOME/suites/notion/run.sh"

if [ "$list_only" = true ]; then
  echo "registered suites (name:budget_seconds):"
  echo "$registry" | while IFS=: read -r name budget _; do
    echo "  $name  budget ${budget}s"
  done
  exit 0
fi

overall_failures=0
run_count=0

run_suite() {  # name budget runner
  local name="$1" budget="$2" runner="$3"
  if [ ! -x "$runner" ]; then
    echo "FAIL  $name - runner not found or not executable: $runner"
    assay_ledger_append "$name" "n/a" "n/a" "$budget" "fail"
    overall_failures=$((overall_failures + 1))
    return
  fi

  local start end elapsed status scalar result_line
  start=$(date +%s)

  # Suite contract: the runner prints exactly one line beginning with
  # "SCALAR:" before it exits, and any number of ordinary report lines
  # around it. Exit 0 = pass, exit 1 = fail, exit 3 = unscoreable (refusal).
  # assay-timeout.sh enforces the fixed-cost budget regardless of what the
  # suite does internally - a suite that hangs fails on time, not content.
  local out
  out=$("$ASSAY_HOME/lib/assay-timeout.sh" "$budget" "$runner" 2>&1)
  status=$?
  end=$(date +%s)
  elapsed=$((end - start))

  if [ "$quiet" = false ]; then
    echo "$out"
  fi

  scalar=$(printf '%s\n' "$out" | grep '^SCALAR:' | tail -1 | sed 's/^SCALAR: *//')
  [ -z "$scalar" ] && scalar="n/a"

  case "$status" in
    0) result_line="pass" ;;
    3) result_line="unscoreable" ;;
    124) result_line="fail"; scalar="timeout"; echo "FAIL  $name - exceeded ${budget}s budget (timed out)" ;;
    *) result_line="fail" ;;
  esac

  assay_ledger_append "$name" "$scalar" "${elapsed}s" "${budget}s" "$result_line"
  run_count=$((run_count + 1))

  if [ "$result_line" != "pass" ]; then
    overall_failures=$((overall_failures + 1))
    [ "$quiet" = true ] && echo "FAIL  $name - scalar=$scalar result=$result_line (${elapsed}s of ${budget}s budget)"
  else
    [ "$quiet" = true ] && echo "ok    $name - scalar=$scalar (${elapsed}s of ${budget}s budget)"
  fi
}

echo "The Assay - running against $project_dir"

while IFS=: read -r name budget runner; do
  [ -z "$name" ] && continue
  if [ -n "$target" ] && [ "$name" != "$target" ]; then
    continue
  fi
  echo "--- suite: $name (budget ${budget}s) ---"
  run_suite "$name" "$budget" "$runner"
done <<< "$registry"

echo "--- verdict ledger: $(assay_ledger_path) ---"

if [ "$run_count" -eq 0 ]; then
  echo "no suite matched target '$target'" >&2
  exit 2
fi

if [ "$overall_failures" -gt 0 ]; then
  echo "ASSAY: $overall_failures of $run_count suite(s) did not pass"
  exit 1
fi

echo "ASSAY: all $run_count suite(s) pass"
exit 0
