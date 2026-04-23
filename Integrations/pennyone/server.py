#!/usr/bin/env python3
"""
Pennyone MCP Server -- Content syndication router.

Thin FastMCP layer over Zernio. Accepts a publish request scoped to a
pipeline (personal, marty_gras, five_points, paradigm, lillie_and_lynette)
and fans it out to any subset of six social platforms (Instagram, TikTok,
Threads, X, Reddit, Snap).

Each pipeline owns its own Zernio account and its own API key, so
personal content cannot publish on venture accounts and venture content
cannot cross into another venture. The pipeline field is the routing key.

Zernio handles platform fan-out internally: a single POST /posts call
takes an array of {platform, accountId} pairs and publishes to each.
Pennyone resolves accountIds by listing the pipeline's connected
accounts and picking the first active account per requested platform.
"""

import mimetypes
import os
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any, Literal

import httpx
import zernio
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ZERNIO_API_BASE = os.getenv("ZERNIO_API_BASE", "https://zernio.com/api/v1")

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


# Zernio uses "twitter" for X and "snapchat" for Snap.
PLATFORM_TO_ZERNIO: Dict[Platform, str] = {
    Platform.INSTAGRAM: "instagram",
    Platform.TIKTOK: "tiktok",
    Platform.THREADS: "threads",
    Platform.X: "twitter",
    Platform.REDDIT: "reddit",
    Platform.SNAP: "snapchat",
}

ZERNIO_TO_PLATFORM: Dict[str, Platform] = {v: k for k, v in PLATFORM_TO_ZERNIO.items()}


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
# Pipeline registry
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
    env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
    value = os.getenv(env_var)
    return value or None


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class MediaAsset(BaseModel):
    """
    A single media attachment. Either `url` (public, pulled by Zernio) or
    `path` (local file, uploaded first via the Zernio SDK) must be set.

    `thumbnail_*` fields apply to video. `thumbnail_url` or `thumbnail_path`
    set Facebook's custom cover (and Facebook Reels). `instagram_thumbnail_url`
    or `instagram_thumbnail_path` set Instagram Reels' cover.
    """

    url: Optional[str] = None
    path: Optional[str] = None
    kind: Literal["image", "video", "gif", "document"] = "image"
    title: Optional[str] = None
    thumbnail_url: Optional[str] = None
    thumbnail_path: Optional[str] = None
    instagram_thumbnail_url: Optional[str] = None
    instagram_thumbnail_path: Optional[str] = None


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
    account_ids: Dict[Platform, str] = Field(
        default_factory=dict,
        description="Optional. If omitted, Pennyone resolves the first active account per platform.",
    )


class PlatformResult(BaseModel):
    platform: Platform
    status: str  # "success", "partial", "failure"
    post_id: Optional[str] = None
    url: Optional[str] = None
    error: Optional[str] = None
    account_id: Optional[str] = None


class PublishResponse(BaseModel):
    success: List[PlatformResult]
    partial: List[PlatformResult]
    failure: List[PlatformResult]
    pipeline: str
    dispatched_at: datetime


# ---------------------------------------------------------------------------
# Zernio adapter -- the single swap point for Zernio API shape.
# ---------------------------------------------------------------------------


async def _zernio_list_accounts(api_key: str) -> List[Dict[str, Any]]:
    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS) as client:
        resp = await client.get(
            f"{ZERNIO_API_BASE}/accounts",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        resp.raise_for_status()
        return resp.json().get("accounts", [])


async def _upload_path(client: Any, path_str: str) -> str:
    path = Path(path_str).expanduser()
    data = path.read_bytes()
    mime_type, _ = mimetypes.guess_type(path.name)
    resp = await client.media.aupload_bytes(
        data,
        filename=path.name,
        mime_type=mime_type or "application/octet-stream",
    )
    if not resp.files:
        raise RuntimeError(f"Zernio returned no files for upload of {path}")
    return str(resp.files[0].url)


async def _zernio_upload_media(api_key: str, media: List[MediaAsset]) -> List[Dict[str, Any]]:
    """
    Resolve every MediaAsset into a Zernio mediaItems[] entry. Uploads any
    local paths (primary or thumbnail) via the Zernio SDK and passes URLs
    through unchanged. Returns one dict per input asset, preserving order.

    Each returned dict has at minimum {type, url}. Optional keys: title,
    thumbnail, instagramThumbnail -- emitted only when the corresponding
    MediaAsset fields are set.
    """
    if not media:
        return []

    items: List[Dict[str, Any]] = []
    async with zernio.Zernio(api_key=api_key) as client:
        for m in media:
            if m.url:
                primary = m.url
            elif m.path:
                primary = await _upload_path(client, m.path)
            else:
                continue

            item: Dict[str, Any] = {"type": m.kind, "url": primary}
            if m.title:
                item["title"] = m.title

            if m.thumbnail_url:
                item["thumbnail"] = m.thumbnail_url
            elif m.thumbnail_path:
                item["thumbnail"] = await _upload_path(client, m.thumbnail_path)

            if m.instagram_thumbnail_url:
                item["instagramThumbnail"] = m.instagram_thumbnail_url
            elif m.instagram_thumbnail_path:
                item["instagramThumbnail"] = await _upload_path(client, m.instagram_thumbnail_path)

            items.append(item)

    return items


async def _zernio_publish_batch(
    api_key: str,
    content_text: str,
    platform_accounts: Dict[Platform, str],
    schedule_at: Optional[datetime],
    media_items: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "content": content_text,
        "platforms": [
            {"platform": PLATFORM_TO_ZERNIO[p], "accountId": acc_id}
            for p, acc_id in platform_accounts.items()
        ],
    }
    if media_items:
        body["mediaItems"] = media_items
    if schedule_at is not None:
        body["scheduledFor"] = schedule_at.isoformat()
    else:
        body["publishNow"] = True

    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS) as client:
        resp = await client.post(
            f"{ZERNIO_API_BASE}/posts",
            headers={"Authorization": f"Bearer {api_key}"},
            json=body,
        )

    return {
        "status_code": resp.status_code,
        "body": resp.json() if resp.headers.get("content-type", "").startswith("application/json") else resp.text,
    }


def _flatten_content(content: ContentPayload) -> str:
    """
    Reduce a ContentPayload to a single string for Zernio's `content` field.
    Text comes first; links are appended with newline separation. Media
    assets are not yet uploaded -- the caller should attach URLs to media
    and link them, or use the override mechanism when we wire media upload.
    """
    parts = [content.text.rstrip()] if content.text else []
    for link in content.links:
        parts.append(link)
    return "\n\n".join(p for p in parts if p)


# ---------------------------------------------------------------------------
# Core publish logic -- the actual work. Importable from the publisher module
# and from any other in-process caller. The MCP tool below wraps it.
# ---------------------------------------------------------------------------


async def _publish_core(request: PublishRequest) -> PublishResponse:
    """
    Fan out a publish request to the selected platforms under the pipeline's
    Zernio account.

    Zernio handles the platform fan-out in a single API call. Pennyone
    resolves the accountId for each requested platform from the pipeline's
    connected accounts (first active account per platform) unless the
    caller supplies account_ids explicitly.

    A platform with no active account in the pipeline's Zernio account
    fails with "no account connected" and is excluded from the batch call.
    If every platform is unmapped, no Zernio call is made.
    """
    now = datetime.now(timezone.utc)
    api_key = _get_pipeline_key(request.pipeline)

    if not api_key:
        env_var = PIPELINE_REGISTRY[request.pipeline]["env_var"]
        return PublishResponse(
            success=[],
            partial=[],
            failure=[
                PlatformResult(
                    platform=platform,
                    status="failure",
                    error=f"Pipeline '{request.pipeline.value}' not provisioned. Set {env_var}.",
                )
                for platform in request.platforms
            ],
            pipeline=request.pipeline.value,
            dispatched_at=now,
        )

    # Resolve accountId for every requested platform.
    resolved: Dict[Platform, Optional[str]] = {p: request.account_ids.get(p) for p in request.platforms}
    if any(v is None for v in resolved.values()):
        accounts = await _zernio_list_accounts(api_key)
        by_platform: Dict[str, List[Dict[str, Any]]] = {}
        for acc in accounts:
            if acc.get("isActive") and acc.get("platformStatus") == "active":
                by_platform.setdefault(acc.get("platform", ""), []).append(acc)
        for platform, acc_id in list(resolved.items()):
            if acc_id is None:
                zernio_name = PLATFORM_TO_ZERNIO[platform]
                candidates = by_platform.get(zernio_name, [])
                resolved[platform] = candidates[0]["_id"] if candidates else None

    # Split dispatchable vs unmapped platforms.
    dispatchable: Dict[Platform, str] = {
        p: acc_id for p, acc_id in resolved.items() if acc_id is not None
    }
    unmapped_failures = [
        PlatformResult(
            platform=p,
            status="failure",
            error=f"No active {PLATFORM_TO_ZERNIO[p]} account connected to the {request.pipeline.value} pipeline.",
        )
        for p, acc_id in resolved.items()
        if acc_id is None
    ]

    if not dispatchable:
        return PublishResponse(
            success=[],
            partial=[],
            failure=unmapped_failures,
            pipeline=request.pipeline.value,
            dispatched_at=now,
        )

    # Zernio takes a single content string per request. Per-platform
    # overrides would require separate calls; loop for the overridden set.
    override_platforms = {p for p in dispatchable if p in request.overrides}
    batch_platforms = {p: acc for p, acc in dispatchable.items() if p not in override_platforms}

    results: List[PlatformResult] = []

    async def _submit(content: ContentPayload, plats: Dict[Platform, str]) -> List[PlatformResult]:
        content_text = _flatten_content(content)
        try:
            media_items = await _zernio_upload_media(api_key, content.media)
        except Exception as exc:
            return [
                PlatformResult(
                    platform=p,
                    status="failure",
                    error=f"Media upload failed: {exc}",
                    account_id=acc_id,
                )
                for p, acc_id in plats.items()
            ]
        try:
            outcome = await _zernio_publish_batch(
                api_key, content_text, plats, request.schedule_at, media_items=media_items
            )
        except httpx.HTTPError as exc:
            return [
                PlatformResult(
                    platform=p,
                    status="failure",
                    error=f"Zernio request failed: {exc}",
                    account_id=acc_id,
                )
                for p, acc_id in plats.items()
            ]

        if outcome["status_code"] >= 400:
            err = str(outcome["body"])[:300]
            return [
                PlatformResult(
                    platform=p,
                    status="failure",
                    error=f"Zernio {outcome['status_code']}: {err}",
                    account_id=acc_id,
                )
                for p, acc_id in plats.items()
            ]

        post_id = None
        if isinstance(outcome["body"], dict):
            post_id = outcome["body"].get("post", {}).get("_id")
        return [
            PlatformResult(
                platform=p,
                status="success",
                post_id=post_id,
                account_id=acc_id,
            )
            for p, acc_id in plats.items()
        ]

    if batch_platforms:
        results.extend(await _submit(request.content, batch_platforms))

    for p in override_platforms:
        content = request.overrides[p]
        acc_id = dispatchable[p]
        results.extend(await _submit(content, {p: acc_id}))

    results.extend(unmapped_failures)

    return PublishResponse(
        success=[r for r in results if r.status == "success"],
        partial=[r for r in results if r.status == "partial"],
        failure=[r for r in results if r.status == "failure"],
        pipeline=request.pipeline.value,
        dispatched_at=now,
    )


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("pennyone")


@mcp.tool()
async def publish(request: PublishRequest) -> PublishResponse:
    """Fan out a publish request to the selected platforms under the pipeline's Zernio account."""
    return await _publish_core(request)


@mcp.tool()
async def list_platforms() -> List[str]:
    """List every platform Pennyone can publish to."""
    return [p.value for p in Platform]


@mcp.tool()
async def list_pipelines() -> List[Dict[str, str]]:
    """Return the pipeline registry -- label, voice, description, env var."""
    return [
        {"pipeline": pipeline.value, **info}
        for pipeline, info in PIPELINE_REGISTRY.items()
    ]


@mcp.tool()
async def pipeline_status() -> Dict[str, Dict[str, Any]]:
    """
    Per-pipeline: is the API key set? Does not make a network call.
    Use list_accounts or health_check for reachability.
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
async def list_accounts(pipeline: Pipeline) -> Dict[str, Any]:
    """
    List the connected social accounts for a pipeline. Returns one entry
    per account with the Pennyone platform name, the underlying Zernio
    platform name, the account ID, username, display name and active flag.
    """
    api_key = _get_pipeline_key(pipeline)
    if not api_key:
        env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
        return {"error": f"Pipeline '{pipeline.value}' not provisioned. Set {env_var}."}

    try:
        accounts = await _zernio_list_accounts(api_key)
    except httpx.HTTPError as exc:
        return {"error": f"Zernio request failed: {exc}"}

    entries = []
    for acc in accounts:
        zernio_platform = acc.get("platform", "")
        entries.append(
            {
                "account_id": acc.get("_id"),
                "platform": ZERNIO_TO_PLATFORM.get(zernio_platform, zernio_platform).value
                if isinstance(ZERNIO_TO_PLATFORM.get(zernio_platform, zernio_platform), Platform)
                else zernio_platform,
                "zernio_platform": zernio_platform,
                "username": acc.get("username"),
                "display_name": acc.get("displayName"),
                "is_active": bool(acc.get("isActive") and acc.get("platformStatus") == "active"),
            }
        )
    return {"pipeline": pipeline.value, "count": len(entries), "accounts": entries}


@mcp.tool()
async def health_check(pipeline: Optional[Pipeline] = None) -> Dict[str, Any]:
    """
    Verify Zernio reachability by listing accounts. If pipeline is given,
    check just that one. Otherwise check every provisioned pipeline.
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
                    f"{ZERNIO_API_BASE}/accounts",
                    headers={"Authorization": f"Bearer {key}"},
                )
            if resp.status_code == 200:
                accounts = resp.json().get("accounts", [])
                active = [a for a in accounts if a.get("isActive") and a.get("platformStatus") == "active"]
                results[p.value] = {
                    "status": "ok",
                    "connected_accounts": len(accounts),
                    "active_accounts": len(active),
                    "platforms": sorted({a.get("platform", "?") for a in active}),
                }
            else:
                results[p.value] = {"status": "error", "zernio_status": resp.status_code}
        except httpx.HTTPError as exc:
            results[p.value] = {"status": "error", "message": str(exc)}

    return results


if __name__ == "__main__":
    mcp.run(transport="stdio")
