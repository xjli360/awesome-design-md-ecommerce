---
version: alpha
name: "Troy Lighting"
source_url: "https://www.hvlgroup.com/Products/Brand/TroyLighting"
captured_at: "2026-09-29T04:16:01.713442+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the Hudson Valley Lighting Group (HVLG) storefront, where Troy Lighting is presented as one of several house brands within a shared Bootstrap-based commerce shell. No Troy-specific stylesheet was supplied, so the palette below is the observed HVLG site-wide color set, and the typography reflects the site's declared font stack (GT Super, GT Eesti, Arial/Helvetica, Roboto) rather than any Troy-only asset. Troy Lighting's copy ("elevating the perfectly imperfect... natural comfort") suggests a warm, artisanal, slightly industrial sensibility, so the interpretation leans on the warmer earth tones in the palette (rust-bronze #8d3f2d, mustard #f4c24c, warm creams) for primary and accent roles, while inking body text in the observed near-black/dark-gray grays. Card and surface tones use the off-white and cream values present in the palette rather than pure white, matching the catalog's dense, warm-neutral grid of product tiles seen in the page text (SKUs, finishes, dimensions). Role assignments beyond literal CSS values (primary, accent, surface-soft) are inferred design choices, not measured brand tokens, since Troy Lighting's dedicated brand site was not the crawled source.

colors:
  primary: "#8d3f2d"
  ink: "#212529"
  canvas: "#fffdfa"
  body: "#343434"
  muted: "#636059"
  hairline: "#dee2e6"
  surface-soft: "#f5f4f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#f4c24c"
  surface-alt: "#eeeae3"
  border-strong: "#adb5bd"
typography:
  display-xl: {fontFamily: "GT Super, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GT Super, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "GT Eesti, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "GT Eesti, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "GT Eesti, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "GT Eesti, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "GT Eesti, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  filter-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** — A solid rust-bronze call-to-action (e.g., "Add to Cart," "Apply for Trade Account") with white text, matching the warm-industrial tone implied by Troy's product finishes. Hover/active/disabled states are proposed, not observed.

**button-secondary** — An outlined variant using the same primary hue for border and text on a transparent background, intended for secondary actions like "View Details" alongside a primary CTA. State transitions are proposed.

**text-input** — A white field with a light hairline border for filter search, quote requests, or account forms, consistent with the site's dense filter sidebar (Price, Finish/Color, Material, Dimensions). Focus ring styling is not observed and is proposed as an accessible default.

**nav-bar** — A warm off-white top bar carrying brand navigation (Our Brands, Collaborations, Trade Program, How To Buy) and category links (Decorative Lighting, Architectural Lighting). Sticky/scroll behavior is not observed.

**product-card** — Represents the catalog tile pattern implied by the product listing text: brand label, product name, price, SKU, stock-status line, and dimensions. White card surface with a hairline border and small-radius corners keeps focus on product imagery; stock badges (In Stock/Low Stock/Estimated date) are proposed as small caption-styled tags.

**hero** — A warm cream/tan band for brand introduction copy such as "Elevating the perfectly imperfect to create inviting atmospheres of natural comfort," using the display-xl serif treatment to give the brand statement editorial weight. Actual hero imagery/layout was not observed.

**footer** — A dark ink-colored footer housing Help, Brands, and Company link columns plus legal copyright lines for the three HVLG-affiliated entities. Multi-column responsive stacking is proposed.

**badge** — A small mustard pill for stock/status indicators (e.g., "Low stock," "Sale") or new-arrival flags, reusing the accent color already present in the palette rather than introducing a new hue.

**search** — A compact input+icon pattern for the product grid's "1394 Products" search/filter context; exact icon placement and interaction (Font Awesome icon fonts are present in evidence) are proposed, not confirmed.

**filter-panel** — A soft-cream sidebar container grouping the observed filter facets (In Stock, International, Price, Brand, Product Category, Finish/Color, Material, Dimensions, Features, Color Temp, Voltage, Components) with a "Clear Filters" action, styled with body-sm typography for compact scanning.

## Responsive Behavior

| Breakpoint | Width | Layout intent (proposed) |
|---|---|---|
| xs | <576px | Single-column product grid, collapsed filter panel behind a toggle, stacked nav |
| sm | 576–767px | 2-column product grid, filters remain collapsed |
| md | 768–991px | 2–3 column grid, filter panel visible as a collapsible accordion |
| lg | 992–1199px | 3–4 column grid, persistent left filter sidebar |
| xl | ≥1200px | 4+ column grid, full nav and filter sidebar always visible |

Touch targets for buttons and filter checkboxes should be at least 44×44px per standard accessibility guidance. Below `md`, the filter sidebar is expected to collapse into a drawer or modal triggered by a "Filters" button, consistent with the "Filters" label present in the page text. This table is a recommendation derived from typical Bootstrap-grid commerce patterns (Bootstrap CSS variables were observed in the stylesheet) and is not a measurement of the live site's actual responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction of the HVLG storefront's Troy Lighting brand listing, not a Troy-specific stylesheet, so brand-exclusive tokens (logo colors, custom iconography) could not be isolated from the shared HVLG palette. Semantic role mapping (primary, accent, surface-soft, etc.) is inferred from the general warm-neutral palette and Troy's brand copy, not confirmed by any brand style guide. Typography sizes and weights are proposed conventions layered onto the observed font-family declarations (GT Super, GT Eesti, Arial/Helvetica, Roboto); no explicit heading font-size or weight values were present in the supplied CSS rules. No interaction states (hover, focus, active, disabled), animation, or mobile/collapsed navigation behavior were observed in the evidence and are marked proposed throughout. Actual page layout, grid column counts, and card dimensions were not measured from rendered output. Licensing and web-availability of GT Super and GT Eesti were not verified and should be confirmed before production use; generic serif/sans-serif fallbacks are included accordingly.
