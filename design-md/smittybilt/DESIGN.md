---
version: alpha
name: "Smittybilt"
source_url: "https://smittybilt.com"
captured_at: "2026-09-29T04:09:01.869063+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Smittybilt's site evidence centers on an off-road, trail-tested identity expressed through a high-contrast black/yellow accent system. A CSS custom property, --tap-color-primary: #ffdc00 with an explicit black opposite (#000), is the clearest brand signal in the supplied evidence and anchors this interpretation's primary color. Surrounding UI relies on a disciplined gray scale (--gray-gray-900 through --gray-1, from #333333 to #ffffff) for text and surfaces, plus an observed dark button fill (#32373c) used across WordPress/WooCommerce block buttons. A deep navy (#002736) appears in the palette and is inferred here as a dark section/footer surface, consistent with a rugged automotive-accessory brand, though its actual usage location is not confirmed. Typography draws only from observed font-family declarations: Montserrat for display/headline weight, Open Sans for body copy, IBM Plex Sans Condensed for compact button/nav labeling, and Space Mono proposed for SKU/spec captions given the technical, parts-catalog nature of the content. Font Awesome icon families are excluded from text typography. Layout, spacing, and component visuals below are proposed conventions for an auto-accessory catalog site and are explicitly not claimed as observed screen measurements.

colors:
  primary: "#ffdc00"
  on-primary: "#000000"
  ink: "#111111"
  body: "#333333"
  muted: "#767676"
  hairline: "#dbdbdb"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#f4f4f4"
  surface-dark: "#002736"
  accent-dark-button: "#32373c"
  disabled: "#dfdfdf"
  link: "#007cba"
  alert: "#d9312b"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Space Mono, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "IBM Plex Sans Condensed, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 1px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.accent-dark-button}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    hairline: "{colors.hairline}"
    height_proposed: "72px"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    skuTypography: "{typography.caption}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayText: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    hoverTextColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary**: The main call-to-action treatment ("SHOP NOW", "VIEW DETAILS") built on the observed --tap-color-primary yellow with black text, echoing the site's explicit opposite-color token. Pill radius is proposed by analogy with the observed 9999px block-button radius.

**button-secondary**: Maps directly to the observed `.wp-block-button__link` / `.wp-element-button` styles (#32373c background, white text, same pill padding formula), used here for secondary or lower-emphasis actions.

**text-input**: A generic form field (newsletter signup, search fallback) using canvas background and the mid-gray hairline for borders; padding and radius are proposed, not measured.

**nav-bar**: Proposed dark header bar hosting category/vehicle navigation ("SHOP BY CATEGORY", "SHOP BY VEHICLE"). Background is inferred from the deep navy present in the palette; exact header styling was not confirmed in the supplied CSS.

**product-card**: Represents the repeating grid items seen in the excerpt (title, SKU, price, "VIEW DETAILS"). SKU is rendered in the monospace caption style to visually separate part numbers from marketing copy, an inferred stylistic choice.

**hero**: The full-width "YOUR CAMPSITE. ANYWHERE." banner is modeled as a dark-background, large-type hero with a primary-colored CTA; imagery, overlay treatment, and exact copy placement are not observed and are proposed conventions.

**footer**: Reflects the long link list and contact/newsletter content in the excerpt (About, Catalog, Warranty, social icons, address). Dark surface and white text are inferred from the palette's navy/black entries rather than confirmed footer CSS.

**badge**: A small alert/sale label using the observed red tone, proposed for promotional flags ("Garage Sale") though no explicit badge markup was supplied.

**search**: A light, bordered search field is proposed for header/product search; no dedicated search CSS was present in evidence.

**vehicle-fitment-selector**: Directly grounded in observed TAP-prefixed selectors (`#header-current-vehicle`, `.TAP-header-vehicle-fit`, `.TAP-button.classic-button`) which set black text on the primary-colored control and white text on hover, matching a year/make/model fitment widget typical of auto-parts catalogs.

## Responsive Behavior
Recommended, not measured breakpoints:
| Range | Layout |
|---|---|
| < 480px | Single-column product grid, stacked nav collapsed to menu icon |
| 480–768px | Two-column product grid, condensed vehicle-fitment selector |
| 768–1024px | Three-column grid, horizontal nav with dropdowns |
| ≥ 1024px | Four+ column grid, full nav bar, persistent fitment widget |

Touch targets should be at least 44px in the compact range; primary/secondary buttons and the fitment selector should expand padding accordingly. Nav collapse to an off-canvas or accordion menu below 768px is a proposed pattern, not an observed behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS custom properties, class declarations, and page text only; no rendered screenshots, computed layout, or interaction states (hover/focus/active beyond the two hover rules shown) were observed. Semantic role assignment for colors such as surface-dark (#002736), accent-dark-button (#32373c), link (#007cba), and alert (#d9312b) is inferred from typical usage patterns, not confirmed placement on the live site. Typography sizes beyond what appears in `--wp--preset--font-size` (16px, 42px) are proposed, not measured. Mobile/responsive behavior, breakpoint values, and the vehicle-fitment widget's full interaction flow were not directly observed and are proposed conventions. Licensing and hosting availability of all listed fonts (e.g., Montserrat, IBM Plex Sans Condensed, Space Mono) were not verified in this exercise.
