---
version: alpha
name: "Baseus"
source_url: "https://www.baseus.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand that lives in the gap between industrial reliability and a bright, almost playful confidence, Baseus anchors itself on a deep near-black ink (#282828) and a high-voltage marigold (#fdbc00) that appears on every primary action — add-to-cart buttons, promotional banners, and the glowing ring around product photography. The palette is unusually wide: alongside the core duo sit a cool technical blue (#00aeef) for secondary actions and link text, a safety green (#05d92d) for stock indicators and success states, and a sharp alert red (#dd2c00) for sale badges and urgency markers. The canvas is pure white (#ffffff) with a family of warm grays (#f5f5f5, #ececec, #dedede) that create soft surface hierarchy without ever feeling cold. Typography runs DM Sans at clean weights — display headlines sit at 500–600 weight, body copy at 400, and the system avoids heavy 700+ except in micro-labels and badges. Corners are modest: buttons use {rounded.sm} (8px), product cards use {rounded.md} (12px), and the only {rounded.full} tokens appear on search inputs and icon badges. The overall mood is "workshop-meets-marketplace" — the black-and-yellow palette recalls tool brands and safety equipment, but the generous whitespace, soft grays, and DM Sans curves keep it from feeling harsh. Every component feels engineered for clarity: high-contrast text on buttons, clear hover states on cards, and a navigation system that prioritizes category discovery over brand storytelling.

colors:
  primary: "#fdbc00"
  primary-active: "#e5a800"
  primary-disabled: "#fdeba8"
  ink: "#282828"
  body: "#464646"
  muted: "#696969"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#ececec"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#282828"
  accent-blue: "#00aeef"
  accent-green: "#05d92d"
  accent-red: "#dd2c00"
  badge-sale: "#dd2c00"
  badge-new: "#00aeef"
  star-rating: "#fdbc00"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  micro-label:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  link:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.1px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-item:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "0 16px"
    height: 64px
  top-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 16px"
    height: 64px
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "2px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  product-card-rating:
    typography: "{typography.caption}"
    padding: "0 {spacing.base} {spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm} 0 0 {rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "0 {rounded.sm} {rounded.sm} 0"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loading:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with marigold (#fdbc00) and dark ink (#282828) text for maximum contrast. Hover shifts to a slightly deeper gold (#e5a800), disabled drops to a pale yellow (#fdeba8) with muted text. Used for add-to-cart, checkout, and primary form submissions.

**`button-secondary`** — An outlined variant on white canvas with a 1px hairline border. Hover darkens the border to ink and fills the background with surface-soft (#f5f5f5). Used for "View Details" and secondary product actions.

**`button-ghost`** — A text-only button with no border or background. Hover adds a soft surface fill. Used for cancel actions, "Learn More" links, and dismissible UI controls.

**`button-pill-primary`** — A smaller, fully rounded variant of the primary button, used for promotional tags, filter chips, and quick-add actions. Same color logic as button-primary but with {rounded.full} and tighter padding.

**`button-pill-outline`** — The pill-shaped outline counterpart, used for category filters and toggle chips. Active state fills with primary color.

### Navigation
**`top-nav`** — A fixed 64px white bar with a soft bottom hairline. Logo sits left, nav items center, utility icons (search, cart, account) right. Active nav item is indicated by a 2px primary-color underline.

**`top-nav-item`** — Individual navigation links in muted gray (#696969) with 500 weight. Active state switches to ink (#282828) and shows the primary underline.

**`search-bar`** — A pill-shaped input on surface-soft background with a 1px hairline border. Focus state swaps to white canvas with a 2px primary border. Includes a search icon on the left and optional clear button on the right.

**`breadcrumb`** — A simple horizontal list of category links in caption size. Active (current page) uses ink, ancestors use muted. Separator is a forward slash or chevron in hairline.

### Cards
**`product-card`** — A white card with soft 12px rounding and a 1px hairline border. Contains a square aspect-ratio image at top, then title, rating, and price stacked below. Hover adds a subtle shadow and darker border. Sale badges are positioned absolutely at top-left.

**`product-card-badge`** — A small uppercase label in red (#dd2c00) for sale items, or blue (#00aeef) for "New" tags. Positioned absolutely over the product image with 4px rounding.

**`category-card`** — A larger card used for department navigation, with an icon or image and category name. Hover swaps the border to primary yellow and fills the background with surface-soft.

### Forms
**`text-input`** — Standard input field with 8px rounding, 1px hairline border, and 44px height. Focus state uses a 2px primary border. Error state uses a 2px red border (#dd2c00).

**`select-dropdown`** — Matches text-input styling but includes a dropdown arrow icon. Used for sorting, filtering, and variant selection.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking a center number. Bordered container with 8px rounding. Used on product detail pages and cart.

**`newsletter-input`** — A split input with a text field on the left (8px rounding on left side only) and a primary submit button on the right (8px rounding on right side only). Used in the footer.

### Footer
**`footer-section`** — A full-width dark section on ink (#282828) background with white text. Contains columns of links, a newsletter signup, and social icons. Links are muted gray with white hover.

### Feedback & Loading
**`loading-spinner`** — A 24px rotating circle in primary yellow. Used for async actions and page transitions.

**`skeleton-loading`** — Gray (#ececec) placeholder blocks with 4px rounding, used while product images and content load.

**`tooltip`** — Small dark box with white text, 4px rounding, and 4px/8px padding. Appears on hover for icon buttons and truncated text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 items), hamburger nav, stacked footer, full-width hero, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid (3–4 items), visible nav items limited to 4, footer splits into 2 rows, hero has reduced padding |
| Desktop | 1128–1440px | Three-column product grid (4–5 items), full nav visible, multi-column footer, standard hero padding |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid, expanded whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 8px internal padding
- Quantity selector buttons are 40x40px
- Product card tap targets (title, price, image) are at least 48px tall
- Pagination buttons are 36x36px (minimum for desktop, 44x44px on mobile)

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grid reduces from 4 columns to 2 columns on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Search bar collapses to a search icon that expands to full-width overlay on tap
- Category strip becomes a horizontal scrollable row on mobile
- Product detail page switches from side-by-side to stacked layout below 744px
- Cart page collapses multi-column table to stacked item rows on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; the above states are inferred from common patterns and the brand's color logic
- Error styling (error messages, validation states, error icons) is not confirmed from the live site; red (#dd2c00) is used as the error color based on its presence in the palette
- Dark mode styling is not present on the live site and has not been defined
- Sub-brand or promotional color palettes (e.g., seasonal campaigns, limited editions) are not captured
- Animation and transition durations, easing curves, and micro-interactions were not extractable
- Icon set and illustration style are not documented; the brand appears to use a mix of custom and generic icons
- Typography scale for mobile (smaller sizes, adjusted line heights) is not confirmed; the above scale is desktop-first
- Specific padding and margin values for nested components (e.g., card content padding, grid gaps) are estimated from visual inspection
- Checkout flow styling (Shopify default vs. custom) could not be determined
- Accessibility contrast ratios for all color combinations have not been verified
- The extracted hex list includes many grays and a few accent colors; the brand's true primary is #fdbc00 (marigold) based on its distinctive, non-generic nature and its use in primary actions on the live site
