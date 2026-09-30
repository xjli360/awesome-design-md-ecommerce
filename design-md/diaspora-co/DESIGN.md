---
version: alpha
name: "Diaspora Co"
source_url: "https://diasporaco.com"
captured_at: "2026-09-28T05:00:44.604946+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Diaspora Co's storefront CSS points to a warm, spice-market palette built around a saturated magenta-pink (#d5137b), a deep indigo-black (#080a5c), and near-black utility tones (#000000, #333333, #3a3a3a) used for text, buttons, and borders. Cream and off-white surfaces (#fff7ee, #fdfdfd, #ffffff) sit against these darker inks, echoing packaging and editorial photography rather than a sterile e-commerce look. Mustard-yellow and marigold accents (#ffd000, #f57320) and a red sale/error tone (#d21625) appear in labels and CTAs, suggesting a spice-tin-inspired accent system layered onto a neutral base. Typography evidence shows serif display candidates (p22-mackinac-pro, Caslon Graphique, Baskerville) alongside sans-serif workhorses (Figtree, Fustat, Fustat Next, PT Sans) — the serif family is inferred for editorial headings (recipes, cookbook) while the sans family is inferred for UI, product cards, and filters, matching the 14px/13px sizes observed in filter and vendor-label rules. Borders/backgrounds frequently hit #000000 and #333333 with 0px radius on interactive buttons, so this interpretation favors sharp, minimally-rounded components with color-blocked labels (sale, sold-out, bestseller) as the primary decorative device, all colors reused verbatim from the supplied palette.

colors:
  primary: "#d5137b"
  secondary: "#080a5c"
  ink: "#000000"
  body: "#3a3a3a"
  muted: "#969595"
  hairline: "#dedede"
  surface-soft: "#fff7ee"
  surface-card: "#fdfdfd"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffd000"
  accent-orange: "#f57320"
  sale: "#d21625"
  success: "#56ad6a"
  border-dark: "#333333"
typography:
  display-xl: {fontFamily: "p22-mackinac-pro, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Caslon Graphique, serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "Fustat, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "PT Sans, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    oldPriceColor: "{colors.muted}"
    vendorColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.secondary}"
    typography: "{typography.display-xl}"
    ctaBackground: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-yellow}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    saleBackground: "{colors.sale}"
    saleText: "#F0F0F0"
    soldoutBackground: "{colors.muted}"
    soldoutText: "{colors.on-primary}"
    bestsellerBackground: "{colors.accent-yellow}"
    bestsellerText: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  origin-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.secondary}"
    typography: "{typography.caption}"
    border: "1px solid {colors.accent-orange}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** uses the near-black ink observed on `.gf-form-button-group button` and add-to-cart controls, with a 0px radius matching the `border-radius: 0px !important` rule; this is the default commerce CTA (add to cart, shop now).

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Notify Me"), inferred from the bordered `#333333` swatch buttons in the filter UI but not directly observed as a secondary CTA style.

**text-input** is a proposed pattern for search and newsletter fields; no input-specific CSS was supplied, so border color, radius, and padding are inferred defaults consistent with the sharp-edged button styling.

**nav-bar** reflects the observed top navigation copy (Shop, Discover, Search) with a white canvas and hairline underline; spacing and sticky behavior are proposed, not measured.

**product-card** is grounded directly in `.spf-product-card__title`, `.spf-product-card__vendor`, and price/old-price rules, including the observed `#333333`, `#969595`, and `#141414` colors for title, vendor, and price text respectively.

**hero** is a proposed large banner pattern (e.g., "The Hella Spicy Tote is back!") using the cream surface and a display serif headline; exact hero markup/CSS was not in evidence.

**footer** is a proposed dark-ink footer using accent-yellow links for contrast; footer-specific selectors were not present in the supplied CSS, so this is an inferred convention.

**badge** directly reflects observed sale (`#d21625`/`#F0F0F0`) and sold-out (`#969595`-family/white) label rules, extended with an inferred "bestseller" yellow badge to match the repeated BESTSELLER tags in page copy.

**search** is a proposed lightweight input+icon pattern for the "Search for anything..." field referenced in page text; no dedicated search CSS was supplied.

**origin-tag** is a category-appropriate proposed component for surfacing single-origin/farm provenance (e.g., "Kandyan," "Aranya") on product pages, using the warm cream surface and orange accent border to reinforce the sourcing-story emphasis in the copy; this pattern is not evidenced in the supplied CSS.

## Responsive Behavior

Recommended, unmeasured breakpoints: mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. Navigation is expected to collapse into a mobile menu/hamburger below 768px, with filter panels (seen as `.gf-refine-toggle-mobile`) toggling into an off-canvas or accordion pattern on small screens. Touch targets should be at least 44×44px for buttons and badges given the dense product-grid labeling implied by the bestseller/sale tags. Product-card grids likely reflow from multi-column desktop to 1–2 columns on mobile; this is a proposed convention, not an observed layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states (hover/focus/active beyond the few `:hover` rules present) were observed. Semantic role assignments — which colors serve as "primary" vs. decorative accent, which font serves display vs. body — are inferred from selector context and cannot be treated as confirmed brand tokens. All typography sizes/weights outside the explicitly cited 13px/14px rules are proposed defaults. Mobile menu behavior, breakpoint values, hero and footer markup, and search-field styling were not present in the supplied evidence and are marked proposed throughout. Availability, licensing, and hosting of the named fonts (p22-mackinac-pro, Caslon Graphique, Fustat, Figtree, PT Sans) have not been verified.
