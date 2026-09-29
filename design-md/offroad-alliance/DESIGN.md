---
version: alpha
name: "Offroad Alliance"
source_url: "https://offroadalliance.com"
captured_at: "2026-09-29T04:00:04.254763+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Offroad Alliance's captured CSS reflects a Bootstrap 4.1.3 foundation layered with light custom theming for a heavy-duty automotive parts catalog. The observed palette centers on a utilitarian near-black/white pairing (#111111, #212529, #333333 on #ffffff) with a saturated red (#cc171d, #cc4749) used sparingly for brand emphasis in header elements. Grays (#e5e5e5, #f4f4f4, #dee2e6, #f7f7f7) supply hairlines and soft surfaces typical of dense mega-navigation and table-heavy catalog pages. Bootstrap's status colors (#28a745, #dc3545, #17a2b8, #ffc107) remain available for inventory/availability badges but no confirmed custom usage was observed beyond the framework defaults.
  Typography is system-stack driven (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial), consistent with an unthemed Bootstrap body font; Montserrat, Karla, and Source Sans Pro appear in the font manifest and are treated here as inferred display/heading candidates for a more branded off-road aesthetic, not confirmed as currently rendered. The interpretation proposes a rugged, dense-navigation commerce layout: bold nav labels, red accent CTAs, and card-based category browsing suited to a 4x4 parts inventory. All semantic role assignments (ink, muted, hairline) are inferred from generic Bootstrap variable usage, not brand-specific declarations.

colors:
  primary: "#cc171d"
  ink: "#111111"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#757575"
  hairline: "#dee2e6"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-secondary: "#cc4749"
  success: "#28a745"
  danger: "#dc3545"
  info: "#17a2b8"
  warning: "#ffc107"
  border-strong: "#cccccc"
  text-secondary: "#495057"
typography:
  display-xl: {fontFamily: "Montserrat, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  category-mega-menu:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.section}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.border-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"

## Components

**button-primary** uses the observed brand red as a solid fill for primary calls-to-action such as "Add to Cart" or "Shop Now," paired with bold button-md type; hover/active states were not captured and are proposed as a modest darken.

**button-secondary** applies the near-black ink tone with a matching border, suited to secondary actions like "Compare" or "View Details" alongside the primary red CTA; this pairing is a proposed convention, not an observed rule.

**text-input** is a light, bordered field styled from Bootstrap's default form conventions (hairline border, soft radius) appropriate for search boxes, quantity fields, and checkout forms; focus-state styling was not present in the supplied CSS and is left undefined.

**nav-bar** reflects the captured `#customMainNav` rule set: full-width items, bold 700-weight labels, generous 50px minimum touch height, and white background with dark ink text — this is directly evidenced by the supplied selector.

**category-mega-menu** is proposed to house the extensive category tree evidenced in the page text (Exterior, Suspension, Recovery, Lighting, etc.), using the soft gray surface and hairline dividers consistent with the `.brands-header` gradient treatment observed in CSS.

**product-card** is a standard bordered, rounded container for SKU imagery, title, and price, inferred from common commerce patterns since no explicit card selector was supplied; radius and border values are proposed defaults from the shared token scale.

**hero** proposes a dark, high-contrast banner treatment (ink background, white text, large display type) suitable for promotional messaging such as the observed "FREE SHIPPING OVER $399" banner text; exact hero markup/CSS was not present in evidence.

**footer** mirrors the dark surface treatment used elsewhere (e.g., `.oa-blog-button` dark background) for a grounded, utilitarian close to the page; content structure is not evidenced and is left generic.

**badge** leverages Bootstrap's danger red for stock/status indicators (e.g., "Scratch & Dent," "Low Stock") as a proposed small pill component; no badge selector was directly observed.

**search** is inferred as a soft-surface input consistent with the site's gray/white palette, intended for the prominent product search implied by the deep category taxonomy; no dedicated search-bar CSS was supplied.

## Responsive Behavior
Breakpoints below are a recommendation inferred from the media-query strings present in the evidence (800px, 1280px, 1681px, 1920px), not measured rendering behavior:

| Range | Target | Notes (proposed) |
|---|---|---|
| ≤800px | Mobile | Single-column, collapsed nav behind toggle menu (evidenced "Toggle menu" text) |
| 800–1280px | Tablet | Condensed mega-menu, 2-column product grids |
| 1280–1681px | Small desktop | Full mega-menu, 3–4 column product grids |
| 1681–1920px+ | Large desktop | Widened containers, 4+ column grids |

Touch targets should meet a 44px minimum; the observed `#customMainNav` 50px min-height satisfies this for primary nav items. Mobile collapse of the extensive category tree into an accordion-style toggle is recommended given the depth of the evidenced taxonomy, but this interaction was not observed directly.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed styles, or DOM screenshots were available. Several colors (e.g., Bootstrap contextual palette) appear in the source but their applied usage on this specific site was not confirmed beyond framework defaults. The brand red's exact hex (`#ed1520` appeared only in inline component CSS, not the root observed palette) was normalized to the closest confirmed palette value, `#cc171d`. Font family assignments for headings (Montserrat) are inferred from the font manifest, not from confirmed selector-level declarations, and licensing/availability of any named font was not verified. All spacing, radius, and typographic scale values beyond the single confirmed `#customMainNav` rule are proposed defaults for internal consistency, not measured site output. Mobile menu interaction, hover/focus states, and animation timing were not observed and are marked proposed throughout.
