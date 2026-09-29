---
version: alpha
name: "Native Trails"
source_url: "https://nativetrails.net"
captured_at: "2026-09-28T09:57:08.058345+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Native Trails presents artisan-crafted kitchen and bath fixtures through a
  restrained, editorial palette built primarily on near-black ink (#1e1e1e),
  a dark charcoal button color (#32373c) observed on WordPress button and
  file-download components, and neutral grays (#dddddd, #e0e0e0, #f0f0f0,
  #eeeeee, #cccccc) used for hairlines and soft surfaces. White (#ffffff)
  serves as the primary canvas, consistent with a product-photography-led
  storefront. A muted gray (#757575) is inferred for secondary text and
  captions. A saturated red (#cc1818) appears in the extracted palette and is
  assigned here to badges or alert states, and a blue (#3858e9) is assigned to
  link/focus affordances, both inferred roles since no interactive states were
  directly observed. Font stacks extracted from CSS include Montserrat, Open
  Sans, Lato, and system sans-serif fallbacks; this interpretation assigns
  Montserrat to display/heading roles and Open Sans to body copy as an
  inferred pairing, since selector-level font assignment was not confirmed in
  the supplied evidence. Rounded corners follow the pill-shaped button radius
  (9999px) actually observed on `.wp-block-button__link`, while card and input
  radii are proposed conservative values consistent with a WooCommerce/WordPress
  build. Spacing and component states beyond the two confirmed button rules
  are proposed, scaled for a materials-and-craftsmanship-forward product
  catalog site rather than measured from live layout.

colors:
  primary: "#32373c"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#757575"
  hairline: "#dddddd"
  surface-soft: "#f0f0f0"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent: "#cc1818"
  link: "#3858e9"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "'Montserrat', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Montserrat', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Montserrat', sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Montserrat', sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
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
  finish-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"

## Components

**button-primary** reflects the one directly observed rule (`.wp-block-button__link`): dark charcoal fill, white text, fully rounded (pill) shape, and generous horizontal padding. This is the confirmed baseline for calls to action such as "Shop Kitchen Sinks."

**button-secondary** is a proposed outline variant, inverting the primary's fill to a bordered, transparent-background treatment for lower-emphasis actions like "Learn More," consistent with the `.is-style-outline` WordPress block pattern referenced in the CSS.

**text-input** is a proposed pattern for search and form fields (e.g., email sign-up), using the light canvas background and a mid-gray border consistent with the extracted `#cccccc`/`#dddddd` tones; no live input styling was confirmed.

**nav-bar** is proposed based on typical WordPress mega-menu structures implied by the extensive "PRODUCTS / RESOURCES / ABOUT US" menu text, using white background and ink text with a hairline bottom border for separation.

**product-card** is a proposed container for sink/vanity listings, using a light card surface (`#eeeeee`) distinct from the pure white canvas to create subtle grouping, with rounded corners and title/body typography pairing.

**hero** is a proposed full-bleed banner treatment for the "Artisan Crafted Luxury for the Kitchen and Bath" headline, using the dark ink tone as background with white display type, though actual hero background color was not confirmed in the evidence.

**footer** uses the same dark charcoal as button-primary, inferred from the confirmed `#footer .signup-info .btn` rule showing white text and border on a footer context, extended here into a full footer background treatment.

**badge** is a proposed small label component (e.g., "New," "Sale") using the observed red (`#cc1818`) as an accent, since red badges are common in WooCommerce contexts though not directly confirmed here.

**search** is a proposed lightweight input styling for the site's confirmed "SEARCH" menu entry, using the soft gray surface tone for a recessed appearance.

**finish-swatch-selector** is a category-appropriate proposed component for selecting sink/fixture finishes (fireclay, copper, nickel, NativeStone), using card surface and border tokens with a primary-colored selected state; this pattern is not present in the supplied CSS but is typical for a materials-driven fixture catalog.

## Responsive Behavior

This is a proposed recommendation, not measured site behavior:

| Breakpoint | Range | Layout guidance |
|---|---|---|
| xs | <480px | Single-column stack, nav collapses to hamburger/off-canvas menu |
| sm | 480–767px | Single-column product grid, sticky search icon |
| md | 768–1023px | Two-column product grid, condensed nav labels |
| lg | 1024–1439px | Three-column product grid, full horizontal nav |
| xl | ≥1440px | Four-column grid, wider hero and footer padding |

Touch targets should be at least 44×44px for nav items, buttons, and swatch selectors. The mega-menu structure implied by the "PRODUCTS/RESOURCES/ABOUT US" text should collapse into an accordion pattern below the `md` breakpoint. None of this responsive behavior was directly observed; it is inferred from conventional WordPress/WooCommerce patterns.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions were observed. Only two button rules and one footer button rule provided confirmed color/shape pairings — all other component definitions (cards, nav, hero, search, footer background, swatch selector) are proposed interpretations, not verified observations. Font-role assignment (Montserrat for headings, Open Sans for body) is inferred from the presence of these families in the extracted font list, not from confirmed selector-to-family mapping; actual licensing and self-hosting status of these fonts was not verified. Color role assignments (e.g., red as badge/accent, blue as link) are inferred from generic WordPress editor palette conventions present in the extracted color list, not from confirmed usage on this specific site. Mobile menu behavior, breakpoint values, and touch-target sizing are proposed defaults, not measured. Spacing scale values beyond the observed button padding are estimates suited to a product-catalog layout.
