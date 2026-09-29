---
version: alpha
name: "Modoker"
source_url: "https://modoker.com"
captured_at: "2026-09-28T04:35:55.196713+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Modoker's storefront CSS exposes a fundamentally grayscale interface system:
  --color-foreground and --color-button both resolve to rgb(18,18,18) against a
  pure white --color-background, giving buttons, links, and headings a
  near-black-on-white contrast, with border-radius set to 0 across buttons and
  the Judge.me review widget (--jdgm-border-radius: 0) — suggesting a squared,
  utilitarian aesthetic fitting a garment/business-bag retailer. Layered on this
  neutral base are two accent families: a warm gold/amber group (#ddbe78,
  #fbaa00, #f48500) driving the Judge.me star-rating and "Write a review"
  components, and a cooler blue pair (#1990c6, hover #136f99) on the unbranded
  Shopify accelerated-checkout button. Soft neutrals (#eeeeee, #f2f2f2, #f3f3f3,
  #dddddd) recur as skeleton-loading and card-adjacent tones. Payment/social
  icon colors (Visa, Mastercard, PayPal, Facebook, Twitter, etc.) appear in the
  CSS but are treated as third-party marks, not brand colors. Font stacks list
  Assistant, Baskerville, Nunito Sans, Helvetica, and Arial; this interpretation
  assigns Baskerville (serif) to headings for a tailored, premium bag-brand
  feel and Assistant/Nunito Sans (sans-serif) to body and UI text, mirroring
  the observed --font-heading-family / --font-body-family split. All semantic
  role assignments below are inferred from variable names and component usage,
  not confirmed live rendering.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f3f3f3"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-gold: "#ddbe78"
  accent-amber: "#fbaa00"
  accent-orange: "#f48500"
  link-blue: "#1990c6"
  link-blue-hover: "#136f99"
  badge-teal: "#108474"
  deep-navy: "#111d3b"
  slate: "#242833"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Baskerville, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Baskerville, serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.04rem"}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04rem"}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.06rem"}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  payment-badge-row:
    backgroundColor: "{colors.surface-soft}"
    iconGap: "{spacing.sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    note: "Third-party payment marks (Visa, Mastercard, PayPal, etc.) retain their own brand colors and are not remapped to the site palette."
---

## Components

**button-primary** uses the observed near-black foreground (`{colors.primary}`) with white text, matching the site's `--color-button` / `--color-button-text` pair. It carries `{rounded.none}` to reflect the squared corners implied by Judge.me's `--jdgm-border-radius: 0` and the default Shopify accelerated-checkout radius. Hover/active/disabled states are proposed, not observed.

**button-secondary** mirrors `.button--secondary` variable swapping (`--color-button: var(--color-secondary-button)`), rendering as an outlined ink-on-white button. Border and fill inversion on hover is a proposed interaction, not confirmed.

**text-input** is a plain bordered field using the hairline gray (`{colors.hairline}`) for its edge and a soft corner radius; focus-ring styling is proposed since no focus-state CSS was supplied.

**nav-bar** is inferred from the grid-based `body` layout (`grid-template-rows: auto auto 1fr auto`), which implies stacked header regions. Background and text follow the base foreground/background variables; sticky behavior is not confirmed by the evidence.

**product-card** draws on `.product-card-wrapper .card` custom properties (border-radius, border-width, shadow, image padding all theme-driven) to justify a bordered, softly-radiused card with a serif title and sans-serif price line.

**hero** is a proposed full-bleed banner using the deep navy accent (`{colors.deep-navy}`) as an inferred premium backdrop color, paired with the large serif display type. No hero markup or imagery was present in the supplied evidence.

**footer** uses the slate tone (`{colors.slate}`) as an inferred darker footer band, distinct from the white body background, with hairline dividers between link columns; column structure is proposed.

**badge** is a pill-shaped outline label modeled on `--color-badge-*` variables (foreground/background/border all tied to the same foreground/background pair), suited to "New," "Bestseller," or material tags on bag listings.

**search** is a soft-gray input treatment using `{colors.surface-soft}`, distinguishing it from standard form fields; predictive-results styling is proposed only.

**payment-badge-row** is a category-appropriate footer/checkout element reflecting the many payment- and social-brand hex values present in the CSS (Visa, Mastercard, PayPal, Amex, Google/Apple/Shop Pay, Union Pay). These icon colors are explicitly kept as third-party marks rather than folded into the Modoker palette.

## Responsive Behavior

*Recommendation only — no live breakpoint or device rendering was observed in the supplied evidence.*

| Breakpoint | Width       | Notes (proposed) |
|------------|-------------|-------------------|
| Mobile     | < 480px     | Single-column nav, collapsed hamburger menu, stacked product grid |
| Tablet     | 480–989px   | 2-column product grid, condensed nav-bar |
| Desktop    | 990–1439px  | Full nav-bar, 3–4 column product grid |
| Wide       | ≥ 1440px    | Max-width container, 4+ column grid |

Touch targets on `button-primary`/`button-secondary` should maintain a minimum 44px height, consistent with the observed `.shopify-payment-button__button` `clamp(25px, 44px, 55px)` sizing. Nav and search collapse into an icon-driven mobile pattern; exact collapse thresholds are proposed, not measured.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, selector declarations, and a title string — no rendered page, DOM layout, or interaction was inspected. Color-to-role mapping (e.g., which accent is "primary" vs. incidental) is inferred from variable naming and third-party widget usage (Judge.me, Shopify Pay), not confirmed brand guidelines. Font pairing (Baskerville for headings, Assistant/Nunito Sans for body/UI) is a plausible assignment based on the font families present in CSS, but actual `--font-heading-family` / `--font-body-family` values, weights, and licensing were not resolvable from the supplied evidence. All pixel sizes in the typography scale beyond the observed `1.5rem`/`0.06rem` body values are proposed defaults. Mobile navigation behavior, hover/focus states, hero content, and footer structure were not observed and are marked as proposed throughout.
