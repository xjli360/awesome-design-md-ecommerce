---
version: alpha
name: "Knack Bags"
source_url: "https://knackbags.com/"
captured_at: "2026-09-29T04:15:44.369194+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Knack's storefront runs on a Shopify Dawn-derived theme, evidenced by the
  base.css custom-property system (--color-base-*, --duration-*) and a
  header block exposing explicit RGB tokens. The header's own CSS sets its
  border and highlight color to #f0ab00 (amber/gold), which is treated here
  as the primary brand accent since it is the only color explicitly wired
  to a highlight role in the supplied evidence. Header background is white
  (#ffffff) with a dark neutral foreground (#282828), and body text runs at
  a comfortable 1.5rem base with generous 0.06rem letter-spacing, consistent
  with a travel/EDC brand favoring airy, uppercase-leaning navigation labels.
  A secondary interactive blue (#1990c6, hover #136f99) appears in the
  Shopify accelerated-checkout button styles and is repurposed here as a
  utility action color (e.g., secondary CTAs, wallet buttons) rather than
  the primary brand color, since it originates from a platform component,
  not brand-specific CSS. Warm off-white neutrals (#f5f3f1, #dad5c5) are
  inferred as soft surface tones echoing product colorway names like
  "Oatmilk." Typography favors Work Sans for UI/body and Lora as an
  available serif for editorial or heading moments; role assignments beyond
  the header tokens are inferred, not measured.

colors:
  primary: "#f0ab00"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#282828"
  muted: "#8e8d92"
  hairline: "#dddddd"
  surface-soft: "#f5f3f1"
  surface-card: "#f7f7f8"
  on-primary: "#231f20"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  surface-warm: "#dad5c5"
  surface-dark: "#1c1c1c"
  sale: "#d72c0d"
  success: "#008060"
  link: "#0000ee"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Lora, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.3px"}
  title-md: {fontFamily: "Work Sans, Helvetica Neue, Arial, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Work Sans, Helvetica Neue, Arial, sans-serif", fontSize: "18px", fontWeight: 400, lineHeight: 1.53, letterSpacing: "0.9px"}
  body-sm: {fontFamily: "Work Sans, Helvetica Neue, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.5px"}
  caption: {fontFamily: "Work Sans, Helvetica Neue, Arial, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Work Sans, Helvetica Neue, Arial, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "1px"}
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
    textColor: "{colors.accent-blue}"
    borderColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.primary}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  review-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the amber highlight (`#f0ab00`) observed in the header's `--color-highlight` token as its fill, with dark ink text for contrast; proposed for primary CTAs like "Add to Cart" and "Find Your Perfect Bag." **button-secondary** repurposes the Shopify accelerated-checkout blue (`#1990c6`) as an outline/utility action style, distinct from the brand accent so wallet-style buttons remain visually separate. **text-input** is a minimal bordered field using the hairline gray, proposed for newsletter signup and search, matching the theme's understated form conventions. **nav-bar** sits on white with dark foreground text and an amber bottom accent, mirroring the header's own CSS variables exactly (background rgb 255,255,255; foreground rgb 40,40,40; border rgb 240,171,0). **product-card** groups bag imagery, title, and price on a light card surface, proposed to hold the repeated pattern of product name → price → colorway swatches seen across Series 1/2 packs. **color-swatch-selector** is a category-specific component modeling the repeated colorway pickers (Alloy Gray, Midnight Black, Steel Blue, Oatmilk, etc.), rendered as small circular swatches with an amber active-state ring. **hero** proposes a warm-neutral banner background for statement copy like "YOU'RE ABOUT TO GO PLACES," using serif display type for editorial weight. **footer** uses a near-black surface with white text for the multi-column SHOP/COMPANY/SUPPORT link groups and social icons. **badge** models "NEW" and sale-style labels using the Shopify-default red, proposed as an inferred semantic role since it is not confirmed as brand-authored. **review-card** structures the "WHAT KNACKPACKERS ARE SAYING" testimonial blocks with quote and attribution typography tiers. **search** proposes a pill-shaped field for site search, unobserved in markup but consistent with the theme's rounded, minimal aesthetic.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Layout guidance |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, swatch selector wraps to 2 rows |
| Tablet | 600–989px | 2-column product grid, nav-bar links may condense into a "SHOP" dropdown |
| Desktop | ≥990px | Full horizontal nav (SHOP BAGS / ACCESSORIES / CORPORATE GIFTS / ABOUT), 3–4 column product grid |

Touch targets for swatches and buttons should be at least 40–44px. Nav collapse threshold is proposed, not confirmed by observed markup or JS behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, open menus, cart drawer) were observed. Color-to-role mapping beyond the header's explicit `--color-header-*` and `--color-highlight` variables (amber `#f0ab00`) is inferred, including the choice of `#1990c6` as a secondary/utility rather than primary accent. Several palette entries (`#eb001b`, `#f79e1b`, `#ff5f00`, `#0071ce`, `#ffcc4b`, `#ffe431`, `#142fbd`, `#1532cb`) closely match third-party payment-brand icon colors (e.g., card networks) and were deliberately excluded from brand role assignment. `#d72c0d` and `#008060` are Shopify default theme semantic colors (commonly sale/success) and are used here as inferred, not confirmed, badge colors. Typography sizes, line-heights, and letter-spacing beyond the root `font-size: 1.5rem; letter-spacing: 0.06rem` are proposed defaults, not measured computed styles. Font availability (Work Sans, Lora, Helvetica Neue) is based on family names present in CSS only; actual licensing, hosting, and fallback behavior were not verified. No mobile menu, cart drawer, or product-detail interaction markup was available in the supplied evidence.
