---
version: alpha
name: "Fi"
source_url: "https://tryfi.com"
captured_at: "2026-09-28T09:36:37.622678+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fi's storefront CSS reflects a neutral, high-contrast UI system built on a
  Tailwind-derived gray scale — ink (#111827, confirmed via the body rule
  color:rgb(17 24 39)), body/mid grays (#374151, #6b7280, #9ca3af), hairlines
  (#e5e7eb, #d1d5db), and near-white surfaces (#f3f4f6, #f3f3f2) — set against
  a white canvas (#ffffff). Two saturated colors interrupt the neutral field:
  a bright yellow (#fffa01, with an alternate #ffff01) and an alert red
  (#e2133c). Given Fi's identity as a GPS/health-tracking collar brand and the
  recurrence of the yellow hex across two variants, it is treated here as the
  inferred primary accent for CTAs and highlight badges, while the red is
  reserved for alert/lost-mode states implied by copy such as "Search Party"
  and "Lost Mode." Typography is set in MessinaSans (var(--messina-sans)) with
  a full system-font fallback stack; the .text-h1 utility confirms a
  42px/700-weight/-0.06em display style, and .legacytext-body classes confirm
  17px and 14px body sizes directly in the stylesheet. A separate serif,
  Meursault Trial VF, appears only inside ".sbf-story-body h2" (blog content)
  and is treated as an editorial-only exception, not part of the core UI type
  system. Darker near-black tones (#101010, #1f2937) are inferred for
  footer/dark-section use. All role assignments beyond literal CSS
  declarations are labeled inferred below.

colors:
  primary: "#fffa01"
  ink: "#111827"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f3f4f6"
  surface-card: "#f3f3f2"
  on-primary: "#000000"
  alert: "#e2133c"
  border-strong: "#d1d5db"
  surface-dark: "#101010"
  ink-secondary: "#1f2937"
  accent-warm: "#968d88"
  placeholder: "#9ca3af"
typography:
  display-xl: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1, letterSpacing: -2.5px}
  display-md: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -1px}
  title-md: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.5px}
  body-md: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.375, letterSpacing: -0.025em}
  body-sm: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.375, letterSpacing: -0.025em}
  caption: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "MessinaSans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: -0.2px}
  editorial-serif: {fontFamily: "Meursault Trial VF, Georgia, Times New Roman, serif", fontSize: 28px, fontWeight: 400, lineHeight: 1.2, letterSpacing: -1.4px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    height: "74px-84px (observed --headerHeight custom property)"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    shadow: "proposed, subtle, not observed"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  weight-selector:
    backgroundColor: "{colors.canvas}"
    buttonBackground: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"

## Components

**button-primary** uses the inferred yellow accent (#fffa01) as its fill with black text for contrast, sized with the observed button-md scale; proposed for "Shop," "Try Fi for free," and other primary CTAs seen in the page copy.

**button-secondary** is a bordered, transparent-fill variant using the hairline gray border and ink text, proposed for secondary actions like "Learn more" alongside a primary CTA.

**text-input** draws on the soft surface gray and hairline border observed in the neutral palette; used for the footer email-capture field ("Enter email") referenced in the page text. States (focus, error) are proposed, not observed.

**nav-bar** is grounded directly in CSS: the `body` selector defines `--headerHeight` custom properties at two values (74px and 84px) alongside `--promoHeight` (72px/46px), strongly suggesting a responsive header plus a promo bar above it. Background and border are inferred from the canvas/hairline pair.

**product-card** applies the off-white surface (#f3f3f2) distinct from pure white canvas to separate product tiles (e.g., Series 3+ collar) from the page background; rounding and shadow are proposed defaults, not measured.

**hero** models the large marketing banner implied by "Meet the world's smartest dog collar" copy, using the confirmed 42px/700-weight `.text-h1` style as its headline typography on a white canvas; dark-mode hero variant is not confirmed.

**footer** is inferred to sit on the darkest observed surface (#101010) given the long list of footer-style links in the page text (About Us, Careers, Press, Blog, Support, Terms), with muted-gray secondary link text and white primary text.

**badge** uses the alert red (#e2133c) for status/urgency markers such as a "Lost Mode" or "Alert" pill, matching the Search Party/Lost Mode narrative in the copy; a secondary yellow badge variant is proposed for "Free Trial" callouts but not separately defined here.

**search** is a proposed pill-shaped input (full radius) reusing the text-input's color pairing, for a header search affordance; no search UI was directly observed in the supplied CSS.

**weight-selector** is grounded in an actual observed component, `.WeightSelector_weight___kLWS .WeightSelector_adjustButton___Cpbk`, a small square (2rem × 2rem) white, borderless, centered stepper button — evidently part of a dog-profile/collar-fit weight input flow. This is the category-appropriate component: a pet-profile numeric stepper used during onboarding/checkout to size the collar, styled here with canvas background, hairline border, and tight padding consistent with its compact observed dimensions.

## Responsive Behavior

This is a proposed recommendation, not measured site behavior; only the `--headerHeight`/`--promoHeight` custom-property shift (74px→84px header, 72px→46px promo) is directly evidenced, implying at least one responsive breakpoint.

| Breakpoint | Width | Header height | Notes |
|---|---|---|---|
| sm | 0–639px | 74px | Promo bar 72px; stacked nav, single-column hero/product grid |
| md | 640–1023px | 74px–84px | Two-column product grids proposed |
| lg | 1024–1279px | 84px | Promo bar 46px; multi-column layouts |
| xl | 1280px+ | 84px | Full desktop nav and 3–4 column grids |

Touch targets are proposed at a minimum 44×44px (the observed weight-selector buttons at 32×32px are below this and should be treated as a desktop-oriented control unless verified otherwise on mobile). Nav collapses to a hamburger/menu pattern below `md` per convention, not per observation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction states were observed. Role assignments — particularly `primary` (yellow), `alert` (red), `surface-dark`, and `ink-secondary` — are inferred from color saturation and copy context, not confirmed component usage. Several near-duplicate near-black and near-white hexes in the supplied palette (#151515, #3c3c3c, #f0f0f0, #f3f3f3, #e5e5e4, #ffff01) were omitted from the token set for restraint rather than mapped to speculative roles. Typography sizes for `display-md`, `title-md`, `caption`, and `button-md` are proposed scale extrapolations from the confirmed `.text-h1` and `.legacytext-body` rules, not directly observed classes. The MessinaSans and Meursault Trial VF font families are referenced via `@font-face`/CSS variables only; actual glyph rendering, weights available, and licensing/self-hosting terms were not verified. Mobile layout, hover/focus states, form validation styling, and the promo-bar/header collapse behavior implied by the `--headerHeight`/`--promoHeight` variables were not directly observed and are described only as inferred from custom-property evidence.
