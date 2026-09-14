#!/usr/bin/env python3
"""The Understudy - carries the local Reference Library corpus into its Notion mirror.

The markdown corpus at Context/Reference Library/ is canonical. Notion is the
reading and capture surface. This script pushes the corpus into Notion and
reports anything captured in Notion that has no card on disk yet.

  --check     report drift, write nothing (default)
  --push      create missing rows, patch changed properties
  --bodies    with --push, also rewrite page bodies
  --harvest   list Notion rows with no card on disk

Requires NOTION_PERSONAL_TOKEN in ~/Alfred Pennyworth/.env
"""
import argparse, json, os, re, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vocabulary as V

ROOT = os.path.expanduser("~/Alfred Pennyworth/Context/Reference Library")
ENV = os.path.expanduser("~/Alfred Pennyworth/.env")
DB_ID = "3db18961-65cf-8090-94a9-e363cd486c8f"
DS_ID = "3db18961-65cf-80f3-9e33-000b674e0373"
SPHERE_DS = "4d195180-7fd5-4b7d-a407-2e1a44124002"
API, VERSION = "https://api.notion.com/v1", "2025-09-03"

TYPE_LABEL = {"creator": "Creator", "brand": "Brand", "work": "Work",
              "curator": "Curator", "anti-reference": "Anti-Reference"}
STATUS_LABEL = {"canon": "Canon", "active": "Active", "watch": "Watch",
                "defunct": "Defunct", "card-pending": "Card pending"}
ICON = {"creator": "user-circle-filled", "brand": "briefcase", "work": "book",
        "curator": "compass", "anti-reference": "flag"}
EXTRACTION = {"creator": "The formula", "brand": "The proposition",
              "work": "Why it lands", "curator": "The filter"}


def token():
    for line in open(ENV):
        if line.strip().startswith("NOTION_PERSONAL_TOKEN"):
            return line.split("=", 1)[1].strip().strip('"\'')
    sys.exit(f"NOTION_PERSONAL_TOKEN not found in {ENV}")


TOKEN = token()


def call(method, path, body=None):
    req = urllib.request.Request(
        API + path, data=json.dumps(body).encode() if body is not None else None,
        method=method, headers={"Authorization": f"Bearer {TOKEN}",
                                "Notion-Version": VERSION,
                                "Content-Type": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            payload = e.read().decode()
            if e.code in (429, 502, 503, 504) and attempt < 4:
                time.sleep(2 ** attempt); continue
            raise SystemExit(f"{method} {path} -> {e.code}\n{payload}")


def paged(path, body):
    cursor, rows = None, []
    while True:
        b = dict(body)
        if cursor:
            b["start_cursor"] = cursor
        r = call("POST", path, b)
        rows += r["results"]
        if not r.get("has_more"):
            return rows
        cursor = r["next_cursor"]


# ---------- reading the corpus ----------

def fm_value(fm, key):
    m = re.search(rf'^{key}:\s*(.*)$', fm, re.M)
    return m.group(1).strip() if m else ""


def listify(raw):
    raw = raw.strip()
    if raw.startswith("["):
        raw = raw[1:-1] if raw.endswith("]") else raw[1:]
    return [x.strip().strip('"\'') for x in raw.split(",") if x.strip()]


def read_corpus():
    cards = []
    for d, _, fs in os.walk(ROOT):
        for f in sorted(fs):
            if not f.endswith(".md") or f == "_index.md":
                continue
            path = os.path.join(d, f)
            txt = open(path).read()
            fm = re.match(r'^---\n(.*?)\n---\n', txt, re.S).group(1)
            body = txt[txt.index("\n---\n", 3) + 5:]
            ctype = fm_value(fm, "type")

            def section(label):
                m = re.search(rf'^\*\*{re.escape(label)}\*\*\s*[–-]\s*(.+?)(?=\n\n\*\*|\Z)',
                              body, re.M | re.S)
                return m.group(1).strip() if m else ""

            title = re.search(r'^# (.+)$', body, re.M)
            cards.append({
                "file": os.path.relpath(path, ROOT),
                "title": title.group(1).strip() if title else fm_value(fm, "name"),
                "type": ctype,
                "status": fm_value(fm, "status"),
                "added": fm_value(fm, "added"),
                "spheres": listify(fm_value(fm, "spheres")),
                "domains": listify(fm_value(fm, "domains")),
                "pull_for": listify(fm_value(fm, "pull_for")),
                "themes": listify(fm_value(fm, "themes")),
                "links": listify(fm_value(fm, "links")),
                "identity": section("Who") or section("What"),
                "why_aligned": section("Why aligned"),
                "extraction_label": EXTRACTION[ctype],
                "extraction": section(EXTRACTION[ctype]),
                "canon": section("Canon"),
                "provenance": section("Provenance"),
                "pull_for_original": section("Pull for").rstrip("."),
            })
    return cards


# ---------- block building ----------

def rich(text):
    out = []
    for tok in re.split(r'(\*\*.+?\*\*|\*[^*]+?\*)', text):
        if not tok:
            continue
        ann = {"bold": False, "italic": False}
        if tok.startswith("**") and tok.endswith("**"):
            content, ann["bold"] = tok[2:-2], True
        elif tok.startswith("*") and tok.endswith("*"):
            content, ann["italic"] = tok[1:-1], True
        else:
            content = tok
        for i in range(0, len(content), 1900):
            out.append({"type": "text", "text": {"content": content[i:i + 1900]},
                        "annotations": ann})
    return out


def para(t):
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rich(t)}}


def h3(t):
    return {"object": "block", "type": "heading_3",
            "heading_3": {"rich_text": [{"type": "text", "text": {"content": t}}]}}


def body_blocks(c):
    b = [para(c["identity"])]
    if c["why_aligned"]:
        b += [h3("Why aligned"), para(c["why_aligned"])]
    b += [h3(c["extraction_label"]), para(c["extraction"]),
          h3("Canon"), para(c["canon"])]
    if c["provenance"]:
        b += [h3("Provenance"), para(c["provenance"])]
    if c["pull_for_original"]:
        b.append({"object": "block", "type": "toggle", "toggle": {
            "rich_text": [{"type": "text", "text": {"content": "Original pull-for"}}],
            "children": [para(c["pull_for_original"])]}})
    return b


def bare_domain(u):
    return re.sub(r'^https?://(www\.)?', '', u).rstrip('/')


def props_for(c, spheres):
    p = {
        "Name": {"title": [{"text": {"content": c["title"]}}]},
        "Type": {"select": {"name": TYPE_LABEL[c["type"]]}},
        "Status": {"select": {"name": STATUS_LABEL[c["status"]]}},
        "Sphere": {"relation": [{"id": spheres[s]} for s in c["spheres"]]},
        "Pull for": {"multi_select": [{"name": x} for x in c["pull_for"]]},
        "Themes": {"multi_select": [{"name": x} for x in c["themes"]]},
        "Domains": {"multi_select": [{"name": x} for x in c["domains"]]},
        "Card": {"rich_text": [{"text": {"content": c["file"]}}]},
    }
    if c["added"]:
        p["Added"] = {"date": {"start": c["added"]}}
    if c["links"]:
        p["Link"] = {"url": bare_domain(c["links"][0])}
    return p


def live_values(row):
    p = row["properties"]
    return {
        "title": "".join(t["plain_text"] for t in p["Name"]["title"]),
        "type": (p["Type"]["select"] or {}).get("name"),
        "status": (p["Status"]["select"] or {}).get("name"),
        "spheres": {r["id"] for r in p["Sphere"]["relation"]},
        "pull_for": {o["name"] for o in p["Pull for"]["multi_select"]},
        "themes": {o["name"] for o in p["Themes"]["multi_select"]},
        "domains": {o["name"] for o in p["Domains"]["multi_select"]},
        "added": (p["Added"]["date"] or {}).get("start"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--bodies", action="store_true")
    ap.add_argument("--harvest", action="store_true")
    args = ap.parse_args()

    cards = {c["file"]: c for c in read_corpus()}
    spheres = {}
    for row in paged(f"/data_sources/{SPHERE_DS}/query", {"page_size": 100}):
        spheres["".join(t["plain_text"] for t in row["properties"]["Name"]["title"]).strip()] = row["id"]

    rows, by_card, orphans = paged(f"/data_sources/{DS_ID}/query", {"page_size": 100}), {}, []
    for r in rows:
        rt = r["properties"].get("Card", {}).get("rich_text") or []
        path = "".join(t["plain_text"] for t in rt)
        (by_card.setdefault(path, r) if path else orphans.append(r))

    missing = [f for f in cards if f not in by_card]
    deleted = [f for f in by_card if f not in cards]
    drifted = []
    for f, c in cards.items():
        if f not in by_card:
            continue
        got, want = live_values(by_card[f]), c
        if (got["title"] != want["title"]
                or got["type"] != TYPE_LABEL[want["type"]]
                or got["status"] != STATUS_LABEL[want["status"]]
                or got["spheres"] != {spheres[s] for s in want["spheres"] if s in spheres}
                or got["pull_for"] != set(want["pull_for"])
                or got["themes"] != set(want["themes"])
                or got["domains"] != set(want["domains"])
                or (want["added"] and got["added"] != want["added"])):
            drifted.append(f)

    print(f"corpus: {len(cards)} cards | Notion: {len(rows)} rows")
    print(f"missing in Notion: {len(missing)} | property drift: {len(drifted)} "
          f"| rows with no card: {len(deleted)} | captured in Notion only: {len(orphans)}")

    if args.harvest or orphans:
        for r in orphans:
            name = "".join(t["plain_text"] for t in r["properties"]["Name"]["title"])
            st = (r["properties"]["Status"]["select"] or {}).get("name")
            print(f"  HARVEST  {name!r} [{st}] {r['url']}")
    for f in deleted:
        print(f"  NO CARD  {f} -> {by_card[f]['url']}")

    if not args.push:
        if missing or drifted:
            print("\nrun with --push to write")
        return

    for f in missing:
        c = cards[f]
        call("POST", "/pages", {
            "parent": {"type": "database_id", "database_id": DB_ID},
            "icon": {"type": "external", "external": {
                "url": f"https://www.notion.so/icons/{ICON[c['type']]}_lightgray.svg"}},
            "properties": props_for(c, spheres), "children": body_blocks(c)})
        print(f"  created  {f}")
        time.sleep(0.34)

    for f in drifted:
        call("PATCH", f"/pages/{by_card[f]['id']}", {"properties": props_for(cards[f], spheres)})
        print(f"  patched  {f}")
        time.sleep(0.34)

    if args.bodies:
        for f, c in cards.items():
            row = by_card.get(f)
            if not row:
                continue
            for b in call("GET", f"/blocks/{row['id']}/children?page_size=100")["results"]:
                call("DELETE", f"/blocks/{b['id']}")
                time.sleep(0.34)
            call("PATCH", f"/blocks/{row['id']}/children", {"children": body_blocks(c)})
            print(f"  body     {f}")
            time.sleep(0.34)


if __name__ == "__main__":
    main()
