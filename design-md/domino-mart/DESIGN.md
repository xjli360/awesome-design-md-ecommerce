---
version: alpha
name: "Domino Mart"
source_url: "https://www.dominomart.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003399 anchors Domino Mart’s identity — not as a corporate navy but as a saturated, almost electric ultramarine that appears on the primary button, the top nav background, and the site’s favicon, giving the label-shop a sense of authoritative calm rather than loud hype. The canvas is a clean white, letting the blue and a small set of accent tones — a sharp red #e71c42 for sale badges and a warm beige #f18e7e for secondary highlights — do the work of hierarchy without visual clutter. Typography runs system-native: the stack of -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, and sans-serif means the site loads instantly with no custom font overhead, a practical choice that reads as quietly confident. Buttons are rectangular with a subtle {rounded.sm} radius, and the search bar follows the same logic — no pill shapes, no floating orbs, just clean, functional geometry. The product grid uses generous {spacing.lg} gutters and cards with a soft shadow and {rounded.md} corners, letting album art and merchandise photography breathe. The footer is dense with links in {colors.muted} on a {colors.surface-soft} background, a familiar e-commerce pattern that prioritizes discoverability over decoration. Domino Mart feels like a record store that knows its catalog is the star — the design steps back, uses a single strong color as its handshake, and otherwise gets out of the way.

colors:
  primary: "#003399"
  primary-active: "#004085"
  primary-disabled: "#b3d7ff"
  ink: "#161414"
  body: "#383d41"
  muted: "#888888"
  muted-soft: "#b9bbbe"
  hairline: "#c8cbcf"
  hairline-soft: "#d6d8db"
  canvas: "#ffffff"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e71c42"
  accent-beige: "#f18e7e"
  success-green: "#155724"
  info-blue: "#0c5460"
  warning-yellow: "#856404"
  error-text: "#721c24"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
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
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  page-section:
    padding: "{spacing.section} 0"
  container:
    maxWidth: 1200px
    padding: "0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Subscribe" actions. Rendered as a solid rectangle in the brand's deep blue {colors.primary} with white text in 16px semibold. On hover, the background shifts to {colors.primary-active} (#004085) with no border change. The disabled state uses {colors.primary-disabled} (#b3d7ff) to signal inactivity while maintaining brand consistency. Padding is 12px top/bottom, 24px left/right, producing a compact 44px-tall button that works well in both product detail and cart contexts.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Continue Shopping." Uses a white background with {colors.primary} text, a 1px solid {colors.primary} border, and the same 44px height as the primary button. The active state inverts to {colors.surface-soft} background with {colors.primary-active} text, providing clear visual feedback without competing with the primary button's hierarchy.

### Cards
**`product-card`** — The core content container for the product grid, featuring a white background, {rounded.md} corners, and a subtle box shadow that lifts the card off the canvas. The image area occupies the top portion with rounded top corners, while the bottom section holds the product title in {typography.title-md} and price in {typography.body-md}. Cards are spaced with {spacing.lg} gutters in a responsive grid that collapses from 4 columns on desktop to 2 on tablet and 1 on mobile.

**`sale-badge`** — A small, high-contrast label pinned to the top-left corner of product cards for discounted items. Uses the brand's accent red {colors.accent-red} (#e71c42) as background with white uppercase text in 11px bold. The badge has {rounded.xs} corners and minimal padding (2px 8px), ensuring it communicates urgency without obscuring the product image.

### Navigation
**`nav-bar`** — A full-width top navigation bar with a {colors.primary} background, 64px tall, containing the Domino Mart logo on the left and navigation links in uppercase 14px semibold white text with 0.5px letter-spacing. The bar is fixed to the top of the viewport on desktop, with a z-index that keeps it above all other content. Links have a hover state that adds a subtle underline or opacity shift, though the exact hover treatment was not fully extractable.

**`nav-link`** — Navigation link styling within the top bar: 14px, 600 weight, uppercase with 0.5px letter spacing, rendered in white on the blue background. The uppercase treatment gives the navigation a editorial, label-shop feel rather than a generic e-commerce one.

### Forms
**`text-input`** — Standard text input fields used in search, newsletter signup, and checkout forms. A white background with {rounded.sm} corners, 44px height, and 16px padding. The focus state adds a 2px blue box-shadow using {colors.primary-disabled} as the glow color, creating a clear but not overwhelming focus indicator. Placeholder text uses {colors.muted} (#888888).

**`search-bar`** — The site search input, visually identical to the text-input but with a search icon positioned on the left side. The input itself is 44px tall with {rounded.sm} corners, and the submit action is triggered either by pressing Enter or clicking a magnifying glass icon rendered in {colors.muted}. The search bar sits within the nav-bar on desktop and expands to full width on mobile.

### Footer
**`footer`** — A full-width footer section on a {colors.surface-soft} (#ececf6) background, containing columns of links for "Shop," "Artists," "About," and "Help." Links are 14px regular weight in {colors.muted} (#888888) with a hover state that darkens to {colors.ink} (#161414). The footer includes a newsletter signup form, social media icons (likely in {colors.muted}), and copyright text in {typography.caption}. Padding is {spacing.section} (64px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; search bar expands to full width below nav; footer columns stack vertically; product card images become full-width |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains visible but links may condense; search bar remains in nav; footer columns display in two rows of two |
| Desktop | 1128–1440px | Four-column product grid; full nav-bar with all links visible; search bar in nav; footer columns in a single row |
| Wide | > 1440px | Max-width container (1200px) centers content; product grid remains four columns; all other layouts scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have at least 44px tap area even if text is smaller
- Product card tap targets cover the full card area
- Search bar and text inputs are 44px tall for comfortable touch interaction

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay or slide-in drawer with all nav links
- Product grid collapses from 4 columns → 2 columns → 1 column as viewport shrinks
- Footer columns stack vertically on mobile, with each link group becoming an accordion or simple stacked list
- Search bar moves from inline in the nav to a full-width element below the nav on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by Bootstrap alert and form-validation colors (success green, info blue, warning yellow, error red) — these are likely framework defaults, not brand choices. The true brand palette is inferred from the distinctive #003399 (primary), #e71c42 (accent red), and #f18e7e (accent beige), but secondary and tertiary brand colors remain unconfirmed.
- Hover and active states for most components (buttons, links, cards) were not reliably extractable from the static CSS analysis. The active states provided are educated estimates based on common darkening patterns.
- Font-family declarations returned only system fonts — no custom typeface was detected. This may be intentional (system font stack for performance) or the custom font may be loaded via JavaScript after initial page render.
- Shadow values for product cards and other elevated elements were not extractable. A standard `0 2px 8px rgba(0,0,0,0.08)` is assumed but unconfirmed.
- Transition durations and easing curves for hover/focus states are unknown.
- Error state styling for form inputs (validation errors, required field indicators) was not present in the extracted data.
- Dark mode or high-contrast mode variants were not detected.
- The exact hamburger menu icon style and animation for mobile navigation are unknown.
- Social media icon colors and hover states were not extractable.
- The newsletter signup form's button styling and success/error messaging were not captured.
