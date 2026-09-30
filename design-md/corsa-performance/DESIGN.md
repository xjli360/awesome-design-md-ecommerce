---
version: alpha
name: "Corsa Performance"
source_url: "https://corsaperformance.com"
captured_at: "2026-09-29T04:08:54.056817+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is grounded in CSS extracted from corsaperformance.com, an American manufacturer
  of performance exhaust systems, headers, and air intakes. The observed palette centers on a near-black
  ink (#1a1a1a) against a white canvas, with #e41e30 red appearing as a button outline/focus color in the
  extracted CSS and inferred here as the primary brand accent, consistent with performance-automotive
  conventions. Supporting neutrals (#f3f3f2, #dedede, #8a8a8a, #c4cdd5) are inferred as soft surfaces,
  hairlines, and muted text from their contrast values, not from confirmed component screenshots. Two
  status colors were directly observed in a vehicle-fitment widget: #11ae66 (green, fitment match) and
  #f4534d (red-orange, fitment fail), which this spec repurposes as semantic success/danger tokens. A
  navy/blue cluster (#0c2131, #1990c6) is present in the palette but its usage context was not captured;
  it is retained as a secondary accent option only.

  Typography uses Barlow, the sole non-monospace font family found in the CSS, with sans-serif fallback;
  the monospace stack (Consolas, Menlo, etc.) is treated as a system/code fallback, not a brand voice.
  Heading scale (h0–h6) and text-xs/sm/base/lg values are taken directly from :root custom properties
  across responsive breakpoints; weights, letter-spacing, and line-heights are proposed since no computed
  font-weight or tracking was captured. The resulting interpretation favors a bold, high-contrast,
  functional layout suited to a parts catalog with vehicle-fitment search as a primary interaction.

colors:
  primary: "#e41e30"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#8a8a8a"
  hairline: "#dedede"
  surface-soft: "#f3f3f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#11ae66"
  danger: "#f4534d"
  border-strong: "#c4cdd5"
  accent-navy: "#0c2131"
  accent-blue: "#1990c6"
typography:
  display-xl: {fontFamily: "Barlow, sans-serif", fontSize: 64px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    successColor: "{colors.success}"
    failColor: "{colors.danger}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders the red brand accent (#e41e30) as a solid call-to-action, matching the
`--button-outline-color: 228 30 48` value observed in the CSS custom properties, used for actions like
"Shop Now" or "Add to Cart." Hover state (a slight opacity reduction, per `--button-background-opacity: 0.85`
observed in the CSS) is confirmed by the stylesheet; all other states are proposed.

**button-secondary** is a low-emphasis outlined variant for secondary actions (e.g., "Shop All" links seen
repeatedly in the navigation text). Border and text colors are inferred from neutral ink/hairline tokens
since no distinct secondary-button styling was captured in the evidence.

**text-input** covers search and account form fields. Border color and padding are proposed conventions;
no explicit input CSS was present besides generic monospace font-stacks used for code-like fields.

**nav-bar** reflects the sticky header behavior explicitly set via `--sticky-header-enabled:1` and
`position: sticky` in the extracted CSS, with a logo sized 120–200px across breakpoints. Background opacity
and blur (`--header-background-blur-radius: 20px`) are observed; exact color treatment during scroll is
proposed.

**product-card** is a proposed pattern for the catalog grid (Exhaust Systems, Air Intakes, Pro Series Parts)
implied by the extensive product-category navigation text; no direct card markup or shadow values were
captured, so surface and border tokens are inferred from the general neutral palette.

**hero** models the homepage's rotating "New Product" promotional slides (e.g., "S550 Shelby GT500 Exhaust,"
"2025+ Ram RHO Exhaust") referenced in the page text. Dark ink background with white text is a proposed
high-contrast treatment; actual hero imagery/background was not observed.

**footer** is inferred as a dark-toned closing section per common Shopify-theme convention and the site's
ink/white palette; no footer-specific CSS rules were included in the evidence.

**badge** repurposes the observed fitment-success green (#11ae66) as a general status/label chip (e.g.,
"New," "In Stock"). This reuse is an interpretive extension beyond its one confirmed use in fitment results.

**fitment-selector** is a category-appropriate custom component modeling the "Search by Vehicle"
Year/Make/Model/Sub Model/Body Style/Engine/Drive tool referenced in the page text and its
`.easysearch-fitment-*` classes, which directly set green (#11ae66) for match and red-orange (#f4534d) for
fail states — the clearest confirmed semantic-color mapping in the evidence.

## Responsive Behavior

The following breakpoint table is a proposed recommendation for implementation, not a measured observation
of live site behavior:

| Breakpoint | Width      | Header/Nav                          | Grid columns |
|-----------|-----------|--------------------------------------|-------------|
| Mobile    | <640px    | Collapsed hamburger nav, stacked logo | 1 |
| Tablet    | 640–1024px| Condensed nav, icon-only search       | 2 |
| Desktop   | 1024–1440px| Full nav ("main-nav logo secondary-nav" grid, as observed in header CSS) | 3–4 |
| Wide      | >1440px   | Full nav, larger logo (200×43px per observed CSS) | 4+ |

Touch targets are recommended at a minimum 44px height, consistent with the observed accelerated-checkout
button clamp (`clamp(25px, 44px, 55px)`). Mobile nav collapse into a hamburger/drawer pattern is a standard
proposal only — no mobile DOM or interaction was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS custom properties, class names, and page text; no rendered
screenshots, computed styles, or interaction states were observed. Font-weight, letter-spacing, and
line-height values in the typography table are proposed defaults layered onto the confirmed Barlow family
and confirmed rem-based size scale. Color-to-role mapping (e.g., red as "primary") is inferred from a single
button-outline-color declaration and general brand convention, not from a verified button screenshot. The
navy/blue cluster (#0c2131, #1990c6, #136f99) has no confirmed usage context and is included only as a
retained palette option. Border-radius values follow the requested default scale, not observed values,
except for the one confirmed `border-radius: 0px` on the accelerated-checkout button. Mobile/responsive
layout, hover/focus states beyond the one documented button-opacity rule, and custom font licensing/hosting
were not verified and should be confirmed against the live site before implementation.
