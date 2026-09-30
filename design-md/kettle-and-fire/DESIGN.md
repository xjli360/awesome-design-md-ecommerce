---
version: alpha
name: "Kettle and Fire"
source_url: "https://kettleandfire.com"
captured_at: "2026-09-28T09:27:21.485426+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kettle & Fire's observed palette centers on a warm, food-safe cream
  (#fff5db) used as the primary canvas/body background, paired with a
  near-black ink (#221e1e) for body copy and secondary UI elements. The
  brand red (#db1e14) drives primary calls-to-action, with a deeper
  oxblood (#660e09) confirmed as the button hover state. A soft parchment
  tone (#ebe3d4) is proposed as a card/surface-soft background to echo the
  cream canvas without full contrast. Hairlines use the observed
  #e5e5e5 border color. A small set of muted grays (#939393, #999999,
  #f2f2f2) is repurposed for secondary text and disabled states, since no
  distinct disabled-specific hex was present in the supplied palette. An
  olive-khaki (#edeca6) and a deep red-brown (#aa141d) are proposed for
  promotional/badge accents, drawing on the site's stock-up and discount
  messaging. Typography reuses the CSS custom properties directly: Coastal
  for headings, Excelsior for body copy, Sanremo for buttons/subheaders,
  and Montserrat for small UI text, all with sans-serif fallback. Rounded
  and spacing scales are proposed conventions, informed by the observed
  50px pill button radius. Semantic role names (surface-soft, badge-alert,
  focus-ring) are inferred groupings of observed hexes, not verified brand
  tokens.

colors:
  primary: "#db1e14"
  on-primary: "#ffffff"
  secondary: "#221e1e"
  ink: "#221e1e"
  body: "#221e1e"
  canvas: "#fff5db"
  surface-card: "#ffffff"
  surface-soft: "#ebe3d4"
  muted: "#939393"
  hairline: "#e5e5e5"
  accent-hover: "#660e09"
  disabled-text: "#999999"
  disabled-bg: "#f2f2f2"
  badge-alert: "#aa141d"
  badge-highlight: "#edeca6"
  focus-ring: "#5897fb"
  footer-bg: "#fff5db"
  footer-text: "#000000"
typography:
  display-xl: {fontFamily: "'Coastal', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.4, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Coastal', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  title-md: {fontFamily: "'Sanremo', sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "'Excelsior', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Excelsior', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "'Montserrat', sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.3px}
  button-md: {fontFamily: "'Sanremo', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.42, letterSpacing: 0.2px}
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
    padding: "{spacing.sm} {spacing.lg}"
    hoverBackgroundColor: "{colors.accent-hover}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    hoverBackgroundColor: "{colors.muted}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focusBorderColor: "{colors.focus-ring}"
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
    badgeBackground: "{colors.badge-highlight}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    resultTextColor: "{colors.ink}"
    resultHoverBackground: "{colors.surface-soft}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary**: Maps directly to the observed `.btn` rule — red background, white text, 50px radius rendered here as `{rounded.full}`, with the confirmed hover shade `#660e09`. Active/pressed state darkening was present in source CSS but used a hex outside the supplied palette, so it is not reproduced; hover color is proposed to double as the active state.

**button-secondary**: Based on `.btn--secondary`, which swaps the background to `--c-secondary` (#221e1e). The hover behavior in source CSS referenced a gray outside the supplied palette; `{colors.muted}` is substituted as a proposed approximation.

**text-input**: Not directly observed in the supplied CSS; proposed using the cream/white surface and hairline border pattern seen elsewhere on the site, with a blue focus ring inferred from the one observed blue value (#5897fb), likely a default browser/link-adjacent accent.

**nav-bar**: Inferred from the cream body background and header search markup; exact header height, sticky behavior, and icon set were not present in the supplied evidence.

**product-card**: Proposed pattern for bone-broth/tallow product tiles referenced in navigation text (Beef Bone Broth, Tallow, etc.). No card CSS was supplied, so padding, radius, and badge placement are inferred defaults appropriate to a grid of packaged food products.

**hero**: Grounded in the observed `.wayfx-hero__slider` dot-indicator rule (white inactive dots at 0.5 opacity, black active dot), confirming a slider hero exists; overall hero copy layout and imagery are not observed and are proposed.

**footer**: Backed by explicit `--c-footer-bg`, `--c-footer-text` custom properties. The originally-referenced footer social-link gray (#bbbbbb) was outside the supplied color-evidence array and has been replaced with the observed muted gray token for link color.

**badge**: Proposed component for promotional labels ("20% OFF", "FALL STOCK-UP", bestseller counts) visible in page text; no badge CSS was supplied, so color pairing (alert red + khaki highlight) is an inferred stylistic choice from the broader palette.

**search**: Grounded in `.wfx-header__search-results` rules, which confirm result-row padding, a #2d2d2d-adjacent text tone (approximated here with ink), and a muted icon color (#949493-class gray, approximated with `{colors.muted}`).

**subscription-card**: Category-appropriate component proposed for the site's visible "subscribe & save 20% off for life" messaging; no dedicated CSS was supplied, so surface color and radius are inferred from the broader cream/parchment palette.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <600px | Single-column stacking, nav collapses to hamburger/menu icon, hero slider dots remain touch-swipeable |
| tablet | 600–1024px | Two-column product grids, condensed nav labels |
| desktop | >1024px | Full multi-item nav, multi-column product/recipe grids |

Touch targets should be a minimum of 44x44px for buttons and nav icons. Navigation and search dropdowns are recommended to collapse into an accordion or off-canvas panel below the tablet breakpoint. This table is a general responsive recommendation based on standard e-commerce patterns; it is not derived from measured breakpoints, media queries, or observed mobile rendering of kettleandfire.com.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is built from static CSS/text extraction only; no live rendering, computed styles, or interaction testing was performed. Several role names (surface-soft, badge-alert, badge-highlight, focus-ring, disabled-text, disabled-bg) are inferred semantic groupings of colors present in the supplied palette array — their actual usage on the live site is not confirmed. Two hex values referenced in raw `:root` CSS (`--c-footer-social-link: #bbbbbb` and the `.btn:active` hex `#370805`) were excluded because they did not appear in the supplied observed-colors evidence array; nearby palette colors were substituted instead. All typography sizes, weights beyond those explicitly stated (body 14px/1.6, headings 400/1.4, buttons 700), letter-spacing, and the entire spacing/rounded scale are proposed conventions, not measured values. Component layouts (product-card, hero copy structure, nav-bar, subscription-card) are inferred from page text and category norms, not observed markup or screenshots. Custom font families (swear-display, Coastal, Excelsior, Sanremo, ASPalmer, Swear, wayfx) are used only as named in CSS; their availability, licensing, and rendering fallback behavior were not verified. Mobile/responsive behavior is a proposed recommendation only.
