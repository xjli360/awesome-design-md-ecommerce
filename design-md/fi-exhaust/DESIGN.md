---
version: alpha
name: "FI Exhaust"
source_url: "https://www.fi-exhaust.com"
captured_at: "2026-09-29T04:19:00.993974+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from Bootstrap-derived utility classes and one
  custom typeface import found in style.css. The brand voice leans dark and
  mechanical: black outlines on white product cards, a single saturated red
  (#ca1f3f, darkening to #b2151b on hover) as the primary action color, and
  square-cornered form controls with no radius. Headings and body copy share
  the imported 'Exo' family with a wide 1.5px letter-spacing, giving the
  site a technical, stenciled feel appropriate for a performance-exhaust
  brand. Bootstrap's default gray/state palette (#212529, #495057, #808080,
  #dee2e6, #f8f9fa, plus semantic reds/greens/blues) is present in the
  evidence and is treated here as the underlying utility layer for text,
  borders, and status messaging (form validation, alerts), not as bespoke
  brand color. Rounded pills appear only on carousel dot indicators
  (border-radius:50%), so "full" rounding is reserved for small indicator
  and badge elements while cards, inputs, and buttons stay flat. Section
  rhythm, exact type sizes, and breakpoints are not present in the evidence
  and are proposed placeholders for a data-dense automotive-parts catalog
  (spec sheets, fitment filters, dealer locator).

colors:
  primary: "#ca1f3f"
  primary-hover: "#b2151b"
  ink: "#212529"
  body: "#000000"
  body-secondary: "#495057"
  muted: "#808080"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  hairline: "#dee2e6"
  dark: "#343a40"
  on-primary: "#ffffff"
  danger: "#dc3545"
  success: "#28a745"
  info: "#17a2b8"
  warning: "#ffc107"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 1.5px}
  display-md: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 1.5px}
  title-md: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 1.5px}
  body-md: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.25px}
  body-sm: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.25px}
  caption: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Exo', 'Helvetica Neue', Roboto, Arial, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 1.5px}
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
    padding: "{spacing.sm} {spacing.lg}"
    hover:
      backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
    hover:
      backgroundColor: "{colors.dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.body}"
    rounded: "{rounded.none}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  search:
    container: "{components.text-input}"
    icon: "Font Awesome caret glyph, positioned inset-right, {colors.body}"
    dropdownSurface:
      backgroundColor: "{colors.canvas}"
      hairline: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    itemSpacing: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    eyebrowTypography: "{typography.caption}"
    titleTypography: "{typography.display-xl}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.section}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    marginBottom: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    metaColor: "{colors.muted}"
  product-spec:
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.muted}"
    divider: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  carousel-indicator:
    size: "8px"
    rounded: "{rounded.full}"
    inactiveColor: "#4d4d4d"
    activeBackground: "{colors.canvas}"
    activeBorder: "#4d4d4d"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

**button-primary** maps directly to the observed `.btn-fi` rule: solid `#ca1f3f` fill, white text, matching-color 1px border, darkening to `#b2151b` on hover. Proposed for primary CTAs like "Buy" and "More +".

**button-secondary** mirrors `.btn-fi-dark`: black fill with a white 1px border, darkening toward `#222` (approximated here as `{colors.dark}`) on hover — proposed for lower-emphasis actions inside dark hero/news panels.

**text-input** reflects `.form-control` rules used in product-search and dealer-filter forms: square corners (`border-radius:0`), black border, no observed fill color beyond canvas white.

**search** extends text-input with the Font Awesome caret glyph absolutely positioned at the right edge, as seen in `.form-group::before`; dropdown/result surfaces are proposed, not observed in the evidence.

**nav-bar** is inferred from the text-only header items (PRODUCT, NEWS, REVIEW, ABOUT US, FAQ, DEALER, LIFESTYLE, CONTACT US) plus the dark button styling used elsewhere on the site; exact bar background/height are proposed.

**hero** is inferred from the "Featured" / "CEL-Free Experience" banner copy; dark background and large display type are proposed to match the brand's black/red performance tone, not measured.

**product-card** matches `.product-card` exactly: black 1px outline, 1.25rem padding, 2rem bottom margin, gray (`#808080`) metadata text for brand/year/material rows, and default-ink title links (`#212529`).

**product-spec** reflects `.product-spec` rules where labels use a lighter gray (~`#9d9d9d`, approximated to `{colors.muted}` since the exact hex is outside the supplied core palette) and values use `#808080`; useful for exhaust dimensions, pipe diameter, and material callouts.

**badge** and **carousel-indicator** are proposed small UI pieces: the badge borrows the primary red for "CEL-Free" or "New" flags, while the indicator dot styling is taken directly from `.product-carousel .carousel-indicators li` (circular, gray, active state turning white with a gray ring).

**footer** is inferred from the black `.mobile-filter .btn` and dark button precedent plus the plain-text footer content (copyright, Terms/Privacy links); no explicit footer CSS was supplied.

## Responsive Behavior

Recommended, not measured from live site:

| Breakpoint | Width | Notes |
|---|---|---|
| sm | ≥576px | Stacked nav collapses to a mobile filter/menu button (`.mobile-filter .btn` suggests an existing off-canvas or collapsed filter pattern). |
| md | ≥768px | Product-card grid moves from 1 to 2 columns. |
| lg | ≥992px | Full nav bar visible inline; product grid 3 columns. |
| xl | ≥1200px | Hero and carousel reach full-bleed width; grid 4 columns. |

Touch targets on buttons and filter controls should stay ≥44px tall given the padded `.btn-fi` sizing implied by `.mobile-filter .btn { padding-top: .5rem }`. Carousel prev/next controls are hidden until hover per `#productCarousel:hover`, so touch devices should force-show these controls or replace hover-reveal with swipe gestures — this touch fallback is proposed, not confirmed in the evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot; no rendered layout, computed spacing, or breakpoint values were observed. Font sizes, line-heights, and the full spacing/rounded scales are proposed defaults, not extracted measurements — only the `'Exo'` family, its 1.5px global letter-spacing, `border-radius:0` inputs, and the `50%` carousel-dot radius are directly evidenced. Some CSS-cited grays (`#4c4c4c`, `#9d9d9d`) fall outside the supplied core color-palette array and were approximated to `{colors.muted}` rather than added as new tokens. Hover/focus/active states beyond `.btn-fi:hover`, `.btn-fi-dark:hover`, and `.carousel-indicators .active` are proposed. Mobile menu behavior, dealer-locator map UI, and product-image carousel interaction are referenced only by class names, not observed behavior. Custom font (`Exo`, via Google Fonts) availability and licensing were not independently verified beyond the `@import` declaration.
