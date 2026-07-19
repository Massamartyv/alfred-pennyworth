#!/usr/bin/env python3
"""Upload a local image to Notion and set it as a page icon.

Usage: python3 upload_icon.py --page <page_id> --file <path/to/image.png>

Requires NOTION_PERSONAL_TOKEN in the environment (sourced from the repo
.env by direnv or the calling shell). The token value is never printed.
The integration must be connected to the target page's database.
"""
import argparse
import json
import mimetypes
import os
import sys
import urllib.request
import uuid

API = "https://api.notion.com/v1"
VERSION = "2022-06-28"


def req(url, data=None, headers=None, method=None):
    r = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(r) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"Notion API error {e.code} on {url}: {e.read().decode()}")


def main():
    ap = argparse.ArgumentParser(description="Set a Notion page icon from a local image.")
    ap.add_argument("--page", required=True, help="Target page ID, with or without dashes")
    ap.add_argument("--file", required=True, help="Path to the image file")
    args = ap.parse_args()

    token = os.environ.get("NOTION_PERSONAL_TOKEN")
    if not token:
        sys.exit("NOTION_PERSONAL_TOKEN is not set. Add it to .env per Manual/secrets-inventory.md.")

    filename = os.path.basename(args.file)
    ctype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    auth = {"Authorization": f"Bearer {token}", "Notion-Version": VERSION}

    created = req(
        f"{API}/file_uploads",
        data=json.dumps({"filename": filename, "content_type": ctype}).encode(),
        headers={**auth, "Content-Type": "application/json"},
        method="POST",
    )
    upload_id = created["id"]
    upload_url = created.get("upload_url") or f"{API}/file_uploads/{upload_id}/send"

    boundary = uuid.uuid4().hex
    with open(args.file, "rb") as f:
        file_bytes = f.read()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: {ctype}\r\n\r\n"
    ).encode() + file_bytes + f"\r\n--{boundary}--\r\n".encode()
    req(
        upload_url,
        data=body,
        headers={**auth, "Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )

    page_id = args.page.replace("-", "")
    req(
        f"{API}/pages/{page_id}",
        data=json.dumps({"icon": {"type": "file_upload", "file_upload": {"id": upload_id}}}).encode(),
        headers={**auth, "Content-Type": "application/json"},
        method="PATCH",
    )

    print(f"Icon set on page {args.page} from {filename} (upload {upload_id}).")


if __name__ == "__main__":
    main()
