---
version: alpha
name: "Sjobergs"
source_url: "https://sjobergs.se"
captured_at: "2026-09-29T04:14:32.565664+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sjöbergs sells Swedish-made workbenches, benches, and workshop cabinetry for
  professionals, schools, and hobbyists. The extracted stylesheet exposes a
  restrained, utilitarian palette built around a cool sky-blue accent
  (#65b2e8) used for primary buttons and links, paired with a muted
  green-grey (#455854) reserved for review widgets and "on light" button
  states. Neutrals dominate: near-black text (#121212), mid-grey body copy
  (#4a4a4a), and a family of off-white/grey surfaces (#f8f8f8, #f2f2f0,
  #eeeeee, #dddddd) that likely structure page backgrounds, cards, and
  hairlines. Status colors (#3fbc20 success, #f42e4f error) and label
  backgrounds (#d6d8d3, #f5f5f5) are inferred from CSS custom properties for
  sale/new/sold-out badges.

  Typography relies on Nunito Sans as the observed webfont, with
  Arial/Helvetica/sans-serif fallbacks; heading and paragraph "font" custom
  properties reference named tokens whose actual family is not resolved in
  the evidence, so heading weight/family mapping below is inferred. The
  observed H1 rule (2.5rem/2.875rem, zero letter-spacing) anchors the
  display-md scale; all larger/smaller sizes are proposed. Border-radius is
  observed as 0 on checkout/review widgets, suggesting a squared, functional
  aesthetic consistent with a tools/workshop brand — the rounded scale below
  is offered for flexible UI use, not a claim of site-wide rounding.

colors:
  primary: "#65b2e8"
  ink: "#121212"
  canvas: "#f8f8f8"
  body: "#4a4a4a"
  muted: "#949990"
  hairline: "#dddddd"
  surface-soft: "#f2f2f0"
  surface-card: "#ffffff"
  on-primary: "#f8f8f8"
  secondary-accent: "#455854"
  tertiary-accent: "#d6d8d3"
  primary-grey: "#393f3e"
  secondary-grey: "#cfd0d5"
  success: "#3fbc20"
  error: "#f42e4f"
  sold-out-bg: "#f5f5f5"
  label-new-bg: "#d6d8d3"
typography:
  display-xl: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito Sans, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "transparent"
    textColor: "{colors.secondary-accent}"
    borderColor: "{colors.secondary-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary-grey}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    onSaleBg: "{colors.tertiary-accent}"
    onSaleText: "#1e242a"
    newBg: "{colors.label-new-bg}"
    newText: "#181b1a"
    soldOutBg: "{colors.sold-out-bg}"
    soldOutText: "#1e242a"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.secondary-grey}"
    iconColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
  price-tag:
    regularPriceColor: "{colors.body}"
    salePriceColor: "{colors.error}"
    typography: "{typography.body-md}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** uses the observed sky-blue accent (#65b2e8) as background with a light on-primary text color, matching the theme's `--button-bg`/`--button-content` variables; radius is set to none to reflect the observed zero-radius checkout buttons. **button-secondary** is a proposed outlined variant using the muted green-grey secondary accent, useful for "see all" or filter actions referenced in the navigation text. **text-input** is inferred from generic Shopify theme conventions since no explicit input styling was captured; border uses the light hairline grey observed in the palette. **nav-bar** reflects the site's multi-level category menu (Shop, Skola och utbildning, Förvaringsskåp, Om Sjöbergs) with a light canvas background and dark ink text, consistent with `--primary_text`. **product-card** is proposed for the dense product grids (Elite, Scandi, Nordic Pro) shown in the excerpt, using a white surface and hairline border for separation. **hero** is proposed for homepage banners like "Sjöbergs Elite" and "Junior/Senior" callouts, using the soft tertiary-grey surface as a calm backdrop. **footer** uses the dark primary-grey (#393f3e) as an inferred footer treatment for contrast, though actual footer styling was not directly observed. **badge** directly maps the observed `--label_*` custom properties for New/Sale/Sold Out states. **search** and **price-tag** are proposed, category-appropriate components supporting product discovery and the "Ordinarie pris" pricing pattern seen in the text excerpt.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width      | Layout guidance                                  |
|-----------|------------|---------------------------------------------------|
| mobile    | <600px     | Single-column nav collapses to hamburger/drawer   |
| tablet    | 600–959px  | 2-column product grid, sticky header retained      |
| desktop   | 960–1279px | 3–4 column product grid, full mega-menu            |
| wide      | ≥1280px    | 4+ column grid, max-width container centered       |

Touch targets should be at least 44px tall (aligned with the observed Shopify accelerated-checkout button clamp of 25–55px). Primary nav and category mega-menus should collapse into an accordion or drawer below tablet width; this collapse behavior is a recommendation and was not observed in captured markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, real interaction states (hover/focus/active), or actual mobile breakpoint behavior were observed. Heading and paragraph font tokens (`--type_heading_font`, `--type_primary_paragraph_font`) reference named custom properties whose resolved font-family value was not present in the evidence, so Nunito Sans is used as the best-supported observed webfont with generic fallbacks; actual heading font may differ. Font licensing/self-hosting status for Nunito Sans on this domain was not verified. Numeric type scale beyond the observed H1 (40px/46px line-height) is proposed, not measured. Border-radius values beyond the observed `0` on checkout and review widgets are inferred defaults for a flexible component system, not confirmed site-wide styling. Color role assignments (e.g., footer background, hero surface) are inferred pairings from the supplied palette and may not match true production usage.
