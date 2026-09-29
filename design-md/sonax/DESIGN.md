---
version: alpha
name: "Sonax"
source_url: "https://sonax.com"
captured_at: "2026-09-29T04:09:12.970152+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sonax's evidence set exposes a compact CSS custom-property system: a saturated
  "sonax red" (#e3000b) as the sole brand accent against a near-white canvas
  (#f9f9f9) and near-black body copy (--ui-emphasis, #313030). Supporting
  neutrals (#ebebeb, #e0e0e0, #b4b4b4, #888888, #5d5c5c, #1b1a1a) form a
  grayscale ramp used for surfaces, hairlines and muted text; a secondary red
  (#be2832, named --ui-danger) and a blue focus ring (#3b82f6) are also
  defined but their exact UI roles are not shown in the excerpt, so they are
  treated as inferred (danger/alert and accessibility focus state,
  respectively). Typography is set entirely in "Lufga, sans-serif" with a
  responsive scale (h1 ~52-66px down to ~14px UI/annotation text); font
  weights are not present in the evidence and are therefore proposed, not
  observed. The interpretation below reads Sonax as a German industrial/
  automotive-care brand: high-contrast red-on-white for calls to action,
  restrained gray surfaces for product cards and range navigation (PROFILINE,
  XTREME, PREMIUM CLASS), and generous copy line-height for instructional,
  spec-driven product content. All spacing and rounding values are proposed
  conventions, not measured from the site.

colors:
  primary: "#e3000b"
  ink: "#1b1a1a"
  canvas: "#f9f9f9"
  body: "#313030"
  muted: "#888888"
  hairline: "#e0e0e0"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  danger: "#be2832"
  strong: "#5d5c5c"
  focus-ring: "#3b82f6"
typography:
  display-xl: {fontFamily: "Lufga, sans-serif", fontSize: 62px, fontWeight: 600, lineHeight: 1.0, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lufga, sans-serif", fontSize: 44px, fontWeight: 600, lineHeight: 1.09, letterSpacing: -0.25px}
  title-md: {fontFamily: "Lufga, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Lufga, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.67, letterSpacing: 0px}
  body-sm: {fontFamily: "Lufga, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lufga, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0px}
  button-md: {fontFamily: "Lufga, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0.25px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  range-tile:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is the sonax-red CTA (e.g. "Explore now", "Learn more") intended for hero and section-level actions; hover/active/disabled states are proposed, not observed in the evidence. **button-secondary** proposes a low-emphasis outlined variant for secondary actions like "Contact us," using the hairline gray border rather than red, to avoid competing with the primary CTA. **text-input** and **search** cover the header search field ("What are you looking for?") with a card-white background and hairline border; focus state is proposed to use the supplied `--focus-ring` blue (#3b82f6), the only accessibility-adjacent color in the evidence. **nav-bar** models the top navigation (Products, Car Care sub-menu, About SONAX, language switcher) on the light canvas color with dark ink text, since no header-specific background override was present in the evidence. **product-card** represents the top-seller grid items (e.g. "XTREME Wheel Cleaner PLUS") on a white card surface with a subtle hairline border; the exact card chrome (shadow, hover lift) is not observed and is proposed. **range-tile** is a category-specific component for Sonax's distinct product ranges (PROFILINE, PREMIUM CLASS, XTREME, Bike, Caravan) shown as tiles on the soft-gray surface with red accent, matching the segmented "business segments" content pattern in the excerpt. **hero** models the dark full-bleed intro band ("Bright times ahead") using the near-black ink color as background with white text, since large marketing headers on automotive sites typically invert contrast; this is inferred, not confirmed by supplied CSS. **footer** and **badge** are proposed conventional patterns — the footer as a dark, muted-text block for legal/contact links, and badge as a small rounded red label for merchandising flags (e.g. "New," "Bestseller") implied by the "Top sellers" carousel content but not visually confirmed.

## Responsive Behavior

The CSS evidence contains multiple `:root` spacing and font-size variable blocks that vary by breakpoint (implying at least small/tablet/desktop/wide tiers), but exact `min-width` values were not included in the supplied rules, so the table below is a **recommendation only**, not a measured breakpoint set:

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| Mobile | < 640px | Single-column product/range grid; nav collapses to a hamburger/off-canvas menu; hero title falls back near `display-md` scale. |
| Tablet | 640–1024px | 2-column product cards; nav shows condensed top-level items only. |
| Desktop | 1024–1440px | Matches the mid-range `--font-size-h1` (~62px) and `--s-*` tokens observed; full mega-menu nav. |
| Wide | > 1440px | Largest observed h1 (~66px) and largest spacing tokens (`--s-extra` up to 216px), used for generous section padding. |

Touch targets should be at least 44×44px for nav, search, and button-primary per general accessibility convention (not site-verified). Mobile nav collapse behavior, menu animation, and carousel interaction ("01 - 00" top-seller slider) were not observed and are proposed based on the presence of an itemized product carousel in the page text.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot, not a rendered or interactive audit. Font **weights** are not present anywhere in the supplied CSS custom properties and are therefore inferred conventional values (400/600), not confirmed Lufga weight availability. The **letter-spacing** values in typography are proposed defaults, not measured. Several palette entries (`#be2832` danger, `#3b82f6` focus-ring, `#0000000d`, `#00000026`) have plausible but unconfirmed semantic roles (alert states, focus outlines, overlay/shadow alpha) since no selector usage was supplied linking them to specific components. Rounded-corner and spacing scales are conventional systems layered onto the brand, not extracted from observed `border-radius`/spacing usage (the evidence only exposes abstract `--s-*` spacing tokens without unit-to-role mapping). Hover, active, disabled, and error states for all interactive components are proposed, not observed. Mobile/tablet layout, menu collapse mechanics, and carousel/slider behavior were not captured in the evidence and are inferred from standard e-commerce/marketing patterns. Licensing and self-hosting status of the "Lufga" font were not verified.
