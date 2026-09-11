---
file_type: integration_registry
department: Agents
venture: "{Venture Name}"
status: template
last_updated: 2026-09-10
---

# Integrations

Plugin and tool connections scoped to {Venture Name}. These are the external systems Alfred can operate within when working in {Venture Name} context.

**On copy:** replace every `{Venture Name}` and `{VENTURE}` token, set `status` to `active`, and work the Provisioning Checklist below from top to bottom. Do not delete unprovisioned rows – an empty row that names what is missing is the point of this file. A registry that says nothing is indistinguishable from a registry nobody wrote.

---

## Plugin Routing Principle

{Venture Name} owns its plugins. When Alfred is operating in {Venture Name} context, all plugin operations target the {Venture Name} accounts. When no venture context is active, Alfred defaults to the personal workspace and personal accounts.

Data never crosses between ventures, or between any venture and personal. This is the boundary established in the global CLAUDE.md Navigation Rules, extended to the plugin layer. Venture A's Stripe is not Venture B's Stripe. Venture A's Notion workspace is not Venture B's Notion workspace.

---

## Provisioning Checklist

Every sovereign venture needs these three before it can be operated rather than merely described. Nothing else is universal.

| Surface | Why it is universal | Status |
|---|---|---|
| Notion workspace | State has to live somewhere scoped. Per the 2026-08-08 ruling, every sovereign venture holds its own workspace and its own integration token. Marty Gras is the single standing exception – it is the personal media identity and routes to the personal workspace. | Not provisioned |
| Pennyone pipeline | The cross-venture syndication router. The venture does not own Pennyone; it owns a Zernio account that Pennyone routes to by pipeline key. Add the pipeline to `Integrations/pennyone/` and mint the key. | Not provisioned |
| Payment rail | Any venture that will take money needs one. Stripe is the house default and is always venture-scoped – no personal Stripe exists in the ecosystem. Defer only while the venture is pre-revenue, and record that it is deferred rather than omitting the row. | Not provisioned |

---

## Active Plugins

Connections that are live and verified. A row belongs here only after a health check or an equivalent live call has returned successfully – never on the strength of a config file entry alone.

| Service | Account scope | MCP server | Package | Status | Env var | Last verified |
|---|---|---|---|---|---|---|
| _none yet_ | | | | | | |

---

## Target-State Plugins

Connections the venture needs but does not yet hold. Each row names the blocking step and who owns it.

### Notion – {Venture Name} workspace

| Field | Value |
|---|---|
| Workspace | {Venture Name} – to be created |
| Scope | The workspace staples – Sphere Manager, Projects, Tasks, Decision Log, Contacts, Annotations, Resources and Codex – plus whatever the venture operations require. Codex ruled a staple 2026-09-05: a prompt bank holding only high-leverage, contextually rich prompts, organised by department; the instruments those prompts produce live in Resources. Five Points is the reference implementation |
| MCP server name | `notion-{venture-slug}` |
| MCP package | `@notionhq/notion-mcp-server` |
| Status | **Not provisioned.** Workspace not created, token not minted, server not registered. |
| Environment variable | `NOTION_{VENTURE}_TOKEN` |
| Blocking step | Operator creates the Notion workspace and mints an internal integration token, then grants it to each database. Alfred registers the server and updates this row. |
| Routing rule | All {Venture Name} state reads and writes target this connection. Never the personal workspace, never another venture workspace. |

### Pennyone – social syndication

| Field | Value |
|---|---|
| Account | Zernio ({Venture Name}) – to be provisioned |
| Scope | Syndication across the platforms the venture actually publishes to |
| Pipeline value | `{venture_slug}` |
| MCP server name | `pennyone` (cross-venture router) |
| MCP package | Custom Python/FastMCP server at `Integrations/pennyone/` |
| Status | **Not provisioned.** Verify with `pennyone health_check`; an unprovisioned pipeline returns `no_key`. |
| Environment variable | `ZERNIO_{VENTURE}_API_KEY` |
| Routing rule | Dispatches pass `pipeline: "{venture_slug}"` and Pennyone routes under the venture Zernio account. Pennyone itself is cross-venture; only the Zernio account is venture-scoped. |

---

## Tool-Only – No MCP Connection

Tools the venture uses that Alfred cannot operate within directly. Alfred may reference them; it cannot act in them.

| Tool | Purpose | Notes |
|---|---|---|
| _none yet_ | | |

---

## Secrets

All keys live in `~/Alfred Pennyworth/.env`, gitignored. `.mcp.json` sources the file at launch and passes keys by reference – no raw value ever enters a config file. Every variable added here must also be added to `Manual/secrets-inventory.md` in the same pass; drift between the two is a restore liability.

| Environment variable | Service | Status |
|---|---|---|
| `NOTION_{VENTURE}_TOKEN` | Notion ({Venture Name} workspace) | Not provisioned |
| `ZERNIO_{VENTURE}_API_KEY` | Zernio ({Venture Name} pipeline) | Not provisioned |

Naming pattern: `SERVICE_{VENTURE}_TOKEN`, or a domain-specific suffix where the service has its own canonical terminology – Stripe uses `_SECRET_KEY` because "secret key" is the Stripe term. Domain-specific naming beats forced uniformity.

---

## Adding a New Plugin

1. Add the key to `~/Alfred Pennyworth/.env` following the naming pattern above.
2. Add the server config to `.mcp.json`, sourcing `.env` by reference.
3. Register it here with account scope, MCP server name, package, status, environment variable, consuming skills and routing rules.
4. Add the variable row to `Manual/secrets-inventory.md` with its re-issue procedure.
5. Add the server row to `Manual/mcp-registry.md`, the canonical wiring table.
6. Update any skills that need access via their `allowed-tools` list.
7. If the same service exists at personal or another venture level, document the routing rule that distinguishes them.
8. Run the live health check before moving the row from Target-State to Active. Record the verification date.

---

*Template. Copy with the venture folder and provision on first use.*
