---
version: alpha
name: "Oars + Alps"
source_url: "https://oarsandalps.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy ink (#1f2021) anchors a brand that lives at the intersection of outdoor performance and deliberate grooming, where the color story reads like a tide chart — teal accents (#025776, #037ca8, #69ced7) pulse through CTAs and product badges against a canvas of pale gray (#f6f6f6) and white. The brand's signature voltage is a sharp coral-red (#d02e2e) that appears sparingly on sale badges and error states, providing the only warm interruption to an otherwise cool, oceanic palette. Type runs Fabriga and Fabrica Regular — clean, utilitarian sans-serifs with modest weight contrast (400–700) that never compete with the product photography. Buttons use tight 8px radii (`{rounded.sm}`) and compact 40px heights, favoring efficiency over pill-shaped friendliness; the brand trusts its deep teal primary to do the heavy lifting rather than oversized tap targets. Product cards sit on white surfaces with thin hairline borders (`{colors.hairline}`), while the persistent top nav uses the full-width ink background — a rare choice for a DTC brand, signaling authority and premium shelf presence rather than airy discovery. The result is a system that feels less like a lifestyle blog and more like a well-edited gear shop: organized, confident, and built for repeat purchase.

colors:
  primary: "#025776"
  primary-active: "#015776"
  primary-disabled: "#6a9bb0"
  ink: "#1f2021"
  body: "#3d3f41"
  muted: "#5a5d60"
  muted-soft: "#717171"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#f6f6f6"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#69ced7"
  accent-teal-dark: "#037ca8"
  accent-red: "#d02e2e"
  accent-green: "#56ad6a"
  accent-green-soft: "#ecfef0"
  badge-sale: "#d02e2e"
  badge-new: "#025776"
  star-rating: "#1f2021"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Fabriga', 'Fabrica Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  full: 9999px

spacing:
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
    padding: 10px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.muted}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-soft:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  top-nav-link-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.md} 0"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep teal (`{colors.primary}`) with white text and a compact 40px height. Uses a modest 8px radius (`{rounded.sm}`) rather than a pill shape, reinforcing the brand's efficient, no-nonsense attitude. On hover, shifts to `{colors.primary-active}` (#015776). Disabled state uses a desaturated teal (`{colors.primary-disabled}`) at reduced opacity.

**`button-secondary`** — An outlined variant on a white or light canvas background, with a 1px hairline border and ink text. Active state darkens the border to `{colors.muted}` and fills with `{colors.surface-soft}`. Used for "Add to Cart" secondary actions, "Learn More" links in content sections, and cancel/back navigation.

**`button-text-link`** — A text-only button styled as an inline link, using `{colors.primary}` and the link typography token. No background, no border, minimal padding. Used for "View All", "See Details", and account-related actions where visual weight should be minimal.

**`button-pill-accent`** — A small, fully rounded accent button in bright teal (`{colors.accent-teal}`) used sparingly for promotional badges, filter chips, and category quick-links. At 32px height, it's the only pill-shaped button in the system, providing a visual break from the otherwise squared-off button family.

### Cards
**`product-card`** — The primary product display unit, a white card with 8px radius and 16px padding. On hover, lifts with a subtle box-shadow (0 2px 8px rgba(0,0,0,0.08)). Product images fill a 1:1 aspect ratio with 4px corner rounding (`{rounded.xs}`). The card contains the product name in `{typography.title-sm}`, price in `{typography.body-sm}`, and optional badge overlays.

**`product-badge`** — Small uppercase labels that overlay product images, using `{typography.badge}` at 11px with 0.5px letter-spacing. Three variants exist: standard teal (`{colors.primary}`) for "NEW" or "BEST SELLER", red (`{colors.accent-red}`) for sale/promotional badges, and green (`{colors.accent-green}`) for "PLANT-BASED" or eco-certifications.

### Navigation
**`top-nav`** — A full-width dark navy bar (`{colors.ink}`) at 64px height, housing the logo, category links, search, and account/cart icons. Link text is white with 14px/500 weight, and active/current links get a subtle white overlay (`rgba(255,255,255,0.1)`) on a 4px rounded background. This persistent dark bar is the brand's most distinctive structural move — it reads as premium and authoritative rather than the white nav-bar convention of most DTC skincare brands.

**`footer`** — A continuation of the dark ink background, with white text and muted gray links (`{colors.muted-soft}`). Organized in a multi-column layout with accordion behavior on mobile. Social icons, newsletter signup, and legal links live here.

### Forms
**`text-input`** — Standard single-line text fields at 44px height with 8px radius and a 1px hairline border. Focus state swaps the border to `{colors.primary}` teal. Error state uses `{colors.accent-red}` border. Used for email capture, shipping addresses, and search queries.

**`select-dropdown`** — Compact 40px dropdowns with the same hairline border and 8px radius. Used for product variant selection (size, scent, subscription frequency) and filter sorting.

**`quantity-selector`** — A 36px compact stepper with minus/plus buttons flanking a numeric input, bordered by `{colors.hairline}`. Used exclusively on product detail pages and cart line items.

### Badges & Indicators
**`star-rating`** — A 16px inline star rating using `{colors.star-rating}` (ink) for filled stars and `{colors.hairline}` for empty. Rendered as a row of five stars with half-star support.

**`divider`** — A 1px hairline rule used between sections, product rows, and accordion items. A softer variant (`{colors.hairline-soft}`) is used within cards and content blocks where less visual weight is desired.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces top-nav links, accordion footer, search collapses to icon-only, product cards stack full-width |
| Tablet | 744–1128px | 2-column product grid, top-nav shows limited links (Shop, Learn, Search icon), footer in 2-column layout, product cards at 50% width |
| Desktop | 1128–1440px | Full top-nav with all category links, 3-4 column product grid, multi-column footer, product cards at 25% width with hover lift |
| Wide | > 1440px | Max-width container (1440px) centered, same as desktop layout with additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 40px height on mobile
- Icon buttons (cart, account, search) use 40px x 40px tap targets
- Product cards are fully tappable on mobile with no hover-dependent interactions
- Accordion headers in footer and FAQ sections have 44px minimum tap height
- Quantity selector buttons are 36px x 36px — slightly below ideal but consistent with the brand's compact aesthetic

### Collapsing Strategy
- Top navigation collapses from full link set to hamburger menu below 744px
- Product grid collapses from 4 columns to 2 to 1 as viewport narrows
- Footer accordion replaces multi-column layout on mobile, with section headers as tap targets
- Search bar collapses to icon-only on mobile, expanding to full-width overlay on tap
- Product detail page reorders: images stack vertically, add-to-cart section moves below fold on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards and buttons are inferred from common patterns; exact box-shadow values and transition durations were not extractable from the static HTML/CSS
- Error styling for form validation (error messages, iconography, animation) was not present in the extracted data
- Dark mode is not supported — the brand uses a light canvas exclusively
- Subscription/refill component styling (frequency selector, savings badge) was not captured
- Mobile navigation drawer (hamburger menu) animation and overlay styling were not extractable
- Font weights beyond 400, 500, 600, and 700 are assumed — exact weight values for display sizes are inferred from common usage
- The extracted font list includes Arial, Baskerville, Consolas, Roboto, Roboto Slab, and monospace which likely appear in checkout widgets, social embeds, or system fallbacks rather than the brand's primary type system. Fabriga and Fabrica Regular are the brand's active fonts based on their presence in the extracted list and their use by similar outdoor-grooming brands
- Secondary button hover border color is inferred — the exact active state may differ
- Product card shadow on hover is an estimate; the brand may use a different elevation system
- Checkout-specific components (Shopify Pay button, Afterpay badge, Klarna modal) were excluded as they belong to third-party systems
- The extracted color list contains many near-identical grays (#f6f6f6, #f2f2f2, #ebebeb, #e9e9e9, #e6e6e6, #d9d9d9, #bfbfbf) — the most frequently occurring values were selected for the palette, but the brand may use a more limited set
- Accent green (#56ad6a) and its soft variant (#ecfef0) appear in the extracted list but their exact usage (badges, progress indicators, or eco-labels) is inferred
