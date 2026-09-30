---
version: alpha
name: "Kanile'a Ukulele"
source_url: "https://www.kanileaukulele.com"
captured_at: "2026-09-28T04:09:32.666065+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from Kanile'a Ukulele's Shopify theme CSS: a warm, low-contrast neutral palette (near-black #232323 and #413f3f/#423f3f charcoal text on white canvas), pill-shaped swiper controls, and squared, minimally-rounded buttons (--btn-border-radius: 4px). Typography is set entirely in Cabin with generic sans-serif fallback for body copy and bold headings; Jost appears in the site's font stack but no selector ties it to a specific role in the supplied evidence, so any display use of Jost here is inferred, not confirmed.

  The system favors restrained, editorial staging appropriate to a handmade-instrument brand: plenty of white space, charcoal ink instead of pure black, and small saturated accents (sale red #e32c2b, preorder green #60a57e, new-badge mauve #b79987) reserved for status labels rather than primary UI. A soft blue (#1f61cc) exists in the palette; it is treated here only as an inferred focus/link accent since no rule in the evidence assigns it a role. Buttons invert on hover (dark-to-white) per the observed :hover rule, and product carousels use circular white controls with a charcoal hover state. Card and section backgrounds draw from near-white neutrals (#f8f8f8, #eeeeee) to create subtle depth without introducing new colors. All semantic labels below (ink, muted, hairline, surface-soft/card) are inferred groupings of the observed hex values, not names found in the source CSS.

colors:
  primary: "#232323"
  ink: "#413f3f"
  canvas: "#ffffff"
  body: "#423f3f"
  muted: "#908e8e"
  hairline: "#e3e2e2"
  surface-soft: "#f8f8f8"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-sale: "#e32c2b"
  accent-preorder: "#60a57e"
  accent-new: "#b79987"
  focus-ring: "#1f61cc"
  overlay: "#00000080"
  shadow-soft: "#0000001a"
  divider-strong: "#423f3f40"
  carousel-control-icon: "#757575"
typography:
  display-xl: {fontFamily: "Cabin, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Cabin, sans-serif", fontSize: "36px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Cabin, sans-serif", fontSize: "22px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Cabin, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Cabin, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Cabin, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Cabin, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.25, letterSpacing: "0.3px"}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "{colors.shadow-soft}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "transparent"
    textColor: "{colors.accent-sale}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  product-media-carousel:
    controlBackground: "{colors.canvas}"
    controlIconColor: "{colors.carousel-control-icon}"
    controlIconHoverColor: "{colors.ink}"
    controlSize: "44px"
    rounded: "{rounded.full}"

## Components

**button-primary** reflects the observed `button,input[type=submit],.button` rule directly: a solid `#232323` fill with white text, 18px/30px padding, and a `.3s` transition on background/color/opacity/border/transform. Hover state (proposed to persist the observed inverse rule) swaps to white background with charcoal text and border.

**button-secondary** mirrors the observed `.button.alt` variant — white background, charcoal border and text — used for lower-emphasis actions like "Learn More" or secondary catalog filters. Its hover state is proposed to invert back to the primary treatment, consistent with the site's toggle pattern between the two button rules.

**text-input** is inferred from general form conventions; no explicit input-field border/background rule was present in the supplied evidence, so hairline border and white background are proposed defaults consistent with the site's neutral palette.

**nav-bar** is proposed as a slim, white header using the `--nav-height` custom property observed in `:root` (currently `0`, suggesting a dynamically-set or overlay nav not captured statically). Link color and border are inferred from the ink/hairline tokens.

**product-card** uses the near-white `#eeeeee` surface token to lift product tiles slightly off the pure-white canvas, paired with the observed sale/preorder/new-badge label colors for stock-status flags. Card radius reuses the site's 4px button radius for visual consistency; this pairing is proposed, not confirmed by a card-specific rule.

**hero** is a full-bleed, centered layout inferred from the `--viewport-height-first-section: 100vh` custom property, implying an above-the-fold section sized to the viewport. Headline styling reuses the bold, centered heading rule (`h1:not(.logo-h1),h2,h3...{text-align:center}`).

**footer** adopts the soft off-white surface and muted text color as a proposed low-contrast footer treatment; no footer-specific selector was present besides `.footer-button-xs`, a fixed-position mobile action bar with white background and a `.3s` cubic-bezier slide transition — that sticky mobile CTA affordance is directly observed.

**badge** encodes the three product-label states found in the CSS (`sale`, `preorder`, `product-label--new`, `unavailable`), each transparent-background with a distinct text color, matching the site's minimal, text-forward status-flag style.

**search** is proposed as a pill-shaped input (full radius) consistent with the circular swiper controls elsewhere in the theme, though no search-bar-specific rule was supplied.

**product-media-carousel** is directly grounded in the `.swiper-button-prev,.swiper-button-next` rule: 44px circular white controls with `#757575` icon color, transitioning to black icon on hover/focus — a strong, observed pattern for product image galleries and testimonial sliders.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not measured site behavior (no media queries were included in the supplied evidence):

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | up to 599px | Single-column stacking; sticky `.footer-button-xs`-style CTA bar retained at viewport bottom (observed pattern, generalized). |
| Tablet | 600–1023px | Two-column product grids; nav may collapse to a toggle menu (proposed). |
| Desktop | 1024px+ | Multi-column grids, full nav bar, hero at `100vh` per observed custom property. |

Touch targets should be at minimum 44×44px, matching the observed swiper control size. Primary/secondary buttons' 18px/30px padding comfortably exceeds this on desktop; mobile padding may need reduction (proposed, unmeasured). Navigation collapse into a hamburger/drawer pattern below tablet width is a standard proposal, not confirmed by supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS extraction only; no rendered page, interaction states, or actual mobile layout were observed.
- Semantic role names (ink, muted, hairline, surface-soft/card, focus-ring) are inferred groupings of raw hex values; the source CSS does not label them as such.
- Heading, display, and caption font sizes are proposed defaults — only the 16px/400-weight/1.5-line-height body style and the 700-weight heading rule were directly observed.
- The `#1f61cc` blue and several near-transparent grays (`#423f3f0d`, `#00000005`, etc.) appear in the palette but have no selector tying them to a specific UI role; their inclusion as focus-ring/shadow tokens is speculative.
- Jost is listed in the site's font stack but no supplied selector assigns it to any element; its potential display/heading use is unconfirmed.
- Font licensing and self-hosting/CDN availability for Cabin and Jost were not verified.
- `--nav-height: 0` and `--viewport-height-first-section: 100vh` suggest dynamic/JS-driven layout behavior that cannot be fully reconstructed from static rules.
