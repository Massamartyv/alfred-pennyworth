#!/bin/bash
# Portable fixed-cost timeout wrapper.
#
# macOS ships no `timeout` binary and GNU coreutils cannot be assumed
# installed. The house scripts target bash 3.2 (the /bin/bash shebang
# resolves there, not the Homebrew 5.x on PATH), which rules out `wait -n`
# and other bash-4+ job-control conveniences. This polls instead of racing
# a background sleep against the command - a background sleep that outlives
# its own kill keeps the command-substitution pipe open in the caller and
# the whole run hangs until the sleep's own timer expires, which is exactly
# the failure this suite tripped during its own build. Polling has no
# orphan process to leak.
#
# Exits 124 on timeout, matching GNU timeout's convention.
#
# Usage: assay-timeout.sh <budget_seconds> <command> [args...]

set -u

budget="$1"; shift

"$@" &
cmd_pid=$!

elapsed=0
while kill -0 "$cmd_pid" 2>/dev/null; do
  if [ "$elapsed" -ge "$budget" ]; then
    kill -TERM "$cmd_pid" 2>/dev/null
    sleep 1
    kill -0 "$cmd_pid" 2>/dev/null && kill -KILL "$cmd_pid" 2>/dev/null
    wait "$cmd_pid" 2>/dev/null
    exit 124
  fi
  sleep 1
  elapsed=$((elapsed + 1))
done

wait "$cmd_pid"
exit $?
