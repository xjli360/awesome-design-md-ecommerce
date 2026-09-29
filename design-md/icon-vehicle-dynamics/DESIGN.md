---
version: alpha
name: "ICON Vehicle Dynamics"
source_url: "https://iconvehicledynamics.com"
captured_at: "2026-09-28T09:42:20.910476+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  ICON Vehicle Dynamics presents itself as a rugged, precision-engineered performance brand
  for truck and SUV suspension, wheels, and armor. The observed palette is dominated by
  near-black inks (#000104, #050505, #141518) and neutral grays (#666666, #999999b, #cccccc,
  #d9d9d9, #f2f2f2) against a white canvas, consistent with an industrial, technical tone.
  A warm gold/amber family (#ffc62f, #f2bc2d, #d9a828, #bf9423, #ffe397) recurs across the
  supplied CSS and is inferred here as the primary accent for CTAs and highlights, since no
  single "brand color" variable was exposed. A secondary orange (#ff6422, #cc4603) also
  appears and is treated as a supporting accent for bumper/armor callouts. Utility colors
  (#198754, #ffc107, #de3535, #17a2b8) resemble generic status/alert tokens and are labeled
  as such rather than brand colors.

  Typography draws on the observed font stack: Russo One for bold display headlines (fitting
  an automotive/off-road identity), Saira and Inter/Roboto for body and UI text, with Arial
  and sans-serif as fallbacks. ConvermaxStar and JudgemeStar are third-party review/rating
  icon fonts, not brand type, and are excluded from typographic roles.

  Observed CSS button variables show a border-radius of 0px, so this interpretation adopts a
  squared-off, no-radius button and card language throughout, reinforcing a tough, mechanical
  aesthetic rather than a soft rounded consumer-goods look. Section spacing variables (30–120px)
  inform the proposed spacing scale below.

colors:
  primary: "#ffc62f"
  primary-deep: "#bf9423"
  accent-orange: "#ff6422"
  accent-orange-deep: "#cc4603"
  ink: "#000104"
  ink-soft: "#231f20"
  canvas: "#ffffff"
  body: "#333436"
  muted: "#666666"
  hairline: "#d9d9d9"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-dark: "#141518"
  on-primary: "#000104"
  on-dark: "#ffffff"
  gold-tint: "#ffe397"
  status-success: "#198754"
  status-warning: "#ffc107"
  status-danger: "#de3535"
  status-info: "#17a2b8"
typography:
  display-xl: {fontFamily: "'Russo One', sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Russo One', sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Saira', sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.05em}
  body-md: {fontFamily: "'Inter', 'Roboto', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Inter', 'Roboto', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Inter', 'Roboto', Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "'Saira', 'Inter', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.1em}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    border: "1px solid {colors.ink-soft}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    labelTypography: "{typography.button-md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the gold accent as a high-visibility call-to-action fill (e.g. "Shop Suspension," "Get Started") with a square edge, matching the observed `--pe-btn-border-radius: 0px`. Hover/active darkening toward `{colors.primary-deep}` is proposed, not observed.

**button-secondary** is an ink-filled or ink-outlined variant for secondary actions ("Learn More," "Locate A Dealer"), preserving the same squared geometry and uppercase tracked label style implied by the `.ymm-block` button CSS (`letter-spacing: 0.1em; text-transform: uppercase`).

**text-input** models generic form fields (VIN entry, license-plate lookup, newsletter) with a thin hairline border and no radius, echoing the flat, technical UI language seen in the Convermax search styles.

**nav-bar** represents the persistent top navigation housing category links (Suspension, Wheels, Armor, Steering, Tools) plus utility links (dealer locator, phone number, login). Layout and scroll behavior are inferred; only typography and border tone are grounded in evidence.

**product-card** covers catalog tiles such as the listed top-seller SKUs (control arms, lift kits, shocks, wheels), with a plain bordered container, title in `{typography.title-md}` and price in `{typography.body-md}`. Stock/quick-add states are proposed and unobserved.

**hero** is a full-bleed dark section for statement imagery/video (the page text references a suspension video block and taglines like "Precision Performance. Proven Results."), using the display font for large impact type on a dark background.

**footer** groups resource links (Help Center, Warranty, ICON Tech, Dealers) on the dark surface tone, consistent with the footer-like link density in the page text; exact column layout is not observed.

**badge** is a small gold label for flags such as "New," "Top Seller," or sale pricing, reusing the primary accent rather than introducing a new color.

**search** models the site search affordance referenced in the CSS (`.cm_search-box-root`), styled flat and white per the Convermax evidence.

**vehicle-selector** is a category-specific component reflecting the "Shop by Vehicle / VIN / License Plate" widget explicitly present in the page text and `.ymm-block` CSS, using a soft gray panel, hairline border, and uppercase tracked labels drawn directly from the observed `.custom-dropdown button` styles.

## Responsive Behavior

Proposed breakpoints (not measured from live site behavior):

| Breakpoint | Width      | Notes                                              |
|-----------|-----------|-----------------------------------------------------|
| xs        | <576px    | Single-column stacking, nav collapses to drawer     |
| sm        | 576–767px | Vehicle-selector tabs stack vertically              |
| md        | 768–1023px| Two-column product grids                            |
| lg        | 1024–1439px | Full nav visible, three/four-column grids         |
| xl        | ≥1440px   | Max-width container, generous section spacing       |

Touch targets should be at least 44×44px for buttons and dropdown triggers, consistent with the observed `.ymm-block` button padding (`18px 24px`). Primary navigation should collapse into an off-canvas or accordion menu below `md`. This table is a recommendation based on common e-commerce patterns, not a measurement of ICON's actual responsive CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no live rendering, computed layout, or DOM screenshots were available.
- Exact hero, grid, and footer layouts were not observed; hero/footer/product-card structures above are inferred from page-text ordering and general e-commerce conventions.
- Color role assignments (primary gold vs. orange accent, dark surface tone) are inferred from frequency and context in the supplied palette, not confirmed via visual inspection of live components.
- Font availability, weights, and licensing for Russo One and Saira were not verified beyond their appearance in the `font_families` list; ConvermaxStar and JudgemeStar are excluded as they appear to be icon/rating fonts.
- Spacing scale values beyond the observed `--pe-section-spacing-*`, `--pe-btn-padding-*`, and container padding variables are proposed for consistency, not directly measured.
- Interaction states (hover, focus, active, disabled) and mobile navigation behavior were not observed and are marked proposed throughout.
- Status colors (`#198754`, `#ffc107`, `#de3535`, `#17a2b8`) resemble common utility/alert conventions but their actual usage on the live site was not confirmed.
