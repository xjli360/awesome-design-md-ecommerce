---
version: alpha
name: "Relapse Records"
source_url: "https://www.relapse.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label and storefront that wears its death-metal lineage in a #ff0000 primary — a red that reads as blood-spatter, not brand-identity warmth, and sits against a #121212 near-black canvas. The extracted palette is deliberately raw: #232323 for ink, #5f605d for muted text, #ebebeb and #e7e7e7 for hairline strokes. There is no gradient, no soft-shadow, no rounded-full pill button — the system uses {rounded.xs} (4px) for cards and {rounded.sm} (8px) for buttons, as if every corner was clipped with a box-cutter. Montserrat runs the typography at 400/600/700 weights, with display sizes at 24–32px and body at 14–16px, never decorative. The #332fd0 accent (a cold, synthetic blue) appears on select badges and sale tags, a rare secondary voltage against the red-and-black. This is a store built for browsing band merch and vinyl: product cards are dense with album art, price, and format badges; the nav is a single dark bar with genre dropdowns; the search is a simple input, not a hero feature. The red is not friendly — it signals limited-edition drops, pre-order urgency, and the label's three-decade history in extreme music.

colors:
  primary: "#ff0000"
  primary-active: "#cc0000"
  primary-disabled: "#ff6666"
  ink: "#232323"
  body: "#5f605d"
  muted: "#9ca3af"
  muted-soft: "#cfcfcf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#232323"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#332fd0"
  sale-badge: "#ff0000"
  preorder-badge: "#332fd0"
  sold-out-badge: "#5f605d"
  star-rating: "#ff0000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 32px
    width: 32px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 60px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  top-nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-compare-price:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    textDecoration: "line-through"
  format-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  format-badge-vinyl:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  preorder-badge:
    backgroundColor: "{colors.preorder-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  sold-out-badge:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.lg}"
    height: 44px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px {spacing.xl}"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "14px {spacing.xl}"
    height: 48px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link-hover:
    typography: "{typography.caption}"
    textColor: "{colors.on-primary}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.on-primary}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.base}"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.base}"
    height: 40px
    border: "1px solid {colors.primary}"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px {spacing.md}"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px {spacing.md}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(18, 18, 18, 0.6)"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px {spacing.xl}"
    height: 48px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} {spacing.xl} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  collection-grid:
    gap: "{spacing.base}"
    padding: "{spacing.xl}"
  product-detail-image:
    rounded: "{rounded.xs}"
    maxWidth: "100%"
  product-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.on-primary}"
  product-detail-artist:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
  product-detail-price:
    typography: "{typography.title-md}"
    textColor: "{colors.on-primary}"
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  product-detail-format-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  cart-item-image:
    rounded: "{rounded.xs}"
    width: 80px
    height: 80px
  cart-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  cart-item-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.on-primary}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px {spacing.xl}"
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, rendered in {colors.primary} (#ff0000) with white text and {rounded.sm} corners. Used for "Add to Cart", "Pre-Order", and "Checkout" actions. On hover, shifts to {colors.primary-active} (#cc0000) for a darker, more urgent state. Disabled state uses {colors.primary-disabled} (#ff6666) to indicate unavailability while maintaining brand color.

**`button-secondary`** — An outlined variant on dark backgrounds, using {colors.surface-card} (#232323) background with a {colors.hairline} (#dedede) border and white text. Used for "View Details" and "Continue Shopping" actions. Active state fills to {colors.ink} (#232323) for a solid dark appearance.

**`button-tertiary-text`** — A text-only button in {colors.primary} (#ff0000) with no background or border. Used for "Clear Filters", "Remove", and secondary navigation links. Hover shifts to {colors.primary-active} (#cc0000) for visual feedback.

**`icon-button`** — A transparent 32px square button for cart, search, and menu icons. Hover state adds a {colors.surface-soft} (#1a1a1a) background with {rounded.sm} corners for subtle distinction against the dark canvas.

### Cards
**`product-card`** — The core product display unit, using {colors.surface-card} (#232323) background with {rounded.xs} (4px) corners — the tightest radius in the system, reflecting the brand's raw aesthetic. Contains a 1:1 product image, title in {typography.title-sm}, price in {typography.body-sm} with {colors.muted}, and optional format/badge tags. Hover state adds a {colors.hairline} border and shifts background to {colors.surface-soft} (#1a1a1a).

**`product-card-image`** — The album art or product photo, cropped to a square aspect ratio with {rounded.xs} corners. No border-radius on the image itself — the card container clips it.

### Badges
**`format-badge`** — Small uppercase labels for product format (CD, Cassette, Digital) using {colors.surface-soft} background and {colors.muted} text. Vinyl format uses a distinct {colors.ink} background with white text for visual hierarchy.

**`sale-badge`** — A {colors.primary} (#ff0000) badge for sale items, using {typography.badge} (11px uppercase, 700 weight). Appears in the top-left corner of product card images.

**`preorder-badge`** — Uses the {colors.accent-blue} (#332fd0) secondary accent for upcoming releases, distinguishing pre-order items from in-stock inventory.

**`sold-out-badge`** — A neutral {colors.sold-out-badge} (#5f605d) badge for unavailable items, using the same uppercase badge typography.

### Navigation
**`top-nav`** — A fixed 60px dark bar on {colors.canvas} (#121212) with a subtle {colors.hairline} bottom border. Navigation links use {typography.nav-link} (13px uppercase, 600 weight) in {colors.muted} (#9ca3af), with active links switching to white and a 2px {colors.primary} bottom border.

**`top-nav-dropdown`** — Genre and collection dropdowns use {colors.surface-card} (#232323) background with {rounded.sm} corners and {typography.body-sm} for list items. No hover color change — items remain white on dark.

### Forms
**`search-input`** — A simple text input on {colors.surface-card} background with a {colors.hairline} border and {rounded.sm} corners. Focus state switches the border to {colors.primary} (#ff0000) for clear active indication. No placeholder styling — the input is minimal.

**`newsletter-input`** — Matches the search input pattern but appears in the footer. The submit button uses {colors.primary} with {typography.button-sm} for a compact CTA.

**`quantity-selector`** — A numeric input for cart quantities, using the same dark card background and hairline border pattern. Height matches button heights (44px) for alignment in product detail layouts.

**`filter-dropdown`** — Collection and genre filters use a 40px compact dropdown with {colors.surface-card} background. Active state switches border to {colors.primary} for visual distinction.

**`filter-chip`** — Pill-shaped filter tags using {rounded.full} with {colors.surface-card} background and hairline border. Active chips fill with {colors.primary} for clear selection state.

### Footer
**`footer`** — A full-width dark section on {colors.canvas} with a {colors.hairline} top border. Links use {colors.muted} with {typography.link} (14px, 400 weight), shifting to white on hover. Contains newsletter signup, navigation links, and social icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, filter dropdowns stack vertically, hero banner collapses to 250px min-height |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links with "More" dropdown, filter sidebar becomes horizontal chip row |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, filter sidebar on left, product detail shows two-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner expands to 500px min-height |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 32px with 44px touch target via padding
- Filter chips are 32px tall with 8px padding for comfortable tapping
- Product cards have full-area tap targets (no nested click zones)

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Filter sidebar collapses to horizontal scrollable chip row below 744px
- Product detail layout shifts from two-column to single-column below 744px
- Footer navigation collapses from multi-column to single-column stack below 744px
- Hero banner text overlay reduces font size from 32px to 24px below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom, overlay, quick-add) could not be reliably extracted from the live site
- Error styling for form validation (red borders, error messages) was not observed in the extracted data
- Dark mode is the default and only observed state — no light mode variant was found
- Checkout flow styling (Shopify checkout, payment buttons) was not extracted and may use default Shopify themes
- Social media icon colors were filtered out — actual brand social icons may use custom colors
- Loading states and skeleton screens were not observed in the extraction
- Mobile navigation drawer (hamburger menu) styling details were not captured
- The #332fd0 accent blue appears on pre-order badges but its usage in other contexts (links, icons) is unconfirmed
- Font weights beyond 400, 600, 700 were not observed — Montserrat variable weight usage is assumed
- Letter-spacing values for display typography are estimated based on common metal/gothic label conventions
- The extracted hex list contains generic grays (#9ca3af, #ebebeb, #e7e7e7, #dedede, #cfcfcf) that may include Shopify default UI colors — the brand's true secondary palette may be more limited
