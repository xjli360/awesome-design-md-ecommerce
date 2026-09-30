---
version: alpha
name: "Bora"
source_url: "https://boratool.com"
captured_at: "2026-09-29T04:12:25.232539+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bora Tool's site runs on WordPress/Elementor/WooCommerce, and its CSS custom
  properties expose a small, consistent brand palette: a saturated
  construction-orange primary (#F7941D), a cool slate secondary (#495965),
  a near-black text color (#25282A), and a muted grey-blue accent (#6D7982).
  These four are declared twice — once as WordPress theme vars and again as
  Elementor globals — confirming they are the intentional brand tokens rather
  than plugin defaults. The remainder of the supplied palette (whites, greys,
  a dark footer tone, and a handful of status reds/greens) reads as WooCommerce
  and form-plugin utility color, not brand identity, and is treated here as
  inferred surface/utility roles rather than confirmed brand color.

  Typography is system-first: Proxima Nova is explicitly named in button and
  review-widget CSS, while Poppins, Open Sans, and Roboto appear only in the
  bundled font stack (some Klaviyo-hosted) without direct selector evidence.
  This interpretation assigns Proxima Nova to body copy and controls (as
  observed) and proposes Poppins for large display headings, labeled inferred.

  The visual language proposed here — bold orange CTAs, rounded product
  cards (20px radius observed on `.product-type-simple`), pill buttons
  (9999px observed on `.wp-block-button__link`), and utilitarian slate-grey
  secondary actions — supports a rugged, trade-tool retail catalog with heavy
  emphasis on product cards, spec callouts, and store-locator conversion paths.

colors:
  primary: "#F7941D"
  ink: "#25282A"
  canvas: "#ffffff"
  body: "#495965"
  muted: "#6D7982"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#495965"
  accent: "#69727d"
  dark-surface: "#0e252c"
  border-strong: "#cccccc"
  danger: "#d9534f"
  success: "#5cb85c"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 10px
  lg: 20px
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
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** carries the orange (`#F7941D`) fill observed in both the
theme and Elementor global color variables, used for high-intent actions like
"View Product" and "Shop." Rounded at 10px, matching the observed
`.elementor-1192 ... .elementor-button` radius.

**button-secondary** uses the slate accent tone (`#69727d`), matching the
generic `.elementor-button` background observed sitewide, for lower-priority
actions such as "Learn More." Proposed hover state: darken toward
`{colors.dark-surface}` (not confirmed by static CSS).

**text-input** is a plain white field with a light hairline border, sized for
search and contact forms; focus-ring styling is proposed, not observed.

**nav-bar** is inferred as a white top bar with dark text and a persistent
"Find a Retailer" and search affordance, consistent with the page-text
excerpt's header order (search, retailer, shop, categories). Sticky/mobile
collapse behavior is not confirmed.

**product-card** reflects the observed `.archive .product-type-simple` rule
directly: white surface, 20px rounded corners, soft box-shadow, center-aligned
content. Used for the featured-products grid (Jobhorse brackets, Clamp Edge,
Workhorse sawhorses).

**hero** is proposed as a dark, full-bleed banner (using the darkest palette
value, `#0e252c`, as an inferred surface) behind the "Adjustable Speedhorse
XT" headline and primary CTA, since no hero-specific CSS was supplied.

**footer** groups the multi-column link structure evident in the page text
(Products, Information, social icons) on a dark surface with orange link
accents, echoing the primary brand color for scannability.

**badge** is proposed for spec/feature tags (e.g., "1,800 lb capacity") as a
pill using the primary color, since no literal badge CSS was supplied but the
pill-radius (`9999px`) is directly observed on `.wp-block-button__link`.

**search** is a rounded search affordance inferred from the "Products
search" label in the header text; exact field chrome is not observed.

**spec-callout** is a category-specific component proposed for woodworking
tool specs (capacity, height range, dimensions) seen in the Speedhorse copy,
styled as a quiet secondary-color info strip beneath product titles.

## Responsive Behavior

Recommended breakpoints (proposed, not measured):

| Range | Layout intent |
|---|---|
| ≥1200px | Multi-column product/category grids, full nav visible |
| 768–1199px | 2–3 column grids, condensed nav |
| 480–767px | Single-column stacked cards, hamburger nav |
| <480px | Full-width stacked cards, sticky CTA buttons |

Touch targets should be at least 44px tall for buttons (`button-primary`,
`button-secondary`, `badge`), given the tool/retail audience likely browsing
on job-site mobile devices. Category and product-grid navigation should
collapse to an accordion or horizontal scroll below 768px. None of this is
derived from measured runtime layout — it is a standard responsive
recommendation for a WooCommerce catalog of this type.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically; no rendered layout, hover/focus states,
  or JavaScript-driven interactions (carousels, mega-menus, mobile drawer)
  were observed.
- Font-family-to-role mapping (Poppins for display type) is inferred from
  the bundled font list, not from a selector explicitly pairing Poppins with
  a heading class.
- Several supplied colors (`#d9534f`, `#5cb85c`, `#5bc0de`, `#f0ad4e`) match
  common Bootstrap/plugin utility defaults and are treated as non-brand
  status colors rather than confirmed brand palette.
- Spacing scale values are proposed conventions, not measured from margin/
  padding rules beyond the button `calc()` paddings observed.
- Rounded tokens for `xs`/`sm` are estimated between the observed 3px
  (`.elementor-button`) and larger observed radii (10px, 20px, 9999px).
- Font licensing/availability for Proxima Nova and Poppins on end-user
  systems is not verified; fallback to system sans-serif is assumed.
- Mobile navigation, search interaction, and store-locator flow are named in
  page text but their visual/interaction design was not present in supplied
  evidence.
