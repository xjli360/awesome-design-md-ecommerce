---
version: alpha
name: "Eastpak"
source_url: "https://eastpak.com"
captured_at: "2026-09-29T04:09:07.134522+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation reads Eastpak's observed CSS as a stripped-back, high-contrast
  system built around pure black and white with a warm ivory support ramp
  (#fffbf5, #fff8eb, #ffedce) and a set of saturated accent hues used for
  promotional and status messaging (#e94e2a orange-red, #089b57 green,
  #ffbb33 amber, #345eb2 blue, #d20000/#ad0000 red). The observed
  `.o-dc-button` rule confirms a flat, radius-0, black-on-white primary
  button with a near-black hover state, reinforcing a utilitarian,
  no-frills aesthetic consistent with a durability-first luggage brand.
  Font evidence shows a proprietary "AS Circular" family (Black/Bold/
  Medium/Book/Light weights) alongside Roboto and Helvetica Neue used for
  buttons and index-section headings; role assignment between these is
  inferred, since CSS custom properties (`--font-stack-body`,
  `--font-stack-header`) were not resolved to literal values in the
  supplied evidence. The `.site-header__cart-count` rule (circular badge,
  primary-colored) is the only concrete UI-chrome pattern observed and is
  used directly below. All spacing, rounding scale (beyond the observed
  radius-0 button), and layout breakpoints are proposed conventions, not
  measured observations.

colors:
  primary: "#000000"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#322f29"
  muted: "#322f294d"
  hairline: "#e5e5e5"
  surface-soft: "#fafafa"
  surface-card: "#fff8eb"
  on-primary: "#ffffff"
  accent-sale: "#e94e2a"
  accent-error: "#d20000"
  accent-success: "#089b57"
  accent-warning: "#ffbb33"
  accent-info: "#345eb2"
  border-strong: "#333333"
typography:
  display-xl: {fontFamily: "AS Circular-Black, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "AS Circular-Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "AS Circular-Medium, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "AS Circular-Book, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "AS Circular-Book, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "AS Circular-Light, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaPadding: "{spacing.md} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    sectionSpacing: "{spacing.xxl}"
    hairline: "{colors.muted}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    size: "1em square, centered content"
  warranty-callout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** reflects the observed `.o-dc-button` rule: solid black background, white text, zero border-radius, generous horizontal padding, and Roboto typography — the site's core add-to-cart/CTA pattern.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "View Details"), inverting the primary to a white fill with a dark hairline border, since no secondary-button CSS was captured directly.

**text-input** is a proposed minimal-chrome field (thin hairline border, no fill contrast) consistent with the flat, high-contrast visual language; no form CSS was observed, so padding and radius are conventions.

**nav-bar** is inferred from `.site-header` and `.site-header__mobile-nav`, both of which set `background-color:var(--color-body)` — interpreted here as white/canvas with dark text, matching a light-header retail pattern.

**product-card** is proposed for grid listings (backpacks, luggage, shoulder bags implied by the nav taxonomy); it uses the warm ivory surface-card tone to differentiate cards from the pure-white canvas, a pattern not directly measured.

**hero** models the homepage banner language ("Fear Of God Essentials For Eastpak," "Getter Pro," "Sleek, Strong & Secure") as a dark, full-bleed panel with large display type and a CTA — proposed composition, not a captured layout.

**footer** is grounded in the extensive observed footer link text (Customer Service, Information & Resources, Terms, VF International legal block) and is modeled as a dark, densely-linked multi-column region; exact grid was not observed.

**badge** and **cart-badge** are split: cart-badge is directly evidenced by `.site-header__cart-count` (circular, primary-colored, absolute-positioned counter). badge is a proposed promotional/sale pill using the observed orange-red accent, inferred from "SALE" nav presence and the accent palette.

**warranty-callout** is a category-specific, brand-appropriate component tied to the repeatedly stated "30 Year Warranty / Built To Resist" messaging — proposed as an inline reassurance strip on product and collection pages, using the green accent to signal durability/trust.

## Responsive Behavior
Recommended, not measured breakpoints: mobile <768px (single-column, hamburger nav collapsing `.site-header__mobile-nav`), tablet 768–1024px (2-column product grid), desktop >1024px (full nav bar, 3–4 column grid). Touch targets should be ≥44px for nav links and the cart-badge control; the mobile nav is assumed to collapse into a slide-in panel given the `.site-header__mobile-nav` selector, though its open/close interaction was not observed. All figures are proposed defaults for a retail storefront of this category.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, viewport screenshots, or interaction states (hover, focus, active, mobile menu open) were observed. Several CSS custom properties (`--font-stack-body`, `--font-stack-header`, `--color-body`, `--color-btn-primary`) were referenced but not resolved to literal values, so font-role and background-role assignments in this spec are inferred approximations rather than confirmed measurements. The "AS Circular" font family's licensing and web-availability were not verified — it is treated as a proprietary brand font per the supplied evidence. Spacing scale, border-radius scale (beyond the one observed `border-radius:0` button rule), typography sizes, and breakpoints are all proposed conventions, not extracted values. Color-to-role mapping (e.g., which neutral is "ink" vs "body") is a best-effort interpretation of a large unlabeled palette rather than a documented design-token source.
