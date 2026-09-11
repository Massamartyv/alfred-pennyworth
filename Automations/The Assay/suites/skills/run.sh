#!/bin/bash
# The Assay - suite two: skills. Trigger accuracy against the unified schema.
#
# Thin wrapper. The heavy lifting - JSON parsing, parallel judge dispatch,
# per-skill aggregation - is runner.py; this file exists so every suite
# under The Assay presents the same run.sh entry point to the harness
# regardless of implementation language, matching the suite contract in
# the-assay.sh (print report lines, one SCALAR: line, exit 0/1/3).
#
# Usage: run.sh [skill-name]   - optionally scope to one registered skill

set -uo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$here/runner.py" "$@"
