---
version: alpha
name: "Diggs"
source_url: "https://diggs.pet"
captured_at: "2026-09-28T05:17:19.123668+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Diggs presents dog crates and crate-adjacent bedding through a restrained,
  warm-neutral system rather than a saturated pet-brand palette. The observed
  Shopify CSS variables anchor a near-white canvas (#ffffff) against a warm
  cream secondary surface (#f4eee9), with a dark charcoal-green
  (#343633) used consistently as both body text and primary button fill,
  paired with a muted plum-gray (#4c4a4e) for hover and secondary text states.
  This is a deliberately quiet, editorial palette suited to a "designed
  object" framing of a crate rather than a typical playful pet-store look.
  Border radii are set extremely small (2px) across buttons, inputs, blocks,
  and product cards via dedicated --border-radius-* variables, producing a
  crisp, squared, almost architectural aesthetic that reinforces the brand's
  safety-engineering positioning. Additional palette values such as sage
  (#c5ceba) and warm taupe (#6d635b) are inferred secondary/decorative
  accents (e.g. product-swatch or lifestyle-photography tones); the blue tones
  (#1990c6/#136f99) come from Shopify's accelerated-checkout button styling
  and are treated as functional utility color, not brand identity. Font
  families found in the stylesheet (Duplet Open, Recta, Inter, Helvetica)
  are present but not conclusively mapped to heading vs. body roles in the
  supplied CSS, so that assignment below is inferred.

colors:
  primary: "#343633"
  ink: "#343633"
  canvas: "#ffffff"
  body: "#343633"
  muted: "#4c4a4e"
  hairline: "#dedede"
  surface-soft: "#f4eee9"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-checkout: "#1990c6"
  accent-checkout-hover: "#136f99"
  sage: "#c5ceba"
  taupe: "#6d635b"
typography:
  display-xl: {fontFamily: "Recta, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Recta, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Duplet Open, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Helvetica, sans-serif", fontSize: 19px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  caption: {fontFamily: "Inter, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0.02em}
  button-md: {fontFamily: "Duplet Open, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "64px"
    padding: "{spacing.none} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  crate-size-selector:
    backgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    gap: "{spacing.xs}"

## Components

**button-primary** is the dark charcoal-green fill (#343633) with white text, mapped directly from the observed `--color-button` / `--color-button-text` pair. The 2px radius reflects the site's `--border-radius-button` variable and should be treated as an intentional squared style, not a rounding oversight.

**button-secondary** uses the warm cream secondary surface as a low-emphasis fill with primary-colored text, matching the `--color-button-secondary` role; a thin hairline border is proposed since no explicit secondary-button border was observed.

**text-input** is proposed on a white canvas with a hairline border and 2px radius, consistent with the observed `--border-radius-input: 2px` variable; focus/error states are not observed and are proposed only.

**nav-bar** reflects the measured `--header-height: 64px` variable; background, spacing, and border are inferred defaults for a sticky/utility header pattern (search, cart, account) referenced in the crawled markup, not visually confirmed.

**product-card** proposes a slightly-off-white card surface distinct from pure white canvas, with the same 2px block radius used site-wide (`--border-radius-product`), sized to hold title, price, and sale-price patterns seen in the excerpt (e.g. "Regular price / Sale price").

**hero** is a proposed full-width band using the cream secondary background and display typography, inferred from the homepage's large intro copy ("Where they choose to rest") but layout proportions are not measured.

**footer** is proposed on the cream surface with muted-gray body text, a typical closing pattern for this kind of Shopify theme; content/links are not enumerated in the supplied evidence.

**badge** is proposed as a pill using the primary fill, useful for "Best-Seller," "Sold Out," or "Award-Winning" labels referenced in the text content; shape and color are inferred, not observed in CSS.

**crate-size-selector** is a category-appropriate proposed component for choosing crate size (per the FAQ's sizing guidance), styled as a small toggle group using primary-fill active state and card-surface inactive state; no such UI was directly observed in the supplied CSS.

## Responsive Behavior

This is a recommended structure, not measured site behavior:

| Breakpoint | Width       | Notes                                      |
|-----------|-------------|---------------------------------------------|
| Mobile     | <600px      | Single-column, nav collapses to drawer menu |
| Tablet     | 600–1024px  | 2-column product grids                      |
| Desktop    | >1024px     | Multi-column grids, persistent nav bar (64px)|

Touch targets should be at least 44px, matching the `clamp(25px, ..., 55px)` range observed in the Shopify accelerated-checkout button CSS. Navigation collapse below tablet width and drawer-based menus are standard for this theme family but not confirmed from the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction only; no rendered layout, spacing rhythm, or interaction states (hover/focus/active, form validation, drawer/menu animation) were observed.
- Font-role mapping (which of Duplet Open, Recta, Inter, Helvetica serves heading vs. body vs. button) is inferred, since supplied CSS references `var(--font-*-family)` without resolved values.
- Font availability, licensing, and self-hosting status for Duplet Open/Recta are not verified.
- Most numeric type sizes (display-xl, display-md, title-md, caption, button-md) are proposed design values, not measured from rendered CSS; body-sm (14px/1.4/.02em) and the body base size (1.2rem via `--font-body-scale`) are the only sizing values grounded in supplied declarations.
- Color-role assignments beyond the explicit `--color-*` variables (e.g. sage, taupe, checkout blues) are inferred from palette presence only and may represent product-swatch or third-party (Shopify wallet) colors rather than core brand identity.
- Mobile menu, cart drawer, and product-page layouts were not present in the supplied evidence and are not described here.
