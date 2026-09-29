---
version: alpha
name: "Lulu and Georgia"
source_url: "https://luluandgeorgia.com"
captured_at: "2026-09-28T04:51:19.165411+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lulu and Georgia is a design-forward home furnishings retailer whose bathroom
  offering (vanities, bathroom lighting, mirrors + medicine cabinets, bath
  accessories) sits inside a much larger home-goods catalog. The observed CSS
  surfaces a warm near-black ink (#1a1713) alongside neutral grayscale
  utilities (#333333, #737373, #cccccc, #eeeeee, #f5f5f5) typical of a
  editorial, product-photography-led storefront. A single saturated teal
  (#108474) recurs across the review-widget custom properties (stars, review
  CTA background, reviewer name) and is treated here, as inferred, as the
  closest available brand accent since no other saturated color repeats with
  similar consistency; red (#dc2626) is reserved for sale/compare-at pricing,
  matching its observed use on strikethrough and discounted price text.
  Typography draws on two observed families: "Iskry" for display/heading
  roles (weight variants Bold/Regular) and "Soehne" (Leicht/Buch/Kraftig) for
  body and UI text, with the button size/weight/letter-spacing values taken
  directly from the .jm-button rule. Rounded corners are treated as sharp
  (radius 0) per the explicit `--jdgm-border-radius: 0` token; any larger
  radii in this spec are proposed conveniences for cards and inputs, not
  observed values. Layout, spacing scale, and breakpoints are proposed
  conventions consistent with a grid-based catalog site, not measured.

colors:
  primary: "#108474"
  ink: "#1a1713"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#737373"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale: "#dc2626"
  subtle: "#eeeeee"
  border: "#cccccc"
typography:
  display-xl: {fontFamily: "Iskry Bold, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Iskry Regular, sans-serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Soehne Kraftig, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Soehne Buch, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Soehne Leicht, sans-serif", fontSize: "14px", fontWeight: 300, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Soehne Leicht, sans-serif", fontSize: "12px", fontWeight: 300, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Soehne Leicht, sans-serif", fontSize: "13px", fontWeight: 800, lineHeight: "24px", letterSpacing: "2px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.sale}"
    compareAtColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    size: "32px"

## Components

**button-primary** renders category CTAs ("Shop Bath Vanities," "Add to Bag") using the teal primary against white text, with the observed sharp-corner, uppercase, letter-spaced treatment from the review-widget button rule extended site-wide as a proposed convention.

**button-secondary** is an outline variant for lower-emphasis actions (filters, "View Details") sharing the same type scale but on a white/ink pairing; hover and focus states are proposed, not observed.

**text-input** covers search fields, newsletter capture, and account forms; the hairline border and soft radius are proposed defaults since no explicit input CSS was supplied.

**nav-bar** reflects the deep mega-menu structure evident in the page text (New / Furniture / Rugs / Lighting / Bathroom, etc.); a white background with hairline dividers between top-level and flyout sections is proposed for legibility over dense category lists.

**product-card** is the primary catalog unit for vanities, mirrors, and bathroom lighting. The compare-at price uses the observed strikethrough ink color and the discounted price switches to `{colors.sale}`, matching the `.picky-byob-pdp` price-wrapper rule exactly.

**hero** proposes a full-bleed editorial banner pattern (consistent with "Fall Living," "September Lookbook" campaign naming in the nav) using the soft neutral surface and display-xl heading type; imagery treatment is not observed.

**footer** is proposed as a dark ink block for contrast against the otherwise light catalog, holding utility links (Accessibility Statement, Customer Support) referenced in the page text.

**badge** covers sale/new labeling using the sale-red pill; "New" and percentage-off tags on product tiles are proposed applications of this token, not confirmed from layout screenshots.

**search** models the header search affordance implied by ecommerce navigation conventions; no dedicated search CSS was present in evidence.

**finish-swatch** is a bathroom-fixture-specific pattern for vanity finish/hardware selection (e.g., oak, marble, brushed brass), using a circular swatch with a teal active-state ring; this is a proposed pattern inferred from the product category, not from observed swatch markup.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| Mobile     | 0–639px     | Single-column product grid, collapsed hamburger nav, sticky add-to-bag bar |
| Tablet     | 640–1023px  | 2-column product grid, mega-menu collapses to accordion |
| Desktop    | 1024–1439px | 3–4 column product grid, full mega-menu on hover |
| Wide       | 1440px+     | Max content width with increased gutter (`{spacing.xxl}`) |

Touch targets should be a minimum of 44×44px for filter chips, swatches, and nav items. Mega-menu flyouts should collapse to expandable accordions below 1024px. This table is a design recommendation only; no responsive behavior was measured from the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction; no rendered layout, breakpoints, or interaction states (hover, focus, active, disabled) were observed.
- The primary accent (#108474) is inferred from third-party review-widget variables and may not represent the core brand palette used in hero/marketing imagery.
- "Iskry" and "Soehne" font weights/styles are named in CSS but their visual character, licensing, and availability as web fonts were not verified.
- Rounded-corner values beyond the explicit `--jdgm-border-radius: 0` token are proposed for usability, not confirmed site conventions.
- Spacing scale, grid columns, and component padding are conventional proposals, not measured from computed styles.
- Bathroom-fixtures-specific UI (vanity configurator, finish selection) is inferred from category taxonomy in the nav text, not from observed product-page markup.
- Mobile navigation and cart-drawer behavior were not present in the supplied CSS/text and are therefore undocumented.
