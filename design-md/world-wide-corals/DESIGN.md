---
version: alpha
name: "World Wide Corals"
source_url: "https://worldwidecorals.com"
captured_at: "2026-09-28T04:47:23.493452+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  World Wide Corals presents as a saltwater-aquarium superstore front, and the
  supplied CSS confirms a deep-navy-to-royal-blue gradient (`#000f69` to
  `#2a3fbc`) used on primary call-to-action buttons, paired with white text
  and a 6px border-radius, 700-weight Figtree labels at 14px. This gradient
  pairing is treated as the brand primary. The remaining palette is a large,
  mostly neutral grayscale set (`#000000` through `#f5f5f5`) typical of a
  Shopify-theme storefront, with scattered saturated accents (lime `#ccff00`,
  `#d8fdb0`, magenta `#ca00fa`, reds `#ff0000`/`#eb001b`, greens `#008a00`)
  that likely originate from icon sets, badges, or payment-method marks rather
  than core brand identity; these are mapped here as optional highlight/status
  colors and their exact UI role is inferred, not confirmed.
  Figtree is the only font family directly tied to a CSS declaration
  (font-family: Figtree, sans-serif; weight 600) and is used for body and
  interface text. Oswald, Barlow, DIN Next, Josefin Sans, Poppins, and Roboto
  appear in the site's loaded font list but without a captured selector
  pairing; Oswald is proposed here for display headings as an inferred,
  unconfirmed role given its common use for bold reef/aquarium retail
  headlines. Layout, spacing, and component states beyond the single button
  rule are proposed conventions for an e-commerce livestock catalog, not
  observed measurements.

colors:
  primary: "#000f69"
  primary-accent: "#2a3fbc"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7b7b7b"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f0f5fb"
  on-primary: "#ffffff"
  highlight: "#ccff00"
  highlight-soft: "#d8fdb0"
  danger: "#ff0000"
  success: "#008a00"
  info: "#0066cc"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}
rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
    backgroundImage: "linear-gradient(71deg, {colors.primary}, {colors.primary-accent} 37%, {colors.primary} 100%)"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.md}"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    backgroundImage: "linear-gradient(71deg, {colors.primary}, {colors.primary-accent} 37%, {colors.primary} 100%)"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "#1a1a1a"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  livestock-status-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    description: "Proposed tag for coral/fish availability states (e.g. In Stock, WYSIWYG, Sold), reusing the success/danger colors observed in the palette; not confirmed against live inventory UI."

## Components

**button-primary** applies the confirmed navy-to-blue diagonal gradient with white text and a 6px radius, matching the only fully captured interactive rule in the evidence (the featured-collection button). This is the highest-confidence component in the file.

**button-secondary** is a proposed outline variant using the same primary navy for border and text on a transparent background, intended for lower-emphasis actions like "View Details"; its visual state is not directly observed.

**text-input** is a proposed neutral field style using the light hairline gray for borders and white canvas fill, suited to search boxes, quantity fields, and account forms common to the site's catalog and account-management links.

**nav-bar** models the flat header/mega-menu structure implied by the extensive top-level categories (Coral, Fish, Inverts, Supplies, Merch, Service) using neutral canvas and ink tones; sticky-header behavior is referenced by a `--header-is-sticky` custom property in the evidence but its visual treatment is not shown.

**product-card** is proposed for the coral/fish product grid (e.g. "Vic's Picks") using the pale blue-white surface card color, a rounded 8px frame, and title/price typography split to accommodate the many priced livestock tiles referenced in the page text.

**hero** reuses the confirmed gradient at larger scale for a homepage or category banner, an extension of the one verified gradient rather than a separately observed hero style.

**footer** is a proposed dark neutral block for the store-info-heavy footer (locations, policies, help links) implied by the page content; exact footer background was not present in the supplied CSS.

**badge** uses the bright lime accent color for promotional or "New" labels, since saturated accent hues in the palette are most plausibly small UI badges rather than large surfaces; role is inferred.

**search** is a proposed lightweight input variant for the site's product search, using the light gray surface tone for subtle differentiation from pure white content areas.

**livestock-status-tag** is a category-specific proposed component for signaling coral/fish availability (In Stock, WYSIWYG, Sold Out), reusing the success and danger colors present in the palette; this pairing is inferred from general e-commerce convention, not from a captured status-badge rule.

## Responsive Behavior

Recommended, not measured, breakpoint table:

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | <480px    | Single-column product grid, collapsed hamburger nav, stacked filters |
| tablet    | 480–1024px| 2–3 column product grid, mega-menu collapses to accordion |
| desktop   | 1024–1440px | Full mega-menu nav bar, 4-column product grid |
| wide      | >1440px   | Max-width content container, additional whitespace |

Touch targets should be at least 44px for cart/add-to-cart controls given the large catalog of individually priced livestock items. Navigation collapse behavior (hamburger vs. inline mega-menu) is inferred from the presence of a `--header-inline-navigation` custom property, but exact breakpoint thresholds were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.



- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted via static CSS/text scraping; no rendered screenshots, computed layout, or DOM structure were available, so actual page composition is not confirmed.
- Only one component (a featured-collection button) had a complete, unambiguous CSS rule; all other components are proposed conventions grounded loosely in the palette and typography evidence.
- Font-family-to-role mapping for Oswald, Barlow, DIN Next, Josefin Sans, Poppins, and Roboto is inferred; only Figtree was directly tied to a captured `font-family` declaration.
- Several saturated palette colors (lime, magenta, bright red/green) could not be confidently attributed to brand identity versus third-party icons, payment badges, or social widgets; their component roles here are inferred.
- All spacing and rounded-corner values beyond the observed 12px padding, 10px gap, and 6px border-radius are proposed design-system defaults, not measured site values.
- Responsive breakpoints, hover/focus states, and mobile menu behavior were not observed and are presented strictly as recommendations.
- Licensing and availability of the referenced font families (e.g. Figtree, Oswald) were not verified as part of this evidence review.
