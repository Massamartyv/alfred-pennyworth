#!/bin/bash
# The Assay - Suite Two judge.
#
# One trigger judgment, one process. Given a skill's frontmatter description
# and a candidate prompt, asks a cheap model whether the router would load
# that skill for that prompt - the same question ui-ux-pro-max's own eval
# notes describe: "Judge each prompt against the SKILL.md frontmatter
# description only: would the router load this skill?"
#
# Run from a neutral, empty working directory rather than the project root.
# Invoking `claude -p` from inside this repo loads the full CLAUDE.md boot
# sequence and every routing file it points to before the model ever sees
# the judge question - that is not a fixed cost, and it is not what the
# real router evaluates when it matches a prompt against a description. A
# neutral cwd keeps every judge call the same small shape.
#
# Usage: judge.sh <description-file> <prompt>
# Prints exactly TRIGGER or SKIP on stdout. Exits 1 if the model produced
# neither (a refusal-shaped result at the level of one query, not the
# suite - the caller counts this as a miss, not a crash).

set -uo pipefail

description_file="$1"
prompt="$2"

[ -f "$description_file" ] || { echo "ERROR: no description file at $description_file" >&2; exit 2; }
description=$(cat "$description_file")

neutral_cwd=$(mktemp -d "${TMPDIR:-/tmp}/assay-judge.XXXXXX")
trap 'rm -rf "$neutral_cwd"' EXIT

judge_prompt="You are simulating a skill router. Given exactly one skill's frontmatter description and one user query, decide whether that skill's router would load it for this query - nothing else, no other skills to compare against, no execution of the skill itself.

Skill description:
${description}

User query:
${prompt}

Reply with exactly one word: TRIGGER if the router would load this skill for this query, SKIP if it would not."

verdict=$(cd "$neutral_cwd" && claude -p "$judge_prompt" --model haiku 2>/dev/null | tr -d '[:space:]' | tr '[:lower:]' '[:upper:]')

case "$verdict" in
  *TRIGGER*) echo "TRIGGER"; exit 0 ;;
  *SKIP*) echo "SKIP"; exit 0 ;;
  *) echo "UNRESOLVED"; exit 1 ;;
esac
