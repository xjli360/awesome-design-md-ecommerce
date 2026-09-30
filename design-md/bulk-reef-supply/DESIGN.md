---
version: alpha
name: "Bulk Reef Supply"
source_url: "https://bulkreefsupply.com"
captured_at: "2026-09-28T09:17:52.706384+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bulk Reef Supply's storefront evidence shows a Magento-based commerce theme built on a neutral gray-and-white foundation punctuated by a black pill-shaped call-to-action button. The primary interactive gesture observed is `.abs-action-addto-product`: a black (#000) background, white text, BebasNeuePro display font, and a 5rem border-radius producing a fully rounded pill — this is treated as the brand's primary button pattern. Link and tab-active states reveal a recurring blue family (#1979c3, #1790fa, #0069d9), inferred here as an accent/interactive color separate from the black CTA. Body and label text lean on grays (#333333, #7d7d7d, #111111) over white and near-white surfaces (#ffffff, #f0f0f0, #f8f8f8), with light hairline borders (#d1d1d1). Typography evidence includes BebasNeuePro (condensed display, used on the observed button), plus Poppins, Open Sans, Roboto, and Montserrat-bold in the broader font stack — mapped here as headline, body, and caption roles by inference, since no heading-specific CSS was supplied. Orange/red tones (#ee7017, #e02b27, #ff5a22) appear in the palette and are treated as inferred sale/alert accents given typical e-commerce deal-badge usage, not confirmed by rule context. Rounded corners, spacing, and most component layouts below are proposed conventions consistent with the observed pill-button radius and Magento-style tab/table patterns, not full-page measurements.

colors:
  primary: "#000000"
  accent: "#1979c3"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7d7d7d"
  hairline: "#d1d1d1"
  surface-soft: "#f0f0f0"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  border-strong: "#585959"
  sale: "#e02b27"
  deal: "#ee7017"
  link-hover: "#0069d9"
typography:
  display-xl: {fontFamily: "BebasNeuePro, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "BebasNeuePro, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 16px, letterSpacing: 0.5px}
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
    padding: "{spacing.lg} {spacing.xxl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hoverColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    borderBottom: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.deal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  reef-calculator-widget:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** mirrors the one concretely observed interactive pattern in the evidence: `.abs-action-addto-product`, a black-background, white-text, fully pill-shaped (5rem radius) button set in BebasNeuePro. This is used for "Add to Cart" actions and is treated as the canonical primary CTA across the storefront.

**button-secondary** is proposed (not directly observed) as an outlined counterpart for secondary actions like "Notify Me When In-Stock," using the same pill shape and button typography but with a white fill and dark border, consistent with the `#585959` border-hover state seen on the primary button.

**text-input** is a proposed pattern for search and account forms (email/password fields referenced in the page text). Rounded corners and hairline borders are inferred from the general gray-bordered aesthetic of tab/table elements rather than direct input CSS.

**nav-bar** represents the top-level "Menu" / account / cart bar referenced in page text (My Cart, My Account, Sign In). Colors and hover states are inferred from the observed blue link/active-state family, since no nav-specific selector was supplied.

**product-card** models the repeating "Add to Cart / Notify Me" product tiles seen in the page text (Sicce pumps, Flipper, Brightwell Aquatics, etc.). Card background and border are inferred from the light surface grays (#f8f8f8, #d1d1d1) present elsewhere in the CSS; no dedicated `.product-card` rule was supplied.

**hero** is a proposed banner treatment for homepage promotional content ("FREE SHIPPING," "Weekly Deals," "See What's New"), using the light gray surface tone and the display-xl BebasNeuePro headline style inferred from the button's font family.

**footer** reflects the extensive footer content (About Us, Customer Center, Resources, social links, address) visible in page text. A dark-on-light inversion is proposed since no footer-specific background color was present in the supplied CSS; ink (#111111) is used as a plausible dark footer background.

**badge** is proposed for sale/deal callouts such as the "$254.99 $299.99" strikethrough pricing pattern seen throughout the product listings, using the inferred deal-orange (#ee7017) accent color.

**search** models the expected header search field; styling is inferred from the general hairline-border, muted-text conventions observed in tab and table components, since no dedicated search selector was present.

**reef-calculator-widget** is a category-specific, fully proposed component addressing the "Rewards Calculator" and "Calculators" links referenced in the page text — a distinctly aquarium-hobbyist utility (e.g., dosing/mixing calculators) styled with the soft surface background and accent-blue highlights to differentiate it from standard commerce components.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not measured site behavior, since no media queries were included in the supplied evidence:

| Breakpoint | Width      | Layout notes (proposed)                          |
|-----------|------------|---------------------------------------------------|
| mobile    | <480px     | Single-column product grid, collapsed nav to menu icon |
| tablet    | 480–1024px | 2-column product grid, condensed nav bar          |
| desktop   | 1024–1440px| 3–4 column product grid, full nav bar visible     |
| wide      | >1440px    | Max-width container, 4+ column product grid       |

Touch targets for buttons and nav items should maintain a minimum 44×44px hit area, consistent with the pill button's generous `1.5rem 3rem` padding. Navigation should collapse to a hamburger/menu pattern below tablet width, matching the "Menu" label referenced in page text. All figures above are proposed conventions, not observed CSS breakpoints.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static, partial CSS extraction and page-text excerpt; no rendered layout, computed styles, or responsive behavior were directly observed. Color-to-role mappings (e.g., which blue serves as the primary accent versus a legacy/unused utility color, and whether orange/red tones function as sale badges) are inferred from typical e-commerce conventions, not confirmed by class-name context for every hex. Only one button pattern (`.abs-action-addto-product`) was concretely observed; button-secondary, text-input, nav-bar, hero, footer, badge, search, and the reef-calculator-widget are proposed extrapolations. Font availability, licensing, and correct loading of BebasNeuePro, Poppins, Open Sans, Roboto, and Montserrat were not verified — these are listed only because they appeared in the supplied `font_families` evidence. All spacing and typography sizes not directly present in the CSS (i.e., anything beyond the button's `2rem`/`1.6rem`/`5rem` and the tab's `1.8rem`/`40px`/`5px 20px`) are proposed values for internal consistency, not measurements. Mobile/touch interaction states (hover, focus, active beyond the two button pseudo-classes shown) were not observed.
