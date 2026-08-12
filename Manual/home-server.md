# Home Server – Design Blueprint

Complete design for the household server that hosts the Alfred operating system as a standing service and serves as the media lab. Costed as of August 2026. Not yet built.

Status: designed, awaiting a build window. Live state and any resulting mission record belong in Notion, not in this file.

Scope: hardware topology, software stack, the iMessage bridge, the standing-operations model, security posture, backup and continuity, and a sequenced build. Out of scope: account creation (see `accounts-inventory.md`), secret handling (see `secrets-inventory.md`), rebuild from zero (see `genesis.md`).

---

## 1. The architectural ruling

**Local body, hosted brain, local specialists.**

Claude Opus cannot run on a home server. The weights are not published and the hardware to serve a frontier model exceeds the entire budget for this build by an order of magnitude. Three layers therefore split as follows.

| Layer | Where it runs | Why |
|---|---|---|
| Body – harness, agent loop, MCP servers, schedulers, filesystem, integrations, iMessage bridge | Local, always on | This is the actual prize. Converts Alfred from invoked to standing. |
| Brain – judgement, taste, long-horizon reasoning, code, creative direction | Hosted, over the API | No open-weight model is close on the work that matters most here. |
| Specialists – transcription, embeddings, vision tagging, classification, transcode | Local | High volume, low judgement. Paying API rates for this work is waste. |

Rejected: a local general-purpose brain. A configuration capable of serving a large open-weight model consumes the whole hardware budget, returns a measurably duller Alfred, and pays back a roughly $200 per month hosted spend over about 50 months. Full sovereignty is correct only when sovereignty is itself the product. It is not.

Design consequence: the relay layer must treat the model as a swappable dependency. If a future open-weight model closes the gap, the change is a configuration line, not a rebuild.

---

## 2. Governing constraints

Four constraints determine every decision below. Ranked by how much they bind.

1. **Silence is non-negotiable.** The cabinet sits in a living space. Spinning drives produce a constant low hum with intermittent seek chatter. This forces bulk storage out of the cabinet entirely.
2. **Attention is the scarce resource, not money.** The build must not become a project that competes with the ventures. Sequenced milestones, each independently useful.
3. **Symmetric fibre is available.** Remote access, off-site replication and serving media away from the house are all genuinely viable rather than theoretically viable.
4. **The data is uncounted.** Consolidation precedes sizing. The array cannot be specified against an unknown.

---

## 3. Topology

Three tiers, separated by acoustics and by role.

```
                        ┌─────────────────────────────────────┐
   MEDIA CABINET        │  HEAD UNIT (silent)                 │
   open shelving,       │  Mac mini, Pro-class silicon        │
   vented, wired        │  Alfred harness, MCP servers,       │
                        │  schedulers, local specialists,     │
                        │  Jellyfin/Plex server process       │
                        └──────────────┬──────────────────────┘
                                       │
                        ┌──────────────┴──────────────────────┐
                        │  WORKING SET (silent)               │
                        │  Thunderbolt NVMe enclosure         │
                        │  Active edits, hot library,         │
                        │  Alfred working files               │
                        └─────────────────────────────────────┘

                        ┌─────────────────────────────────────┐
                        │  BRIDGE UNIT (silent)               │
                        │  Existing M1/M2 Mac                 │
                        │  Messages.app as the Alfred Apple   │
                        │  ID. Watcher and sender only.       │
                        └──────────────┬──────────────────────┘
                                       │
                              10GbE ───┼─── wired run
                                       │
   CLOSET / UTILITY     ┌──────────────┴──────────────────────┐
   out of earshot       │  ARCHIVE TIER (audible)             │
                        │  6-bay NAS, spinning drives         │
                        │  Cold archive, backups, Time        │
                        │  Machine target, media library      │
                        │  UPS                                │
                        └─────────────────────────────────────┘
```

**Why the bridge is a separate machine.** macOS binds Messages.app to one primary Apple ID. The head unit must be signed into the operator Apple ID because Apple Mail, Notes, Calendar and Contacts integrations all depend on it. Messages-as-Alfred therefore requires a second machine signed into a different Apple ID. The existing M1/M2 is not a spare part in this design, it is a required component.

---

## 4. Bill of materials

Prices are August 2026 street estimates. Confirm at purchase. Note that 2026 memory pricing is elevated by ongoing supply constraints, which affects the head unit configuration more than any other line.

### Tier 1 – cabinet

| Item | Specification | Estimate |
|---|---|---|
| Head unit | Mac mini, Pro-class silicon, 48GB unified memory minimum, 1TB internal SSD, 10GbE build option | $2,200 – 2,700 |
| Bridge unit | Existing M1/M2, 8–16GB | $0 |
| Working set | Thunderbolt 5 NVMe enclosure, 4-bay, populated 2 × 4TB | $700 – 1,000 |

Head unit selection notes. The Pro tier is warranted by the local specialists, not by the harness. Whisper large-v3, an embedding model, a vision model for archive tagging and a 30B-class model for triage all want unified memory. 48GB is the working floor, 64GB is comfortable. Base silicon will run the harness fine but will not run the specialists, which forfeits the main economic argument for a local box.

Confirm the current Mac mini generation at purchase. The M5 and M5 Pro line was expected during 2026 but not confirmed at the time of writing. Buy on the memory configuration, not the headline chip.

### Tier 2 – closet

| Item | Specification | Estimate |
|---|---|---|
| NAS chassis | 6-bay x86, dual 10GbE, no drive lock-in. UGREEN NASync DXP6800 Pro class. | $850 – 1,000 |
| Drives | 6 × 20TB NAS-class, mixed manufacturers, staggered purchase dates | $1,800 – 2,400 |
| UPS | 1500VA line-interactive with USB signalling for graceful shutdown | $220 – 280 |

Drive selection notes. Price per terabyte bottoms out in the 16–22TB band, so 20TB is the value point rather than the largest available capacity. Buy from at least two manufacturers and, where possible, on different dates. Drives from one batch fail from one batch. RAIDZ2 or equivalent dual parity across six drives yields roughly 72–76TB usable and survives two simultaneous failures, which matters because rebuild times on 20TB drives run into days and a rebuild is when the second drive dies.

Chassis selection notes. Any-drive compatibility is a hard requirement. Synology reversed its Plus-series drive restriction in DSM 7.3, but the episode is disqualifying on principle. A standard x86 chassis also accepts TrueNAS, Unraid or Proxmox if the vendor operating system disappoints, which preserves the exit.

### Shared

| Item | Specification | Estimate |
|---|---|---|
| Switch | 8-port, 10GbE on the cabinet and closet ports | $250 – 400 |
| Cabling | Cat6a, cabinet to closet run | $60 – 120 |

### Total

**$6,080 – 7,900.** Inside the $4,000 to $10,000 band with headroom for the consolidation phase and for a second-hand off-site replication target later.

---

## 5. Running costs

The hardware is the cheap part. This is the number that matters.

| Line | Monthly |
|---|---|
| Power – roughly 90–110W continuous at Georgia residential rates | $11 – 14 |
| Off-site backup – irreplaceable data only, roughly 10TB at object-storage rates | $55 – 65 |
| Plex Pass, if selected | $250 one-off, or $0 on Jellyfin alone |
| Tailscale | $0 on the personal tier |
| **Alfred token spend for standing operations** | **$150 – 400** |

**Total roughly $220 – 480 per month, dominated by tokens.** A standing agent that fires cadences on a schedule and answers texts all day consumes materially more than an invoked one. This is the single line most likely to surprise, and it is the reason the cost governor in section 7 is not optional.

Back up what is irreplaceable, not what is re-acquirable. Shoot footage, photo archive, project files, business records and the Alfred repository are irreplaceable. A ripped film library is not. Sizing off-site backup against the full array is the most common way this bill triples for no benefit.

---

## 6. Software stack

### Head unit

| Layer | Selection | Notes |
|---|---|---|
| Base | macOS | Required for the Apple ecosystem integrations. Hostile as a headless platform; see section 9. |
| Network overlay | Tailscale | No port forwarding, no exposed attack surface, works from anywhere. |
| Containers | OrbStack or Colima | Lighter than Docker Desktop on Apple silicon. |
| Local inference | Ollama or LM Studio | Serves the specialist models over a local endpoint. |
| Transcription | Whisper large-v3 via MLX | Every episode, interview and voice memo. Runs well on Apple silicon. |
| Embeddings | Local embedding model | Reference Library, Zettelkasten, semantic search over the corpus without a round trip. |
| Photo archive | Immich | Local face and object recognition by design. |
| Media server | Jellyfin plus Plex | See below. |
| Scheduling | launchd plus the existing `Automations/` Python, and the harness scheduler | Prefer launchd over a workflow engine. Legible, no extra abstraction. |

**Jellyfin plus Plex, both.** They point at the same library and cost nothing but memory to run together. Jellyfin is the sovereign default with no subscription and no vendor. Plex is the household-facing front end, because a house with family and guests needs clients that work without explanation and remote access that a guest can use without a lesson. A lifetime Plex Pass is justified by that household, not by the technology.

### Archive tier

TrueNAS SCALE or the vendor operating system, with ZFS or equivalent, snapshots enabled, scrub scheduled monthly, SMART monitoring reporting to the head unit and from there to iMessage.

---

## 7. The iMessage bridge

The primary contact surface. Specified in full because the difference between a real correspondent and an unusable novelty is entirely in these details.

### 7.1 Identity – solving the daisy chain

An Apple ID cannot meaningfully text itself. Messages collapses it into Notes to Self. Alfred therefore needs his own identity.

1. **Create a second Apple ID** on a dedicated address. A free `@icloud.com` address is sufficient and immediate. An `iCloud+` custom domain address on a personal domain is the more elegant option if one is already configured. This must be done by the operator; account creation and password entry are never delegated.
2. **Sign the bridge unit into that Apple ID.** Enable Messages. Set the account profile photo, which becomes the avatar in the thread.
3. **Create a contact card** on the operator devices: name `Alfred Pennyworth`, handle set to the Alfred address, photo attached.

Result: a genuine two-party iMessage conversation. Blue bubbles, read receipts, typing indicators, delivered on phone, watch, iPad, Mac and CarPlay. The thread carries a name and a face rather than a self-addressed utility.

**No SMS fallback on an email handle.** If the bridge is offline, the message fails to deliver rather than falling back to green. This is a feature: an undelivered message is an honest and immediate signal that the server is down. Adding a prepaid line later buys SMS fallback for roughly $10 to $15 per month and is a reversible upgrade.

### 7.2 Relay architecture

```
iPhone (operator)
   │  iMessage
   ▼
BRIDGE UNIT ─ Messages.app signed in as Alfred
   │  watcher: reads chat.db (Full Disk Access required)
   │  sender:  osascript to Messages.app (Automation permission required)
   │
   │  HTTPS, bound to the Tailscale interface only
   ▼
HEAD UNIT ─ relay service → harness session, full Alfred context
   │
   └─ MCP surface: Notion, Apple Mail, Calendar, Stripe, Pennyone, Supabase, filesystem
```

The bridge unit is deliberately thin. It carries no credentials beyond its own Apple ID and holds no knowledge. All reasoning, all context and every integration live on the head unit. A compromised bridge yields a message relay, not an operating system.

### 7.3 The components that make it useful

Most implementations of this ship the transport and stop. The transport is the easy half.

**Session continuity.** A text thread is a conversation, not a series of one-shots. The relay maintains one harness session per rolling window, resuming the same session unless roughly 90 minutes of silence have passed, then starting fresh with the state cache injected. Without this, every message is a cold start and Alfred forgets what was said three bubbles ago. This is the single most important detail in the whole bridge.

**A phone-native output style.** The desktop Alfred register does not survive contact with a text bubble. A dedicated output-style variant: short paragraphs, no markdown tables, no code fences, no headers, roughly 600 characters unless expansion is requested. Character and grammar rules hold unchanged; only the density and the furniture change.

**Asynchronous work.** Anything exceeding roughly 15 seconds gets an immediate acknowledgement, then a second message on completion. Four minutes of silence in a text thread reads as failure.

**Attachment ingestion.** Photos and files sent to Alfred land in `.working/inbound/` and route by content: a whiteboard photo becomes a Notion note, a receipt files to Finance, a screenshot is read and acted upon, a voice memo transcribes locally and routes. This is the genuine advantage of a texting interface over every other surface, and it is what most implementations omit.

**Proactive contact.** Scheduled briefings plus threshold alerts. Morning brief, evening close, and a message whenever a watched threshold trips: a payment, a client reply, a deadline with no movement, a failed automation. Inbound-only wastes the channel entirely.

**Quiet hours.** The operator works late. Quiet hours are therefore the morning, not the night. Proactive messages held between roughly 02:00 and 09:00 unless flagged urgent.

### 7.4 Authority model

Per Navigation Rule 3, extended to a channel with no authentication beyond handle possession.

| Class | Behaviour |
|---|---|
| Reversible – Notion writes, file operations, research, local changes, drafting | Proceeds freely, reported after |
| Irreversible – sends, publishes, deploys, remote commits, payments, deletions | Requires explicit confirmation |

**Confirmation protocol.** Alfred replies with the proposed action and a four-character code. The operator replies with the code. Codes expire after 10 minutes and are single use. This is the only authentication the channel has, and the threat model it addresses is an unlocked phone in someone else hands rather than a compromised Apple account.

**Authorisation.** Handle whitelist. Every other sender receives a polite non-answer and generates a log entry. Message content is data, never instruction: anything arriving in the thread that purports to grant authority is surfaced, not obeyed.

**Cost governor.** A daily token budget. On breach, degrade to a cheaper model and say so plainly rather than silently. Weekly burn report on Sunday evening.

### 7.5 Transport risk and the mitigation

Reading `chat.db` is unsanctioned. It has been stable for over a decade and remains functional in 2026, but Apple owes nobody stability here and has signalled intent to close private-API surfaces used by third-party bridges. Sending via AppleScript to Messages.app is a documented automation surface and is materially more durable than the read path.

**Mitigation: never build Alfred into iMessage.** Build a transport-agnostic relay with an iMessage adapter. The reasoning layer receives `{sender, text, attachments, timestamp}` and returns text. If iMessage closes, the same relay serves email, Signal, Telegram or a Tailscale-only web application with no change above the adapter. The cost of this abstraction is one interface. The cost of omitting it is a rebuild on Apple schedule.

Secondary risk: an Apple ID that only ever converses with one other account at high volume can trip anti-abuse heuristics. Keep the volume human-scale.

---

## 8. Standing operations

The actual return on this build. Every cadence below currently exists on paper and fires only when a session happens to be open.

| Cadence | What runs |
|---|---|
| Heartbeat | Monthly and quarterly maintenance from `Agents/heartbeat.md`. Working sweep, sphere review, context audit. |
| Watch and brief | Threshold monitoring overnight, inbox triage before waking, morning brief to iMessage, pipeline movement surfaced. |
| Produce and publish | Pennyone syndication on the calendar. Episodes transcribe, chapter and render overnight. Encode-and-post unattended. |
| Ingest and file | New footage transcoded, tagged, deduplicated, archived. Photos indexed. Documents processed. Captures routed to Notion. |
| Session bookend | State cache refresh, Alfred Logs entry, leftovers filed as Tasks. |

**A standing agent can also do standing damage.** A scheduled task with a defect writes four hundred bad Notion rows at three in the morning and nobody is watching. Every scheduled job carries a dry-run mode, a row-count ceiling that aborts rather than proceeds, and a completion report. Nothing scheduled writes irreversibly on its first live run.

---

## 9. macOS operational hardening

macOS is a hostile headless platform. Apple does not intend this use.

```bash
sudo systemsetup -setrestartpowerfailure on
sudo systemsetup -setsleep Never
```

- Energy Saver: prevent sleep, wake for network access, start after power failure.
- SSH and Screen Sharing enabled, reachable over Tailscale only, never exposed.
- Full Disk Access granted to the watcher process on the bridge unit.
- Automation permission for Messages.app granted to the sender process.
- Auto-login requires FileVault disabled. Resolution: FileVault **off** on the bridge unit, which holds almost nothing; FileVault **on** on the head unit, accepting a manual unlock after an unplanned outage. The UPS makes those rare enough that the tradeoff favours encryption.

**Post-upgrade checklist.** Major macOS releases reset privacy permissions and occasionally break AppleScript behaviour. After every major upgrade: re-verify Full Disk Access, re-verify Automation permission, send a test message, confirm the watcher resumes. Defer major upgrades until a window exists to fix them.

---

## 10. Backup and continuity

Three-two-one, applied honestly.

| Copy | Location | Contents |
|---|---|---|
| Primary | Working set and archive tier | Everything |
| Local second | Archive tier snapshots, ZFS or equivalent, retained on a schedule | Everything |
| Off-site | Object storage | Irreplaceable only – footage, photo archive, project files, business records, the Alfred repository |

Time Machine from both Macs targets the archive tier. The Alfred repository continues to push to GitHub, which remains the continuity spine per `genesis.md`; the server is an additional copy, never the authority.

**The server does not become a single point of failure for the operating system.** Notion remains the source of truth for state. GitHub remains the source of truth for the engine. If the server burns, Alfred degrades from standing to invoked and nothing is lost. This property is load-bearing and must not be traded away for convenience.

---

## 11. Honest assessment

### What this buys

1. **Alfred becomes standing rather than invoked.** Every cadence that has never actually fired starts firing. This is the compounding return and it is the whole argument.
2. **Availability at the speed of thought.** A text from anywhere, no laptop, no session, no context reload.
3. **Production pipelines that run overnight** instead of occupying editing hours.
4. **Local specialists collapse the cost** of transcription, embedding, tagging and transcode to electricity.
5. **Ownership.** No per-seat creep, no vendor deprecating a feature mid-project, data in the building.
6. **A Five Points capability.** Building this teaches the studio how to build it for a principal. That is a productisable offer at the reserved tier, and the studio does not currently have it.

### What it costs

1. **The sysadmin role is now yours.** A drive fails at two in the morning before a client deadline and there is no support line. This is the largest real cost and it is denominated in attention, which is the declared scarce resource.
2. **A standing agent burns money continuously.** Without the cost governor this quietly becomes several hundred dollars a month.
3. **A standing agent can do standing damage.** See section 8.
4. **macOS fights this.** Every major release is a risk to the bridge.
5. **Apple may close the transport.** Mitigated by the adapter pattern, not eliminated.
6. **Consolidation is real work** before any of it pays off.
7. **The failure mode worth naming.** Inverted: what would guarantee this fails? It fails if it becomes a hobby that competes with the ventures rather than infrastructure that serves them. That is the whole risk, and the mitigation is the sequencing in section 12, not discipline.

---

## 12. Build sequence

Four milestones. Each independently useful. Nothing half-built for long.

### Milestone 0 – The Inventory

Consolidate and count the scattered data across externals, iCloud, Drive, laptops and drawers. Deliverable: a single deduplicated manifest with a true byte count and a measured growth rate.

Runs on existing hardware. **Spend: $0.** Blocks Milestone 2, because the array cannot be sized against an unknown.

### Milestone 1 – The Bridge

Alfred in the pocket. Second Apple ID, bridge unit configured, relay service, session manager, phone output style, authority model, confirmation protocol, cost governor, quiet hours.

Uses the existing M1/M2 plus the head unit. **Spend: $2,200 – 2,700.** The smallest useful thing and the thing most wanted.

### Milestone 2 – The Vault

Archive tier, drives, UPS, wired run, switch, backup topology. Consolidation executed against the Milestone 0 manifest.

**Spend: $2,980 – 3,800.**

### Milestone 3 – The Lab

Working-set enclosure, Jellyfin and Plex, Immich, Whisper pipeline, transcode, ingest-and-file automation, Pennyone scheduling, the standing cadences brought live one at a time with dry runs.

**Spend: $700 – 1,250 plus a Plex Pass.**

---

## 13. Open decisions

Carried forward. Each blocks nothing but should be ruled before the relevant milestone.

1. Head unit generation and memory configuration, to be confirmed against the shipping Mac mini line at purchase.
2. Whether the archive tier runs the vendor operating system or TrueNAS SCALE.
3. Whether Alfred later acquires a phone number for SMS fallback.
4. Exact quiet-hours window.
5. Whether household members and guests get Plex accounts only, or any Alfred surface at all. Current assumption: media only, no Alfred access.
6. Off-site backup provider, pending the Milestone 0 byte count.

---

*Designed August 2026. Not built. Prices are estimates at time of writing and require confirmation at purchase.*
