---
version: alpha
name: "Oxbow Animal Health"
source_url: "https://oxbowanimalhealth.com"
captured_at: "2026-09-29T04:24:10.717363+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from Oxbow Animal Health's Astra/WooCommerce-based storefront CSS, which exposes a WordPress default block-editor palette (WP core colors like #cf2e2e, #00d084, #8ed1fc) alongside a smaller set of theme-level brand colors: a deep teal (#007d66), an amber/orange (#f8951c), and supporting blues (#0274be, #0170b9). Because the supplied CSS references CSS custom properties (--ast-global-color-0 through -5) without resolved hex values, the mapping of primary/secondary brand roles below is inferred from the button and hover-state rules, which consistently pair a saturated color for backgrounds with white (#ffffff) text. Neutral grays (#3a3a3a, #808285, #f7f6f1, #eeeeee) are treated as ink, muted text, and soft-surface roles based on typical Astra defaults and their proximity in the palette.
  Typography is defined only by the system-font stack applied to body, buttons, and form controls (-apple-system through Helvetica Neue). Several named display fonts (Filson Bold/Regular, Sweet Sans Heavy, Sagona Bold/Book Italic, Montserrat) appear in the extracted font list and are used here for heading-level type roles as an inferred brand-voice layer, since no selector-level font-family rule ties them to headings in the supplied evidence. Spacing, radii, and component states are proposed conventions suited to a pet-nutrition/education storefront, not measured layout facts.

colors:
  primary: "#007d66"
  secondary: "#f8951c"
  ink: "#3a3a3a"
  canvas: "#ffffff"
  body: "#555d66"
  muted: "#808285"
  hairline: "#e6e6e6"
  surface-soft: "#f7f6f1"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-blue: "#0274be"
  accent-blue-alt: "#0170b9"
  success-green: "#5fb6a6"
  alert-red: "#cf2e2e"
  warm-orange: "#eb993f"
typography:
  display-xl: {fontFamily: "Filson Bold, Sweet Sans Heavy, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Filson Bold, Sweet Sans Heavy, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Filson Regular, Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.65, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1em, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  species-filter-tab:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** uses the theme's solid button pattern observed directly in the CSS (`.wp-block-button__link`, `input[type="submit"]`), where a global color variable fills the background and text renders in white with 15px/30px padding; this is a directly observed pattern, with the specific hex mapped to `{colors.primary}` as an inferred assignment.

**button-secondary** mirrors the `.is-style-outline` rules observed in the CSS, where the border and text share a color while the background stays transparent; hover states (also observed) invert to a solid fill. Proposed here as a lower-emphasis action for secondary CTAs like "Explore" links seen in the page text.

**text-input** is a proposed pattern for search and account/newsletter fields; no explicit input-styling CSS was supplied beyond font-family inheritance, so border, radius, and padding are conventions, not measurements.

**nav-bar** reflects the deeply nested mega-menu structure implied by the repeated "Products & Care / Rabbits / Guinea Pigs / Chinchillas…" taxonomy in the page text, suggesting a multi-column species-based dropdown; visual styling (background, hairline) is proposed, not observed.

**product-card** is proposed for the "Shop Our Best" and "Most Viewed / Newest Products" grid referenced in the page text; surface, radius, and padding follow generic e-commerce card conventions since no product-card CSS was supplied.

**hero** corresponds to the "WE GROW GOOD THINGS…" banner copy; soft warm background and large display type are proposed to match the brand's nurturing tone, not measured from layout.

**footer** is proposed using the ink color as background for contrast, consistent with common dark-footer patterns on content-heavy sites, though no footer-specific CSS was supplied.

**badge** is proposed for labeling content like "Award," "New," or species tags, using the secondary amber as an accent per the observed warm palette.

**search** reflects the "Search All Post Types / Posts / Products / Ingredient" control referenced in the page text; field chrome is proposed since no dedicated search-input CSS was supplied.

**species-filter-tab** is a proposed component supporting the repeated Rabbits/Guinea Pigs/Chinchillas/Gerbils & Hamsters/Rats & Mice/Ferrets taxonomy, styled as pill tabs to aid quick species-based navigation; this pattern is inferred from content structure, not observed styling.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤600px, tablet 601–1024px, desktop 1025–1200px (matching the `--ast-normal-container-width:1200px` custom property), and wide >1200px. At mobile widths, the species mega-menu is expected to collapse into an accordion or off-canvas panel given its deep nesting; touch targets should be at least 44×44px for nav items, filter tabs, and buttons. Product grids are expected to reflow from multi-column to single/double-column stacks below tablet width. This section is a recommendation for implementation, not a description of measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, live interaction states (hover/focus/active beyond the few explicit CSS rules), or JavaScript-driven behavior (e.g., mega-menu open state, cart drawer) were observed. The `--ast-global-color-0` through `-5` custom properties were not resolved to hex values in the supplied evidence, so primary/secondary/ink color role assignments are inferred from proximity and typical Astra theme conventions, not confirmed computed styles. Heading-level font-family assignments (Filson, Sweet Sans Heavy, Sagona, Montserrat) are drawn from the raw font list but were not tied to specific selectors in the supplied CSS, so their use for display/title roles is inferred. All spacing, radius, and typographic sizes beyond the explicitly quoted 15px body font and 15px/30px button padding are proposed conventions. Mobile/responsive behavior is a recommendation only. Licensing and availability of the custom fonts (Filson, Sweet Sans Heavy, Sagona) were not verified and should be confirmed before implementation.
