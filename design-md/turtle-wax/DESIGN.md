---
version: alpha
name: "Turtle Wax"
source_url: "https://turtlewax.com"
captured_at: "2026-09-29T04:12:56.431791+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Turtle Wax's storefront CSS shows a white-canvas, black-ink foundation accented by a
  saturated green (#168246, with a near-twin #00953a used as "--color-link-green") that
  carries the brand's automotive-care energy across hero copy, span highlights, and the
  primary button token (--color-button). Buttons and pills consistently use fully-rounded
  (100px) shapes in both black-on-white and white-on-black variants, suggesting a
  pill-first interaction language. A secondary blue pairing (#1990c6 / #136f99 hover) is
  visible only on Shopify's accelerated-checkout button, so it is treated as a
  platform-level accent rather than a core brand color. Neutral grays (#f5f5f5, #f2f2f2,
  #dedede, #9d9d9d, #333333) supply soft surfaces, hairlines, and muted text, while
  #121212 and #242833 read as near-black ink variants used interchangeably with pure
  #000000. Typography evidence includes TradeGothicLTStd (Regular/Bold/Light/Oblique
  cuts) alongside Libre Franklin, Exo, Arial, and Helvetica; TradeGothicLTStd is inferred
  as the display/heading face given its condensed industrial character fits an automotive
  brand, while Libre Franklin/Arial are inferred as body candidates. All heading colors,
  button radii, and the 55px H1 size are directly observed; font-role assignments,
  intermediate type scale sizes, and spacing are proposed extrapolations grounded in the
  supplied tokens.

colors:
  primary: "#168246"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#9d9d9d"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link-green: "#00953a"
  success-green: "#16a34a"
  ink-soft: "#242833"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  accent-indigo: "#334fb4"
typography:
  display-xl: {fontFamily: "TradeGothicLTStd-Bold, Arial, sans-serif", fontSize: 55px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "TradeGothicLTStd-Bold, Arial, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "TradeGothicLTStd, Libre Franklin, Arial, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Libre Franklin, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Libre Franklin, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Libre Franklin, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Libre Franklin, Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    accentColor: "{colors.primary}"
    ctaRounded: "{rounded.full}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.ink-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.link-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  kit-promo-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    badgeBackgroundColor: "{colors.link-green}"
    badgeTextColor: "{colors.on-primary}"
    priceStrikeColor: "{colors.muted}"
    padding: "{spacing.base}"

## Components
**button-primary** is modeled on the observed `.carousel .content .button` and instagram-linkbutton rules: solid fill, fully-rounded (100px) pill, uppercase bold 16px label. It is the primary CTA for "Shop Car Wash," "Add to cart," and similar actions.

**button-secondary** mirrors the `.slide-button` pattern — transparent/white fill with a 1px border, same pill radius — proposed here as an outline variant for use on darker or image-heavy sections; the hover/active fill-swap seen in `.slide-button.active` is treated as a proposed interaction state, not confirmed globally.

**text-input** is inferred; no dedicated input CSS was supplied, so soft-gray background, hairline border, and small radius are proposed defaults consistent with the site's rounded, low-contrast surface language.

**nav-bar** reflects the deeply nested mega-menu category text (Exterior, Interior, Wheel & Tire, etc.) implied by the page structure; visual chrome (height, shadow) is not observed and is proposed as a clean white bar with hairline underline.

**product-card** is proposed for the featured kits (Car Ick Preventer Kit, Black Car Care Kit, etc.); white surface-card, hairline border, and modest radius align with the neutral gray tokens observed, though actual card markup/CSS was not supplied.

**hero** reflects the observed `#Banner...h1` rule set directly: 55px black headline with a green (`#168246`) span highlight, on a white canvas, consistent with the "It all started in a bathtub" brand-story banner.

**footer** is proposed as a black/near-black band (using observed `--color-badge-background`/ink tokens) with white text, since no footer-specific selectors were present in the evidence.

**badge** leverages the "20% Off" / "Sale" labels seen repeatedly in the featured-products text; a small green fill with white text is proposed as a plausible treatment consistent with `--color-link-green`.

**search** is proposed as a pill-shaped input consistent with the button radius language; no search-bar CSS was supplied.

**kit-promo-card** is a category-appropriate component for Turtle Wax's bundled "Car Care Kits" merchandising pattern (regular/sale price pairs, sold-out states), using the observed muted gray for strikethrough pricing and the green badge for the recurring "20% Off" flag.

## Responsive Behavior
Recommended, not measured: mobile <768px stacks the mega-menu into an accordion, hero text drops from `display-xl` (55px) toward `display-md` (36px), and CTA buttons retain full pill radius with a minimum 44px touch target. Tablet 768–1023px keeps a two-column product-card grid; desktop ≥1024px expands to three or four columns. The one observed mobile-specific rule (`.mobile-button-wrapper .button`, 24px radius, black fill) suggests a distinct compact CTA treatment below the primary breakpoint, but the exact breakpoint value was not present in evidence, so 768px/1024px are proposed conventions.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven behavior were observed. The mapping of TradeGothicLTStd vs. Libre Franklin to specific heading/body roles is inferred from typical brand usage, not confirmed via `--font-body-family`/`--font-heading-family` values, which were not resolved in the supplied CSS. Base font-size (`1.5rem` on `body`) could yield a larger-than-typical body size if root font-size is 16px, or a smaller one under a common 62.5% root reset; actual root value was not supplied, so `body-md` at 16px is a proposed approximation. Spacing and rounded scales beyond the directly observed 100px/24px radii and button padding are proposed conventions, not measured. Licensing and web-availability of TradeGothicLTStd and Exo were not verified. Mobile/tablet layout behavior, navigation collapse mechanics, and card grid breakpoints are proposed design recommendations only.
