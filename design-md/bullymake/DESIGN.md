---
version: alpha
name: "Bullymake"
source_url: "https://bullymake.com"
captured_at: "2026-09-29T04:01:53.757788+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bullymake's storefront runs on a Shopify/Bootstrap-derived stylesheet, giving a
  neutral utility layer (grays, form-control states, Bootstrap's default red/green/
  yellow status colors) beneath a bold, brand-specific display treatment. The clearest
  brand signal is condensed, heavy-weight display type — dharma-gothic-p for headings
  and alternate-gothic for buttons — paired with Arial-based fallbacks for body copy,
  consistent with a rugged, tough-chewer positioning. The observed accent orange
  (#ff6105) reads as the primary brand color given its prominence alongside the
  near-black #231f20 ink used in webkit tap-highlight and heading defaults. A soft
  teal (#5ec4a2) appears distinct enough from Bootstrap's utility palette to be
  treated as a secondary/accent color, inferred for use on "healthy," "safe," or
  guarantee-related callouts. A blue (#1990c6/#136f99 hover) is tied specifically to
  Shopify's unbranded accelerated-checkout button and is scoped to that component only.
  This interpretation proposes a card-and-badge system for subscription toy/treat
  selection, condensed display type for hero and section headers, and Bootstrap-derived
  border-radius/spacing defaults where no bespoke values were observed. Semantic role
  assignments (primary, muted, hairline) are inferred from usage context, not confirmed
  brand documentation.

colors:
  primary: "#ff6105"
  secondary: "#5ec4a2"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#4b4b4b"
  muted: "#7b7c80"
  hairline: "#dedede"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border: "#ced4da"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  success: "#198754"
  warning: "#ffc107"
  danger: "#dc3545"
typography:
  display-xl: {fontFamily: "dharma-gothic-p, Adjusted Arial Narrow Fallback, sans-serif", fontSize: 64px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "dharma-gothic-p, Adjusted Arial Narrow Fallback, sans-serif", fontSize: 40px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "dharma-gothic-p, Adjusted Arial Narrow Fallback, sans-serif", fontSize: 28px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "alternate-gothic, Arial, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-box-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"

## Components
**button-primary** is proposed as the main call-to-action treatment ("Join Now," "Subscribe Now," "Get Offer Now"), using the observed orange as background and the condensed alternate-gothic button typography seen in `.btn`. Hover/active states are proposed, not observed.

**button-secondary** offers an outlined alternative for lower-emphasis actions (e.g., "Learn More," "FAQ"), reusing ink for border/text since no distinct secondary-button CSS was supplied.

**text-input** covers account/newsletter/form fields. Border color and radius are inferred from Bootstrap `.form-control` conventions present in the stylesheet; no bespoke input styling was observed.

**nav-bar** is a light, canvas-backed header separated by a hairline, holding logo, "My Account," and menu links; sticky/scroll behavior is not confirmed by the evidence.

**product-card** represents individual toy-type tiles (Nylon, Rubber, Rope, Ballistic, Plush) as seen in the "Super Tough Toys + Treats" section — a bordered card with title, short description, and feature list, using surface-card and hairline border.

**hero** models the top banner ("Durable Dog Toys & Delicious Treats / First Box Only $19"), using a soft neutral background and the largest display type for the condensed headline treatment.

**footer** is proposed as a dark, ink-backed band for legal/contact links, contrasting with the light body; no footer-specific selectors were supplied, so styling is inferred from the ink/on-primary pairing.

**badge** covers small callouts like "Made in the USA," "FDA Food Grade Safe," or allergy-friendly labels, using the teal secondary color as a distinguishing but non-primary accent, fully pill-shaped.

**subscription-box-card** is a category-specific component modeling the core "what's in the box" customization unit — toy/treat bundle selection — combining a larger card radius, orange accent detailing, and prominent display typography to match the subscription-commerce nature of the product.

## Responsive Behavior
Recommended breakpoints, reused from the Bootstrap custom-property scale found in `:root` (`--bs-breakpoint-*`), which the theme appears to inherit rather than override:

| Breakpoint | Width   | Notes (proposed) |
|-----------|---------|-------------------|
| xs        | 0       | Single-column stacking, full-width buttons |
| sm        | 576px   | Two-column product/toy cards begin |
| md        | 768px   | Nav collapses to hamburger (proposed, not observed) |
| lg        | 992px   | Three/four-column card grids, full nav visible |
| xl        | 1200px  | Max-width content container |
| xxl       | 1400px  | Additional gutter, no new column count assumed |

Touch targets for buttons should meet a 44px minimum height, matching the `--shopify-accelerated-checkout-button-block-size` default of 44px seen in the checkout CSS. Mobile nav collapse, carousel swipe behavior, and card stacking order are recommendations only — none of this was confirmed via rendered/mobile capture.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS and text extraction only; no rendered screenshots, computed layout, or JavaScript-driven interaction states were observed. Color-to-role mapping (primary, secondary, muted, hairline) is inferred from usage context (e.g., checkout button colors, Bootstrap utility defaults) rather than confirmed brand guidelines, and some supplied hex values (Bootstrap status colors, Mastercard/Visa brand colors in payment icons) are excluded from role assignment as unrelated to Bullymake's own brand system. Font availability and licensing for `dharma-gothic-p`, `dharma-gothic-e`, and `alternate-gothic` were not verified — these are third-party/custom font names observed in CSS declarations only, with fallback stacks assumed from adjacent Arial/sans-serif references. All typography sizes beyond the confirmed `.btn` font-size (24px/700) are proposed, not measured. Breakpoints reflect Bootstrap defaults present in `:root` variables but actual responsive behavior (collapse points, column counts, touch interactions) was not observed on a live or mobile render. Border-radius values for buttons/cards are approximated against the observed `0.625rem` (10px) `.btn` radius using the nearest fixed scale step, not an exact match.
