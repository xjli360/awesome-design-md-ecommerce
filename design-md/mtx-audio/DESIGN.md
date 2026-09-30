---
version: alpha
name: "MTX Audio"
source_url: "https://mtx.com"
captured_at: "2026-09-28T10:02:30.043330+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from MTX's supplied CSS fragments (jQuery UI theme assets and a Slider Revolution hero-caption module) plus a broad observed color and font palette. The clearest brand signal is a saturated red pair (#ed1b2e, #ec1b2d) proposed here as primary and primary-alt, paired with near-black surfaces (#111111, #292e31) consistent with a performance-audio, dark-UI aesthetic. Raleway is the only font family tied to actual component rules (hero title, subtitle, content, and menu-item captions), so it anchors display and button typography; Arial/Helvetica, evidenced in jQuery UI form widgets, is used for utilitarian body and input text. Numerous other font families (Oswald, Roboto Condensed, Open Sans, Lato, Playfair Display, etc.) appear in the supplied font list but have no attached selector, so they are treated as available-but-unconfirmed and excluded from active roles.

  Semantic color mapping (ink, muted, hairline, surface tokens) is inferred from generic UI-state grays since no page-body selectors were supplied. Yellow (#ffd658), blue (#0096ff), and green (#8bc027) are proposed as accent, link, and success roles respectively based on typical usage of such tones, not confirmed placement. Layout, spacing, and radii are proposed conventions, not measured.

colors:
  primary: "#ed1b2e"
  primary-alt: "#ec1b2d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent: "#ffd658"
  link: "#0096ff"
  success: "#8bc027"
  warning: "#f39c12"
typography:
  display-xl: {fontFamily: "Raleway, sans-serif", fontSize: 90px, fontWeight: 100, lineHeight: 1.0, letterSpacing: 0px}
  display-md: {fontFamily: "Raleway, sans-serif", fontSize: 40px, fontWeight: 300, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Raleway, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Raleway, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Raleway, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.33, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Raleway, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1.33, letterSpacing: 2px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    hoverBackgroundColor: "{colors.canvas}"
    hoverTextColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    titleColor: "{colors.body}"
    titleTypography: "{typography.display-xl}"
    subtitleColor: "{colors.muted}"
    subtitleTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  power-rating-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the red primary color observed in the palette (#ed1b2e) with white text, intended for high-commitment actions like "Add to Cart" or "Shop Now." The wide letter-spacing button typography is drawn directly from the observed `WebProduct-Menuitem` caption rule.

**button-secondary** proposes an outlined variant sharing the same typography, for lower-emphasis actions (e.g., "Learn More") sitting beside a primary button. Its bordered, transparent-fill treatment is inferred, not observed.

**text-input** is modeled on generic form conventions since no dedicated input selectors were supplied beyond jQuery UI widget resets; hairline borders and muted placeholder text are proposed defaults appropriate to a dark-accented commerce site.

**nav-bar** directly reflects the observed `WebProduct-Menuitem` and its `:hover` rule: a dark background with white text that inverts to a light background with muted-gray text on hover. This is one of the few components with a confirmed interaction state in the supplied CSS.

**product-card** is a proposed container for subwoofers, amplifiers, and speaker listings, using a light card surface, hairline border, and title/price typography pairing. No card-specific selectors were present in the evidence, so structure and elevation are inferred from category norms.

**hero** interprets the Slider Revolution caption classes as a large display headline (90px, weight 100) over a subtitle and content line. Notably the observed title color (#333333) is dark, implying hero captions may sit on lighter imagery panels rather than solid dark backgrounds; this is flagged as an inferred layout assumption.

**footer** is proposed as a dark, muted-text band echoing the nav-bar's ink background, appropriate for the newsletter signup and legal-link footer content referenced in the page text.

**badge** and **power-rating-badge** are category-appropriate additions: the generic badge (accent yellow) suits promotional or "New" labels, while the power-rating-badge (primary red) is tailored to car-audio merchandising conventions seen in the source text (e.g., "500-Watt RMS," "1000-Watt RMS" callouts on product tiles).

**search** proposes a soft-surface input field with a muted icon, consistent with header search patterns common to multi-category audio catalogs (Mobile, Powersports, Marine, In Home) implied by the site's navigation structure.

## Responsive Behavior

This is a recommendation, not measured site behavior, since no media queries or breakpoint-specific rules were supplied.

| Breakpoint | Width        | Notes (proposed) |
|-----------|--------------|-------------------|
| mobile    | <480px       | Single-column product grid; nav collapses to hamburger/off-canvas menu |
| tablet    | 480–1024px   | Two-column product grid; condensed mega-menu |
| desktop   | 1024–1440px  | Full mega-navigation with category flyouts (Mobile, Powersports, Marine, In Home) |
| wide      | >1440px      | Increased hero and section padding using `{spacing.section}` |

Touch targets should be a minimum 44px height for nav and buttons; the mega-menu structure implied by the page text (deeply nested category lists) suggests an accordion pattern on mobile is advisable, though not confirmed by any supplied mobile CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static, partial CSS extraction (a jQuery UI theme file and a slider-caption plugin) rather than the site's primary stylesheet, so core layout, grid, and component-level rules for navigation, product cards, and forms are not directly observed and are marked as proposed. Semantic role assignments for grays (ink, muted, hairline, surface tokens) are inferred from generic UI-state colors, not confirmed brand tokens. Font usage outside Raleway and Arial/Helvetica (e.g., Oswald, Roboto Condensed, Open Sans, Lato) appears only in a supplied font-family list without attached selectors, so their actual application, licensing, and availability are unverified. No interaction states beyond the nav hover and jQuery UI widget states were observed; mobile layout, breakpoint values, and touch behavior were not measured and are presented purely as recommendations.
