---
version: alpha
name: "Corbett Lighting"
source_url: "https://www.hvlgroup.com/Products/Brand/CorbettLighting"
captured_at: "2026-09-29T04:22:26.859737+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Hudson Valley Lighting Group's (HVLG) shared
  e-commerce platform, on the page that lists Corbett Lighting's product catalog
  under the HVLG parent site. It reflects the current parent-site presentation of
  Corbett Lighting, not a reconstruction of the brand's former standalone
  corbettlighting.com site. The supplied CSS evidence is largely shared
  infrastructure (Bootstrap custom-property scaffolding, jQuery UI widget
  defaults) rather than brand-specific styling, so most color-to-role and
  typography-to-role mappings below are inferred from the broader observed
  palette and font stack, not confirmed from Corbett-specific selectors.
  The palette favors warm off-white canvases (#fffdfa, #f1ece0, #eeeae3)
  against deep charcoal and near-black inks (#212529, #343434, #16232e), with
  muted grays (#6c757d, #dee2e6) for secondary text and hairlines. A warm
  brown (#8d3f2d) and soft gold (#f4c24c) are proposed as accent tones,
  consistent with Corbett's "sophisticated-chic" tagline, though their actual
  on-site usage was not confirmed. Font evidence includes GT Eesti and GT
  Super (likely display/heading faces) alongside Roboto and the Arial/
  Helvetica stack used by jQuery UI form controls; roles below are proposed
  pairings, not measured usage.

colors:
  primary: "#8d3f2d"
  ink: "#212529"
  canvas: "#fffdfa"
  body: "#343434"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f1ece0"
  on-primary: "#ffffff"
  accent-gold: "#f4c24c"
  charcoal-deep: "#16232e"
  cream: "#eeeae3"
  border-subtle: "#e9ecef"
  error: "#eb4034"
  success: "#32a852"
typography:
  display-xl: {fontFamily: "GT Super, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GT Super, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "GT Eesti, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.md} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.charcoal-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.cream}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** proposes the warm brown accent (#8d3f2d) as a call-to-action surface (e.g., "Add to Cart," "Shop Now"), paired with white text for contrast. This role is inferred from the palette's warm tones, not confirmed as the site's live CTA color.

**button-secondary** is an outlined, canvas-backed alternative for lower-priority actions such as "Clear Filters," matching the observed filter-heavy product listing described in the page text (663 Products, multiple filter facets).

**text-input** supports the extensive filter sidebar (Price, Brand, Finish/Color, Material, Dimensions, etc.) implied by the page content. Border and placeholder colors are drawn from the neutral hairline/muted tokens; focus and error states are proposed, not observed.

**nav-bar** represents the shared HVLG top navigation (Our Brands, Collaborations, Trade Program, etc.) referenced in the page text. A light canvas background with dark ink text is inferred from the general neutral-forward palette; no header-specific selector was supplied.

**product-card** models the repeating product-tile pattern evident in the text excerpt (product name, brand label, price, SKU, stock status, dimensions). A warm cream card surface (#f1ece0) is proposed to differentiate cards from the page canvas.

**hero** proposes a dark charcoal banner for brand-introduction moments (e.g., the "Sophisticated-chic lighting" tagline), using the largest display typography. This treatment is a proposed pattern; no hero-section CSS was supplied.

**footer** reflects the multi-column HELP/BRANDS/COMPANY footer content visible in the page text, using dark ink background with cream/white text for legibility, consistent with the observed dark-neutral palette.

**badge** proposes a gold accent chip for stock-status labels ("In stock," "Low stock," "On the way!") that appear throughout the product listing text, using pill-shaped rounding for visual distinction from price/SKU text.

**search / finish-swatch-selector** address category-specific needs: a search input for the large 663-product catalog, and a circular finish/color swatch selector to support the "Finish/Color" filter facet named explicitly in the page content — a common pattern for lighting-fixture finish selection, proposed rather than observed in markup.

## Responsive Behavior

This is a recommendation based on typical catalog-listing patterns and is **not** measured from live site behavior:

| Breakpoint | Width | Layout notes |
|---|---|---|
| xs | <576px | Single-column product grid; filters collapse into a drawer/modal triggered by a "Filters" button. |
| sm | 576–767px | Two-column product grid; nav collapses to hamburger menu. |
| md | 768–991px | Two- to three-column grid; sidebar filters may persist alongside grid. |
| lg | 992–1199px | Three- to four-column grid; persistent left filter sidebar. |
| xl | ≥1200px | Four-column grid; full nav bar with all brand/category links visible. |

Touch targets should be at least 44×44px for filter checkboxes, swatch selectors, and pagination controls. Filter panels should collapse to an accordion or off-canvas drawer below the `md` breakpoint. None of this is confirmed from captured markup or scripts.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static, non-interactive CSS/text evidence and carries meaningful limitations:

- The supplied CSS is almost entirely shared platform styling (Bootstrap CSS custom properties, jQuery UI widget defaults) rather than Corbett Lighting– or brand-specific rules; no page-specific selectors for hero, product-card, or nav-bar were present in evidence.
- Color-to-role assignments (primary, accent-gold, surface-card, etc.) are inferred from a shared, multi-brand palette (the full HVLG color list spans several sub-brands); actual Corbett-specific brand color usage was not isolated or confirmed.
- Font-family-to-role pairings (GT Super for display, GT Eesti for titles, Roboto for body) are proposed based on typical usage patterns for these named families; no font-weight, size, or actual rendered-usage evidence was supplied.
- All numeric type sizes, spacing values, and rounded-corner values are proposed defaults for a lighting-catalog interface, not measured from the live site.
- No interaction states (hover, focus, active, disabled) beyond generic jQuery UI defaults were observed; component states described above are proposed.
- Mobile/responsive layout behavior was not observed; the breakpoint table is a UX recommendation only.
- Licensing and web-availability of GT Eesti and GT Super were not verified; fallback to generic serif/sans-serif is recommended until confirmed.
- This page is HVLG's current parent-site product listing for the Corbett Lighting brand; it is not a reconstruction of the brand's former independent corbettlighting.com site, and no migration or legacy-layout claims are made.
