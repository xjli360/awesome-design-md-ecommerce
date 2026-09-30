---
version: alpha
name: "Kalon Studios"
source_url: "https://kalonstudios.com"
captured_at: "2026-09-28T09:38:57.642250+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kalon Studios' front-end CSS shows a restrained, editorial system built on WordPress/WooCommerce defaults rather than a fully bespoke design language. Body copy renders in AdelleSans (14px, line-height ~1.43, color #404040) on a soft off-white canvas (#f4f4f4), with headings set in the same family at bold weight (700) and tight line-height (1.1), color inherited from context. The only clearly branded interactive element observed is the primary button: a dark charcoal fill (#32373c), white text, and a fully pill-shaped radius (9999px) — this becomes the anchor for the proposed button and badge components. Bootstrap-derived status colors (success #3c763d/#dff0d8, warning #8a6d3b/#fcf8e3, danger #a94442) indicate WooCommerce form validation styling, relevant to cart, wholesale, and product-registration flows. A large block of WordPress default editor-palette swatches (vivid blues, oranges, purples) also appears in the evidence; these are treated as CMS tooling defaults, not confirmed brand colors, and are excluded from the core palette. Surface tones (#eeeeee, #ffffff, #f5f5f5) are inferred as card/section backgrounds to support the "material integrity" content (wood, stone, metal, textile imagery) without adding unverified brand hues.

colors:
  primary: "#32373c"
  ink: "#000000"
  canvas: "#f4f4f4"
  body: "#404040"
  muted: "#606060"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#999999"
  divider: "#cccccc"
  status-success: "#3c763d"
  status-success-bg: "#dff0d8"
  status-warning: "#8a6d3b"
  status-warning-bg: "#fcf8e3"
  status-danger: "#a94442"
typography:
  display-xl: {fontFamily: "AdelleSans, sans-serif", fontSize: "42px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.3px"}
  display-md: {fontFamily: "AdelleSans, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.2px"}
  title-md: {fontFamily: "AdelleSans, sans-serif", fontSize: "20px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "AdelleSans, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "AdelleSans, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.43, letterSpacing: "0px"}
  caption: {fontFamily: "AdelleSans, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "AdelleSans, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1, letterSpacing: "0.3px"}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.status-success-bg}"
    textColor: "{colors.status-success}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  material-swatch:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.divider}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"

## Components

**button-primary** mirrors the one confirmed brand interaction pattern in the evidence: `.wp-block-button__link` and `.wp-element-button`, which set a dark charcoal fill (#32373c), white text, and a full pill radius (9999px). This is treated as the primary CTA for "Shop," "Subscribe," and account actions.

**button-secondary** is a proposed outline variant sharing the pill radius and charcoal color for use where a lighter-weight action is needed (e.g., "Learn More" links inside hero or collection modules). No secondary button styling was observed; this is inferred from the primary button's shape language.

**text-input** is proposed for search, newsletter signup, and WooCommerce account/cart forms implied by the page text (mailing list preferences, wholesale application, product registration). Border and radius are conservative, drawn from the neutral hairline gray (#dddddd) since no explicit input styling was captured.

**nav-bar** reflects the site's flat, text-driven navigation structure (Shop, Collections, Studio, Wholesale + Trade, Support) on the observed canvas background (#f4f4f4), with a hairline bottom border proposed for separation from content.

**product-card** is inferred for the "Shop Products" and collection grids (e.g., Nursery, Seating, Tables & Desks). It uses the white surface color and a small radius to stay visually quiet, letting product photography of wood/stone/metal pieces carry the design — consistent with the stated "material integrity" positioning.

**hero** corresponds to homepage modules like "Shop Our Work" and "Rugosa — The Art of Simplicity." Typography uses the largest observed heading scale (700 weight, tight line-height), with generous section padding proposed to match the editorial, image-forward tone described in the page copy.

**footer** groups the extensive link taxonomy (Studio, Culture, Wholesale + Trade, Support, social links) on a light gray surface (#eeeeee, the WordPress "very-light-gray" utility class), using muted body text (#606060) for secondary link styling.

**badge** is proposed for status/confirmation messaging (form success, in-stock, "Ready to Ship" tags) using the Bootstrap-style success palette (#3c763d on #dff0d8) present in the CSS, which strongly suggests WooCommerce alert styling rather than a custom brand badge.

**material-swatch** is a category-appropriate addition for a materials-led furniture brand: a compact card for showing wood/metal/stone/textile samples referenced under "Our Materials" and "Material Samples & Hardware Kits." No swatch-specific CSS was observed; sizing and border derive from the general neutral/divider tones.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior — no media queries or viewport-specific rules were present in the supplied evidence.

| Breakpoint | Width       | Nav behavior                     | Grid                          |
|-----------|-------------|-----------------------------------|--------------------------------|
| Mobile    | < 640px     | Collapsed hamburger nav (proposed)| 1-column product grid          |
| Tablet    | 640–1024px  | Condensed horizontal nav          | 2-column product grid          |
| Desktop   | > 1024px    | Full horizontal nav               | 3–4 column product grid        |

Touch targets on buttons and nav items should maintain a minimum 44px hit area; the pill-shaped button radius (9999px) supports this comfortably at the proposed padding scale. Collapse/expand interaction for mobile navigation, filters, and cart drawer is not observed and should be validated against live implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically (CSS rules, page text, title); no rendered layout, hover/focus states, or JavaScript-driven interactions (cart drawer, filters, mega-menu) were observed.
- Heading color is set via `color:inherit`; the actual rendered heading color (assumed near-black/#000000 here) is an inferred mapping, not a direct observation.
- Font sizes for display-md, title-md, caption, and button-md are proposed/estimated; only 14px (body), 16px, and 42px were directly present in the CSS via WordPress presets.
- A large set of WordPress default editor-palette colors (e.g., #0693e3, #ff6900, #9b51e0, #7a00df) appear in the evidence but were excluded from the core role mapping as they are CMS tooling defaults, not confirmed brand colors.
- AdelleSans is a licensed commercial typeface; availability/licensing for implementation was not verified, and a system sans-serif fallback should be used if the license is not confirmed.
- Responsive breakpoints, touch-target sizing, and mobile nav collapse behavior are proposed conventions only, not measured from the live site.
