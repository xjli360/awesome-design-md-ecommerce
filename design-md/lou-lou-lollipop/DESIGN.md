---
version: alpha
name: "Lou Lou Lollipop"
source_url: "https://louloulollipop.com"
captured_at: "2026-09-29T04:02:54.578412+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lou Lou Lollipop's storefront CSS shows a muted, spa-like palette built around a dusty
  teal-blue (#59757D, used as --ethos-primary-button-bg) against warm off-white and near-black
  text (#1d1d1d). Secondary accents — a terracotta (#a85636) and sage-green (#566b54) — appear
  in product-label-overlay variables for "new" and "meta" badges, while a brick red (#cf2f22)
  marks reduction/sale badges. These CSS-custom-property names strongly suggest badge/label
  roles, so they are mapped accordingly rather than inferred from visual inspection.
  Typography relies on the licensed web fonts "sofia-pro" and "avenir-next-lt-pro" with a full
  system-font fallback stack (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial), which is
  interpreted here as display and body families respectively, though this pairing is a
  reasonable inference rather than a confirmed style-guide split. No explicit font-size,
  radius, or breakpoint values were present in the supplied evidence beyond CSS variable
  references (e.g. --btn-border-radius, --button-text-size) whose computed values were not
  captured; all numeric type, radius, and spacing scales below are therefore proposed,
  editorial-friendly defaults consistent with a soft, rounded, baby-goods aesthetic. The
  resulting interpretation favors gentle contrast, generous whitespace, and pill/rounded
  affordances suited to a nursery and sleepwear catalog.

colors:
  primary: "#59757d"
  ink: "#1d1d1d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#80807f"
  hairline: "#dddddd"
  surface-soft: "#faf9f6"
  surface-card: "#fdfdfa"
  on-primary: "#ffffff"
  accent-sale: "#cf2f22"
  accent-new: "#a85636"
  accent-meta: "#566b54"
  sage-tint: "#d9e1e4"
  sage-deep: "#6a8b95"
  gold: "#f2b321"
  success: "#108043"
typography:
  display-xl: {fontFamily: "sofia-pro, Avenir Next, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "sofia-pro, Avenir Next, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "sofia-pro, Avenir Next, Helvetica Neue, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "avenir-next-lt-pro, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "avenir-next-lt-pro, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "avenir-next-lt-pro, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "sofia-pro, Avenir Next, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1em, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
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
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"

## Components

**button-primary** maps directly to the observed `--ethos-primary-button-bg: #59757D` / `--ethos-primary-button-text: #FFFFFF` pair, used for primary CTAs like "Shop TENCEL™" or add-to-cart actions. Hover/active states referencing `--btn-bg-hover-color` were present as variable names only, so darkened-state values are proposed, not measured.

**button-secondary** is inferred from the `.btn--secondary` rule structure, which swaps in "alt" background/text variables without resolved values; here it is proposed as an outlined, soft-background variant using the same primary teal for text/border to keep a cohesive two-tier CTA system.

**text-input** is a proposed pattern for search and account/newsletter fields; no explicit input CSS was supplied, so border, radius, and padding are editorial defaults consistent with the site's soft, rounded button styling.

**nav-bar** reflects the extensive multi-category mega-menu implied by the page-text excerpt (Sleep & Bedding, Clothing, Feeding, Bathe, Toys & Play, etc.). Its visual treatment (white background, hairline divider) is proposed since no header-specific CSS declarations were captured.

**product-card** is proposed for the "Best-Selling Favorites" and category grids referenced in the text (e.g., Baby Sleeper, Muslin Swaddle listings with USD pricing). Card surface and radius draw on the neutral off-white/white palette to keep print-heavy product imagery legible.

**hero** represents the homepage banner area ("The easiest way to swaddle") using the soft canvas tone `#faf9f6` as background, which appears in the supplied palette as a warm off-white distinct from pure white — a plausible section-background candidate, though its actual usage location is unverified.

**footer** is proposed using the near-black ink color as a grounding band, a common pattern for lifestyle DTC sites; no footer-specific selectors were present in evidence, so this remains an inferred layout choice.

**badge** models the `--product-label-overlay-*` variables directly: reduction/sale badges use `#cf2f22`, "new" badges use `#a85636`, and meta badges use `#566b54` — these are the most concretely evidenced color-role mappings in the whole system.

**search / swatch-selector** are category-appropriate additions: search reflects the visible "Search" nav item, while swatch-selector addresses the many color/print variant lists in the text excerpt (e.g., OneC™ Pacifier Clip in Pink Quartz, Coconut Milk, Sage Green) — a pill-shaped color-dot selector is proposed as a standard pattern for this product type, not an observed component.

## Responsive Behavior

Recommended, non-measured breakpoints (informed only by the presence of `--gutter-mobile`, `--gutter-desktop`, `--gutter-large`, and stepped `--container-pad-x` values of 16px/30px/50px/60px in the CSS):

| Breakpoint | Width | Container padding | Notes |
|---|---|---|---|
| Mobile | <768px | 16px | Single-column nav, stacked hero |
| Tablet | 768–1024px | 30px | 2-column product grid (proposed) |
| Desktop | 1024–1440px | 50px | Full mega-menu, 3–4 column grid |
| Large | >1440px | 60px | Max-width container, extra gutter |

Touch targets are recommended at a minimum 44×44px for buttons and swatch selectors. Mega-menu collapse into an accordion/drawer pattern below tablet width is a standard proposal for this nav complexity, not a confirmed behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS variable declarations, a homepage text excerpt, and a flat color/font list — no rendered layout, computed styles, hover states, or DOM screenshots were available. Several CSS custom properties (`--btn-border-radius`, `--button-text-size`, `--btn-alt-bg-color`, `--container-pad-x` in some contexts) were referenced but never resolved to concrete values in the supplied evidence, so all radius and typographic size figures above are proposed defaults rather than extracted values. Color-to-role assignments for general UI (ink, muted, hairline, surface tones) are reasonable inferences from usage context (e.g., `#1d1d1d` appearing repeatedly as an explicit text color) but were not confirmed against live element inspection. Font availability, licensing, and exact weights for "sofia-pro" and "avenir-next-lt-pro" (both Adobe/Monotype-hosted identifiers) were not verified. No mobile menu, cart drawer, or form-validation states were observed; all such interaction patterns above are explicitly proposed.
