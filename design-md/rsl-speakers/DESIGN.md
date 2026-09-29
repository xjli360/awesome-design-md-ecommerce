---
version: alpha
name: "RSL Speakers"
source_url: "https://rslspeakers.com"
captured_at: "2026-09-28T04:57:02.276118+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  RSL Speakers presents itself as a straightforward, factory-direct audio
  manufacturer, and the observed CSS reflects a utilitarian, high-contrast
  interface built on Shopify theme tokens (--bg-color, --text-color,
  --header-accent-color). The header defines a stark white/near-black scheme
  (rgb 255 255 255 / rgb 7 7 7), with a mid-gray accent (#777777) for
  secondary navigation text — directly observed. The Judge.me review widget
  contributes the clearest brand-adjacent accents: a bright cyan (#00bff3)
  driving interactive elements like the "Write a Review" button and
  pagination, and warm gold tones (#d4af37, #fbc31a) marking star ratings and
  reviewer names. --jdgm-border-radius: 0 signals a flat, squared-off visual
  language, which this interpretation extends to buttons and cards as an
  inferred default. Supporting neutrals (#f7f7f7, #eeeeee, #e4e4e4, #cccccc)
  suggest soft card and hairline surfaces typical of a product-grid commerce
  layout, though exact application was not observed in context. Typography
  draws from a large detected stack — Bebas Neue and Oswald (condensed,
  uppercase-friendly display faces common in audio/AV branding) alongside
  Open Sans and Roboto for body copy; a custom-named family
  (BureauGrotesque-ThreeFive) appears in the font list but its assigned
  selectors and licensing are unverified. Sizes, weights, and spacing/radius
  scales below are proposed conventions, not measured page metrics.

colors:
  primary: "#00bff3"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#e4e4e4"
  surface-soft: "#f7f7f7"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  accent-gold: "#d4af37"
  accent-star: "#fbc31a"
  accent-tint: "#bbd7ef"
  border-strong: "#cccccc"
  footer-dark: "#2e2e2e"
typography:
  display-xl: {fontFamily: "'Bebas Neue', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Bebas Neue', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Oswald', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', 'Roboto', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', 'Roboto', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Oswald', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-dark}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  rating-stars:
    filledColor: "{colors.accent-star}"
    emptyColor: "{colors.hairline}"
    reviewerNameColor: "{colors.accent-gold}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"

## Components

**button-primary** reuses the Judge.me-observed cyan (#00bff3) as the site's most interactive-feeling accent, paired with white text and a squared corner (rounded.none) consistent with the observed `--jdgm-border-radius: 0`. Proposed for "Add to Cart," "Shop Now," and newsletter signup actions.

**button-secondary** is an outlined, transparent variant using the same cyan for border/text, proposed for lower-emphasis actions like "Learn More" or "View All Benefits" links seen in the page text.

**text-input** maps to the theme's generic `--input-bg-color`/`--input-text-color` custom properties, styled with a light hairline border and minimal radius; used for account/login, search, and cart quantity fields. States (focus, error) are proposed, not observed.

**nav-bar** reflects the directly observed header tokens: white background, near-black text, and a gray (#777777) accent for secondary/dropdown items (Products, Encore Store, Reviews, More From RSL). Mobile collapse behavior is proposed, not confirmed.

**product-card** is inferred for the SUBWOOFERS/ARCHITECTURAL/ACCESSORIES grids referenced in the page text (e.g., Speedwoofer 10E $339). Uses a soft neutral surface and hairline border typical of Shopify product grids; exact card styling was not directly observed.

**hero** is proposed for the homepage banner ("Hears What's Next," W25E showcase) using a dark/ink background with large display type, since no hero-specific CSS was supplied — treat sizing and imagery as inferred.

**footer** is proposed using one of the site's darker observed neutrals (#2e2e2e) for the newsletter/social/contact block ("Facebook Instagram YouTube," phone number, hours); exact footer background was not confirmed in the supplied CSS.

**badge** repurposes the gold Judge.me color for callouts like "Encore" refurbished-gear labels or "Free Shipping" ribbons; pill shape is a proposed convention, not observed.

**search** follows the same input styling as text-input, with a muted icon color; used for the header search affordance implied by standard Shopify theme structure.

**rating-stars** (category-appropriate for an audio/reviews-driven storefront) directly reflects Judge.me tokens: gold filled stars (#fbc31a), gold reviewer names (#d4af37), and zero border-radius, used across product pages and the "Audiophiles Choose RSL Speakers" testimonial slideshow.

## Responsive Behavior

Proposed, not measured — no explicit media-query breakpoints were present in the supplied evidence beyond fluid `--fluid-max-vw: 1536` scaling variables and gutter tiers (`--gutter-sm: 20px`, `--gutter-md: 32px`, `--gutter-lg: 80px`), which hint at roughly small/medium/large tiers.

| Tier | Width | Gutter |
|------|-------|--------|
| Mobile | < 750px | {spacing.base} |
| Tablet | 750–990px | {spacing.xl} |
| Desktop | ≥ 990px | {spacing.xxl} |

Touch targets should be at least 44px for nav and cart controls; primary/secondary buttons should collapse to full-width on mobile with stacked product-card grids (1-column mobile, 2–3 column tablet/desktop). This table is a recommendation derived from generic Shopify gutter conventions observed in the CSS variables, not measured live layout behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/token extraction and page-text scraping only; no live rendering, computed styles, or interaction states were observed. Color role assignments (e.g., cyan as "primary," gold as rating/accent) are inferred from Judge.me widget variables and general commerce conventions, not from confirmed brand-guideline documentation. Font usage is uncertain: Bebas Neue, Oswald, Open Sans, and Roboto were detected in the font stack list, but which elements actually render in each family was not confirmed via computed styles; the custom-named "BureauGrotesque-ThreeFive" face may be a licensed/proprietary font whose availability and licensing terms are unverified. All spacing, radius, and typography sizes beyond the literal CSS custom properties (`--space-unit`, `--gutter-*`, `--fluid-*`) are proposed design-system conventions, not measured pixel values from rendered pages. Mobile menu behavior, hover/focus states, and cart-drawer interactions referenced in the page text ("Your cart," slideshow controls) were not visually observed. Breakpoint values are estimates based on common Shopify Dawn-theme patterns, not confirmed media queries.
