---
version: alpha
name: "Focusrite"
source_url: "https://www.focusrite.com"
captured_at: "2026-09-28T05:08:29.917546+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Focusrite's public storefront runs on a shared BigCommerce Stencil theme also used by
  sibling brands (Novation, Sonnox, ADAM Audio), so the CSS evidence mixes a neutral base
  theme with brand-specific overrides. The base theme sets a white canvas (#ffffff) against
  near-black ink (#1d1d20) for body copy and headings, with mid-grey (#727272) reserved for
  secondary/small text such as sub-labels. Primary buttons are solid black (#000000) with
  white text, hovering to a dark grey (#333333) — the only interaction state directly
  observed. A family of blue tones (#1062eb, #3461ec, #2754ab) recurs across the palette and
  is interpreted here as the link/accent system used for in-page CTAs and highlighted
  states, since no other clear accent role is evidenced. A red (#db2b21) is mapped to
  alert/sale usage and a teal-green (#00ac7d) to success/trust-badge usage (e.g. Trustpilot
  rating), both inferred rather than confirmed. Typography draws on Karla for body copy,
  Montserrat (weight 400, +0.25px tracking) for headings, and "TT Norms Pro Demi-Bold" for
  header/nav labels — all directly observed in the CSS. This interpretation adapts that
  system for a microphone/pro-audio storefront: dark, technical, product-photography-forward,
  with restrained color used mainly for interactive and status cues.

colors:
  primary: "#000000"
  ink: "#1d1d20"
  canvas: "#ffffff"
  body: "#1d1d20"
  muted: "#727272"
  hairline: "#e1e1e6"
  surface-soft: "#f5f5f7"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent: "#1062eb"
  accent-deep: "#2754ab"
  alert: "#db2b21"
  success: "#00ac7d"
  hover-dark: "#333333"
typography:
  display-xl: {fontFamily: "Montserrat, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0.25px}
  display-md: {fontFamily: "Montserrat, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.25px}
  title-md: {fontFamily: "Montserrat, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "Karla, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  body-sm: {fontFamily: "Karla, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "Karla, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: normal}
  button-md: {fontFamily: "Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1, letterSpacing: 0px}
  nav-md: {fontFamily: "'TT Norms Pro Demi-Bold', sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.25px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-md}"
    hairline: "{colors.hairline}"
    height: "30px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
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
  spec-highlight:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** — Solid black CTA with white text, directly evidenced by `.button--primary` (background/border `#000`, color `#fff`), used for primary purchase/order actions like "Buy now" and "Order now."

**button-secondary** — Outlined variant on transparent background, inferred from the base `.button` rule's transparent fill and border-driven states; proposed for secondary actions such as "Find out more."

**text-input** — Standard bordered field using the hairline neutral and body typography; states beyond default (focus, error) are proposed, not observed in the supplied CSS.

**nav-bar** — Compact 30px-tall utility bar (`.fc-sitewide-header__list`) with white background and centered demi-bold labels; the deep mega-menu structure (Products/Software/Solutions/Support/Explore) is evidenced in page text but its visual layout is inferred.

**product-card** — Off-white card surface for range tiles (Scarlett, Clarett+, ISA, Vocaster, etc.); background, radius, and internal spacing are proposed to match the neutral surface tokens, as no dedicated card CSS was supplied.

**hero** — Dark, full-bleed banner styled on the ink color with large Montserrat display type and white body copy, matching the campaign-style pattern implied by "Scarlett 4th Gen" and "ISA C8X" hero copy in the page text; exact hero markup was not in evidence.

**footer** — Dark ink-background footer with blue accent links, proposed by analogy to the hero treatment; link color reuses the accent blue observed elsewhere in the palette, semantic role inferred.

**badge** — Small pill using the success-green token, proposed for trust/rating cues (e.g., Trustpilot excellence, in-stock status); color role is inferred, not confirmed as a UI badge in the CSS.

**spec-highlight** — Category-appropriate module for microphone/interface technical specs (e.g., polar pattern, sample rate, channel count) pairing a caption-weight label with a title-weight value on a soft surface; entirely a proposed pattern to suit the pro-audio/microphone catalog, not present in supplied evidence.

## Responsive Behavior
Breakpoint hints appear in the evidence as media-query fragments (max-width:551px, 551–801px, 801–1261px, 1261–1681px, min-width:1681px), suggesting a five-tier fluid layout. Proposed mapping:

| Range | Target |
|---|---|
| ≤551px | Mobile: single-column, collapsed nav-bar into a drawer |
| 551–801px | Large mobile/small tablet |
| 801–1261px | Tablet: 2-column product grids |
| 1261–1681px | Desktop: full mega-menu, 3–4 column grids |
| ≥1681px | Wide desktop: max-width content container |

Touch targets should be at least 44px tall for nav and button elements; the mega-menu should collapse to an accordion below 801px. This table is a recommendation derived from media-query breakpoints in the CSS, not measured or screenshot-verified site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover/focus/active beyond the one documented `.button` set) were observed. Several colors (accent blues, red, green, gold tones) appear in the palette but their functional roles are inferred by convention, not confirmed by selector context. Font availability and licensing for "TT Norms Pro," "DINPro," and "Montserrat" custom weights were not verified. The evidence mixes theme rules shared across multiple BigCommerce-hosted brands (Novation, Sonnox, ADAM Audio); rules scoped to `[data-store]` selectors for those other brands were excluded, but the base theme defaults may still be shared rather than Focusrite-exclusive. Spacing scale, card layout, hero structure, and mobile navigation behavior are proposed design patterns, not measured from the live site.
