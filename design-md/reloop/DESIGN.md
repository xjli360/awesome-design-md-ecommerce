---
version: alpha
name: "Reloop"
source_url: "https://www.reloop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A DJ-gear brand that uses a heavy black canvas (#181818) as its foundation, punctuated by a sharp, urgent red (#cc3333) that appears on primary calls-to-action, price highlights, and sale badges — a color pairing that reads as nightclub lighting rather than e-commerce warmth. The extracted palette is dominated by Bootstrap-era utility colors (#a94442 for error, #3c763d for success, #31708f for info) suggesting the site was built on a framework base and then overlaid with the brand's own dark-and-red identity. Typography defaults to Open Sans at moderate weights, with display headlines at 24–28px in weight 600 and body copy at 14–16px in weight 400, creating a clean, readable hierarchy that lets product photography and technical specs take center stage. The brand's signature move is the use of the red (#cc3333) as a single accent voltage — it never appears on backgrounds, only on text, borders, and small UI elements like add-to-cart buttons and stock indicators, preserving the dark canvas as the dominant visual field. Product cards use a slightly lighter surface (#f2f2f2) for contrast against the black background, with hairline borders (#d9d9d9) that define edges without competing with the product imagery. The overall feel is utilitarian and high-contrast, built for DJs who scan quickly for specs and prices rather than browsing leisurely.

colors:
  primary: "#cc3333"
  primary-active: "#a94442"
  primary-disabled: "#ebccd1"
  ink: "#181818"
  body: "#4b4b4b"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  info: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  error: "#a94442"
  error-bg: "#f2dede"
  error-border: "#ebccd1"
  badge-sale: "#cc3333"
  badge-new: "#31708f"
  badge-stock: "#3c763d"
  price-highlight: "#cc3333"
  rating-star: "#cc3333"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  price-md:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Open Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  button-icon-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    border: "1px solid {colors.error}"
    boxShadow: "0 0 0 2px {colors.error-bg}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 16px
    width: 16px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 16px
    width: 16px
  radio:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 16px
    width: 16px
  radio-checked:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 16px
    width: 16px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 64px
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 64px
    borderBottom: "2px solid {colors.primary}"
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  nav-bar-dropdown-item:
    padding: "{spacing.sm} {spacing.lg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  nav-bar-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    height: 200px
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.price-highlight}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-rating-star:
    textColor: "{colors.rating-star}"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
    marginTop: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    height: 400px
    padding: "{spacing.xxl}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginTop: "{spacing.md}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  search-bar-icon:
    textColor: "{colors.muted}"
    height: 16px
    width: 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-stock:
    backgroundColor: "{colors.badge-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-out-of-stock:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.success-border}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.info-border}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.warning-border}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.error-border}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  spec-table-row:
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
    width: 120px
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-item:
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.sm}"
  pagination-item-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.sm}"
  pagination-item-hover:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  breadcrumb-link-hover:
    textColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for add-to-cart, checkout, and submit actions. Rendered in the brand's signature red (#cc3333) with white text and a subtle 4px border radius. On hover, it shifts to a deeper red (#a94442) for a clear state change. The disabled state uses a light pink (#ebccd1) with muted gray text, signaling the action is unavailable without visual noise.

**`button-secondary`** — A secondary action button with a white background, black text, and a 1px hairline border. Used for "View Details," "Compare," and "Cancel" actions. On hover, the background shifts to soft gray (#f5f5f5) and the border darkens to muted gray (#777777). The active state maintains the same structure.

**`button-ghost`** — A text-only button with no background, using the primary red for text color. Used for "Clear Filters," "Remove," and "Learn More" links that need to be less prominent than a full button. On hover, a light red background (#f2dede) appears behind the text for a subtle interaction cue.

### Cards
**`product-card`** — The primary product display unit, using a light gray background (#f2f2f2) with a soft hairline border (#e5e5e5) and 8px rounded corners. Each card contains a product image (200px tall, 4px rounded), a title in 14px/600 weight, a price in 18px/700 weight in the brand red, and optional badges for sale, new, or stock status. On hover, the card gains a subtle box shadow and the border shifts to a darker gray (#d9d9d9). The add-to-cart button sits at the bottom of the card, using the primary button style at a smaller size.

**`hero-banner`** — A full-width promotional banner with a black background (#181818) and white text, used for seasonal sales, new product launches, and brand campaigns. The headline uses the largest display type (28px/600), with a subtitle in body weight and a primary CTA button. The banner is 400px tall with generous padding (48px) to create breathing room around the text.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a black background (#181818) and white text, 64px tall. Links are uppercase 14px/600 weight with 16px horizontal padding. The active link is highlighted with the brand red text color and a 2px red bottom border. Dropdown menus use a white background with a subtle box shadow, and items show a soft gray background on hover with red text.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px hairline border, and 4px rounded corners. On focus, the border shifts to the brand red with a 2px red shadow ring (#ebccd1). Error states use a red border with a light red shadow ring (#f2dede). Checkboxes and radio buttons use the brand red for checked states, with 16px dimensions and appropriate border radii.

### Alerts
**`alert-success`**, **`alert-info`**, **`alert-warning`**, **`alert-error`** — Four alert variants using the Bootstrap-style utility colors extracted from the site. Each uses a light background, matching border, and colored text. Success uses green (#3c763d), info uses blue (#31708f), warning uses amber (#8a6d3b), and error uses red (#a94442). These are used for form validation messages, stock notifications, and system feedback.

### Badges
**`badge-sale`**, **`badge-new`**, **`badge-stock`**, **`badge-out-of-stock`** — Small uppercase labels that appear on product cards and listing pages. Sale badges use the brand red, new badges use blue, in-stock badges use green, and out-of-stock badges use the error red. All badges use 11px/700 weight type with 0.5px letter spacing and 2px border radius.

### Spec Table
**`spec-table`** — A structured table for displaying product specifications, used extensively on product detail pages. Each row contains a label (12px/600 uppercase, muted gray) and a value (14px/400, black). The table has a 1px hairline border and 8px rounded corners, with rows separated by soft hairline dividers.

### Pagination
**`pagination`** — A horizontal pagination component for product listing pages. Items are spaced with 4px padding and have 4px rounded corners. The active page uses the brand red background with white text, while inactive items show a soft gray background on hover.

### Breadcrumb
**`breadcrumb`** — A simple breadcrumb navigation using 12px/400 type in muted gray. Links are black and turn red on hover. Separators use a lighter muted gray with 4px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, collapsed nav to hamburger menu, hero banner reduced to 250px height, spec tables stack vertically, pagination shows only prev/next |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero banner at 300px height, spec tables remain horizontal but with reduced padding |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with dropdowns, hero banner at 400px height, full spec tables with side-by-side layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner at 450px height with wider padding |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav bar links have 64px touch targets (full nav bar height)
- Product card add-to-cart buttons are 32px tall (below 44px minimum — known gap)
- Search bar has 40px height (below 44px minimum — known gap)
- Checkbox and radio inputs are 16px (below 44px minimum — known gap, but standard for web forms)

### Collapsing Strategy
- Top navigation collapses from full link set to hamburger menu at < 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 column as viewport shrinks
- Hero banner text stack collapses from side-by-side to stacked at < 744px
- Spec tables collapse from horizontal rows to stacked label-value pairs at < 744px
- Footer link columns collapse from 4 columns to 2 to 1 column as viewport shrinks
- Pagination collapses from full number set to prev/next only at < 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards were inferred from common patterns — exact extracted hover colors were not available
- Error styling for form inputs was inferred from Bootstrap utility colors — exact brand error states may differ
- Dark mode is not present on the live site and was not extracted
- Sub-brand palettes (if any exist for product lines) were not extracted
- The extracted font list includes framework defaults (FontAwesome, Glyphicons) — the brand's actual font stack may be simpler
- The extracted hex colors include many Bootstrap utility colors — the brand's true primary (#cc3333) was identified as the most distinctive accent, but secondary colors may differ
- Animation and transition timings were not extracted
- Iconography style and sizing were not extracted
- Product card image aspect ratios and zoom behavior were not extracted
- The meta theme-color was not set on the live site
- The site does not appear to be on Shopify, so checkout widget colors were not relevant
- The extracted color list had 30+ entries, many of which are Bootstrap defaults — the palette above focuses on the most brand-relevant colors
