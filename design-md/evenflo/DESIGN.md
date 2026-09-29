---
version: alpha
name: "Evenflo"
source_url: "https://evenflo.com"
captured_at: "2026-09-29T04:08:04.731737+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Evenflo's storefront runs on a Shopify Online Store 2.0 theme (Dawn-family CSS
  custom-property naming: --color-background, --color-foreground, --color-button)
  layered with a third-party mega-menu app. The observed palette centers on a
  teal-cyan action color (#00aea9, with a darker #007e79/#00908b hover/pressed
  family) against a near-black ink (#121212) and white canvas, which reads as a
  clinical, safety-forward pediatric-product identity rather than a soft nursery
  palette. Supporting blues (#1990c6, #136f99, #0f3c5a) appear on Shopify's
  accelerated-checkout buttons and are treated here as a secondary/informational
  accent family. A muted sage (#cbdc82) and a red (#c93844) surface in the
  evidence and are mapped, as inferred roles, to "eco/Green & Gentle" messaging
  and sale/clearance flagging respectively, since no other semantic signal was
  captured.

  Typography pairs a proprietary display face (mr-eaves-sans, inferred for
  headings) with mr-eaves-modern (confirmed on an add-to-cart button) and a
  system/Assistant-led sans stack for body copy, per the theme's font-family
  fallback list. Body font-size and letter-spacing values (1.5rem / 0.06rem) are
  taken directly from base.css. All other sizes, radii, and spacing are proposed
  defaults for a clean, trust-oriented commerce layout, not measured breakpoints.

colors:
  primary: "#00aea9"
  primary-hover: "#007e79"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#666666"
  hairline: "#e6e6e6"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfd"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  accent-red: "#c93844"
  accent-green: "#cbdc82"
  deep-navy: "#0f3c5a"
typography:
  display-xl: {fontFamily: "\"mr-eaves-sans\", sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"mr-eaves-sans\", sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "\"mr-eaves-sans\", sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "\"Assistant\", \"Noto Sans\", sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "\"Assistant\", \"Noto Sans\", sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.04rem}
  caption: {fontFamily: "\"Assistant\", \"Noto Sans\", sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05rem}
  button-md: {fontFamily: "\"mr-eaves-modern\", sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.02rem}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  fabric-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** maps directly to the observed `--color-button: 0,174,169` / `--color-button-text: 255,255,255` pair, with the darker `#007e79` reserved as a proposed hover state seen elsewhere in the CSS as an add-to-cart hover color.

**button-secondary** is a proposed outline treatment using ink-on-white, inferred from the theme's `--color-secondary-button` / `--color-secondary-button-text` variables (white background, dark text) rather than any directly captured secondary button screenshot.

**text-input** is a proposed pattern; no input-specific CSS was supplied, so border and padding values follow the theme's general hairline and body-typography conventions.

**nav-bar** reflects the mega-menu text color (`rgba(68,68,68,1)` → `#444444`) confirmed in the evidence, with layout (sticky/height) left unobserved and proposed.

**product-card** is inferred from Shopify's `.product-card-wrapper .card` custom-property scaffold (corner-radius, border, shadow variables referenced but not resolved to concrete values), so radius and shadow are proposed defaults rather than measured.

**hero** is a proposed full-bleed banner pattern appropriate to the "Revolve Rotating Car Seats" promotional module named in the page text; no hero CSS block was captured.

**footer** color is inferred by assigning the deep navy (`#0f3c5a`) from the palette to a dark footer surface, a plausible but unverified semantic mapping since no footer selector was present in evidence.

**badge** uses `#c93844` for a proposed "Sale"/clearance indicator, consistent with the many "Sale" labels in the page text, though the badge's actual color was not directly evidenced (theme default badge tokens were white/black).

**search** is a proposed pill-shaped input, styled from general surface/hairline tokens; no search-bar CSS was supplied.

**fabric-swatch-selector** is a category-appropriate proposed component for car-seat/stroller fabric color options (e.g., "Quartz," "Champagne," "Agate," "Travertine" named in bestseller listings), using the primary teal as an active-state ring.

## Responsive Behavior
Recommendation only — no live breakpoints, resize behavior, or device layouts were observed in the supplied evidence.

| Breakpoint | Width       | Layout guidance (proposed)                          |
|------------|-------------|------------------------------------------------------|
| mobile     | 0–599px     | Single-column, collapsed hamburger nav, stacked hero |
| tablet     | 600–989px   | 2-column product grid, condensed mega-menu           |
| desktop    | 990–1279px  | Full mega-menu, 3–4 column product grid              |
| wide       | 1280px+     | Max-width container, 4+ column grid, persistent nav  |

Touch targets should be at least 44×44px for cart, add-to-cart, and swatch controls. The mega-menu (evidenced by `.gm-menu` selectors) should collapse to an accordion/drawer pattern below tablet width; this is a standard proposed pattern, not a confirmed interaction from the CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered screenshots, computed layout, or JavaScript-driven interaction states (hover, focus, mega-menu open/close, cart drawer) were observed.
- Several colors (e.g., `#c93844`, `#cbdc82`, `#0f3c5a`) were present in the supplied palette but their functional role (sale badge, eco tag, footer) is an inferred semantic assignment, not a captured usage context.
- `mr-eaves-sans` as the heading font is inferred from the broader `mr-eaves-*` font family group; only `mr-eaves-modern` was directly tied to a CSS rule (an add-to-cart button). Licensing/self-hosting status of both is unverified.
- All font sizes above 15px (body) and all letter-spacing/line-height values for headings, captions, and buttons are proposed, not measured, since only body-level typography rules were supplied.
- Border radius and spacing scales are proposed defaults; the theme references corner-radius via unresolved CSS custom properties (`--product-card-corner-radius`, etc.) whose actual pixel values were not in evidence.
- No mobile menu, filter/sort UI, or checkout-page styling was captured beyond the generic Shopify accelerated-checkout button.
