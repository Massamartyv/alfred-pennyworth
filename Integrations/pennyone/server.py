#!/usr/bin/env python3
"""
Pennyone MCP Server -- Content syndication router.

Thin FastMCP layer over Zernio. Accepts a publish request scoped to
a pipeline (personal, marty_gras, five_points, paradigm, lillie_and_lynette)
and fans it out to any subset of six social platforms (Instagram, TikTok,
Threads, X, Reddit, Snap).

Each pipeline owns its own Zernio account and its own API key, so
personal content cannot accidentally publish on venture accounts and
venture content cannot cross into another venture. The pipeline field
is the routing key.
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

ZERNIO_API_BASE = os.getenv("ZERNIO_API_BASE", "https://api.zernio.com/v1")

REQUEST_TIMEOUT_SECONDS = 30.0
HEALTH_TIMEOUT_SECONDS = 10.0


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class Platform(str, Enum):
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    THREADS = "threads"
    X = "x"
    REDDIT = "reddit"
    SNAP = "snap"


class Pipeline(str, Enum):
    """
    Routing key for a publish request. Each pipeline is isolated -- it has
    its own Zernio account, its own connected social accounts and its own
    API key. Personal and venture pipelines never share credentials.
    """

    PERSONAL = "personal"
    MARTY_GRAS = "marty_gras"
    FIVE_POINTS = "five_points"
    PARADIGM = "paradigm"
    LILLIE_AND_LYNETTE = "lillie_and_lynette"


# ---------------------------------------------------------------------------
# Pipeline registry -- one row per pipeline.
# `env_var` names the environment variable that holds that pipeline's
# Zernio API key. `voice` is populated as each venture's content pipeline
# ships and a voice guide exists; TBD until then.
# ---------------------------------------------------------------------------

PIPELINE_REGISTRY: Dict[Pipeline, Dict[str, str]] = {
    Pipeline.PERSONAL: {
        "label": "Personal",
        "voice": "direct first-person",
        "description": "Marty as an individual, separate from any venture",
        "env_var": "ZERNIO_PERSONAL_API_KEY",
    },
    Pipeline.MARTY_GRAS: {
        "label": "Marty Gras",
        "voice": "architect of vibe",
        "description": "Personal media venture -- podcast, newsletter, cultural curation",
        "env_var": "ZERNIO_MARTYGRAS_API_KEY",
    },
    Pipeline.FIVE_POINTS: {
        "label": "Five Points Digital Studio",
        "voice": "pentagram partnership",
        "description": "Premium digital marketing agency",
        "env_var": "ZERNIO_FIVEPOINTS_API_KEY",
    },
    Pipeline.PARADIGM: {
        "label": "Paradigm",
        "voice": "TBD",
        "description": "Pipeline not yet provisioned",
        "env_var": "ZERNIO_PARADIGM_API_KEY",
    },
    Pipeline.LILLIE_AND_LYNETTE: {
        "label": "Lillie and Lynette",
        "voice": "TBD",
        "description": "Pipeline not yet provisioned",
        "env_var": "ZERNIO_LILLIEANDLYNETTE_API_KEY",
    },
}


def _get_pipeline_key(pipeline: Pipeline) -> Optional[str]:
    """Return the configured API key for a pipeline, or None if unset."""
    env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
    value = os.getenv(env_var)
    return value or None


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


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
    pipeline: Pipeline
    schedule_at: Optional[datetime] = None
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
    pipeline: str
    dispatched_at: datetime


# ---------------------------------------------------------------------------
# Zernio adapter -- the single swap point once the API shape is confirmed.
# ---------------------------------------------------------------------------


async def _zernio_publish(
    api_key: str,
    content: ContentPayload,
    platform: Platform,
    schedule_at: Optional[datetime],
) -> PlatformResult:
    """
    Publish to a single platform via Zernio's unified API using the
    supplied pipeline-scoped API key.

    The request shape below is the expected v1 pattern; once the account
    is provisioned and the SDK or docs are confirmed, adjust this one
    function. The rest of Pennyone is decoupled from the Zernio shape.
    """
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
                headers={"Authorization": f"Bearer {api_key}"},
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
    Fan out a publish request to the selected platforms under the pipeline's
    Zernio account.

    The pipeline field is mandatory. If the pipeline's API key is not set,
    every platform call fails with a clear "pipeline not provisioned"
    error -- no Zernio call is made. Overrides let you swap the content
    payload per platform while keeping a single dispatch.
    """
    api_key = _get_pipeline_key(request.pipeline)
    now = datetime.now(timezone.utc)

    if not api_key:
        env_var = PIPELINE_REGISTRY[request.pipeline]["env_var"]
        failures = [
            PlatformResult(
                platform=platform,
                status="failure",
                error=f"Pipeline '{request.pipeline.value}' not provisioned. Set {env_var}.",
            )
            for platform in request.platforms
        ]
        return PublishResponse(
            success=[],
            partial=[],
            failure=failures,
            pipeline=request.pipeline.value,
            dispatched_at=now,
        )

    results: List[PlatformResult] = []
    for platform in request.platforms:
        content = request.overrides.get(platform) or request.content
        result = await _zernio_publish(api_key, content, platform, request.schedule_at)
        results.append(result)

    return PublishResponse(
        success=[r for r in results if r.status == "success"],
        partial=[r for r in results if r.status == "partial"],
        failure=[r for r in results if r.status == "failure"],
        pipeline=request.pipeline.value,
        dispatched_at=now,
    )


@mcp.tool()
async def list_platforms() -> List[str]:
    """List every platform Pennyone can publish to."""
    return [p.value for p in Platform]


@mcp.tool()
async def list_pipelines() -> List[Dict[str, str]]:
    """
    Return the full pipeline registry -- one entry per pipeline with its
    label, voice hint, description and the env var that holds its key.
    """
    return [
        {"pipeline": pipeline.value, **info}
        for pipeline, info in PIPELINE_REGISTRY.items()
    ]


@mcp.tool()
async def pipeline_status() -> Dict[str, Dict[str, Any]]:
    """
    For each pipeline, report whether its Zernio API key is set. Does not
    make network calls. Use health_check for reachability tests.
    """
    status: Dict[str, Dict[str, Any]] = {}
    for pipeline in Pipeline:
        info = PIPELINE_REGISTRY[pipeline]
        key = _get_pipeline_key(pipeline)
        status[pipeline.value] = {
            "provisioned": key is not None,
            "env_var": info["env_var"],
            "label": info["label"],
        }
    return status


@mcp.tool()
async def health_check(pipeline: Optional[Pipeline] = None) -> Dict[str, Any]:
    """
    Verify Zernio reachability. If a pipeline is given, check just that
    one. Otherwise check every provisioned pipeline.
    """
    pipelines_to_check = [pipeline] if pipeline else list(Pipeline)
    results: Dict[str, Any] = {}

    for p in pipelines_to_check:
        key = _get_pipeline_key(p)
        if not key:
            results[p.value] = {"status": "no_key"}
            continue

        try:
            async with httpx.AsyncClient(timeout=HEALTH_TIMEOUT_SECONDS) as client:
                resp = await client.get(
                    f"{ZERNIO_API_BASE}/health",
                    headers={"Authorization": f"Bearer {key}"},
                )
            results[p.value] = {
                "status": "ok" if resp.status_code == 200 else "error",
                "zernio_status": resp.status_code,
            }
        except httpx.HTTPError as exc:
            results[p.value] = {"status": "error", "message": str(exc)}

    return results


if __name__ == "__main__":
    mcp.run(transport="stdio")
