---
file_type: reference
document_type: design_tokens
scope: cross-venture
last_updated: 2026-04-23
source: Extracted from retired alfred-os/ BabylonJS scene on 2026-04-23
---

# Studio Colours

The canonical colour palette for the seven studios. Extracted from the retired `alfred-os/` visualisation (BabylonJS Pokémon-world scene) where each studio was represented as a Pokémon-type colour. This is the design-token reference for any UI work that surfaces studio activity – dashboards, monitoring displays, briefing visuals.

Applies across every venture (Five Points, Marty Gras, Paradigm, Lillie and Lynette, and any future addition) because the seven-studio model is cross-venture.

---

## Palette

| Studio | Hex | RGB (0–255) | Normalised (0.0–1.0) | Visual Feel |
|---|---|---|---|---|
| Creative | `#FF6B36` | 255, 107, 54 | 1.00, 0.42, 0.21 | Burnt orange. Heat, expression, output energy. |
| Strategy | `#A854F7` | 168, 84, 247 | 0.66, 0.33, 0.97 | Violet. Thinking, depth, pattern recognition. |
| Production | `#94A3B8` | 148, 163, 184 | 0.58, 0.64, 0.72 | Slate. Tooling, grounded execution. |
| Growth | `#21C55E` | 33, 196, 94 | 0.13, 0.77, 0.37 | Green. Revenue, expansion, life. |
| Operations | `#EBB208` | 235, 178, 8 | 0.92, 0.70, 0.03 | Amber. Pipeline, throughput, motion. |
| Finance | `#05B5D4` | 5, 181, 212 | 0.02, 0.71, 0.83 | Cyan. Cool, liquidity, numbers. |
| Administration | `#D3A673` | 211, 166, 115 | 0.83, 0.65, 0.45 | Tan. Structure, paper, foundation. |

**Default (unmatched / fallback):** `#A8A88F` – 168, 168, 143 – muted olive-grey for anything that does not cleanly map to a studio.

---

## Shared Resource Colours

Knowledge Base and Foundation are shared resources, not studios. If they need visual representation in the same system:

| Resource | Suggested Hex | Visual Feel |
|---|---|---|
| Knowledge Base | `#6B7280` | Graphite grey – library, reference |
| Foundation | `#84CC16` | Lime – community, giving, rootedness |

These are a recommendation from 2026-04-23, not extracted from the source scene. Adjust if a design pass revisits them.

---

## Variant Derivations

For UI states that need depth (hover, active, disabled, darkened):

- **Dark (60%)**: multiply each RGB channel by 0.6. Used for backgrounds in the original scene.
- **Light (tint)**: blend with white at 20–40%. Used for subtle backgrounds or inactive states.

The original scene used the dark variant for base-colour backgrounds and the full variant for accents and particle FX.

---

## Usage Notes

- These colours are a design-token reference, not a strict brand palette. Ventures still carry their own brand colours for external-facing work (Five Points, Marty Gras have their own fingerprints).
- When an internal dashboard or briefing needs to distinguish studios at a glance, this palette is the default.
- The seven colours are deliberately high-contrast against each other so multi-studio activity reads clearly.

---

*This palette is preserved because the finished creative work of selecting and pairing seven distinct studio colours took real effort. The `alfred-os/` visualisation that originated it has been retired, but the colour system itself survives as a reusable reference.*
