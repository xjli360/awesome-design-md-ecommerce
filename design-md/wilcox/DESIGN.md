---
version: alpha
name: "Wilcox"
source_url: "https://wilcoxallpro.com"
captured_at: "2026-09-28T10:34:24.237679+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wilcox All-Pro is a USA-made heavy-duty gardening-tool brand built on a "lifetime guarantee"
  and no-nonsense durability positioning ("Sharpest Tool in the Shed! Since 1966"). The observed
  stylesheet is a standard e-commerce theme (Bootstrap-derived utility classes, alert/table
  color sets) layered with one brand-specific rule: a `.header` background of `#7676b3`, a muted
  violet-blue that is the strongest brand signal in the evidence and is treated here as the
  primary accent, even though it sits somewhat apart from the tool-shop subject matter. Body
  copy uses `"Helvetica Neue", Helvetica, Arial, sans-serif` at 16px/1.43 in `#595959` on a white
  canvas — this pairing is directly observed and used as the system's sole confirmed font stack.
  Font names such as Lato, Montserrat, Open Sans, and Playfair Display SC appear in the site's
  loaded font list but are not tied to any supplied selector, so they are omitted from typed
  roles as unconfirmed. Status and badge colors (warning amber, danger red, success green) are
  inferred from Bootstrap-style alert classes present in the CSS and are mapped here to product
  states like "(blemish)" and "SALE" call-outs seen in the page text. Layout, spacing, and
  component geometry below are proposed conventions, not measured observations.

colors:
  primary: "#7676b3"
  ink: "#262626"
  canvas: "#ffffff"
  body: "#595959"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-link: "#005fbf"
  border-input: "#cccccc"
  sale: "#ff0000"
  success: "#3c763d"
  success-bg: "#dff0d8"
  warning-ink: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  danger-ink: "#a94442"
  danger-bg: "#ffe5e5"
typography:
  display-xl: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 40px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.25px}
  display-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 28px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4285714, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "{colors.hairline}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.sale}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderTop: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning-bg}"
    borderColor: "{colors.warning-border}"
    textColor: "{colors.warning-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  guarantee-callout:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components
**button-primary** uses the header's `#7676b3` brand tone as the fill with white text, intended for primary conversion actions like "Add to Cart" or "Checkout." State transitions (hover/active/disabled) are proposed, not observed.

**button-secondary** is an outlined variant sharing the primary hue for border and text on a white fill, suited to lower-emphasis actions such as "View All" or "Continue Shopping"; interaction states are proposed.

**text-input** takes the observed neutral border color `#cccccc` from the theme's form-control conventions, with dark ink text and generous padding to suit a simple product-search or checkout form. Focus-state styling is not observed and is proposed as a primary-colored border.

**nav-bar** is modeled as a white bar with a light hairline division, since no header-specific text color was supplied beyond the violet-blue background block; link hover in primary color is a proposed convention to tie navigation back to the brand accent.

**product-card** reflects the storefront's grid of trowels, weeders, and probes seen in the page text, with sale pricing rendered in the observed `#ff0000` red used for `.product-price[data-on-sale]` spans. Card elevation/shadow was not supplied and is omitted rather than invented.

**hero** proposes the primary violet-blue as a full-bleed banner background for the "Sharpest Tool in the Shed! Since 1966" headline, since this is the only large-surface brand color in evidence; actual homepage hero styling was not directly supplied.

**footer** uses the light gray surface tone with muted gray text, consistent with the theme's neutral surface palette, for the observed site-link list (Home, About, Products, Contact, Terms).

**badge** maps to the "(blemish)" and discount-percentage labels visible in the product excerpt, using the Bootstrap-style warning triad (`#fcf8e3` / `#faebcc` / `#8a6d3b`) found in the CSS evidence — a reasonable, evidence-grounded fit for a secondary/clearance indicator, though its exact use on this element is inferred.

**search** is a proposed lightweight input pattern for the "Search" nav item, using the theme's soft-gray surface and hairline border; no dedicated search-box CSS was supplied.

**guarantee-callout** is a category-appropriate component built for Wilcox's central trust message ("backed with a lifetime guarantee... replace them no questions asked"), using the observed Bootstrap success green/green-tint pair to visually reinforce durability and trust messaging on product or about pages. This pairing is inferred from generic alert styling, not a confirmed brand usage.

## Responsive Behavior
Proposed breakpoints (not measured from the live site): mobile ≤ 599px, tablet 600–959px, desktop ≥ 960px. Navigation should collapse into a toggled menu below tablet width, consistent with the "Toggle navigation" label seen in the page text, though actual collapse behavior and menu animation were not observed. Touch targets on buttons and nav items should maintain a minimum 44×44px hit area. Product-card grids are recommended to reflow from a multi-column desktop layout to a single or two-column mobile layout; exact column counts were not supplied and are a design recommendation only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS/text extraction only; no rendered screenshots, computed layout, or DOM structure were available. The `#7676b3` primary role is inferred solely from a single `.header` background rule and may not represent the full brand identity. Font families beyond the confirmed `"Helvetica Neue", Helvetica, Arial, sans-serif` body/heading stack (e.g., Lato, Montserrat, Open Sans, Playfair Display SC) appear in the site's loaded assets but have no selector evidence tying them to specific roles, so they were excluded from typed tokens. All font sizes beyond the confirmed 16px body value are proposed, not measured. Hover, focus, active, and disabled interaction states, as well as mobile menu behavior, are proposed conventions and were not observed. Licensing and availability of any non-system font referenced in the site's asset list were not verified and should be confirmed before production use.
