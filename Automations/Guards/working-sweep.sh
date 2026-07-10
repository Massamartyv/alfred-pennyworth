#!/bin/bash
# Sweep .working/ subdirectories untouched for 30 days.
# Dry-run by default: prints one disposition per directory. --execute moves
# eligible directories to Context/Archive/working-YYYY-MM/ (never deletes).
# Exemptions: session-buffer/ is always held; a directory whose handoff.md
# frontmatter status is partial or blocked is held until the mission closes.

set -euo pipefail

project_dir="${CLAUDE_PROJECT_DIR:-$HOME/Alfred Pennyworth}"
working="$project_dir/.working"
month=$(date +%Y-%m)
archive="$project_dir/Context/Archive/working-$month"
cutoff=$(( $(date +%s) - 30*86400 ))
mode="dry-run"
[ "${1:-}" = "--execute" ] && mode="execute"

[ -d "$working" ] || { echo "no .working directory"; exit 0; }

echo "working-sweep ($mode) - 30-day rule"

for dir in "$working"/*/; do
  [ -d "$dir" ] || continue
  name=$(basename "$dir")

  if [ "$name" = "session-buffer" ]; then
    echo "HELD     $name (offline buffer, always held)"
    continue
  fi

  newest=$(find "$dir" -type f -exec stat -f %m {} + 2>/dev/null | sort -rn | head -n 1)
  newest=${newest:-0}
  if [ "$newest" -ge "$cutoff" ]; then
    echo "ACTIVE   $name (touched within 30 days)"
    continue
  fi

  handoff="${dir}handoff.md"
  if [ -f "$handoff" ] && head -n 12 "$handoff" | grep -Eqi '^status:[[:space:]]*(partial|blocked)'; then
    echo "HELD     $name (open mission handoff)"
    continue
  fi

  if [ "$mode" = "execute" ]; then
    mkdir -p "$archive"
    mv "$dir" "$archive/"
    echo "MOVED    $name -> Context/Archive/working-$month/"
  else
    echo "ELIGIBLE $name (would move to archive)"
  fi
done

find "$working" -maxdepth 1 -type f -mtime +30 -print 2>/dev/null | while read -r f; do
  echo "LOOSE    $(basename "$f") (over 30 days, manual disposition)"
done

echo "done"
