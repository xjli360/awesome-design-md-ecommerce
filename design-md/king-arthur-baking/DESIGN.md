---
version: alpha
name: "King Arthur Baking"
source_url: "https://kingarthurbaking.com"
captured_at: "2026-09-28T09:29:17.415613+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from static CSS evidence for kingarthurbaking.com, a Vermont-based
  employee-owned baking brand selling flour, mixes, tools, and pans. The supplied stylesheet
  fragments are largely Drupal/jQuery-UI utility CSS rather than curated brand tokens, so color and
  type roles below are inferred from the most brand-plausible values in the observed palette rather
  than measured from rendered pages. The signature red (#da1a32, with a darker #a00f28 variant) reads
  as the primary brand and CTA color, consistent with King Arthur's red-accented identity. Warm
  off-whites and tans (#f8f5f0, #dcd0ad) are treated as bakery-appropriate surface tones against a
  white canvas, while grays (#333333, #757575, #e0e0e0) supply body text and hairlines. Amber/brown
  accents (#fbb040, #6a4434) are proposed for gold-toned badges and crust-like secondary accents,
  reused rather than invented. Typography pairs the observed serif Playfair Display for display
  headings with sans-serif Open Sans/brandon-grotesque for UI and body text, falling back to Arial/
  Helvetica/Georgia per the CSS stacks actually present. All sizing, spacing, and radius values are
  proposed defaults for an e-commerce/recipe hybrid site, not measured layout.

colors:
  primary: "#da1a32"
  primary-hover: "#a00f28"
  ink: "#232323"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#e0e0e0"
  surface-soft: "#f8f5f0"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-gold: "#fbb040"
  accent-brown: "#6a4434"
  wheat: "#dcd0ad"
  focus-ring: "#3e63dd"
typography:
  display-xl: {fontFamily: "'Playfair Display', Georgia, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Playfair Display', Georgia, serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "brandon-grotesque, 'Open Sans', Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "brandon-grotesque, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  recipe-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the observed brand red (#da1a32) as a solid fill with white text, intended for "Add to Cart," "Shop Now," and rewards CTAs; a darker red (#a00f28) is proposed for hover/pressed states, unobserved but consistent with typical hover-darkening patterns.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g., "View Details"), reusing the primary red as border/text color on a transparent background; focus and disabled states are proposed, not confirmed from the CSS.

**text-input** covers search boxes, newsletter signup, and account/cart form fields. It borrows the neutral hairline gray for borders and body gray for placeholder/typed text, since no dedicated form-field color tokens were present in the evidence.

**nav-bar** represents the extensive mega-menu structure visible in the page text (Shop, Recipes, Learn, Baking School, Impact). It is proposed as a white bar with dark ink text and a bottom hairline, since the megamenu's actual background/elevation was not present in the supplied rules.

**product-card** supports the large Shop taxonomy (flours, mixes, tools, pans) with a light card surface, subtle border, and a title/price hierarchy pairing the sans title style with body-weight pricing.

**recipe-card**, the category-specific component, addresses the site's dual identity as both a retailer and a recipe/education hub (Bread, Pie, Sourdough categories). It uses a plain white background to differentiate editorial recipe content from commerce product cards, with caption-sized metadata (time, difficulty) proposed but unobserved.

**hero** is proposed for homepage/campaign banners such as the "20% off Baking Mixes" promotion, using the warm off-white surface tone to evoke a bakery/kitchen backdrop behind large serif display type.

**footer** inverts to a dark ink background with white text for site-wide links (Impact, Community Giving, policies), a common pattern for content-dense e-commerce footers; this contrast is proposed, not confirmed from the supplied CSS.

**badge** and **search** are supporting utility components: badge uses the observed amber/gold accent for sale or "New" labels rounded to a pill shape, while search reuses the standard input styling in a compact bar, both proposed for typical retail navigation patterns.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | up to 599px | Single-column product/recipe grid, collapsed hamburger nav for the large Shop/Recipes/Learn menu structure |
| tablet | 600–959px | 2-column card grids, nav may condense secondary items into a "More" menu |
| desktop | 960–1279px | Full mega-menu with multi-column dropdowns as implied by the extensive category text |
| wide | 1280px+ | Max-width content container, 3–4 column product grids |

Touch targets are recommended at a minimum 44×44px for buttons and nav items given the dense category structure. Mega-menu collapse behavior, sticky-header behavior, and actual grid column counts were not observed and are proposed conventions only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

The supplied CSS is dominated by generic Drupal/jQuery-UI framework rules (dialogs, accordions, widget states) and one React search-component stylesheet using CSS custom properties without resolved values; very little brand-specific styling was present. Consequently: (1) the mapping of specific hex values to semantic roles (primary vs. accent vs. status colors) is inferred from plausibility, not confirmed selector usage on branded elements; (2) all typography sizes, weights, and the display/body font pairing are proposed, since no font-size or font-weight rules tied to Playfair Display, Open Sans, or brandon-grotesque were included in the evidence; (3) spacing and radius scales are conventional defaults, not extracted measurements; (4) no responsive/mobile layout, hover, focus, or interaction states were observed directly — all are labeled proposed; (5) the licensing and actual availability of brandon-grotesque and "Para Supreme" as web fonts on this domain was not verified and should be confirmed before implementation; (6) component structures (recipe-card, hero, footer) are reasonable inferences from the page-text navigation but no corresponding DOM/CSS selectors were supplied to confirm their existence or styling.
