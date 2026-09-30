---
version: alpha
name: "Kosterina"
source_url: "https://kosterina.com"
captured_at: "2026-09-28T10:21:00.998262+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kosterina's observed CSS surfaces a cool, muted blue-grey system built around a
  primary button color of #55789e (rgb 85,120,158) against a white canvas, with
  black used for foreground text and links. A cluster of pale blue tints
  (#e4eff7, #f2f7fb, #eff5fa, #c1daed) appear in the palette and are treated here
  as soft section and card backgrounds, evoking olive-oil-tin blues without any
  literal green or gold branding being confirmed in the supplied evidence. A few
  saturated accents (#970000 deep red, #d87787 pink, #249e6b green) recur in
  promo-specific selectors (e.g. a "mothers-day" drawer link and a corporate
  gifting CTA) and are mapped as optional seasonal/badge accents, not core brand
  color. Typography evidence shows CSS custom properties (--k-font-sans,
  --k-font-serif) alongside a font stack containing "circe", "athelas",
  "campton", and "kudryashev-d-excontrast" family names; these are treated as
  the brand's sans, serif body/display, and condensed display candidates
  respectively, with generic serif/sans-serif fallbacks. Buttons observed at
  14px, 700 weight, uppercase, 0.15em tracking; inputs at 4px radius. Sizes
  beyond these literal values are proposed, editorial-leaning choices suited to
  a premium Greek olive-oil and vinegar DTC brand.

colors:
  primary: "#55789e"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#3e3f3f"
  muted: "#6b7280"
  hairline: "#dedede"
  surface-soft: "#e4eff7"
  surface-card: "#f2f7fb"
  on-primary: "#ffffff"
  border-dark: "#bababa"
  accent-red: "#970000"
  accent-pink: "#d87787"
  accent-green: "#249e6b"
  accent-gold: "#f6d86f"
typography:
  display-xl: {fontFamily: "kudryashev-d-excontrast, Georgia, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "kudryashev-d-excontrast, Georgia, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "athelas, Georgia, serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "circe, system-ui, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "circe, system-ui, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "circe, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05em}
  button-md: {fontFamily: "campton, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.15em}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-dark}"
    focusBorderColor: "{colors.primary}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** maps directly to the observed `--color-button:85,120,158` / `--color-button-text:255,255,255` pair (=#55789e on white), used site-wide for primary CTAs like "Shop Now." Radius is set to `none` since the accelerated-checkout button CSS explicitly sets `border-radius:0` by default.

**button-secondary** mirrors the observed `--color-secondary-button` (white background, black text, black border) pattern used for lower-emphasis actions such as "Continue shopping."

**text-input** is grounded in the `.rc-login-form-email` rule: 48px min-height, 12px/16px padding, 4px radius, 1px border, with a focus state that switches border color to `--k-color-accent` (mapped to primary here as a proposed equivalence).

**nav-bar** is inferred from the mega-menu text content (Shop All, Subscription, Olive Oil, Vinegar, Olives, Skincare, Bundles & Gifts) but no header layout CSS was supplied, so spacing and color assignment are proposed, not measured.

**product-card** is a proposed pattern for bestseller/collection grids implied by repeated "Bestsellers" sections; card background uses the light blue surface tint observed in the palette.

**hero** reflects the homepage's large promotional banner content ("Shop the Mediterranean," "NEW LAUNCH") with a soft blue background tint and the display-xl serif treatment; exact hero CSS was not in evidence.

**footer** is a proposed low-key text block using body-sm typography and the hairline color for dividers; no footer-specific selectors were supplied.

**badge** models the "mothers-day" promo drawer link explicitly styled with `color:#d87787`, reused here as a pill-shaped seasonal/sale indicator — a proposed generalization of one observed rule.

**search** is a standard proposed pattern consistent with the input styling observed on the login form, since no distinct search-bar CSS was supplied.

**subscription-card** is the category-appropriate component addressing Kosterina's prominent "Best-Selling Subscriptions" and "Build a Custom Subscription" content; it reuses the primary accent for subscribe-and-save framing, proposed rather than observed.

## Responsive Behavior
This is a recommendation, not measured site behavior — no media queries or breakpoint values were present in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product/hero stacks; nav collapses to hamburger drawer |
| Tablet | 480–1024px | 2-column product grids; mega-menu may remain a drawer |
| Desktop | >1024px | 3–4 column product grids; full horizontal nav with flyout mega-menus |

Touch targets should be at least 44px (aligning with the observed `--shopify-accelerated-checkout-button-block-size:44px` default). Mega-menu flyouts should collapse into accordions below tablet width; this behavior is proposed based on menu content depth, not observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, selector fragments, and page text only — no rendered layout, computed styles, or JavaScript-driven interaction states were observed. Font role assignments (serif vs. sans vs. display) for "circe," "athelas," "campton," and "kudryashev-d-excontrast" are inferred from stack presence, not confirmed usage on specific elements, and licensing/availability of these proprietary families was not verified. Several accent colors (#970000, #d87787, #249e6b, #f6d86f, #e88d21) appear in the raw palette but their functional roles (sale, seasonal, category tagging) are inferred from limited selector context. Type scale sizes beyond the two literal CSS values found (14px button text, 1.6rem input text) are proposed for editorial consistency, not measured. Mobile menu behavior, hover/focus states beyond the documented input focus rule, and footer structure were not present in the supplied evidence and are marked proposed throughout.
