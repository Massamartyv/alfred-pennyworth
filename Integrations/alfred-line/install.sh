#!/bin/bash
# Install the Alfred line into a login session.
#
# Run once in each session:
#   ./install.sh --operator    from the operator account, installs the wake agent
#   ./install.sh --alfred      from the alfred account, installs the two daemons
#
# The Alfred session cannot read the operator home directory, so the daemons it
# needs are staged in /Users/Shared/alfred-line/bin.

set -euo pipefail

SPOOL="/Users/Shared/alfred-line"
BIN="$SPOOL/bin"
LOGS="$SPOOL/logs"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS="$HOME/Library/LaunchAgents"

usage() {
	echo "usage: $0 --operator | --alfred | --stage" >&2
	exit 1
}

stage() {
	mkdir -p "$SPOOL"/{outbox,sent,failed,inbox,handled} "$BIN" "$LOGS"
	chmod 777 "$SPOOL"/{outbox,sent,failed,inbox,handled} "$LOGS"
	chmod 755 "$SPOOL" "$BIN"
	cp "$SRC/config.py" "$SRC/send_daemon.py" "$SRC/receive_daemon.py" "$BIN/"
	chmod 755 "$BIN"/*.py
	echo "staged daemons in $BIN"
}

install_alfred() {
	mkdir -p "$AGENTS"
	for label in send receive; do
		cp "$SRC/launchagents/com.alfredpennyworth.line.$label.plist" "$AGENTS/"
		launchctl bootout "gui/$(id -u)/com.alfredpennyworth.line.$label" 2>/dev/null || true
		launchctl bootstrap "gui/$(id -u)" "$AGENTS/com.alfredpennyworth.line.$label.plist"
		echo "loaded com.alfredpennyworth.line.$label"
	done
	echo
	echo "Next: send one test message so macOS raises the Automation prompt for"
	echo "Messages.app, and grant Full Disk Access to /usr/bin/python3 in this"
	echo "session so the receive daemon can read chat.db."
}

install_operator() {
	mkdir -p "$AGENTS"
	local plist="$AGENTS/com.alfredpennyworth.line.wake.plist"
	sed -e "s|WAKE_SCRIPT_PATH|$SRC/wake.py|" \
	    -e "s|WORKING_DIR|$SRC|" \
	    "$SRC/launchagents/com.alfredpennyworth.line.wake.plist" > "$plist"
	launchctl bootout "gui/$(id -u)/com.alfredpennyworth.line.wake" 2>/dev/null || true
	launchctl bootstrap "gui/$(id -u)" "$plist"
	echo "loaded com.alfredpennyworth.line.wake"
}

[ $# -eq 1 ] || usage

case "$1" in
	--stage) stage ;;
	--alfred) stage; install_alfred ;;
	--operator) stage; install_operator ;;
	*) usage ;;
esac
