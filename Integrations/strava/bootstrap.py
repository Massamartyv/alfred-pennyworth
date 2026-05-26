#!/usr/bin/env python3
"""
Strava OAuth bootstrap.

One-time setup to authorize the personal Strava developer app and save
an initial access + refresh token pair. After this runs successfully the
MCP server handles all token refresh internally.

Prerequisites:
  1. Create a personal app at https://www.strava.com/settings/api
     - Category: anything (Web Application is fine)
     - Authorization Callback Domain: localhost
  2. Export the client ID and client secret before running:
       export STRAVA_CLIENT_ID=12345
       export STRAVA_CLIENT_SECRET=abc123...
  3. Run: python bootstrap.py
  4. Browser opens Strava authorization page. Approve.
  5. Tokens land at ~/.config/alfred/strava-tokens.json.
"""

from __future__ import annotations

import http.server
import json
import os
import secrets
import socketserver
import sys
import urllib.parse
import webbrowser
from pathlib import Path

import httpx

STRAVA_AUTHORIZE_URL = "https://www.strava.com/oauth/authorize"
STRAVA_TOKEN_URL = "https://www.strava.com/oauth/token"
REDIRECT_PORT = 8765
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/callback"
SCOPE = "read,activity:read_all,profile:read_all"

TOKEN_PATH = Path.home() / ".config" / "alfred" / "strava-tokens.json"


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    """Single-shot handler that captures the authorization code."""

    received_code: str | None = None
    received_state: str | None = None
    received_error: str | None = None

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        CallbackHandler.received_code = params.get("code", [None])[0]
        CallbackHandler.received_state = params.get("state", [None])[0]
        CallbackHandler.received_error = params.get("error", [None])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        if CallbackHandler.received_error:
            body = (
                "<h2>Authorization failed</h2>"
                f"<p>{CallbackHandler.received_error}</p>"
                "<p>You can close this window.</p>"
            )
        else:
            body = (
                "<h2>Strava authorization successful</h2>"
                "<p>You can close this window and return to the terminal.</p>"
            )
        self.wfile.write(body.encode("utf-8"))

    def log_message(self, format: str, *args) -> None:  # noqa: A002
        return


def wait_for_callback(state: str) -> str:
    with socketserver.TCPServer(("", REDIRECT_PORT), CallbackHandler) as httpd:
        httpd.timeout = 300
        httpd.handle_request()

    if CallbackHandler.received_error:
        raise SystemExit(f"Strava returned error: {CallbackHandler.received_error}")
    if CallbackHandler.received_state != state:
        raise SystemExit("State mismatch -- possible CSRF, aborting.")
    if not CallbackHandler.received_code:
        raise SystemExit("No authorization code received.")
    return CallbackHandler.received_code


def exchange_code(client_id: str, client_secret: str, code: str) -> dict:
    response = httpx.post(
        STRAVA_TOKEN_URL,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def save_tokens(payload: dict, client_id: str, client_secret: str) -> Path:
    TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "access_token": payload["access_token"],
        "refresh_token": payload["refresh_token"],
        "expires_at": payload["expires_at"],
        "athlete_id": payload.get("athlete", {}).get("id"),
        "athlete_username": payload.get("athlete", {}).get("username"),
    }
    TOKEN_PATH.write_text(json.dumps(data, indent=2))
    TOKEN_PATH.chmod(0o600)
    return TOKEN_PATH


def main() -> None:
    client_id = os.environ.get("STRAVA_CLIENT_ID")
    client_secret = os.environ.get("STRAVA_CLIENT_SECRET")

    if not client_id or not client_secret:
        print(
            "Missing STRAVA_CLIENT_ID or STRAVA_CLIENT_SECRET.\n"
            "Set them in the shell before running this script. See README.md.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    state = secrets.token_urlsafe(16)
    authorize_params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "approval_prompt": "auto",
        "scope": SCOPE,
        "state": state,
    }
    authorize_url = f"{STRAVA_AUTHORIZE_URL}?{urllib.parse.urlencode(authorize_params)}"

    print("Opening Strava authorization in your browser...")
    print(f"If the browser does not open, visit:\n  {authorize_url}\n")
    webbrowser.open(authorize_url)

    print(f"Waiting for redirect on {REDIRECT_URI} ...")
    code = wait_for_callback(state)

    print("Exchanging authorization code for access and refresh tokens...")
    payload = exchange_code(client_id, client_secret, code)

    token_path = save_tokens(payload, client_id, client_secret)
    athlete = payload.get("athlete", {})
    print(
        f"Tokens saved to {token_path}\n"
        f"Authorized athlete: {athlete.get('firstname', '')} {athlete.get('lastname', '')} "
        f"(id={athlete.get('id')})"
    )


if __name__ == "__main__":
    main()
