---
version: alpha
name: "Micuna"
source_url: "https://micuna.com"
captured_at: "2026-09-28T10:15:39.359035+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Micuna's site is built on the Avada/WooCommerce stack, so most tokens
  observed are framework defaults rather than confirmed brand marks. The
  clearest brand signal is the dark slate button color (#32373c) applied
  consistently to `.wp-element-button` and file-download CTAs, paired with
  white text and a fully-rounded pill shape (9999px) on block buttons. Body
  and label text sit in a narrow gray band (#333333, #6d6e73, #747474)
  against a white canvas, with a soft off-white (#ebeaea, #f6f6f6) used for
  card borders and section backgrounds. Product-variant selectors
  (avada-color-select/avada-image-select) use light gray borders (#d2d2d2)
  around swatch chips, which likely carry dusty terracotta, sage green, and
  denim-blue accents (#d8ab90, #65bc7b, #6596cb) tied to wood-finish or
  fabric options rather than the core brand palette — this mapping is
  inferred from swatch-container evidence, not confirmed brand identity.
  Font evidence lists Lora, Montserrat, DM Sans, and PT Sans; this spec
  assigns Lora to display headings for a warm, editorial nursery feel and
  Montserrat/DM Sans to UI and body text, following common Avada pairing
  conventions. All sizing beyond the button variables is proposed, not
  measured.

colors:
  primary: "#32373c"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#6d6e73"
  muted: "#747474"
  hairline: "#ebeaea"
  surface-soft: "#f6f6f6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  border-select: "#d2d2d2"
  accent-terracotta: "#d8ab90"
  accent-green: "#65bc7b"
  accent-red: "#a64242"
  accent-blue: "#6596cb"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lora, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "DM Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "PT Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 16px, letterSpacing: 0.5px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.border-select}"
    padding: "{spacing.sm} {spacing.base}"
  variant-swatch-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-select}"
    activeBorder: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
    size: "50px"
    padding: "{spacing.xxs}"

## Components

**button-primary** is the dark slate pill button (`#32373c`, 9999px radius) confirmed directly in the `.wp-element-button` and `.wp-block-button__link` rules; it is the strongest observed brand action mark on the site.

**button-secondary** is a proposed outline variant using the same primary color as border and text against white, for lower-emphasis actions like "Discover all our cribs" links — not directly observed, inferred from typical Avada button pairing.

**text-input** proposes a light-bordered field using the hairline gray seen on product-card borders, since no dedicated form-field CSS was supplied.

**nav-bar** is inferred from the site's mega-menu text list (Cots & Minicots, Nursery Furniture, Highchair OVO, etc.); no header background or height was directly measured, so white canvas and hairline underline are proposed defaults.

**product-card** reflects the confirmed `.products li .fusion-product-wrapper` white background and `#ebeaea` border, used for listing cots, wardrobes, and highchairs in the catalog grid.

**hero** is a proposed section pattern for the homepage's featured "Cot NORDIKA / Cot SALONICA" callouts, using the soft off-white surface and large Lora display type; exact hero markup was not in the supplied CSS.

**footer** is inferred to invert to the primary dark slate with white text, consistent with the button color acting as the site's one strong dark anchor; actual footer background was not directly confirmed.

**badge** proposes a small pill using the sage-green accent (`#65bc7b`) for stock/availability or "new" labels common in nursery furniture catalogs; this color's role is inferred from swatch evidence, not a confirmed badge use.

**search** is a rounded field styled from the border-select gray, matching the site's visible "Search for:" toggle, though its expanded-state styling was not observed.

**variant-swatch-selector** is a category-appropriate component modeled directly on the confirmed `.avada-button-select`/`.avada-color-select`/`.avada-image-select` rules (50px square, 1px `#d2d2d2` border, white background), used for selecting cot wood finishes or fabric colors — a pattern central to configurable nursery furniture like the OVO highchair or Nordika cot.

## Responsive Behavior

| Breakpoint | Range | Layout intent (proposed) |
|---|---|---|
| Mobile | <600px | Single-column stacking, nav collapses to toggle menu (site confirms a "Toggle Navigation" pattern) |
| Tablet | 600–1024px | Two-column product grid, swatch selectors wrap to row |
| Desktop | 1024–1440px | Multi-column product grid, full mega-menu visible |
| Wide | >1440px | Max-width content container, generous section padding |

Touch targets should be at least 44px, aligning with the observed 50px swatch-selector size. Navigation collapse behavior is confirmed to exist ("Toggle Navigation" text appears in page content) but its exact breakpoint and animation were not measured. This table is a recommendation only, not observed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, loading) were directly observed. Color-role assignments — particularly the terracotta/green/blue accents tied to product-variant swatches — are inferred from selector context, not confirmed brand guidelines, and may represent product photography or configurator options rather than core brand colors. Typography sizes beyond the two confirmed button variables (`13px`/`16px` line-height) are proposed defaults, not measured from live headings or body copy. Mobile menu behavior, hero section markup, and footer structure were not present in the supplied CSS and are inferred from page text and common Avada/WooCommerce theme conventions. Availability and licensing of the listed fonts (Lora, Montserrat, DM Sans, PT Sans) were not verified beyond their appearance in the font-family list; no proprietary or custom webfont was confirmed.
