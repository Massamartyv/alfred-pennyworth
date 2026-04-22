#!/usr/bin/env python3
"""
Pinterest Board Organizer -- one-time reorganization tool.
Self-destructs after use.

Usage:
    python organizer.py --token <TOKEN> audit
    python organizer.py board <name_or_id>
    python organizer.py batch plan.json --dry-run
    python organizer.py destroy
"""

import argparse
import json
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("Missing dependency. Run: pip install requests")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

API_BASE = "https://api.pinterest.com/v5"
PAGE_SIZE = 25
RATE_LIMIT_RETRIES = 3
CASE_STUDY_DIR = Path(__file__).parent / "Case Study"


# ---------------------------------------------------------------------------
# API Client
# ---------------------------------------------------------------------------

class Pinterest:
    """Thin wrapper around Pinterest API v5 with pagination and rate limiting."""

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })
        self._board_cache: dict[str, dict] = {}

    # -- HTTP primitives ----------------------------------------------------

    def _call(self, method, path, params=None, body=None, retries=RATE_LIMIT_RETRIES):
        url = f"{API_BASE}{path}"
        for attempt in range(retries):
            r = self.session.request(method, url, params=params, json=body)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 5))
                print(f"  Rate limited. Waiting {wait}s...")
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json() if r.content else None
        raise RuntimeError(f"Rate limited {retries} times on {method} {path}")

    def _paginate(self, path, params=None):
        params = dict(params or {})
        params["page_size"] = PAGE_SIZE
        items = []
        while True:
            data = self._call("GET", path, params=params)
            items.extend(data.get("items", []))
            bookmark = data.get("bookmark")
            if not bookmark:
                break
            params["bookmark"] = bookmark
        return items

    # -- Board name resolution ----------------------------------------------

    def _load_board_cache(self):
        if not self._board_cache:
            for b in self._paginate("/boards"):
                self._board_cache[b["id"]] = b
        return self._board_cache

    def resolve_board(self, name_or_id: str) -> dict:
        """Accept a board ID or a case-insensitive name fragment. Return board dict."""
        cache = self._load_board_cache()
        if name_or_id in cache:
            return cache[name_or_id]
        matches = [
            b for b in cache.values()
            if name_or_id.lower() in b["name"].lower()
        ]
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            print(f"Ambiguous board name '{name_or_id}'. Matches:")
            for m in matches:
                print(f"  {m['id']}  {m['name']}")
            sys.exit(1)
        print(f"No board found matching '{name_or_id}'.")
        sys.exit(1)

    # -- Boards -------------------------------------------------------------

    def list_boards(self):
        return self._paginate("/boards")

    def get_board(self, board_id):
        return self._call("GET", f"/boards/{board_id}")

    def create_board(self, name, description="", privacy="PUBLIC"):
        return self._call("POST", "/boards", body={
            "name": name,
            "description": description,
            "privacy": privacy,
        })

    def update_board(self, board_id, **fields):
        return self._call("PATCH", f"/boards/{board_id}", body=fields)

    def delete_board(self, board_id):
        return self._call("DELETE", f"/boards/{board_id}")

    # -- Sections -----------------------------------------------------------

    def list_sections(self, board_id):
        return self._paginate(f"/boards/{board_id}/sections")

    def create_section(self, board_id, name):
        return self._call("POST", f"/boards/{board_id}/sections", body={"name": name})

    def update_section(self, board_id, section_id, name):
        return self._call("PATCH", f"/boards/{board_id}/sections/{section_id}", body={"name": name})

    def delete_section(self, board_id, section_id):
        return self._call("DELETE", f"/boards/{board_id}/sections/{section_id}")

    # -- Pins ---------------------------------------------------------------

    def list_board_pins(self, board_id):
        return self._paginate(f"/boards/{board_id}/pins")

    def list_section_pins(self, board_id, section_id):
        return self._paginate(f"/boards/{board_id}/sections/{section_id}/pins")

    def get_pin(self, pin_id):
        return self._call("GET", f"/pins/{pin_id}")

    def move_pin(self, pin_id, board_id, section_id=None):
        """Move pin to a different board/section via PATCH.

        Note: PATCH /pins is flagged as beta in Pinterest docs.
        If this fails with 403, the app may not have access yet.
        """
        body = {"board_id": board_id}
        if section_id:
            body["board_section_id"] = section_id
        return self._call("PATCH", f"/pins/{pin_id}", body=body)

    def save_pin(self, pin_id, board_id, section_id=None):
        """Save (copy) a pin to a board/section via the /save endpoint.
        Fallback for when PATCH /pins is unavailable.
        """
        body = {"board_id": board_id}
        if section_id:
            body["board_section_id"] = section_id
        return self._call("POST", f"/pins/{pin_id}/save", body=body)

    def delete_pin(self, pin_id):
        return self._call("DELETE", f"/pins/{pin_id}")

    # -- Audit --------------------------------------------------------------

    def full_audit(self):
        boards = self.list_boards()
        result = []
        for b in boards:
            bid = b["id"]
            sections = self.list_sections(bid)
            sec_info = []
            for s in sections:
                s_pins = self.list_section_pins(bid, s["id"])
                sec_info.append({
                    "id": s["id"],
                    "name": s.get("name") or s.get("title", ""),
                    "pin_count": len(s_pins),
                })
            result.append({
                "id": bid,
                "name": b["name"],
                "description": b.get("description", ""),
                "pin_count": b.get("pin_count", 0),
                "sections": sec_info,
            })
        return result

    def board_audit(self, board_id):
        board = self.get_board(board_id)
        all_pins = self.list_board_pins(board_id)
        sections = self.list_sections(board_id)

        def summarize(pin):
            return {
                "id": pin["id"],
                "title": pin.get("title", ""),
                "description": pin.get("description", ""),
                "link": pin.get("link", ""),
            }

        sec_details = []
        sectioned_ids = set()
        for s in sections:
            s_pins = self.list_section_pins(board_id, s["id"])
            for p in s_pins:
                sectioned_ids.add(p["id"])
            sec_details.append({
                "id": s["id"],
                "name": s.get("name") or s.get("title", ""),
                "pins": [summarize(p) for p in s_pins],
            })

        unsectioned = [summarize(p) for p in all_pins if p["id"] not in sectioned_ids]

        return {
            "id": board["id"],
            "name": board["name"],
            "description": board.get("description", ""),
            "unsectioned_pins": unsectioned,
            "sections": sec_details,
        }

    # -- Snapshots (case study) ---------------------------------------------

    def snapshot(self, label, scope="full", board_id=None):
        """Capture current state as a before/after snapshot for the case study.

        Args:
            label: Human-readable label, e.g. "before" or "after-wardrobe"
            scope: "full" for entire account, "board" for a single board
            board_id: Required when scope is "board"
        """
        CASE_STUDY_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        slug = label.lower().replace(" ", "-")

        if scope == "full":
            data = self.full_audit()
            filename = f"{timestamp}_{slug}_full.json"
            summary = _format_full_snapshot(data, label, timestamp)
        elif scope == "board" and board_id:
            data = self.board_audit(board_id)
            board_slug = data["name"].lower().replace(" ", "-")[:30]
            filename = f"{timestamp}_{slug}_{board_slug}.json"
            summary = _format_board_snapshot(data, label, timestamp)
        else:
            print("Snapshot error: board scope requires board_id.")
            return

        # Save raw JSON
        json_path = CASE_STUDY_DIR / filename
        with open(json_path, "w") as f:
            json.dump(data, f, indent=2)

        # Save formatted markdown
        md_path = CASE_STUDY_DIR / filename.replace(".json", ".md")
        with open(md_path, "w") as f:
            f.write(summary)

        print(f"  Snapshot saved: {md_path.name}")

    # -- Teardown -----------------------------------------------------------

    @staticmethod
    def self_destruct():
        """Remove tool files but preserve the Case Study folder."""
        target = Path(__file__).parent
        case_study = target / "Case Study"
        has_case_study = case_study.exists() and any(case_study.iterdir())

        if has_case_study:
            confirm = input(
                f"Delete tool files, keep Case Study folder in {target}? Type 'destroy': "
            )
        else:
            confirm = input(f"Permanently delete {target}? Type 'destroy': ")

        if confirm.strip().lower() != "destroy":
            print("Cancelled.")
            return False

        if has_case_study:
            # Remove everything except Case Study
            for item in target.iterdir():
                if item.name == "Case Study":
                    continue
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
            print("Tool files removed. Case Study preserved.")
            print(f"  {case_study}")
        else:
            shutil.rmtree(target)
            print("Pinterest Organizer removed.")
        return True

    @staticmethod
    def destroy_case_study():
        """Final cleanup -- remove the Case Study folder."""
        case_study = Path(__file__).parent / "Case Study"
        if not case_study.exists():
            # Script already gone, try the expected path
            case_study = Path.home() / "Alfred Pennyworth" / "Automations" / "Pinterest Organizer" / "Case Study"
        if not case_study.exists():
            print("No Case Study folder found.")
            return False
        confirm = input(f"Permanently delete {case_study}? Type 'destroy': ")
        if confirm.strip().lower() != "destroy":
            print("Cancelled.")
            return False
        parent = case_study.parent
        shutil.rmtree(case_study)
        # If the parent folder is now empty, remove it too
        if parent.exists() and not any(parent.iterdir()):
            parent.rmdir()
            print("Case Study and empty folder removed. Clean.")
        else:
            print("Case Study removed.")
        return True


# ---------------------------------------------------------------------------
# Snapshot formatters
# ---------------------------------------------------------------------------

def _format_full_snapshot(audit, label, timestamp):
    total = sum(b["pin_count"] for b in audit)
    lines = [
        f"# {label.upper()}",
        f"*{timestamp}*\n",
        f"{len(audit)} boards | {total} pins\n",
        "---\n",
    ]
    for b in sorted(audit, key=lambda x: x["name"].lower()):
        secs = b["sections"]
        lines.append(f"### {b['name']}")
        lines.append(f"{b['pin_count']} pins | {len(secs)} sections\n")
        if secs:
            for s in secs:
                lines.append(f"- {s['name']} ({s['pin_count']})")
            lines.append("")
    return "\n".join(lines)


def _format_board_snapshot(audit, label, timestamp):
    lines = [
        f"# {audit['name']} – {label.upper()}",
        f"*{timestamp}*\n",
        "---\n",
    ]
    unsectioned = audit.get("unsectioned_pins", [])
    if unsectioned:
        lines.append(f"### Unsectioned ({len(unsectioned)})\n")
        for p in unsectioned:
            title = p["title"] or "(untitled)"
            lines.append(f"- {title}")
        lines.append("")
    for s in audit.get("sections", []):
        lines.append(f"### {s['name']} ({len(s['pins'])})\n")
        for p in s["pins"]:
            title = p["title"] or "(untitled)"
            lines.append(f"- {title}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def show_audit(audit):
    total = sum(b["pin_count"] for b in audit)
    print(f"\n{'=' * 60}")
    print(f"  PINTEREST ACCOUNT AUDIT")
    print(f"  {len(audit)} boards  |  {total} pins")
    print(f"{'=' * 60}\n")

    for b in sorted(audit, key=lambda x: x["name"].lower()):
        secs = b["sections"]
        print(f"  {b['name']}")
        print(f"    {b['pin_count']} pins  |  {len(secs)} sections")
        for s in secs:
            print(f"      - {s['name']} ({s['pin_count']})")
        print()


def show_board(audit):
    print(f"\n{'=' * 60}")
    print(f"  BOARD: {audit['name']}")
    if audit["description"]:
        print(f"  {audit['description']}")
    print(f"{'=' * 60}\n")

    unsectioned = audit["unsectioned_pins"]
    if unsectioned:
        print(f"  Unsectioned ({len(unsectioned)}):")
        for p in unsectioned:
            title = p["title"] or "(untitled)"
            print(f"    - {title}")
            if p["link"]:
                print(f"      {p['link']}")
        print()

    for s in audit["sections"]:
        print(f"  [{s['name']}] ({len(s['pins'])} pins)")
        for p in s["pins"]:
            title = p["title"] or "(untitled)"
            print(f"    - {title}")
        print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(description="Pinterest Board Organizer")
    p.add_argument("--token", help="Access token (or set PINTEREST_TOKEN)")
    sub = p.add_subparsers(dest="cmd")

    # -- Audit
    sub.add_parser("audit", help="Full account overview")
    b = sub.add_parser("board", help="Detailed board audit")
    b.add_argument("board", help="Board ID or name")

    # -- Board CRUD
    cb = sub.add_parser("create-board", help="Create a board")
    cb.add_argument("name")
    cb.add_argument("--desc", default="")
    cb.add_argument("--privacy", default="PUBLIC", choices=["PUBLIC", "SECRET", "PROTECTED"])

    rb = sub.add_parser("rename-board", help="Rename a board")
    rb.add_argument("board", help="Board ID or name")
    rb.add_argument("new_name")

    db = sub.add_parser("delete-board", help="Delete a board")
    db.add_argument("board", help="Board ID or name")

    # -- Section CRUD
    cs = sub.add_parser("create-section", help="Add section to a board")
    cs.add_argument("board", help="Board ID or name")
    cs.add_argument("name")

    rs = sub.add_parser("rename-section", help="Rename a section")
    rs.add_argument("board", help="Board ID or name")
    rs.add_argument("section_id")
    rs.add_argument("new_name")

    ds = sub.add_parser("delete-section", help="Delete a section")
    ds.add_argument("board", help="Board ID or name")
    ds.add_argument("section_id")

    # -- Pin operations
    mv = sub.add_parser("move", help="Move a pin to board/section")
    mv.add_argument("pin_id")
    mv.add_argument("target_board", help="Target board ID or name")
    mv.add_argument("--section", help="Target section ID")

    bt = sub.add_parser("batch", help="Execute a JSON move plan")
    bt.add_argument("plan_file")
    bt.add_argument("--dry-run", action="store_true")

    dp = sub.add_parser("delete-pin", help="Delete a pin")
    dp.add_argument("pin_id")

    # -- Snapshots
    sn = sub.add_parser("snapshot", help="Capture state for case study")
    sn.add_argument("label", help="Label, e.g. 'before' or 'after-wardrobe'")
    sn.add_argument("--board", help="Board ID or name (omit for full account)")

    # -- Export
    ex = sub.add_parser("export", help="Export full audit to JSON")
    ex.add_argument("--output", default="pinterest-audit.json")

    # -- Teardown
    sub.add_parser("destroy", help="Remove tool, keep Case Study")
    sub.add_parser("destroy-case-study", help="Final cleanup of Case Study folder")

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()
        return

    # Teardown commands need no token
    if args.cmd == "destroy":
        Pinterest.self_destruct()
        return
    if args.cmd == "destroy-case-study":
        Pinterest.destroy_case_study()
        return

    token = getattr(args, "token", None) or os.environ.get("PINTEREST_TOKEN")
    if not token:
        print("Provide --token or set PINTEREST_TOKEN env var.")
        sys.exit(1)

    api = Pinterest(token)

    try:
        if args.cmd == "audit":
            show_audit(api.full_audit())

        elif args.cmd == "board":
            b = api.resolve_board(args.board)
            show_board(api.board_audit(b["id"]))

        elif args.cmd == "create-board":
            b = api.create_board(args.name, args.desc, args.privacy)
            print(f"Created: {b['name']}  (ID: {b['id']})")

        elif args.cmd == "rename-board":
            b = api.resolve_board(args.board)
            updated = api.update_board(b["id"], name=args.new_name)
            print(f"Renamed to: {updated['name']}")

        elif args.cmd == "delete-board":
            b = api.resolve_board(args.board)
            confirm = input(f"Delete '{b['name']}'? Type 'yes': ")
            if confirm.strip().lower() == "yes":
                api.delete_board(b["id"])
                print("Deleted.")
            else:
                print("Cancelled.")

        elif args.cmd == "create-section":
            b = api.resolve_board(args.board)
            s = api.create_section(b["id"], args.name)
            name = s.get("name") or s.get("title", "")
            print(f"Created section: {name}  (ID: {s['id']})")

        elif args.cmd == "rename-section":
            b = api.resolve_board(args.board)
            api.update_section(b["id"], args.section_id, args.new_name)
            print(f"Renamed section to: {args.new_name}")

        elif args.cmd == "delete-section":
            b = api.resolve_board(args.board)
            confirm = input(f"Delete section {args.section_id}? Type 'yes': ")
            if confirm.strip().lower() == "yes":
                api.delete_section(b["id"], args.section_id)
                print("Deleted.")
            else:
                print("Cancelled.")

        elif args.cmd == "move":
            b = api.resolve_board(args.target_board)
            try:
                api.move_pin(args.pin_id, b["id"], args.section)
                print(f"Moved pin {args.pin_id} to {b['name']}")
            except requests.exceptions.HTTPError as e:
                if e.response is not None and e.response.status_code == 403:
                    print("PATCH /pins is in beta and may not be enabled for this app.")
                    print("Attempting save-and-delete fallback...")
                    api.save_pin(args.pin_id, b["id"], args.section)
                    api.delete_pin(args.pin_id)
                    print(f"Moved pin {args.pin_id} to {b['name']} (via save + delete)")
                else:
                    raise

        elif args.cmd == "batch":
            with open(args.plan_file) as f:
                plan = json.load(f)
            moves = plan if isinstance(plan, list) else plan.get("moves", [])
            total = len(moves)

            if args.dry_run:
                print(f"Dry run: {total} moves")
                for m in moves[:15]:
                    note = f"  ({m['note']})" if m.get("note") else ""
                    sec = f" -> section {m['section_id']}" if m.get("section_id") else ""
                    print(f"  pin {m['pin_id']} -> board {m['board_id']}{sec}{note}")
                if total > 15:
                    print(f"  ... and {total - 15} more")
                return

            success, errors = 0, []
            use_fallback = False

            for i, m in enumerate(moves, 1):
                pid = m["pin_id"]
                bid = m["board_id"]
                sid = m.get("section_id")
                try:
                    if use_fallback:
                        api.save_pin(pid, bid, sid)
                        api.delete_pin(pid)
                    else:
                        try:
                            api.move_pin(pid, bid, sid)
                        except requests.exceptions.HTTPError as e:
                            if e.response is not None and e.response.status_code == 403 and not use_fallback:
                                print("  PATCH unavailable. Switching to save + delete fallback.")
                                use_fallback = True
                                api.save_pin(pid, bid, sid)
                                api.delete_pin(pid)
                            else:
                                raise
                    success += 1
                    note = f"  ({m['note']})" if m.get("note") else ""
                    print(f"  [{i}/{total}] {pid}{note}")
                except Exception as e:
                    errors.append({"move": m, "error": str(e)})
                    print(f"  [{i}/{total}] FAILED {pid}: {e}")

            print(f"\nDone. {success}/{total} moved.")
            if errors:
                err_path = args.plan_file.replace(".json", "-errors.json")
                with open(err_path, "w") as f:
                    json.dump(errors, f, indent=2)
                print(f"Errors: {err_path}")

        elif args.cmd == "delete-pin":
            confirm = input(f"Delete pin {args.pin_id}? Type 'yes': ")
            if confirm.strip().lower() == "yes":
                api.delete_pin(args.pin_id)
                print("Deleted.")
            else:
                print("Cancelled.")

        elif args.cmd == "snapshot":
            if args.board:
                b = api.resolve_board(args.board)
                api.snapshot(args.label, scope="board", board_id=b["id"])
            else:
                api.snapshot(args.label, scope="full")

        elif args.cmd == "export":
            audit = api.full_audit()
            with open(args.output, "w") as f:
                json.dump(audit, f, indent=2)
            print(f"Exported to {args.output}")

    except requests.exceptions.HTTPError as e:
        print(f"API error: {e}")
        if hasattr(e, "response") and e.response is not None:
            try:
                detail = e.response.json()
                print(f"  {json.dumps(detail, indent=2)}")
            except Exception:
                print(f"  {e.response.text}")
        sys.exit(1)


if __name__ == "__main__":
    main()
