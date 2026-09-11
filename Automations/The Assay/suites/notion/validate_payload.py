#!/usr/bin/env python3
"""The Assay - Suite Three: Notion write payload validator.

Schema-correctness validation on a captured write payload - the shape a
call to notion-create-pages / API-post-page would carry - against the
house Notion conventions in memory/notion.md and
memory/notion_formatting_framework.md. Deterministic, no model call, no
live workspace touched: every fixture here is a captured JSON payload, not
a real API call. A live-workspace adapter is out of scope by the operation
brief; this validates shape, not whether the target page or database
actually exists.

Five checkable classes of malformed write, each with a clean deterministic
verifier:

  A. property-type   - multi_select/relation value is not the JSON-array-
                        string shape the enhanced connector requires.
  B. icon             - icon is an emoji, or a URL that does not match the
                        built-in Notion icon set pattern, or names an icon
                        confirmed NOT to exist in that set.
  C. heading-level     - body content uses H1 or H2 instead of H3-only.
  D. link-protocol     - a Link/URL property stores the protocol instead of
                        the bare domain.
  E. missing-required  - a database that requires a Sphere relation
                        (per "Resource databases live in the sphere") has
                        no Sphere property, or no template_id is set.

Usage: validate_payload.py <payload.json> [<payload.json> ...]
Prints one PASS/FAIL line per payload and per violation found. Exit 0 if
every payload's violations matched its own fixture's expected_violations
list (fixtures self-declare what they should trip, so this file doubles as
its own test suite), exit 1 otherwise.
"""

import json
import re
import sys

# Names confirmed present in the built-in Notion icon set, per
# memory/notion.md. Any other {name} in an icons.notion.so URL is either an
# unconfirmed guess or one of the four names confirmed NOT to exist.
KNOWN_ICON_NAMES = {
    "robot", "calendar", "calendar-day", "help-alternate", "person-masculine",
    "person-feminine", "user-circle-filled", "graduate", "government", "home",
    "leaf", "book", "microphone", "compass", "cash", "credit-card", "run",
    "skull-profile", "paste", "medication", "tooth", "orbit", "view",
    "checkmark", "folder", "tag", "poo", "heart", "heart-rate", "briefcase",
    "flag", "target", "hammer", "globe", "upward", "downward", "backward",
    "pencil", "username", "report",
}
CONFIRMED_MISSING_ICON_NAMES = {"brush", "palette", "paintbrush", "brush-alternate"}

ICON_URL_RE = re.compile(r"^https://www\.notion\.so/icons/([a-z-]+)_([a-z]+)\.svg$")
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]"
)
HEADING_RE = re.compile(r"^(#{1,2})\s", re.MULTILINE)
PROTOCOL_RE = re.compile(r"^https?://")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Databases where a missing Sphere relation is a defect, per the house rule
# that every task, project, note and resource relates back to a sphere.
SPHERE_REQUIRED_DATABASES = {"Tasks", "Projects", "Resources", "Annotations"}


def check_property_types(payload, violations):
    props = payload.get("properties", {})
    for name, prop in props.items():
        ptype = prop.get("type")
        value = prop.get("value")
        if ptype in ("multi_select", "relation"):
            if not isinstance(value, str):
                violations.append(("property-type", f"{name}: {ptype} value must be a JSON array string, got {type(value).__name__}"))
                continue
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                violations.append(("property-type", f"{name}: {ptype} value '{value}' is not valid JSON - expected a JSON array string per the enhanced-connector convention"))
                continue
            if not isinstance(parsed, list):
                violations.append(("property-type", f"{name}: {ptype} value parses to {type(parsed).__name__}, not a list"))
        if ptype == "date" and value is not None:
            if not isinstance(value, str) or not DATE_RE.match(value):
                violations.append(("property-type", f"{name}: date value '{value}' is not ISO YYYY-MM-DD"))


def check_icon(payload, violations):
    icon = payload.get("icon")
    if icon is None:
        return
    if EMOJI_RE.search(icon):
        violations.append(("icon", f"icon '{icon}' is an emoji - built-in Notion icon set only, never emojis"))
        return
    m = ICON_URL_RE.match(icon)
    if not m:
        violations.append(("icon", f"icon '{icon}' does not match the built-in icon URL pattern https://www.notion.so/icons/{{name}}_{{color}}.svg"))
        return
    name = m.group(1)
    if name in CONFIRMED_MISSING_ICON_NAMES:
        violations.append(("icon", f"icon name '{name}' is confirmed NOT to exist in the built-in set"))
    elif name not in KNOWN_ICON_NAMES:
        violations.append(("icon", f"icon name '{name}' is not in the confirmed-existing set - verify before shipping"))


def check_headings(payload, violations):
    body = payload.get("body_markdown", "")
    for m in HEADING_RE.finditer(body):
        violations.append(("heading-level", f"body uses {m.group(1)} heading - H3 only, never H1 or H2"))


def check_link_protocol(payload, violations):
    props = payload.get("properties", {})
    for name, prop in props.items():
        if prop.get("type") == "url":
            value = prop.get("value", "")
            if isinstance(value, str) and PROTOCOL_RE.match(value):
                violations.append(("link-protocol", f"{name}: '{value}' stores the protocol - Link/URL properties carry the bare domain only"))


def check_missing_required(payload, violations):
    db = payload.get("target_database")
    props = payload.get("properties", {})
    if db in SPHERE_REQUIRED_DATABASES:
        sphere = props.get("Sphere")
        if sphere is None or not sphere.get("value"):
            violations.append(("missing-required", f"{db} entry has no Sphere relation - every entry relates back to a sphere"))
    if not payload.get("template_id"):
        violations.append(("missing-required", "no template_id set - templates first, do not build content from scratch when a template exists"))


CHECKS = [check_property_types, check_icon, check_headings, check_link_protocol, check_missing_required]


def validate(payload):
    violations = []
    for check in CHECKS:
        check(payload, violations)
    return violations


def main():
    paths = sys.argv[1:]
    if not paths:
        print("usage: validate_payload.py <payload.json> [...]", file=sys.stderr)
        return 2

    total = 0
    correct = 0
    classes_caught = set()

    for path in paths:
        total += 1
        with open(path) as f:
            fixture = json.load(f)

        payload = fixture.get("payload", fixture)
        expected = set(fixture.get("expected_violation_classes", []))

        violations = validate(payload)
        found_classes = {v[0] for v in violations}
        classes_caught |= found_classes

        if found_classes == expected:
            correct += 1
            status = "PASS"
        else:
            status = "FAIL"

        print(f"{status}  {path}")
        print(f"      expected classes: {sorted(expected) or ['none']}")
        print(f"      found classes:    {sorted(found_classes) or ['none']}")
        for cls, detail in violations:
            print(f"      - {cls}: {detail}")

    print(f"malformed classes demonstrably caught across fixture set: {sorted(c for c in classes_caught if c)}")
    rate = correct / total if total else 0.0
    print(f"SCALAR: {correct}/{total} ({rate:.2f})")

    return 0 if correct == total else 1


if __name__ == "__main__":
    sys.exit(main())
