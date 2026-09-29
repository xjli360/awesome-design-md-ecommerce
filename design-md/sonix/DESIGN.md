---
version: alpha
name: "Sonix"
source_url: "https://www.shopsonix.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A pink that doesn't blush — #f3818b, #fd848d, and #e69392 form a three-note chord of coral-rose that runs through every product page, badge, and accent on a site that sells protective phone cases. The brand's visual identity is built on the tension between soft, almost cosmetic pastels and the hard, functional reality of drop protection and MagSafe alignment. A deep navy ink (#272d45) anchors the typography, while #444444 and #676986 handle body copy — the palette reads like a makeup compact designed by an industrial engineer. The extracted hex list is unusually long (30+ colors), suggesting heavy use of Shopify checkout widgets, social icons, and stock photography, but the core brand signal is unmistakable: a warm, feminine-leaning pink-navy combination that avoids both millennial pink's saccharine and luxury's austerity. Product cards use generous white space with rounded corners, and the navigation stays clean and minimal — the pink does the emotional work. The site runs on Shopify, which means the checkout flow inherits platform defaults, but the brand pages themselves feel curated, with soft dividers (#d3d3d3, #e5e5e5) and a light gray canvas (#f6f6f6) that keeps the pink accents from overwhelming. The extracted font stack is entirely system-level (monospace fallbacks, emoji fonts, widget icons), indicating no custom brand typeface — Sonix relies on weight and spacing rather than proprietary letterforms. The result is a DTC storefront that feels more like a beauty brand than an accessories brand, where the pink is the product and the case is just the canvas.

colors:
  primary: "#f3818b"
  primary-active: "#e69392"
  primary-disabled: "#feced1"
  ink: "#272d45"
  body: "#444444"
  muted: "#676986"
  muted-soft: "#d3d3d3"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#f6f6f6"
  surface-soft: "#faecec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#fd848d"
  accent-coral: "#e69392"
  navy-dark: "#272824"
  navy-mid: "#2c3e50"
  badge-red: "#fc0000"
  badge-yellow: "#f59e0b"
  badge-green: "#22c55e"
  badge-blue: "#38bdf8"
  badge-gold: "#f3e008"
  link-blue: "#1878b9"
  warm-bg: "#fffded"
  sage: "#6d888a"
  deep-red: "#630000"
  deep-gold: "#634004"
  deep-green: "#0b4320"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-outline-pink:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-outline-pink-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.badge-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sold-out-badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-accent:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    outline: none
  search-icon:
    color: "{colors.muted}"
    size: 18px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    fontWeight: 600
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    border: "2px solid {colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    height: 24px
    width: 24px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  review-stars:
    color: "{colors.badge-gold}"
    size: 16px
  review-stars-empty:
    color: "{colors.muted-soft}"
    size: 16px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  toast-success:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  toast-error:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  toast-info:
    backgroundColor: "{colors.link-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's coral-rose (#f3818b) and white text. Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, shifts to the deeper `{colors.primary-active}` (#e69392). Disabled state uses `{colors.primary-disabled}` (#feced1) — a pale pink that signals the button is present but non-interactive. The `{rounded.sm}` (8px) corners keep it friendly without being pill-like.
**`button-secondary`** — A white button with a thin `{colors.hairline}` border and navy ink text. Used for "Learn More", "View Details", and secondary actions alongside the primary. Active state fills the background with `{colors.surface-soft}` (#faecec) — a whisper of pink that echoes the brand accent without competing.
**`button-outline-pink`** — A transparent button with a 2px solid `{colors.primary}` border and pink text. Used for "Customize" or "Select Options" when the primary button is already occupied. Hover fills the background with `{colors.surface-soft}` and deepens the border to `{colors.primary-active}`.
**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for filter tags, category chips, and compact CTAs. Smaller padding and `{typography.button-sm}` keep it from overwhelming tight layouts.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.md}` (12px) corners and `{spacing.base}` padding. The product image sits at a 1:1 aspect ratio with `{rounded.sm}` (8px) corners. Title uses `{typography.title-sm}` in `{colors.ink}`, price uses `{typography.body-md}` in `{colors.body}` with 600 weight. On hover, a subtle `boxShadow` lifts the card. Badges (sale, new, sold out) overlay the image at the top-left with `{rounded.xs}` (4px) and `{typography.badge}` — the sale badge is `{colors.badge-red}` (#fc0000), the new badge is `{colors.primary}` (#f3818b), and sold out is `{colors.muted}` (#676986).

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 64px (56px when scrolled) with a white background and a thin `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` — 14px, 500 weight, uppercase with 0.5px letter spacing. Active links get `{colors.primary}` text and a 2px bottom border in the same pink. Inactive links are `{colors.muted}` (#676986). The sticky state adds a subtle `boxShadow` for depth. The nav typically includes the brand logo (left), product category links (center), and cart/search icons (right).

### Forms
**`text-input`** — Standard text input at 44px height with `{rounded.sm}` (8px), a `{colors.hairline}` border, and `{typography.body-md}`. Focus state swaps to a 2px `{colors.primary}` border with no outline. Error state uses a 1px `{colors.badge-red}` border. The `{colors.canvas}` background keeps it clean and readable.
**`select-input`** — Matches the text input in height, border, and rounding. Used for size, color, and quantity dropdowns. The dropdown arrow is typically `{colors.muted}`.
**`quantity-selector`** — A compact input group (40px height) with a central numeric display and two flanking `{rounded.xs}` buttons for increment/decrement. The buttons use `{colors.muted}` icons on transparent backgrounds.

### Footer
**`footer-section`** — A dark navy (`{colors.ink}`) footer with white text. Links use `{colors.muted-soft}` (#d3d3d3) and hover to `{colors.primary}`. Headings use `{typography.title-sm}` in white with 600 weight. The footer typically includes columns for customer service, about, shop, and social links, plus a copyright line at the bottom. Padding is `{spacing.xxl}` (48px) top and bottom.

### Badges & Indicators
**`product-card-badge`** — Small uppercase labels (11px, 700 weight, 0.5px tracking) with `{rounded.xs}` (4px) and 2px/8px padding. The brand uses three badge variants: new (pink `{colors.primary}`), sale (red `{colors.badge-red}`), and sold out (gray `{colors.muted}`). All use white text for contrast.
**`review-stars`** — Gold (`{colors.badge-gold}` #f3e008) 16px stars for filled ratings, `{colors.muted-soft}` (#d3d3d3) for empty. Typically shown as a row of 5 stars below the product title on cards and on the product detail page.

### Feedback & Utility
**`toast-success`** — Green (`{colors.badge-green}` #22c55e) notification bar with white text, `{rounded.sm}` (8px), and `{spacing.base}` padding. Used for "Added to Cart" confirmations.
**`toast-error`** — Red (`{colors.badge-red}` #fc0000) notification bar for errors like "Out of Stock" or payment failures.
**`toast-info`** — Blue (`{colors.link-blue}` #1878b9) notification bar for informational messages like "Free Shipping on Orders Over $50".
**`loading-spinner`** — A 24px spinning indicator in `{colors.primary}` (#f3818b), used during product loading, cart updates, and checkout transitions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces full nav links, product cards stack vertically, hero text reduces to `{typography.display-lg}`, footer collapses to single column, search bar moves to a slide-out panel |
| Tablet | 744–1128px | Two-column product grid, nav links shown but condensed (maybe 3-4 links), hero maintains `{typography.display-xl}` but with reduced padding, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav links displayed, hero at full width with `{spacing.section}` padding, footer uses 3-4 column layout, product cards show hover effects |
| Wide | > 1440px | Max-width container (1440px) centered, product grid can expand to 4 columns, hero may include background imagery, extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (cart, search, hamburger) are at least 44x44px with `{rounded.full}` for easy tapping
- Color swatches are 32x32px with a 36x36px selected state to provide adequate touch area
- Quantity selector buttons are 24x24px but sit within a 40px tall container
- Product card links have full-card tap targets on mobile (the entire card is clickable)

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px; the hamburger icon opens a full-screen or slide-out drawer
- Product filters (size, color, price) collapse into an accordion or a "Filter" button that opens a modal on mobile
- Footer columns collapse from 3-4 columns on desktop to a single stacked column on mobile
- Hero sections reduce padding and font size on mobile; background images may be cropped or replaced with simpler gradients
- Product image galleries switch from thumbnail grid to swipeable carousel on mobile
- Search bar collapses from a full-width input on desktop to an icon that expands on tap on mobile
- Accordion content (product descriptions, reviews, shipping info) is collapsed by default on all breakpoints, expanding on click

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface was extracted from the live site — the font stack is entirely system-level fallbacks. The typography tokens above use a generic system stack; a real brand font (if one exists) would need to be specified by the design team.
- Hover and focus states for many components (text-input, select-input, nav-links) are inferred from common ecommerce patterns rather than extracted from the live site. The extracted CSS did not include `:hover` or `:focus` pseudo-classes.
- Error state styling (form validation, 404 pages, empty cart) was not observed in the extraction. The error colors used (red borders, red toast) are best-guess implementations.
- Dark mode is not supported — the extracted palette is entirely light-mode. No dark-mode media queries or color overrides were found.
- The extracted hex list includes many colors that appear to be from third-party widgets (Shopify Pay buttons, Klarna badges, Afterpay logos, social media icons) rather than the brand's core palette. The primary pink (#f3818b) and navy (#272d45) are the most distinctive and likely brand-owned, but the full palette above includes several colors that may be widget-specific.
- No animation or transition tokens were extracted (durations, easing curves, keyframes). The design system would benefit from a defined motion language.
- The extracted font-family declarations include widget-specific fonts (oke-widget-icons) that are not part of the brand's typography system. These have been excluded from the typography block.
- No spacing or layout grid system was explicitly extracted — the spacing tokens above are based on common ecommerce patterns and the observed density of the site.
- No shadow/elevation tokens were extracted. The product-card hover shadow is an inferred value.
- No icon set or iconography guidelines were extracted. The search-icon size is an estimate.
- No loading state patterns beyond the spinner were observed (skeleton screens, shimmer effects).
