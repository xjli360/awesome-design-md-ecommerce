---
version: alpha
name: "Durston Gear"
source_url: "https://durstongear.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-teal (#108474) spine runs through a site that sells ultralight backpacking tents and cookware to people who count every gram — the brand’s primary voltage appears in the header background, the add-to-cart button, and the footer, while a secondary teal (#579787) softens secondary buttons and informational banners. The canvas is a clean, near-white (#f9fafb) that shifts to a slightly warmer off-white (#f9f9f9) on product cards, giving the grid a subtle layered feel without introducing hard contrast. Accent yellow (#fbcd0a) appears sparingly — on sale badges and small callout tags — like a single reflective patch on an otherwise muted pack. Typography runs Nunito Sans for body and headings, set at modest weights (400–600) with generous line heights; the brand trusts product photography and spec tables over decorative type. Borders are thin and soft: hairline (#dedede) on cards, a slightly lighter hairline-soft (#e9e9e9) on input fields, and a muted gray (#7b7b7b) for secondary text that avoids the harshness of pure black. The overall mood is technical but not cold — the teal brings an outdoor, water-source freshness, and the rounded corners (8px on buttons, 12px on cards) keep the interface approachable for a gear audience that might be reading specs on a phone at a trailhead.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#8dcfc4"
  ink: "#121212"
  body: "#272727"
  muted: "#555555"
  muted-soft: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-teal-light: "#c1e6e6"
  accent-teal-mid: "#579787"
  accent-teal-bg: "#edf5f5"
  star-rating: "#fbcd0a"
  error: "#c13515"
  success: "#108474"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
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
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.accent-teal-mid}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "#4a7a6e"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-outline-active:
    backgroundColor: "{colors.accent-teal-bg}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 12px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.error}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 36px 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(16,132,116,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-alt:
    backgroundColor: "{colors.accent-teal-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.md}"
  section-subheading:
    typography: "{typography.title-md}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    textColor: "{colors.on-primary}"
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-teal-light}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  breadcrumb-active:
    textColor: "{colors.body}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
    padding: "0 12px"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 44px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  cart-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and primary form submissions. Rendered in the brand teal (#108474) with white text and 8px rounded corners. On hover, shifts to a darker teal (#0d6b5e). Disabled state uses a muted teal (#8dcfc4) with white text. **`button-secondary`** — A secondary action button in the mid-teal (#579787), used for "View Details", "Learn More", and secondary checkout flows. Same shape and padding as primary but a lighter teal to create visual hierarchy without introducing a new color. **`button-outline`** — An outlined variant with a 2px teal border on a transparent background, used for "Compare" and "Wishlist" actions. On hover, fills with a light teal background (#edf5f5). **`button-ghost`** — A text-only button with no border or background, used for "Cancel", "Clear Filters", and inline actions within cards.

### Cards
**`product-card`** — The primary product display container, a white card with a 1px hairline border (#dedede) and 12px rounded corners. The product image sits flush to the top corners (rounded top, square bottom). Title uses title-sm, price uses the price token at 20px bold. On hover, the card gains a teal border and a subtle box-shadow. **`product-card-badge`** — A small yellow (#fbcd0a) badge with uppercase bold text, positioned at the top-left of the product image. Used for "Sale" or "New" indicators. **`product-card-sold-out`** — A gray badge (#555555) with white text for sold-out items, same shape and position as the sale badge.

### Navigation
**`nav-bar`** — A fixed top navigation bar in solid teal (#108474) at 64px height. Logo and navigation links are white. On scroll, the bar compresses to 56px. **`nav-link`** — White text links with 8px horizontal padding. Active state has a semi-transparent white background (15% opacity) with 8px rounded corners. The mobile hamburger icon is also white.

### Forms
**`text-input`** — Standard text input with a white background, 1px hairline border, 8px rounded corners, and 44px height. On focus, the border thickens to 2px teal. Error state uses a 2px red (#c13515) border. **`select-input`** — Same base styling as text-input but with a 36px right padding to accommodate a custom dropdown arrow. **`quantity-selector`** — A compact input for product quantities, matching the text-input shape but typically used at smaller widths (60-80px).

### Footer
**`footer`** — A full-width teal (#108474) footer with white text at 14px. Links are white at 85% opacity, increasing to full opacity on hover. Section headings use title-sm (16px, 600 weight). Padding is 48px vertical, 24px horizontal.

### Badges & Indicators
**`badge-sale`** — Yellow (#fbcd0a) badge with dark text, 4px rounded corners, 2px vertical and 8px horizontal padding. Used on product cards and collection pages. **`badge-new`** — Light teal (#c1e6e6) badge with dark teal text, same shape. **`badge-sold-out`** — Gray (#555555) badge with white text. **`cart-badge`** — A circular yellow badge (20px diameter) with dark text, positioned on the cart icon in the navigation.

### Content Sections
**`hero-section`** — A teal-background hero area using display-xl (32px, bold) for the headline, with 64px vertical padding. Used for collection headers and promotional banners. **`hero-section-alt`** — A light teal (#edf5f5) background variant with dark text, used for informational sections like "Why Ultralight" or brand stories. **`accordion-header`** — A light gray (#f9f9f9) header with 12px padding, 8px rounded corners, used for product description accordions and FAQ sections. **`spec-table-row`** — A bordered row with a soft hairline (#e9e9e9) bottom border, containing a bold uppercase label and a regular value. Used extensively on product detail pages for weight, dimensions, materials.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 32px; product cards stack full-width; accordions always open; spec tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 48px padding; product cards in 2-column grid; accordions collapsible |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 64px padding; product cards in 3-column grid; side-by-side spec tables on product pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero centered with max-width; product cards in 4-column grid; additional whitespace on product detail pages |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 44px tap area (padding extends beyond visible text)
- Product card tap targets (title, image, button) minimum 48px
- Quantity selector buttons minimum 44px
- Accordion headers minimum 48px tap area
- Cart icon badge minimum 44px tap area

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button that opens a drawer on mobile
- Product description and specs collapse into accordions below 744px
- Footer columns stack vertically on mobile (single column)
- Hero content stacks (image below text) on mobile
- Product image gallery switches from row to swipeable carousel on mobile
- Breadcrumbs truncate to show only "Home > Current Page" on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all interactive elements could not be fully extracted; primary and secondary button hover states are inferred from common patterns
- Error state styling for forms (red borders, error messages) is assumed from common e-commerce patterns; exact error message typography and spacing not confirmed
- Dark mode is not supported on the live site; no dark mode tokens exist
- Sub-brand or collection-specific color variations (e.g., limited edition colors) not captured
- The extracted font list includes JudgemeIcons and JudgemeStar (review widget fonts) which are not part of the brand's typography system
- Social icon colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1, #fffb00) are platform defaults, not brand colors
- The extracted hex list contains several near-duplicate whites and grays (#f9fafb, #f9f9f9, #fafafa, #f2f2f2, #eeeeee, #e9e9e9, #dadada) — the most frequently occurring values were selected for the palette
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted list but are not part of the brand design system
- Animation durations, easing curves, and transition properties not extracted
- Loading states, skeleton screens, and empty state designs not documented
- Print stylesheet behavior not verified
- Accessibility contrast ratios between text and background colors not verified against WCAG standards
