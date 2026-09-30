---
version: alpha
name: "Peter Pots Pottery"
source_url: "https://peterpots.com"
captured_at: "2026-09-29T04:14:03.912484+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Peter Pots Pottery is a family stoneware studio in Rhode Island operating since 1948, selling
  tableware, servingware, bakeware, and home/garden pieces through a Shopify-style storefront.
  The only colors present in the supplied evidence are two neutral grays, #555555 and #262524,
  with no accent hue, background swatch, or brand color captured in the extraction. This document
  therefore treats #262524 as the primary ink/brand-dark tone and #555555 as a secondary/muted
  gray, and reuses both across canvas, surface, and hairline roles as an inferred, low-confidence
  approximation rather than a measured light background. Actual page backgrounds and any warm
  clay/glaze accent colors were not captured and should be re-verified against the live site.
  Typography draws on three observed font families: EB Garamond, a classic serif, is assigned to
  display and heritage-forward headings to reflect the brand's 75+ year craft story; Didact Gothic,
  a plain geometric sans, is used for titles, buttons, and captions; Roboto, a neutral UI sans, is
  used for body copy and product descriptions. Layout guidance (spacing, radii, breakpoints,
  component shapes) is proposed based on typical e-commerce conventions for a handmade-goods
  catalog with product variants (color, size, design), not from measured CSS layout.

colors:
  primary: "#262524"
  ink: "#262524"
  canvas: "#555555"
  body: "#555555"
  muted: "#555555"
  hairline: "#555555"
  surface-soft: "#555555"
  surface-card: "#262524"
  on-primary: "#555555"
typography:
  display-xl: {fontFamily: "'EB Garamond', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'EB Garamond', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Didact Gothic', sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Roboto', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Roboto', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Didact Gothic', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "'Didact Gothic', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    size: "{spacing.lg}"

## Components

**button-primary** is the main add-to-cart and checkout action, using the darker observed gray as a solid fill with the lighter gray reused as a proposed foreground text color; hover/pressed states are not observed and are proposed as a slight opacity shift.

**button-secondary** is an outlined variant for secondary actions like "Quick View," sharing the hairline color as its border; its transparent fill is inferred, not measured.

**text-input** covers newsletter, search, and account fields, using the card surface tone as fill with a hairline border; focus-state styling is proposed, not observed.

**nav-bar** models the top navigation (Pottery, Peter's Pumpkin Patch, Limited Editions, Vintage & Rarities, Goods, About, Visit) seen in the page text; sticky/collapse behavior is proposed only.

**product-card** represents catalog tiles such as the Grandfathers' Cup, Coffee Cup, and Chowder Bowl entries, pairing a title in the sans display style with price in body type; image treatment is inferred since no image CSS was supplied.

**hero** models the homepage welcome banner ("celebrating 75 years of handcrafting stoneware") with a large serif headline and a supporting sans subhead; exact background imagery/color was not captured in evidence.

**footer** groups store info (hours, phone number) and secondary links on the darkest observed tone, with the lighter gray reused for readable text; this contrast pairing is inferred rather than confirmed via rendered screenshot.

**badge** is proposed for labels like "Limited Edition" or "Best Seller," using the primary tone as a pill fill; no such component was directly observed in the evidence, so it is speculative but stylistically consistent.

**search** is a compact input variant for the account/cart area; states (open/closed, autocomplete) are not observed.

**color-swatch-selector** is a category-specific component for the repeated glaze-color variant pattern seen in the text (Seagull Blue, Mahogany Brown, Spruce Green) — proposed as circular swatches with an active-state ring, since actual swatch markup/CSS was not supplied.

## Responsive Behavior

This is a recommendation only; no live breakpoints, media queries, or mobile layout were present in the supplied CSS.

| Breakpoint | Width       | Behavior (proposed) |
|-----------|-------------|----------------------|
| xs        | <480px      | Single-column product grid, stacked nav collapses to a hamburger menu |
| sm        | 480–767px   | 2-column product grid, condensed hero padding |
| md        | 768–1023px  | 2–3 column product grid, inline nav with wrapping |
| lg        | 1024–1439px | 3–4 column product grid, full horizontal nav |
| xl        | ≥1440px     | 4+ column grid, max-width content container centered |

Touch targets for buttons and swatches should be at least 44×44px per common accessibility guidance (proposed, not verified against live markup). Navigation should collapse into a disclosure/hamburger pattern below `md`; this collapse behavior was not observed and is a standard e-commerce inference.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- The supplied evidence contains only two neutral gray hex values (#555555, #262524); no true background/canvas color, warm clay accent, or brand hue was captured, so `canvas`, `surface-soft`, and `on-primary` roles are low-confidence reuses of these grays rather than measured colors.
- No layout CSS (grid, flexbox, container widths) was supplied beyond a single `--product-block-padding: initial;` custom property repeated across product blocks, so spacing, radii, and grid structure in this document are proposed conventions, not extracted values.
- Font sizes, weights, and letter-spacing in the typography scale are proposed; only the three font family names (Didact Gothic, EB Garamond, Roboto) were confirmed in evidence, not their applied sizes or weights.
- No interaction states (hover, focus, active, disabled), animations, or mobile menu behavior were observed; all such states above are labeled proposed.
- Custom font hosting, licensing, and availability (e.g., Google Fonts vs. self-hosted) were not verified from the supplied evidence.
- Component existence (badges, search UI, swatch selectors) is inferred from page text describing variants (color, size, design options) rather than from directly observed component markup or styles.
