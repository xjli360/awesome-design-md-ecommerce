---
version: alpha
name: "Comotomo"
source_url: "https://comotomo.com/collections/shop-all"
captured_at: "2026-09-29T04:11:45.669626+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the Comotomo Shop All collection page, the
  brand's own Shopify-hosted storefront for its feeding line (Baby Bottle Gen 2,
  Replacement Nipple, Teether, Food Container, Toddler Tumbler). The CSS exposes
  a neutral, editorial system built on "Noto Sans Display" with "Pretendard" as a
  secondary/CJK-aware family, heavy heading weight (900) and uppercase button
  styling (weight 600). The captured palette is dominated by neutral grays and
  near-blacks (#1c1c1c, #3a3a3a, #707070) layered over light surfaces (#ffffff,
  #f7f7f8, #f4f4f6), with a single soft mint (#b2f9e9) as the only warm/brand-
  adjacent accent observed — treated here as an inferred decorative accent rather
  than a confirmed primary brand color. A darker neutral (#272d45) is proposed as
  the primary action color because product-card buttons render white text
  (color:#fff), implying a dark button fill; the exact background hex was not
  directly captured and is therefore inferred. Card, hairline, and review-widget
  colors (#dbdde4, #e5e5eb, #e5e5e5) come from Okendo review-widget CSS variables
  bundled on the page and are reused here for borders and soft surfaces rather
  than invented. Payment-icon colors (e.g. #eb001b, #0071ce) are excluded from
  brand roles as they likely belong to card-network logos, not the Comotomo
  identity.

colors:
  primary: "#272d45"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#777777"
  hairline: "#dbdde4"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  on-primary: "#ffffff"
  accent-mint: "#b2f9e9"
  surface-alt: "#e5e5eb"
  border-light: "#e5e5e5"
  text-secondary: "#676986"
typography:
  display-xl: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 32px, fontWeight: 900, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.8, letterSpacing: 0px}
  body-sm: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "'Noto Sans Display', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px, textTransform: uppercase}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  review-widget:
    backgroundColor: "{colors.canvas}"
    buttonBackground: "{colors.surface-soft}"
    buttonBackgroundHover: "{colors.surface-card}"
    buttonBackgroundActive: "{colors.text-secondary}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"

## Components

**button-primary** is proposed for "BUY" and cart actions seen on product tiles; the dark fill and white label are inferred from the `.card-information .button span { color:#fff }` rule, since the exact background hex was not directly captured in the extracted CSS.

**button-secondary** is a proposed outline variant for secondary actions (e.g. "SIGN UP" in a lighter context, or filter toggles), using the same ink tone as an outline to keep visual weight subordinate to the primary button. Not directly observed as a distinct style.

**text-input** covers the newsletter email field and any future search/account inputs. Border and radius are inferred from the general neutral hairline palette; no dedicated input CSS was present in the supplied evidence.

**nav-bar** represents the top utility row (OUR STORY / PRODUCTS / SHOP / HELP CENTER / CART). Only text content and general body typography were observed; exact nav padding, sticky behavior, and active-state styling are proposed.

**product-card** models the Shop All grid tiles (Baby Bottle Gen 2, Nipple, Teether, Food Container, Tumbler). The soft card background and hairline border are drawn from the `.product-list-slider .cover::after` divider rule and the Okendo surface tokens; card corner radius is a proposed value, not measured.

**hero** models the top-of-collection banner pairing a product name with a short tagline (e.g. "Baby Bottle. Refined."). Generous vertical padding is proposed to match the page's spacious, editorial tone implied by `line-height:1.8` on body copy.

**footer** groups the PRODUCTS / COMPANY / HELP CENTER / COMMUNITY link columns and social icons. A dark ink background with white text is proposed for contrast; the actual footer background color was not directly observed in the supplied CSS.

**badge** is a proposed small accent chip (e.g. "New," "Gen 2") using the one clearly non-neutral color in the evidence, the soft mint `#b2f9e9`, to give the otherwise grayscale system a brand-adjacent highlight without overreaching beyond observed data.

**search** is a proposed lightweight search affordance for the Shop All collection, styled consistently with text-input using the same neutral surface and hairline tokens; no search-specific CSS was present in the evidence.

**review-widget** directly reflects the bundled Okendo (`oke-`) review component variables — button background, hover, and active states, border color, and text-primary color are all taken verbatim from the `:root` Okendo variable block, making this the most evidence-grounded component in the set.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width        | Layout guidance                                  |
|-----------|--------------|---------------------------------------------------|
| mobile    | < 480px      | Single-column product grid, stacked nav → hamburger, full-width buttons |
| tablet    | 480–959px    | 2-column product grid, condensed nav links visible |
| desktop   | 960–1279px   | 3-column product grid, full horizontal nav |
| wide      | ≥ 1280px     | 4-column product grid, max-width content container |

Touch targets should be at least 44×44px for cart/buy buttons and nav items. Below tablet width, primary navigation is assumed to collapse into a menu icon; this collapse pattern was not observed directly and is a standard proposal for this layout scale.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- This document is built from static CSS/text extraction only; no rendered layout, breakpoints, hover states, or JavaScript-driven interactions were directly observed.
- The primary button background (#272d45) is inferred from a white button-text rule, not from a captured background-color declaration.
- Several palette entries (e.g. #0071ce, #eb001b, #f79e1b, #ff5f00, #142fbd, #1532cb) closely resemble standard payment-network brand colors and were deliberately excluded from Comotomo's own role mapping.
- Font availability, licensing, and exact weight/style variants for "Noto Sans Display" and "Pretendard" were not verified beyond the `:root` CSS custom properties.
- All numeric type scale sizes (display-xl, display-md, title-md, body-sm, caption, button-md) beyond the root `1.4rem` body size and stated scale ratios are proposed approximations, not measured render sizes.
- Component states (hover, focus, disabled, active) beyond the Okendo review-widget variables are proposed patterns, not confirmed from captured CSS.
- Mobile navigation collapse and grid column counts are conventional recommendations, not observed DOM/CSS evidence.
