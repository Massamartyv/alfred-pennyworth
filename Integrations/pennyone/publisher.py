#!/usr/bin/env python3
"""
Pennyone publisher -- reads Notion Content Calendar entries and dispatches
them through Pennyone.

The mapping layer between Notion and Pennyone. Keeps Pennyone pure (generic
syndication router) while giving each pipeline a clean path from planning
to published.

Two modes:

1. Library: import build_request_from_notion() and format_pennyone_log()
   directly. Callers that already have a page dict (Claude sessions using
   the managed Notion MCP) feed their own data in.

2. CLI: `python publisher.py --pipeline personal [--dry-run] [--page-id ID]`.
   Reads the pipeline's Notion integration token from env, queries the
   Content Calendar for eligible entries, dispatches each through Pennyone,
   writes results back.

Workflow contract:
- Eligible entry: Status = "Scheduled" AND Publish Date <= now.
- After dispatch: Status -> "Published", Zernio Post ID populated, Pennyone
  Log written, Publish Date left alone as the historical record.
- On failure: Status stays "Scheduled", Pennyone Log records the error, no
  Zernio Post ID set. Next run retries.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import mimetypes
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

import httpx

# The server module lives next to this file.
sys.path.insert(0, str(Path(__file__).parent))
import server  # noqa: E402

# ---------------------------------------------------------------------------
# Pipeline -> Notion plumbing
# ---------------------------------------------------------------------------

# Per-pipeline Notion integration token env var. Personal is the only one
# without a Stripe-style per-venture naming because it is the default scope.
PIPELINE_TO_NOTION_TOKEN_ENV: Dict[server.Pipeline, str] = {
    server.Pipeline.PERSONAL: "NOTION_PERSONAL_TOKEN",
    server.Pipeline.MARTY_GRAS: "NOTION_MARTYGRAS_TOKEN",
    server.Pipeline.FIVE_POINTS: "NOTION_FIVEPOINTS_TOKEN",
    server.Pipeline.PARADIGM: "NOTION_PARADIGM_TOKEN",
    server.Pipeline.LILLIE_AND_LYNETTE: "NOTION_LILLIEANDLYNETTE_TOKEN",
}

# Per-pipeline Content Calendar data source ID. Each pipeline runs its own
# Notion workspace with its own Content Calendar; Five Points and the rest
# come online as their workspaces are provisioned.
PIPELINE_TO_CONTENT_CALENDAR: Dict[server.Pipeline, Optional[str]] = {
    server.Pipeline.PERSONAL: "ad36d098-c55c-46f9-b133-b3bfbd5cd81f",
    server.Pipeline.MARTY_GRAS: None,
    server.Pipeline.FIVE_POINTS: None,
    server.Pipeline.PARADIGM: None,
    server.Pipeline.LILLIE_AND_LYNETTE: None,
}

# Notion Platform page name -> Pennyone Platform. Unknown names are skipped.
PLATFORM_NAME_MAP: Dict[str, server.Platform] = {
    "Instagram": server.Platform.INSTAGRAM,
    "TikTok": server.Platform.TIKTOK,
    "Threads": server.Platform.THREADS,
    "X": server.Platform.X,
    "Twitter": server.Platform.X,
    "Reddit": server.Platform.REDDIT,
    "Snap": server.Platform.SNAP,
    "Snapchat": server.Platform.SNAP,
}

# Notion Content Calendar Type -> default MediaAsset kind. Maps the
# editorial Type field to the media shape Zernio expects.
TYPE_TO_MEDIA_KIND: Dict[str, str] = {
    "Photograph": "image",
    "Graphic Design": "image",
    "Carousel": "image",
    "Short Form Videography": "video",
    "Long Form Videography": "video",
    "Blog": "image",
}

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_API_VERSION = "2025-09-03"

# ---------------------------------------------------------------------------
# Pure mapping helpers -- no I/O. Testable, importable.
# ---------------------------------------------------------------------------


def _extract_text(rich_text: List[Dict[str, Any]]) -> str:
    return "".join(rt.get("plain_text", "") for rt in rich_text or []).strip()


def _extract_files(files_prop: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return a normalized list of {name, url, expiry_time} for each file."""
    out: List[Dict[str, Any]] = []
    for f in files_prop.get("files", []) or []:
        if f.get("type") == "external":
            url = f.get("external", {}).get("url")
        else:
            url = f.get("file", {}).get("url")
        out.append(
            {
                "name": f.get("name", ""),
                "url": url,
                "expiry_time": f.get("file", {}).get("expiry_time"),
                "type": f.get("type"),
            }
        )
    return out


def build_request_from_notion(
    page_properties: Dict[str, Any],
    platform_name_by_id: Dict[str, str],
    pipeline: server.Pipeline,
    media_local_paths: Optional[List[str]] = None,
) -> Tuple[server.PublishRequest, List[str]]:
    """
    Convert a Notion Content Calendar page into a Pennyone PublishRequest.

    Parameters
    ----------
    page_properties : dict
        The "properties" block from the Notion page object.
    platform_name_by_id : dict
        Lookup from Notion Platform page ID to the Platform row's Name.
        The caller resolves these ahead of time.
    pipeline : server.Pipeline
        Which pipeline this entry belongs to (derived from which workspace
        or Content Calendar the page lives in).
    media_local_paths : list of str, optional
        Local paths for downloaded Notion media files, in the same order
        as the page's Media property. If supplied, MediaAssets use `path`;
        otherwise MediaAssets use the Notion `url` directly (which may
        expire for Notion-hosted files).

    Returns
    -------
    (PublishRequest, list of warnings)
        The request plus any non-fatal warnings (unknown platforms, empty
        captions, missing dates, etc.).
    """
    warnings: List[str] = []

    caption_prop = page_properties.get("Caption", {})
    caption = _extract_text(caption_prop.get("rich_text", []))
    if not caption:
        warnings.append("Caption is empty.")

    platform_rel = page_properties.get("Platform", {}).get("relation", []) or []
    platforms: List[server.Platform] = []
    for rel in platform_rel:
        name = platform_name_by_id.get(rel.get("id", ""), "")
        mapped = PLATFORM_NAME_MAP.get(name)
        if mapped is None:
            if name:
                warnings.append(f"Unknown platform '{name}' -- skipped.")
            continue
        if mapped not in platforms:
            platforms.append(mapped)

    date_prop = page_properties.get("Publish Date", {}).get("date") or {}
    schedule_at: Optional[datetime] = None
    start = date_prop.get("start")
    if start:
        try:
            dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            if dt > datetime.now(timezone.utc):
                schedule_at = dt
        except ValueError:
            warnings.append(f"Unparseable Publish Date '{start}'.")

    type_name = page_properties.get("Type", {}).get("select", {}) or {}
    default_kind = TYPE_TO_MEDIA_KIND.get(type_name.get("name", ""), "image")

    media_files = _extract_files(page_properties.get("Media", {}))
    media_assets: List[server.MediaAsset] = []
    for idx, f in enumerate(media_files):
        if media_local_paths and idx < len(media_local_paths) and media_local_paths[idx]:
            media_assets.append(server.MediaAsset(path=media_local_paths[idx], kind=default_kind))
        elif f["url"]:
            if f.get("expiry_time"):
                warnings.append(
                    f"Media '{f['name']}' uses a Notion-hosted URL that expires; download before scheduled publish."
                )
            media_assets.append(server.MediaAsset(url=f["url"], kind=default_kind))
        else:
            warnings.append(f"Media '{f['name']}' has no URL and no local path -- skipped.")

    request = server.PublishRequest(
        content=server.ContentPayload(text=caption, media=media_assets),
        platforms=platforms,
        pipeline=pipeline,
        schedule_at=schedule_at,
    )
    return request, warnings


def format_pennyone_log(response: server.PublishResponse, warnings: List[str] | None = None) -> str:
    """
    Format a PublishResponse as a plain-text log suitable for the Pennyone
    Log field on a Content Calendar page. Lists per-platform outcomes plus
    any pre-dispatch warnings from the mapper.
    """
    lines = [f"Dispatched {response.dispatched_at.isoformat()} (pipeline: {response.pipeline})."]
    for r in response.success:
        lines.append(f"[success] {r.platform.value}: post_id={r.post_id} account={r.account_id}")
    for r in response.partial:
        lines.append(f"[partial] {r.platform.value}: {r.error}")
    for r in response.failure:
        lines.append(f"[failure] {r.platform.value}: {r.error}")
    if warnings:
        lines.append("")
        lines.append("Warnings:")
        for w in warnings:
            lines.append(f"- {w}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Notion I/O for the CLI mode
# ---------------------------------------------------------------------------


def _notion_headers(token: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_API_VERSION,
        "Content-Type": "application/json",
    }


async def _notion_query_scheduled(
    token: str, data_source_id: str, now: datetime
) -> List[Dict[str, Any]]:
    body = {
        "filter": {
            "and": [
                {"property": "Status", "status": {"equals": "Scheduled"}},
                {"property": "Publish Date", "date": {"on_or_before": now.isoformat()}},
            ]
        },
        "page_size": 100,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(
            f"{NOTION_API_BASE}/data_sources/{data_source_id}/query",
            headers=_notion_headers(token),
            json=body,
        )
        resp.raise_for_status()
        return resp.json().get("results", [])


async def _notion_resolve_platforms(
    token: str, platform_ids: List[str]
) -> Dict[str, str]:
    """For each Platform page ID, fetch its Name (title property)."""
    out: Dict[str, str] = {}
    if not platform_ids:
        return out
    async with httpx.AsyncClient(timeout=30.0) as client:
        for pid in set(platform_ids):
            resp = await client.get(
                f"{NOTION_API_BASE}/pages/{pid}", headers=_notion_headers(token)
            )
            if resp.status_code >= 300:
                continue
            props = resp.json().get("properties", {})
            title = props.get("Name", {}).get("title", [])
            out[pid] = _extract_text(title)
    return out


async def _download_notion_files(
    files: List[Dict[str, Any]], work_dir: Path
) -> List[Optional[str]]:
    """Download each Notion file (expiring URL) to a local path."""
    paths: List[Optional[str]] = []
    async with httpx.AsyncClient(timeout=60.0, follow_redirects=True) as client:
        for idx, f in enumerate(files):
            if not f.get("url"):
                paths.append(None)
                continue
            if f.get("type") == "external":
                # External URLs are stable; skip download, use URL directly.
                paths.append(None)
                continue
            ext = Path(f.get("name", "")).suffix or mimetypes.guess_extension(
                f.get("mimeType", "") or ""
            ) or ""
            local = work_dir / f"media_{idx}{ext}"
            try:
                resp = await client.get(f["url"])
                resp.raise_for_status()
                local.write_bytes(resp.content)
                paths.append(str(local))
            except httpx.HTTPError:
                paths.append(None)
    return paths


async def _notion_update_page(
    token: str, page_id: str, updates: Dict[str, Any]
) -> None:
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.patch(
            f"{NOTION_API_BASE}/pages/{page_id}",
            headers=_notion_headers(token),
            json={"properties": updates},
        )
        resp.raise_for_status()


def _writeback_properties(
    response: server.PublishResponse, log_text: str, mark_published: bool
) -> Dict[str, Any]:
    first_success = response.success[0] if response.success else None
    properties: Dict[str, Any] = {
        "Pennyone Log": {"rich_text": [{"type": "text", "text": {"content": log_text[:2000]}}]},
    }
    if first_success and first_success.post_id:
        properties["Zernio Post ID"] = {
            "rich_text": [{"type": "text", "text": {"content": first_success.post_id}}]
        }
    if mark_published:
        properties["Status"] = {"status": {"name": "Published"}}
    return properties


# ---------------------------------------------------------------------------
# CLI orchestration
# ---------------------------------------------------------------------------


async def run_cli(pipeline: server.Pipeline, page_id: Optional[str], dry_run: bool) -> int:
    token_env = PIPELINE_TO_NOTION_TOKEN_ENV[pipeline]
    token = os.getenv(token_env)
    if not token:
        print(
            f"Error: {token_env} not set. Create a Notion integration for the "
            f"{pipeline.value} workspace, grant it Content Calendar access, and "
            f"add the token to ~/Alfred Pennyworth/.env.",
            file=sys.stderr,
        )
        return 2

    calendar_id = PIPELINE_TO_CONTENT_CALENDAR[pipeline]
    if not calendar_id:
        print(
            f"Error: no Content Calendar data source registered for pipeline "
            f"{pipeline.value}. Add one to PIPELINE_TO_CONTENT_CALENDAR in "
            f"publisher.py.",
            file=sys.stderr,
        )
        return 2

    now = datetime.now(timezone.utc)

    if page_id:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.get(
                f"{NOTION_API_BASE}/pages/{page_id}", headers=_notion_headers(token)
            )
            resp.raise_for_status()
            pages = [resp.json()]
    else:
        pages = await _notion_query_scheduled(token, calendar_id, now)

    if not pages:
        print(f"No eligible entries for pipeline {pipeline.value}.")
        return 0

    print(f"Found {len(pages)} eligible entries for pipeline {pipeline.value}.")

    overall_rc = 0
    for page in pages:
        page_id = page["id"]
        props = page.get("properties", {})
        title = _extract_text(props.get("Name", {}).get("title", [])) or "(untitled)"
        print(f"\n--- {title} ({page_id}) ---")

        # Resolve platform names
        platform_ids = [
            r.get("id", "") for r in props.get("Platform", {}).get("relation", []) or []
        ]
        platform_names = await _notion_resolve_platforms(token, platform_ids)

        # Download media to a per-page temp dir
        files = _extract_files(props.get("Media", {}))
        with tempfile.TemporaryDirectory(prefix=f"pennyone-{page_id}-") as work_dir:
            local_paths = await _download_notion_files(files, Path(work_dir))

            request, warnings = build_request_from_notion(
                props, platform_names, pipeline, media_local_paths=local_paths
            )

            for w in warnings:
                print(f"  warn: {w}")

            if not request.platforms:
                log_text = "No mapped platforms on this entry. Pennyone skipped."
                if warnings:
                    log_text += "\n\nWarnings:\n" + "\n".join(f"- {w}" for w in warnings)
                print(f"  skip: {log_text}")
                if not dry_run:
                    await _notion_update_page(
                        token, page_id, {
                            "Pennyone Log": {"rich_text": [{"type": "text", "text": {"content": log_text[:2000]}}]},
                        },
                    )
                continue

            if dry_run:
                print(f"  DRY RUN: would dispatch to {[p.value for p in request.platforms]}")
                continue

            response = await server._publish_core(request)
            log_text = format_pennyone_log(response, warnings)
            print(f"  dispatched: success={len(response.success)} partial={len(response.partial)} failure={len(response.failure)}")

            mark_published = bool(response.success) and not response.failure and not response.partial
            updates = _writeback_properties(response, log_text, mark_published)
            await _notion_update_page(token, page_id, updates)

            if not mark_published:
                overall_rc = 1

    return overall_rc


def main() -> int:
    parser = argparse.ArgumentParser(description="Pennyone Notion publisher.")
    parser.add_argument(
        "--pipeline",
        required=True,
        choices=[p.value for p in server.Pipeline],
        help="Which pipeline to dispatch from.",
    )
    parser.add_argument(
        "--page-id",
        help="Dispatch a single Content Calendar page by ID instead of querying.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Map and print what would dispatch; do not call Zernio or write back.",
    )
    args = parser.parse_args()
    pipeline = server.Pipeline(args.pipeline)
    return asyncio.run(run_cli(pipeline, args.page_id, args.dry_run))


if __name__ == "__main__":
    sys.exit(main())
