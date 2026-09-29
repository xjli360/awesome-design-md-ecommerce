---
version: alpha
name: "Fireclay Tile"
source_url: "https://fireclaytile.com"
captured_at: "2026-09-28T04:21:08.474560+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Fireclay Tile's public CSS shows a warm, craft-oriented palette built from
  a dark clay-brown (#312a29), a warm off-white (#fcf9f4), and a saturated
  terracotta red (#c31e1c) that reads as the brand's accent/CTA color given
  its isolation from the neutral majority of the palette. Supporting warm
  neutrals (#d0cac1, #f2ebe6, #e9e8e7) and near-black text tones (#1a1a1a,
  #1b1b1d) suggest a materials-forward, handmade aesthetic consistent with
  ceramic tile. A cluster of secondary browns (#6e2f1b, #5f2b1c, #3f2016)
  and a muted blue/green pair (#1990c6, #557b24) appear alongside the core
  set; these are treated here as inferred secondary/status accents rather
  than confirmed brand colors, since CSS presence alone does not prove
  intended role.

  Typography is more directly evidenced: heading elements explicitly declare
  'Playwright Display' at weight 600 with slight positive letter-spacing,
  giving headlines a crafted, editorial serif-like character. Body/UI text
  families (Muli, MuseoSans 300/700) are inferred as the sans-serif working
  type for paragraphs, labels, and buttons, since no explicit body selector
  rule was supplied. Fluid heading-size custom properties (--text-h0…h6)
  indicate a deliberate responsive type scale. This interpretation proposes
  a warm-neutral canvas with terracotta accents, generous section spacing,
  and restrained rounded corners to match a tactile, artisanal retail feel.

colors:
  primary: "#c31e1c"
  ink: "#1a1a1a"
  canvas: "#fcf9f4"
  body: "#312a29"
  muted: "#5e5e5e"
  hairline: "#e3e3e3"
  surface-soft: "#f2ebe6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-clay: "#6e2f1b"
  accent-sand: "#d0cac1"
  info-link: "#1990c6"
  success: "#557b24"
  warning: "#f5b301"
  border-dark: "#1b1b1d"
  overlay: "#00000066"
typography:
  display-xl: {fontFamily: "'Playwright Display', serif", fontSize: 72px, fontWeight: 600, lineHeight: 1.1, letterSpacing: "0.01em"}
  display-md: {fontFamily: "'Playwright Display', serif", fontSize: 44px, fontWeight: 600, lineHeight: 1.15, letterSpacing: "0.01em"}
  title-md: {fontFamily: "'Playwright Display', serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.01em"}
  body-md: {fontFamily: "Muli, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0"}
  body-sm: {fontFamily: "Muli, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0"}
  caption: {fontFamily: "Muli, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "'MuseoSans 700', Muli, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1, letterSpacing: "0.03em"}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.border-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
    typography: "{typography.caption}"

## Components

**button-primary** — Terracotta-red fill with white text, intended for primary purchase/CTA actions (e.g. "Add to Cart", "Order Samples"). Hover/active/disabled states are proposed, not observed.

**button-secondary** — Neutral canvas background with a hairline border and dark ink text, for secondary actions like "Learn More" or filter toggles. A subtle background-opacity hover treatment was present in the CSS for generic `.button` hover states, so a slight fill-darken on hover is proposed here.

**nav-bar** — Sticky header (position: sticky confirmed in CSS) on a light canvas background, with logo width/height tokens shifting between a compact mobile size and a larger desktop size. Exact breakpoint pixel values were not supplied, so the transition point is inferred.

**product-card** — Light card surface with a soft border and generous internal padding, used for tile/product grid tiles. Rounded corners are proposed at a small radius consistent with a tactile, non-skeuomorphic catalog presentation.

**hero** — Full-bleed dark section (using the observed `#312a29`-family background) with large Playwright Display type in white, for landing banners and campaign imagery overlays. Overlay scrim uses the observed alpha-black token.

**footer** — Dark, warm-brown footer band with light text, echoing the hero's dark treatment to bookend the page. Column/link structure is proposed, not measured.

**badge** — Small pill using the observed gold/amber tone for promotional or "New"/"Sale" labeling on product cards; contrast and exact usage are inferred.

**search** — Soft warm-neutral input field distinct from standard text inputs, intended for a persistent header search affordance; icon and autosuggest states are proposed.

**swatch-selector** — A tile/color-and-finish swatch component specific to a tile retailer: small bordered squares on a card surface, sized for grid display of glaze or material options; selected/hover states are proposed, not observed.

## Responsive Behavior

Recommended breakpoints (not measured from live rendering): mobile ≤767px, tablet 768–1023px, desktop ≥1024px. This aligns loosely with the CSS's own mobile/desktop custom-property pairs (e.g. header logo 100×26px scaling to 130×33px, header padding moving from `--spacing-3` to `--spacing-6`, and heading scale `--text-h0` moving from 3.5rem to 4.5rem), though the exact pixel threshold triggering these swaps was not present in the supplied rules. Navigation likely collapses to a hamburger/drawer pattern below tablet width; this is a standard-practice recommendation, not a verified behavior. Touch targets for buttons and nav items should maintain a minimum 44×44px hit area regardless of visual padding. Product grids should reduce column count (e.g. 3–4 desktop columns to 1–2 mobile columns) and increase row gap using `{spacing.xl}` or `{spacing.xxl}` for readability on small viewports.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties and selector rules only; no live-rendered layout, computed styles, or DOM screenshots were available, so component composition, spacing rhythm, and grid structure are largely inferred from token names rather than observed rendering. Color-to-role mapping (primary, muted, hairline, etc.) is a best-effort semantic inference from value frequency and context clues (e.g. a dark background-color rule), not confirmed brand documentation. All rounded-corner and most spacing values are proposed defaults, not extracted from the site's CSS. No hover, focus, active, error, or loading states were observed in the supplied evidence; all interaction styling is proposed. Mobile/tablet layout composition (stacking order, drawer behavior, breakpoint pixel values) was not observed and is recommended practice only. Font availability and licensing for 'Playwright Display', Muli, and MuseoSans have not been verified; these names are taken directly from the supplied CSS but their legal usage terms and self-hosting/web-font-service status are unknown.
