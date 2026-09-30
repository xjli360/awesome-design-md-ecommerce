---
version: alpha
name: "Mobvoi"
source_url: "https://www.mobvoi.com"
captured_at: "2026-09-29T04:18:12.764269+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from CSS rules and a page-text excerpt captured from mobvoi.com/us, the brand's own storefront for TicWatch smartwatches, TicNote, and related wearables/smart-life gear. The observed palette is a neutral, tech-forward set: pure white canvas, near-black body text, two blues (#0091ff used on a subscribe CTA, #3487dc used on a header buy button), a legacy hyperlink blue (#0000ee), warm dark charcoal tones (#232427, #3e3a39) likely used for dark header/footer surfaces, mid grays (#999999, #767676) for secondary text and hairlines, and two reds (#ff5c5c, #f23434) that plausibly mark sale/discount badges given the "0% APR" and "2% off" promotional copy. Typography relies on a custom sfText family (Regular/Bold) with SFProText and CJK fallbacks (Microsoft JhengHei/YaHei, SimHei, WenQuanYi Micro Hei), confirming an international, Latin+CJK-ready stack rather than a distinctive brand typeface. Several sizes in the CSS use rem units consistent with a mobile flexible-root scaling pattern (assumed ~100px root); those pixel equivalents are treated as inferred. The proposed system favors compact pill buttons, thin borders over heavy shadows, and a product-grid, review-quote, and blog-card layout matching the page's "BEST-SELLERS," "curated gears," and press-quote content.

colors:
  primary: "#0091ff"
  primary-alt: "#3487dc"
  ink: "#000000"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#999999"
  hairline: "#767676"
  surface-soft: "#3e3a39"
  surface-card: "#232427"
  on-primary: "#ffffff"
  accent-sale: "#ff5c5c"
  accent-sale-strong: "#f23434"
  link: "#0000ee"
typography:
  display-xl: {fontFamily: "sfTextBold, SFProText-Bold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "sfTextBold, SFProText-Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "sfTextBold, SFProText-Bold, \"Microsoft JhengHei\", sans-serif", fontSize: 21px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "sfTextRegular, SFProText, \"Microsoft YaHei\", SimHei, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "sfTextRegular, SFProText, \"Microsoft YaHei\", sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "sfTextRegular, SFProText, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "sfTextBold, SFProText-Bold, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.7, letterSpacing: 0.2px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-secondary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  spec-highlight:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components
**button-primary** renders the main add-to-cart/subscribe actions in the observed `#0091ff` blue with white text, matching the `.subscribe button` rule; a fully rounded pill shape is proposed for consistency with the header's rounded buy button. **button-secondary** is a transparent, white-bordered outline button, directly reflecting `.index-banner-img .btn-more`'s `border:1px solid #fff` pattern for hero overlays on imagery. **text-input** is a proposed neutral field using the hairline gray border since no form-field CSS was supplied. **nav-bar** is inferred as a white top bar with black text and a dropdown "site-select-icon," consistent with `.header .site-map .site-select-icon{color:#000}`. **product-card** is a proposed white card with an 8px radius for the "BEST-SELLERS"/"HOME GYM" grid sections referenced in the page text; no card CSS was directly observed. **hero** proposes a dark charcoal (`surface-soft`) banner section with large display type and an outline CTA, mirroring the banner button pattern. **footer** uses the darkest charcoal (`surface-card`) with muted gray body text and white links, inferred from the long footer link list (Warranty, Privacy policy, Store map) and the two dark near-black tones present in the palette. **badge** is a small rounded label in the stronger red (`#f23434`) for sale/refurbished callouts, supporting "Top Deals" and "Refurbished Products" navigation items; this color-to-role mapping is inferred, not confirmed by badge-specific CSS. **search** is a proposed pill-shaped input for the product catalog, unobserved directly. **spec-highlight** is a wearables-specific proposed component for battery-life/dual-screen feature callouts (e.g., "628mAh," "dual-screen") seen in the press-quote copy, styled on the dark card surface with primary-blue accents to draw attention to technical specs.

## Responsive Behavior
This is a recommendation, not measured site behavior, since no media queries were supplied.

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column product grid; nav collapses to a menu icon; hero CTA stacks below title. |
| tablet | 600–1024px | Two-column product grid; nav-bar shows condensed top-level items only. |
| desktop | >1024px | Multi-column ("BEST-SELLERS," "SMARTLIFE") grids; full nav with "Products/Community/Supports/About/Offers/Platform" dropdowns visible. |

Touch targets are recommended at a minimum 44×44px for buy buttons and nav dropdown triggers. The `.header-buy-btn`'s 26px height is below this threshold and should be enlarged for touch contexts in this proposal.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS rules, a title tag, and a page-text excerpt; no live rendering, computed layout, or interaction states (hover/focus/active, dropdown open states, cart drawer behavior) were observed. Several role assignments — surface-soft/surface-card as dark section backgrounds, accent-sale colors as badge colors, and hairline as border gray — are inferred from limited, indirect evidence and may not match actual usage. Font sizes derived from rem values (e.g., 0.21rem, 0.18rem) assume a mobile flexible-root scaling convention that was not directly confirmed. All typography sizes other than the 15px button rule are proposed, not measured. Mobile/responsive breakpoints and collapse patterns are recommendations only. Custom font availability, licensing, and whether "sfTextRegular/sfTextBold" are proprietary, licensed, or self-hosted assets was not verified.
