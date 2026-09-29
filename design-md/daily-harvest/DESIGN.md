---
version: alpha
name: "Daily Harvest"
source_url: "https://daily-harvest.com"
captured_at: "2026-09-29T04:10:34.262418+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Daily Harvest's live Shopify storefront evidence: a
  neutral, warm-leaning palette (near-white canvas #ffffff and #fdf6f3, warm cream
  surfaces #f5f0e7/#fdfaf3, near-black ink #1f1f1f/#1a1a1a) paired with small accent
  hues that recur across the supplied swatches — a muted forest green (#298266), a
  warm harvest orange (#ec9808), and a coral-red (#dc5742) — which read as organic/
  promotional accent colors for badges, tags, and seasonal callouts (e.g. "Fall
  Flavor Flights," "BEST SELLER"). The only concretely observed interactive
  color pair is a blue accelerated-checkout button (#1990c6, hover #136f99),
  which is preserved here for payment-specific components. Typography centers on
  a condensed Futura family (FuturaCondensed, loaded via @font-face) for
  display/heading use, and the Kaliedoscope reviews widget explicitly sets
  font-family: futura; font-weight: 500 for buttons — used here as the basis
  for button-md. Body copy is mapped to the system/Helvetica-Arial stack visible
  in third-party embed CSS, as no first-party body font rule was supplied.
  Layout, spacing, and rounding values below are proposed conventions, not
  measured page metrics, except where a literal CSS value (e.g. 9999px pill
  radius) is cited.

colors:
  primary: "#298266"
  ink: "#1f1f1f"
  canvas: "#ffffff"
  body: "#414042"
  muted: "#7e7f80"
  hairline: "#e3e5e6"
  surface-soft: "#f5f0e7"
  surface-card: "#fdfaf3"
  on-primary: "#ffffff"
  accent-warm: "#ec9808"
  accent-coral: "#dc5742"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  badge-green-soft: "#c3e7c3"
  badge-yellow-soft: "#fff7d9"
  border-strong: "#cacccc"
  overlay-scrim: "#00000080"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "'FuturaCondensed', Futura, Helvetica, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "'FuturaCondensed', Futura, Helvetica, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Futura, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.4px}
  button-md: {fontFamily: "futura, Helvetica, Arial, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-checkout:
    backgroundColor: "{colors.accent-blue}"
    backgroundColorHover: "{colors.accent-blue-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    backgroundColorScrolled: "#ffffffeb"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "106px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    badgeBackground: "{colors.accent-warm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairline: "#ffffff24"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-green-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  nutrition-tag:
    backgroundColor: "{colors.badge-yellow-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** is proposed as the main add-to-box/shop CTA, using the inferred harvest-green primary with a fully rounded (pill) shape consistent with the site's playful, food-forward tone; hover/active states are not observed and are proposed only. **button-secondary** covers outline-style actions (e.g. "Learn more") using ink text on a transparent fill with a hairline border. **button-checkout** is the one component with directly observed styling — the Shopify accelerated-checkout button explicitly sets background #1990c6 with a #136f99 hover, square corners, and white text; it is kept isolated from the general button system since it is a third-party payment widget, not a first-party brand button. **text-input** proposes a simple bordered field for search/newsletter signup ("GET ON THE LIST"), no focus-state color was observed so focus styling is not specified. **nav-bar** reflects the measured `--category-nav-height`/`--header-spacer` of 106px and the observed transparent-to-solid header transition (background-color #ffffffeb with a `0 1px #1f1f1f14` shadow on scroll/hover), a real CSS behavior in the supplied rules. **product-card** is a proposed pattern for smoothie/bundle tiles (e.g. "Best Sellers," "Detox Bundle") with a warm off-white card surface and an orange promo badge slot, inferred from the bundle pricing/description content in the page text. **hero** models the large "LET'S GET REAL" statement section against a warm cream background, using the display-xl condensed Futura style. **footer** is proposed as a dark, ink-colored block echoing the site's near-black ink tone, housing the multi-column Shop/Learn/Share link groups visible in the page text. **badge** and **nutrition-tag** are proposed small pill/rect components for labels like "BEST SELLER," "20G PROTEIN," and "GLUTEN-FREE," using the softer green and yellow tints present in the palette as non-alarming informational colors.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column stacks; nav collapses to hamburger + cart icon; hero CTA full-width |
| Tablet | 640–1024px | 2-column product grids; sticky nav height may reduce from 106px |
| Desktop | >1024px | Multi-column product/bundle grids; full mega-menu nav at 106px height |

Touch targets should be a minimum of 44px, matching the `clamp(25px, …, 55px)` button block-size pattern observed in the accelerated-checkout CSS. Mobile nav collapse, drawer/cart behavior, and swiper carousel touch gestures (swiper-button-prev/next classes are present) are structurally implied by the CSS but their interactive behavior was not observed and should be treated as proposed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, open menu, cart drawer) were observed. Color-to-role mapping (e.g. which exact hex serves as the "true" brand primary) is inferred from palette frequency and thematic fit, not confirmed via a labeled brand style guide — Daily Harvest's actual primary action color could differ from the green chosen here. The `#1990c6`/`#136f99` pair is the only literal button-state pair in evidence and belongs to a generic Shopify payment widget, not necessarily first-party brand styling. Font roles for PlayfairDisplay, Sailec, and GTStandard-M appear in the raw font list but have no associated selector in the supplied CSS, so their usage is unconfirmed and excluded from the typography scale. All spacing and rounding values, and most typography sizes, are proposed conventions rather than measured pixel values. Font licensing/availability for FuturaCondensed and Futura variants was not verified.
