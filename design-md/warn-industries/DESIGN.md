---
version: alpha
name: "Warn Industries"
source_url: "https://warn.com"
captured_at: "2026-09-28T10:01:25.077612+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Warn.com presents a rugged, automotive-utility aesthetic built around a
  saturated red accent (#c22735) against a light gray canvas (#eeeeee) and
  near-black ink (#121212). The observed Shopify theme variables define this
  red as both button and link color, with white (#ffffff) as the on-primary
  text, and a matching light-gray secondary button surface reusing the
  canvas tone. Several close red variants (#bb2733, #b52532, #dd2739) appear
  across component CSS and are treated here as interchangeable hover/shade
  states of the same primary, since no single rule ties them to a distinct
  role. Supporting neutrals (#747474, #d5d2d2, #bdbdbd, #333333) come from a
  vehicle-fitment widget and suggest a muted, industrial gray system for
  secondary panels. A small set of functional colors (info blue #1990c6,
  success green #009e1d, pale success/danger tints) is present in checkout
  and form CSS and is mapped to standard UI feedback roles as an inference.
  Typography draws on four condensed/display families found in the font
  list — Agency FB Bold, Teko, Rajdhani, and Roboto Condensed — consistent
  with an automotive-accessory brand; exact element-to-font assignment is
  inferred, not directly observed. Corner radii trend toward 0px on
  buttons, reinforcing a squared, mechanical visual language.

colors:
  primary: "#c22735"
  primary-hover: "#b52532"
  ink: "#121212"
  canvas: "#eeeeee"
  body: "#333333"
  muted: "#797979"
  hairline: "#bbbbbb"
  surface-soft: "#f5f5f5"
  surface-card: "#f9faf8"
  surface-panel: "#d5d2d2"
  surface-panel-alt: "#bdbdbd"
  on-primary: "#ffffff"
  accent-dark: "#1b2529"
  info: "#1990c6"
  info-hover: "#136f99"
  success: "#009e1d"
  success-bg: "#ccffd9"
  danger-bg: "#ffcccc"
  slate: "#6c7a87"
typography:
  display-xl: {fontFamily: "'Agency FB Bold', 'Teko', sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: "0.5px"}
  display-md: {fontFamily: "'Agency FB Bold', 'Teko', sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.1, letterSpacing: "0.25px"}
  title-md: {fontFamily: "'Teko', sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.53, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Rajdhani', sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "'Rajdhani', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: "0.5px"}
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
  section: 60px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.on-primary}"
    borderColor: "{colors.hairline}"
    borderWidth: "2px"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "2px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
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
    backgroundColor: "{colors.on-primary}"
    borderColor: "{colors.hairline}"
    borderWidth: "2px"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fit-widget:
    backgroundColor: "{colors.slate}"
    panelBackground: "{colors.surface-panel}"
    resultBackground: "{colors.surface-panel-alt}"
    textColor: "{colors.on-primary}"
    accentButtonText: "{colors.info}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components
**button-primary** uses the observed `--color-button` red with white text, matching the Shopify theme's `--color-button-text` variable; squared corners follow the 0px radius seen on the accelerated-checkout and AI-block buttons. **button-secondary** inverts to a canvas background with red text/border, mirroring the theme's `--color-secondary-button` / `--color-secondary-button-text` pairing; hover state is proposed. **text-input** reflects the search field's observed white fill and `#bbbbbb` 2px border. **nav-bar** reuses the same hairline border-bottom found on `.header__inline-menu`. **product-card** is a proposed pattern (not directly observed) using the off-white `#f9faf8` surface tone present elsewhere in the palette, with condensed title typography for a category grid. **hero** is inferred, pairing the dark slate `#1b2529` with the large display font stack for category/landing banners; the site's custom `--warn-bg` background image confirms a full-bleed imagery pattern, though exact hero markup is not observed. **footer** is proposed, using ink-on-dark convention typical of the visible dark utility panels. **badge** is a proposed pill treatment for stock/fit indicators, not directly observed in the supplied CSS. **search** mirrors the real `#Inline-Search` input styling. **vehicle-fit-widget** is grounded directly in the `#vehicle-lookup`, `#info-container`, and `#answers-table` rules, including the `#747474` header, `#d5d2d2` panel, `#bdbdbd` results area, and `#93b8e2` button text color observed in the custom stylesheet.

## Responsive Behavior
Proposed breakpoints (not measured from live site): mobile ≤599px, tablet 600–989px, desktop ≥990px, following common Shopify Dawn-theme conventions implied by the CDN asset paths. Recommend a minimum 44px touch target for buttons and nav items, collapsing the inline nav menu into a drawer below 990px (consistent with the presence of a `header-drawer` selector in the evidence), and stacking the vehicle-fit widget's panel/result blocks vertically on narrow viewports. This section is a recommendation only; no responsive/mobile layout was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS custom properties and isolated selector rules, not a rendered DOM or visual screenshot, so real layout, spacing rhythm, and component composition are not confirmed. The `--font-body-family` variable's actual value was not resolved from the supplied evidence; font-to-role mapping (Agency FB Bold, Teko, Rajdhani, Roboto Condensed) is inferred from the font list order and general automotive-brand convention, not from direct selector-to-font CSS. The `body { font-size: 1.5rem }` value is used for body-md but may be a theme-level base variable rather than final rendered copy size. Several near-duplicate reds (#bb2733, #b52532, #dd2739, etc.) are treated as shade/hover variants without confirmed state bindings. Border-radius values beyond the observed 0px buttons are proposed defaults. Hover, focus, active, and error/success interaction states are proposed, not verified through interaction testing. Mobile/responsive layout behavior was not observed and is a recommendation only. Custom font availability, self-hosting, and licensing (particularly for Agency FB Bold) were not verified.
