---
version: alpha
name: "eStarland"
source_url: "https://www.estarland.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A retro game retailer that operates on a lean, high-contrast system anchored by a single dark gray (#313131) that serves as both primary ink and brand accent — there is no secondary color, no gradient, no decorative palette. The site reads as a utilitarian marketplace built for collectors who care about stock lists and price drops, not visual flourish. Body text runs at 14px in a system-ui stack (Arial, Helvetica Neue, sans-serif) with no custom typeface, a deliberate choice that prioritizes page speed and scannability over typographic personality. Buttons are compact rectangles at 32px height with 8px rounding ({rounded.sm}), using the same #313131 fill as the nav bar and footer — the brand treats every interactive surface as a functional container rather than a decorative element. Product cards stack in a dense grid with thin 1px hairlines, each card holding a small thumbnail, a game title in 13px bold, and a price in the same #313131. The search bar sits prominently at the top of every page, a full-width white field with a magnifying-glass icon and no placeholder text — the assumption being that users arrive knowing exactly what they want. The overall feel is that of a well-organized warehouse catalog: no hero imagery, no lifestyle photography, no brand storytelling. Every pixel earns its place by supporting the core transaction — finding a retro game and adding it to cart.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6a6a6a"
  muted-soft: "#8a8a8a"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  price-green: "#2e7d32"
  stock-green: "#388e3c"
  sold-out-red: "#c62828"
  badge-gold: "#f9a825"
  badge-silver: "#9e9e9e"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica Neue, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 8px 16px
    height: 32px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 7px 15px
    height: 32px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    padding: 7px 15px
    height: 32px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "2px solid {colors.sold-out-red}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
    padding: "0 {spacing.base}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
    height: 48px
  nav-link-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 {spacing.md}"
    height: 40px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    height: 120px
    width: 120px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    margin: "{spacing.xs} 0 0 0"
  product-card-price:
    typography: "{typography.button-md}"
    textColor: "{colors.primary}"
    margin: "{spacing.xxs} 0 0 0"
  product-card-stock-badge:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-sold-out-badge:
    backgroundColor: "{colors.sold-out-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    padding: "{spacing.xxs} 0"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    height: 28px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    height: 28px
  category-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
    border: "1px solid {colors.hairline}"
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
  cart-badge:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 6px"
    minWidth: 20px
    height: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Submit." A compact 32px tall rectangle with 8px rounding ({rounded.sm}) filled in the brand's dark gray (#313131). Text is white, bold at 14px. On hover, the fill deepens to `{colors.primary-active}` (#1a1a1a). When disabled, the fill shifts to `{colors.primary-disabled}` (#b0b0b0) with no border change — the button simply fades into the background.

**`button-secondary`** — Used for secondary actions like "View Details," "Cancel," and "Clear Filters." A white button with a 1px hairline border and dark gray text. On hover, the border thickens to the primary color and the background shifts to `{colors.surface-soft}`. Same 32px height and 8px rounding as the primary button, maintaining visual rhythm.

**`pagination-button`** — Small square buttons (28px tall) used in the page-number strip at the bottom of product listings. Default state is white with a hairline border and 4px rounding. The active page uses the primary fill with white text. Hover state adds a subtle background tint.

### Navigation
**`nav-bar`** — A fixed 48px dark gray bar spanning the full viewport width. Contains the brand logo on the left and category links (Nintendo, PlayStation, Xbox, Sega, etc.) on the right. No dropdowns — each link goes to a filtered product listing. The bar uses `{typography.nav-link}` at 14px bold white.

**`nav-link`** — Individual navigation items with 12px horizontal padding. Active state uses `{colors.primary-active}` as background. No underline or border indicators — the brand relies on background color change alone to signal current section.

**`breadcrumb`** — A thin row of muted gray text (12px) showing the current page path (e.g., Home > Nintendo > NES > Games). The active (last) item uses the ink color. No separators other than the ">" character. Sits directly above the page title.

### Cards
**`product-card`** — The core content unit of the site. A 120px square thumbnail sits at the top, followed by the game title in 13px bold, then the price in 14px bold dark gray. The card has a 1px soft hairline border and 4px rounding. On hover, the background shifts to `{colors.surface-soft}` and the border darkens. Stock status appears as a small badge in the top-right corner of the thumbnail — green for "In Stock," red for "Sold Out."

**`product-card-stock-badge`** — A small green rectangle (2px vertical padding, 6px horizontal) with white text reading "In Stock." Uses 11px bold type and 4px rounding. Positioned absolutely over the top-right of the product thumbnail.

**`product-card-sold-out-badge`** — Same dimensions and positioning as the stock badge, but filled with a deep red (#c62828) and reading "Sold Out." The entire card gets a slight opacity reduction (0.6) when sold out, signaling unavailability without removing the listing.

### Forms
**`text-input`** — A 36px tall white input field with a 1px hairline border and 8px rounding. On focus, the border thickens to 2px and turns to the primary dark gray. Error state swaps the border to `{colors.sold-out-red}`. Placeholder text uses `{colors.muted-soft}` at 14px regular weight.

**`search-bar`** — A full-width white input field (40px tall) with a magnifying-glass icon on the left. No placeholder text — the brand assumes users know what they're looking for. On focus, the border thickens to 2px primary. The search bar sits in a dedicated row below the nav bar, spanning the full content width.

**`category-filter`** — A pill-shaped filter button (32px tall) used in the sidebar or above product listings. Default is white with a hairline border. Active state fills with the primary dark gray and inverts text to white. Multiple filters can be active simultaneously.

### Footer
**`footer`** — A dark gray bar matching the nav bar, containing links to About Us, Contact, Shipping Info, Returns, and Privacy Policy. Links are 14px regular weight white text with 2px vertical padding. The footer uses `{spacing.lg}` vertical padding and `{spacing.base}` horizontal padding. No columns or grid — links stack vertically in a single column on mobile and spread horizontally on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), nav links collapse to hamburger menu, footer links stack vertically, search bar remains full-width but reduces height to 36px |
| Tablet | 744–1128px | Two-column product grid, nav links show as abbreviated text (icons only for categories), footer links spread to two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav link text visible, sidebar category filters appear, footer links spread horizontally |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centers content, nav bar spans full viewport width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 32px height and 32px width
- Nav links have 12px horizontal padding, ensuring at least 44px tap targets on mobile
- Search bar is 40px tall on all breakpoints (36px on mobile) — exceeds the 32px minimum
- Category filter buttons are 32px tall with 12px horizontal padding
- Pagination buttons are 28px tall — slightly below the 32px ideal but acceptable for the compact design

### Collapsing Strategy
- Nav links collapse to a hamburger menu at < 744px, revealing a full-screen overlay with all category links
- Product grid collapses from 4 columns to 1 column as viewport shrinks
- Sidebar category filters collapse to a horizontal scrollable strip above the product grid on mobile
- Footer links collapse from horizontal row to single vertical stack on mobile
- Breadcrumb text truncates on mobile, showing only the last two path segments with "..." for earlier segments

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was successfully extracted from the live site. The brand's true palette may include additional colors (e.g., a green for stock indicators, red for sold-out badges, gold for cart badges) that were inferred from common e-commerce patterns rather than extracted from the site. These inferred colors are marked with descriptive names (price-green, stock-green, sold-out-red, badge-gold, badge-silver) and should be verified against the actual site.
- No font-family declarations beyond the system-ui stack were found. The brand may use a custom web font that wasn't detected during extraction.
- Hover, focus, and active states for all components are inferred from common patterns — the actual site may use different transition durations, opacity values, or color shifts.
- Error styling for forms (text-input-error) is speculative — the actual error state may use a different color, icon, or layout pattern.
- The cart badge (badge-gold) color is inferred from common e-commerce patterns — the actual site may use a different accent color for cart indicators.
- No dark mode or high-contrast mode tokens were extracted. The brand may not support these modes.
- Spacing values (spacing block) are based on common e-commerce patterns rather than extracted from the site. The actual spacing system may differ.
- Typography sizes (display-xl through caption) are inferred from common patterns for a text-heavy retail site. The actual type scale may use different sizes or weights.
- The product card dimensions (120px thumbnail) are estimated based on typical retro game card layouts — the actual dimensions may vary.
- No animation or transition tokens were extracted. The brand may use subtle transitions for hover states that aren't captured here.
