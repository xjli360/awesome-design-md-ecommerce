---
version: alpha
name: "Barnes Made"
source_url: "https://barnesmade.com"
captured_at: "2026-09-28T10:24:14.166846+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Barnes Made's available CSS evidence comes largely from Squarespace's shared
  product-component stylesheet rather than bespoke brand styling, so this
  interpretation leans conservative. The confirmed palette is neutral and
  editorial: near-black text (#0e0e0e, #222222) on white (#ffffff), a light
  gray surface (#f2f2f2) and a muted gray hairline/disabled tone (#cccccc).
  The only saturated colors observed are red-family values (#cc0000, #db3642,
  #c32d38) used for out-of-stock states, scarcity messaging, and validation
  alerts — inferred here as the brand's single accent, reused for primary
  actions in the absence of any other observed hue. Typography is set in
  "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif," a serif-adjacent
  named font paired with standard sans fallbacks; its availability/licensing
  as a custom face is unverified from static CSS alone. Observed text
  treatments include a 14px/22px body style, 12px status copy, and an
  uppercase 9.75px label with 0.75px letter-spacing, which anchor the
  proposed type scale. The resulting system favors a quiet, artisanal,
  ingredient-forward aesthetic — dark ink on white with a single warm-red
  accent for calls to action and stock alerts — appropriate for a small-batch
  Vermont soap and candle maker.

colors:
  primary: "#db3642"
  ink: "#0e0e0e"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#cccccc"
  hairline: "#cccccc"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  danger: "#cc0000"
  danger-strong: "#c32d38"
  overlay: "#000000"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 22px, letterSpacing: 0px}
  caption: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 16px, letterSpacing: 0px}
  button-md: {fontFamily: "Clarkson, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 9.75px, fontWeight: 500, lineHeight: 16px, letterSpacing: 0.75px}
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
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  quantity-stepper:
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.transparent}"
    padding: "{spacing.none}"

## Components

**button-primary** uses the sole observed accent (a red in the #db3642/#c32d38 family) as an inferred primary action color, since no other saturated hue appears in the evidence; text is set on-primary white. Proposed for "Add to Cart" and checkout actions.

**button-secondary** is an outlined, ink-on-transparent treatment for lower-emphasis actions like "Quick View," inferred from the site's otherwise monochrome UI language rather than directly observed borders.

**text-input** proposes a bordered field using the observed #cccccc hairline/disabled gray and body-sm typography; the focus and error states are not confirmed but color:#000 on select:focus was observed, supporting an ink-colored focus text state.

**nav-bar** is a white bar with ink text and a hairline bottom border, proposed from the general light-canvas/dark-text pattern; the actual collapsed/mobile menu markup ("Open Menu"/"Close Menu" text was observed) confirms a toggle exists but not its visual styling.

**product-card** renders product tiles (soap bars, candles) on a white surface with a hairline border, using body-sm for names/prices; the scarcity/out-of-stock text color (#cc0000/#c32d38) is directly observed and should be applied to low-stock messaging within the card.

**hero** proposes a soft, light-gray-backed introductory section for the "Handcrafted in Vermont" statement, sized with the largest display typography; background choice is inferred, not measured.

**footer** inverts to an ink background with white text, a common pattern for small artisan sites; this specific inversion is proposed, not confirmed from the supplied CSS.

**badge** is directly grounded in observed CSS: a dark (#222) background with white uppercase text, absolute-positioned in the original product image corner — reused here as a generic status/label component (e.g., "New," "Limited").

**search** proposes a pill-shaped, soft-surface input for site search; no search-specific CSS was supplied, so styling is fully inferred from the broader neutral palette.

**quantity-stepper** reflects the observed product-quantity-input-wrapper: a borderless, transparent, center-aligned numeric input inheriting text color — a category-appropriate control for selecting soap/candle quantities before add-to-cart.

## Responsive Behavior

Proposed breakpoints (not measured): mobile up to 599px, tablet 600–959px, desktop 960px and above. The observed "Open Menu / Close Menu" text pair implies a collapsible navigation pattern on smaller viewports, but its exact trigger width and animation are not present in the evidence. Recommend touch targets of at least 44×44px for cart, quantity-stepper, and nav-toggle controls, single-column stacking of product-card grids below 600px, and preserving the badge's absolute top-right placement across breakpoints since no responsive override was supplied.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from a static CSS/text excerpt dominated by Squarespace's shared product-component stylesheet, not page-specific layout rules; actual hero, nav, and footer markup/styling were not present in evidence and are marked proposed. The brand "primary" color is an inferred choice from red tones used for scarcity/error states (#cc0000, #db3642, #c32d38) — no confirmed brand-accent usage (e.g., on buttons or links) was observed. "Clarkson" is used as the primary font-family value in the stylesheet, but its licensing, weight availability, and whether it is a paid/custom font versus a system-available one are unverified. All spacing, rounded-corner, and breakpoint values beyond the handful of explicit pixel figures in the source CSS are proposed conventions, not measurements. No interactive states (hover, focus, active, disabled) beyond the single observed select:focus color and out-of-stock red were confirmed, and no mobile/responsive layout was directly observed.
