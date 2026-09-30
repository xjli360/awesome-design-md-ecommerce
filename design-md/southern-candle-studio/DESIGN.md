---
version: alpha
name: "Southern Candle Studio"
source_url: "https://southerncandlestudio.com"
captured_at: "2026-09-29T03:54:18.403614+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Southern Candle Studio's storefront CSS points to a deep navy-on-white system anchored by
  `--color-base-text: #002D57` and `--color-base-background-1: #FFFFFF`, with a warm terracotta
  red (`--color-base-accent-1` / `--color-base-link: #D03523`) carrying links and calls to action.
  A secondary neutral layer (`#F4F4F5`, `#FAFAFA`, `#F7F9FB`, `#E7EFF4`) supports dropdown panels,
  footer bands, and a newsletter block, while a small teal accent (`#27ACAE`) is explicitly wired
  to product tag styling (`--color-tag-foreground`). A coral (`#F66560`) and periwinkle (`#DFE2F0`)
  pair appear only inside decorative dot-pattern SVG assets, so they are treated here as optional
  ornamental accents rather than core UI colors. Typography is singular and observed directly:
  Work Sans for both body (400) and heading (600) roles, falling back to system sans-serif stacks
  seen in the wider font list. Border radius is lightly used (a 4px product-card radius is the only
  measured value); all other radii and every spacing value beyond the `.75rem` header padding are
  proposed, not measured. The resulting interpretation favors a calm, editorial "coastal apothecary"
  feel: navy ink on white/off-white surfaces, a single warm accent for action and links, and a quiet
  teal used sparingly for scent/ingredient tagging, consistent with a small-batch candle and soap
  studio rather than a high-saturation retail brand.

colors:
  primary: "#d03523"
  ink: "#002d57"
  canvas: "#ffffff"
  body: "#002d57"
  muted: "#7a8fa3"
  hairline: "#e0e0e0"
  surface-soft: "#f4f4f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-teal: "#27acae"
  accent-coral: "#f66560"
  border-soft: "#dfe2f0"
  footer-bg: "#f7f9fb"
  newsletter-bg: "#e7eff4"
typography:
  display-xl: {fontFamily: "Work Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Work Sans, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Work Sans, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Work Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Work Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Work Sans, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
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
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    dropdownBackground: "{colors.surface-card}"
    dropdownTextColor: "#2e2e2e"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    newsletterBackground: "{colors.newsletter-bg}"
    headingColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    triggerBackground: "{colors.ink}"
    triggerTextColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fragrance-tag:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.accent-teal}"
    borderColor: "{colors.border-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the observed accent-1/link red (`#D03523`) as a solid fill with white text, sized for the `button-md` weight-500 type seen on header icon labels. Hover/active states are not present in the supplied CSS and are proposed as a modest darken, not measured.

**button-secondary** is an outlined proposed variant using the navy ink for both border and text on a transparent background, intended for secondary actions like "Continue shopping" seen in the cart-empty state text.

**text-input** is inferred from general Shopify-theme conventions since no explicit input CSS was supplied; it borrows the hairline gray for borders and the base canvas/ink pairing for legibility, with a small `xs` radius consistent with the theme's generally low-radius aesthetic.

**nav-bar** reflects the measured `.header` grid (`heading` / `drawer icons` areas) and the `.75rem` vertical padding literally present in `.header`. The dropdown surface color (`#FAFAFA`) and dropdown text color (`#2E2E2E`) are taken directly from the `--header--dropdown-*` custom properties.

**product-card** is proposed structurally, but its `4px` corner radius is the one directly observed value in the evidence (`--product-card--border-radius: 4px`), so this is the most evidence-grounded non-color/typography token in the file.

**hero** is a proposed full-bleed section using the softer background-2 tone (`#F4F4F5`) to separate it from the pure-white body canvas, paired with the `display-xl` scale that extends beyond the measured 36px heading variable for a large marketing headline; this size extension is explicitly a proposal.

**footer** maps directly to measured custom properties: `--footer-background-light-color: #F7F9FB`, `--footer-newsletter-background-color: #E7EFF4`, and `--footer--heading-color: #002D57`, giving this component unusually high confidence relative to the rest of the file.

**badge** repurposes the literal `--color-tag-background: #FFFFFF` / `--color-tag-foreground: #27ACAE` pair found in the CSS, applied here as a generic small-label component (e.g., "New," "Sale") beyond its likely original product-tag context.

**search** is proposed as a dark trigger/panel using ink-on-canvas inversion, consistent with the `.search__button` rule where button background/text swap to the header's text/background colors (`--color-button-background: var(--header--text-color)`).

**fragrance-tag** is the category-appropriate component: a small pill for scent names (e.g., "Hope," "Coastal Breeze") styled with the same teal tag color and a soft periwinkle border (`#DFE2F0`) drawn from the decorative-element palette, suited to a candle/soap catalog that foregrounds named scents.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Range | Layout intent |
|---|---|
| < 480px | Single-column, header collapses to `drawer` + `icons` grid area (matches observed `.header` grid-template-areas), stacked product cards |
| 480–768px | Two-column product grids, nav remains drawer-based |
| 768–1024px | Three-column product grids, inline nav menu likely replaces drawer |
| ≥ 1024px | Four+ column grids, full horizontal nav with dropdown submenus |

Touch targets should be at least 44px tall (aligning with the observed Shopify payment-button clamp of `44px` default block size). Dropdown/submenu collapse behavior is proposed to follow standard disclosure patterns; no JS/interaction states were present in the supplied evidence to confirm actual collapse thresholds or animation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a text excerpt, and a color/font list — no rendered layout, computed box model, hover/focus states, or responsive DOM behavior was observed. The `--color-base-text` role is assumed to govern both headings and body copy since only one text variable was supplied; a true secondary/muted text color (`#7A8FA3`) is inferred by proximity in the palette, not confirmed by a matching CSS variable. Most spacing and all rounded values beyond the single confirmed `4px` product-card radius are proposed conventions, not measurements. The coral (`#F66560`) and periwinkle (`#DFE2F0`) tones are tied only to decorative SVG dot-pattern assets in the source and may not be intended as UI-component colors; they are included here as optional accents. Font availability, weights actually shipped, and licensing for Work Sans on this storefront were not verified beyond the `@font-face`-adjacent custom properties. No mobile menu, cart-drawer, or checkout interaction states were observed; all component states beyond default (hover, focus, disabled, error) are proposed placeholders.
