---
version: alpha
name: "Analogue"
source_url: "https://analogue.co"
captured_at: "2026-09-28T09:08:53.594580+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Analogue's observed palette is dominated by a stark white canvas (#ffffff) and near-black ink
  (#0f0f12/#000000), consistent with a minimal, hardware-forward retro-tech aesthetic. Mid-grey
  values (#686868, #d9d9d9, #efefef, #f3f3f3) are inferred to serve as muted text, hairlines, and
  soft/card surfaces. A small set of saturated colors (#94ff88 green, #615fc6 purple, #d42422 red,
  #f4cd01 yellow) appear in the extracted palette and are treated as inferred accent/badge colors
  for status, review, or promotional callouts rather than confirmed brand primaries, since no CSS
  rule ties them to a specific UI role. Three font families are present in the evidence: circularXx
  (a grotesque sans, used here for UI and body text), neueBit (a compact display face, used for large
  headings in keeping with the brand's technical/retro tone), and unicaMono (a monospace face, applied
  to captions, labels, and technical specs). Only generic fallbacks (sans-serif, monospace) are used
  alongside these observed families; no specific fallback typefaces were confirmed. Rounded corners,
  spacing scale, and most component states are proposed conventions layered onto the observed tokens,
  not measured from live layout.

colors:
  primary: "#000000"
  ink: "#0f0f12"
  canvas: "#ffffff"
  body: "#242424"
  muted: "#686868"
  hairline: "#d9d9d9"
  surface-soft: "#f3f3f3"
  surface-card: "#efefef"
  on-primary: "#ffffff"
  accent-green: "#94ff88"
  accent-purple: "#615fc6"
  accent-red: "#d42422"
  accent-yellow: "#f4cd01"
typography:
  display-xl: {fontFamily: "neueBit, sans-serif", fontSize: 96px, fontWeight: 700, lineHeight: 1.0, letterSpacing: -1px}
  display-md: {fontFamily: "neueBit, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  title-md: {fontFamily: "circularXx, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "circularXx, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "circularXx, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "unicaMono, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "circularXx, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"

## Components
**button-primary** is a solid black call-to-action ("Buy Now", "Shop Now") intended for the highest-priority actions like purchasing hardware; hover/active/disabled states are proposed, not observed. **button-secondary** is an outlined variant for lower-emphasis actions such as "Explore Now," using the canvas background with a hairline border. **text-input** covers newsletter and search fields, styled with a thin hairline border and muted placeholder text; focus-ring styling is proposed. **nav-bar** represents the top-level Store/Products/Editions/Developer/Support navigation implied by the page text, rendered on a white ground with a bottom hairline; sticky/scroll behavior is not confirmed. **product-card** is proposed for grid listings of consoles (Analogue 3D, Analogue Pocket), pairing a title in the neueBit-derived title style with mono-leaning price/spec text on a soft card surface. **hero** models the large marquee banner pattern evident from repeated "Shipping Now"/"Out of Stock" messaging, using the display-xl scale for product names. **footer** inverts to a dark ink background carrying legal links (Terms, Privacy, Press, RSS) and social icons, matching the copyright/newsletter text visible in the evidence. **badge** is proposed for status labels like "Sold Out," "New," or review-score chips, borrowing one of the saturated accent colors (green shown) with a pill shape. **search** is a lightweight proposed field for site search. **spec-callout** is a category-specific component for technical spec sheets or press-quote blocks (e.g., the review scores from Gizmodo, Wired, IGN), using the monospace caption style to echo a technical, spec-sheet tone appropriate for a hardware brand.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤480px, tablet 481–1024px, desktop ≥1025px. Navigation is expected to collapse into a hamburger/menu pattern below tablet width, with the marquee/hero stacking to single-column text over full-bleed product imagery. Touch targets for buttons and nav items should maintain a minimum 44×44px hit area on mobile. Product-card grids likely reflow from a multi-column desktop layout to a single column on mobile. This section is a recommendation based on common e-commerce patterns, not observed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no live rendering, DOM inspection, or responsive breakpoints were observed. Color-to-role mapping (e.g., which accent color denotes success vs. promotional badges) is inferred from generic palette presence, not confirmed component usage. Font sizes, weights, and line-heights beyond the few Tailwind utility classes shown (e.g., `.release-notes-content` heading clamp) are proposed conventions, not measured values. Interaction states (hover, focus, active, disabled) and mobile/collapsed navigation behavior were not observed. Availability and licensing of the custom fonts circularXx, neueBit, and unicaMono were not verified; they are referenced only because they appear in the supplied font-family evidence.
