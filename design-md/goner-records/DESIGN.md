---
version: alpha
name: "Goner Records"
source_url: "https://goner-records.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Memphis institution that wears its red like a bloodstain on a white t-shirt — #d1171c is the meta-theme-color and the brand's primary voltage, a stop-sign red that appears on the site's header, cart badge, and checkout buttons, while #eb001b and #f00036 pulse as accent variations across sale tags and limited-edition banners. The palette is a chaotic archive of payment-gateway blues (#006fcf, #3086c8, #003087) and Klarna pinks (#ff5f00, #f79e1b) that the Shopify backend drags in, but the brand's own voice lives in the near-black #231f20 for body text and the pure #111111 for headlines, with #dedede as the sole gray for dividers and muted backgrounds. No custom font declarations were extracted — the site likely falls back to system sans-serif stacks (Helvetica, Arial), a deliberate punk austerity that prioritizes album art and raw product photography over typographic polish. Product cards use sharp right angles ({rounded.none}) for vinyl sleeves and cassette cases, while the cart and checkout flow introduce soft pills ({rounded.full}) for quantity selectors and add-to-cart buttons, a pragmatic concession to e-commerce usability. The header is a minimal black bar with white text, the red logo mark, and a search icon — no mega-menu, no category strip, just the records and the noise.

colors:
  primary: "#d1171c"
  primary-active: "#a81216"
  primary-disabled: "#f0a0a2"
  ink: "#111111"
  body: "#231f20"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#eb001b"
  accent-new: "#f00036"
  accent-limited: "#f37521"
  payment-blue: "#006fcf"
  payment-green: "#17d13e"
  header-bg: "#111111"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
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
    border: "1px solid {colors.muted}"
  button-pill-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-cart-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-sale}"
  nav-bar:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.base}"
  nav-link:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Subscribe". Rendered as a solid red rectangle with white text, using `{colors.primary}` (#d1171c) as background. On hover, it shifts to `{colors.primary-active}` (#a81216). The disabled state uses `{colors.primary-disabled}` (#f0a0a2) with no border. Padding is 12px 24px with a height of 44px and `{rounded.sm}` corners.

**`button-secondary`** — Used for "View Details", "Continue Shopping", and secondary form actions. A white button with a 1px `{colors.hairline}` border and `{colors.ink}` text. On hover, the background becomes `{colors.surface-soft}` and the border darkens to `{colors.muted}`. Same height and padding as the primary button.

**`button-pill-cart`** — A compact pill-shaped button used specifically in cart line items and mini-cart drawers. Smaller at 36px tall with `{rounded.full}` corners, `{colors.primary}` background, and `{colors.on-primary}` text. Active state mirrors the primary button's hover.

### Navigation
**`nav-bar`** — A fixed-height 56px black bar (`{colors.header-bg}`) spanning the full viewport width. Contains the Goner Records logo (red text or mark), a set of uppercase nav links, and a search icon. Links are white with `{colors.primary}` active state. No dropdown menus — the navigation is flat and minimal.

**`nav-link`** — Uppercase, 14px, weight 600, with 0.5px letter-spacing. Links are spaced with `{spacing.sm}` vertical and `{spacing.md}` horizontal padding. Active link uses `{colors.primary}`.

### Cards
**`product-card`** — A sharp-cornered (`{rounded.none}`) card with a 1:1 aspect ratio product image, title, price, and optional badge. The card has no border or shadow — it relies on the white background against `{colors.surface-soft}` or `{colors.canvas}`. Title uses `{typography.title-sm}`, price uses `{typography.price}` in `{colors.ink}`. Badges (e.g., "SALE", "NEW") are positioned at the top-left of the image, using `{colors.accent-sale}` or `{colors.accent-new}`.

**`product-card-badge`** — A small, sharp-cornered label overlaid on product images. Uses `{typography.badge}` (11px, weight 700, uppercase) with `{colors.accent-sale}` background and white text. Padding is 2px 6px.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. White background, `{colors.body}` text, 44px height, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`. Error state uses `{colors.accent-sale}` border.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) used in the header and mobile menu. 40px tall with 8px 16px padding, white background, and a 1px `{colors.hairline}` border. Focus state uses `{colors.primary}` border. No icon inside — the search icon is a separate element in the nav bar.

### Footer
**`footer`** — A black background (`{colors.header-bg}`) section with white text. Links are white and turn `{colors.primary}` on hover. Padding is `{spacing.xl}` top/bottom and `{spacing.base}` left/right. Contains store info, social links, and legal text in `{typography.body-sm}`.

### Hero
**`hero-banner`** — A full-width black section used on the homepage and collection pages. Contains a large headline (`{typography.display-xl}` in white) and a subtitle (`{typography.body-md}` in `{colors.muted-soft}`). Padding is `{spacing.section}` vertical and `{spacing.base}` horizontal. No background image — the hero is purely typographic.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero padding reduces to 32px; search bar moves to a full-width drawer; footer links stack vertically |
| Tablet | 744–1128px | Product cards display in 2–3 column grid; nav links remain visible but reduce font size to 12px; hero padding at 48px; search bar remains in header |
| Desktop | 1128–1440px | Product cards in 4-column grid; full nav link set visible; hero at full padding; search bar in header with expanded width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5-column grid; hero content centered with max-width 800px |

### Touch Targets
- All buttons and links have minimum 44px height and 44px width (or 44px tap area via padding)
- Nav links have 44px minimum tap height
- Quantity selector buttons in cart are 44px x 44px
- Search bar has 44px minimum tap height on mobile

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger icon; the full nav links appear in a slide-out drawer from the left
- Product card grids collapse from 4 columns to 2 columns (tablet) to 1 column (mobile)
- Footer links collapse from 4 columns to 2 columns (tablet) to 1 column (mobile)
- The search bar moves from the header to a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font-family declarations were extracted from the live site; the typography block uses a generic system sans-serif stack. The brand may use a custom font (e.g., a punk or gothic typeface) that is loaded via @font-face but not detectable from CSS extraction.
- Hover and focus states for many components (e.g., product card image zoom, footer link underline) could not be reliably extracted.
- Error state styling for forms (e.g., validation messages, error icons) is not confirmed.
- Dark mode styling is not present on the live site.
- The extracted color palette is heavily polluted with Shopify payment gateway colors (Klarna pink, PayPal blue, Afterpay green, etc.). The brand's true palette is likely smaller: #d1171c (primary red), #111111 (ink), #231f20 (body), #dedede (hairline), and #ffffff (canvas). The other colors should be treated as third-party imports.
- No sub-brand or seasonal palette data is available.
- Spacing values are estimated based on common e-commerce patterns; the exact values used by the brand may differ.
- The `hero-banner` component is inferred from the homepage design; the brand may use a different hero layout (e.g., with featured album art).
