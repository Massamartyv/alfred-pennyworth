#!/usr/bin/env python3
"""
Five Points Mail MCP Server -- Venture-scoped Gmail access.

Thin FastMCP layer over the Gmail API. Every tool takes a `mailbox`
routing key which selects one of the Five Points inboxes. A single
Google Cloud service account with domain-wide delegation impersonates
the target user per request, so five inboxes are reached with one
credential.

The inboxes live under the fivepoints.studio Google Workspace, with
hello@ as the admin and the others as users under the same domain.

Write tools carry `writes: True` in their description so the calling
agent follows Navigation Rule 3 and asks for confirmation before
dispatch. The server itself does not enforce the gate.
"""

import base64
import os
from email.message import EmailMessage
from enum import Enum
from functools import lru_cache
from typing import Optional, List, Dict, Any

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_DEFAULT_CREDENTIALS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "credentials",
    "service-account.json",
)

SERVICE_ACCOUNT_PATH = os.getenv(
    "FIVEPOINTS_MAIL_SERVICE_ACCOUNT",
    _DEFAULT_CREDENTIALS_PATH,
)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
]


# ---------------------------------------------------------------------------
# Mailbox registry
# ---------------------------------------------------------------------------


class Mailbox(str, Enum):
    """
    Routing key for a Five Points Mail request. Each value maps to one
    address inside the fivepoints.studio Google Workspace.
    """

    HELLO = "hello"
    MARTAVIOUS = "martavious"
    SYSTEMS = "systems"
    OPPORTUNITIES = "opportunities"
    FINANCE = "finance"


MAILBOX_REGISTRY: Dict[Mailbox, Dict[str, str]] = {
    Mailbox.HELLO: {
        "email": "hello@fivepoints.studio",
        "label": "Hello",
        "role": "Workspace admin. General engagements and admin.",
    },
    Mailbox.MARTAVIOUS: {
        "email": "martavious@fivepoints.studio",
        "label": "Martavious",
        "role": "Owner-direct. Personal studio communications.",
    },
    Mailbox.SYSTEMS: {
        "email": "systems@fivepoints.studio",
        "label": "Systems",
        "role": "Technical infrastructure and dev tooling.",
    },
    Mailbox.OPPORTUNITIES: {
        "email": "opportunities@fivepoints.studio",
        "label": "Opportunities",
        "role": "Sponsors, press, hiring and vendor inquiries.",
    },
    Mailbox.FINANCE: {
        "email": "finance@fivepoints.studio",
        "label": "Finance",
        "role": "Business banking, invoicing, financial platforms.",
    },
}


def _mailbox_email(mailbox: Mailbox) -> str:
    return MAILBOX_REGISTRY[mailbox]["email"]


# ---------------------------------------------------------------------------
# Gmail client factory -- one service per mailbox, cached.
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def _gmail_service(mailbox_email: str):
    """
    Build a Gmail service object impersonating `mailbox_email` via the
    service account's domain-wide delegation. Cached so repeated calls
    do not re-read the key file.
    """
    if not os.path.exists(SERVICE_ACCOUNT_PATH):
        raise FileNotFoundError(
            f"Service account key not found at {SERVICE_ACCOUNT_PATH}. "
            f"Drop the JSON key there or set FIVEPOINTS_MAIL_SERVICE_ACCOUNT."
        )
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_PATH,
        scopes=SCOPES,
        subject=mailbox_email,
    )
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def _service(mailbox: Mailbox):
    return _gmail_service(_mailbox_email(mailbox))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _header(headers: List[Dict[str, str]], name: str) -> Optional[str]:
    for h in headers:
        if h.get("name", "").lower() == name.lower():
            return h.get("value")
    return None


def _decode_part(data: Optional[str]) -> str:
    if not data:
        return ""
    return base64.urlsafe_b64decode(data.encode("utf-8")).decode("utf-8", errors="replace")


def _extract_body(payload: Dict[str, Any]) -> Dict[str, str]:
    """Walk the MIME tree and pull out text/plain and text/html bodies."""
    text, html = "", ""

    def walk(part: Dict[str, Any]):
        nonlocal text, html
        mime = part.get("mimeType", "")
        body = part.get("body", {}) or {}
        data = body.get("data")
        if mime == "text/plain" and data and not text:
            text = _decode_part(data)
        elif mime == "text/html" and data and not html:
            html = _decode_part(data)
        for sub in part.get("parts", []) or []:
            walk(sub)

    walk(payload or {})
    return {"text": text, "html": html}


def _summarise_message(msg: Dict[str, Any]) -> Dict[str, Any]:
    payload = msg.get("payload", {}) or {}
    headers = payload.get("headers", []) or []
    return {
        "id": msg.get("id"),
        "thread_id": msg.get("threadId"),
        "snippet": msg.get("snippet"),
        "from": _header(headers, "From"),
        "to": _header(headers, "To"),
        "cc": _header(headers, "Cc"),
        "subject": _header(headers, "Subject"),
        "date": _header(headers, "Date"),
        "label_ids": msg.get("labelIds", []),
        "size_estimate": msg.get("sizeEstimate"),
    }


def _build_rfc822(
    sender: str,
    to: List[str],
    subject: str,
    body: str,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    in_reply_to: Optional[str] = None,
    references: Optional[str] = None,
) -> str:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = ", ".join(to)
    if cc:
        msg["Cc"] = ", ".join(cc)
    if bcc:
        msg["Bcc"] = ", ".join(bcc)
    msg["Subject"] = subject
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
    if references:
        msg["References"] = references
    msg.set_content(body)
    return base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class MessageSummary(BaseModel):
    id: Optional[str] = None
    thread_id: Optional[str] = None
    snippet: Optional[str] = None
    from_: Optional[str] = Field(default=None, alias="from")
    to: Optional[str] = None
    cc: Optional[str] = None
    subject: Optional[str] = None
    date: Optional[str] = None
    label_ids: List[str] = Field(default_factory=list)
    size_estimate: Optional[int] = None

    model_config = {"populate_by_name": True}


class DraftRequest(BaseModel):
    mailbox: Mailbox
    to: List[str]
    subject: str
    body: str
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None
    thread_id: Optional[str] = None


class ReplyRequest(BaseModel):
    mailbox: Mailbox
    message_id: str
    body: str
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None


class SendRequest(BaseModel):
    mailbox: Mailbox
    to: List[str]
    subject: str
    body: str
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None
    thread_id: Optional[str] = None


class LabelUpdate(BaseModel):
    mailbox: Mailbox
    message_id: str
    add_labels: List[str] = Field(default_factory=list)
    remove_labels: List[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("fivepoints-mail")


# --- Read tools ------------------------------------------------------------


@mcp.tool()
async def list_mailboxes() -> List[Dict[str, str]]:
    """List the Five Points mailboxes this MCP routes to."""
    return [
        {"mailbox": m.value, **info}
        for m, info in MAILBOX_REGISTRY.items()
    ]


@mcp.tool()
async def health_check(mailbox: Optional[Mailbox] = None) -> Dict[str, Any]:
    """
    Verify Gmail API access for each mailbox by calling users.getProfile.
    If `mailbox` is given, check just that one; otherwise check all.
    """
    targets = [mailbox] if mailbox else list(Mailbox)
    results: Dict[str, Any] = {}
    for m in targets:
        try:
            profile = _service(m).users().getProfile(userId="me").execute()
            results[m.value] = {
                "status": "ok",
                "email": profile.get("emailAddress"),
                "messages_total": profile.get("messagesTotal"),
                "threads_total": profile.get("threadsTotal"),
            }
        except FileNotFoundError as exc:
            results[m.value] = {"status": "no_credentials", "message": str(exc)}
        except HttpError as exc:
            results[m.value] = {"status": "error", "message": str(exc)}
        except Exception as exc:
            results[m.value] = {"status": "error", "message": str(exc)}
    return results


@mcp.tool()
async def list_messages(
    mailbox: Mailbox,
    query: Optional[str] = None,
    max_results: int = 25,
    label_ids: Optional[List[str]] = None,
    include_spam_trash: bool = False,
) -> Dict[str, Any]:
    """
    List messages in a mailbox. `query` uses Gmail search syntax, e.g.
    'is:unread newer_than:7d from:@example.com'. Returns summaries, not
    full bodies.
    """
    svc = _service(mailbox)
    req = svc.users().messages().list(
        userId="me",
        q=query,
        maxResults=max(1, min(int(max_results), 100)),
        labelIds=label_ids,
        includeSpamTrash=include_spam_trash,
    )
    resp = req.execute()
    ids = [m["id"] for m in resp.get("messages", [])]

    messages: List[Dict[str, Any]] = []
    for mid in ids:
        msg = svc.users().messages().get(
            userId="me", id=mid, format="metadata",
            metadataHeaders=["From", "To", "Cc", "Subject", "Date"],
        ).execute()
        messages.append(_summarise_message(msg))

    return {
        "mailbox": mailbox.value,
        "email": _mailbox_email(mailbox),
        "count": len(messages),
        "next_page_token": resp.get("nextPageToken"),
        "messages": messages,
    }


@mcp.tool()
async def search(mailbox: Mailbox, query: str, max_results: int = 25) -> Dict[str, Any]:
    """
    Gmail search. Alias for list_messages with a required query. Useful
    for tool-call ergonomics when the intent is search.
    """
    return await list_messages(mailbox, query=query, max_results=max_results)


@mcp.tool()
async def read_message(
    mailbox: Mailbox,
    message_id: str,
    format: str = "full",
) -> Dict[str, Any]:
    """
    Fetch a single message with headers, snippet and decoded bodies
    (text and html). `format` is 'full' (default), 'metadata', or 'raw'.
    """
    svc = _service(mailbox)
    msg = svc.users().messages().get(
        userId="me", id=message_id, format=format,
    ).execute()
    summary = _summarise_message(msg)
    body = _extract_body(msg.get("payload", {}) or {}) if format == "full" else {}
    return {
        "mailbox": mailbox.value,
        "email": _mailbox_email(mailbox),
        **summary,
        "body_text": body.get("text", ""),
        "body_html": body.get("html", ""),
        "internal_date": msg.get("internalDate"),
        "history_id": msg.get("historyId"),
    }


@mcp.tool()
async def list_threads(
    mailbox: Mailbox,
    query: Optional[str] = None,
    max_results: int = 25,
    label_ids: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """List threads in a mailbox. Query uses the same Gmail search syntax."""
    svc = _service(mailbox)
    resp = svc.users().threads().list(
        userId="me",
        q=query,
        maxResults=max(1, min(int(max_results), 100)),
        labelIds=label_ids,
    ).execute()
    threads = [
        {
            "id": t.get("id"),
            "snippet": t.get("snippet"),
            "history_id": t.get("historyId"),
        }
        for t in resp.get("threads", [])
    ]
    return {
        "mailbox": mailbox.value,
        "email": _mailbox_email(mailbox),
        "count": len(threads),
        "next_page_token": resp.get("nextPageToken"),
        "threads": threads,
    }


@mcp.tool()
async def get_thread(mailbox: Mailbox, thread_id: str) -> Dict[str, Any]:
    """Fetch a thread with all its messages (summarised)."""
    svc = _service(mailbox)
    thread = svc.users().threads().get(
        userId="me", id=thread_id, format="full",
    ).execute()
    messages = [
        {
            **_summarise_message(m),
            **_extract_body(m.get("payload", {}) or {}),
        }
        for m in thread.get("messages", [])
    ]
    return {
        "mailbox": mailbox.value,
        "email": _mailbox_email(mailbox),
        "thread_id": thread.get("id"),
        "history_id": thread.get("historyId"),
        "messages": messages,
    }


@mcp.tool()
async def list_labels(mailbox: Mailbox) -> Dict[str, Any]:
    """List all labels (system and user) in a mailbox."""
    svc = _service(mailbox)
    resp = svc.users().labels().list(userId="me").execute()
    return {
        "mailbox": mailbox.value,
        "email": _mailbox_email(mailbox),
        "labels": resp.get("labels", []),
    }


@mcp.tool()
async def list_drafts(mailbox: Mailbox, max_results: int = 25) -> Dict[str, Any]:
    """List draft messages in a mailbox."""
    svc = _service(mailbox)
    resp = svc.users().drafts().list(
        userId="me",
        maxResults=max(1, min(int(max_results), 100)),
    ).execute()
    drafts = resp.get("drafts", [])
    out: List[Dict[str, Any]] = []
    for d in drafts:
        did = d.get("id")
        mid = (d.get("message") or {}).get("id")
        summary = {"draft_id": did, "message_id": mid}
        if mid:
            msg = svc.users().messages().get(
                userId="me", id=mid, format="metadata",
                metadataHeaders=["From", "To", "Cc", "Subject", "Date"],
            ).execute()
            summary.update(_summarise_message(msg))
        out.append(summary)
    return {
        "mailbox": mailbox.value,
        "email": _mailbox_email(mailbox),
        "count": len(out),
        "drafts": out,
    }


# --- Write tools -- Navigation Rule 3 applies ------------------------------


@mcp.tool()
async def create_draft(request: DraftRequest) -> Dict[str, Any]:
    """
    writes: True. Create a Gmail draft. Does not send. Returns the draft
    id so a follow-up call can send it after user confirmation.
    """
    svc = _service(request.mailbox)
    raw = _build_rfc822(
        sender=_mailbox_email(request.mailbox),
        to=request.to,
        subject=request.subject,
        body=request.body,
        cc=request.cc,
        bcc=request.bcc,
    )
    body: Dict[str, Any] = {"message": {"raw": raw}}
    if request.thread_id:
        body["message"]["threadId"] = request.thread_id
    draft = svc.users().drafts().create(userId="me", body=body).execute()
    return {
        "mailbox": request.mailbox.value,
        "draft_id": draft.get("id"),
        "message_id": (draft.get("message") or {}).get("id"),
        "thread_id": (draft.get("message") or {}).get("threadId"),
    }


@mcp.tool()
async def update_draft(
    mailbox: Mailbox,
    draft_id: str,
    to: List[str],
    subject: str,
    body: str,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    thread_id: Optional[str] = None,
) -> Dict[str, Any]:
    """writes: True. Replace a draft's contents."""
    svc = _service(mailbox)
    raw = _build_rfc822(
        sender=_mailbox_email(mailbox),
        to=to,
        subject=subject,
        body=body,
        cc=cc,
        bcc=bcc,
    )
    body_payload: Dict[str, Any] = {"message": {"raw": raw}}
    if thread_id:
        body_payload["message"]["threadId"] = thread_id
    draft = svc.users().drafts().update(
        userId="me", id=draft_id, body=body_payload,
    ).execute()
    return {
        "mailbox": mailbox.value,
        "draft_id": draft.get("id"),
        "message_id": (draft.get("message") or {}).get("id"),
    }


@mcp.tool()
async def delete_draft(mailbox: Mailbox, draft_id: str) -> Dict[str, Any]:
    """writes: True. Delete a draft. Irreversible."""
    svc = _service(mailbox)
    svc.users().drafts().delete(userId="me", id=draft_id).execute()
    return {"mailbox": mailbox.value, "draft_id": draft_id, "deleted": True}


@mcp.tool()
async def send_draft(mailbox: Mailbox, draft_id: str) -> Dict[str, Any]:
    """
    writes: True. Send an existing draft. Navigation Rule 3 -- the
    calling agent must confirm with the user before this is invoked.
    """
    svc = _service(mailbox)
    sent = svc.users().drafts().send(
        userId="me", body={"id": draft_id},
    ).execute()
    return {
        "mailbox": mailbox.value,
        "message_id": sent.get("id"),
        "thread_id": sent.get("threadId"),
        "label_ids": sent.get("labelIds", []),
    }


@mcp.tool()
async def send_message(request: SendRequest) -> Dict[str, Any]:
    """
    writes: True. Compose and send a message in one step. Navigation
    Rule 3 -- the calling agent must confirm with the user before this
    is invoked. Prefer create_draft + send_draft for review-first flows.
    """
    svc = _service(request.mailbox)
    raw = _build_rfc822(
        sender=_mailbox_email(request.mailbox),
        to=request.to,
        subject=request.subject,
        body=request.body,
        cc=request.cc,
        bcc=request.bcc,
    )
    body: Dict[str, Any] = {"raw": raw}
    if request.thread_id:
        body["threadId"] = request.thread_id
    sent = svc.users().messages().send(userId="me", body=body).execute()
    return {
        "mailbox": request.mailbox.value,
        "message_id": sent.get("id"),
        "thread_id": sent.get("threadId"),
        "label_ids": sent.get("labelIds", []),
    }


@mcp.tool()
async def create_reply_draft(request: ReplyRequest) -> Dict[str, Any]:
    """
    writes: True. Create a draft reply to an existing message, preserving
    thread and In-Reply-To / References headers.
    """
    svc = _service(request.mailbox)
    original = svc.users().messages().get(
        userId="me", id=request.message_id, format="metadata",
        metadataHeaders=["From", "To", "Cc", "Subject", "Message-ID", "References"],
    ).execute()
    headers = (original.get("payload", {}) or {}).get("headers", []) or []
    orig_from = _header(headers, "From") or ""
    orig_subject = _header(headers, "Subject") or ""
    orig_msg_id = _header(headers, "Message-ID") or ""
    orig_refs = _header(headers, "References") or ""

    subject = orig_subject if orig_subject.lower().startswith("re:") else f"Re: {orig_subject}"
    refs = f"{orig_refs} {orig_msg_id}".strip() if orig_refs else orig_msg_id

    raw = _build_rfc822(
        sender=_mailbox_email(request.mailbox),
        to=[orig_from],
        subject=subject,
        body=request.body,
        cc=request.cc,
        bcc=request.bcc,
        in_reply_to=orig_msg_id or None,
        references=refs or None,
    )
    draft = svc.users().drafts().create(
        userId="me",
        body={"message": {"raw": raw, "threadId": original.get("threadId")}},
    ).execute()
    return {
        "mailbox": request.mailbox.value,
        "draft_id": draft.get("id"),
        "message_id": (draft.get("message") or {}).get("id"),
        "thread_id": (draft.get("message") or {}).get("threadId"),
    }


@mcp.tool()
async def modify_labels(update: LabelUpdate) -> Dict[str, Any]:
    """
    writes: True. Add and/or remove labels on a message. Use for archive
    (remove INBOX), star (add STARRED), mark read (remove UNREAD), etc.
    """
    svc = _service(update.mailbox)
    resp = svc.users().messages().modify(
        userId="me",
        id=update.message_id,
        body={
            "addLabelIds": update.add_labels,
            "removeLabelIds": update.remove_labels,
        },
    ).execute()
    return {
        "mailbox": update.mailbox.value,
        "message_id": resp.get("id"),
        "label_ids": resp.get("labelIds", []),
    }


@mcp.tool()
async def trash_message(mailbox: Mailbox, message_id: str) -> Dict[str, Any]:
    """writes: True. Move a message to trash. Reversible via untrash."""
    svc = _service(mailbox)
    resp = svc.users().messages().trash(userId="me", id=message_id).execute()
    return {
        "mailbox": mailbox.value,
        "message_id": resp.get("id"),
        "label_ids": resp.get("labelIds", []),
    }


@mcp.tool()
async def untrash_message(mailbox: Mailbox, message_id: str) -> Dict[str, Any]:
    """writes: True. Restore a message from trash."""
    svc = _service(mailbox)
    resp = svc.users().messages().untrash(userId="me", id=message_id).execute()
    return {
        "mailbox": mailbox.value,
        "message_id": resp.get("id"),
        "label_ids": resp.get("labelIds", []),
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
