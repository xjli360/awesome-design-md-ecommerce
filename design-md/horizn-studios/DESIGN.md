---
version: alpha
name: "Horizn Studios"
source_url: "https://horizn-studios.com"
captured_at: "2026-09-29T04:19:50.565296+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Horizn Studios presents itself as a German-engineered hard-shell luggage
  brand with a restrained, editorial aesthetic. The only concretely observed
  CSS values are the root color variables (foreground rgb 27,27,27 on a white
  background, button color matching foreground, button text white) and a
  card-level utility color (#4a4a4a) used for secondary swatch-count text.
  The remaining palette entries are drawn from the site's broader observed
  color inventory (product imagery, badges, payment-icon brand colors, and
  UI accents) and are here assigned inferred design-system roles rather than
  confirmed component roles, since no selector-level evidence ties most of
  them to a specific UI element.

  The interpretation leans into a near-monochrome ink-on-white system typical
  of premium DTC luggage retail, with the dark neutral (#1b1b1b) as the sole
  primary/button color observed in the CSS custom properties, and cooler
  slate and olive tones (#385265, #4f5d56) proposed as secondary accents
  echoing the brand's "Night Blue," "Pine Green," and "Dark Olive" product
  colorways referenced in the page copy. Warm sale/badge tones (#db302a,
  #f1ea7f) are proposed for promotional and flash-sale UI only. Typography
  uses the observed font-family token "Assistant" with system sans-serif
  fallback; all sizes, weights, and the button corner-radius (matching the
  observed default --cta-radius: 0px) are proposed unless stated otherwise.

colors:
  primary: "#1b1b1b"
  ink: "#1b1b1b"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#6e767f"
  hairline: "#d8d8d8"
  surface-soft: "#f5f5f5"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  accent-slate: "#385265"
  accent-olive: "#4f5d56"
  border-contrast: "#cccccc"
  sale: "#db302a"
  highlight: "#f1ea7f"
  success: "#559b00"
typography:
  display-xl: {fontFamily: "Assistant, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Assistant, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Assistant, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    swatchLabelColor: "{colors.body}"
  hero:
    backgroundColor: "{colors.canvas}"
    overlayColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaRounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    resultsBackground: "{colors.surface-card}"
    typography: "{typography.body-md}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-slate}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    typography: "{typography.title-md}"

## Components

**button-primary** uses the one CSS-confirmed brand action color (#1b1b1b on white text) and a squared corner (0px), matching the observed `--cta-radius` default. Proposed for "Add to Cart," "Save Now," and "Discover More" CTAs.

**button-secondary** is an inverted outline treatment (white fill, dark border/text) proposed for lower-emphasis actions such as "Continue shopping" in the empty-cart state; no direct selector evidence confirms this variant, so states are proposed.

**text-input** is a light-bordered field using the inferred hairline gray for its border since no explicit input CSS was supplied; padding and radius are proposed conventions for a Shopify-style storefront.

**nav-bar** represents the persistent header containing the mega-menu categories (Luggage, Backpacks, Bags, Accessories, Sets, Customise, Stores, About) visible in the page text; sticky behavior and collapse states are proposed, not observed.

**product-card** reflects the bestseller/grid tiles seen in the content excerpt (e.g. "H5 Pro Cabin Luggage"), and directly reuses the one confirmed non-root color (#4a4a4a) for the "+N" swatch-overflow count label, per the supplied `.card__swatch-overflow` rule.

**hero** models the full-bleed slideshow sections ("Pine Green is Here," "It's Your Journey") described in the page text, with a custom CTA button whose background/text/border are theme-variable driven (`--cta-bg-color`, etc.) and default to transparent/inherit per the supplied CSS — treated here as an inferred dark-overlay hero pattern.

**footer** is proposed as a muted, low-contrast information zone (About, Impact, Sustainability, Quality, Collaborations, Press) using the soft surface tone; no footer-specific selectors were supplied.

**badge** covers promotional labels like "GO Flash Sale," "GQ: Best Suitcase of Year 2026," and "Lifetime Warranty" call-outs; the sale-red assignment is inferred from the broader palette, not from a confirmed badge selector.

**search** is a proposed pattern for the (unobserved) storefront search affordance, styled consistently with the input and card tokens.

**configurator-panel** is a category-specific component for the "HORIZN ID" personal-luggage customization flow referenced in the page copy, using a slate accent to differentiate configurator UI (color/material pickers) from standard product cards.

## Responsive Behavior

This is a recommended layout pattern, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | <768px | Single-column cards, hamburger nav, sticky bottom cart bar (proposed) |
| Tablet | 768–1024px | 2-column product grid, condensed mega-menu |
| Desktop | >1024px | Full mega-menu, 3–4 column grids, hover-revealed swatches |

Touch targets should be at least 44×44px for cart, swatch, and nav controls. The mega-menu (Luggage/Backpacks/Bags/Accessories/Sets) should collapse into an accordion on mobile. None of this reflects actual measured DOM breakpoints from the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is a static CSS/text snapshot; no rendered layout, computed box model, or JS-driven interaction (e.g. cart drawer, HORIZN ID configurator) was observed.
- Only two selectors carried explicit, unambiguous color roles (`:root` foreground/background/button variables and `.card__swatch-overflow`); all other palette-to-role assignments (accents, badges, footer tone) are inferred from a raw color list without selector context.
- No hex was directly tied to named product colors ("Pine Green," "Night Blue," "Sand Grey," "Mocha"); accent-slate/accent-olive assignments are best-effort inferences, not confirmed brand swatches.
- Corner-radius values beyond the observed `--cta-radius: 0px` default are proposed conventions.
- Breakpoints, spacing scale, and component padding are proposed design-system defaults, not measured from live CSS media queries.
- "Assistant" is the only observed font-family token; actual weight availability, licensing, and fallback rendering were not verified.
- Mobile menu behavior, hover/focus states, and swatch-selection interaction were not observed and are labeled proposed throughout.
