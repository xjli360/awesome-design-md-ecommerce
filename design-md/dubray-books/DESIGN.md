---
version: alpha
name: "Dubray Books"
source_url: "https://www.dubraybooks.ie"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy canvas (#00205b) anchors Dubray Books — not as a background but as the brand's primary voltage, appearing on the top navigation bar, footer blocks, and the site's meta-theme-color strip, lending a studious, grounded presence that sets it apart from the pastel-and-white conventions of most independent bookstores. Against this dark ink, a seafoam accent (#70c8b5) surfaces on hover states, sale badges, and secondary decorative elements, while a sharp coral (#ef7b3d) and a vivid orange (#fb681c) provide energetic call-to-action pulses for "Add to Basket" buttons and promotional banners. The typography runs Poppins at moderate weights — display headlines sit at 500–600 weight rather than heavy 700+, letting the book cover photography and generous whitespace carry the visual load rather than typographic muscle. Search bars adopt a softly rounded rectangle (`{rounded.sm}`), while product cards use a gentle `{rounded.md}` that reads as approachable without sacrificing the brand's serious literary tone. The checkout flow introduces a bright blue (#00bbff) accent for progress indicators, and a muted gray (#9ca3af) handles secondary metadata like author names and publication dates. The overall system feels like a well-stocked library — orderly, warm, and confident in its navy-and-seafoam identity, with orange serving as the friendly bookseller who points you to the right shelf.

colors:
  primary: "#00205b"
  primary-active: "#002758"
  primary-disabled: "#9ca3af"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#fefeff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-seafoam: "#70c8b5"
  accent-seafoam-hover: "#7ecdc3"
  accent-coral: "#ef7b3d"
  accent-orange: "#fb681c"
  accent-blue: "#00bbff"
  accent-purple: "#3e34d3"
  badge-green: "#39b757"
  badge-red: "#dc2626"
  star-rating: "#0098a0"
  scrim: "#0b0307"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  link-nav:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.47
    letterSpacing: 0
  price:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
    textDecoration: line-through

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-coral-hover:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.badge-red}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  top-nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
  top-nav-link-hover:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
  top-nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    fontWeight: 600
  secondary-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.link-nav}"
    height: 44px
    borderBottom: "1px solid {colors.hairline-soft}"
  secondary-nav-link:
    textColor: "{colors.body}"
    typography: "{typography.link-nav}"
    padding: "10px 16px"
  secondary-nav-link-hover:
    textColor: "{colors.primary}"
  secondary-nav-link-active:
    textColor: "{colors.primary}"
    fontWeight: 600
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3/4"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.accent-seafoam}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 320px
  hero-banner-accent:
    backgroundColor: "{colors.accent-seafoam}"
    textColor: "{colors.ink}"
  hero-banner-overlay:
    backgroundColor: "rgba(0, 32, 91, 0.6)"
  hero-cta:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
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
    opacity: 1
    textDecoration: underline
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  category-chip-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  pagination-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-inactive-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  rating-text:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginLeft: "{spacing.xs}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    backgroundColor: "{colors.surface-soft}"
  accordion-content:
    padding: "{spacing.base} {spacing.lg}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
    width: "100%"
  newsletter-submit:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 2px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-light:
    color: "{colors.on-primary}"
    size: 24px
  toast-success:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  toast-error:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  toast-info:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  modal-overlay:
    backgroundColor: "rgba(11, 3, 7, 0.6)"
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    maxWidth: 600px
  modal-header:
    typography: "{typography.title-lg}"
    marginBottom: "{spacing.base}"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  tab-inactive-hover:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 28px
    width: 28px
  quantity-selector-button-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  add-to-cart-button:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-hover:
    backgroundColor: "{colors.accent-orange}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  wishlist-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-coral}"
    border: "1px solid {colors.accent-coral}"
  wishlist-button-active:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.accent-coral}"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered in deep navy (`{colors.primary}`) with white text on a softly rounded rectangle (`{rounded.sm}`). On hover, it darkens to `{colors.primary-active}` (#002758). The disabled state drops to `{colors.primary-disabled}` (#9ca3af), a muted gray that signals unavailability without visual noise. Used for "Sign In," "Register," and primary checkout actions.

**`button-secondary`** — An outlined variant with a 2px navy border on a white canvas. The text inherits `{colors.primary}` and shifts to `{colors.primary-active}` on hover, while the background fills with `{colors.surface-soft}` (#f4f4f4). This button appears alongside primary CTAs for "Cancel" or "View Details" actions where emphasis is needed without full color weight.

**`button-accent-coral`** — The high-energy CTA, using `{colors.accent-coral}` (#ef7b3d) as a warm, inviting background. This is the "Add to Basket" button on product pages and the hero banner's primary call-to-action. On hover, it shifts to `{colors.accent-orange}` (#fb681c), creating a subtle warmth gradient. Uses `{typography.button-lg}` for slightly larger, bolder text.

**`button-accent-orange`** — A secondary accent button using the brighter `{colors.accent-orange}` (#fb681c). Used for promotional CTAs, "Shop Now" banners, and limited-time offer buttons. Same rounded rectangle shape as the primary button but with a more urgent, sale-oriented color.

**`button-ghost`** — A text-only button with no background or border, using `{colors.primary}` text. On hover, it gains a `{colors.surface-soft}` background. Used for "Learn More," "See All," and tertiary navigation actions where minimal visual weight is desired.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with a soft `{rounded.md}` (12px) corner and a subtle `{colors.hairline-soft}` border. On hover, the border strengthens to `{colors.hairline}` and a light box shadow lifts the card. The image area maintains a 3:4 aspect ratio (standard book proportions) with a `{rounded.sm}` (8px) corner. The title uses `{typography.title-sm}` (16px, weight 600), the author sits in `{typography.body-sm}` (13px, weight 400, `{colors.muted}`), and the price uses a bold 16px weight-600 style. Sale prices render with a line-through in `{colors.muted}`.

**`product-card-badge`** — A small, uppercase label positioned absolutely at the top-left of the card image. The default badge uses `{colors.accent-seafoam}` (#70c8b5) for "Staff Pick" or "Recommended." A sale variant uses `{colors.accent-orange}` (#fb681c) for "Sale" or "Offer." A "New" variant uses `{colors.badge-green}` (#39b757). All badges share `{typography.badge}` (11px, weight 600, uppercase) with `{rounded.xs}` (4px) corners and 2px/8px padding.

### Navigation
**`top-nav`** — A full-width navy (`{colors.primary}`) bar at 60px height, containing site logo, primary navigation links, and a search icon. Links use `{typography.nav-link}` (15px, weight 500) in white with 8px/16px padding and a subtle `{rounded.xs}` (4px) hover state using a semi-transparent white background (rgba(255, 255, 255, 0.1)). Active links get a slightly stronger overlay (rgba(255, 255, 255, 0.15)) and weight 600.

**`secondary-nav`** — A light gray (`{colors.surface-soft}`) bar at 44px height below the top nav, separated by a `{colors.hairline-soft}` bottom border. Links use `{typography.link-nav}` (14px, weight 500) in `{colors.body}` (#374151), shifting to `{colors.primary}` on hover. Active links display a 2px navy bottom border and weight 600, indicating the current category or section.

### Forms
**`text-input`** — A standard text input with white background, `{colors.hairline}` border, and `{rounded.sm}` (8px) corners. The placeholder uses `{colors.muted-soft}` (#9ca3af). On focus, the border thickens to 2px `{colors.primary}` with no outline. Error state uses a 2px `{colors.badge-red}` (#dc2626) border. Height is 44px with 10px/16px padding for comfortable touch interaction.

**`search-bar`** — Similar to `text-input` but with a search icon positioned inside the left padding. The icon uses `{colors.muted}` (#6b7280). Focus state mirrors the text input with a 2px navy border. Used in the top nav and on search results pages.

### Footer
**`footer`** — A full-width navy (`{colors.primary}`) footer with white text at 85% opacity for links. Headings use `{typography.title-sm}` (16px, weight 600) with full opacity. Links use `{typography.link}` (14px, weight 400, underline on hover). The footer contains columns for "About Us," "Customer Service," "Quick Links," and a newsletter signup form. Padding is `{spacing.xxl}` (48px) vertical and `{spacing.lg}` (24px) horizontal.

### Hero Banner
**`hero-banner`** — A large promotional area with a navy (`{colors.primary}`) background and white text using `{typography.display-lg}` (28px, weight 500). Minimum height is 320px with generous padding. An accent variant uses `{colors.accent-seafoam}` (#70c8b5) background with dark text. The CTA button (`{hero-cta}`) uses `{colors.accent-coral}` (#ef7b3d) with `{typography.button-lg}` (16px, weight 600) and `{rounded.sm}` (8px) corners.

### Badges & Chips
**`category-chip`** — A pill-shaped (`{rounded.full}`) chip for genre or category filtering. Default state is light gray (`{colors.surface-soft}`) with `{colors.body}` text and a `{colors.hairline}` border. On hover and active states, it fills with `{colors.primary}` and white text. Padding is 6px/16px with `{typography.button-sm}` (12px, weight 500).

### Pagination
**`pagination`** — Numbered page navigation using `{typography.body-md}` (14px). Active pages show a navy (`{colors.primary}`) background with white text in a `{rounded.sm}` (8px) rectangle. Inactive pages have a white background with `{colors.hairline}` border, shifting to `{colors.surface-soft}` on hover with a navy border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack single-column (1 col); hero banner reduces to 240px min-height; category chips wrap to 2 columns; footer columns stack vertically; search bar moves to full-width below nav; secondary nav hides behind "Categories" dropdown |
| Tablet | 744–1128px | Top nav shows limited links (Home, Books, Gifts, More); product cards display in 2-column grid; hero banner at 280px min-height; category chips in horizontal scrollable strip; footer columns in 2x2 grid; secondary nav shows as horizontal scroll |
| Desktop | 1128–1440px | Full top nav with all links; product cards in 3-column grid; hero banner at 320px min-height; category chips in horizontal wrap; footer in 4-column grid; secondary nav fully visible |
| Wide | > 1440px | Max-width container at 1440px centered; product cards in 4-column grid; hero banner at 360px min-height with larger typography; extra whitespace on sides; footer columns at max 280px width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons (wishlist, quantity selector) are 36px minimum with 44px touch area via padding
- Category chips are 36px minimum height
- Top nav links have 60px touch area (full nav height)
- Pagination buttons are 36px minimum with 44px touch area
- Modal close button is 32px with 44px touch area

### Collapsing Strategy
- Top nav: On mobile, all links collapse into a hamburger menu; the logo and search icon remain visible
- Secondary nav: On mobile, collapses into a single "Categories" dropdown button; on tablet, becomes a horizontal scrollable strip
- Product grid: Collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer: Collapses from 4 columns (desktop) → 2x2 grid (tablet) → single column stack (mobile)
- Category chips: On mobile, wraps to 2 columns; on tablet, becomes a horizontal scrollable strip
- Hero banner: Reduces min-height and font size on smaller screens; CTA button becomes full-width on mobile
- Search bar: On mobile, expands to full width below the top nav when activated

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for many components are inferred from common patterns; actual hover transitions (duration, easing) not extracted
- Error states for forms (validation messages, error icons) not observed on live site
- Dark mode not present on live site; no dark palette tokens available
- Focus states for keyboard navigation not reliably extracted
- Loading states (skeleton screens, shimmer animations) not observed
- Dropdown menu styles (mega menu, nested categories) not fully captured
- Mobile hamburger menu animation and overlay behavior not documented
- Cart drawer / mini-cart flyout styling not observed
- Checkout flow styling (multi-step, progress indicators) partially inferred from extracted colors
- Newsletter signup success/error states not documented
- Stock availability indicators ("In Stock," "Low Stock," "Out of Stock") colors not confirmed
- Book preview / look-inside modal styling not observed
- Author page layout and book series display patterns not documented
- Gift card and e-book specific UI patterns not captured
- Print stylesheet behavior not tested
- Accessibility compliance (ARIA labels, focus order, color contrast ratios) not verified
- Animation and transition timing values (duration, easing functions) not extracted
- Custom select / dropdown arrow styling not observed
- Radio button and checkbox custom styling not documented
- Tooltip and popover component styles not present on live site
