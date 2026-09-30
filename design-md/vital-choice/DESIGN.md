---
version: alpha
name: "Vital Choice"
source_url: "https://vitalchoice.com"
captured_at: "2026-09-28T05:02:52.735956+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Vital Choice is a wild-caught seafood and specialty food e-commerce site built on
  Material-UI (MUI) components, evidenced by MuiButton, MuiTypography, and related
  class selectors in the supplied CSS. The observed UI type system runs on Helvetica
  with sans-serif fallback, rendered at MUI's default scale (button text at 1rem/500
  weight/uppercase; body copy split across two size tiers). A serif display family
  (Playfair Display) appears in the site's loaded font list and is treated here as an
  inferred hero/heading typeface consistent with a premium food brand, though no CSS
  rule in evidence ties it to a specific selector.
  The color palette centers on a burnt-orange accent (#cf3d02, with a darker
  #ad3100 variant) used for secondary/link-style buttons, paired with near-black text
  (#1f1f1b, #2f2f2f) on white and light-gray surfaces (#f5f5f5, #e3e3e3 hairlines).
  Deep teal tones (#173945, #1c586c) and a muted sage green (#5d8c78) are present in
  the palette and are mapped here as ocean/organic accent colors — an inferred
  semantic role, not a confirmed brand system. A saturated red (#b01116) is proposed
  for sale/certification badges given its presence alongside MSC-certified product
  copy. Rounded-sm (4px) directly matches the observed MuiButton-root border-radius.

colors:
  primary: "#cf3d02"
  primary-hover: "#ad3100"
  ink: "#1f1f1b"
  body: "#2f2f2f"
  muted: "#6b6d76"
  hairline: "#e3e3e3"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  teal-deep: "#173945"
  teal-mid: "#1c586c"
  green-organic: "#5d8c78"
  badge-red: "#b01116"
  link-blue: "#086ee0"
typography:
  display-xl: {fontFamily: "Playfair Display, serif", fontSize: 96px, fontWeight: 300, lineHeight: 1.167, letterSpacing: -0.5px}
  display-md: {fontFamily: "Playfair Display, serif", fontSize: 40px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Helvetica, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Helvetica, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.75, letterSpacing: 0.5px}
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
    padding: "{spacing.sm} {spacing.base}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.teal-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  certification-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.teal-mid}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** — A solid burnt-orange call-to-action (Add to Cart, Shop Now), matching the `#cf3d02` accent color visible in the secondary-text button rule. Uppercase button typography and 4px radius are directly observed from `.MuiButton-root`. Hover/disabled darkening to `primary-hover` is proposed, not measured.

**button-secondary** — An outlined variant echoing `.MuiButton-outlinedPrimary` (border at ~50% opacity ink), used here for lower-emphasis actions like "Learn More." Fill-on-hover behavior is proposed.

**text-input** — Search and account-form fields on a white card with a light hairline border, sized to the body-sm scale. Focus-ring color and validation states are proposed; not present in supplied CSS.

**nav-bar** — Persistent header housing Search, Sign In, and Cart, inferred from the page-text ordering ("Search Search Sign In Sign In ... My Orders Cart"). White background with hairline bottom border is proposed for a clean grocery-retail feel; sticky behavior is not confirmed.

**product-card** — Repeating unit for items like "Wild Pacific King Salmon," pairing a title (title-md), review count and ship-date metadata (caption), and a price line. Card shadow/elevation is proposed since MUI's `.MuiButtonBase-root` suggests a Material-style component library is in use.

**hero** — Full-width promotional banner using the deep teal (`#173945`) as an ocean-themed background with white display type, sized from the observed MUI h1 metrics (96px/300 weight). Actual homepage hero copy/imagery was not confirmed in evidence.

**footer** — Dark ink-toned closing band for site links, certifications, and newsletter signup, using body-sm typography on white text. Column structure is proposed, not observed.

**badge** — Small pill label in `badge-red`, proposed for "Bestseller," "MSC Certified," or "Sale" flags referenced in the bestseller/MSC copy. Color choice is inferred from the palette's red cluster, not confirmed as the literal badge color.

**search** — Lightweight input embedded in the nav, using surface-soft background to differentiate from the white nav bar; icon and autocomplete behavior are proposed.

**certification-badge** — Category-specific component for sustainability marks (MSC Certified Seafood), styled in teal-mid text on a soft surface to align with the site's repeated "MSC" labeling in bestseller listings. Iconography is not confirmed from CSS.

## Responsive Behavior

Recommended (not measured) breakpoints:

| Breakpoint | Width | Nav | Product grid |
|---|---|---|---|
| xs | <600px | Collapsed hamburger, search icon-only | 1 column |
| sm | 600–959px | Collapsed hamburger | 2 columns |
| md | 960–1279px | Full horizontal nav | 3 columns |
| lg+ | 1280px+ | Full horizontal nav + secondary utility row | 4 columns |

Touch targets should be a minimum 44×44px for cart/search icons on mobile. Category mega-menu (Bestsellers, Wild Salmon, etc.) should collapse to an accordion under 960px. This table is a design recommendation only; no live responsive behavior was observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static CSS/text only; no rendered screenshots, computed styles, or interaction states (hover, focus, active, loading, error) were observed.
- Color-to-role mapping (e.g., teal as "ocean accent," green as "organic accent," red as "badge") is inferred from palette clustering and page-text context (MSC certification, bestsellers), not confirmed brand documentation.
- Typography sizes for display-md, title-md, caption, and text-input are proposed/estimated; only button, body1, body2, and h1 rules were directly present in the supplied CSS.
- Playfair Display's use as a heading font is inferred from its presence in the site's loaded font list; no selector-level rule confirms where it is applied.
- Spacing scale is a proposed convention; only MuiButton padding (6px 16px) was directly observed and does not map exactly to the proposed token steps.
- Mobile/tablet layout, breakpoint values, and menu-collapse behavior were not observed and are marked as recommendations.
- Custom/licensed font availability (Loretta VF, Canela, ivypresto-text, museo-sans, Yantramanav, etc.) and their licensing terms were not verified; only Helvetica/sans-serif is used in this spec due to direct CSS confirmation.
