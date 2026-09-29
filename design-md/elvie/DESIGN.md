---
version: alpha
name: "Elvie"
source_url: "https://elvie.com"
captured_at: "2026-09-29T03:58:44.933049+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Elvie's storefront evidence points to a clinical-meets-soft aesthetic built around a muted slate-blue primary (#484b5d, darkening to #575b70 on hover) against a predominantly white canvas. Body copy uses near-black (#333333/#111111) for legibility, while warm off-white surfaces (#faf8f6, #f5f5f5) separate cards and sections from pure white. Accent hues are used sparingly and semantically: a muted teal (#54b8b3) suggests a wellness/calm accent tone, a deep red (#a70100) marks discount and sale badges, and a bronze/gold (#7e6b45) marks "best seller" badges — these role assignments are inferred from the supplied badge selectors, not confirmed brand guidelines. A system blue (#007aff) appears only in a Swiper carousel theme variable, so it is treated as a utility/interaction color rather than brand identity.

  Typography evidence lists MuseoSans alongside a standard system/Noto Sans stack; MuseoSans is treated as the probable brand display font for headings, with Noto Sans/system-ui as body and fallback, since no distinct proprietary body font was observed. Spacing, radius, and breakpoint scales below are proposed conventions consistent with the evidence but are not measured page geometry. The result is a restrained, clinical-soft design language suited to a medical-adjacent feeding/wellness brand.

colors:
  primary: "#484b5d"
  primary-hover: "#575b70"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#737373"
  hairline: "#e8e8e8"
  surface-soft: "#f5f5f5"
  surface-card: "#faf8f6"
  on-primary: "#ffffff"
  accent-teal: "#54b8b3"
  accent-sale: "#a70100"
  accent-gold: "#7e6b45"
  accent-link: "#007aff"
  accent-success: "#478947"
  accent-sage: "#c2ccb6"
  dark-ink: "#1c1d27"
  border-strong: "#9ca3af"
typography:
  display-xl: {fontFamily: "MuseoSans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "MuseoSans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "MuseoSans, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "MuseoSans, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    hoverBackgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "transparent"
    saleColor: "{colors.accent-sale}"
    bestSellerColor: "{colors.accent-gold}"
    newColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  pump-compare-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed `--color-background-primary-button: #484b5d` and its hover state `#575b70`, taken directly from the product-form add-to-cart submit rule. This is the highest-confidence component since both default and hover values were explicitly present in the CSS.

**button-secondary** is a proposed outline variant, inverting the primary color onto a white background for lower-emphasis actions like "View Details." No secondary button styling was directly observed, so its border/text treatment is inferred from the primary palette.

**text-input** is a proposed form-field treatment using the light hairline gray for a resting border and the primary slate for focus, following common e-commerce conventions; no input-specific CSS was supplied.

**nav-bar** is inferred from the extracted navigation text structure (Breast Pumps, Accessories, Elvie Rise, Offers, Sign In) rather than measured styles; a white background with hairline underline is proposed for a clinical, uncluttered header.

**product-card** reflects the repeated pattern of product name, badge, and "Unit price / per" copy seen in the page text, styled on the warm off-white `#faf8f6` surface with a soft radius, consistent with a feeding/wellness storefront selling multiple SKUs (Pump, Stride, Stride 2, accessories).

**hero** is proposed to carry the large promotional banner text ("MEET ELVIE RISE", pump discount codes) seen in the excerpt, using the largest display typography on the soft surface tone rather than pure white, for visual separation from body sections.

**footer** uses the darkest observed ink tone (`#1c1d27`) as an inferred footer background with white text, a common pattern for brand trust/warranty messaging (free shipping, 2-year warranty, chat support) referenced in the text.

**badge** directly maps the three observed `.product-badge[data-handle]` rules: sale discounts in red (#A70100), best-seller in bronze (#7e6b45), and new-product labels in black — this is one of the few components with explicit selector-level color evidence.

**search-bar** and **pump-compare-table** are proposed, category-appropriate components: search is a generic rounded utility pattern, while the compare table addresses the site's core task of differentiating Elvie Pump vs. Stride vs. Stride 2 by suction, noise, and price — using the teal accent to highlight recommended specs. Neither was observed in the supplied CSS.

## Responsive Behavior

Recommended breakpoints (not measured, but aligned with the `--media-*` custom properties observed in theme CSS): mobile up to 479px, small tablet 480–719px, tablet 720–959px, desktop 960–1199px, wide desktop 1200px+ (theme also defines a 1400px max content width). Navigation should collapse to a hamburger/flyout below 960px, consistent with the observed `--flyout-width: 460px` variable suggesting an off-canvas panel pattern. Touch targets for buttons and badges should maintain a minimum 44px height, mirroring the Swiper navigation's own `--swiper-navigation-size: 44px`. Product grids are recommended to reflow from a multi-column desktop layout to single or two-column stacks on mobile. This section is a design recommendation only; no live responsive behavior was observed or tested.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variable names, a handful of explicit selectors, and page text extraction — not from rendered layout, computed styles, or interaction testing. Semantic color roles (e.g., which grays serve as "ink" vs. "muted" vs. "hairline") are inferred from typical usage patterns and may not match Elvie's internal design tokens. Typography sizes for all tokens except those tied to named CSS variables (e.g., `--font-size-body-*`) are proposed, not measured, since actual pixel values for those variables were not resolved in the evidence. MuseoSans is assumed to be a licensed/custom brand font based on its presence in the font-family list, but its availability, licensing, and actual weight range were not verified. No mobile menu, cart drawer, checkout flow, or hover/focus states beyond the two explicitly supplied button rules were observed. Spacing and radius scales are conventional proposals, not extracted from layout measurements.
