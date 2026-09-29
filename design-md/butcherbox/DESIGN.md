---
version: alpha
name: "ButcherBox"
source_url: "https://butcherbox.com"
captured_at: "2026-09-28T04:33:36.316675+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The observed palette centers on a warm off-white canvas (#fbfaf9, #f3f0ec) paired with a saturated red (#b81504) that appears explicitly as a background-color paired with white text in the extracted CSS, supporting its role as the primary call-to-action color for a meat-focused meal kit brand. Text relies on a CSS custom property named --color-charcoal-green-800, which is inferred (not directly hex-confirmed) to correspond to the dark end of an adjacent neutral-green ramp (#f6f7f7 through #050a08); we map this to #1c2623 as the primary ink color. A secondary green ramp (#bfecdc to #00945f) and a gold tone (#dfa70f) are present but their exact usage is unobserved, so they are treated as inferred accent/badge candidates evoking freshness and quality claims common to prepared-meat marketing. A blue ramp (#1773b0, #1990c6, #136f99) appears tied to a Shopify accelerated-checkout widget rather than confirmed brand identity, so it is excluded from primary brand roles. Typography combines a condensed display face, Bebas Neue, for bold headline treatment with Lato for body copy and Poppins for intermediate UI labeling; all fallback to sans-serif. Layout, spacing, and interaction states below are proposed conventions for a meal-kit e-commerce experience, not measured site behavior.

colors:
  primary: "#b81504"
  ink: "#1c2623"
  canvas: "#fbfaf9"
  body: "#333333"
  muted: "#717070"
  hairline: "#dddddd"
  surface-soft: "#f3f0ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-red-soft: "#ffe6e3"
  surface-cream: "#fcf6dd"
  accent-gold: "#dfa70f"
  accent-green: "#00945f"
  accent-green-soft: "#bfecdc"
  charcoal-900: "#050a08"
  neutral-700: "#454b4a"
typography:
  display-xl: {fontFamily: "Bebas Neue, sans-serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.05, letterSpacing: 0.5px}
  display-md: {fontFamily: "Bebas Neue, sans-serif", fontSize: 34px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.5px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "0 2px 7px 0 rgba(0,0,0,0.15)"
  hero:
    backgroundColor: "{colors.charcoal-900}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.charcoal-900}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  tabbed-selector:
    backgroundColor: "{colors.surface-soft}"
    activeTabBackground: "{colors.surface-card}"
    activeTabText: "{colors.ink}"
    typography: "{typography.body-sm}"
    dividerColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    shadow: "0 2px 7px 0 rgba(0,0,0,0.15)"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** is proposed as the site's dominant conversion element (e.g., "Get Started," "Add Box"), grounded in the observed pairing of #b81504 background with white text found directly in the CSS. Its square corner treatment is inferred from a zero border-radius default seen on the checkout button.

**button-secondary** is a proposed outline-style variant for lower-emphasis actions such as "Learn More," using the card white surface with dark ink text and a hairline border; hover/focus states are not observed and are proposed only.

**text-input** represents form fields (email capture, address entry) using the light card surface and hairline border consistent with the neutral palette; focus-ring styling is not observed and is proposed.

**nav-bar** is inferred as a top-level navigation bar on the warm canvas background with dark ink labels; sticky behavior and mobile menu iconography were not observed in the supplied CSS.

**product-card** models individual meat/box product tiles, using the white surface, a subtle drop shadow value taken directly from the tabbed-products CSS (`0 2px 7px 0 rgba(0,0,0,0.15)`), and Poppins-based product titles.

**hero** is a proposed full-bleed banner pattern using the darkest charcoal tone for backgrounds and Bebas Neue for large display type, consistent with the brand's condensed headline face; actual hero imagery and copy were not observed.

**footer** reuses the charcoal-900 tone with light text for a grounded, dark closing section; column structure and link groupings are proposed, not extracted.

**badge** covers small inline labels (e.g., "Grass-Fed," "New") using the cream surface tone observed among the palette's warm off-whites, styled as a pill; this is an inferred rather than confirmed usage.

**tabbed-selector** directly reflects observed CSS for a tabbed-products component: an active tab receives a white background, dark ink text, and the same box-shadow as product cards, with hairline (#f3f0ec) dividers between tab labels — useful for meal-plan or cut-type category switching.

**search** is a proposed pill-shaped input pattern for product/recipe search, styled consistently with text-input but rounded fully; no search UI was present in the supplied evidence.

## Responsive Behavior
The following breakpoint table is a recommendation for implementation and is not derived from measured site behavior:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product/tab stacking, nav collapses to menu icon |
| Tablet | 480–1024px | Two-column product grids, tabbed-selector remains horizontal |
| Desktop | >1024px | Three-to-four column product grids, full horizontal nav |

Touch targets for button-primary/secondary and tabbed-selector items should maintain a minimum 44px tap height (proposed). Navigation and tab lists should collapse into a horizontally scrollable or accordion pattern below tablet width (proposed, not observed).

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS extraction and a fixed color/selector snapshot; no live rendering, computed styles, or interaction states (hover, focus, active, disabled) were observed beyond the two explicit `:hover` background-color rules captured for the Shopify payment button. The mapping of `--color-charcoal-green-800` to a specific hex value (#1c2623) is inferred from ramp position, not directly confirmed. Blue tones (#1773b0, #1990c6, #136f99, etc.) are likely tied to a third-party Shopify checkout widget rather than core brand identity, and their exclusion from primary roles is a judgment call. All font sizes, weights, spacing values, rounded-corner values, and the responsive breakpoint table are proposed conventions, not measured from the live site. Mobile navigation patterns, hero content, and footer structure were not present in the supplied evidence and are marked as proposed. Availability, licensing, and hosting terms for Bebas Neue, Lato, and Poppins were not verified.
