---
version: alpha
name: "Omnitype"
source_url: "https://omnitype.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision-engineering enthusiast's playground where #ff3533 — a stop-sign red that reads as both urgency and obsession — anchors a system otherwise built on warm grays (#eeeeee, #f7f8f7, #f9fafb) and the occasional teal surprise (#108474). The brand's visual language is that of a machinist's workshop translated into pixels: generous whitespace, sharp rectangular cards with {rounded.sm} corners, and a typographic hierarchy that lets product photography do the heavy lifting. The red appears in primary CTAs, sale badges, and the theme-color meta tag — it's the single voltage that signals "this matters" against a canvas of #ffffff and #f9f9f9. Secondary accents drift into purple (#a89cc8, #cbaaff, #9c5dff) and mint (#c1e6e6), suggesting limited-edition colorways or category badges rather than core brand tokens. The extracted font stack is thin — Nunito Sans appears alongside system fallbacks — but the design compensates with consistent 16px body copy, 14px captions, and 48px section spacing that gives each product page the breathing room of a gallery wall. There is no rounded-full anywhere except the occasional badge; Omnitype prefers the honesty of a straight edge.

colors:
  primary: "#ff3533"
  primary-active: "#e60200"
  primary-disabled: "#f9bebc"
  ink: "#242320"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#bbbbbb"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f7f8f7"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-purple: "#a89cc8"
  accent-purple-strong: "#9c5dff"
  accent-mint: "#c1e6e6"
  accent-gold: "#fbcd0a"
  badge-sale: "#ff3533"
  badge-new: "#108474"
  badge-preorder: "#a89cc8"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.25px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  button-pill-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  button-pill-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    color: "{colors.canvas}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  variant-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  variant-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.ink}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base} 0"
  section-subheader:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "0 0 {spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand's signature red (#ff3533) on a white background with 8px rounded corners. On hover, shifts to a deeper red (#e60200). Disabled state uses a soft pink (#f9bebc). All primary buttons use 15px Nunito Sans at weight 600 with 12px vertical and 24px horizontal padding, producing a 44px tall button that feels substantial without overwhelming the layout.

**`button-secondary`** — An outlined alternative for less prominent actions. White background with a 1px hairline border (#dedede). On hover, the background shifts to #f7f8f7 and the border darkens to #bbbbbb. Same dimensions as primary buttons for alignment in forms and grouped actions.

**`button-tertiary`** — A text-only button for secondary actions like "View details" or "Cancel". Uses the brand red as text color with no background or border. On hover, shifts to the deeper red (#e60200). Maintains the same 12px vertical padding as other buttons for consistent alignment.

**`button-pill-sale`**, **`button-pill-new`**, **`button-pill-preorder`** — Small pill-shaped badges used on product cards and collection pages to indicate product status. Each uses a distinct color: red for sale, teal (#108474) for new arrivals, and purple (#a89cc8) for pre-orders. Uses 11px uppercase Nunito Sans at weight 700 with 6px vertical and 16px horizontal padding, fully rounded.

### Cards
**`product-card`** — The primary product display component. A white card with 8px rounded corners and no shadow — the brand relies on the hairline-soft border (#e9e9e9) between cards in a grid rather than elevation. The image occupies the top portion with rounded top corners, followed by the product title in 16px weight 600, and the price in 16px weight 400. Badges overlay the image at the top-left corner.

### Navigation
**`nav-bar`** — A fixed 64px white header with a 1px soft hairline bottom border (#ebebeb). Navigation links use 14px Nunito Sans at weight 600. Active links display in the brand red (#ff3533), while inactive links use the muted gray (#7b7b7b). The search bar sits within the nav on desktop, collapsing into a search icon on mobile.

### Forms
**`text-input`** — Standard text input with white background, 8px rounded corners, and a 1px hairline border (#dedede). On focus, the border switches to the brand red (#ff3533). Error state also uses the brand red border. All inputs are 44px tall with 10px vertical and 16px horizontal padding, using 16px Nunito Sans at weight 400.

**`select-input`** — Matches the text input styling for visual consistency. Uses the same dimensions, border, and typography. The dropdown arrow is rendered as a system default or custom SVG in the brand's ink color (#242320).

**`quantity-selector`** — A compact input for selecting product quantities. Matches the text input styling but with tighter padding (8px vertical, 12px horizontal). Used in cart and product detail pages alongside the add-to-cart button.

### Badges
**`badge-sale`**, **`badge-new`**, **`badge-preorder`** — Small rectangular badges with 4px rounded corners. Each uses a distinct background color matching the pill buttons but with a rectangular shape for overlay positioning on product images. Uses 11px uppercase Nunito Sans at weight 700 with 2px vertical and 8px horizontal padding.

### Footer
**`footer-section`** — A dark footer with the brand's ink color (#242320) as background and white text. Links use the muted-soft gray (#bbbbbb) and shift to white on hover. The section uses 48px vertical padding on each side with 24px horizontal padding for content alignment.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, search bar collapses to icon, hero section reduces padding to 32px, product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, search bar remains full-width but collapses to icon on scroll, hero section uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid, full nav with search bar, hero section uses 64px padding, product cards show hover states with quick-add buttons |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero section uses 80px padding, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain a minimum 44px height for touch accessibility
- Icon buttons and badge pills use a minimum 32px touch area
- Product card tap targets extend to the full card width on mobile
- Variant selector pills use 40px height with 16px horizontal padding for comfortable tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Search bar collapses to a search icon with expandable overlay on mobile
- Product filters collapse into a "Filter" button with slide-out drawer on mobile
- Footer link columns collapse into accordion sections on mobile
- Multi-column product grids reduce to single column below 744px
- Hero section text and CTA stack vertically on mobile, with the CTA taking full width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns rather than extracted from live CSS — the extracted color list didn't include hover variants for secondary buttons, text inputs, or navigation links
- Error styling for form validation (error messages, error icons, error state colors) was not extractable from the page — the red primary is used as a reasonable error indicator but may differ from the actual implementation
- The font stack is incomplete — only Nunito Sans was found in extracted declarations, but the brand may use additional weights or a secondary font for display text that wasn't captured
- Dark mode colors were not extractable — the site may not support dark mode, or it may use a different palette that wasn't present in the extracted colors
- Sub-brand or collection-specific color palettes (e.g., limited edition keyboard colorways) were not extractable — the accent colors (teal, purple, mint, gold) are inferred from extracted hex values but their exact usage context is unknown
- Animation and transition durations, easing functions, and micro-interaction patterns were not extractable from the static page
- Shadow/elevation tokens were not extractable — the site may use box-shadows on cards or modals that weren't present in the extracted CSS
- The extracted color list includes potential Shopify checkout widget colors and social icon colors that may not be part of the brand's core design system — the true brand palette may be more limited than what's listed
