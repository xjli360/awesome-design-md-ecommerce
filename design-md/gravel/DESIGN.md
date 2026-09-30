---
version: alpha
name: "Gravel"
source_url: "https://gravel.co/"
captured_at: "2026-09-29T04:15:16.087864+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gravel presents itself as a utilitarian, gear-forward travel accessories
  brand, and the supplied evidence supports a restrained, functional palette
  built on a warm off-white canvas (#ffffed) paired with near-black ink
  (#232323) and a softer body-copy gray (#363636). The most concrete
  brand-action color is the accelerated-checkout button blue (#1990c6,
  hover #136f99), which we treat as the primary interactive color since it
  is the only button fill directly observed in the CSS. Secondary teal
  tones (#00caaa, #b2f9e9) and a muted green (#4cb963) appear in the
  palette without a confirmed UI role, so they are mapped as inferred
  accent/status colors (e.g., success or promo highlights) rather than
  core brand color. Neutral surfaces (#f0f0f2, #ffffff, #e5e5eb) support
  card and hairline treatments typical of a Shopify storefront theme.
  Typography draws on the observed font stack: Selecta (Bold/Regular) is
  interpreted as a proprietary-feeling display face for headlines, Plus
  Jakarta Sans as the primary body/UI sans-serif, and Fragment-Mono as a
  technical, tag-like label face fitting the "field goods" gear framing.
  All sizing beyond the one measured 14px button token is proposed, not
  observed.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#232323"
  canvas: "#ffffed"
  body: "#363636"
  muted: "#9ca3af"
  hairline: "#e5e5eb"
  surface-soft: "#f0f0f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#00caaa"
  accent-teal-light: "#b2f9e9"
  accent-success: "#4cb963"
  navy: "#272d45"
  warm-clay: "#aa6659"
  black: "#000000"
typography:
  display-xl: {fontFamily: "Selecta-Bold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Selecta-Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Selecta-Regular, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Fragment-Mono-Regular, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.navy}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** uses the one concretely observed button fill (#1990c6, hover #136f99) from the accelerated-checkout CSS, extended here as the general primary call-to-action style; hover/active states beyond the checkout button are proposed.

**button-secondary** is an inferred outline/ghost treatment using the hairline gray for borders, intended for tertiary actions like "Shop All" links; no secondary button was directly observed.

**text-input** proposes a card-white field with a thin hairline border, matching the neutral surface tones seen in the review-widget CSS variables (`--oke-border-color:#e5e5eb`); focus states are not observed and are proposed.

**nav-bar** is inferred from the visible top navigation labels (SHOP, SALE %, LOGIN, CART) and uses the cream canvas as background with ink text for a light, minimal header; sticky/scroll behavior is not confirmed.

**product-card** reflects the grid of "BEST SELLER" and "% OFF" product tiles referenced in the page text (Explorer Plus™, Layover™ Blanket), using a white surface with a soft border and rounded corners; exact card padding is proposed.

**hero** is modeled on the large banner copy ("FIELD GOODS + MORE ESSENTIALS," "Toiletry Bags. Built to Organize.") using a soft neutral background and the largest display type scale; no hero image treatment was observed in CSS.

**footer** uses ink as a dark background with light text, echoing typical DTC footer patterns and the multi-column link structure (Company, Support, Connect) present in the text content; this color pairing is inferred, not directly styled in the supplied CSS.

**badge** represents sale/best-seller labels ("19% OFF," "BEST SELLER") using the teal accent as a plausible highlight color since no explicit badge CSS was supplied; shape and color are proposed.

**search** is a minimal inferred component consistent with the cart/login/shop nav pattern; no search-specific CSS was present in the evidence.

**announcement-bar** directly reflects the repeated "FREE US SHIPPING ON ORDERS $99+" marquee text at the top of the page, styled here as a dark strip with mono-style caption type for a technical, gear-label feel; exact colors and animation were not observed.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet | 640–1024px | 2-column product grid, condensed nav bar |
| desktop | >1024px | 3–4 column product grid, full horizontal nav |

Touch targets should be a minimum of 44px for buttons and nav items. The nav bar should collapse into a drawer/hamburger pattern below tablet width. None of this responsive structure was directly observed in the supplied CSS; it is a standard proposal for a Shopify-based storefront of this category.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS rules, a color list, and font-family names extracted from the page; no live layout, spacing, or interaction states were observed.
- Only one concrete UI color (#1990c6 button fill) and one concrete radius (4px, from the review-widget button token) were directly tied to a component; all other color-to-role and radius assignments are inferred.
- Font sizes, weights, and letter-spacing in the typography scale are proposed conventions, not measured values, aside from the 14px `--oke-text-regular` token used for button-md.
- Availability, licensing, and exact weight range of the custom fonts (Selecta-Bold/Regular, Fragment-Mono-Regular) were not verified; fallback stacks are provided.
- Mobile navigation, hover/focus states, and animation behavior (e.g., the shipping marquee) were not observed and are marked proposed throughout.
