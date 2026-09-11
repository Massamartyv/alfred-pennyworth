# Shared ledger helper for The Assay.
#
# Sourced by the-assay.sh, never executed directly. Appends one line per
# suite run to the verdict ledger. The ledger is machine-derived state that
# lives under the harness home by explicit carve-out in the operation brief
# ("the verdict ledger lives under the harness home and is machine-derived,
# not hand-authored state") - it is not a Status/Stage/Pending block in a
# tracked markdown file, and it is never hand-edited.
#
# Format: tab-separated, one run per line.
#   timestamp_utc  suite  scalar  budget_used  budget_declared  result
#
# result is one of: pass, fail, unscoreable

assay_ledger_path() {
  echo "$ASSAY_HOME/ledger/verdicts.tsv"
}

assay_ledger_append() {  # suite scalar budget_used budget_declared result
  local suite="$1" scalar="$2" budget_used="$3" budget_declared="$4" result="$5"
  local ledger; ledger=$(assay_ledger_path)
  local stamp; stamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  mkdir -p "$(dirname "$ledger")"
  if [ ! -f "$ledger" ]; then
    printf 'timestamp_utc\tsuite\tscalar\tbudget_used\tbudget_declared\tresult\n' > "$ledger"
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$stamp" "$suite" "$scalar" "$budget_used" "$budget_declared" "$result" >> "$ledger"
}
