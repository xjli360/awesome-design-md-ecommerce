---
version: alpha
name: "Ruvati"
source_url: "https://ruvati.com"
captured_at: "2026-09-28T09:19:41.140171+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ruvati's public site runs on WordPress/WooCommerce with a Twenty-Twenty-era block
  theme, so the observed palette mixes genuine storefront styling with default block-
  editor swatches. The one directly observed component rule — the WordPress button
  block — sets a dark slate background (#32373c) with white text and a fully pill-
  shaped radius (9999px), and this is treated here as the inferred brand primary and
  button pattern. Body copy relies on the system font stack (-apple-system, Segoe UI,
  Roboto, Helvetica, Arial) while product-listing page titles explicitly use "PT Sans"
  at 26px bold, so PT Sans is adopted for display/heading roles and the system stack
  for body text. Surface tones are drawn from the observed neutral grays (#ffffff,
  #f4f4f4, #f8f8f8, #dddddd, #333333, #555555, #808080). A secondary teal-blue
  (#3e8aaa) present in the palette is used as an inferred accent, plausible for a
  water-fixture brand but not confirmed by any captured component rule. Layout,
  spacing, and most component sizing below are proposed conventions suited to a
  sink/faucet catalog, not measured page geometry.

colors:
  primary: "#32373c"
  accent: "#3e8aaa"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#555555"
  muted: "#808080"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'PT Sans', sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  display-md: {fontFamily: "'PT Sans', sans-serif", fontSize: 26px, fontWeight: 700, lineHeight: 1.5, letterSpacing: 0px}
  title-md: {fontFamily: "'PT Sans', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.muted}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  room-selector-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components
**button-primary** reflects the one directly observed component rule: a dark slate (#32373c) fill, white text, and a fully rounded 9999px pill — used for calls to action like "Shop Now." **button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Read More" links) using the same primary color and pill shape for visual consistency. **text-input** is a proposed field style for search and account forms, using the neutral hairline border since no explicit input CSS was captured. **nav-bar** is inferred from the presence of a deep "By Room / By Material / By Style" mega-menu structure in the page text; a white background with dark text is assumed default WooCommerce/theme styling. **product-card** is proposed for sink and faucet grid listings, pairing a light card surface with the PT Sans title style seen on category pages. **hero** models the homepage banner ("Explore Fireclay Sinks," "Bold Finish," room-selector tiles) using the display-xl scale drawn from the 42px "huge" preset. **footer** is proposed as a dark-on-light-text block consistent with the site's dark neutral (#313131/#333333) tones used elsewhere for text and backgrounds. **badge** is a proposed small accent tag (e.g., "New," "As Seen on HGTV") using the inferred teal accent color. **search** models the WooCommerce product-search widget referenced in the CSS (selectize dropdown styles), given a pill shape to match button conventions. **room-selector-tile** is a category-specific pattern for the homepage's Kitchen/Bathroom/Laundry/Workstation navigation tiles, proposed with a soft surface background and title-weight type.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <600px | Single-column stacking; room-selector tiles and product cards full-width |
| tablet | 600–1024px | 2-column product grid; nav collapses to a hamburger/mega-menu toggle (proposed) |
| desktop | 1024–1440px | 3–4 column product grid; full mega-menu nav bar visible |
| wide | >1440px | Max-width content container (~1280–1400px, proposed), extra gutter spacing |

Touch targets for buttons and nav items should be at least 44px tall (proposed). Mega-menu categories (By Room, By Material, By Style, By Finish) should collapse into an accordion on mobile (proposed, not observed). No actual responsive CSS or media queries were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted statically; no live rendering, computed styles, or JavaScript-driven behavior (e.g., mega-menu interaction, mobile nav collapse) was observed.
- The supplied color list mixes genuine site styling with WordPress core/default block-editor palette swatches and admin-only theme colors (e.g., #007cba, #006ba1, #005a87 are WP admin UI defaults, not confirmed brand colors); role assignments here are inferred, not verified brand choices.
- Only one component (`.wp-block-button__link`) had a fully captured background/radius rule; all other component definitions (product-card, hero, footer, nav-bar, search, badge) are proposed patterns for a kitchen/bath fixture catalog, not observed selectors.
- Typography sizes beyond 26px, 42px, 16px, and 13px are proposed, not measured.
- PT Sans and the system font stack are the only observed font families; licensing/self-hosting of PT Sans was not verified.
- No breakpoints, container widths, or grid columns were present in the supplied CSS; the responsive table above is a design recommendation only.
