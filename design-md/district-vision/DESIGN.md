---
version: alpha
name: "District Vision"
source_url: "https://www.districtvision.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A running brand that uses a stark red (#e11f26) as its only color accent — not as a secondary highlight but as the primary signal, applied to CTAs, cart badges, and the single line of the brand mark. The palette is otherwise monochrome: near-black (#121212) for ink, a warm mid-gray (#dedede) for hairline borders and surface edges, and white canvas. This is a brand that refuses the gradient, the drop shadow, the decorative flourish — every component is flat, every corner is either hard ({rounded.none}) or fully pill-shaped ({rounded.full}), and every typographic decision prioritizes legibility over personality. The product grid uses a 2-column layout on desktop with generous {spacing.lg} gutters, each card showing a single studio-lit product image against white, with the price set in a condensed sans-serif at 14px. The top nav is a simple left-aligned logo with right-aligned utility links (Search, Account, Cart) — no mega-menu, no category dropdowns, no hero carousel. The brand's voice is direct and technical: product descriptions cite lens material, frame weight, and UV protection rating rather than lifestyle copy. The red badge on the cart icon uses a 10px pill with white text, the only place where the red appears at small scale. The checkout flow is Shopify-native with minimal customization, meaning the red primary bleeds into the standard Shopify Pay button — a pragmatic concession that the brand accepts rather than overrides.

colors:
  primary: "#e11f26"
  primary-active: "#b0181e"
  primary-disabled: "#f5a0a4"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#e11f26"
  success: "#2e7d32"
  badge-red: "#e11f26"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  product-price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  product-title:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.ink}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: 0 {spacing.lg}
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-item-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.product-title}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-price:
    typography: "{typography.product-price}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 40px
    border: none
  cart-icon-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    minWidth: 18px
    height: 18px
    padding: 0 4px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: 1px solid "{colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: 1px solid "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. A flat, hard-cornered red rectangle with white uppercase text at 14px/600. No hover shadow, no border radius — the brand's refusal of decoration is most visible here. On hover, the red deepens to `{colors.primary-active}` (#b0181e). Disabled state uses `{colors.primary-disabled}` (#f5a0a4) with no opacity change. Used for "Add to Cart", "Checkout", and "Subscribe" actions.

**`button-secondary`** — An outlined variant with a 1px black border on white background. Same uppercase typography and hard corners. Used for "View Details", "Continue Shopping", and secondary form actions. Hover state fills the background to `{colors.ink}` with white text.

**`button-tertiary-text`** — A text-only button with no background or border. Used for "Cancel", "Clear Filters", and inline actions. Hover state underlines the text.

**`button-pill-red`** — A pill-shaped red button used sparingly for promotional badges and sale indicators. Smaller typography (12px uppercase) with `{rounded.full}` corners. This is the only pill-shaped button in the system, reserved for temporary or promotional contexts.

### Navigation
**`nav-bar`** — A 60px fixed-height top bar with white background. The logo sits left-aligned, with navigation links right-aligned. No mega-menu, no dropdown — the nav is intentionally sparse. On scroll, a 1px `{colors.hairline}` bottom border appears. The cart icon includes a red pill badge (`{rounded.full}`) showing item count.

**`nav-link-item`** — Uppercase 13px/500 links with 8px horizontal padding. Active state uses `{colors.primary}` red for the text color. No underline or border indicator — the red text alone signals the current page.

### Product Cards
**`product-card`** — A minimal product display card with no border, no shadow, and no background color (white on white). The product image fills the full width with a `{colors.surface-soft}` placeholder background. Below the image, the product title appears in 14px regular weight, with the price in 14px medium weight below it. No ratings, no reviews, no color swatches — the brand trusts the product photography alone.

**`product-card-badge`** — A small red pill badge overlaid on the product image for "New", "Sale", or "Limited Edition" indicators. Uses 10px uppercase bold white text on `{colors.primary}` background.

### Forms
**`text-input`** — A hard-cornered input with a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.ink}` black. Error state uses `{colors.error}` red border. No rounded corners, no inset shadow, no label animation — the placeholder text serves as the label.

**`search-input`** — A borderless input on a `{colors.surface-soft}` gray background. Used in the search overlay and mobile search. No icon by default — the placeholder text reads "Search products...".

### Footer
**`footer-section`** — A full-width black (`{colors.ink}`) footer with white text. Links are set in `{colors.muted-soft}` gray and turn white on hover. The footer includes columns for "Shop", "About", "Support", and "Follow" (social links). No newsletter signup form — the footer is purely informational.

### Filters
**`filter-chip`** — A pill-shaped filter toggle with a 1px `{colors.hairline}` border and white background. Active state fills the chip with `{colors.ink}` black and white text. Used in collection pages for size, color, and category filtering.

### Dividers
**`divider`** — A 1px `{colors.hairline}` line used between sections and product rows. `divider-soft` uses `{colors.hairline-soft}` for less visual weight in secondary contexts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; filter chips stack vertically; hero section reduces padding to {spacing.lg}; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce font size to 11px; filter chips wrap in a horizontal row; hero section uses {spacing.xl} padding |
| Desktop | 1128–1440px | Two-column product grid with {spacing.lg} gutters; full nav links visible; filter chips in a single row; hero section at full {spacing.section} padding |
| Wide | > 1440px | Max-width container at 1440px centered; product grid remains two-column; all other layouts scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Nav links have 44px minimum tap area (padding extends touch zone)
- Filter chips have 36px minimum height with 44px tap area via padding
- Cart icon badge is positioned with 44px minimum touch radius around the icon

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid collapses from 2 columns to 1 column below 744px
- Filter chips collapse from horizontal row to vertical stack below 744px
- Footer columns collapse from 4 columns to 2 columns below 744px, then to single column below 480px
- Hero section reduces vertical padding from {spacing.section} to {spacing.lg} below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the system uses a generic sans-serif stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`) as a best-guess based on common Shopify running-brand choices. The actual brand may use a custom or licensed typeface.
- Hover and focus states for most components were inferred from common patterns rather than extracted from the live site.
- Error states for forms (validation messages, error icons) were not observed on the live site.
- The extracted hex list (#dedede, #e11f26, #ff0000, #121212) includes #ff0000 which appears to be a Shopify checkout widget default (Shopify Pay button) rather than a brand color. The brand's true primary is #e11f26.
- Dark mode is not supported and was not observed on the live site.
- Sub-brand or collection-specific color palettes (e.g., limited edition drops) were not observed.
- Loading states, skeleton screens, and empty states were not captured.
- The brand may use a custom icon set or SVG illustrations that were not extractable from the page source.
- Animation and transition timing values were not extractable.
