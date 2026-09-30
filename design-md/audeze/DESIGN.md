---
version: alpha
name: "Audeze"
source_url: "https://audeze.com"
captured_at: "2026-09-28T04:25:31.730471+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Audeze's storefront CSS shows a neutral, editorial base — white canvas (#ffffff),
  near-black body copy (#161616) and charcoal headings (#333333) — layered with a
  narrow band of warm gold accents (#ca8d27, #af7a22, #9d6d1e) that recur across
  promo and badge-style declarations. A cyan/blue family (#00adef, #00b3ff, #09aeec)
  also appears repeatedly and is inferred here as a secondary "technology" accent,
  distinct from the gold, though its exact UI role is not confirmed by the supplied
  evidence. Typography is dominated by two proprietary stacks: "Verbatim Extended"
  variants for headlines/logo and "Visby" variants for body, nav and buttons, both
  falling back to sans-serif per :root custom properties. Observed h1 styling
  (32px, 400 weight, 1px letter-spacing, color #333333) anchors the display scale;
  larger display sizes here are proposed, not measured. Grays (#efefef, #f9f9f9,
  #dcdcdc, #8c8c8c) are read as surface, hairline and muted-text roles by
  convention, not by explicit semantic labeling in the CSS. The interpretation
  favors a restrained, high-contrast audio-gear aesthetic with gold used sparingly
  for emphasis and CTAs, keeping most surfaces neutral and letting product imagery
  carry visual weight.

colors:
  primary: "#ca8d27"
  ink: "#161616"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#8c8c8c"
  hairline: "#dcdcdc"
  surface-soft: "#f9f9f9"
  surface-card: "#efefef"
  on-primary: "#ffffff"
  primary-hover: "#af7a22"
  primary-active: "#9d6d1e"
  logo-ink: "#191919"
  heading-hover: "#363636"
  accent-tech: "#00adef"
  danger: "#cb1f2a"
  success: "#099e4d"
  border-strong: "#000000"
  disabled-text: "#888888"
typography:
  display-xl: {fontFamily: "'Verbatim Extended Medium', sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "1px"}
  display-md: {fontFamily: "'Verbatim Extended', sans-serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "1px"}
  title-md: {fontFamily: "'Visby Medium', sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Visby Regular', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Visby Regular', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Visby Light', sans-serif", fontSize: "11px", fontWeight: 300, lineHeight: 1.4, letterSpacing: "0.3px"}
  button-md: {fontFamily: "'Visby Medium', sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.logo-ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.logo-ink}"
    textColor: "{colors.surface-card}"
    linkTypography: "{typography.body-sm}"
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
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  audio-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-tech}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders CTAs (e.g., "Add to Cart," "Shop Now") using the observed gold accent as fill, with white text drawn from the Visby Medium button font-family declaration. Hover/pressed states using `primary-hover`/`primary-active` are proposed, not confirmed in the evidence.

**button-secondary** is a proposed outline/ghost variant for lower-emphasis actions (e.g., "Learn More"), using canvas background and a hairline border so it recedes against product photography.

**text-input** covers search and form fields; background and border colors are inferred defaults consistent with the site's neutral palette, since no explicit input styling was present in the supplied CSS.

**nav-bar** is modeled on the `.logo`/`.header__logo` and `#header .top-bar` rules, using the logo-ink color and small body typography; sticky/transparent states are proposed and not verified.

**product-card** reflects the `h2.product_name` and `.title.product_name` link-color rule (#333333), paired with an inferred light card surface (#efefef) to separate products from the white page background.

**hero** is a proposed full-bleed banner pattern for the homepage, using dark ink as a background to let large Verbatim Extended headline type and product imagery dominate; this specific composition was not directly observed.

**footer** is inferred from the dark logo-ink tone appearing elsewhere in the palette, paired with light surface text for contrast; actual footer markup/styling was not present in the supplied rules.

**badge** captures small labeling elements (e.g., "New," category tags) using the gold accent pill shape; rounded-full styling is a proposed convention, not evidenced directly.

**search** is inferred from the presence of fancybox/utility styling patterns and the general muted-gray text conventions (#888, #ccc) seen in disabled/hover states.

**audio-spec-panel** is a category-specific, proposed component for displaying planar-magnetic driver specs, pairing the muted surface tone with the cyan/blue accent to visually separate technical data from marketing copy — this is a design proposal, not an observed pattern.

## Responsive Behavior
This is a recommended, non-measured breakpoint scheme, since no media queries were included in the supplied evidence:

| Breakpoint | Width       | Notes                                  |
|-----------|-------------|-----------------------------------------|
| mobile    | 0–599px     | single-column, stacked nav, full-width buttons |
| tablet    | 600–1023px  | 2-column product grids, collapsed nav into menu |
| desktop   | 1024–1439px | full nav bar, 3–4 column product grids |
| wide      | 1440px+     | max-width content container, extra gutter |

Touch targets should be a minimum of 44×44px for buttons and nav items; primary navigation is assumed to collapse into a hamburger/menu pattern below tablet width. None of this responsive behavior was directly observed in the static CSS extraction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static CSS/selector snapshot and a color/font list, not a rendered or interactive audit. Specific limitations:

- **No layout observation**: grid structures, spacing rhythms, and component composition (hero, product-card, footer) are proposed patterns based on typical e-commerce conventions, not measured from live pages.
- **Uncertain semantic mapping**: several palette colors (e.g., #00adef, #cb1f2a, #099e4d) appear in the raw list without clear selector context; their assignment to "accent," "danger," and "success" roles is inferred and may not reflect actual site usage.
- **Proposed sizing**: most typography sizes beyond the observed h1 (32px) and body (14px) rules are estimated to fill out a usable type scale.
- **No interaction or mobile states observed**: hover, focus, active, and responsive collapse behaviors are proposed conventions, not captured in the supplied evidence.
- **Font licensing unverified**: "Verbatim Extended" and "Visby" family variants appear to be licensed/proprietary fonts; their availability, weights, and licensing terms were not verified and are not redistributable assumptions.
