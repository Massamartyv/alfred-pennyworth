# Spring Cleaning — Session Kickoff Prompt

Paste the block below into a fresh Claude Code session at the root of `~/Alfred Pennyworth/`.

---

## Prompt

Conduct a full architectural audit of this repository. Dispatch nine parallel Opus subagents, one per lane. Do not share context between agents during the audit phase — each agent works independently and returns a report.

Before dispatching, read the following to establish ground truth on intended architecture and active state:

- `~/.claude/CLAUDE.md`
- `.claude/CLAUDE.md`
- `Context/Spheres/` cluster index files
- `Agents/_index.md`
- `~/.claude/projects/-Users-martyspicer-Alfred-Pennyworth/memory/MEMORY.md`

Then dispatch all nine agents in a single message (parallel). Each agent receives its lane, reads only the files in its lane, and returns a report in the standard format below.

### The nine lanes

1. **Context architecture** — Sphere files, cluster indices, graduated files, cross-cutting files. Check structural compliance with the project CLAUDE.md, consistency between cluster index and actual sphere folders, staleness of dates and active-state snapshots, orphaned files, and whether graduated files are still referenced correctly.

2. **Identity and governance** — Global CLAUDE.md, project CLAUDE.md, and the cross-cutting identity files (`personal-brand-identity.md`, `martyv-identity.md`, `creative-director.md`). Check for internal contradictions, duplicated rules across files, rules that are stated but not enforced anywhere, and missing governance on capabilities that have been added.

3. **Skills** — All skills at `~/.claude/skills/`. Inventory every skill. Identify: skills referenced in MEMORY.md or CLAUDE.md that do not exist; skills that exist but are never referenced; skills with weak or ambiguous triggers; skills whose `allowed-tools` lists are out of date with current MCP connections; skills that should be merged or split. Flag missing skills that the architecture implies should exist.

4. **Agents** — `Agents/` directory. Audit definition completeness against the frontmatter standard in project CLAUDE.md, working directory hygiene (`.working/{agent-name}/`), dispatch protocol coherence, crew classification correctness, and any agent referenced in docs that lacks a definition file or vice versa.

5. **Ventures** — `Context/Spheres/System/Entrepreneurship/`. Verify every active venture mirrors the seven-studio + two-shared-resources filing standard. Check the `New Venture/` template matches current standard. Inventory client folders under each venture and flag any that are incomplete, mislabeled, or outside the standard. Verify each venture has `Agents/integrations.md` and `Agents/agent-guidelines.md` if warranted.

6. **Integrations and plugins** — All `integrations.md` files and the MCP routing map. Cross-reference claimed MCP connections against what is actually available in this session. Flag dead connections, undocumented connections, routing ambiguity (same service used by multiple scopes with unclear rules), and missing routing rules for connected services.

7. **Automations and routines** — `Automations/` directory and the standing autonomous tasks listed in global CLAUDE.md Cross-Cluster Maintenance. Verify each scheduled task has a corresponding executable or documented procedure. Flag cadences that have drifted, automations with no owner, and routines that should exist but do not (e.g., venture-level maintenance, agent working-directory cleanup).

8. **Memory and logs** — `~/.claude/projects/-Users-martyspicer-Alfred-Pennyworth/memory/` and `Logs/`. Audit the MEMORY.md index against actual memory files (missing entries, dead pointers, duplicates). Identify stale project memories where work has completed. Check for memories that contradict current repo state. Review log hygiene.

9. **Open loops and capability gaps** — Cross-cutting lane. Grep for TODO, FIXME, "pending," "deferred," "not yet set," dangling references to files that do not exist, and mentions of people or resources not yet captured in the Notion Contacts database. Then propose capability gaps: new skills, agents, automations, or integrations that the architecture suggests should exist but do not — each suggestion with rationale and placement.

### Report format (every agent, every lane)

1. **Inventory** — what exists in scope of this lane
2. **Findings** — specific violations, gaps, inconsistencies. Cite file paths and line numbers. No abstract observations.
3. **Recommendations** — prioritized as `Do now` / `Do soon` / `Consider`
4. **Open questions** — items requiring the principal's judgment before any action is taken

### Synthesis (after all agents return)

Produce four artifacts:

- **Consolidated punch list** — all findings grouped by priority across lanes
- **Dependency map** — where one fix blocks or enables another
- **Decision queue** — every open question requiring the principal's input before action
- **Proposed execution order** — sequenced by dependency and effort, with rough time estimates

### Constraints

- Do not modify any file during the audit phase. Audit first, remediate second, on explicit approval per item.
- All conversational output maintains the Alfred Pennyworth persona defined in the global CLAUDE.md — composed, precise, British, no filler, no em dashes, no contractions.
- Findings must cite file paths. Opinions without evidence get stripped in synthesis.
- If an agent discovers work that looks in-progress (uncommitted changes, recent edits, drafts), flag it — do not classify it as drift.
- Use the project's `.working/` directory for any intermediate agent output.

Present the four synthesis artifacts and wait for approval before touching anything.
