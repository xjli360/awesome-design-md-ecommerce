---
version: alpha
name: "Amoeba Music"
source_url: "https://www.amoeba.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage yellow (#fff200) cuts through a dense, almost entirely gray-and-black palette — the single color that signals every add-to-cart button, sale badge, and genre tag across a site that sells movies, music, and pop-culture ephemera. The brand's visual system is built on contrast: a near-black ink (#202020) on a white canvas, with a secondary yellow (#fff000) used sparingly for urgency and price callouts. Red (#ed1c24) appears for sale markers and limited-time offers, while a deep purple (#36043c) surfaces in footer backgrounds and special-section headers, giving the site a record-store basement mood. Typography leans on system sans-serifs (Arial, Helvetica, Verdana) with two proprietary faces — standard0758Regular and standard0765Regular — used for display headers and product titles, suggesting a custom type system that hasn't been fully documented. Buttons are sharp-cornered rectangles with {rounded.sm} 4px radius, never pills — the brand avoids the friendly roundness of modern ecommerce in favor of a utilitarian, almost warehouse aesthetic. Product cards use a soft gray surface (#f3f3f3) with hairline borders (#d7d7d7), and the search bar sits as a full-width field rather than a compact icon, reflecting a catalog-heavy browsing experience. The overall effect is a digital storefront that feels like walking into a cavernous, fluorescent-lit record store: everything is legible, nothing is precious, and the yellow is the only thing that shouts.

colors:
  primary: "#fff200"
  primary-active: "#e6d900"
  primary-disabled: "#fff9b3"
  ink: "#202020"
  body: "#404040"
  muted: "#777777"
  muted-soft: "#a0a0a0"
  hairline: "#d7d7d7"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#202020"
  accent-red: "#ed1c24"
  accent-purple: "#36043c"
  accent-purple-light: "#411246"
  accent-blue: "#003399"
  accent-blue-light: "#133c9a"
  accent-green: "#327947"
  sale-yellow: "#fff000"
  dark-surface: "#0f0f0f"
  dark-muted: "#313131"
  dark-hairline: "#434343"

typography:
  display-xl:
    fontFamily: "'standard0765Regular', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'standard0765Regular', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'standard0758Regular', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'standard0758Regular', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-red-active:
    backgroundColor: "#c4161e"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px
    border: "2px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.muted}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-red}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-genre:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-genre-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(0,0,0,0.4)"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
  section-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0"
    borderBottom: "2px solid {colors.ink}"
  filter-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  footer-heading:
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
    letterSpacing: "1px"
  cart-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  cart-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 36px
    width: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature yellow (#fff200) with black text. Used for "Add to Cart," "Checkout," and primary form submissions. On hover, shifts to a slightly darker yellow (#e6d900). Disabled state uses a pale yellow (#fff9b3) with muted gray text. All buttons use uppercase, bold system sans-serif at 14px with 0.5px letter spacing.

**`button-secondary`** — An outlined variant with a 2px black border on white background. Used for secondary actions like "View Details" or "Save for Later." Active state fills with the soft surface gray (#f3f3f3). Height matches the primary button at 40px for alignment in forms.

**`button-accent-red`** — A red variant (#ed1c24) with white text, used exclusively for sale-related CTAs, limited-time offers, and destructive actions. Hover darkens to #c4161e. This button carries urgency and should be used sparingly.

**`button-ghost`** — A text-only button with no background or border, used for inline actions like "Clear Filters" or "Cancel." Maintains the same uppercase, bold typography as other buttons for visual consistency.

### Navigation
**`nav-bar`** — A 56px fixed-height bar with white background and a single 1px hairline bottom border. Navigation links are uppercase, bold, 14px with 0.3px letter spacing. The active link is indicated by a 3px yellow underline. On scroll, the nav gains a subtle box shadow. The bar contains the Amoeba logo (typically rendered in black or as an SVG), genre dropdowns, and the cart icon with badge.

**`nav-link`** — Inline navigation items with horizontal padding of 16px. Hover state fades to muted gray (#777777). Active state uses the yellow underline treatment. No rounded corners — the brand avoids pill-shaped navigation entirely.

### Cards
**`product-card`** — A rectangular card with a 1px hairline border and no border radius. Contains a product image on a soft gray background (#f3f3f3), followed by the title in 16px bold, and price in 16px bold. Sale prices render in red (#ed1c24). On hover, the card gains a subtle shadow and the border shifts to muted gray. Cards are designed for grid layouts with consistent aspect ratios for images.

**`badge-sale`** — A small red badge with white text, 2px horizontal padding, and a 2px border radius. Used to overlay on product images or sit next to prices. Text is 11px bold uppercase with 0.5px letter spacing.

**`badge-new`** — A yellow badge matching the primary brand color, used for new arrivals. Same dimensions and typography as the sale badge but communicates discovery rather than urgency.

**`badge-genre`** — A soft gray pill-shaped badge (8px radius) used for genre tags in filter bars and category strips. Active state inverts to black background with white text. These are the only elements that use a larger border radius, distinguishing them as interactive filters.

### Forms
**`text-input`** — A standard 40px input field with 1px hairline border and 4px radius. On focus, the border becomes 2px solid yellow. Error state uses a 2px red border. Placeholder text uses muted gray (#777777). Input text is 15px regular weight Arial.

**`search-bar`** — A full-width 48px search field with a 2px hairline border and 4px radius. Unlike modern ecommerce sites that use pill-shaped or icon-only search, Amoeba's search is a prominent text field with a magnifying glass icon inside. On focus, the border becomes 2px solid black. The search bar sits prominently at the top of the page, reflecting the catalog-heavy browsing experience.

**`filter-dropdown`** — A compact 36px dropdown with 1px hairline border and 4px radius. Used in filter bars for sorting by genre, format, price range, etc. The dropdown arrow is typically rendered as a custom SVG rather than the browser default.

### Footer
**`footer`** — A deep purple (#36043c) section with white text, spanning the full page width. Contains columns of links, social media icons, and the Amoeba newsletter signup. Footer links render at 80% opacity, increasing to full opacity on hover. Section headings use the primary yellow (#fff200) in uppercase with 1px letter spacing. The footer is one of the few places where the brand uses a colored background, creating a visual "basement" feel that contrasts with the white canvas above.

### Cart
**`cart-icon`** — A 32px yellow circle with a shopping bag or cart icon in black. The icon sits in the top navigation bar. When items are in the cart, a small red badge appears at the top-right corner showing the item count.

**`cart-badge`** — An 18px red circle with white text, positioned absolutely over the cart icon. Displays the number of items in the cart. Uses the same badge typography as other badges.

**`quantity-selector`** — A 36px horizontal control with a center text field and two square buttons on either side for incrementing/decrementing. The buttons use the soft surface gray (#f3f3f3) background. The entire control has a 1px hairline border and 4px radius.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), nav collapses to hamburger menu, search bar becomes collapsible, filter bar stacks vertically, footer columns stack |
| Tablet | 744–1128px | Two-column product grid, nav shows top-level links only (genres in dropdown), search bar remains full-width, filter bar uses horizontal scroll |
| Desktop | 1128–1440px | Three-to-four-column product grid, full nav with genre dropdowns, persistent search bar, multi-column footer |
| Wide | > 1440px | Four-to-five-column product grid, max-width container (1440px) for content, extended nav with sub-genre flyouts |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height on mobile
- Filter dropdowns and quantity selectors use 36px height (below 44px recommendation but consistent with desktop)
- Cart icon and nav hamburger are 44px minimum on mobile
- Product card images are tappable with a minimum 120px height

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px, with a slide-out drawer containing all links and genre categories
- Filter bar collapses to a single "Filter" button that opens a modal overlay on mobile
- Product grid reduces from 4 columns to 2 columns on tablet, 1 column on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Search bar collapses to an icon on mobile, expanding to full-width on tap
- Secondary navigation (breadcrumbs, sub-genre links) hides on mobile, accessible via the filter modal

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The proprietary fonts `standard0758Regular` and `standard0765Regular` could not be found in any public font repository; their exact weights, fallback behavior, and licensing are unknown. The system assumes they are custom web fonts loaded via @font-face, but the source URL is not documented.
- Hover and focus states for many components (especially in the footer and filter bar) are inferred from common patterns rather than extracted from the live site.
- Error states for forms (validation messages, error icons) are not documented in the extracted data.
- The extracted color list includes several blues (#003399, #133c9a, #146ff8, #a7bbfe) that may belong to third-party payment widgets (PayPal, Klarna) rather than the brand itself. These are included as accent tokens but should be verified.
- The purple palette (#36043c, #411246) appears in footer backgrounds but its usage in other contexts (badges, headers, hover states) is not confirmed.
- Dark mode is not supported; the site uses a white canvas with black text exclusively.
- The extracted font list includes `LasVegasOTJackpot` and `BurbankBigMedium`, which may be used in hero banners or promotional sections but their application context is unknown.
- Spacing values for specific components (padding inside product cards, margin between grid items) are estimated from common ecommerce patterns rather than measured from the live site.
- The hero banner component is inferred from the brand's visual identity; no hero banner was present in the extracted page data.
- Animation durations, easing curves, and transition properties are not documented.
