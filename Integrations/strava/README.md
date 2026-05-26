# Strava MCP

Thin FastMCP layer over the Strava v3 API with an optional bridge to the personal Notion Fitness Journal. Reads from Strava, writes Cardiovascular Workout entries into the Fitness Journal on demand.

Personal-scope integration. Tokens belong on `martavious.spicer@icloud.com`.

## Tools

| Tool | What it does |
|---|---|
| `strava_auth_status` | Confirms tokens are valid, returns the authorized athlete. |
| `strava_list_activities` | Lists activities in a date range with imperial-unit summaries. |
| `strava_get_activity` | Full detail for one activity including per-mile splits and HR zones. |
| `strava_sync_activity_to_notion` | Creates one Cardiovascular Workout page in the Fitness Journal. |
| `strava_sync_range_to_notion` | Batch sync a date range into the Fitness Journal. |

All distance values are converted to miles, elevation to feet, pace to minutes per mile.

## Setup

### 1. Create a Strava developer app

1. Visit https://www.strava.com/settings/api while signed in as the personal Strava account.
2. Create an app. Category does not matter. Important field: **Authorization Callback Domain** must be `localhost`.
3. Copy the Client ID and Client Secret.

### 2. Create a Notion internal integration (for sync tools)

Only needed if you want the sync tools to write to Notion. The Strava-only tools work without it.

1. Go to https://www.notion.so/my-integrations.
2. Create a new internal integration named "Alfred Strava Sync".
3. Copy the Internal Integration Secret.
4. Open the Fitness Journal database in Notion. Click the three-dot menu, Connections, and add the new integration. Without this step the integration cannot write to the database.

### 3. Install dependencies

From this directory:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 4. Run the bootstrap once

```bash
export STRAVA_CLIENT_ID=<your client id>
export STRAVA_CLIENT_SECRET=<your client secret>
.venv/bin/python bootstrap.py
```

A browser window opens. Approve the authorization. Tokens land at `~/.config/alfred/strava-tokens.json`. The MCP server handles refresh from here.

### 5. Register the MCP in Claude Code

Add the entry to `~/Alfred Pennyworth/.mcp.json`. Append, do not replace existing servers:

```json
"strava": {
  "type": "stdio",
  "command": "/Users/martyspicer/Alfred Pennyworth/Integrations/strava/.venv/bin/python",
  "args": ["/Users/martyspicer/Alfred Pennyworth/Integrations/strava/server.py"],
  "env": {
    "NOTION_PERSONAL_TOKEN": "${NOTION_PERSONAL_TOKEN}"
  }
}
```

Then set the `NOTION_PERSONAL_TOKEN` env var in your shell profile:

```bash
export NOTION_PERSONAL_TOKEN=<secret_...>
```

Restart Claude Code to pick up the new server.

## Usage

Once registered, the tools are available to Claude directly. Typical flows:

**Pull yesterday's run summary without writing anything**

```
Use strava_list_activities after "2026-04-22" before "2026-04-23"
```

**Sync last week of runs into Notion**

```
Use strava_sync_range_to_notion after "2026-04-16" before "2026-04-23" sport_types ["Run", "TrailRun"]
```

**Sync a specific activity**

```
Use strava_sync_activity_to_notion activity_id 12345678901
```

## Field mapping

Cardiovascular Workout template fields are populated from Strava as follows:

| Template field | Source |
|---|---|
| Discipline | `sport_type` (Run, Ride, Swim, etc.) |
| Environment | Derived from `trainer` and `type` flags |
| Total Distance | `distance` converted to miles |
| Total Time | `moving_time` as H:MM:SS |
| Average Pace | Derived from `average_speed`, min/mi |
| Average Heart Rate | `average_heartrate` in bpm |
| Max Heart Rate | `max_heartrate` in bpm |
| Calories | `calories` |
| Elevation Gain | `total_elevation_gain` converted to feet |
| Cadence | `average_cadence` |
| RPE | Blank (subjective, fill manually) |
| Splits | `splits_standard` per-mile breakdown |
| Heart Rate Zones | `/activities/{id}/zones` distribution buckets |
| Session Notes | `description` plus `gear.name` |

Difficulty is inferred from Strava's `suffer_score`: 100 and above is High Intensity, 40 to 99 is Medium Intensity, below 40 is Low Intensity.

## Troubleshooting

**`Strava tokens not found`** — run `bootstrap.py` first. Confirm `~/.config/alfred/strava-tokens.json` exists.

**`NOTION_PERSONAL_TOKEN is not set`** — sync tools need a personal Notion integration token. See setup step 2.

**`Strava rate limit exceeded`** — 100 requests per 15 minutes, 1000 per day. Wait and retry.

**Notion returns `object_not_found` on create** — the integration has not been added to the Fitness Journal database. Re-do step 2.4 (add Connection).

## Security

- Strava tokens live in `~/.config/alfred/strava-tokens.json`, permission 600.
- Notion token is passed via environment variable only.
- The `.gitignore` excludes `.env`, `.tokens.json`, and the virtual environment.
- Never commit the tokens file or the client secret.

## Scope

Strava OAuth requests: `read,activity:read_all,profile:read_all`. No write scopes against Strava. The only writes this MCP performs are to Notion, which the user has authorized by adding the integration to the Fitness Journal.
