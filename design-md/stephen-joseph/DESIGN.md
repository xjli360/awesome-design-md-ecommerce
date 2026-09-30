---
version: alpha
name: "Stephen Joseph"
source_url: "https://stephenjosephgifts.com"
captured_at: "2026-09-28T05:05:45.676268+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Stephen Joseph Gifts sells kids' backpacks, luggage, lunchboxes, and related
  gear, and its storefront CSS shows a Bootstrap-derived foundation layered
  with a small set of brand-specific choices. The observed palette leans on
  strict black (#000000) and white (#ffffff) for structural chrome—header
  background, primary text, and buttons—while a single distinct accent blue
  (#208fea) marks interactive states such as nav-dropdown hover and
  special-price text. Bootstrap's stock grays (#6c757d, #dee2e6, #f8f9fa,
  #e9ecef) supply muted text, hairlines, and soft surfaces; Bootstrap's
  standard success/danger/warning hues (#28a745, #dc3545, #ffc107) are
  retained for status and sale messaging. A separate orange-red (#f04723)
  appears outside the Bootstrap variable set and is treated here as an
  inferred accent for sale/promo emphasis, not confirmed as a primary brand
  color. Typography combines system fallbacks with three named families
  actually present in the CSS—Questrial, Nunito, and Karla—which this
  document assigns to display, heading, and body roles respectively based on
  their typical single-weight (Questrial) versus rounded-friendly (Nunito/
  Karla) character, appropriate for a playful kids' product catalog. No
  spacing scale, radii, or breakpoints were directly measured; those below
  are proposed conventions sized for a product-grid retail layout.

colors:
  primary: "#000000"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#208fea"
  accent-warm: "#f04723"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#ffc107"
  border-subtle: "#e9ecef"
typography:
  display-xl: {fontFamily: "Questrial, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Questrial, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Nunito, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Karla, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Karla, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Karla, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.accent}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.accent}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-subtle}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.accent-warm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    linkHoverColor: "{colors.accent}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  pattern-swatch:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
    selectedBorderColor: "{colors.accent}"

## Components

**button-primary** renders on a solid black fill with white text, matching the `.header-bg-color` and `--primary:#000000` values found in the Bootstrap root variables; used for primary calls-to-action like "Add to Cart."

**button-secondary** is a proposed lighter counterpart using the soft gray surface and a hairline border, intended for secondary actions (e.g., "View Details") where a full black fill would be too heavy in a dense product grid.

**text-input** follows the plain white/black input styling seen in `.bottom_header .header_search .input-group-field`, with a proposed focus ring in the accent blue since no focus state was captured in the CSS.

**nav-bar** reflects `.header-bg-color` (black) paired with white nav text (`.left_bottom_header`, `.bottom_header a`) and uses the confirmed `#208fea` hover color drawn from the mega-menu dropdown hover rule.

**product-card** is a proposed pattern for the product-grid listings referenced in `.products-grid .product-item`; sale pricing is mapped to the orange-red accent as an inferred merchandising color, since `.special-price` styling in the source CSS was truncated before its color value could be confirmed.

**hero** is a proposed banner treatment using the soft surface background and display typography; no hero markup or imagery was present in the supplied evidence.

**footer** mirrors the black header treatment for visual bookending, a proposed symmetry rather than an observed footer rule.

**badge** is proposed for "Sale," "New," or "Coming Soon" labels seen in the product-text excerpt (e.g., "Coming Soon," "Previously $X.XX"), using the warm accent for visibility.

**search** reuses the confirmed `.search-header` white background with black border-bottom and text color from the supplied CSS.

**pattern-swatch** is a category-specific, fully proposed component for selecting "All Over Print" designs common across this brand's backpacks, luggage, and lunchboxes—no swatch markup was present in the evidence, so sizing and interaction are inferred conventions only.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| xs | 0–575px | Single-column product grid, collapsed hamburger nav, stacked header search |
| sm | 576–767px | 2-column product grid |
| md | 768–991px | 3-column product grid, inline search bar |
| lg | 992–1199px | Full mega-menu nav, 4-column product grid |
| xl | 1200px+ | Max-width container, 4–5 column grid |

Touch targets for buttons and nav items should be at least 44×44px. The primary navigation is expected to collapse into a slide-out or accordion menu below the `md` breakpoint, consistent with the category-heavy mega-menu implied by the CSS selectors, but this collapse behavior was not directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS and page-text extraction only; no rendered layout, real breakpoints, or interaction states (hover, focus, active, disabled) were observed.
- Several selectors in the source were truncated (e.g., `.special-price` color, `nu .site-nav-dropdown`), so some color-to-role mappings, especially the sale-price and accent-warm assignment, are inferred rather than confirmed.
- Font availability and licensing for Questrial, Nunito, and Karla were not verified; fallback stacks assume standard web-safe or Google Fonts hosting but this was not confirmed in the evidence.
- All spacing, radius, and typographic size/weight values not explicitly present in the supplied CSS are proposed conventions for a kids' retail catalog, not measured site values.
- Mobile navigation collapse, drawer behavior, and cart/checkout flows were not present in the supplied evidence and are described only as recommendations.
