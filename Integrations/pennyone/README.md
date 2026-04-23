# Pennyone

Content syndication router. Thin MCP layer over Zernio. Fans out a single publish request to Instagram, TikTok, Threads, X, Reddit and Snap.

Pennyone does not write the content. It does not decide when to publish. It takes an existing publish request and executes the fan-out.

## Architecture

Pennyone is a thin FastMCP server that wraps Zernio, a unified social media API covering 14+ platforms. Pennyone uses six of them.

```
Alfred --> Pennyone (FastMCP) --> Zernio API --> 6 platforms
```

Pennyone adds:

- Venture-scoped branding mode (marty_gras, five_points, paradigm, lillie_and_lynette)
- Per-platform content overrides
- Unified success, partial and failure response lists
- Notion Content pipeline hooks (future)

## Status

Scaffold complete. Zernio integration isolated in `_zernio_publish()`. Requires `ZERNIO_API_KEY` to go live.

## Setup

### 1. Zernio account

Sign up at [zernio.com](https://zernio.com). Generate an API key. Connect Instagram, TikTok, Threads, X, Reddit and Snap through Zernio's dashboard with the Marty Gras accounts.

### 2. Environment variable

Add to `~/Alfred Pennyworth/.env`:

```
ZERNIO_API_KEY=your_key_here
```

### 3. Install dependencies

```bash
cd ~/Alfred\ Pennyworth/Integrations/pennyone
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Register with MCP

Once the key is set, add to `.mcp.json`:

```json
"pennyone": {
  "type": "stdio",
  "command": "/Users/martyspicer/Alfred Pennyworth/Integrations/pennyone/.venv/bin/python",
  "args": ["/Users/martyspicer/Alfred Pennyworth/Integrations/pennyone/server.py"],
  "env": {
    "ZERNIO_API_KEY": "${ZERNIO_API_KEY}"
  }
}
```

### 5. Verify

Restart the MCP-hosting client and call `health_check` to confirm Zernio connectivity.

## Tools

| Tool | Purpose |
|---|---|
| `publish` | Fan out a publish request to multiple platforms |
| `list_platforms` | Return every platform Pennyone can publish to |
| `branding_registry` | Return the current branding mode registry |
| `health_check` | Verify Zernio connectivity |

## Platform coverage

All six platforms route through Zernio.

| Platform | Via |
|---|---|
| Instagram | Zernio |
| TikTok | Zernio |
| Threads | Zernio |
| X | Zernio |
| Reddit | Zernio |
| Snap | Zernio |

## Adapter swap point

The Zernio REST call lives in one function, `_zernio_publish()` in `server.py`. The current shape assumes `POST /v1/posts` with a `platform` field and `Authorization: Bearer` header. Confirm against Zernio's actual API once the account exists, then adjust that single function. No other part of Pennyone depends on the Zernio shape.

## References

- Zernio docs: https://docs.zernio.com
- Zernio Python SDK: https://pypi.org/project/zernio-sdk/
- Pennyone agent definition: `Agents/Orchestration/pennyone.md`
- Marty Gras integrations: `Context/Spheres/System/Entrepreneurship/Marty Gras/Agents/integrations.md`

---

*Last updated: 2026-04-23*
