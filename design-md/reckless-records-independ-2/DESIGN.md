---
version: alpha
name: "Reckless Records"
source_url: "https://www.reckless.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A gritty, music-first marketplace where #111111 ink meets #868e96 muted steel, and the only polish is on the vinyl. This is a record store's digital counter — utilitarian, dense with information, and built for the crate-digger who knows what they want. The palette is pulled from the physical space: deep black for the bins, warm gray for the concrete floor, and a single voltage of #004085 blue that appears on price tags and category headers like a sticker slapped on a used jacket. Typography runs system-native (-apple-system, Segoe UI, Roboto) at modest sizes — no brand font, no display face, just the browser's own voice — because the records are the typography. Cards use {rounded.sm} (8px) corners, buttons use {rounded.md} (12px), and the search bar uses {rounded.full} pills, but nothing is precious: the layout is a single-column stack on mobile, a two-column grid on desktop, and the footer is a wall of text links. The site doesn't sell an experience; it sells a catalog. Every hex in the palette — from #155724 (success green) to #721c24 (error red) to #856404 (warning amber) — comes from Bootstrap's alert classes, suggesting the store uses a framework boilerplate for its admin panels and checkout flows. The brand's true primary is #004085, a deep corporate blue that appears on the site's primary CTAs and navigation elements, standing out against the sea of grays and blacks like a record label's logo on a plain sleeve.

colors:
  primary: "#004085"
  primary-active: "#003570"
  primary-disabled: "#8099c2"
  ink: "#111111"
  body: "#464a4e"
  muted: "#868e96"
  muted-soft: "#b9bbbe"
  hairline: "#dae0e5"
  hairline-soft: "#ececf6"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#155724"
  error: "#721c24"
  warning: "#856404"
  info: "#0c5460"
  success-bg: "#b1dfbb"
  error-bg: "#f1b0b7"
  warning-bg: "#ffe8a1"
  info-bg: "#bee5eb"

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
    fontWeight: 500
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
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.muted}"
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.hairline-soft}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  category-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.lg}"
    rounded: "{rounded.sm}"
  price-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-indicator:
    typography: "{typography.caption}"
    color: "{colors.success}"
  cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Checkout," and "Search." Rendered in the brand's deep blue {colors.primary} with white text and {rounded.md} (12px) corners. On hover, shifts to {colors.primary-active} (#003570). Disabled state uses {colors.primary-disabled} (#8099c2) with reduced opacity. Height is 48px with 12px 24px padding for comfortable touch targets.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Clear Filters." White background with {colors.ink} text and a 2px {colors.hairline} border. Active state darkens the border to {colors.muted} and adds a {colors.surface-soft} background. Disabled state fades to {colors.muted-soft} text and {colors.hairline-soft} border.

### Cards
**`product-card`** — The core inventory display unit, used for vinyl, CDs, DVDs, and merchandise. White background with {rounded.sm} (8px) corners and 12px padding. On hover, the card shifts to {colors.surface-soft} and gains a subtle box-shadow. The image container uses a 1:1 aspect ratio with matching {rounded.sm}. Title is set in {typography.body-md} at 600 weight, price in {typography.body-sm} at {colors.muted}. Cards stack in a single column on mobile and grid into 2-4 columns on larger screens.

### Badges
**`badge-success`** — Used for "In Stock" indicators. Light green background ({colors.success-bg}) with dark green text ({colors.success}). {rounded.xs} (4px) with 2px 8px padding. **`badge-error`** — For "Out of Stock" or "Backordered" labels. Light red background ({colors.error-bg}) with dark red text ({colors.error}). **`badge-warning`** — For "Limited Stock" or "Pre-order." Light amber background ({colors.warning-bg}) with dark amber text ({colors.warning}). **`badge-info`** — For "New Arrival" or "Staff Pick." Light teal background ({colors.info-bg}) with dark teal text ({colors.info}). All badges share the same {typography.badge} sizing and {rounded.xs} corners.

### Navigation
**`nav-bar`** — A fixed-height (56px) top bar in {colors.ink} (#111111) with white text. Contains the store logo, category links, and a search icon. Links use {typography.nav-link} (14px, 600 weight). Active links are indicated by a 2px {colors.primary} bottom border. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard input field for search, checkout forms, and account pages. White background with 1px {colors.hairline} border, {rounded.sm} (8px), and 10px 16px padding. On focus, the border thickens to 2px and switches to {colors.primary}. Height is 48px for comfortable typing.

### Search
**`search-bar`** — A pill-shaped search input ({rounded.full}) with white background and 1px {colors.hairline} border. 48px height with 8px 16px padding. On focus, the border becomes 2px {colors.primary}. Used on the homepage and category pages for catalog-wide searches.

### Footer
**`footer`** — A dense information footer on {colors.surface-soft} background. Contains store hours, location, contact info, and policy links. Text is {colors.muted} in {typography.body-sm}. Links hover to {colors.ink}. Padding is {spacing.xl} (32px) top and bottom.

### Category Header
**`category-header`** — A full-width banner in {colors.primary} with white text, used to label record genres (Rock, Jazz, Classical, etc.) and store sections. {rounded.sm} (8px) corners with {spacing.md} {spacing.lg} padding. Text is {typography.title-md} (18px, 600 weight).

### Price Tag
**`price-tag`** — A small {colors.primary} badge with white text, {rounded.xs} (4px), and 2px 6px padding. Used inline on product cards and category listings. Typography matches {typography.badge}.

### Stock Indicator
**`stock-indicator`** — A simple text label in {colors.success} (#155724) using {typography.caption} (12px). Displays "In Stock," "Low Stock," or "Out of Stock" based on inventory levels. No background or border — just text.

### Cart Button
**`cart-button`** — A compact, pill-shaped button ({rounded.full}) in {colors.primary} with white text. 36px height with 8px 16px padding. Uses {typography.button-sm} (14px, 500 weight). Designed for the mini-cart and "Add to Cart" inline actions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves to top; footer stacks vertically; category headers become full-width pills |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links; search bar is inline in nav; footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; search bar is prominent in header; footer uses three columns |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; nav remains full; footer uses four columns |

### Touch Targets
- All buttons and links have a minimum height of 44px for touch accessibility
- Product cards have 12px padding to prevent accidental taps on adjacent items
- Search bar is 48px tall for easy thumb targeting
- Nav links have 8px padding on mobile for comfortable tapping
- Cart button is 36px tall — slightly below the 44px ideal but acceptable for secondary actions

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a full-screen overlay for link selection
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 3 to 2 to 1 as viewport shrinks
- Category headers collapse from full-width banners to compact pills on mobile
- Search bar moves from inline in nav (desktop) to a standalone element below the header (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., product-card, footer links) are inferred from common patterns, not extracted from the live site
- Error styling for form validation (red borders, error messages) is not confirmed — the extracted error colors (#721c24, #f1b0b7) suggest Bootstrap alert patterns but may not be used in form contexts
- Dark mode is not supported and no extracted data suggests it exists
- Sub-brand or seasonal palettes (e.g., Record Store Day, holiday promotions) are not captured
- The extracted color list is heavily weighted toward Bootstrap utility classes (alerts, buttons, backgrounds) — the brand's true primary (#004085) is the most distinctive non-gray, non-blue accent in the list, but its usage may be limited to navigation and CTAs
- Font sizes and weights are inferred from common system font stacks — no brand-specific type scale was found
- Animation and transition durations are not specified (likely 150-300ms ease-in-out based on Bootstrap defaults)
- The platform is not Shopify, so checkout flow and cart behavior may differ from standard e-commerce patterns
- Accessibility contrast ratios have not been verified against WCAG standards
- Iconography and illustration style are not documented — the site likely uses FontAwesome or Material Design Icons based on extracted font declarations
