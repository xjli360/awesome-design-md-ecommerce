---
version: alpha
name: "Trunki"
source_url: "https://www.trunki.co.uk/"
captured_at: "2026-09-29T04:37:19.531217+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Trunki's storefront CSS exposes a compact root palette: white canvas
  (#ffffff), a deep navy foreground (#123b62) used for body copy, badge
  borders and secondary-button hover states, and a coral-red button/link
  color (#f15c5f) that recurs across CTA templates, collection buttons and
  footer promo hovers. A separate --color-heading variable resolves to a
  pale sky blue (#80d2ec); because no rendered heading rule in the supplied
  evidence directly sets this as visible text color, it is treated here as
  an inferred accent rather than a confirmed heading color. Secondary navy
  hover states (#003a62, #003f63) reinforce navy as the brand's structural
  ink. Warmer/teal tones (#11b1a7, #ffda00, #e69e6c) appear only inside
  product-swatch or article imagery contexts and are kept as optional
  product-accent colors, not core identity claims. Neutrals (#dddddd,
  #f7f8fa, #777777) resemble generic UI/framework grays and are used
  cautiously for hairlines and soft surfaces. Poppins is the one font with
  a verified @font-face declaration (hosted woff2/woff), so it anchors the
  type system; Josefin Sans and Avenir Next Rounded appear only in the raw
  font-family list and are treated as unverified alternates. The resulting
  interpretation favors a clean white canvas, navy text, and a single
  coral action color, with pill-shaped buttons matching the observed
  44px/100px radii.

colors:
  primary: "#f15c5f"
  secondary: "#003a62"
  ink: "#123b62"
  canvas: "#ffffff"
  body: "#123b62"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f7f8fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-heading-unverified: "#80d2ec"
  swatch-teal: "#11b1a7"
  swatch-yellow: "#ffda00"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
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
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  ride-on-swatch-picker:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    swatchColors: ["{colors.swatch-teal}", "{colors.swatch-yellow}", "{colors.primary}"]
    typography: "{typography.caption}"
    padding: "{spacing.xs}"

## Components
**button-primary** renders the coral CTA (#f15c5f) seen across collection buttons and add-to-cart actions, using the pill radius observed in `.collections-button-template` rules (border-radius 30–44px, generalized to `rounded.full`). **button-secondary** proposes a white-fill/coral-border inverse for lower-emphasis actions; the hover-swap to navy seen in supplied CSS suggests a state pattern, not a distinct secondary component. **text-input** is a proposed pattern for forms (email signup, login) using generic hairline/gray borders, since no dedicated input selector was supplied. **nav-bar** reflects the header's flat white background and navy text implied by root variables; sticky/collapse behavior is not observed. **product-card** is inferred from the bestseller/product-grid text content (title, regular/sale price, add-to-cart) styled with card surface and hairline border. **hero** models the homepage banner ("Meet the whole family") using soft surface background and display typography; exact hero image treatment is not in evidence. **footer** uses ink-navy background with white text, matching footer promo button styles (`.footer-button-promo`) and hover-to-coral fill. **badge** covers trust markers like "5-year guarantee" or sale tags, built from the `--color-badge-*` variables (white background, navy border/text). **search** is a proposed pill-shaped input, stylistically consistent with other pill controls but not directly observed. **ride-on-swatch-picker** is a category-specific proposed component for selecting suitcase/character color variants (e.g., Una, Dougie, Frank), using teal/yellow/coral swatch dots drawn from the supplied palette to represent product color options; exact swatch UI is not confirmed from static CSS.

## Responsive Behavior
Proposed breakpoints (not measured from rendered site): `sm` ≤480px (single-column product grid, stacked nav), `md` 481–768px (2-column grid, condensed nav), `lg` 769–1024px (3–4 column grid, full nav), `xl` ≥1025px (full desktop grid, multi-column footer). Touch targets should be ≥44px height for pill buttons and swatch pickers given the kids/parent audience. Navigation is expected to collapse into a hamburger/drawer pattern below `md`, and product filters/sort controls likely stack above the grid on narrow viewports. This table is a recommendation based on common ecommerce patterns, not an observation of Trunki's actual responsive CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven interactions, or mobile breakpoints were observed. The `--color-heading` variable (#80d2ec) has no confirmed visible-text usage in the supplied rules and is marked unverified. Several neutral grays (#ced4da, #6c757d, #495057, #80bdff) resemble generic framework/Bootstrap defaults and may not represent intentional brand choices; they are used sparingly and only where no clearer brand-specific value existed. Cookie-consent button colors (e.g., #e5e97e) and review-widget colors were explicitly excluded from brand-identity claims per guidance. Poppins is the only font with a verified `@font-face` declaration in evidence; Josefin Sans, Avenir Next Rounded, and other listed families are unconfirmed as to actual role or licensing. All pixel sizes in the typography scale are proposed, not measured. Component states (hover/focus/active beyond the two documented button hovers) and mobile navigation behavior are not observed and are labeled proposed throughout.
