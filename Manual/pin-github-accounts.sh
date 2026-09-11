#!/usr/bin/env bash
# Pin each local GitHub clone to the gh account that owns it.
#
# Why: gh's git credential helper only ever serves the ACTIVE gh account.
# With studio-fivepoints active (the default, for the Five Points repos),
# every fetch or push to a private Massamartyv repo fails with
# "Repository not found", and the reverse happens if Massamartyv is active.
#
# Fix: a repo-local credential helper that asks gh for the owning account's
# token by name at the moment git needs it. Nothing secret is written to
# disk; the token stays in gh's keyring. Repo-local config does not survive
# a fresh clone, so rerun this after every clone (see Manual/genesis.md).
#
# Usage:
#   Manual/pin-github-accounts.sh            # discover and pin every clone in the estate
#   Manual/pin-github-accounts.sh REPO...    # pin only the given clones
#
# Idempotent. Repos owned by accounts not signed in to gh (client repos) are skipped.

set -uo pipefail

GH="$(command -v gh || echo /opt/homebrew/bin/gh)"
ESTATE=("$HOME/.claude" "$HOME/Alfred Pennyworth")

accounts="$("$GH" auth status 2>&1 | sed -nE 's/.*Logged in to github\.com account ([^ ]+).*/\1/p')"
if [ -z "$accounts" ]; then
  echo "No gh accounts signed in. Run: gh auth login" >&2
  exit 1
fi

if [ "$#" -gt 0 ]; then
  repos=("$@")
else
  repos=()
  for root in "${ESTATE[@]}"; do
    [ -d "$root" ] || continue
    while IFS= read -r gitdir; do
      repos+=("${gitdir%/.git}")
    done < <(find "$root" -maxdepth 10 -name .git -type d -not -path '*/node_modules/*' 2>/dev/null)
  done
fi

pinned=0; skipped=0; failed=0
for repo in "${repos[@]}"; do
  url="$(git -C "$repo" remote get-url origin 2>/dev/null)" || { skipped=$((skipped+1)); continue; }
  owner="$(printf '%s' "$url" | sed -nE 's#.*github\.com[:/]([^/]+)/.*#\1#p')"
  label="${repo#$HOME/}"

  if [ -z "$owner" ] || ! printf '%s\n' "$accounts" | grep -qx "$owner"; then
    echo "skip   $label (owner ${owner:-none} is not a signed-in gh account)"
    skipped=$((skipped+1)); continue
  fi

  helper="!f() { test \"\$1\" = get || exit 0; echo username=$owner; echo \"password=\$($GH auth token --user $owner)\"; }; f"
  git -C "$repo" config --local --unset-all credential.https://github.com.helper 2>/dev/null
  git -C "$repo" config --local credential.username "$owner"
  git -C "$repo" config --local --add credential.https://github.com.helper ""
  git -C "$repo" config --local --add credential.https://github.com.helper "$helper"

  if git -C "$repo" ls-remote origin HEAD >/dev/null 2>&1; then
    echo "pinned $label → $owner"
    pinned=$((pinned+1))
  else
    echo "FAILED $label → $owner (pinned, but the remote is not reachable)"
    failed=$((failed+1))
  fi
done

echo "done: $pinned pinned, $skipped skipped, $failed failed"
[ "$failed" -eq 0 ]
