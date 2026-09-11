#!/usr/bin/env bash
#
# The Almanac -- wrapper that sources the repo dotenv and runs the
# renderer on the apple-calendar venv, which already carries the
# bridge's dependencies. Dry run unless --execute is passed through.
#
# Usage:
#   ./almanac.sh check
#   ./almanac.sh render --from-now
#   ./almanac.sh render --week next --execute

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
PYTHON="$ROOT/Integrations/apple-calendar/.venv/bin/python"

if [[ ! -x "$PYTHON" ]]; then
  echo "apple-calendar venv missing at $PYTHON" >&2
  echo "Build it: cd '$ROOT/Integrations/apple-calendar' && python3.12 -m venv .venv && .venv/bin/pip install -r requirements.txt" >&2
  exit 1
fi

if [[ -f "$ROOT/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$ROOT/.env"
  set +a
fi

exec "$PYTHON" "$HERE/almanac.py" "$@"
