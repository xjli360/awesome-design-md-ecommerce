---
version: alpha
name: "Channellock"
source_url: "https://channellock.com"
captured_at: "2026-09-29T04:22:15.625000+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Channellock's public site pairs an industrial, American-manufacturing narrative with a compact set of observed brand colors. The CSS exposes a bright blue (#009ddb, echoing the "Channellock Blue®" trademark text) and a strong red (#ce1141), consistent with the red/white/blue heritage messaging on the homepage. Neutrals run from near-black text (#212121/#231f20) through mid grays (#767676, #333333) to light surfaces (#efefef, #f4f4f4, #dddddd hairlines), giving a utilitarian, high-contrast reading experience appropriate for a tool catalog. The only brand-specific font family found in evidence is "Barlow Condensed," a condensed grotesk well suited to bold, industrial headlines; body copy is assumed to fall back to system sans-serif since no separate body font was declared. WordPress block defaults (fully rounded 9999px buttons, dark slate #32373c button background) appear in the CSS but are treated here as generic CMS defaults rather than confirmed brand identity, so this interpretation substitutes the observed brand red/blue for button coloring. Layout, spacing, and breakpoints below are proposed conventions for a hand-tools e-commerce site, not measured from a rendered page, and are labeled accordingly throughout.

colors:
  primary: "#009ddb"
  accent: "#ce1141"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#efefef"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  link: "#1863dc"
  dark-surface: "#313131"
  warning: "#ffae00"
typography:
  display-xl: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  trade-category-tile:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

**button-primary** uses the observed brand blue as its fill with white text, intended for primary calls to action such as "Shop 'Em All" or "Submit." Hover/active states are proposed, not observed.

**button-secondary** is an outlined variant in the same blue, for lower-emphasis actions (e.g., "View" on FAQ links); fill-on-hover is a proposed interaction, not confirmed.

**text-input** models newsletter and search fields with a light hairline border and white background, matching the clean-neutral palette found in the CSS custom properties; focus-ring styling is proposed only.

**nav-bar** represents the top utility/category navigation ("SHOP TOOLS," "SUPPORT," etc.) as a white bar with dark text and a bottom hairline; sticky behavior and dropdown states are inferred conventions, not measured.

**hero** maps to the "140 Years" banner section, using the dark surface color found in the block-editor gray class (#313131) with the brand blue as an accent for eyebrow text or underlines; the large display type reflects the condensed headline style suggested by Barlow Condensed.

**product-card** is proposed for tool listings (Pliers, Snips, Wrenches) using a light card surface and hairline border; image aspect ratio and hover elevation are unobserved and proposed.

**badge** applies the accent red pill shape, useful for labels like "Made in USA" or "New," borrowing the fully-rounded button radius already present in the WordPress CSS.

**search** is a simple soft-background field for the site's "SEARCH BAR" element referenced in the page text; icon placement is proposed.

**trade-category-tile** is a category-specific component for the "Made for the Trades" grid (Plumbing, HVAC, Electrical, etc.), using a soft neutral background with a blue accent stripe or icon color; grid arrangement is proposed, not observed.

**footer** uses the dark surface with white text and blue links, consistent with the newsletter/contact block at the page bottom; column layout is a proposed structure.

## Responsive Behavior

Recommended breakpoints (not measured from the live site):

| Breakpoint | Width | Behavior (proposed) |
|---|---|---|
| small | 0–39.9em | Single-column stack; nav collapses to a menu icon; hero text reduces to `display-md`. |
| medium | 40em–63.9em | Two-column product grids; nav shows partial inline links. |
| large | 64em–74.9em | Full horizontal nav; three-column product/trade grids. |
| xlarge+ | 75em+ | Max-width container with four-column grids and larger hero padding (`{spacing.section}`). |

Touch targets for buttons and nav items should be at least 44px tall. Category and trade tiles should stack vertically below `medium`. This table is a design recommendation only; no responsive CSS or media-query behavior was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a cookie-consent stylesheet, and page text — not from a rendered or interactive session. Color roles (primary vs. accent, surface-soft vs. surface-card) are inferred from usage context (e.g., WordPress "has-*-background-color" classes) rather than confirmed brand guidelines. Only "Barlow Condensed" was identified as a distinctive family; all other typography values (sizes, weights, line-heights) are proposed defaults, not extracted from computed styles. No hover, focus, active, or error states were observed. Mobile menu behavior, product grid layout, and card imagery were not present in the evidence and are therefore proposed only. Font licensing/self-hosting status for Barlow Condensed was not verified. The WordPress button radius (9999px) and dark button fill (#32373c) reflect generic theme defaults rather than confirmed Channellock brand styling, and have been substituted with palette-consistent brand colors in this interpretation.
