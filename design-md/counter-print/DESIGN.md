---
version: alpha
name: "Counter-Print"
source_url: "https://www.counter-print.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A London-based publisher of graphic design books and zines that uses a single red stroke — #c00000 — as its only color accent, applied sparingly against a near-black ink (#111111) and a spectrum of warm grays (#989898, #dedede, #c6c4c4). The site reads like a printed catalog: a white canvas (#ffffff) holds a grid of book covers at equal weight, each thumbnail a miniature poster. There is no hero image, no carousel, no full-bleed photography — the covers are the content, arranged in a disciplined three-column layout that trusts the reader to browse. The primary navigation is a thin horizontal bar with dropdowns that appear on hover, using the same red as the only highlight. Search is a simple text input with a red border on focus, not a pill or an orb. The checkout flow, powered by Shopify, introduces a secondary gray palette (#e6e6e6 for surfaces, #121212 for text) that feels slightly detached from the editorial front end — a known tension between the brand's print-shop identity and the ecommerce platform it runs on. Buttons are rectangular with {rounded.xs} corners, filled in red for primary actions and outlined in gray for secondary. The overall mood is that of a small press: confident in its restraint, letting the work — the books themselves — do the selling.

colors:
  primary: "#c00000"
  primary-active: "#a00000"
  primary-disabled: "#e6a0a0"
  ink: "#111111"
  body: "#121212"
  muted: "#989898"
  muted-soft: "#c6c4c4"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  checkout-surface: "#e6e6e6"
  checkout-text: "#121212"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
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
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
  button-secondary-disabled:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  nav-dropdown-item:
    padding: 8px 24px
    typography: "{typography.body-sm}"
  nav-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
  cart-item:
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The single call-to-action in the system, filled with #c00000 red and white uppercase text. Used for "Add to Cart", "Checkout", and "Subscribe". On hover, darkens to #a00000. Disabled state uses a washed-out red (#e6a0a0) with white text. The button has minimal 4px rounding ({rounded.xs}), keeping it rectangular and print-like.

**`button-secondary`** — An outlined button with a transparent background, #111111 text, and a 1px solid #dedede border. Used for "View Details", "Continue Shopping", and secondary actions. On hover, gains a light gray background (#f5f5f5) and a darker border (#989898). Disabled state fades to #c6c4c4 text and border.

**`button-ghost`** — A text-only button with no background or border, using smaller uppercase type (12px). Used for "Clear Filters", "Cancel", and inline actions within dropdowns or modals.

### Navigation
**`nav-bar`** — A 64px white bar with a thin bottom border (#dedede). The logo sits left-aligned, navigation links are center-aligned (or right-aligned on mobile). Links use 14px uppercase type with 0.3px letter spacing. The active page or hover state is indicated by the #c00000 red applied to the link text.

**`nav-dropdown`** — Appears on hover over parent nav items. A white panel with no rounding, an 8px vertical padding, and a subtle box shadow. Each item has 8px vertical padding and 24px horizontal padding. Hover state adds a light gray background (#f5f5f5). No red is used in dropdowns — the system reserves red for primary actions and badges.

### Product Cards
**`product-card`** — A simple container with no background color (inherits white from the page) and no rounding. The book cover image sits at full width, with the title below in 16px medium weight and the price in 16px medium weight in #989898 gray. Cards are arranged in a 3-column grid on desktop, 2-column on tablet, and single-column on mobile. There is no border, no shadow, no hover lift — the cover art provides all the visual interest.

**`product-card-badge`** — A small red label with white uppercase text, used for "New", "Sale", or "Signed Edition". Positioned absolutely over the top-left corner of the product image. The badge has 4px rounding and minimal padding (2px top/bottom, 8px left/right).

### Forms & Inputs
**`text-input`** — A standard text input with a 1px #dedede border, 44px height, and 10px/14px padding. On focus, the border turns red (#c00000) with a matching box-shadow ring. Error state also uses the red border. Used for search, newsletter signup, and checkout fields.

**`search-input`** — Identical to `text-input` in styling but used specifically in the search context. The search icon is placed inside the input on the left, and a red "X" clear button appears on the right when text is entered.

### Footer
**`footer`** — A dark section with #111111 background and white text. Links are in #c6c4c4 gray and turn white on hover. The footer contains three columns: "About", "Customer Service", and "Social/Newsletter". The newsletter signup uses a white input with a red submit button. Social icons are rendered in white with no background.

### Cart & Checkout
**`cart-item`** — Each line item in the cart has 16px vertical padding and a thin bottom border (#dedede). The product image is 80px square, with title, price, and quantity selector to the right. The quantity selector is a 44px tall input with a 1px border, styled like `text-input`.

**`checkout-button`** — A full-width primary button used at the bottom of the cart and checkout pages. Identical to `button-primary` in styling but spans the container width.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; footer stacks vertically; search becomes full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but may wrap; footer remains three-column |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav; standard layout |
| Wide | > 1440px | Max-width container at 1440px; product grid may expand to 4 columns if content allows |

### Touch Targets
- All buttons and links have a minimum height of 44px to meet WCAG touch target recommendations.
- Nav dropdown items have 8px vertical padding, making each item at least 30px tall — acceptable for touch but could be increased to 44px on mobile.
- Product card images are tappable and link to product pages; no minimum size enforced beyond the image itself.
- Quantity selector buttons (+/-) are 44px × 44px to ensure easy tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The hamburger icon is red (#c00000) on white.
- The search bar collapses from a visible input in the nav to a search icon that expands on tap.
- The product grid collapses from 3 columns to 2 columns on tablet, and to 1 column on mobile.
- The footer collapses from 3 columns to a single stacked column on mobile.
- Dropdown menus in the nav are replaced by expandable accordion sections on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The system uses a Helvetica Neue / Arial fallback stack as a reasonable default for a print-focused publisher, but the actual brand typeface (if any) is unknown.
- Hover states for buttons and links were inferred from common patterns; exact extracted values are unavailable.
- Error states for form inputs (beyond the red border) are not documented — no error message styling, iconography, or animation data was extracted.
- The checkout flow uses Shopify's default styling for payment widgets (Shopify Pay, Klarna, Afterpay), which may introduce colors (#e6e6e6, #121212) that are not part of the Counter-Print brand system. These are noted in the palette as `checkout-surface` and `checkout-text` but should be reviewed.
- Dark mode is not supported and no dark mode tokens exist.
- No sub-brand or seasonal palette variations were detected.
- The extracted hex list is dominated by grays and one red (#c00000). The red is distinctive and is used as the primary brand color. However, the grays (#989898, #dedede, #c6c4c4, #e6e6e6, #121212) form a cohesive neutral palette that may have intentional hierarchy — the exact usage rules (which gray for what context) were not fully extracted.
- No animation or transition timing data was extracted (hover transitions, page load animations, etc.).
- The site uses Shopify as a platform; some UI elements (cart drawer, checkout pages) may inherit Shopify's default styling rather than custom brand tokens.
