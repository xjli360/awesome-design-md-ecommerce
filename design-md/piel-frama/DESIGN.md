---
version: alpha
name: "Piel Frama"
source_url: "https://www.pielframa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Spanish leather workshop that has been handcrafting cases for mobile devices since 1996, Piel Frama’s digital presence is a study in restrained material honesty — the brand’s signature marigold-orange accent (#ff9a52) cuts through a near-monochrome palette of deep charcoal (#0a0a0a), warm taupe (#85502b), and cool gray (#acaaa6) like a thread of saddle-stitching across dark bridle leather. The site reads as a catalog of craft: product photography dominates, text is set in system sans-serif stacks (Arial, Helvetica Neue, Roboto) at modest weights, and the only decorative flourish is that single orange voltage used sparingly on add-to-cart buttons, navigation highlights, and category markers. There is no hero video, no parallax, no full-bleed imagery — the brand trusts the grain of the leather and the precision of the cut to sell itself. Typography runs small and tight: body copy at 14px, captions at 12px, with generous vertical spacing between product rows. The checkout flow introduces a secondary blue (#b3d7ff) for informational banners and status indicators, but the core identity remains anchored in warm neutrals and that singular orange point of entry. The overall impression is of a workshop showroom translated into a single-page application — utilitarian, unhurried, and confident in the quality of its raw materials.

colors:
  primary: "#ff9a52"
  primary-active: "#ff7c1f"
  primary-disabled: "#ffd4a8"
  ink: "#0a0a0a"
  body: "#383d41"
  muted: "#818182"
  muted-soft: "#acaaa6"
  hairline: "#dae0e5"
  hairline-soft: "#e9ecef"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#85502b"
  accent-cool: "#004085"
  status-info: "#b3d7ff"
  status-success: "#c3e6cb"
  status-warning: "#ffeeba"
  status-error: "#f5c6cb"
  border-focus: "#80bdff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.border-focus}"
    boxShadow: "0 0 0 2px rgba(128, 189, 255, 0.25)"
  text-input-error:
    border: "2px solid {colors.status-error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-price:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    color: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.status-error}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-tile-active:
    border: "2px solid {colors.primary}"
    color: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.border-focus}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 36px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 4px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and primary form submissions. Rendered in the brand's signature marigold orange (#ff9a52) with white text and a subtle 4px corner radius. On hover, the background deepens to #ff7c1f. The disabled state uses a lighter tint (#ffd4a8) to signal inactivity without losing brand identity. Text is set in 14px/600 weight with 0.5px letter spacing for a confident, slightly elevated feel.

**`button-secondary`** — Used for secondary actions like "View Details," "Continue Shopping," or cancel flows. A white background with dark ink text and a 1px hairline border. On hover, the background shifts to soft gray and the border darkens to muted. Maintains the same 40px height and 4px radius as the primary button for visual consistency in form layouts.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft hairline border and 8px corner radius. Contains a square-ratio product image with 4px rounded corners, the product title in body-sm, and the price in title-sm. On hover, the border strengthens to full hairline and a subtle shadow lifts the card. Sale prices render in the primary orange. Each card includes a badge overlay for "New," "Sale," or "Out of Stock" states.

**`category-tile`** — Used on the homepage and category navigation to represent leather types (e.g., "Cowhide," "Nappa," "Vintage"). A white card with 8px radius, 24px padding, and a soft hairline border. When selected or active, the border becomes a 2px orange stroke and the text color shifts to primary. The tile acts as both navigation and filter.

### Navigation
**`nav-bar`** — A fixed 56px header with white background and a single hairline bottom border. Navigation links are set in 13px uppercase with 0.5px tracking, reflecting the brand's utilitarian, workshop-catalog tone. The active page link receives a 2px orange bottom border. The bar collapses to a hamburger menu below 744px.

**`breadcrumb`** — A secondary navigation element appearing on product listing and detail pages. Links are set in 12px caption weight in muted gray, with the current page rendered in full ink. Separators are simple forward slashes in muted-soft gray with 4px horizontal padding.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. A white background with 1px hairline border, 4px radius, and 8px/12px padding. On focus, the border becomes a 2px blue (#80bdff) with a subtle blue box-shadow ring. Error states use a 2px red border (#f5c6cb). Height is consistent at 40px to align with buttons.

**`quantity-selector`** — A compact 36px input for adjusting product quantities on the cart and product detail pages. Uses the same styling as text-input but with tighter padding and a centered number. Typically paired with increment/decrement buttons.

### Footer
**`footer`** — A full-width dark section with deep charcoal (#0a0a0a) background and white text. Links are set in muted-soft gray (#acaaa6) at 14px and shift to full white on hover. The footer contains three columns: company info, customer service links, and legal/payment information. Padding is generous at 64px top/bottom with 24px horizontal gutters.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger, footer stacks vertically, hero section reduces padding to 32px, category tiles become 2-column grid |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, footer maintains 2-column layout, hero uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, footer in 3 columns, hero uses 64px padding |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero image scales but text remains constrained |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the full card surface, not just the title
- Quantity selector buttons are 44px x 44px on mobile
- Hamburger menu icon is 44px x 44px

### Collapsing Strategy
- Top navigation links collapse into a hamburger menu below 744px
- Product grid columns reduce from 4 to 1 as viewport narrows
- Footer columns collapse from 3 to 1 below 744px
- Category filter strip collapses into a dropdown select below 744px
- Hero section text and image stack vertically below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include many framework defaults (Bootstrap alert colors, form validation colors) that may not represent the brand's intentional palette — the primary orange (#ff9a52) and deep charcoal (#0a0a0a) are the only confidently brand-specific colors
- Font stack is entirely system defaults (Arial, Helvetica Neue, Roboto) — no custom or branded typeface was detected
- Hover, active, and focus states for most components are inferred from common patterns rather than extracted from the live site
- Error message styling, form validation states, and toast notifications could not be reliably extracted
- Dark mode is not present on the live site
- The brand may use additional accent colors for seasonal collections or sub-brands that were not captured
- Button padding and height values are estimated from common e-commerce patterns and may differ from the actual implementation
- The checkout flow likely uses Shopify's default styling, which may override brand colors for payment buttons
