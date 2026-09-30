---
version: alpha
name: "QuickJack"
source_url: "https://quickjack.com"
captured_at: "2026-09-28T10:02:58.816624+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  QuickJack's storefront runs on a Magento/Bootstrap foundation, evidenced directly
  by the :root custom-property block (--primary:#007bff, --secondary:#6c757d,
  --light:#f8f9fa, --dark:#343a40) and the .btn-primary rule that ties #007bff to
  the primary call-to-action. Body copy uses the Bootstrap system-font stack
  (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial) at 1rem/1.5 line-height
  in #212529 on a white canvas, confirmed by the body selector. The wider palette
  mixes Bootstrap utility colors (success green #28a745, danger red #dc3545,
  warning yellow #ffc107, info cyan #17a2b8) with several warmer, brand-leaning
  tones -- #ff5501, #ff5216, #e02b27, #f05f40 -- and a deep navy #1c2537. Because
  no selector in the supplied CSS attaches these to a specific component, their
  role as accent/highlight and dark-surface colors is inferred, not confirmed,
  from repetition and hue clustering. This interpretation treats #007bff as the
  functional primary action color (directly observed), reserves the orange
  cluster for promotional or highlight accents typical of a lift-capacity/sale
  callout, and uses #1c2537 as an inferred dark header/footer surface. Rounded
  corners follow the observed .btn border-radius of .25rem (4px).

colors:
  primary: "#007bff"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent: "#ff5501"
  accent-alt: "#006bb4"
  dark-surface: "#1c2537"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#ffc107"
  info: "#17a2b8"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0.2px}
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
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    borderColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripeColor: "rgba(0,0,0,.05)"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.md}"

## Components
- **button-primary**: Directly grounded in the `.btn-primary` rule (`#007bff` background, white text, `.25rem` radius). Used here as the default add-to-cart / "Shop Now" action. Hover/active states are proposed, not observed.
- **button-secondary**: An outlined variant using the Bootstrap `secondary` gray for lower-emphasis actions like "Compare Models" or "Explore Accessories." Border and hover fill are proposed.
- **text-input**: Styled from the generic Bootstrap form reset (`button,input...{font-family:inherit}`); border, radius, and padding are proposed conventions, not measured from a specific input rule.
- **nav-bar**: Inferred from the presence of a "Toggle Nav" menu label in page text (Car Lifts, Accessories, How It Works, Support). Layout and sticky behavior are proposed; no nav-specific CSS was supplied.
- **product-card**: Represents the accessory/model grid seen in the excerpt (Box Complete, Drop-In Tray Set, Caster Kit, etc.), each with title, price, and "Shop Now" link. Card background and spacing are proposed; the source data confirms only the content pattern, not the visual container.
- **hero**: Represents the "New Models" / "Better way to lift" banner sections. Dark-navy background is inferred from the presence of `#1c2537` in the palette; no hero-specific selector was supplied.
- **footer**: Proposed dark surface reusing the same inferred navy, holding contact info (phone number) and secondary links; exact footer markup was not in the evidence.
- **badge**: Proposed component for capacity callouts ("3,500-lbs.", "6,000-lb.") or "Most Popular Model" tags, using the orange accent color observed repeatedly in the palette (`#ff5501`/`#ff5216`) as a plausible highlight hue.
- **search**: Proposed header search field; no search-specific selector was in the supplied CSS, so styling follows the generic light-surface/input convention.
- **spec-table**: Grounded in the supplied `.table-striped`/`.table-hover` rules, appropriate for the site's "Compare Models" and lift-capacity comparison tables referenced in the page text.

## Responsive Behavior
Proposed breakpoints (not measured from live rendering), aligned to the Bootstrap `--breakpoint-*` custom properties present in `:root`:

| Breakpoint | Width | Behavior (proposed) |
|---|---|---|
| xs | 0px | Single-column stack; nav collapses to toggle/hamburger |
| sm | 576px | Two-column accessory/product grid begins |
| md | 768px | Nav expands to inline links; hero text scales up |
| lg | 992px | Three/four-column product grid; sidebar filters visible |
| xl | 1200px | Max-width container; full desktop spacing |

Touch targets should be at least 44x44px for buttons and nav toggles. This table is a recommendation based on standard Bootstrap breakpoint values found in the CSS variables, not an observation of actual rendered layout or JavaScript-driven behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Color roles beyond `.btn-primary` (`#007bff`) are inferred from frequency and hue grouping, not from selector-level confirmation; the orange, navy, and secondary-blue assignments are educated guesses.
- No hero, footer, nav, or product-card CSS selectors were included in the supplied evidence; those components are reconstructed from page-text content patterns only.
- "Open Sans," "Roboto," and "Noto Sans" appear in the raw font list but the only confirmed `font-family` declaration (on `body`) is the Bootstrap system-font stack; any custom webfont usage, weight availability, and licensing are unverified.
- Typography sizes beyond the observed `body{font-size:1rem}` are proposed conventions, not measured from headings or specific selectors.
- No interaction states (hover, focus, active, disabled), mobile menu behavior, or JS-driven UI (cart, filters) were observed; all are proposed/standard patterns.
- Spacing and radius scales beyond the single observed `.btn{border-radius:.25rem}` value are proposed conventions for internal consistency, not extracted measurements.
