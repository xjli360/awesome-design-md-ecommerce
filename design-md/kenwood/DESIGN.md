---
version: alpha
name: "Kenwood"
source_url: "https://kenwood.com"
captured_at: "2026-09-28T04:29:57.408056+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The extracted evidence for kenwood.com is dominated by CSS reset rules
  (normalize.css, main.css) rather than finished brand styling, so this
  interpretation treats the palette as a neutral foundation and infers a
  restrained, technical car-audio aesthetic on top of it. The only
  confirmed brand-adjacent value is the body text color #222222, paired
  with sans-serif as the declared interface font family for html, button,
  input, select, and textarea elements. Because no headline color, accent
  color, or custom webfont was observed in use, primary, surface, and
  accent roles below are inferred from the surrounding grayscale evidence
  (#000000, #ffffff, #b4b6b8, #71787f, #cccccc, #999999, #616161, #c0c0c0,
  #848484, #47617a). A small cluster of highly saturated values (#ff0000,
  #00ff00, #ffff00, #b3d4fc, #66000000) is present in the raw palette but
  reads as browser-default or third-party widget/test styling rather than
  brand color, so it is excluded from semantic roles and flagged in Known
  Gaps. The resulting interpretation favors a black-and-white, high-contrast
  industrial-electronics look with gray hairlines and monospace accents for
  technical/spec content, consistent with a car-electronics manufacturer
  site rather than a lifestyle brand.

colors:
  primary: "#000000"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#71787f"
  hairline: "#cccccc"
  surface-soft: "#b4b6b8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary-muted: "#848484"
  border-strong: "#616161"
  disabled: "#999999"
  overlay: "#c0c0c0"
  accent-slate: "#47617a"
typography:
  display-xl: {fontFamily: "sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.25px"}
  button-md: {fontFamily: "sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.5px"}
  spec-mono: {fontFamily: "monospace", fontSize: "13px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-mono}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  badge:
    backgroundColor: "{colors.accent-slate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.secondary-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

**button-primary** — Proposed solid black button for primary calls to action (e.g. "Shop Now", "Find a Dealer"), using `on-primary` white text for maximum contrast, consistent with the grayscale-dominant evidence. Hover/active/disabled states are not observed and are proposed only.

**button-secondary** — An outlined variant on white canvas with a `border-strong` (#616161) hairline and black text, intended for lower-emphasis actions like "Compare" or "Learn More." Focus and pressed states are proposed, not measured.

**text-input** — A minimal bordered field using the observed `#cccccc` hairline and `#222222` ink text, matching the reset-level `color: #222` rule. Placeholder, error, and focus-ring styling are not present in the evidence and are proposed conventions.

**nav-bar** — Inferred top navigation in solid black with white labels, appropriate for a global electronics manufacturer header. No sticky, mega-menu, or scroll behavior was observed; this is a structural proposal only.

**hero** — A dark, high-contrast banner region (ink background, white display type) intended for flagship product or campaign imagery. Actual homepage hero markup/CSS was not present in the supplied evidence.

**product-card** — A white card with a light hairline border for AV receivers, speakers, and accessories, pairing a title-md heading with muted body copy. Image aspect ratio and hover elevation are proposed, not observed.

**spec-table** — A category-specific component for technical specification blocks (power output, connectivity, dimensions), using the observed monospace fallback to visually distinguish numeric spec data from prose, on a light `surface-soft` gray background.

**badge** — A small pill using the muted slate accent (#47617a) for status labels such as "New" or "Hi-Res Audio," with white caption text. Color choice is inferred, not confirmed brand usage.

**search** — A rounded search field with muted placeholder text, consistent with typical retail/e-commerce header patterns; no such component was directly observed in the supplied CSS.

**footer** — A black footer band with secondary-muted (#848484) link/label text for legal, support, and sitemap content, mirroring the dark nav-bar treatment for visual bookending.

## Responsive Behavior

Proposed breakpoints (not measured from live layout):

| Breakpoint | Width       | Notes                                   |
|-----------|-------------|------------------------------------------|
| mobile    | 0–599px     | Single-column, nav collapses to menu icon |
| tablet    | 600–959px   | 2-column product grids                    |
| desktop   | 960–1279px  | Full nav, 3–4 column grids                |
| wide      | 1280px+     | Max-width container, generous section spacing |

Touch targets should be at least 44×44px; navigation and search are assumed to collapse into an off-canvas or hamburger pattern below tablet width. This table is a recommendation for implementation, not an observation of Kenwood's actual responsive markup or breakpoints.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.

- **Evidence correction:** A font found only in a legacy `_font-family` browser hack was removed; the remaining observed fallback family is used.

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS extraction (normalize.css and main.css reset rules) rather than rendered pages, so layout, spacing, component structure, and interaction states were not directly observed. Only `color: #222` and `font-family: sans-serif` are confirmed brand-adjacent values; all role assignments for primary, surface, accent, and hairline colors are inferred from the remaining grayscale palette. Several supplied colors (#ff0000, #00ff00, #ffff00, #b3d4fc, #66000000) appear to be browser-default, accessibility-outline, or third-party widget artifacts rather than brand colors and were deliberately excluded from semantic mapping. Courier New/monospace and serif were present in the font-family evidence but their actual usage context on the site is unknown; monospace has been assigned speculatively to a spec-table use case appropriate for the car-electronics category. No custom/proprietary webfont was observed, and no font licensing has been verified. All component states (hover, focus, active, error, disabled) and all responsive/mobile behavior are proposed conventions, not measured site behavior.
