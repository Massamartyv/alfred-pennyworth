#!/usr/bin/env python3
"""
MCP Server for Fullscript -- Personal Supplement Tracking.

Provides tools to interact with the Fullscript API for viewing
patients, treatment plans, supplement recommendations and products.
Personal health context only.
"""

import json
import os
import sys
import time
import webbrowser
from contextlib import asynccontextmanager
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from threading import Thread
from typing import Optional, List, Dict, Any
from urllib.parse import urlencode, urlparse, parse_qs

import httpx
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

FULLSCRIPT_ENV = os.getenv("FULLSCRIPT_ENV", "sandbox")
FULLSCRIPT_CLIENT_ID = os.getenv("FULLSCRIPT_CLIENT_ID", "")
FULLSCRIPT_CLIENT_SECRET = os.getenv("FULLSCRIPT_CLIENT_SECRET", "")

if FULLSCRIPT_ENV == "sandbox":
    AUTH_BASE = "https://us-snd.fullscript.io"
    API_BASE = "https://api-us-snd.fullscript.io"
else:
    AUTH_BASE = "https://api-us.fullscript.io"
    API_BASE = "https://api-us.fullscript.io"

REDIRECT_URI = "http://localhost:8765/callback"
TOKEN_FILE = Path(__file__).parent / ".tokens.json"

# ---------------------------------------------------------------------------
# OAuth Token Management
# ---------------------------------------------------------------------------

_tokens: Dict[str, Any] = {}


def _load_tokens() -> Dict[str, Any]:
    """Load stored tokens from disk."""
    global _tokens
    if TOKEN_FILE.exists():
        with open(TOKEN_FILE) as f:
            _tokens = json.load(f)
    return _tokens


def _save_tokens(tokens: Dict[str, Any]) -> None:
    """Persist tokens to disk."""
    global _tokens
    _tokens = tokens
    with open(TOKEN_FILE, "w") as f:
        json.dump(tokens, f, indent=2)


async def _refresh_access_token() -> str:
    """Use the refresh token to obtain a new access token."""
    if not _tokens.get("refresh_token"):
        raise RuntimeError(
            "No refresh token available. Run the authorize tool first."
        )

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{AUTH_BASE}/oauth/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": _tokens["refresh_token"],
                "client_id": FULLSCRIPT_CLIENT_ID,
                "client_secret": FULLSCRIPT_CLIENT_SECRET,
            },
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        _save_tokens(data)
        return data["access_token"]


async def _get_access_token() -> str:
    """Return a valid access token, refreshing if necessary."""
    _load_tokens()

    if _tokens.get("access_token"):
        expires_at = _tokens.get("created_at", 0) + _tokens.get("expires_in", 0)
        if time.time() < expires_at - 60:
            return _tokens["access_token"]

    return await _refresh_access_token()


async def _exchange_code_for_token(code: str) -> Dict[str, Any]:
    """Exchange an authorization code for access and refresh tokens."""
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{AUTH_BASE}/oauth/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
                "client_id": FULLSCRIPT_CLIENT_ID,
                "client_secret": FULLSCRIPT_CLIENT_SECRET,
            },
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        _save_tokens(data)
        return data


# ---------------------------------------------------------------------------
# API Client
# ---------------------------------------------------------------------------

async def _api_request(
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict] = None,
    json_body: Optional[Dict] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to the Fullscript API."""
    token = await _get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method,
            f"{API_BASE}{endpoint}",
            headers=headers,
            params=params,
            json=json_body,
            timeout=30.0,
        )
        resp.raise_for_status()
        return resp.json()


def _handle_api_error(e: Exception) -> str:
    """Consistent error formatting."""
    if isinstance(e, httpx.HTTPStatusError):
        status = e.response.status_code
        if status == 401:
            return "Error: Authentication failed. Run fullscript_authorize to re-authenticate."
        if status == 403:
            return "Error: Permission denied. Check your Fullscript API scopes."
        if status == 404:
            return "Error: Resource not found. Check the ID is correct."
        if status == 422:
            return f"Error: Validation failed. {e.response.text}"
        if status == 429:
            return "Error: Rate limit exceeded. Wait before retrying."
        return f"Error: API returned status {status}. {e.response.text}"
    if isinstance(e, httpx.TimeoutException):
        return "Error: Request timed out. Try again."
    if isinstance(e, RuntimeError) and "refresh token" in str(e).lower():
        return "Error: Not authenticated. Run fullscript_authorize first to connect your Fullscript account."
    return f"Error: {type(e).__name__}: {e}"


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def _format_patient(p: Dict) -> str:
    """Format a patient record as markdown."""
    lines = [f"### {p.get('first_name', '')} {p.get('last_name', '')}"]
    lines.append(f"- **ID**: {p.get('id', 'N/A')}")
    if p.get("email"):
        lines.append(f"- **Email**: {p['email']}")
    if p.get("date_of_birth"):
        lines.append(f"- **DOB**: {p['date_of_birth']}")
    if p.get("gender"):
        lines.append(f"- **Gender**: {p['gender']}")
    return "\n".join(lines)


def _format_treatment_plan(tp: Dict) -> str:
    """Format a treatment plan as markdown."""
    lines = [f"### Treatment Plan: {tp.get('id', 'N/A')}"]
    lines.append(f"- **Status**: {tp.get('state', 'unknown')}")
    if tp.get("created_at"):
        lines.append(f"- **Created**: {tp['created_at']}")

    recs = tp.get("recommendations", [])
    if recs:
        lines.append(f"- **Recommendations**: {len(recs)}")
        for r in recs:
            product = r.get("product", {})
            name = product.get("name", "Unknown product")
            dosage = r.get("dosage", {})
            dose_str = ""
            if dosage:
                amt = dosage.get("recommended_amount", "")
                freq = dosage.get("recommended_frequency", "")
                dose_str = f" -- {amt} {freq}".strip()
            lines.append(f"  - {name}{dose_str}")

    return "\n".join(lines)


def _format_product(p: Dict) -> str:
    """Format a product as markdown."""
    lines = [f"### {p.get('name', 'Unknown')}"]
    brand = p.get("brand", {})
    if brand:
        lines.append(f"- **Brand**: {brand.get('name', 'N/A')}")
    if p.get("description_html"):
        lines.append(f"- **Description**: {p['description_html'][:200]}...")

    dosage = p.get("dosage", {})
    if dosage:
        if dosage.get("recommended_amount"):
            lines.append(f"- **Dosage**: {dosage['recommended_amount']}")
        if dosage.get("recommended_frequency"):
            lines.append(f"- **Frequency**: {dosage['recommended_frequency']}")
        if dosage.get("format"):
            lines.append(f"- **Form**: {dosage['format']}")

    variant = p.get("primary_variant", {})
    if variant:
        if variant.get("units"):
            lines.append(f"- **Size**: {variant['units']} {variant.get('unit_of_measure', '')}")
        if variant.get("msrp"):
            lines.append(f"- **MSRP**: ${variant['msrp']}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP("fullscript_mcp")

# -- Authentication --

class AuthorizeInput(BaseModel):
    """Input for the authorize tool."""
    model_config = ConfigDict(str_strip_whitespace=True)


@mcp.tool(
    name="fullscript_authorize",
    annotations={
        "title": "Authorize Fullscript",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    },
)
async def fullscript_authorize(params: AuthorizeInput) -> str:
    """Initiate OAuth authorization with Fullscript.

    Opens a browser window for Fullscript login. After authorizing,
    the callback is captured locally and tokens are stored for future use.
    Only needs to be run once -- refresh tokens handle subsequent sessions.

    Returns:
        str: Success or error message.
    """
    auth_url = (
        f"{AUTH_BASE}/oauth/authorize?"
        + urlencode(
            {
                "client_id": FULLSCRIPT_CLIENT_ID,
                "redirect_uri": REDIRECT_URI,
                "response_type": "code",
            }
        )
    )

    captured_code = {}

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            if "code" in query:
                captured_code["code"] = query["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(
                    b"<html><body><h1>Authorized</h1>"
                    b"<p>You can close this window and return to Alfred.</p>"
                    b"</body></html>"
                )
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"No authorization code received.")

        def log_message(self, format, *args):
            pass  # Suppress HTTP logs on stdout

    server = HTTPServer(("localhost", 8765), CallbackHandler)
    thread = Thread(target=server.handle_request, daemon=True)
    thread.start()

    webbrowser.open(auth_url)

    thread.join(timeout=120)
    server.server_close()

    if "code" not in captured_code:
        return "Error: Authorization timed out. No code received within 2 minutes."

    try:
        tokens = await _exchange_code_for_token(captured_code["code"])
        return (
            "Fullscript authorized successfully. "
            f"Access token expires in {tokens.get('expires_in', 'unknown')} seconds. "
            "Refresh token stored for future sessions."
        )
    except Exception as e:
        return _handle_api_error(e)


# -- Patients --

class ListPatientsInput(BaseModel):
    """Input for listing patients."""
    model_config = ConfigDict(str_strip_whitespace=True)

    limit: Optional[int] = Field(
        default=20,
        description="Maximum patients to return (1-100)",
        ge=1,
        le=100,
    )
    page: Optional[int] = Field(
        default=1,
        description="Page number for pagination",
        ge=1,
    )
    patient_type: Optional[str] = Field(
        default=None,
        description="Filter by type: 'all', 'dependent', or 'guardian'",
    )


@mcp.tool(
    name="fullscript_list_patients",
    annotations={
        "title": "List Fullscript Patients",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fullscript_list_patients(params: ListPatientsInput) -> str:
    """List all patients in the connected Fullscript clinic.

    Returns patient names, IDs, emails, and demographics.
    Supports pagination and filtering by patient type.

    Returns:
        str: Markdown-formatted list of patients with pagination info.
    """
    try:
        query_params = {"page[size]": params.limit, "page[number]": params.page}
        if params.patient_type:
            query_params["patient_type"] = params.patient_type

        data = await _api_request("/api/clinic/patients", params=query_params)
        patients = data.get("data", data.get("patients", []))
        meta = data.get("meta", {})

        if not patients:
            return "No patients found."

        lines = ["# Patients", ""]
        for p in patients:
            attrs = p.get("attributes", p)
            lines.append(_format_patient(attrs))
            lines.append("")

        if meta:
            lines.append(f"Page {meta.get('current_page', '?')} of {meta.get('total_pages', '?')} -- {meta.get('total_count', '?')} total")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


class SearchPatientsInput(BaseModel):
    """Input for searching patients."""
    model_config = ConfigDict(str_strip_whitespace=True)

    query: str = Field(
        ...,
        description="Search term (name or email)",
        min_length=1,
        max_length=200,
    )


@mcp.tool(
    name="fullscript_search_patients",
    annotations={
        "title": "Search Fullscript Patients",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fullscript_search_patients(params: SearchPatientsInput) -> str:
    """Search for patients by name or email.

    Returns:
        str: Markdown-formatted list of matching patients.
    """
    try:
        data = await _api_request(
            "/api/clinic/search/patients",
            params={"query": params.query},
        )
        patients = data.get("data", data.get("patients", []))

        if not patients:
            return f"No patients found matching '{params.query}'."

        lines = [f"# Patient Search: '{params.query}'", ""]
        for p in patients:
            attrs = p.get("attributes", p)
            lines.append(_format_patient(attrs))
            lines.append("")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# -- Treatment Plans --

class ListTreatmentPlansInput(BaseModel):
    """Input for listing treatment plans."""
    model_config = ConfigDict(str_strip_whitespace=True)

    patient_id: str = Field(
        ...,
        description="The patient ID to list treatment plans for",
        min_length=1,
    )
    page: Optional[int] = Field(default=1, description="Page number", ge=1)


@mcp.tool(
    name="fullscript_list_treatment_plans",
    annotations={
        "title": "List Treatment Plans",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fullscript_list_treatment_plans(params: ListTreatmentPlansInput) -> str:
    """List all treatment plans for a specific patient.

    Treatment plans contain supplement recommendations with dosage instructions.
    Use fullscript_list_patients or fullscript_search_patients first to find
    the patient ID.

    Returns:
        str: Markdown-formatted list of treatment plans with supplement recommendations.
    """
    try:
        data = await _api_request(
            f"/api/clinic/patients/{params.patient_id}/treatment_plans",
            params={"page[number]": params.page},
        )
        plans = data.get("data", data.get("treatment_plans", []))

        if not plans:
            return f"No treatment plans found for patient {params.patient_id}."

        lines = [f"# Treatment Plans for Patient {params.patient_id}", ""]
        for tp in plans:
            attrs = tp.get("attributes", tp)
            lines.append(_format_treatment_plan(attrs))
            lines.append("")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


class GetTreatmentPlanInput(BaseModel):
    """Input for retrieving a specific treatment plan."""
    model_config = ConfigDict(str_strip_whitespace=True)

    treatment_plan_id: str = Field(
        ...,
        description="The treatment plan ID to retrieve",
        min_length=1,
    )


@mcp.tool(
    name="fullscript_get_treatment_plan",
    annotations={
        "title": "Get Treatment Plan Details",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fullscript_get_treatment_plan(params: GetTreatmentPlanInput) -> str:
    """Retrieve a specific treatment plan with full supplement recommendations and dosages.

    Returns:
        str: Markdown-formatted treatment plan with all supplement details.
    """
    try:
        data = await _api_request(
            f"/api/clinic/treatment_plans/{params.treatment_plan_id}"
        )
        plan = data.get("data", data.get("treatment_plan", data))
        attrs = plan.get("attributes", plan)
        return _format_treatment_plan(attrs)
    except Exception as e:
        return _handle_api_error(e)


# -- Products --

class GetProductInput(BaseModel):
    """Input for retrieving a product."""
    model_config = ConfigDict(str_strip_whitespace=True)

    product_id: str = Field(
        ...,
        description="The Fullscript product ID",
        min_length=1,
    )


@mcp.tool(
    name="fullscript_get_product",
    annotations={
        "title": "Get Product Details",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fullscript_get_product(params: GetProductInput) -> str:
    """Retrieve details for a specific supplement product.

    Returns brand, dosage instructions, form, size, and pricing.

    Returns:
        str: Markdown-formatted product details.
    """
    try:
        data = await _api_request(f"/api/catalog/products/{params.product_id}")
        product = data.get("data", data.get("product", data))
        attrs = product.get("attributes", product)
        return _format_product(attrs)
    except Exception as e:
        return _handle_api_error(e)


class SearchProductsInput(BaseModel):
    """Input for searching the product catalog."""
    model_config = ConfigDict(str_strip_whitespace=True)

    query: str = Field(
        ...,
        description="Search term for products (e.g., 'magnesium', 'vitamin D')",
        min_length=1,
        max_length=200,
    )
    limit: Optional[int] = Field(
        default=10,
        description="Maximum results to return",
        ge=1,
        le=50,
    )


@mcp.tool(
    name="fullscript_search_products",
    annotations={
        "title": "Search Supplement Products",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fullscript_search_products(params: SearchProductsInput) -> str:
    """Search the Fullscript supplement catalog by name, ingredient, or brand.

    Returns:
        str: Markdown-formatted list of matching products with details.
    """
    try:
        data = await _api_request(
            "/api/product-search",
            params={"q": params.query, "page[size]": params.limit},
        )
        products = data.get("data", data.get("products", []))

        if not products:
            return f"No products found matching '{params.query}'."

        lines = [f"# Product Search: '{params.query}'", ""]
        for p in products:
            attrs = p.get("attributes", p)
            lines.append(_format_product(attrs))
            lines.append("")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# -- Auth Status --

@mcp.tool(
    name="fullscript_auth_status",
    annotations={
        "title": "Check Fullscript Auth Status",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def fullscript_auth_status() -> str:
    """Check whether Fullscript is currently authenticated.

    Returns:
        str: Authentication status and token expiry information.
    """
    _load_tokens()
    if not _tokens.get("refresh_token"):
        return "Not authenticated. Run fullscript_authorize to connect your Fullscript account."

    expires_at = _tokens.get("created_at", 0) + _tokens.get("expires_in", 0)
    if time.time() < expires_at - 60:
        remaining = int(expires_at - time.time())
        return f"Authenticated. Access token valid for {remaining // 60} minutes. Refresh token available."
    else:
        return "Access token expired. Refresh token available -- will auto-refresh on next API call."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
