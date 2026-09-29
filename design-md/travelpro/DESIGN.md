---
version: alpha
name: "Travelpro"
source_url: "https://travelpro.com"
captured_at: "2026-09-28T09:12:31.097337+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Travelpro's storefront evidence shows a functional, trust-driven retail palette built around
  neutrals with a single saturated brand blue (#000f9f) reserved for accents such as sale
  callouts, links, and interactive controls; this is inferred as the primary action color
  given its contrast against the otherwise near-monochrome (#1a1a1a, #2f3441, #ffffff,
  #f8f9fa) surface system. A muted tan (#8b7355) appears specifically on product-highlight
  icons, suggesting a secondary "craft/durability" accent used sparingly for feature
  callouts rather than primary actions. A saturated red (#e60000) is explicitly scoped to
  sale-labeled navigation text, so it is modeled here strictly as a sale/badge color, not a
  general accent. Typography is set in Figtree with system sans-serif fallbacks
  (Helvetica Neue, Roboto, Segoe UI, -apple-system), consistent with a Shopify-hosted DTC
  storefront prioritizing legibility over display flourish. The interpretation favors a
  clean, spacious commerce layout: soft-cornered cards, hairline dividers over heavy borders,
  and a restrained button system that echoes the brand's aviation-professional,
  performance-luggage positioning rather than a decorative fashion aesthetic.

colors:
  primary: "#000f9f"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#2f3441"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f8f9fa"
  surface-card: "#fdfcf6"
  on-primary: "#ffffff"
  accent-teal: "#236192"
  accent-tan: "#8b7355"
  sale-red: "#e60000"
  border-subtle: "#e6e6e6"
typography:
  display-xl: {fontFamily: "Figtree, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Figtree, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.border-subtle}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-subtle}"
    activeBorder: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** models the deep brand blue (#000f9f) as the sole high-saturation call-to-action color observed against an otherwise neutral palette; used for "Add to Cart," "Shop Now," and checkout actions. Hover/active states are proposed, not observed.

**button-secondary** provides an outlined variant using the same blue for text/border on a white ground, suited to secondary actions like "Learn More" or "Compare" links inferred from the guide-heavy navigation (Carry-on Comparison Guide, Hard Side vs. Soft Side).

**text-input** is a light, hairline-bordered field appropriate for search, email capture, and account forms; corner radius and padding are proposed defaults consistent with the site's restrained visual density.

**nav-bar** reflects the observed multi-tier menu structure (Shop All, Luggage, Bags, Accessories, Collections) with a white background and thin bottom hairline; dropdown/mega-menu interaction states are proposed, not measured.

**product-card** is inferred from the repeated product-name/price pairing pattern in the page text (e.g., "Platinum® Elite Carry-On Spinner $390"); a warm off-white card surface (#fdfcf6) is proposed as distinct from pure white to add tactile warmth suited to a luggage brand.

**hero** models the "25% Off Optima" promotional banner and swiper-based hero slider evidence (`.new-hero-slider`), using a soft neutral background with large display type; slide transition timing/behavior is not observed.

**footer** uses the darkest observed ink tone as a full-bleed dark footer band, a common commerce pattern; actual footer content/columns were not present in supplied evidence and are therefore structurally inferred only.

**badge** captures the explicit `color: #e60000 !important` rule scoped to sale-labeled navigation text, formalized here as a small pill/label component for "Sale," "New," and similar merchandising flags.

**search** is proposed as a pill-shaped input consistent with the rounded, softened swiper controls (`border-radius: 50%`) observed elsewhere in the CSS, extending that rounded-affordance language to the search field.

**color-swatch-selector** is the category-appropriate component for soft luggage, directly justified by the observed "Shop by Color" and "Exclusive Colors" navigation entries; modeled as a row of circular swatches with a blue active-state ring matching the primary brand color.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid; nav collapses to hamburger/off-canvas menu; hero slider controls shrink to 36px touch targets. |
| Tablet | 600–1023px | Two-column product grid; mega-menu may condense to accordion. |
| Desktop | 1024–1439px | Full mega-menu nav bar; 3–4 column product grid. |
| Wide | ≥1440px | Max-width content container with increased section padding ({spacing.section}). |

Touch targets should be a minimum of 44px per side (matching the observed 44px swiper arrow buttons) on mobile and tablet. Menu collapse thresholds and gesture behavior are proposed, not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction was observed. Color-role assignments (e.g., primary action blue, sale red, tan accent) are inferred from selector context and may not represent the full production stylesheet. Font availability, weights, and licensing for Figtree were not verified beyond `font-family` declarations. Layout structure for footer, mobile navigation, and hero slide count/timing is inferred from partial selector names and is not confirmed. All spacing, radius, and typographic scale values beyond those explicitly present in supplied CSS (e.g., the 14px/36px sizes) are proposed defaults for a cohesive system, not measured values. Hover, focus, error, and disabled states for all components are proposed and unverified against the live site.
