#!/bin/bash
# Alfred voice mode - Stop hook gate.
#
# Fires when the assistant finishes a response. Checks the voice flag first and
# exits immediately when voice is off, so silent turns never pay the cost of
# starting Python. When voice is on, the hook payload is piped to speak.py,
# which reads the response aloud.

FLAG="$CLAUDE_PROJECT_DIR/.working/voice/enabled"
[ -f "$FLAG" ] || exit 0

cat | /usr/bin/python3 "$CLAUDE_PROJECT_DIR/Automations/Voice/speak.py"
exit 0
