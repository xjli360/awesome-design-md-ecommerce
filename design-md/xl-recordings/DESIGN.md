---
version: alpha
name: "XL Recordings"
source_url: "https://www.xlrecordings.com"
captured_at: "2026-09-28T09:35:00.600745+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  XL Recordings pairs a stripped, mono-typographic system with a single
  alarm-red accent against near-black ink. The observed root palette
  (--black:#00120f, --white:#fff, --grey:#d6d7d9, --red:#f00b1b) plus the
  rendered body background rgb(128,136,135) and a light neutral #ebecec
  suggest a restrained, editorial catalog interface: white surfaces
  carrying dense dark text, a muted grey-green body backdrop, thin grey
  hairlines, and red reserved for a single accent role. Red only appears
  as a CSS custom property in the supplied evidence, not tied to a
  confirmed button use, so its assignment to primary/CTA is inferred.
  Typography mixes Helvetica (with unusual monospace/serif fallbacks) for
  body copy and headlines with a manufactured-feel mono family
  (ABC ROM Mono Light, falling back to Courier/monospace) reserved for
  uppercase micro-labels, matching the observed .content-button rule.
  This fits a label's release-sheet aesthetic: catalog numbers, dates,
  and format tags (lp/ep/single) visible throughout the page text. The
  system below extends that logic into dense discography rows, uppercase
  mono format badges, and minimal bordered cards for shop items. Corner
  radii and spacing scale are proposed conventions, not evidenced, since
  no radius or spacing values were present in the supplied CSS.

colors:
  primary: "#f00b1b"
  ink: "#00120f"
  canvas: "#ffffff"
  body: "#808887"
  muted: "#9ca3af"
  hairline: "#d6d7d9"
  surface-soft: "#ebecec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  contrast: "#000000"
  overlay: "#00000000"
typography:
  display-xl: {fontFamily: "Helvetica, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.13, letterSpacing: -0.24px}
  display-md: {fontFamily: "Helvetica, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.16px}
  title-md: {fontFamily: "Helvetica, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica, monospace", fontSize: 16px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica, monospace", fontSize: 13px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "ABC ROM Mono Light, Courier, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.5px}
  button-md: {fontFamily: "ABC ROM Mono Light, Courier, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.5px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.body}"
    overlayColor: "{colors.overlay}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  release-list-item:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    catalogTypography: "{typography.caption}"
    catalogColor: "{colors.muted}"
    titleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.md} {spacing.base}"

## Components

**button-primary** renders the site's single high-contrast call-to-action (e.g. "Buy Now") using the observed red token as fill and white as text, drawing on the .content-button pattern's uppercase mono typography. Hover/active/disabled states are proposed, not observed.

**button-secondary** is a bordered, transparent-fill variant using the hairline grey border and ink text, intended for lower-emphasis actions like "Follow" or "Sign Up," which appear in the nav text but whose exact styling was not present in the supplied CSS.

**text-input** is a proposed form field (e.g. for a newsletter "Sign Up" flow referenced in the page text) using the canvas white background, hairline border, and body-sm typography; focus/error states are proposed.

**nav-bar** reflects the observed header items ("Logo Shop Releases Follow Sign Up") on a white canvas background with ink text set in the uppercase mono button typography; sticky behavior and mobile menu open/close states are proposed, not observed.

**product-card / release-list-item** models the repeating catalog rows visible in the page text (format label, date, catalog number like XL1723DA, artist, title, Buy Now button). Catalog metadata uses the small mono caption style in a muted tone, while the title uses body-md; this pairing is inferred from the .content-button rule and root type scale.

**hero** is a proposed full-width intro panel using the rendered body background (#808887) as a backdrop with a display-xl headline, appropriate for the label's editorial "Behind The Scenes" feature entries; an overlay/scrim value is proposed for text legibility over imagery, not confirmed.

**footer** reuses the body background token with caption-level mono links and hairline dividers, consistent with the minimal, catalog-first tone; exact footer content and layout were not present in the supplied evidence.

**badge** is a small pill-shaped label proposed for format tags such as "LP," "EP," or "Single" that recur throughout the release listing text, using the caption typography and body-toned fill with white text; this specific badge markup was not observed in the CSS.

**search** is a proposed input pattern for locating releases/artists, styled consistently with text-input; no search UI or selectors were present in the supplied evidence.

## Responsive Behavior

Recommended (not measured) breakpoint table:

| Range | Target | Notes |
|---|---|---|
| < 480px | Mobile | Single-column release list, nav collapses to a menu toggle, hero title drops to display-md scale |
| 480–768px | Large mobile / small tablet | Two-column product-card grid, condensed nav |
| 768–1024px | Tablet | Nav-bar shows full link set, three-column catalog grid |
| > 1024px | Desktop | Full nav-bar, multi-column release/shop grids, display-xl hero |

Touch targets are recommended at a minimum 44×44px for button-primary/secondary and badge tap areas. Nav collapse to a hamburger/menu pattern below 768px is a proposed convention only; the supplied evidence contains no viewport, media-query, or JS-driven layout data confirming actual breakpoints or collapse behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built solely from a static CSS/text extraction and does not reflect live rendering, computed layout, or interaction testing. The root font-size (and therefore the rem-to-px conversions used for display-xl, body-md, and caption sizes) is assumed at a conventional 10px base and is not explicitly confirmed in the supplied CSS. Color role assignments — particularly `primary` (red), `body` (rendered grey-green background), `muted`, and `surface-soft` — are semantic inferences from a small set of CSS custom properties and one body rule; no button, badge, or card selectors using red were present in the evidence. Rounded-corner and spacing scales are conventional proposals, since no border-radius, margin, or padding-scale values beyond the single .content-button rule were supplied. The custom font "ABC ROM Mono Light" was observed only as a font-family declaration; its availability, licensing, and actual rendered appearance are unverified. No hover, focus (beyond the generic outline rule), active, disabled, mobile-menu, or search-interaction states were observed. Component definitions for nav-bar, hero, footer, badge, text-input, and search are proposed patterns consistent with the observed palette/typography, not confirmed markup from the site.
