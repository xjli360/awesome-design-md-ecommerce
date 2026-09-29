---
version: alpha
name: "Game Over Video Games"
source_url: "https://gameovervideogames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A retro game retailer that wears its nostalgia on its sleeve through a warm, amber-toned palette anchored on #f8bb86 — a soft, aged gold that reads like the glow of a CRT monitor in a dimly lit basement. The brand pairs this with #0da19a, a teal accent that feels lifted from a 90s soda can, creating a complementary tension that keeps the interface from drifting into sepia monotony. Buttons and badges lean into #f27474 (a coral error-red) and #a5dc86 (a mint success-green), suggesting a system built for transactional clarity — add-to-cart, sold-out, in-stock — rather than atmospheric storytelling. The canvas is #f9f9f9, a warm off-white that avoids the sterile hospital feel of pure white, while #222222 and #3a3a3a handle body and ink duties with enough contrast to keep product listings legible. The typography stack is utilitarian — Open Sans, Arial, Helvetica — no custom retro pixel font, no arcade revival; the brand lets the product photography (cartridges, consoles, boxes) carry the period flavor. Cards use soft {rounded.sm} corners, search is a pill-shaped bar at {rounded.full}, and the nav sits at a compact 64px height, prioritizing shelf space over brand theater. The overall effect is a clean, commerce-forward system that trusts its inventory — not its chrome — to evoke the era.

colors:
  primary: "#f8bb86"
  primary-active: "#f0a05e"
  primary-disabled: "#fce4c8"
  ink: "#222222"
  body: "#3a3a3a"
  muted: "#575757"
  muted-soft: "#797979"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f9f9f9"
  surface-soft: "#f1f1f0"
  surface-card: "#ffffff"
  on-primary: "#222222"
  accent-teal: "#0da19a"
  accent-teal-active: "#017b86"
  success-green: "#a5dc86"
  error-coral: "#f27474"
  badge-sold: "#ea7d7d"
  badge-new: "#f8d486"
  star-rating: "#f8bb86"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.25px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.25px
  link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px

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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-teal-active:
    backgroundColor: "{colors.accent-teal-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.ink}"
  product-card-price-sale:
    color: "{colors.error-coral}"
  badge-condition:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sold-out:
    backgroundColor: "{colors.badge-sold}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new-arrival:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Subscribe". Rendered in the warm amber {colors.primary} with dark text for contrast. On hover, shifts to {colors.primary-active}. Disabled state uses a desaturated {colors.primary-disabled} with muted text, signaling the action is unavailable. Height is 44px with {rounded.sm} corners, compact enough to stack in product grids without overwhelming the card.

**`button-secondary`** — A ghost-style button with a white fill and a 1px hairline border, used for "View Details", "Cancel", or secondary form actions. Active state swaps the border to {colors.ink} for clear focus. Shares the same 44px height and padding as primary for alignment in button groups.

**`button-accent-teal`** — Reserved for high-impact actions like "Pre-order" or "Notify Me" where the brand wants to signal urgency without using error red. Uses {colors.accent-teal} background with white text, darkening to {colors.accent-teal-active} on hover. Same dimensions as primary buttons.

**`button-pill-search`** — A fully rounded pill button used inside the search bar or as a filter trigger. Smaller padding (10px 20px) and {rounded.full} shape differentiate it from standard CTAs. Uses {colors.primary} background.

### Cards
**`product-card`** — The core inventory display unit, a white card with {rounded.sm} corners and no internal padding (image fills top, content pads below). The product image gets rounded top corners only, creating a clean break between photo and text. Title uses {typography.title-sm} at 16px/600 weight, price uses {typography.body-md} at 600 weight. Sale prices render in {colors.error-coral} for immediate visual priority.

**`product-card-image`** — The image container within a product card, with top-left and top-right radius matching the card's {rounded.sm}. No bottom radius, so the image bleeds cleanly into the text section below.

### Badges
**`badge-condition`** — A teal badge for "Like New", "Good", or "Acceptable" condition labels. Uses {colors.accent-teal} background with white uppercase text at 11px/700 weight. Tight {rounded.xs} corners and 2px/8px padding keep it unobtrusive on product images.

**`badge-sold-out`** — A coral badge for out-of-stock items, using {colors.badge-sold} background. Same typography and sizing as condition badge, but the color signals unavailability without blocking the product image.

**`badge-new-arrival`** — A warm yellow badge ({colors.badge-new}) for recently listed items. Uses dark text for readability against the light background. Same dimensions as other badges.

**`badge-sale`** — An error-coral badge for discounted items, using {colors.error-coral} background with white text. Same sizing as other badges.

### Navigation
**`nav-bar`** — A compact 64px top navigation bar with white background and a soft bottom border. Navigation links use {typography.nav-link} at 15px/600 weight. Active links get a 2px bottom border in {colors.primary}, inactive links render in {colors.muted}. The bar collapses to a hamburger menu on mobile.

**`nav-link-active`** — The active navigation state, with an underline in {colors.primary} and full-weight {colors.ink} text. No background fill — the underline is the only indicator.

**`nav-link-inactive`** — Default navigation link state, using {colors.muted} text and no underline. On hover, text shifts to {colors.ink}.

### Forms
**`text-input`** — Standard text input for search, checkout forms, and newsletter signups. White background, 44px height, {rounded.sm} corners, and a 1px {colors.hairline} border. Focus state swaps the border to {colors.primary}. Error state uses {colors.error-coral} border.

**`search-bar-pill`** — The primary search input, rendered as a pill shape ({rounded.full}) with 48px height. Used on the homepage and category pages. Focus state highlights the border in {colors.primary}. The pill shape differentiates search from other form inputs.

**`quantity-selector`** — A compact input for cart quantity adjustments, with 44px height and {rounded.sm} corners. Uses a 1px hairline border and centered text.

### Footer
**`footer`** — A full-width footer with {colors.surface-soft} background and muted text. Links use {typography.link} at 14px/400 weight in {colors.muted}, shifting to {colors.ink} on hover. Padding is generous at {spacing.xxl} vertical and {spacing.base} horizontal.

### Hero
**`hero-banner`** — A full-width hero section used on the homepage and category landing pages. Uses {colors.surface-soft} background with {typography.display-lg} text. Padding is {spacing.section} vertical, creating a spacious entry point for promotional content.

### Filters
**`category-chip`** — A pill-shaped filter chip for browsing by console or genre. Uses {colors.surface-soft} background with muted text. Active state swaps to {colors.primary} background with dark text. The {rounded.full} shape and compact padding (6px 16px) allow horizontal scrolling strips.

### Pagination
**`pagination-button`** — Standard pagination control with white background and 1px hairline border. Active page uses {colors.primary} background and border. All buttons are 40px square with {rounded.sm} corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), nav collapses to hamburger, search bar reduces to icon-only, category chips scroll horizontally, hero banner reduces padding to {spacing.xl}, footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but compact, search bar shows as icon+text, category chips wrap to 2 rows, hero banner uses {spacing.xxl} padding |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links visible, expanded search bar with placeholder text, category chips in single horizontal row, hero banner at full {spacing.section} padding |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, nav and footer extend full width with content constrained, hero banner uses wider inner padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category chips are minimum 40px tall with 16px horizontal padding
- Quantity selector buttons are 44px square
- Pagination buttons are 40px square
- Search bar pill is 48px tall
- Nav links have 44px minimum tap area (padding + line-height)

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-out drawer for links
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Category chip strip collapses from single row to horizontally scrollable on mobile
- Footer link columns collapse from 4 columns (desktop) to 2 (tablet) to single column (mobile)
- Search bar collapses from full text input (desktop) to icon-only trigger (mobile) that opens a full-screen overlay
- Hero banner text reduces from {typography.display-xl} to {typography.display-md} on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for badges (condition, sold-out, new-arrival, sale) could not be extracted — assumed no hover change based on static nature of badges
- Error styling for form validation (error messages, helper text) not observed — only error border color inferred from {colors.error-coral}
- Dark mode or high-contrast mode styles not present on live site
- Sub-brand or seasonal palette variations not observed
- Loading states (skeleton screens, spinners) not extracted
- Focus-visible ring styles not observed — assumed browser default or missing
- Checkout flow styling (Shopify checkout override) not captured — may use platform defaults
- Mobile navigation drawer animation and overlay styling not observed
- Product quick-view modal or lightbox styling not extracted
- Stock indicator (e.g., "Only 3 left") styling not observed — may use {colors.error-coral} or {colors.accent-teal}
- Newsletter signup success/error states not extracted
- Cart drawer or mini-cart styling not observed
- Breadcrumb component styling not extracted
- Accordion or FAQ section styling not observed
- Tooltip or popover styling not extracted
- Print stylesheet not present on live site
- Reduced-motion preferences not addressed in observed CSS
