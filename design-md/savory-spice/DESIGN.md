---
version: alpha
name: "Savory Spice"
source_url: "https://savoryspiceshop.com"
captured_at: "2026-09-28T10:21:10.247219+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Savory Spice presents itself as a small-batch, expert-crafted spice merchant,
  and the observed CSS supports a warm, editorial retail aesthetic rather than a
  generic e-commerce look. Root variables define an explicit brand triad: a
  burnt-orange accent (#EB5628), a near-black contrast ink (#202124), and a soft
  off-white surface (#FAFAFA), paired with a serif display face (Recoleta) for
  headings and product titles against a utilitarian sans (Franklin Gothic) for
  body copy, navigation, and buttons. A secondary condensed serif (Oraganatto)
  appears only on product descriptions with wide (.3em) letter-spacing,
  suggesting an intentional "label copy" treatment — this role is inferred from
  a single selector and should be treated as decorative, not structural.
  Supporting greens (#515C3B, #EAF3E8) and a chartreuse "active" state (#D8DF6D
  on #001B00) recur across promo bars and primary buttons, implying an
  agricultural/pantry accent family layered on top of the orange brand color.
  A standalone red (#D20004) is mapped here to sale/alert use as an inferred
  role, since no selector confirms its purpose. The interpretation below treats
  --color-primary/contrast/accent as authoritative and everything else as
  supporting palette to be reused across surfaces, badges, and states.

colors:
  primary: "#eb5628"
  ink: "#202124"
  canvas: "#fafafa"
  body: "#332d27"
  muted: "#7c7a75"
  hairline: "#d9d9d9"
  surface-soft: "#f8f7f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#515c3b"
  on-accent-green: "#fefaf6"
  lime: "#d8df6d"
  on-lime: "#001b00"
  sale: "#d20004"
  surface-alt: "#eaf3e8"
typography:
  display-xl: {fontFamily: "Recoleta, serif", fontSize: 60px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Recoleta, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Recoleta, serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Franklin Gothic', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Franklin Gothic', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Franklin Gothic', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "'Franklin Gothic', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
  eyebrow: {fontFamily: "Oraganatto, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.3em}
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
    backgroundColor: "{colors.lime}"
    textColor: "{colors.on-lime}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid transparent"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "6rem"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    descriptionTypography: "{typography.eyebrow}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.lime}"
    activeTextColor: "{colors.on-lime}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** uses the root `--color-accent` orange with white text, matching the theme's `.btn` pill-shaped pattern (`border-radius:100px`, min-height 44px) observed in the CSS; this is the primary add-to-cart / shop-now action.

**button-secondary** reflects the observed `.btn-primary` and `.button-grid-trigger.active` rules, which pair a chartreuse background (`#d8df6d`) with a near-black-green text (`#001b00`). Its role here is inferred as a secondary or "active filter" state rather than the main CTA, since it appears on toggle/grid controls in the evidence.

**text-input** is a proposed pattern; no input-specific styling was present in the supplied CSS, so border, radius, and padding follow the general `.button`/hairline conventions observed elsewhere. State (focus, error) is proposed, not observed.

**nav-bar** derives its height from the `--height-nav:6rem` custom property and uses the canvas/ink pair for a light, high-contrast header. Sticky behavior and scroll-state changes are not observed and should be treated as proposed.

**product-card** combines the confirmed `.product-title`/`.card-title` → Recoleta mapping with the `.product-description` → Oraganatto, letter-spaced treatment, giving product tiles a distinct "label" feel for the description line. Card chrome (border, radius, padding) is inferred from the general button radius scale, not a captured card selector.

**hero** is a proposed composition using the soft green surface-alt tone (`#eaf3e8`) as a banner background, paired with the large display typography scale confirmed via `--font-size-display`. No hero-specific selector was supplied, so background choice is inferred from adjacent section coloring in the palette.

**footer** reuses the dark olive-green (`#515c3b`) and cream (`#fefaf6`) pairing seen on the `product-links-bar` selector, extended here as an inferred footer treatment since no dedicated footer selector was captured.

**badge** maps the standalone red (`#d20004`) to a sale/promo tag, an inferred role given the presence of a live "Fall Baking Sale — Save 20%" promotional message in the page text but no confirmed badge selector.

**search** and **size-selector** are both proposed, category-appropriate patterns: search follows the pill/hairline convention seen in buttons, while size-selector reflects the repeating "Jar / Refill Bag / Large Bag / Try Me Size" variant pattern visible in the page text, using the same active-state lime/on-lime pairing as button-secondary for consistency.

## Responsive Behavior

This is a recommended structure, not measured site behavior — no breakpoint or device-specific layout was present in the supplied evidence beyond the theme's `--height-nav` step changes (3rem → 4rem → 6rem), which hint at three responsive tiers.

| Breakpoint | Width       | Nav height | Notes (proposed) |
|-----------|-------------|-----------|-------------------|
| Compact    | < 640px     | 3rem      | Single-column product grid, collapsed hamburger nav |
| Medium     | 640–1024px  | 4rem      | Two-column product grid, condensed mega-menu |
| Wide       | > 1024px    | 6rem      | Full mega-menu, multi-column grid, display-xl hero type |

Touch targets should follow the `.btn` `min-height:44px` convention observed in the CSS for all interactive controls (buttons, size-selector chips, search field). Mega-menu categories (Shop All, Gifts, Recipes, etc., seen in page text) are recommended to collapse into an accordion below the Medium breakpoint; this collapse behavior is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no rendered layout, hover/focus states, animations, or actual mobile breakpoints were observed. The `--color-primary/contrast/accent` root variables are treated as authoritative brand roles, but secondary colors (green, lime, red) have their functional roles (footer, active-state, sale) inferred from selector context, not confirmed design documentation. Font availability and licensing for Recoleta, Oraganatto, and Franklin Gothic were not verified — these are proprietary/commercial faces and generic fallbacks (`serif`, `sans-serif`) are included per system rules. Font sizes for `body-sm`, `caption`, `title-md`, and all `rounded`/`spacing` scale values beyond those explicitly present in `:root` are proposed conventions, not extracted measurements. Component padding, borders, and states (hover, disabled, error) are inferred from adjacent CSS patterns (e.g., `.btn`, `.button`) and should be validated against the live site before implementation.
