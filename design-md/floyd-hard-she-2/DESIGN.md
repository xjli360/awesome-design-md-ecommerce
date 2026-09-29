---
version: alpha
name: "Floyd"
source_url: "https://floyd.one"
captured_at: "2026-09-29T04:16:17.250008+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Floyd's public CSS exposes a small, restrained palette built around deep
  wine/plum darks (#372229, #522e3e, #43273a) paired with near-black text
  (#121212, #373737) on a white canvas (#ffffff). These plum tones appear in
  the navigation text and border variables and are treated here, as an
  inferred mapping, as the brand's identity color for headers and footers.
  A single saturated blue (#1990c6, hover #136f99) appears only inside the
  Shopify accelerated-checkout widget; it is adopted here as the interactive
  "primary" action color since no other accent exists in the evidence, and
  this substitution is explicitly inferred rather than confirmed brand usage.
  Neutral grays (#dedede, #8f8d8d) and translucent overlays (#00000033,
  #3636364d, #ffffffe6) support hairlines, muted text, and card surfaces.
  Two font families are present in the evidence, Instrument Sans and Nunito,
  both sans-serif; monospace stacks appear to be system/code fallbacks and
  are not used for brand type. The root scale (--text-xs through --text-xl,
  16-22px) is used directly for body-level type; larger display sizes are
  proposed extrapolations, not measured. The interpretation favors a clean,
  minimal, product-forward layout suited to a modern hard-shell luggage
  brand referencing skate-culture origins.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#373737"
  muted: "#8f8d8d"
  hairline: "#dedede"
  surface-soft: "#c8c8c833"
  surface-card: "#ffffffe6"
  on-primary: "#ffffff"
  wine: "#522e3e"
  wine-dark: "#372229"
  wine-alt: "#43273a"
  success: "#307a07"
  overlay-faint: "#0000000d"
  overlay-soft: "#00000033"
  overlay-medium: "#3636364d"
  overlay-strong: "#00000066"
  ink-pure: "#000000"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Nunito, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Nunito, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Nunito, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Instrument Sans, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Instrument Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.wine-dark}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    overlay: "{colors.overlay-strong}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.wine-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.wine}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  case-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the checkout-widget blue as an inferred primary action color for "Add to cart" and checkout CTAs; the hover state (`#136f99`) is directly observed in the accelerated-checkout CSS and is proposed here as the general button hover treatment.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Learn more," size guides), using the hairline gray for its border and ink for text, since no secondary-button CSS was present in evidence.

**text-input** models newsletter and account form fields observed in the page text (email signup, login). Border and radius values are proposed defaults; no explicit input CSS was supplied.

**nav-bar** reflects the `--floyd-navigation-*` custom properties directly: a white background, wine-dark text, and a 15%-opacity wine-dark hairline border, matching the observed solid-header state.

**product-card** is proposed for the Travel Cases/Bags grid ("CABIN," "CHECK-IN," "TRUNK" listings with sale prices), using the translucent white card surface for subtle separation on imagery-heavy backgrounds.

**hero** models the homepage video/banner section ("wheel it your way!") using the dark overlay variables (`--page-overlay`, `--header-transparent-header-text-color`) to justify a dark-background, light-text treatment over full-bleed media.

**footer** uses the darkest wine tone as an inferred footer background to visually bookend the wine-toned navigation, though the actual footer background color was not directly present in the supplied CSS.

**badge** covers "NEW" and sale-price labels seen in the product excerpts; since the true on-sale red (`227 44 43`) is not part of the supplied hex palette, wine is reused here as a compliant substitute, explicitly labeled inferred.

**search** is a proposed pattern for a site search field, using the softest translucent gray surface token for a recessed appearance consistent with the neutral surface family.

**case-spec-panel** is a category-specific proposed component for hard-shell luggage product pages, intended to hold dimensions/weight/material specs (relevant to CABIN, CABIN ALUMINUM, CHECK-IN, BOLD, TRUNK cases), styled with the same soft-surface and hairline tokens as other content panels for visual consistency.

## Responsive Behavior

This is a recommended, non-measured breakpoint structure, since no media-query evidence was supplied:

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| sm        | 0–639px    | Single-column nav collapses to a menu icon; stacked product cards. |
| md        | 640–1023px | Two-column product grids; nav remains collapsed. |
| lg        | 1024–1279px| Full horizontal nav grid (`primary-nav logo secondary-nav`) per observed header structure. |
| xl        | 1280px+    | Max-width content container with `--container-gutter` (2rem–3rem observed) applied. |

Touch targets should be a minimum 44px height, matching the observed `--shopify-accelerated-checkout-button-block-size` default of 44px. Navigation and filter collapse behavior for mobile is not observed and should be validated against the live site before implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed.
- The mapping of wine/plum tones and blue to "primary"/"brand" roles is inferred; no CSS variable explicitly labeled a single brand primary color.
- Display-level typography sizes (display-xl, display-md, title-md) are proposed extrapolations beyond the observed `--text-xs`–`--text-xl` scale (16–22px), which itself appears intended for body/UI text, not headings.
- Font availability, licensing, and actual weight/style variants for Instrument Sans and Nunito were not verified beyond their presence in the CSS font-family list.
- Sale/error/success badge colors reference RGB triples in CSS custom properties that do not correspond to any hex in the supplied palette; where reuse was necessary, this is explicitly noted as a substitution.
- Mobile/responsive layout, breakpoint values, and nav-collapse behavior are proposed recommendations, not measured from the live site.
- Rounded-corner values are template defaults; the only radius evidence observed was a `0px` fallback on the Shopify payment button, so all other radius values are unconfirmed.
