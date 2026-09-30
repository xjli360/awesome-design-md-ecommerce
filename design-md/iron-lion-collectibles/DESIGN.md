---
version: alpha
name: "Iron Lion Collectibles"
source_url: "https://ironlioncollectibles.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A trading card marketplace that announces itself with #bd202e — a deep, confident red that covers the primary button, the top nav bar, and the footer, creating a visual spine of intensity across the entire experience. Against a canvas of #fefefe, the red reads as deliberate and passionate rather than aggressive, especially when paired with the secondary teal #25878c that appears in sale badges and accent links. The brand uses a tight monochrome scale — #2d2d2d for body text, #292929 for headings, #121212 for the darkest UI elements — with #dedede and #bdbdbd providing the structural grays for borders and dividers. Roboto at 400 weight carries the product listings and category descriptions, while bolder weights (500–700) handle the card names, prices, and navigation labels. The layout is dense but organized: product cards stack in responsive grids with {rounded.sm} corners, search sits in a pill-shaped field at {rounded.full}, and the red CTA button maintains a consistent 48px height across breakpoints. There is no decorative flourish — every design decision supports the primary action of browsing and buying cards, from the high-contrast price tags to the sticky top nav that keeps the search and cart always within reach.

colors:
  primary: "#bd202e"
  primary-active: "#7c1316"
  primary-disabled: "#dedede"
  ink: "#292929"
  body: "#2d2d2d"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#bdbdbd"
  hairline-soft: "#dedede"
  canvas: "#fefefe"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#fefefe"
  accent-teal: "#25878c"
  accent-blue: "#1199ff"
  dark-bg: "#121212"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    height: 48px
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
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
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
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sold-out:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    height: 24px
  mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Sign Up" actions. Rendered in the brand red {colors.primary} with white text and {rounded.sm} corners. On hover, the background deepens to {colors.primary-active} (#7c1316) for a clear state change. The disabled state uses {colors.primary-disabled} (#dedede) with muted text, signaling the action is unavailable.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Cancel". Uses a white background with a 2px solid {colors.ink} border, maintaining the same 48px height as the primary button for visual consistency. On hover, the background fills with a subtle {colors.surface-soft} tint.

**`button-tertiary`** — A text-only button for inline actions like "Clear Filters" or "See More". Uses {colors.primary} text on a transparent background with no border, keeping the interface clean while maintaining brand color presence.

**`button-pill`** — A compact, fully rounded button used for quick actions like "Quick Add" or filter tags. Smaller padding and {rounded.full} corners make it suitable for tight spaces within product cards or category strips.

### Navigation
**`nav-bar`** — The sticky top navigation bar, rendered in the brand red {colors.primary} with white text. At 64px on desktop, it contains the site logo, primary navigation links, search bar, and cart icon. On scroll, it collapses to 56px while maintaining the same color treatment. Navigation links use {typography.nav-link} at 15px with 500 weight and subtle letter-spacing.

**`nav-bar-sticky`** — The collapsed state of the navigation bar when the user scrolls past the hero area. Reduces height to 56px while preserving all functionality and color treatment.

### Cards
**`product-card`** — The primary content container for displaying trading cards and collectibles. Each card features a square aspect ratio image with {rounded.sm} corners, the card name in {typography.title-sm}, and the price in {typography.price}. Cards sit on a white background with 12px padding and gain a subtle box-shadow on hover to indicate interactivity.

**`product-card-sale-badge`** — A small teal badge overlaid on product images to indicate sale items. Uses {colors.accent-teal} (#25878c) background with white text in uppercase {typography.badge} at 11px. The badge sits at the top-left corner of the product image with {rounded.xs} corners.

### Search
**`search-bar`** — A pill-shaped search field with {rounded.full} corners, white background, and a 1px {colors.hairline} border. On focus, the border switches to a 2px {colors.primary} stroke, providing clear visual feedback. The search bar maintains a 44px height and sits within the navigation bar on desktop, expanding to full width on mobile.

### Badges
**`badge-new`** — A blue badge used to indicate newly added inventory. Uses {colors.accent-blue} (#1199ff) background with white text in uppercase {typography.badge}. Applied to product cards or category sections to draw attention to fresh stock.

**`badge-sold-out`** — A red badge indicating items that are no longer in stock. Uses {colors.primary} background with white text, maintaining brand consistency even in status indicators.

### Filters
**`filter-dropdown`** — Dropdown selectors used in the product listing sidebar for filtering by category, condition, price range, and set. Uses a white background with {rounded.sm} corners and a 1px {colors.hairline} border. The 40px height keeps filters compact while remaining touch-friendly.

### Footer
**`footer`** — The site footer rendered on a dark background ({colors.dark-bg} #121212) with muted gray text. Contains navigation links, contact information, and legal text. Links use {typography.link} at 14px and lighten to white on hover for clear interactivity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; search bar moves below nav; product grid goes to 2 columns; filter sidebar becomes a bottom sheet or dropdown; footer stacks vertically |
| Tablet | 744–1128px | Navigation shows limited links with "More" dropdown; product grid uses 3 columns; filter sidebar collapses to a horizontal strip of chips; search bar remains in nav but narrower |
| Desktop | 1128–1440px | Full navigation with all links visible; product grid uses 4 columns; filter sidebar is persistent on the left; search bar at full width in nav |
| Wide | > 1440px | Maximum content width of 1440px with centered layout; product grid expands to 5 columns; additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum height of 44px for touch accessibility
- Product card tap targets are at least 48px for the primary action button
- Filter chips and category chips are 40px tall with 16px horizontal padding
- Mobile menu toggle is 40px with 24px icon area

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Filter sidebar collapses into a horizontal chip strip below 1128px, then into a bottom sheet below 744px
- Product grid reduces from 5 columns to 2 columns as viewport narrows
- Search bar collapses from full-width to icon-only on mobile, expanding on tap
- Footer links stack vertically below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from common patterns; exact transitions and box-shadow values were not extracted
- Error styling for form inputs (validation states, error messages) was not visible in the extracted data
- The exact font weight for body text (400 vs 300) is assumed based on Roboto's standard weights; the site may use 300 for lighter text
- Sub-brand or promotional palette variations (e.g., holiday themes, special editions) were not captured
- Dark mode styling was not present in the extracted data
- The exact spacing values for product card grids (gap between cards) were not reliably extracted
- Animation durations and easing curves for hover states and transitions are not documented
- The specific hex for the site's primary red in different states (hover, active, disabled) beyond the extracted colors is inferred
- Checkout flow styling (Shopify checkout pages) may use different colors than the main site
- The brand may use additional accent colors for specific categories or promotions that were not captured in the top 10 extracted hexes
