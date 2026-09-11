# fullscript-mcp

Local FastMCP server that wraps the Fullscript practitioner API.

## Scope

**Personal.** Fullscript is scoped to the personal context – supplement research, formulation references and protocol development for personal wellness work. It is not a Five Points, Martywood, Paradigm or Lillie and Lynette venture tool.

## Purpose

Fullscript is a practitioner-grade supplement dispensary. The MCP wraps the practitioner API so Alfred can search catalogue products, reference formulations and pull practitioner documentation when answering personal wellness questions or drafting supplement protocols for personal use.

## Environment Variables

The server reads from the personal section of `~/Alfred Pennyworth/.env`:

| Variable | Purpose |
|---|---|
| `FULLSCRIPT_CLIENT_ID` | OAuth app client identifier |
| `FULLSCRIPT_CLIENT_SECRET` | OAuth app client secret |
| `FULLSCRIPT_ENV` | `sandbox` or `production` |
| `FULLSCRIPT_BASE_URL` | API base URL (environment-specific) |

All four are personal credentials. Rotated 2026-04-22 via OAuth app delete-and-recreate during the credential rotation sweep.

## Running

```
cd "~/Alfred Pennyworth/Integrations/fullscript-mcp"
source ../../.env
python3 server.py
```

## MCP Registration

Connected via local server entry in `.mcp.json` (or an equivalent local runner). Because scope is personal, Fullscript is not referenced in any venture `Agents/integrations.md`.
