---
version: alpha
name: "Sugar Percussion"
source_url: "https://www.sugarpercussion.com"
captured_at: "2026-09-28T09:02:55.231446+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sugar Percussion is a small-batch solid-wood drum maker built on a Shopify
  storefront (theme base.css v10) with Lato as the sole observed typeface,
  rendered with antialiased smoothing across body and heading tags via CSS
  custom properties (--font-paragraph--family, --font-h1..h6--family). The
  supplied palette is neutral and print-adjacent: near-black text (#000000,
  #1a1a1a, #333333) on white/off-white surfaces (#ffffff, #fafafa, #f5f5f5,
  #f4f4f4), with a warm cream (#fff5e7) explicitly named as
  --color-submenu, suited to menu and card surfaces. A small set of
  saturated colors appear (#8b0000 dark red, #660000 deep maroon, #006400
  green, #ee9441 amber, #1990c6/#1d3686 blues, #3ed660 bright green) without
  confirmed roles in the evidence; this interpretation assigns the deep red
  as the primary accent (inferred, echoing the brand's craft/workshop tone)
  and treats the blues and greens as unused/status-reserve colors rather
  than core UI. Hairlines and borders draw from the observed grays
  (#dedede, #dfdfdf, #c8c8c8). Spacing values of 16px and 24px are evidenced
  in product-grid card padding/gap; all other spacing, radii, and font
  sizes beyond the one observed 0.875rem menu token are proposed defaults
  for a utilitarian, workshop-craft storefront.

colors:
  primary: "#8b0000"
  primary-deep: "#660000"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#888888"
  hairline: "#dedede"
  hairline-strong: "#c8c8c8"
  surface-soft: "#f5f5f5"
  surface-card: "#fff5e7"
  surface-alt: "#fafafa"
  on-primary: "#ffffff"
  accent-amber: "#ee9441"
  accent-green: "#006400"
  accent-blue: "#1990c6"
typography:
  display-xl: {fontFamily: "Lato, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lato, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Lato, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
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
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    gap: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-callout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
    borderColor: "{colors.primary-deep}"

## Components

**button-primary** is the checkout/add-to-cart call-to-action, using the inferred deep-red accent against white text; hover/active states are not observed and are proposed as a modest opacity or shade shift consistent with the theme's `--hover-*` custom properties present in base.css.

**button-secondary** serves outline actions (e.g., "View all," filters) with a transparent fill and hairline border, keeping the palette restrained; focus and disabled states are proposed, not measured.

**text-input** covers search and account/login fields, using a light hairline border on white, matching the neutral, print-shop aesthetic implied by the palette.

**nav-bar** reflects the header structure evidenced in the text excerpt (About, Gallery, Snares, Kits, Merch, YouTube, Workshops, Contact, region/currency selector, search, cart) on a white background with dark ink text; sticky/collapse behavior is proposed, not confirmed in the CSS.

**product-card** models the Shopify `product-grid__card` class, using the evidenced 16px gap and 24px block padding; the cream surface color is inferred from the explicitly named `--color-submenu` token as a warm, craft-shop card background, though its confirmed use is menu/submenu, not cards.

**hero** is proposed for the homepage video/banner area (evidence shows an autoplaying muted video block with mute/unmute controls); dark background with white display type is inferred to suit workshop/product photography, not confirmed by CSS.

**footer** is proposed as a light, muted-text band typical of Shopify themes; no footer-specific selectors were present in evidence.

**badge** is proposed for stock/availability or "handmade" labels using the amber accent color, which appears in the palette without a confirmed role; treat as decorative/status accent only.

**search** covers the predictive search drawer referenced in the page text ("Search Search Clear Products…"), styled as a soft-surface input consistent with the input pattern above.

**spec-callout** is a category-specific component proposed for drum specification panels (shell wood, size, hardware) on custom-shop or snare product pages, using the cream surface with a deep-red border accent to echo the brand's craftsman framing; not present in the supplied CSS evidence.

## Responsive Behavior

Recommended breakpoints (proposed, not measured): mobile ≤599px, tablet 600–899px, desktop 900–1279px, wide ≥1280px. Navigation is expected to collapse to a hamburger/drawer pattern below tablet width, consistent with common Shopify theme conventions, though no media queries were included in the supplied evidence. Touch targets for buttons and nav items should maintain a minimum 44×44px hit area. Product grids likely reflow from the desktop `zoom-out` multi-column layout (evidenced `repeat(10, …)` grid-template) down to 2 columns on tablet and 1–2 on mobile; exact column counts at each breakpoint are inferred, not confirmed. This section is a recommendation only and does not reflect observed responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom-property names, a partial rule set, and page text — no rendered layout, computed styles, or interaction states were observed. Font sizes, weights, and line-heights are proposed defaults except the single evidenced `0.875rem` menu-localization token; no other numeric type scale was present in the supplied CSS. Color role assignments (primary, accent-amber, accent-green, accent-blue) are inferred from a flat palette list without confirmed selector usage, apart from `--color-submenu: #fff5e7`, which is explicitly named. Border radii are proposed; no `border-radius` values appeared in evidence. Hover, focus, active, and disabled states referenced in components are proposed based on generic `--hover-*` variables in base.css, not verified visually. Mobile/tablet layout, navigation collapse behavior, and touch interactions were not observed. Lato's licensing and self-hosting/Google Fonts delivery were not verified from the supplied evidence.
