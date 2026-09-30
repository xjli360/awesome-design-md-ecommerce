---
version: alpha
name: "iam8bit"
source_url: "https://www.iam8bit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A hot-pink #e01a78 voltage runs through an otherwise black-and-white indie merchandise store, where the brand's signature color appears as a primary CTA button, a navigation accent, and a limited-edition vinyl variant badge. The site reads like a gallery catalog for gaming artifacts — products float on a pure white canvas (#ffffff) with generous whitespace, while product cards use a near-black #0c0c0c for product titles and a softer #121212 for body text, creating a high-contrast editorial feel. Montserrat in medium weights (500–600) handles all typography, from 28px display headlines to 11px badge labels, with no serif or script relief — the brand trusts its product photography and the single pink accent to provide all the personality. Product cards use soft 8px rounding ({rounded.sm}) and a hairline #dedede border, while the primary CTA button takes the full pink treatment with white text, 12px rounding, and a 48px height that feels substantial without being aggressive. The navigation bar is a simple white strip with black links and a pink "Shop" highlight, and the footer collapses into a dense column of links and social icons on mobile. The overall effect is a merchandise store that treats its products like art objects — clean, restrained, with one deliberate pop of color that signals "this is the thing to click."

colors:
  primary: "#e01a78"
  primary-active: "#c01566"
  primary-disabled: "#f5a3c9"
  ink: "#0c0c0c"
  body: "#121212"
  muted: "#4a4a4a"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#e01a78"
  badge-sale: "#0c0c0c"
  star-rating: "#121212"
  social-icon: "#121212"
  footer-bg: "#0c0c0c"
  footer-text: "#dedede"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.md}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.md}"
    height: 40px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price-sale:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.badge}"
    textColor: "{colors.canvas}"
    letterSpacing: "1px"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  social-icon-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.md}"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.md}"
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.md}"
    height: 48px
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.md}"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "2px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
  pagination-disabled:
    typography: "{typography.body-sm}"
    textColor: "{colors.hairline}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  toast-success:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  toast-error:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  modal-overlay:
    backgroundColor: "rgba(12, 12, 12, 0.6)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 560px
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-chip-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  review-card-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  review-card-date:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.md} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  tooltip-arrow:
    color: "{colors.ink}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  slider-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  slider-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  slider-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "2px solid {colors.primary}"
  slider-thumb-hover:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "2px solid {colors.hairline}"
  table-cell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline}"
  table-row-hover:
    backgroundColor: "{colors.surface-soft}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-item-image:
    rounded: "{rounded.xs}"
    width: 80px
    height: 80px
  cart-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  cart-item-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  cart-item-remove:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  cart-summary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  cart-summary-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature hot pink #e01a78 with white uppercase Montserrat text. On hover, the background shifts to a slightly deeper pink (#c01566). The disabled state uses a washed-out pink (#f5a3c9) to signal inactivity while maintaining brand color recognition. All primary buttons use 12px rounding ({rounded.md}) and 48px height for a substantial, clickable feel.

**`button-secondary`** — An outlined alternative with a white background, black text, and a 2px black border. The active state adds a light gray (#f5f5f5) background fill. This button is used for "View Details" or "Learn More" actions where the primary pink would compete with other page elements.

**`button-tertiary-text`** — A text-only button in the brand pink, used for inline actions like "Clear filters" or "Cancel." No background or border — just the pink text with uppercase Montserrat styling.

**`button-pill-primary`** — A smaller, fully rounded pill button in the brand pink, used for filter chips, tag actions, or compact CTAs in product cards. Uses 36px height and 10px horizontal padding.

**`button-pill-outline`** — An outlined pill button with a transparent background, black text, and a 1px hairline border. Used for secondary filter chips or "Add to wishlist" actions.

### Cards
**`product-card`** — The primary product display unit, a white card with an 8px rounding ({rounded.sm}) and a 1px hairline border (#dedede). Contains a square product image with 4px rounding, a product title in 14px/500 Montserrat, a price in 14px/400, and optional badges. On hover, the border shifts to the brand pink and a subtle box shadow appears.

**`product-card-badge`** — A small uppercase label in the brand pink with white text, used for "NEW" or "EXCLUSIVE" indicators. Uses 4px rounding and tight 2px/8px padding.

**`product-card-badge-sale`** — A black badge with white text for sale or discount indicators. Same sizing as the standard badge but inverted color scheme.

**`review-card`** — A white card with a hairline border and 8px rounding, containing the review text, author name in 14px/600, and a date in 12px/400. Star ratings use a 16px black star icon with gray (#dedede) empty stars.

### Navigation
**`top-nav`** — A 72px white navigation bar with uppercase Montserrat links in 14px/500. The active link (typically "Shop") renders in the brand pink (#e01a78). The nav includes a logo on the left, links in the center, and a search icon + cart icon on the right. On mobile, the nav collapses into a hamburger menu.

**`nav-link-active`** — Active navigation link in brand pink. No background, just the color change.

**`nav-link-inactive`** — Inactive navigation link in black (#0c0c0c). Hover state transitions to a darker gray.

### Forms
**`text-input`** — A standard text input with a white background, 12px padding, 48px height, and a 1px hairline border. On focus, the border becomes a 2px brand pink line. Error state also uses a 2px pink border.

**`select-dropdown`** — A styled select element matching the text input dimensions and border treatment. Uses a custom dropdown arrow in the brand pink.

**`checkbox`** — A 4px rounded square with a 2px hairline border. When checked, the background fills with brand pink and a white checkmark appears.

**`radio`** — A fully rounded radio button with a 2px hairline border. When selected, the border turns brand pink and a pink dot appears in the center.

**`toggle`** — A 44px wide, 24px tall pill-shaped toggle with a gray background. When active, the background fills with brand pink and the circular thumb slides to the right.

**`quantity-selector`** — A compact input group with minus, number, and plus buttons. Uses 40px height, 8px padding, and a 1px hairline border. The number field is centered and editable.

### Search
**`search-bar`** — A compact search input with a light gray (#f5f5f5) background, 40px height, and 8px rounding. On focus, the background turns white and the border becomes a 2px brand pink line. Includes a magnifying glass icon in the muted gray (#8a8a8a).

### Footer
**`footer`** — A full-width black (#0c0c0c) footer with light gray (#dedede) text. Contains columns for "Shop," "Support," "About," and "Connect," each with an uppercase heading in 10px/700 with 1px letter spacing. Social media icons are 32px circles that turn pink on hover. The footer includes a newsletter signup form with a white text input and a pink submit button.

### Badges
**`badge-new`** — Pink badge for new arrivals.
**`badge-sale`** — Black badge for sale items.
**`badge-limited`** — Pink badge with tighter micro-label typography for limited edition items.
**`badge-preorder`** — Black badge with micro-label typography for pre-order items.

### Category Chips
**`category-chip`** — A fully rounded pill chip with a light gray background and body-colored text. Active chips invert to black background with white text. Hover state uses a slightly darker gray (#dedede) background.

### Modal
**`modal-overlay`** — A semi-transparent black overlay (60% opacity) that covers the viewport.
**`modal-content`** — A white modal container with 12px rounding, 32px padding, and a max width of 560px. Includes a close button in the top-right corner — a 32px light gray circle with a black X icon.

### Loading & Feedback
**`loading-spinner`** — A 24px spinning circle in the brand pink.
**`toast-success`** — A black toast notification with white text, 8px rounding, and 16px/24px padding.
**`toast-error`** — A pink toast notification with white text, same sizing as success.

### Cart & Checkout
**`cart-item`** — A row layout with an 80px square product image (4px rounding), title in 14px/600, price in 16px/400, and a remove link in 13px/500 muted gray. Items are separated by a 1px hairline border.

**`cart-summary`** — A light gray (#f5f5f5) container with 12px rounding and 24px padding, showing subtotal, shipping, and total. The total uses 16px/600 Montserrat.

**`checkout-button`** — A full-width primary button (pink background, white text, uppercase) for the checkout action. Same 48px height and 12px rounding as the standard primary button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 columns), hamburger menu replaces top nav, search bar moves to a collapsible panel, footer stacks vertically, hero banner reduces to 250px min-height, product card padding reduces to 12px |
| Tablet | 744–1128px | Two-column product grid, top nav shows all links but with reduced padding, search bar remains visible but compact, footer shows 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, search bar at full width, footer shows 4-column layout, hero banner at 400px min-height |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero banner expands to full viewport width with max-height 500px |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Category chips and pill buttons use 32px minimum height with 16px horizontal padding
- Product card images maintain a 1:1 aspect ratio for consistent tap targets
- Search bar and text inputs use 48px height for comfortable touch interaction
- Cart item remove links include a minimum 44px tap area even though the text is smaller
- Social media icons in the footer use 32px circles with 44px touch targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), with the logo centered and cart icon remaining visible
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 (desktop) to 2 (tablet) to a single stacked column (mobile)
- Search bar collapses to an icon on mobile, expanding to a full-width input when tapped
- Category filter chips collapse to a horizontal scrollable strip on mobile
- Hero banner text and CTA stack vertically on mobile, with reduced padding
- Product card badges stack vertically on mobile if multiple badges are present
- Cart summary moves below cart items on mobile, rather than sitting in a sidebar
- Modal content uses full viewport width on mobile with reduced padding (16px instead of 32px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; exact transition durations and easing curves were not extracted
- Focus ring styles (color, width, offset) for keyboard navigation were not observed
- Error message styling for form validation (color, icon, position) was not extracted
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or collection-specific color palettes (e.g., limited edition vinyl variants) were not captured
- The exact font weight for Montserrat used in headings vs. body text is inferred from common usage; the site may use additional weights
- Animation and transition specifications (duration, easing, stagger) for page loads, card reveals, and modal openings were not extracted
- The extracted hex colors (#e01a78, #dedede, #0c0c0c, #121212) are limited to four values; additional colors for success, warning, error, and info states were not found
- Shopify checkout page styling (Shopify Pay button, cart drawer, address forms) uses platform defaults and may not match the brand's custom design system
- The site may use a secondary accent color for specific product categories or promotions that was not captured in the extraction
- Print stylesheet specifications were not available
- Accessibility compliance details (contrast ratios, ARIA labels, skip navigation) were not extracted
- The exact spacing scale used in production may differ from the inferred values; padding and margin values are based on common e-commerce patterns
- Image aspect ratios for hero banners, collection pages, and product detail pages were not consistently extracted
- The brand's logo SVG or specific typographic treatment for the "iam8bit" wordmark was not captured
- Social media icon colors and hover states are inferred; exact brand guidelines for social assets were not available
