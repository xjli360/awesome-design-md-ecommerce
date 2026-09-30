---
version: alpha
name: "Elkwood Leather"
source_url: "https://elkwoodleather.com"
captured_at: "2026-09-28T09:32:22.870400+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Elkwood Leather's storefront runs on a stock Shopify theme (base.css / Dawn-family
  tokens) layered with a warm, undyed-leather palette. The CSS custom properties
  expose a clear brand triad: a canvas of stone/parchment (`#ece6d9`, also used as
  the gradient-background and secondary-button fill), a tan-leather accent used for
  buttons and links (`#d0a06d`), and a near-black ink (`#1d1c1a`) used for both
  foreground text and button text, echoing tanned hide and stitched thread. Neutral
  greys (`#eeeeee`, `#dddddd`, `#cccccc`, `#89928a`) appear across generic UI chrome
  (badges, borders, skeleton loaders) and are treated here as muted/hairline/surface
  roles — this mapping is inferred, not labeled in source. A third-party review widget
  (Judge.me) injects a separate gold/mustard accent (`#d2bb39`) and star-rating yellow
  (`#efbf04`); these are kept distinct as "accent" tokens rather than merged into the
  primary brand palette, since they originate from an app, not the theme.

  Typography is defined only through CSS variables (`--font-heading-family`,
  `--font-body-family`) without literal family names resolved in the supplied
  evidence; Baskerville and Montserrat/Nunito Sans appear in the font stack and are
  used here as the most plausible serif-heading / sans-body pairing for a
  handcrafted-leather brand, explicitly flagged as inferred. Border-radius tokens
  observed (`--jdgm-border-radius: 0`, checkout button `border-radius:0px`) suggest a
  deliberately sharp, unrounded aesthetic, which the interpretation honors by
  defaulting most components to `rounded.none` or `rounded.xs`.

colors:
  primary: "#d0a06d"
  ink: "#1d1c1a"
  canvas: "#ece6d9"
  body: "#333333"
  muted: "#89928a"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#1d1c1a"
  accent-gold: "#d2bb39"
  rating-star: "#efbf04"
  surface-alt: "#f2f2f2"
  border-alt: "#cccccc"
  dark-contrast: "#000000"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Baskerville, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.06rem}
  body-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.04rem}
  caption: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.04rem}
  button-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.06rem}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.dark-contrast}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    border: "1px solid {colors.dark-contrast}"
  search:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.border-alt}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.md}"
    border: "1px solid {colors.primary}"

## Components

**button-primary** renders the tan leather-tone (`#d0a06d`) fill with dark-ink text, matching the theme's `--color-button` / `--color-button-text` pair used for add-to-cart and checkout actions. Sharp corners (`rounded.none`) are proposed to match the `border-radius:0` behavior seen on checkout buttons and the Judge.me widget.

**button-secondary** inverts the pairing — canvas background with tan text and a tan hairline border — mirroring the theme's `.button--secondary` variable swap (`--color-button` becomes `--color-secondary-button`). Hover/focus states are not observed and are proposed only.

**text-input** is a proposed pattern for account, search, and contact forms; no explicit `input` selector was supplied, so surface, border, and padding values are inferred from the general card/border tokens (`--color-shadow`, hairline greys).

**nav-bar** assumes the canvas parchment tone carries through the header, consistent with `:root`/`.color-background-1` scoping seen in the CSS variables. Sticky/mobile-menu behavior was not observed.

**product-card** uses white surface with hairline border, referencing `.product-card-wrapper .card` custom-property scaffolding (corner radius, border width/opacity, shadow) whose concrete values were not resolved in the supplied evidence — treated as proposed defaults.

**hero** is a proposed full-bleed section on the canvas background using the largest display type, intended for lifestyle imagery of handcrafted wallets/cardholders; no hero markup or imagery was supplied.

**footer** inverts to the dark ink tone (`#1d1c1a`) with light text, a common Shopify footer pattern; this contrast pairing is proposed, not confirmed from a footer-specific selector.

**badge** is modeled as a pill using the theme's `--color-badge-background`/`--color-badge-border` variables (canvas fill, black border), likely used for "New," "Handmade in England," or stock badges.

**search** is a proposed overlay/input pattern using a light-grey surface distinct from the card white, for visual separation in a predictive-search dropdown.

**material-tag** is a category-specific proposed component for labeling leather types (e.g., "Shell Cordovan," "Pueblo Leather") referenced in the site's navigation and copy, styled as a small outlined chip in the tan accent color to reinforce material storytelling on PDPs.

## Responsive Behavior

Recommended, not measured breakpoints:

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| mobile    | ≤ 749px    | single-column, nav collapses to hamburger, product grid 2-up |
| tablet    | 750–989px  | product grid 3-up, nav may remain collapsed |
| desktop   | ≥ 990px    | full horizontal nav, product grid 4-up, hero at full width |

Touch targets should be at least 44px tall (aligning with the observed `min-height:44px` default on `.shopify-payment-button__button`). Navigation collapse, drawer/off-canvas cart behavior, and any sticky-header behavior were not observed in the supplied CSS and are recommendations only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS custom properties, selector fragments, and a page-text excerpt only — no live rendering, DOM screenshots, or interaction testing were performed. Semantic role assignments (e.g., treating `#89928a` as "muted" or `#dddddd` as "hairline") are inferred from typical Shopify theme conventions, not from explicit CSS comments. Heading/body font family names (Baskerville, Montserrat) are inferred from the font-stack list since the actual computed values of `--font-heading-family`/`--font-body-family` were not resolved in evidence; availability and licensing of any custom/paid fonts were not verified. All component states (hover, focus, active, disabled, error) are proposed, not observed. Numeric type scale (font sizes above the two confirmed 1.5rem values) and the responsive breakpoint table are proposed design defaults, not measured from source. Third-party widget colors (Judge.me gold/star yellow) are visually present in the codebase but are not confirmed as intentional brand colors.
