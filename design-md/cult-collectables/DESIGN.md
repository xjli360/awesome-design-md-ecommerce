---
version: alpha
name: "Cult Collectables"
source_url: "https://cultcollectables.com"
captured_at: "2026-09-28T04:13:21.697028+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cult Collectables presents a high-contrast, collector-focused retail interface built on a black-and-white foundation. The observed palette is dominated by pure black (#000000) and white (#ffffff), with grayscale steps (#eeeeee, #dddddd, #cccccc, #666666, #333333) used for borders, muted text, and surface layering. A small set of saturated accents (#108474 teal, #ee0000 red, #008a00 green, #fbcd0a yellow) appear alongside payment-icon and social-brand colors (#3b5998, #1da1f2, #eb001b, #f79e1b) that are treated here as third-party marks rather than brand colors. Typography evidence shows Baskerville (a classic serif) alongside Nunito Sans and system fallbacks (Arial, Helvetica); JudgemeIcons/JudgemeStar are review-widget icon fonts, not applied to body or heading text.

  This interpretation proposes Baskerville for display headings to give the "cult"/collector branding a distinctive, slightly editorial character, paired with Nunito Sans for body copy and UI text, reflecting the two families most plausibly tied to readable content rather than plugin icons. Buttons, badges, and reviews reuse the black/white pairing observed in CSS custom properties (--jdgm-primary-color: #000, --shopify-chat-accent-bg-color: #000000). Rounded corners are treated as minimal/proposed since Judge.me evidence shows --jdgm-border-radius: 0. All semantic role assignments (primary, ink, muted, hairline) are inferred from usage context, not confirmed brand guidelines.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-light: "#eeeeee"
  border-mid: "#cccccc"
  overlay: "#0000004d"
  accent-teal: "#108474"
  danger: "#ee0000"
  success: "#008a00"
  badge-yellow: "#fbcd0a"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: "proposed, not measured"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay}"
    titleTypography: "{typography.display-xl}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** reflects the observed `--jdgm-write-review-bg-color: #000000` / white-text pairing used for primary calls to action such as "Add to Cart" or review submission; hover/active states are proposed and not confirmed in the static CSS.

**button-secondary** is an inferred outline variant for lower-priority actions (e.g., "View Details"), reusing the same black ink on a white canvas with a hairline border rather than a filled background.

**text-input** covers search and form fields; the hairline border and near-black text color are drawn from the `.search-bar__filter select { color: black }` rule, with padding and radius proposed for touch usability.

**nav-bar** is modeled on the header CSS forcing `color: #ffffff !important` across menu items, implying a dark (black) header bar with white navigation text; sticky behavior is suggested by the `--header-is-sticky: 1` custom property, though exact scroll behavior is not observed.

**product-card** is a proposed pattern for the Funko Pop grid, using a white surface, light hairline border, and the `product-item__action-button` black-on-white/white-on-black button color rules observed in the CSS for its embedded action button.

**hero** is an inferred banner pattern based on `#block-slide-1 .button { color:#000000; background:#ffffff }`, suggesting a dark hero image with a light, contrasting call-to-action button; exact imagery and copy are not part of the CSS evidence.

**footer** is proposed as a dark, black-background band echoing the header's ink/white treatment, intended to house payment-method icons (Amex, PayPal, Klarna, etc.) referenced in the page title/evidence text.

**badge** is proposed for "Rare," "Grail," or "Exclusive" labels implied by the site title copy, using the observed yellow accent (#fbcd0a) as a distinguishing but unconfirmed brand marker.

**search-bar** reflects the `.header__search-bar-wrapper` and `.search-bar__results` rules forcing black text, implying a light-background search overlay with dark result text, layered on the surface-soft tone.

## Responsive Behavior
This is a proposed, non-measured breakpoint recommendation, not an observation of live site behavior:

| Breakpoint | Width      | Notes                                      |
|-----------|-----------|---------------------------------------------|
| mobile    | <600px    | single-column product grid, collapsed nav to hamburger menu |
| tablet    | 600–991px | 2-column product grid, inline search icon    |
| desktop   | 992–1279px| inline nav menu (`--header-inline-navigation: 1` observed), 3–4 column grid |
| wide      | ≥1280px   | max-content width, 4+ column grid            |

Touch targets should be at least 44x44px for cart/search icons; the header's forced white text on black background should maintain sufficient contrast when collapsed into a mobile drawer. Sticky header behavior is suggested by CSS variables but its exact scroll offset and animation are not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- This document is derived from static CSS/custom-property extraction only; no live rendering, computed layout, or DOM screenshots were available.
- Semantic role mapping (e.g., which black value serves as "primary" vs. "ink") is inferred from repeated usage patterns, not from a documented design system.
- Component states (hover, focus, disabled, loading) are proposed conventions, not verified interactions.
- Mobile/responsive layout, menu collapse behavior, and touch interactions are not observed; the breakpoint table above is a recommendation only.
- Font availability, licensing, and exact weights for Baskerville and Nunito Sans are not verified beyond their appearance in the supplied `font_families` list; JudgemeIcons/JudgemeStar are excluded from text roles as they are icon fonts.
- Numeric type scale, spacing, and radius values beyond the Judge.me `--jdgm-border-radius: 0` are proposed defaults, not measured from the site.
