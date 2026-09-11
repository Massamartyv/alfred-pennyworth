#!/bin/bash
# The Assay - suite three: Notion writes. Fixture-backed payload validation.
#
# Deterministic, no model call, no live workspace touched. Every fixture is
# a captured payload - the shape a create-page/patch-page call would carry
# - not a real API call. A live-workspace adapter is explicitly out of
# scope for this pass. Thin wrapper matching the other suites' entry point;
# validate_payload.py does the checking.

set -uo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$here/validate_payload.py" "$here"/fixtures/*.json
