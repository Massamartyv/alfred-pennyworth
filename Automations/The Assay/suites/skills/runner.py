#!/usr/bin/env python3
"""The Assay - Suite Two runner: trigger accuracy across the registered skills.

Reads registry.txt, reads each skill's evals/evals.json against the unified
schema documented in schema.md, extracts each skill's SKILL.md frontmatter
description, and judges every declared query with a single cheap model call
per query via judge.sh. This is the one suite in the harness that is
model-judged rather than deterministic - it has a fixed-cost budget in two
dimensions: a per-skill query ceiling (the turn budget) and the wall-clock
timeout the outer harness enforces on the whole suite process.

Refusal is a valid outcome. If the `claude` CLI is not on PATH, there is no
verifier available in this environment and the suite reports unscoreable
(exit 3) rather than inventing a number. If an individual skill's eval file
is missing or malformed, that skill is skipped with a warning and excluded
from the scalar - the suite does not fail outright for one bad file, but if
every skill ends up excluded the whole suite is unscoreable.

Exit codes: 0 pass (overall accuracy >= PASS_THRESHOLD), 1 fail (ran, scored
below threshold), 3 unscoreable (no verifier available or nothing to score).
"""

import json
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

HOME = os.path.dirname(os.path.abspath(__file__))
JUDGE = os.path.join(HOME, "judge.sh")
REGISTRY = os.path.join(HOME, "registry.txt")

# Fixed-cost knobs. PER_SKILL_QUERY_CAP is the turn ceiling the operation
# brief asks a model-judged suite to declare - a skill whose eval file grows
# past this is truncated deterministically (first N should_trigger, first N
# should_not_trigger), not silently run in full. WORKERS bounds concurrent
# `claude -p` subprocesses so cost per run stays predictable regardless of
# how many skills are registered. PASS_THRESHOLD is a provisional bar - see
# schema.md and the handoff for why 0.80, and the note that it should be
# revisited once real fire telemetry exists.
PER_SKILL_QUERY_CAP = 20
WORKERS = 6
PASS_THRESHOLD = 0.80
JUDGE_TIMEOUT_S = 30


def read_registry():
    rows = []
    with open(REGISTRY) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            name, path = line.split(":", 1)
            rows.append((name.strip(), path.strip()))
    return rows


def extract_description(skill_home):
    skill_md = os.path.join(skill_home, "SKILL.md")
    if not os.path.isfile(skill_md):
        return None
    in_frontmatter = 0
    with open(skill_md) as f:
        for line in f:
            if line.strip() == "---":
                in_frontmatter += 1
                if in_frontmatter == 2:
                    break
                continue
            if in_frontmatter == 1 and line.startswith("description:"):
                desc = line[len("description:"):].strip()
                if desc.startswith('"') and desc.endswith('"') and len(desc) > 1:
                    desc = desc[1:-1]
                return desc
    return None


def load_evals(skill_home):
    path = os.path.join(skill_home, "evals", "evals.json")
    if not os.path.isfile(path):
        return None, f"no evals.json at {path}"
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return None, f"malformed JSON in {path}: {e}"
    if data.get("eval_type") != "trigger":
        return None, f"{path} is not eval_type trigger (unified schema violation)"
    return data, None


def build_worklist(skill, data):
    work = []
    trig = data.get("queries", {}).get("should_trigger", [])[:PER_SKILL_QUERY_CAP]
    skip = data.get("queries", {}).get("should_not_trigger", [])[:PER_SKILL_QUERY_CAP]
    for q in trig:
        work.append((skill, "TRIGGER", q["prompt"]))
    for q in skip:
        work.append((skill, "SKIP", q["prompt"]))
    return work


def judge_one(desc_file, item):
    skill, expected, prompt = item
    try:
        out = subprocess.run(
            [JUDGE, desc_file, prompt],
            capture_output=True, text=True, timeout=JUDGE_TIMEOUT_S,
        )
        actual = out.stdout.strip() or "UNRESOLVED"
    except subprocess.TimeoutExpired:
        actual = "TIMEOUT"
    match = 1 if actual == expected else 0
    return (skill, expected, actual, match, prompt)


def main():
    target = None
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            target = arg

    if shutil.which("claude") is None:
        print("SCALAR: unscoreable")
        print("no `claude` CLI on PATH - no verifier available for trigger judgment in this environment")
        return 3

    if not os.path.isfile(REGISTRY):
        print("SCALAR: unscoreable")
        print(f"no registry at {REGISTRY}")
        return 3

    rows = read_registry()
    if target:
        rows = [r for r in rows if r[0] == target]
        if not rows:
            print("SCALAR: unscoreable")
            print(f"no skill named '{target}' in registry")
            return 3

    worklist = []
    desc_files = {}
    skipped_skills = []
    tmp_dir = os.path.join(HOME, ".desc-cache")
    os.makedirs(tmp_dir, exist_ok=True)

    for skill, skill_home in rows:
        desc = extract_description(skill_home)
        if desc is None:
            skipped_skills.append((skill, "no SKILL.md description found"))
            continue
        data, err = load_evals(skill_home)
        if err:
            skipped_skills.append((skill, err))
            continue
        desc_file = os.path.join(tmp_dir, f"{skill}.desc")
        with open(desc_file, "w") as f:
            f.write(desc)
        desc_files[skill] = desc_file
        worklist.extend(build_worklist(skill, data))

    for skill, reason in skipped_skills:
        print(f"WARN  {skill} - excluded: {reason}")

    if not worklist:
        print("SCALAR: unscoreable")
        print("no skill in the registry produced a scoreable eval set")
        shutil.rmtree(tmp_dir, ignore_errors=True)
        return 3

    results = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [
            pool.submit(judge_one, desc_files[item[0]], item)
            for item in worklist
        ]
        for fut in as_completed(futures):
            results.append(fut.result())

    shutil.rmtree(tmp_dir, ignore_errors=True)

    per_skill = {}
    for skill, expected, actual, match, prompt in results:
        per_skill.setdefault(skill, {"pass": 0, "total": 0, "misses": []})
        per_skill[skill]["total"] += 1
        if match:
            per_skill[skill]["pass"] += 1
        else:
            per_skill[skill]["misses"].append((expected, actual, prompt))

    total_pass = sum(v["pass"] for v in per_skill.values())
    total_all = sum(v["total"] for v in per_skill.values())

    for skill in sorted(per_skill):
        v = per_skill[skill]
        rate = v["pass"] / v["total"] if v["total"] else 0.0
        print(f"skill {skill}: {v['pass']}/{v['total']} ({rate:.2f})")
        for expected, actual, prompt in v["misses"]:
            print(f"  MISS  expected {expected}, got {actual} - \"{prompt}\"")

    overall_rate = total_pass / total_all if total_all else 0.0
    print(f"SCALAR: {total_pass}/{total_all} ({overall_rate:.2f})")

    if overall_rate >= PASS_THRESHOLD:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
