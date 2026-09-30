---
version: alpha
name: "Secrid"
source_url: "https://secrid.com"
captured_at: "2026-09-28T09:30:34.564799+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Secrid's storefront evidence shows a warm, neutral palette anchored by a
  muted off-white canvas (#f5f4f0) and near-black ink (#2e2e2b), consistent
  with the brand's "industrial design meets fashion" positioning for Dutch
  leather-and-aluminum wallets. A single warm terracotta accent (#c05746) is
  declared as `--highlight-color` in the site's CSS custom properties and is
  treated here as the primary interactive/brand color. A secondary blue
  (#007aff) appears only as a Swiper carousel default and is retained in the
  palette but flagged as likely incidental rather than brand-intentional.
  Supporting neutrals (#686868, #8d897f, #888888, #32312a, #5c5648, #d6ceba)
  are mapped to muted text, hairlines, and soft surface roles by inference,
  since no border or divider selectors were captured directly.

  Typography relies on four custom font tokens observed in the CSS
  (TYPE_CAPITOLIUM, TYPE_DINPRO_COND, TYPE_IMPACT, TYPE_VERDANA), each paired
  with its own "Fallback" variant. Roles below assign these tokens by
  plausible naming convention (serif-leaning Capitolium for display,
  condensed DinPro for titles/navigation, Verdana for body copy, Impact for
  buttons/CTAs) — these role assignments are inferred, not confirmed by
  rendered layout. Rounded and spacing scales are proposed conventions, with
  `rounded.none` corroborated by an observed `border-radius:0` button reset.

colors:
  primary: "#c05746"
  ink: "#2e2e2b"
  canvas: "#f5f4f0"
  body: "#2e2e2b"
  muted: "#686868"
  hairline: "#d6ceba"
  surface-soft: "#d6ceba"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#5c5648"
  neutral-warm: "#8d897f"
  ink-strong: "#32312a"
  muted-alt: "#888888"
  focus: "#007aff"
  black: "#000000"
typography:
  display-xl: {fontFamily: "TYPE_CAPITOLIUM, TYPE_CAPITOLIUM Fallback, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "TYPE_CAPITOLIUM, TYPE_CAPITOLIUM Fallback, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "TYPE_DINPRO_COND, TYPE_DINPRO_COND Fallback, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "TYPE_VERDANA, TYPE_VERDANA Fallback, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "TYPE_VERDANA, TYPE_VERDANA Fallback, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "TYPE_VERDANA, TYPE_VERDANA Fallback, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "TYPE_IMPACT, TYPE_IMPACT Fallback, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    height: "72px"
    padding: "{spacing.md} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink-strong}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  cardprotector-spec-panel:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** carries the terracotta highlight color declared in the site's CSS root as the primary call-to-action treatment (e.g. "Add to cart", "Shop now"); the sharp `rounded.none` reflects the observed global `button { border-radius: 0 }` reset.

**button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g. "View details"), using ink-colored text and border on the canvas background; no outlined button was directly observed.

**text-input** proposes a light canvas-toned field with a soft hairline border for forms such as newsletter signup or the engraving customizer; exact input styling was not present in the supplied CSS.

**nav-bar** assumes a canvas-background header using the condensed DinPro-style title typography for category links (Wallets, Accessories, Stores); header height and exact padding are proposed, not measured.

**product-card** is inferred for wallet/cardprotector listing grids, pairing a white surface card with hairline borders; title and price typography roles are proposed mappings from the general type scale.

**hero** models the homepage banner pattern implied by the page text (e.g. "Cardprotector for Magsafe" feature block), using the soft tan surface as a background field with display-scale headline type; actual hero markup/CSS was not captured.

**footer** uses the darker olive tone (`#5c5648`) observed as a distinct `body.newsletter-page` background, repurposed here as a plausible footer/newsletter-section color with light text for contrast; this pairing is inferred, not confirmed sitewide.

**badge** proposes a small pill using the primary accent color for labels like "New" or "Bestseller" seen in the page text navigation ("New releases", "Bestsellers"); pill shape and sizing are conventional proposals.

**search** is a proposed lightweight input treatment matching the general text-input pattern, sized smaller for a header search affordance; no search UI was present in the supplied evidence.

**cardprotector-spec-panel** is a category-specific proposed component for presenting RFID/quick-access feature call-outs (as referenced in the page text: "RFID protected", "Quick access") in a bordered card format consistent with the product-card treatment.

## Responsive Behavior

Proposed breakpoints (not measured from the live site):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | < 480px | Single-column stacks; nav collapses to a menu toggle |
| tablet | 480–1024px | Two-column product grids; condensed nav labels |
| desktop | > 1024px | Full multi-column grids; expanded nav-bar |

Touch targets are recommended at a minimum of 44×44px for buttons and nav items. Mobile navigation collapse (hamburger/drawer pattern) is a standard recommendation for a category-heavy wallet-guide site structure, not an observed interaction. All spacing/breakpoint values above are proposed defaults for a responsive e-commerce layout, not extracted from the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed. Font role assignments (display/title/body/button mapped to TYPE_CAPITOLIUM, TYPE_DINPRO_COND, TYPE_VERDANA, TYPE_IMPACT) are inferred from token naming conventions, not confirmed via rendered typography; actual font licensing, availability, and whether these are proprietary or third-party fonts were not verified. Font sizes, weights, and line-heights beyond generic conventions are proposed. The `rounded` and `spacing` scales are largely proposed conventions, with only `rounded.none` corroborated by an observed global button reset. Color-to-role mapping (e.g. hairline, surface-soft, on-primary) is inferred from a flat palette list without confirmed selector-to-role evidence for most values; `#007aff` is retained from the palette but is most likely a third-party Swiper carousel default rather than an intentional brand color. No mobile menu, cart, or checkout markup was present in the supplied evidence, so those flows are entirely unobserved.
