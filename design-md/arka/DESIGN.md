---
version: alpha
name: "Arka"
source_url: "https://www.arka.com"
captured_at: "2026-09-28T04:05:47.873423+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Arka's storefront runs on a Shopify theme with Bootstrap-derived base styles
  layered under custom brand tokens. The CSS exposes explicit custom properties
  (--arka-primary-cta: #3d5675, --arka-secondary-background: #F2F3F4,
  --arka-danger: #E14744, --arka-blue-text: #011f3a) which are treated here as
  authoritative brand roles: a muted slate-blue for primary actions, a pale
  grey-blue for section backgrounds, and a deep navy for emphasis text. Body
  copy is set via the theme default (Helvetica Neue/Helvetica/Arial) at 14px
  with a 1.4286 line-height, both directly observed in base.css. Font variables
  for Lato, Euclid Flex, Futura, and Futura PT are declared at :root but their
  applied selectors are not present in the supplied evidence; this spec infers
  Lato as the likely display/heading family and Futura PT as a secondary title
  face, both labeled inferred. The remaining palette (Bootstrap alert colors,
  greys, link blues) is preserved for status and utility roles rather than
  discarded. Two saturated outliers (#f112b7, #fec7f6) appear in the raw color
  scan but are not tied to any observed selector and are treated as noise, not
  brand color. Layout, spacing, and component states below are proposed
  conventions, not measured page structure.

colors:
  primary: "#3d5675"
  ink: "#222222"
  navy: "#011f3a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  eyebrow: "#a1a1a1"
  hairline: "#dddddd"
  border-light: "#eeeeee"
  surface-soft: "#f2f3f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#337ab7"
  link-hover: "#23527c"
  disabled: "#cccccc"
  danger: "#e14744"
  danger-bg: "#f2dede"
  success: "#3c763d"
  success-bg: "#dff0d8"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  info: "#31708f"
  info-bg: "#d9edf7"
  accent-teal: "#72bda3"
typography:
  display-xl: {fontFamily: "'Lato', sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Lato', sans-serif", fontSize: 34px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Futura PT', sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.428571429, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Lato', sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.navy}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.eyebrow}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
  quote-calculator:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.body-sm}"
    ctaColor: "{colors.primary}"

## Components

**button-primary** is the core conversion action (e.g. "Get Instant Quote," "Add to Cart"), using the slate-blue `{colors.primary}` background observed as `--arka-primary-cta` with white text. Hover/active/disabled states are proposed, not observed.

**button-secondary** offers an outlined alternative for lower-emphasis actions like "Learn More," reusing `{colors.primary}` as a border and text color on a white field to avoid introducing new hues.

**text-input** covers quote-request and account forms; the hairline border and focus-to-primary transition are proposed conventions consistent with the Bootstrap-based form styling implied in the CSS, though no `:focus` rule was captured in evidence.

**nav-bar** is inferred from the presence of `.navbar-default` link rules (`color:#777`) in base.css; the proposed pattern uses body-grey links that shift to the brand blue on hover/active, a state not directly observed.

**product-card** supports the packaging-catalog grid (box styles, mailers, tape). Card chrome uses `{colors.border-light}` and `{rounded.md}`, both proposed defaults layered onto the plain white background rule found in base.css.

**hero** proposes a lead section using `{colors.surface-soft}` (the observed `--arka-secondary-background`) as a calmer backdrop for a large display headline in navy text, appropriate for sustainability/CTA messaging implied by the page title.

**footer** uses the deep `{colors.navy}` value observed as `--arka-blue-text` as a dark footer field with light `{colors.eyebrow}` link text, a common ecommerce pattern; exact footer markup was not present in evidence.

**badge** repurposes the Bootstrap alert-success pairing (`#dff0d8` / `#3c763d`) for small status labels such as "Eco-Friendly" or "In Stock," reusing existing palette rather than inventing new accent colors.

**search** proposes a standard header search field styled like `text-input`, since no distinct search-bar selector was present in the supplied CSS.

**quote-calculator** is a category-specific proposed component for Arka's core use case — custom box/quote configuration — styled as an elevated card using `{rounded.lg}` and the primary CTA color for its submit action; no calculator markup or interaction was present in evidence.

## Responsive Behavior

*Recommendation only — no responsive/mobile layout was observed in the supplied evidence.*

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 600px | Single-column stack, nav collapses to menu icon |
| Tablet | 600–1024px | Two-column product grid, condensed nav |
| Desktop | > 1024px | Full multi-column grid, expanded nav |

Touch targets should be at least 44px tall for buttons and inputs (`button-md` padding `{spacing.md} {spacing.lg}` approximates this). Navigation is expected to collapse behind a hamburger control below the tablet breakpoint; this is a standard ecommerce convention, not a measured behavior of arka.com.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction only; no rendered/live layout, computed sizes, or interaction states (hover, focus, active, error) were observed.
- Font application is uncertain: `Lato`, `Futura`, `Futura PT`, and `Euclid Flex` are declared as `:root` custom properties but no selector in evidence assigns them to specific elements; their use in this spec (display/title roles) is inferred, not confirmed.
- Custom font licensing and hosting (self-hosted vs. third-party) were not verified.
- All typographic sizes except `body-md` (14px / 1.428571429 line-height, directly observed) are proposed scale values, not measured.
- Two palette entries (`#f112b7`, `#fec7f6`) could not be tied to any selector and are treated as extraction noise rather than brand color.
- Component states (hover, focus, disabled, loading) beyond the Shopify payment-button skeleton animation are proposed patterns for a plausible ecommerce UI, not confirmed site behavior.
- Mobile navigation, cart, and checkout flow structure were not present in the supplied evidence.
