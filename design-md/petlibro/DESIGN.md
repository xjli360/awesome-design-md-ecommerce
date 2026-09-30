---
version: alpha
name: "Petlibro"
source_url: "https://petlibro.com"
captured_at: "2026-09-28T09:03:59.353558+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Petlibro's storefront evidence shows a neutral, high-contrast foundation: near-black text (#121212, #303030) on white and near-white canvases (#ffffff, #fafafa, #f6f6f6, #f3f3f3), with mid-gray (#616161) for secondary copy and light hairlines (#dedede, #cccccc) for card and section dividers. A dark olive-green (#315800) appears in the palette alongside a cooler olive (#46691a) and a teal-green (#29845a); given Petlibro's nature/pet-care positioning, #315800 is inferred here as the primary brand/CTA color, with mint (#69ce82) and pale mint (#cdfee1) as supporting accent tones for success or "in-stock" style states. A cluster of saturated blues (#005bd3, #2332d5, #334fb4, #142fbd) and payment-mark colors (Mastercard reds/oranges, PayPal blue) are present in the raw CSS but are treated as third-party checkout iconography, not brand palette, and are excluded from primary role assignment. A warm red-orange (#ff3800) is inferred as a sale/promo accent given the observed "Save up to 50%" and giveaway banner language. Typography evidence lists only "pitch" and "sohne" as font-family tokens (plus the non-text "swiper-icons" glyph font); both are mapped to generic sans-serif fallbacks since no serif/weight/size evidence was captured. This interpretation favors a clean, product-photography-forward e-commerce layout with generous white space, soft off-white section backgrounds, and restrained green accenting for primary actions, consistent with a smart pet-tech DTC brand.

colors:
  primary: "#315800"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#616161"
  hairline: "#dedede"
  surface-soft: "#fafafa"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent-blue: "#005bd3"
  success-mint: "#69ce82"
  success-mint-soft: "#cdfee1"
  sale-red: "#ff3800"
  promo-yellow: "#fff8db"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "pitch, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "pitch, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "pitch, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "sohne, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "sohne, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "sohne, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "sohne, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineBottom: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-picker:
    itemShape: "{rounded.full}"
    itemSize: "24px"
    selectedRing: "2px solid {colors.primary}"
    spacing: "{spacing.xs}"

## Components

**button-primary** is the main conversion action (Shop Now, Add to Cart). It uses the inferred brand green fill with white text for high contrast against the light canvas; hover/pressed states are proposed, not observed.

**button-secondary** is an outlined variant for lower-emphasis actions (Compare, Help me choose) sharing the primary green as border/text color on a transparent background, proposed for pairing beside filled buttons in product-selection modules.

**text-input** covers newsletter and giveaway email fields seen in the page copy ("Please enter a valid email address"); styled with a light hairline border and white fill, consistent with the neutral palette. Focus and error states are proposed.

**nav-bar** reflects the mega-menu structure implied by the text excerpt (Feeders, Fountains, Litter Box, Camera, Learn, Support, Cart, Log in). A white background with a bottom hairline is proposed for a clean sticky header; dropdown panel styling is inferred, not measured.

**product-card** represents catalog tiles (e.g., Granary 2, Luma, Dockstream 2, Scout camera) using the soft card surface color and a subtle hairline border, with title/price typography scaled for grid density. Badge overlays (New, Best seller) are proposed as absolutely-positioned children.

**hero** models the homepage banner ("Less guesswork. More insight into your pet's day.") on the off-white surface-soft background with large display typography; imagery treatment is not observed and left to implementation.

**footer** is proposed as a dark ink-colored band (inverting the light body theme) to visually close the page, holding support/legal links (Warranty, Shipping Policy, Track Order) noted in the source text; this inversion is a design choice, not an observed rule.

**badge** covers promotional flags like "New" and sale callouts ("Save up to 50%," "Save up to 17%"), using the inferred sale-red for urgency against the mostly neutral/green palette.

**search** is a pill-shaped input proposed for header search, using the full-radius token and soft surface fill consistent with the light, rounded aesthetic suggested by the swatch/pill patterns in the color-picker CSS.

**color-swatch-picker** is directly evidenced by the `.dl-option-color-item-*` selectors, which render circular color swatches (bisque, black, blue, charcoal, green, ivory, lake, mist, orange, purple, stainless) for product variant selection on PDPs; this is the one component with concrete CSS backing in the supplied evidence.

## Responsive Behavior

Proposed breakpoints (not measured from live site):
| Breakpoint | Range | Layout notes |
|---|---|---|
| mobile | <480px | Single-column product grid, collapsed hamburger nav, stacked hero text over image |
| tablet | 480–1024px | 2-column product grid, mega-menu collapses to accordion |
| desktop | 1024–1440px | 3–4 column product grid, full horizontal mega-menu |
| wide | >1440px | Max-width content container (~1280–1440px), extra whitespace margins |

Touch targets for buttons and swatch pickers should target a minimum 44×44px hit area, even though the swatch visual size is smaller (~24px), via padding. Navigation should collapse to a slide-in or accordion pattern below 1024px. All of the above is recommended practice, not observed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This DESIGN.md is derived from static CSS/text extraction only; no rendered layout, computed box model, or actual breakpoints were observed. Font weights, sizes, and line-heights for "pitch" and "sohne" are proposed defaults, not measured values — actual site typography may differ. The role of "primary" (#315800) is inferred from thematic fit (pet/nature brand) rather than confirmed usage in a CTA rule; several blue and multi-color tokens in the source palette are believed to be third-party payment-icon colors (Mastercard, PayPal, etc.) and were deliberately excluded from brand role assignment, but this exclusion is inferential. Interaction states (hover, focus, active, disabled) and mobile navigation/menu behavior were not observed and are marked proposed throughout. Custom font availability, hosting, and licensing for "pitch" and "sohne" were not verified. Component existence for footer, search, and hero styling is inferred from page text/structure rather than confirmed CSS rules, aside from the color-swatch-picker, which is directly evidenced.
