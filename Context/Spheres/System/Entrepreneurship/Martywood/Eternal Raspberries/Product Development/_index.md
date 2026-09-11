---
file_type: reference
venture: Martywood
sub_brand: Eternal Raspberries
status: active
last_updated: 2026-09-10
related_files:
  - "Context/Spheres/System/Entrepreneurship/Martywood/Eternal Raspberries/_index.md"
---

# Eternal Raspberries – Product Development

Build documentation for the product line.

## Holds

- The Agent Brief template, once authored – the page each product ships so a model can read the system once and then operate it
- Per-product build notes: architecture pass, finishing pass, listing pass
- The listing asset specification per channel – Gumroad cover and gallery, Pinterest vertical pins, Facebook organic

## Route notes

- Architecture is built through the Notion API. Inline databases, built-in icons, columns with ratios, callouts, toggles and all copy are reachable that way.
- View types, view names, filters, sorts, page-level small text and full width are not reachable through the API. They run as a second pass through Claude in Chrome, verified working 2026-09-10.
- A database nested inside a column does not accept `inline="true"` or its icon on the first write. Run a second targeted pass on those lines.
