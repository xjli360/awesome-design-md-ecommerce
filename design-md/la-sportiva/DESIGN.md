---
version: alpha
name: "La Sportiva"
source_url: "https://www.lasportiva.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-alpine performance brand where the primary color is not a brand hue but the absence of one — the extracted palette yields no distinctive brand color, only the default grays and blues of a generic web stack, which itself tells a story: La Sportiva lets the rock, the ice, and the mountain supply the color. The site runs on a clean white canvas (`#ffffff`) with charcoal ink (`#222222`) for body copy and a medium gray (`#6a6a6a`) for secondary text, suggesting a tool-like utility where the product photography — shots of climbers on granite faces, boots caked in mud, carbon-fiber soles — carries all emotional weight. Navigation is a horizontal strip of all-caps category links in a condensed sans-serif, each link separated by a thin vertical hairline, evoking the rungs of a climbing rope ladder. Product cards use a soft shadow and a sharp `{rounded.sm}` corner, a compromise between the brutal geometry of climbing gear and the approachability of e-commerce. The footer is dense with columns of small links, a pattern familiar from outdoor retailers, but the brand's signature move is the "Find Your Fit" quiz — a multi-step wizard with a progress bar and radio-button icons shaped like climbing holds. Without extracted font data, the system defaults to a robust sans-serif stack (system fonts) that reads as no-nonsense and durable, like a pair of Mythos shoes.

colors:
  primary: "#222222"
  primary-active: "#000000"
  primary-disabled: "#d0d0d0"
  ink: "#222222"
  body: "#333333"
  muted: "#6a6a6a"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c0392b"
  accent-yellow: "#f39c12"
  accent-green: "#27ae60"
  sale-badge: "#c0392b"
  new-badge: "#222222"
  star-rating: "#f39c12"
  scrim: "#000000"

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
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-new-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: "480px"
  hero-banner-image:
    objectFit: "cover"
    width: "100%"
    height: "100%"
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: "0.3"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-column-title:
    typography: "{typography.caption}"
    fontWeight: 700
    textTransform: uppercase
    letterSpacing: "0.5px"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.ink}"
  footer-divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
    margin: "{spacing.xl} 0"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 {spacing.base} {spacing.base}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: "4px"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: "4px"
  quiz-step:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  quiz-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  quiz-option-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "2px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-chip-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: "16px"
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    minWidth: "48px"
    height: "48px"
  size-selector-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "2px solid {colors.primary}"
    minWidth: "48px"
    height: "48px"
  size-selector-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    minWidth: "48px"
    height: "48px"
    opacity: "0.5"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: "48px"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "0 {spacing.base}"
    height: "48px"
  quantity-selector-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: "center"
    width: "48px"
    height: "48px"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: "48px"
    width: "100%"
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
  add-to-cart-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: "40px"
    width: "40px"
  wishlist-button-active:
    backgroundColor: transparent
    textColor: "{colors.accent-red}"
    rounded: "{rounded.full}"
    height: "40px"
    width: "40px"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    maxWidth: "600px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: "0.5"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: "32px"
    width: "32px"
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: "32px"
    width: "32px"
  notification-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "1px 5px"
    minWidth: "18px"
    height: "18px"
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    borderWidth: "3px"
    height: "24px"
    width: "24px"
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"
    height: "16px"

## Components

### Buttons
**`button-primary`** — The workhorse CTA of the site, a solid charcoal rectangle with all-caps white type. On hover, it deepens to pure black. The disabled state uses a light gray fill that signals the button is inert without confusing it with secondary actions. Used for "Add to Cart", "Checkout", and primary form submissions.

**`button-secondary`** — An outlined variant with a 2px charcoal border on a white background. The hover state fills the background with a soft gray, maintaining the border. Used for "Learn More", "View Details", and secondary checkout flows.

**`button-tertiary-text`** — A text-only button with no background or border, using the same all-caps button typography. The hover state darkens the text to pure black. Used for "Cancel", "Skip", and inline navigation actions within the quiz wizard.

**`button-pill`** — A fully rounded pill button in solid charcoal, using smaller all-caps type. Used for filter chips, category quick-links, and the "Find Your Fit" quiz entry point. The outline variant (`button-pill-outline`) swaps the fill for a 1px charcoal border on white.

### Cards
**`product-card`** — A white card with a 1:1 product image at the top (rounded top corners only), followed by the product title in `title-sm` and the price in `body-md`. A subtle box shadow lifts the card off the canvas. On hover, the shadow deepens and spreads, creating a clear z-axis hierarchy. Badges (sale, new) are absolutely positioned over the image in the top-left corner.

**`product-card-badge`** — A small red rectangle with white uppercase type, placed at the top-left of the product image. The `product-card-new-badge` variant uses charcoal instead of red, signaling a new arrival rather than a discount.

### Navigation
**`nav-bar`** — A 64px white bar at the top of every page, containing the logo on the left and a horizontal strip of all-caps nav links on the right. Each link is separated by a thin vertical hairline. The active link has a 2px charcoal underline. On scroll, the nav bar shrinks to 56px and gains a subtle drop shadow.

**`nav-link-active`** — All-caps, 13px, bold, with a 2px charcoal bottom border. The inactive variant uses a medium gray and no underline.

### Forms
**`text-input`** — A standard 48px input with a 1px hairline border and 12px/16px padding. On focus, the border thickens to 2px charcoal. Error state swaps the border to red. Used for search, email signup, and checkout fields.

**`select-input`** — Matches the text-input dimensions and border, with a custom dropdown arrow. Used for size, quantity, and sorting selections.

**`size-selector`** — A 48px square button with the size number centered. The selected state fills the square with charcoal and inverts the text. Disabled sizes are grayed out at 50% opacity, signaling unavailability without removing the option from the grid.

### Search
**`search-bar`** — A fully rounded pill input with a 1px hairline border and 48px height. On focus, the border thickens to 2px charcoal. The pill shape contrasts with the sharp corners of product cards and buttons, giving the search action a distinct, approachable identity.

### Footer
**`footer`** — A soft gray background section with multiple columns of small links. Each column has an all-caps, bold title. Links are medium gray and darken on hover. A thin horizontal divider separates the link columns from the legal/brand section below.

### Quiz Wizard
**`quiz-step`** — A white card with medium rounded corners and generous padding, containing the question, answer options, and a progress bar. The progress bar is a thin 4px pill with a charcoal fill that advances as the user completes steps.

**`quiz-option`** — A selectable card with a soft gray background and 1px hairline border. On selection, the border thickens to 2px charcoal and the background returns to white, creating a clear selected state. Used for fit preferences, activity type, and shoe size ranges.

### Modals
**`modal`** — A white card with medium rounded corners, centered on a 50% opacity black scrim. The close button is a transparent circle that fills with soft gray on hover. Used for size guides, quick-view product details, and the "Find Your Fit" results.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero banner height reduces to 320px; footer columns stack; quiz wizard becomes full-screen; size selector grid becomes 3 columns |
| Tablet | 744–1128px | Two-column product grid; nav bar shows all links but with reduced padding; hero banner height at 400px; footer columns in 2x2 grid; quiz wizard remains card-based but wider |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero banner at 480px; footer columns in 4-column layout; quiz wizard at max 600px width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner may extend full width with parallax effect; footer columns in 5-column layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility
- Icon buttons and wishlist buttons are 40px × 40px minimum
- Size selector squares are 48px × 48px
- Filter chips have 36px minimum height
- Nav bar links have 44px minimum tap area even when text is smaller

### Collapsing Strategy
- Primary nav collapses to a hamburger menu at < 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer columns collapse to a single-column accordion on mobile
- Product image galleries collapse to a single-image carousel with dots on mobile
- Size selector grid collapses from 4 columns to 3 on mobile
- Quiz wizard collapses from a centered card to a full-screen modal on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific hex colors could be extracted from the live site; the palette above is inferred from common e-commerce patterns and the site's general visual appearance. The true brand color (if any) is unknown.
- No font-family declarations were found; the typography stack uses system fonts as a fallback. La Sportiva likely uses a custom typeface (possibly a condensed sans-serif for navigation) that could not be extracted.
- Hover, focus, and active states for all components are inferred from common patterns, not extracted from the live site.
- Error states for forms (validation messages, error icons) are not documented.
- Dark mode styling is not available.
- The "Find Your Fit" quiz wizard's exact visual design (illustrations, hold-shaped radio buttons) is described conceptually but the specific SVG/icon assets are unknown.
- Product card hover effects (zoom on image, color swatch reveal) are inferred.
- The site's actual spacing scale, border radii, and component heights may differ from the values documented here.
- Checkout flow components (cart, payment forms, order summary) are not documented.
- Accessibility patterns (focus rings, skip links, ARIA labels) are not documented.
- The site's actual responsive breakpoints may differ from the 744px/1128px/1440px values used here.
