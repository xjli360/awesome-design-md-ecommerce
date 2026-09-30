---
version: alpha
name: "Holdit"
source_url: "https://www.holdit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Swedish phone-accessory brand that wraps its products in a near-monochrome palette anchored on #ebebeb, a warm light gray that reads as soft-touch silicone rather than cold digital metal. The brand's only color voltage is #2563eb — a saturated, almost electric blue that appears on every primary CTA, every add-to-cart button, and every active navigation element, creating a single-point focus against the otherwise neutral canvas of #f5f5f5 and #ffffff. The extracted palette reveals a system built on tonal grays — #6b7280 for body text, #9ca3af for muted labels, #898989 for secondary information — with #1d1b1b and #1a1a1d serving as deep ink for headlines and product titles. A sharp #f40000 red appears sparingly, likely for sale badges or error states, providing the only secondary accent in an otherwise restrained system. Typography runs system-native stacks — -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue — suggesting a performance-first approach where loading custom fonts is deemed unnecessary for the clean, utilitarian product pages. The design language favors generous whitespace, soft pill-shaped buttons ({rounded.full}), and product cards with subtle rounding ({rounded.md}) that echo the rounded corners of the phone cases themselves. There is no visual noise — no gradients, no heavy shadows, no decorative flourishes — just a clear hierarchy of product photography against a light gray backdrop, with the blue CTA as the single action point on every page.

colors:
  primary: "#2563eb"
  primary-active: "#1d4ed8"
  primary-disabled: "#93c5fd"
  ink: "#1d1b1b"
  body: "#6b7280"
  muted: "#9ca3af"
  muted-soft: "#898989"
  hairline: "#ebebeb"
  hairline-soft: "#f5f5f5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#f40000"
  dark-surface: "#1a1a1d"
  dark-muted: "#37383a"

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
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-pill-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.canvas}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button with a solid {colors.primary} (#2563eb) background and white text. On hover, the background shifts to {colors.primary-active} (#1d4ed8) for a subtle darkening effect. The disabled state uses {colors.primary-disabled} (#93c5fd) to signal inactivity while maintaining brand consistency. Used for "Add to Cart", "Checkout", and primary form submissions.

**`button-secondary`** — An outlined variant with a white background, {colors.ink} text, and a 2px {colors.hairline} border. On active/hover, the border darkens to {colors.ink} and the background shifts to {colors.surface-soft}. Used for "View Details", "Continue Shopping", and secondary actions where visual hierarchy is needed without competing with the primary button.

**`button-pill-add-to-cart`** — The dedicated add-to-cart button on product pages, identical in styling to `button-primary` but with slightly tighter horizontal padding (24px vs 32px) to accommodate the product card layout. Maintains the full pill shape and blue voltage that signals the single purchase action on the page.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 64px height with a white background and a subtle bottom border in {colors.hairline}. Navigation links use {typography.nav-link} at 14px weight 500, with the active page or section highlighted in {colors.primary}. The bar contains the brand logo on the left, category links in the center, and utility icons (search, cart, account) on the right.

**`nav-link-active`** — The active navigation state uses {colors.primary} text color to indicate the current page or section, providing a clear wayfinding signal against the otherwise neutral nav bar.

### Cards
**`product-card`** — A white card with {rounded.md} (12px) rounding containing a product image, title, and price. The image area uses {colors.surface-soft} as a placeholder background before the product photo loads. The title sits below the image with {spacing.sm} margin, set in {typography.title-sm} (16px weight 600), followed by the price in {typography.price} (16px weight 600) with {spacing.xs} margin. Badges for sales or new arrivals overlay the top-left corner of the image area.

### Badges
**`badge-sale`** — A small, compact badge with a {colors.accent-red} (#f40000) background and white text, set in uppercase 11px weight 700 with 0.5px letter spacing. Rounded at {rounded.xs} (4px) with 2px vertical and 8px horizontal padding. Used to flag discounted items on product cards and listing pages.

**`badge-new`** — Identical in structure to `badge-sale` but using {colors.primary} (#2563eb) as the background color. Used to indicate newly added products or collections.

### Forms
**`text-input`** — A standard text input field with a white background, {colors.ink} text, and a 1px {colors.hairline} border rounded at {rounded.sm} (8px). On focus, the border thickens to 2px and switches to {colors.primary} for a clear active state. Used for search fields, newsletter signups, and checkout form inputs.

**`search-bar`** — A pill-shaped search input with a {colors.surface-soft} background, {colors.body} placeholder text, and {rounded.full} rounding. At 44px height with 10px vertical and 20px horizontal padding, it sits prominently in the nav bar or as a standalone component on collection pages.

### Footer
**`footer`** — A dark section with {colors.dark-surface} (#1a1a1d) background and {colors.muted-soft} (#898989) text. Links use {typography.link} and shift to white on hover for clear interaction feedback. The footer spans the full page width with {spacing.section} vertical padding and contains brand information, customer service links, legal text, and social media icons.

### Product Details
**`quantity-selector`** — A compact input control with a white background, {colors.ink} text, and a 1px {colors.hairline} border rounded at {rounded.sm} (8px). At 40px height, it contains minus/plus buttons flanking a numeric display, used on product pages for adjusting order quantities before adding to cart.

**`color-swatch`** — A circular 32px button representing a product color variant, with {rounded.full} rounding and a 2px transparent border. When selected, the border switches to {colors.ink} to indicate the active choice. Multiple swatches are displayed in a horizontal row below the product image on detail pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; product cards stack vertically; search bar moves to persistent header; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; nav bar shows limited category links; product cards display in 2-column layout; footer uses 2-column link layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all categories; product cards in 3-column grid; footer uses 4-column link layout |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; product cards in 4-column grid; footer maintains 4-column layout with increased horizontal padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Color swatches are 32px with 8px tap padding (effective 48px touch target)
- Nav bar links have 48px minimum tap area
- Quantity selector buttons are 40px with 4px internal padding
- Search bar maintains 44px height for easy thumb targeting

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with a slide-out drawer revealing all category links
- Product grid reduces from 4 columns to 1 column on mobile, with images scaling to full viewport width
- Footer link columns collapse from 4 to 1, stacking vertically with increased spacing between sections
- Search bar transitions from inline in nav to a persistent full-width bar below the header on mobile
- Product detail page moves image gallery above description on mobile, with sticky add-to-cart button at bottom of viewport

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette is heavily weighted toward grays (#ebebeb, #f5f5f5, #6b7280, #9ca3af, #898989, #37383a, #1a1a1d, #1d1b1b) with only two accent colors (#2563eb blue, #f40000 red) — the brand may use additional accent colors for seasonal collections or sub-brands that weren't captured in the extraction
- The #007aff color in the extracted list is likely a system/Apple blue (standard iOS link color) rather than a brand color — excluded from the primary palette
- No custom font family was detected; the site uses system fonts exclusively — the brand may use a custom font for marketing materials or hero sections that isn't loaded on product pages
- Hover states for buttons and links are inferred from common patterns — exact hover colors, transition durations, and animation curves couldn't be extracted
- Error states for form inputs (red borders, error message styling) are not confirmed from the extraction
- Dark mode styling is not present in the extracted data — the brand may not support dark mode, or it may use a different approach
- The brand's Swedish-language site may use different typographic scales or spacing for localized content
- Product card hover states (scale, shadow, border changes) are not confirmed
- Checkout flow styling (Shopify Pay, Klarna integration) may introduce additional colors not captured in the extraction
- The exact border radius values for product cards and buttons are inferred from common patterns — the live site may use slightly different values
- Loading states, skeleton screens, and empty state designs are not documented
