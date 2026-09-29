---
version: alpha
name: "Brightland"
source_url: "https://brightland.co"
captured_at: "2026-09-28T05:00:41.954127+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Brightland's public site surfaces a warm, editorial pantry-brand aesthetic built on a cream-and-ink foundation with a small set of saturated accent hues. Observed CSS shows a near-black button background (#0a0200) used consistently in the review-widget button tokens, alongside a neutral text-helper gray (#676986) and a soft cream surface (#f5f3ec) that likely serves as section backgrounds given the brand's "California harvest" positioning. A cluster of saturated accents — terracotta (#e9522e), marigold (#f68e00), cobalt (#0061a0), and plum (#a61f67) — appear in the palette and are inferred here as seasonal or badge accents (e.g. "Best Seller," "Almost Gone," sale pricing) rather than primary UI color, since no selector evidence ties them to core buttons or links.

  Typography evidence lists a serif family (Fraunces) alongside a rounded sans (CircularXXWeb) and several display-only faces (Advercase, Tilda, Fairplex-Medium, Sailing) that appear to be decorative/seasonal fonts rather than core UI type. This interpretation assigns Fraunces to display headlines and CircularXXWeb to body and UI text, reflecting the h0–h6 fluid type scale explicitly defined in :root. Rounded corners lean toward pill-shaped buttons (oke borderRadius:1000px), reused here as the primary button shape. Spacing values are proposed to match Shopify-theme spacing-scale conventions referenced by variable names, not measured pixel gaps.

colors:
  primary: "#0a0200"
  ink: "#1b1b1b"
  canvas: "#ffffff"
  body: "#1b1b1b"
  muted: "#676986"
  hairline: "#dddddd"
  surface-soft: "#f5f3ec"
  surface-card: "#f9f2ea"
  on-primary: "#ffffff"
  accent-terracotta: "#e9522e"
  accent-marigold: "#f68e00"
  accent-cobalt: "#0061a0"
  accent-plum: "#a61f67"
  accent-blush: "#f2d4d7"
  overlay-scrim: "#00000066"
typography:
  display-xl: {fontFamily: "Fraunces, serif", fontSize: 72px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Fraunces, serif", fontSize: 44px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "CircularXXWeb, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "CircularXXWeb, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "CircularXXWeb, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "CircularXXWeb, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "CircularXXWeb, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary** is proposed as the near-black (#0a0200) filled pill button, the only button background color directly evidenced (via the oke review-widget's `--oke-button-backgroundColor`), reused here for "Add to Bag" and primary CTAs.

**button-secondary** is a proposed outline variant, inferred from the theme's `.button--outline` hover rules which swap fill and outline colors on interaction — an observed *pattern*, though the resting-state colors are proposed.

**text-input** is a plain-bordered field using the hairline gray and canvas white; no dedicated input CSS was captured, so padding and radius are proposed conventions.

**nav-bar** reflects the site's flat header pattern (Shop, Best Sellers, Gifts, Login, Cart) implied by the extracted menu text; visual styling (height, sticky behavior) is not observed and is proposed.

**product-card** is inferred from repeated "Add to Bag / Subscribe & Save / Sale price" text blocks for products like Rosette Garlic Olive Oil, suggesting a repeating card grid; card background and radius are proposed.

**hero** corresponds to the "Hello, Cozy Season / Shop Fall Flavors" banner text, using the soft cream surface as an inferred full-bleed background; imagery and exact copy placement are not observed.

**footer** is inferred from the link list (Field Guides, Store Locator, Our Story, FAQ, Account Hub) and given a dark-ink treatment for contrast; this color choice is proposed, not confirmed by footer-specific CSS.

**badge** models the "Best Seller," "Almost Gone," and "Oprah's Favorite Things" labels seen in product text, assigned the marigold accent as a proposed, non-evidenced color choice for visual distinction.

**search** is a minimal pill-shaped input inferred from the header's "Search" link; no search-bar CSS was present in evidence.

**subscription-selector** is a category-appropriate component modeling the observed "Once Monthly / Every 2 Months / Every 3 Months / One-time Purchase" subscribe-and-save control found repeatedly in the page text; interactive/active states are proposed since only text content, not styling, was captured.

## Responsive Behavior
Recommended breakpoints (not measured from the live site): mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. The `:root` variables show a smaller type/spacing scale (e.g. h0: 3.5rem) shifting to a larger scale (h0: 4.5rem) at wider viewports, confirming *some* fluid scaling exists, though exact breakpoint widths were not captured. Nav is expected to collapse into a hamburger/drawer below tablet width; product grids likely reduce from multi-column to 1–2 columns on mobile. Touch targets for buttons and the subscription-selector should maintain a minimum 44×44px hit area. This section is a design recommendation, not an observed layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven interactions, or actual breakpoint pixel values were observed. Color-to-role mapping (e.g. which hex is "primary" vs. seasonal accent) is inferred from limited selector context, primarily the third-party review widget's variable names, and may not reflect the brand's actual core UI palette. Font availability, weights, and licensing for Fraunces, CircularXXWeb, Advercase, Tilda, Fairplex-Medium, and Sailing were not verified — some may be seasonal/limited-use assets rather than core UI fonts. Spacing and rounded-corner values follow common design-token conventions and are proposed, not measured, except where a specific pixel value (e.g. 1000px border-radius) appeared directly in evidence. No hover, focus, error, or mobile-menu states were observed; all interaction states listed above are proposed.
