---
version: alpha
name: "Numskull (Geek Store)"
source_url: "https://www.geekstore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's paradise that announces itself with a single, unapologetic voltage: #ffff00, a high-frequency yellow that appears on every primary CTA, badge, and accent element across the site. This is not a muted, nostalgic geekdom — it's a loud, confident celebration of pop-culture fandom where the yellow acts as a visual handshake between the brand and its audience. The canvas is pure white (#ffffff), creating maximum contrast for the yellow to pop against product photography of collectible figures, statues, and apparel. Type runs Montserrat at moderate weights — display headlines sit at 28px weight 600, body copy at 14px, and the system trusts product imagery and generous whitespace over typographic hierarchy. Navigation is a clean, full-width white bar with a prominent search field, category dropdowns, and a cart icon — utility over decoration. Product cards use soft corners ({rounded.sm} ~8px) and a subtle hairline border (#dddddd) to contain the visual energy of the product images, while the yellow accent appears on "Add to Cart" buttons, sale badges, and limited-edition callouts. The overall mood is that of a well-lit convention floor — bright, organized, and buzzing with the excitement of discovery.

colors:
  primary: "#ffff00"
  primary-active: "#e6e600"
  primary-disabled: "#ffffb3"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#222222"
  badge-sale: "#ff0000"
  badge-new: "#00cc00"
  badge-limited: "#ffff00"
  star-rating: "#ffa500"
  link: "#0066cc"
  footer-bg: "#222222"
  footer-text: "#cccccc"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Montserrat', 'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.badge-sale}"

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
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  review-count:
    typography: "{typography.caption}"
    color: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature yellow (#ffff00) with dark text (#222222). Used for "Add to Cart", "Shop Now", and primary checkout actions. On hover, shifts to a slightly deeper yellow (#e6e600). Disabled state uses a pale yellow (#ffffb3) with muted text to signal inactivity without visual noise.

**`button-secondary`** — An outlined alternative for less prominent actions like "View Details" or "Wishlist". Uses a white background with a thin hairline border (#dddddd) and dark text. Active state fills the background with a soft gray (#f5f5f5) and darkens the border to ink (#222222).

**`button-text`** — A minimal, borderless button for tertiary actions such as "Cancel" or "Clear Filters". Relies entirely on typography and spacing, with no background or border, keeping the visual hierarchy clean.

**`button-icon`** — A circular icon button (40x40px) for utility actions like search, cart, or menu toggle. Transparent background with a dark icon, expanding to a full rounded shape on hover for better touch feedback.

### Cards
**`product-card`** — The primary product display unit. A white card with a soft border (#eeeeee) and 8px rounded corners. The product image occupies the top portion with matching corner radius, followed by the title and price in a stacked layout. On hover, the border darkens slightly and a subtle box shadow lifts the card, signaling interactivity.

**`product-card-image`** — The image container within a product card, using top-rounded corners to match the card shape. Designed for 1:1 or 4:5 aspect ratio product photography, with object-fit: cover to maintain consistency.

**`product-card-title`** — The product name, set in Montserrat 14px weight 500 with 8px horizontal padding and 8px top padding. Truncated to two lines for grid consistency.

**`product-card-price`** — The price display, set in Montserrat 16px weight 700. Sale prices render in red (#ff0000) to draw immediate attention, while regular prices remain in ink (#222222).

### Badges
**`badge-sale`** — A small, high-contrast red badge (#ff0000) with white text, positioned at the top-left corner of product images. Uses uppercase 11px weight 700 type with 0.5px letter spacing for maximum readability at small sizes.

**`badge-new`** — A green badge (#00cc00) for newly arrived products. Same typographic treatment as the sale badge, but communicates freshness rather than discount.

**`badge-limited`** — A yellow badge (#ffff00) with dark text for limited-edition or exclusive items. Matches the brand's primary color, creating a visual link between the badge and the brand identity.

### Navigation
**`nav-bar`** — A full-width white navigation bar (64px height) with a thin bottom border (#eeeeee). Contains the brand logo on the left, category links in the center, and utility icons (search, account, cart) on the right. Sticky on desktop, collapsing to a hamburger menu on mobile.

**`nav-dropdown`** — A white dropdown panel for category navigation, appearing on hover or click of nav links. Uses 8px vertical padding for link spacing and soft rounded corners for a polished feel.

**`search-bar`** — A pill-shaped search field (40px height) with a soft gray background (#f5f5f5) and thin border. On focus, the border switches to ink (#222222) for clear visual feedback. Placeholder text guides the user to search by product, brand, or character.

**`category-chip`** — A pill-shaped filter chip for browsing by category (e.g., "Marvel", "Star Wars", "Gaming"). Uses a soft gray background with dark text. Active state inverts to a dark chip with white text, clearly indicating the current filter.

### Forms
**`text-input`** — A standard text input for forms (address, payment, search filters). White background with a hairline border (#dddddd) and 8px rounded corners. Focus state darkens the border to ink. Error state switches to red (#ff0000) border for clear validation feedback.

**`quantity-selector`** — A compact input for adjusting product quantities in the cart. Uses a bordered container with increment/decrement buttons on either side and the current quantity displayed in the center. Designed for quick, precise adjustments.

### Footer
**`footer`** — A dark footer section (#222222) with light gray text (#cccccc). Contains brand information, customer service links, social media icons, and legal text. Links lighten to white on hover for clear interactivity. Uses generous vertical padding (48px) to create breathing room against the dark background.

### Hero
**`hero-banner`** — A full-width promotional banner at the top of the homepage or category pages. Uses a soft gray background (#f5f5f5) with large display type and a prominent yellow CTA button. Designed to feature new collections, exclusive drops, or seasonal sales with high visual impact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; hamburger menu replaces nav links; product cards stack vertically; hero banner reduces to 32px padding; search bar collapses to icon-only; category chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar full width in header; category chips in a scrollable strip; hero banner maintains 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with dropdowns; search bar in header; category chips in a grid layout; hero banner at full padding (64px) |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; nav bar expands with additional utility links; hero banner may include larger imagery |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain a minimum 44x44px touch target on mobile
- Icon buttons (search, cart, menu) are 40x40px with 4px padding for comfortable tapping
- Category chips are 32px tall with 16px horizontal padding, exceeding the 44px minimum on one axis
- Quantity selector buttons are 36x36px, slightly below ideal but compensated by generous spacing between controls

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px, with the menu panel sliding in from the left
- Product grid reduces from 4 columns (wide) to 1 column (mobile), with images scaling proportionally
- Category filter chips transition from a visible grid to a horizontally scrollable strip on mobile
- Hero banner text and CTA stack vertically on mobile, with the CTA button expanding to full width
- Footer links collapse into accordion-style sections on mobile, with expandable categories to save vertical space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- Extracted color palette is minimal (only #ffff00 and #ffffff from the live site analysis); additional colors (ink, muted, badge colors, footer colors) are inferred from common e-commerce patterns and may not match the exact live site values
- Font-family declarations found include Montserrat, Roboto, arial, monospace, sans-serif — Montserrat is assumed as the primary display font based on common usage in the collectibles space, but the exact hierarchy (weights, sizes, letter-spacing) is estimated from typical implementations
- Hover states for buttons and cards are inferred from common patterns; exact transitions, box shadows, and color shifts may differ on the live site
- Error states for forms (colors, icons, message placement) are not extracted and use standard red (#ff0000) as a placeholder
- Dark mode is not supported by the extracted data; the site appears to use a light-only theme
- Sub-brand or collection-specific color palettes (e.g., for Marvel vs. Star Wars categories) are not captured
- Typography scale (font sizes, line heights, letter-spacing) is estimated from the extracted font families and common e-commerce patterns; exact values may vary
- Spacing scale is a standard 4px/8px system; the live site may use a different base unit
- Component heights and padding values are estimated from typical implementations and may not match the live site exactly
- The extracted hex list may include checkout-widget colors (Shopify Pay, Klarna, Afterpay) that were not fully filtered; the primary yellow (#ffff00) is the most distinctive brand color in the list and is used as the primary accent
