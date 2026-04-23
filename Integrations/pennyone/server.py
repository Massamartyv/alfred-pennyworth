#!/usr/bin/env python3
"""
Pennyone MCP Server -- Content syndication router.

Thin layer over Zernio. Accepts a single publish request and fans out
to six social platforms (Instagram, TikTok, Threads, X, Reddit, Snap)
via Zernio's unified social media API. Adds venture-scoped branding
mode, per-platform overrides, and unified response aggregation.
"""

import os
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any

import httpx
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ZERNIO_API_KEY = os.getenv("ZERNIO_API_KEY", "")
ZERNIO_API_BASE = os.getenv("ZERNIO_API_BASE", "https://api.zernio.com/v1")

REQUEST_TIMEOUT_SECONDS = 30.0
HEALTH_TIMEOUT_SECONDS = 10.0

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Platform(str, Enum):
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    THREADS = "threads"
    X = "x"
    REDDIT = "reddit"
    SNAP = "snap"


class BrandingMode(str, Enum):
    MARTY_GRAS = "marty_gras"
    FIVE_POINTS = "five_points"
    PARADIGM = "paradigm"
    LILLIE_AND_LYNETTE = "lillie_and_lynette"


class MediaAsset(BaseModel):
    url: Optional[str] = None
    path: Optional[str] = None
    caption: Optional[str] = None


class ContentPayload(BaseModel):
    text: str
    media: List[MediaAsset] = Field(default_factory=list)
    links: List[str] = Field(default_factory=list)


class PublishRequest(BaseModel):
    content: ContentPayload
    platforms: List[Platform]
    schedule_at: Optional[datetime] = None
    branding: BrandingMode = BrandingMode.MARTY_GRAS
    overrides: Dict[Platform, ContentPayload] = Field(default_factory=dict)


class PlatformResult(BaseModel):
    platform: Platform
    status: str  # "success", "partial", "failure"
    post_id: Optional[str] = None
    url: Optional[str] = None
    error: Optional[str] = None


class PublishResponse(BaseModel):
    success: List[PlatformResult]
    partial: List[PlatformResult]
    failure: List[PlatformResult]
    branding: str
    dispatched_at: datetime


# ---------------------------------------------------------------------------
# Branding registry -- per-venture voice guides.
# Voice descriptions are populated as each venture's content pipeline ships.
# ---------------------------------------------------------------------------

BRANDING_REGISTRY: Dict[BrandingMode, Dict[str, str]] = {
    BrandingMode.MARTY_GRAS: {
        "voice": "architect of vibe",
        "description": "Warm, deliberate, culturally layered",
    },
    BrandingMode.FIVE_POINTS: {
        "voice": "pentagram partnership",
        "description": "Precise, editorial, quietly confident",
    },
    BrandingMode.PARADIGM: {
        "voice": "TBD",
        "description": "Voice to be documented as Paradigm content ships",
    },
    BrandingMode.LILLIE_AND_LYNETTE: {
        "voice": "TBD",
        "description": "Voice to be documented as Lillie and Lynette content ships",
    },
}


# ---------------------------------------------------------------------------
# Zernio adapter -- the single swap point once the API shape is confirmed.
# ---------------------------------------------------------------------------


async def _zernio_publish(
    content: ContentPayload,
    platform: Platform,
    schedule_at: Optional[datetime],
) -> PlatformResult:
    """
    Publish to a single platform via Zernio's unified API.

    The request shape below is the expected v1 pattern; once the account
    is provisioned and the SDK or docs are confirmed, adjust this one
    function. The rest of Pennyone is decoupled from the Zernio shape.
    """
    if not ZERNIO_API_KEY:
        return PlatformResult(
            platform=platform,
            status="failure",
            error="ZERNIO_API_KEY not set. Sign up at zernio.com and configure the key.",
        )

    payload: Dict[str, Any] = {
        "platform": platform.value,
        "text": content.text,
        "media": [m.model_dump(exclude_none=True) for m in content.media],
        "links": content.links,
    }
    if schedule_at is not None:
        payload["schedule_at"] = schedule_at.isoformat()

    try:
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS) as client:
            resp = await client.post(
                f"{ZERNIO_API_BASE}/posts",
                headers={"Authorization": f"Bearer {ZERNIO_API_KEY}"},
                json=payload,
            )
    except httpx.HTTPError as exc:
        return PlatformResult(
            platform=platform,
            status="failure",
            error=f"Zernio request failed: {exc}",
        )

    if resp.status_code >= 400:
        return PlatformResult(
            platform=platform,
            status="failure",
            error=f"Zernio {resp.status_code}: {resp.text[:200]}",
        )

    data = resp.json()
    return PlatformResult(
        platform=platform,
        status="success",
        post_id=data.get("id"),
        url=data.get("url"),
    )


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("pennyone")


@mcp.tool()
async def publish(request: PublishRequest) -> PublishResponse:
    """
    Fan out a single publish request to multiple platforms.

    Accepts a ContentPayload with text, media and links, a list of target
    platforms, optional scheduling timestamp and a branding mode. Each
    platform is dispatched through Zernio. Returns unified success,
    partial and failure lists.
    """
    results: List[PlatformResult] = []
    for platform in request.platforms:
        content = request.overrides.get(platform) or request.content
        result = await _zernio_publish(content, platform, request.schedule_at)
        results.append(result)

    return PublishResponse(
        success=[r for r in results if r.status == "success"],
        partial=[r for r in results if r.status == "partial"],
        failure=[r for r in results if r.status == "failure"],
        branding=request.branding.value,
        dispatched_at=datetime.now(timezone.utc),
    )


@mcp.tool()
async def list_platforms() -> List[str]:
    """List every platform Pennyone can publish to."""
    return [p.value for p in Platform]


@mcp.tool()
async def branding_registry() -> Dict[str, Dict[str, str]]:
    """Return the current branding mode registry."""
    return {mode.value: info for mode, info in BRANDING_REGISTRY.items()}


@mcp.tool()
async def health_check() -> Dict[str, Any]:
    """Verify that Pennyone can reach Zernio."""
    if not ZERNIO_API_KEY:
        return {"status": "no_key", "message": "ZERNIO_API_KEY not set"}

    try:
        async with httpx.AsyncClient(timeout=HEALTH_TIMEOUT_SECONDS) as client:
            resp = await client.get(
                f"{ZERNIO_API_BASE}/health",
                headers={"Authorization": f"Bearer {ZERNIO_API_KEY}"},
            )
        return {
            "status": "ok" if resp.status_code == 200 else "error",
            "zernio_status": resp.status_code,
        }
    except httpx.HTTPError as exc:
        return {"status": "error", "message": str(exc)}


if __name__ == "__main__":
    mcp.run(transport="stdio")
