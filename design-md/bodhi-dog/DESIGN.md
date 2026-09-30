---
version: alpha
name: "Bodhi Dog"
source_url: "https://www.thebodhidog.com/"
captured_at: "2026-09-29T03:58:47.295099+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bodhi Dog is a Shopify-hosted storefront for a family-owned natural pet care brand selling grooming, bath, dental, and odor-control products. The observed CSS exposes a warm, retail-friendly palette anchored by a saturated orange (#f89522) used for primary calls-to-action, paired with a deep navy (#124067) reserved for secondary buttons. Body chrome sits on a soft off-white (#f7f7f7) rather than pure white, with card and section surfaces likely using #ffffff and #f9f8f4 for contrast. Text colors range from near-black (#1a1a1a/#262626) for headings to mid-gray (#666666/#757575) for body copy, consistent with a light, legible commerce layout.
  Font-family declarations reference Inter, Lora, Roboto, and SF Pro Text alongside generic serif/sans-serif/monospace fallbacks; no single family is confirmed as the enforced brand typeface, so this spec treats Inter as the primary UI sans (buttons, nav, product data) and Lora as an inferred serif accent for display headlines, reflecting a "natural/artisanal" positioning common to small-batch pet brands. All sizing, weights, and spacing scales below are proposed defaults calibrated to a compact Shopify grid, not measured from rendered layout. Interactive states (hover/focus/disabled) are drawn directly from theme CSS (e.g. #e07c07 hover, #ae6006 focus, #d5d5d5 disabled) and are the most reliably observed values in this file.

colors:
  primary: "#f89522"
  primary-hover: "#e07c07"
  primary-active: "#ae6006"
  secondary: "#124067"
  secondary-hover: "#164d7d"
  secondary-active: "#1d68a8"
  ink: "#1a1a1a"
  heading: "#262626"
  body: "#666666"
  muted: "#757575"
  hairline: "#dedede"
  hairline-strong: "#d8d8d8"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f9f8f4"
  on-primary: "#ffffff"
  disabled-bg: "#d5d5d5"
  disabled-text: "#757575"
  link: "#1990c6"
  link-hover: "#136f99"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Lora, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 500, lineHeight: 1, letterSpacing: "0px"}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    saleTextColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.heading}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  press-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.lg} {spacing.base}"
    description: |-
      Proposed pattern for the "As seen on" press-logo row (BuzzFeed, CNN, Oprah, AKC),
      a category-relevant trust signal common to grooming/pet-care storefronts.

## Components

**button-primary** renders the site's main add-to-cart and CTA actions using the observed orange (#f89522) with white text, transitioning to a darker orange (#e07c07) on hover and deep amber (#ae6006) on focus/active — these three states are directly present in the theme CSS.

**button-secondary** uses the navy (#124067) fill from `.btn--secondary`, stepping through `#164d7d` (hover) and `#1d68a8` (active/focus), giving the brand a two-tone primary/secondary action system suitable for "Shop Now" vs "Learn More" pairings.

**button-outline** is a proposed variant modeled on `.btn--secondary-accent`, which the CSS defines with an orange border/text on a white background — useful for tertiary actions like "Add to Wishlist" on product tiles.

**text-input** is inferred for search and account/login forms; no explicit input CSS was supplied, so border, padding, and radius follow the theme's general button/card conventions for visual consistency.

**nav-bar** represents the top utility/navigation bar (Home, All Products, About Us, Account, Cart) implied by the page text; colors and hairline are inferred from the global palette since no nav-specific selectors were captured.

**product-card** models the featured-product grid ("On sale from $13.99," etc.) with a soft card surface, hairline border, and the orange sale-price accent — layout metrics (grid columns, image ratio) are not observed and are left to implementation.

**hero** covers the top banner ("Natural Pet Care / Shop all products") plus the promotional ribbon; background uses the softer canvas tone to differentiate from white content sections, per the body/html background-color rule.

**footer** is inferred as a navy band (reusing `{colors.secondary}`) housing site links, social icons, and the "family owned" trust copy, consistent with the secondary-button color already present in the palette.

**badge-sale** captures the repeated "Sale" labels seen throughout featured products, using the primary orange in a pill shape — radius and padding are proposed, not measured.

**search** is a proposed overlay/input pattern for the "SEARCH / Search" control referenced in the nav, styled consistently with text-input.

**press-strip** is a category-appropriate addition for the "As seen on" / "Found at these retailers" press-logo sections, using muted text on the soft surface background to stay visually secondary to product content.

## Responsive Behavior
This is a **recommendation**, not measured site behavior — no breakpoints, media queries, or mobile screenshots were present in the supplied evidence.

| Breakpoint | Width      | Layout notes (proposed)                          |
|-----------|------------|---------------------------------------------------|
| mobile    | <600px     | single-column hero/product grid, collapsed nav (hamburger), full-width buttons |
| tablet    | 600–959px  | 2-column product grid, condensed nav labels        |
| desktop   | 960–1279px | 3–4 column product grid, full nav bar visible      |
| wide      | ≥1280px    | max-width content container, 4+ column grid, press-logo row on one line |

Touch targets should be a minimum of 44×44px for buttons and nav icons; the mobile nav is expected to collapse into a slide-out or dropdown menu given the "Home / All Products / About Us / Contact Us" link list, though this interaction was not observed in the supplied CSS/HTML.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from a static CSS/text snapshot; no rendered DOM, computed layout, or JavaScript-driven interaction (cart drawer, search overlay, mobile menu toggle) was observed. Font-family roles (Inter for UI, Lora for display) are an inferred pairing based on which families appear in the supplied `font_families` list — actual heading/body assignment in the live theme is unconfirmed, and custom font licensing/availability was not verified. Several color roles (ink vs. heading, muted vs. body, hairline) are inferred by proximity to gray/neutral values in the palette rather than confirmed via matched selectors. Typography sizes, spacing scale, and border-radius values are proposed defaults, not measured from the site. Component layouts (nav-bar, hero, footer, search, text-input) are structurally inferred from page text and generic Shopify theme conventions, since no corresponding selectors were supplied for them. Interactive/hover states are reliable only where explicitly present in theme CSS (buttons); all other states are proposed.
