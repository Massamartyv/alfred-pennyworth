#!/usr/bin/env python3
"""
Instantly MCP Server -- Outbound lead pipeline router.

Thin FastMCP layer over the Instantly v2 API. Exposes read access to
campaigns, leads, inbox and analytics, plus a gated set of write
operations for qualifying responses and pausing campaigns.

Each pipeline owns its own Instantly workspace and its own API key.
Today only the `five_points` pipeline is provisioned; the pipeline
registry is ready to accept additional pipelines (personal, other
ventures) without an API break.

Write tools carry `writes: True` in their description so the calling
agent follows Navigation Rule 3 and asks for confirmation before
dispatch. The server itself does not enforce the gate.
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

INSTANTLY_API_BASE = os.getenv("INSTANTLY_API_BASE", "https://api.instantly.ai/api/v2")

REQUEST_TIMEOUT_SECONDS = 30.0
HEALTH_TIMEOUT_SECONDS = 10.0


# ---------------------------------------------------------------------------
# Pipelines
# ---------------------------------------------------------------------------


class Pipeline(str, Enum):
    """
    Routing key for an Instantly request. Each pipeline is isolated --
    its own Instantly workspace, its own API key. Personal and venture
    pipelines never share credentials.
    """

    FIVE_POINTS = "five_points"
    # Future: PERSONAL = "personal"


PIPELINE_REGISTRY: Dict[Pipeline, Dict[str, str]] = {
    Pipeline.FIVE_POINTS: {
        "label": "Five Points Digital Studio",
        "description": "Premium digital marketing agency -- outbound lead pipeline",
        "env_var": "INSTANTLY_FIVEPOINTS_API_KEY",
    },
}


def _get_pipeline_key(pipeline: Pipeline) -> Optional[str]:
    env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
    value = os.getenv(env_var)
    return value or None


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class LeadFilter(BaseModel):
    """Optional filters passed to list_leads. All fields optional."""

    campaign_id: Optional[str] = None
    list_id: Optional[str] = None
    email: Optional[str] = None
    interest_status: Optional[int] = Field(
        default=None,
        description="Instantly interest status code (1=interested, 2=meeting booked, etc.)",
    )
    limit: int = 50
    starting_after: Optional[str] = None


class PipelineResponse(BaseModel):
    """Wrapper for responses that may fail before reaching Instantly."""

    pipeline: str
    ok: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# Instantly HTTP adapter -- the single swap point for API shape.
# ---------------------------------------------------------------------------


async def _request(
    pipeline: Pipeline,
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: float = REQUEST_TIMEOUT_SECONDS,
) -> PipelineResponse:
    """
    Execute a single Instantly v2 API call scoped to a pipeline.

    Returns a PipelineResponse envelope. Never raises -- every error
    (missing key, network, non-2xx) is surfaced through `ok` and `error`.
    """
    api_key = _get_pipeline_key(pipeline)
    if not api_key:
        env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
        return PipelineResponse(
            pipeline=pipeline.value,
            ok=False,
            error=f"Pipeline '{pipeline.value}' not provisioned. Set {env_var}.",
        )

    url = f"{INSTANTLY_API_BASE}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    }
    if json_body is not None:
        headers["Content-Type"] = "application/json"

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.request(
                method,
                url,
                headers=headers,
                params=params,
                json=json_body,
            )
    except httpx.HTTPError as exc:
        return PipelineResponse(
            pipeline=pipeline.value,
            ok=False,
            error=f"HTTP request failed: {exc}",
        )

    body: Any
    if resp.headers.get("content-type", "").startswith("application/json"):
        try:
            body = resp.json()
        except ValueError:
            body = resp.text
    else:
        body = resp.text

    if resp.status_code >= 400:
        return PipelineResponse(
            pipeline=pipeline.value,
            ok=False,
            status_code=resp.status_code,
            error=f"Instantly {resp.status_code}: {str(body)[:500]}",
            data=body if isinstance(body, dict) else None,
        )

    return PipelineResponse(
        pipeline=pipeline.value,
        ok=True,
        status_code=resp.status_code,
        data=body,
    )


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("instantly")


# ---------------------------------------------------------------------------
# Helper tools
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_pipelines() -> List[Dict[str, str]]:
    """Return the pipeline registry -- label, description, env var."""
    return [
        {"pipeline": pipeline.value, **info}
        for pipeline, info in PIPELINE_REGISTRY.items()
    ]


@mcp.tool()
async def pipeline_status() -> Dict[str, Dict[str, Any]]:
    """
    Per-pipeline: is the API key set? Does not make a network call.
    Use health_check to test reachability.
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
async def health_check(pipeline: Pipeline = Pipeline.FIVE_POINTS) -> Dict[str, Any]:
    """
    Verify Instantly reachability by fetching the current workspace.
    Returns workspace id, name, owner and plan on success.
    """
    result = await _request(
        pipeline, "GET", "/workspaces/current", timeout=HEALTH_TIMEOUT_SECONDS
    )
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 1 -- Read-only
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_campaigns(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    limit: int = 50,
    starting_after: Optional[str] = None,
    search: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List campaigns in the pipeline's Instantly workspace. Supports
    cursor pagination via `starting_after` and optional name search.
    """
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if search:
        params["search"] = search
    result = await _request(pipeline, "GET", "/campaigns", params=params)
    return result.model_dump(mode="json")


@mcp.tool()
async def get_campaign_analytics(
    campaign_id: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    Return campaign-level analytics (sent, opened, replied, positive
    reply, bounce) for one campaign.
    """
    result = await _request(
        pipeline, "GET", f"/campaigns/{campaign_id}/analytics"
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def get_analytics_overview(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    Aggregate analytics across every campaign in the pipeline. Top-of-
    funnel view for Watchtower and weekly briefings.
    """
    result = await _request(
        pipeline, "GET", "/campaigns/analytics/overview"
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def get_daily_analytics(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    campaign_id: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Daily analytics time series. Optionally filter by campaign and date
    range (YYYY-MM-DD). Used for trend analysis.
    """
    params: Dict[str, Any] = {}
    if campaign_id:
        params["campaign_id"] = campaign_id
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date
    result = await _request(
        pipeline, "GET", "/campaigns/analytics/daily", params=params or None
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def list_leads(
    filters: Optional[LeadFilter] = None,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    List leads in the pipeline. Supports filters by campaign, list,
    email and interest status. Uses Instantly's POST /leads/list.
    """
    filters = filters or LeadFilter()
    body: Dict[str, Any] = {"limit": filters.limit}
    if filters.campaign_id:
        body["campaign_id"] = filters.campaign_id
    if filters.list_id:
        body["list_id"] = filters.list_id
    if filters.email:
        body["email"] = filters.email
    if filters.interest_status is not None:
        body["filter"] = {"interest_status": filters.interest_status}
    if filters.starting_after:
        body["starting_after"] = filters.starting_after
    result = await _request(pipeline, "POST", "/leads/list", json_body=body)
    return result.model_dump(mode="json")


@mcp.tool()
async def get_lead(
    lead_id: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """Fetch a single lead's full record, including custom variables."""
    result = await _request(pipeline, "GET", f"/leads/{lead_id}")
    return result.model_dump(mode="json")


@mcp.tool()
async def list_inbox_emails(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    limit: int = 25,
    starting_after: Optional[str] = None,
    is_unread: Optional[bool] = None,
    campaign_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List emails in the pipeline's unibox. Optionally filter to unread
    only or to a specific campaign.
    """
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if is_unread is not None:
        params["is_unread"] = "true" if is_unread else "false"
    if campaign_id:
        params["campaign_id"] = campaign_id
    result = await _request(pipeline, "GET", "/emails", params=params)
    return result.model_dump(mode="json")


@mcp.tool()
async def count_unread(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """Count unread emails across the pipeline's unibox. Watchtower signal."""
    result = await _request(pipeline, "GET", "/emails/unread/count")
    return result.model_dump(mode="json")


@mcp.tool()
async def search_campaign_by_lead(
    email: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    Find which campaigns contain a given lead email. Attribution and
    de-duplication check before adding a lead to a new campaign.
    """
    result = await _request(
        pipeline,
        "POST",
        "/campaigns/search-by-lead-email",
        json_body={"email": email},
    )
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 2 -- Writes (gated in chat per Navigation Rule 3)
# ---------------------------------------------------------------------------


@mcp.tool()
async def update_lead_interest(
    lead_id: str,
    interest_status: int,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    WRITE. Update a lead's interest status. Standard Instantly codes:
    1 = interested, 2 = meeting booked, 3 = meeting completed,
    4 = closed, -1 = not interested, -2 = wrong person, -3 = lost.

    Alfred must confirm with the user before calling. Changes are
    visible in the Instantly inbox and campaign reports.
    """
    result = await _request(
        pipeline,
        "PATCH",
        f"/leads/{lead_id}/interest-status",
        json_body={"interest_status": interest_status},
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def add_leads_bulk(
    leads: List[Dict[str, Any]],
    campaign_id: Optional[str] = None,
    list_id: Optional[str] = None,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    skip_if_in_workspace: bool = True,
) -> Dict[str, Any]:
    """
    WRITE. Add leads in bulk to a campaign or list. Each lead dict
    must include at minimum `email`; `first_name`, `last_name`,
    `company_name` and custom variables are optional.

    Alfred must confirm with the user before calling. Volumes over
    50 leads should be split into batches to avoid surprises.
    """
    body: Dict[str, Any] = {
        "leads": leads,
        "skip_if_in_workspace": skip_if_in_workspace,
    }
    if campaign_id:
        body["campaign"] = campaign_id
    if list_id:
        body["list_id"] = list_id
    result = await _request(
        pipeline, "POST", "/leads/bulk-add", json_body=body
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def pause_campaign(
    campaign_id: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    WRITE. Pause an active campaign. Stops further sends until the
    campaign is reactivated. Alfred must confirm with the user before
    calling.
    """
    result = await _request(
        pipeline, "POST", f"/campaigns/{campaign_id}/pause"
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def reply_to_email(
    email_id: str,
    body_text: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    body_html: Optional[str] = None,
    subject: Optional[str] = None,
) -> Dict[str, Any]:
    """
    WRITE. Reply to an email in the Instantly unibox. Always gated --
    Alfred must show the drafted reply to the user and receive
    explicit confirmation before calling. Treats this call as a
    send, not a draft.
    """
    body: Dict[str, Any] = {"body": body_text}
    if body_html:
        body["body_html"] = body_html
    if subject:
        body["subject"] = subject
    result = await _request(
        pipeline, "POST", f"/emails/{email_id}/reply", json_body=body
    )
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    mcp.run(transport="stdio")
