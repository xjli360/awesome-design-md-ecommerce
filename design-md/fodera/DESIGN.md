---
version: alpha
name: "Fodera"
source_url: "https://www.fodera.com"
captured_at: "2026-09-28T09:51:30.423261+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fodera is a Brooklyn-based luthier producing handmade custom basses and guitars since 1983, and the evidence reflects a crafted, materials-forward storefront rather than a mass-market retailer. The observed palette centers on warm brass and wood tones (#ab8c52, #9a7e4a, #806430, #868154, #7d784e) layered over a family of near-white and cream neutrals (#ffffff, #fcfbf9, #f5f2ec, #f7f4ef, #f4f0e8, #ece7db) with charcoal-to-black text values (#121212, #212121, #303030). These warm neutrals and metallic-gold tones are inferred as the primary brand accent, evoking hardware finishes and tonewood, since no single CSS rule labels a "brand color" variable. A small set of cool grays (#c9cccf, #d3d3d3, #e3e3e3) appears reserved for hairlines and structural chrome, while #de3618 is treated as an inferred alert/sale color and #0070c9/#c9e7ff/#00ffff are Algolia search-widget system colors, not brand colors, and are excluded from the core palette. Typography draws on three observed sans-serif families — IBM Plex Sans, Inter, and Poppins — with roles assigned by inference: Poppins for display headings, IBM Plex Sans for body and UI text, and Inter for compact search/utility text. Layout figures (header height, logo width) are taken directly from CSS custom properties; all spacing/radius scales beyond that are proposed conventions suited to a premium instrument-maker aesthetic.

colors:
  primary: "#ab8c52"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#636262"
  hairline: "#d3d3d3"
  surface-soft: "#f5f2ec"
  surface-card: "#fcfbf9"
  on-primary: "#ffffff"
  accent-dark: "#806430"
  accent-olive: "#7d784e"
  cream: "#f7f4ef"
  taupe: "#a49c8b"
  border-light: "#e3e3e3"
  alert: "#de3618"
  overlay-scrim: "#00000033"
typography:
  display-xl: {fontFamily: "'Poppins', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Poppins', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Inter', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-light}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xxl}"

## Components

**button-primary** is proposed as the brass-toned call-to-action (e.g. "Add to Cart," "Inquire") using `{colors.primary}` as fill; hover/active states are proposed to darken toward `{colors.accent-dark}` but were not observed in static CSS.

**button-secondary** is an outlined variant for lower-emphasis actions such as "View Details," using the hairline gray border so it recedes against product photography; its states are proposed.

**text-input** covers search fields and any contact/inquiry forms; padding and border values are proposed conventions since only Algolia-widget input tokens were present in evidence, not a native site input style.

**nav-bar** is inferred from the `.theme__header` and `.header__logo__link` rules, which supply real padding (`--PT`/`--PB: 15px`) and logo width (300px desktop / 120px mobile). The bar is modeled as a light, low-contrast strip appropriate to a craft-goods brand rather than a high-chroma retail header.

**product-card** represents individual bass/guitar listings in a grid; the cream-white card surface and thin border are proposed to separate instrument photography from the warm off-white page background (`{colors.surface-soft}`).

**hero** models the homepage introduction ("Handmade in Brooklyn, NY since 1983") as a large display headline over the soft cream background; exact hero markup and imagery placement were not present in the supplied CSS, so this is a proposed pattern.

**footer** is proposed as a dark, near-black band (`{colors.ink}`) for contrast against the light body, appropriate to a workshop/atelier brand; content structure (links, newsletter) was not observed.

**badge** uses the one clearly non-neutral, high-chroma color in the palette (#de3618) as an inferred sale/limited-availability indicator; no badge markup was present in evidence, so this role is proposed.

**search** reflects the real Algolia Autocomplete (`aa-*`) classes found in the CSS, including `.aa-DetachedSearchButton` and `.aa-ClearButton`; colors here are approximated from the neutral/hairline palette since the Algolia component ships its own RGB custom properties (e.g. `--aa-text-color-rgb`) rather than exposing hex values matching the observed palette.

**swatch-selector** is a category-appropriate proposed component for wood/finish or hardware options, justified by the observed `--swatch-size`, `--swatch-size-product`, and `--swatch-size-filters` custom properties, which indicate a swatch-driven variant picker exists on product or filter pages even though its visual styling was not captured.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior, informed only by the real header-height and logo-width custom properties observed (`--HEADER-HEIGHT`, `--HEADER-HEIGHT-MEDIUM`, `--HEADER-HEIGHT-MOBILE`, and logo widths of 300px/120px):

| Breakpoint | Range | Header height | Logo width | Notes |
|---|---|---|---|---|
| Mobile | <768px | ~67px | 120px | Nav collapses to a menu icon + search icon; touch targets ≥44px |
| Tablet/Medium | 768–1199px | ~147px | 120–300px (proposed transition) | Condensed nav, product grid narrows to 2 columns (proposed) |
| Desktop | ≥1200px | ~200px | 300px | Full nav, multi-column product grid (proposed) |

Touch targets should be at least 44×44px for nav icons and swatch selectors (proposed, not verified). Navigation collapse behavior, menu animation, and exact grid column counts were not present in the supplied CSS and are therefore proposed conventions only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is built from static CSS custom properties, a color list, font-family names, and a page-text excerpt dominated by a currency/country selector; no rendered layout, hover/focus states, or mobile interaction were observed. Semantic role assignment (primary brand color, heading vs. body font pairing) is inferred from typical craft/luxury-brand conventions and the relative prominence of warm gold-brown tones in the palette, not from an explicit brand style declaration. Several palette entries (`#0070c9`, `#c9e7ff`, `#00ffff`) belong to the Algolia search widget's own RGB variable system and were deliberately excluded from brand color roles. Spacing, radius, and most typography sizes are proposed scales consistent with the observed header/logo measurements, not extracted values. Font availability, licensing, and actual weights served for IBM Plex Sans, Inter, and Poppins were not verified. No product-detail, cart, or checkout markup was present in evidence, so `product-card`, `swatch-selector`, `badge`, and `hero` are proposed patterns grounded only in adjacent CSS signals (e.g. swatch-size variables) rather than direct observation.
