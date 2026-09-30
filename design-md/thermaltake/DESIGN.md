---
version: alpha
name: "ThermalTake"
source_url: "https://www.thermaltake.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-contrast gaming ecosystem built on a foundation of deep grays (#222222, #303030, #343434) and a single electric accent — #006bb4, a cool, saturated blue that appears on every primary CTA, navigation highlight, and product badge. The palette is deliberately restrained: the brand trusts its hardware's RGB lighting and liquid-cooling loops to provide the color, not the interface itself. Surfaces stack from #f8f8f8 canvas through #e5e5e5 hairline to #c6c6c6 muted, creating a clean, almost industrial hierarchy that reads as serious and performance-oriented. The one exception is #e02b27, a warning red used sparingly for sale tags and error states, and #ff5501, an orange accent that occasionally surfaces on limited-edition or "Toughpower" branded components. Typography runs Open Sans and Roboto at moderate weights — display heads sit at 500–600 weight rather than the aggressive 700+ common in gaming, signaling that ThermalTake positions itself as premium hardware rather than esports spectacle. Buttons carry {rounded.sm} corners (8px) — enough to feel intentional, not soft. Product cards use {rounded.md} (12px) with subtle #e5e5e5 borders, and the nav bar is a full-width #222222 strip with white text, a classic dark-header gaming layout. The overall impression is of a toolmaker's interface: functional, high-contrast, and designed to recede behind the glowing hardware it sells.

colors:
  primary: "#006bb4"
  primary-active: "#005a99"
  primary-disabled: "#8cbce0"
  ink: "#222222"
  body: "#343434"
  muted: "#676767"
  muted-soft: "#c6c6c6"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#f8f8f8"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#e02b27"
  accent-orange: "#ff5501"
  dark-bg: "#222222"
  dark-surface: "#303030"
  dark-hairline: "#545b62"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-dark-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "rgba(0, 107, 180, 0.08)"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.dark-bg}"
    height: 56px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-item-active:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  nav-link-item-hover:
    backgroundColor: "rgba(255, 255, 255, 0.05)"
    textColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-price-sale:
    typography: "{typography.price}"
    textColor: "{colors.accent-red}"
  product-price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-banner-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 24px 24px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 12px 0
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
    rounded: "{rounded.sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  category-tab-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 8px"
  rating-stars:
    textColor: "#ff5501"
    height: 16px
  review-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 8px 12px
  quantity-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with #006bb4 blue and white text. On hover, it shifts to #005a99 with no border change. The disabled state uses #8cbce0, a washed-out version of the primary. All primary buttons use {rounded.sm} (8px) and 44px height for comfortable touch targets. **`button-secondary`** — An outlined variant on white background with a 2px #e5e5e5 border. On hover, the border switches to #006bb4 and the background gains a subtle #f0f0f0 fill. **`button-dark`** — For use on light backgrounds where a dark button is needed, filled with #222222 and white text. Active state shifts to #303030. **`button-ghost`** — A text-only button in primary blue with no background. Hover adds a 8% opacity blue tint. **`button-accent-red`** — A compact, high-urgency button in #e02b27 used for sale CTAs and clearance badges.

### Cards
**`product-card`** — The standard product display card on white background with a 1px #e5e5e5 border and {rounded.md} (12px) corners. On hover, the border becomes #006bb4 and a subtle box shadow lifts the card. The product image area uses {rounded.sm} (8px) and a 1:1 aspect ratio. **`product-badge`** — Small uppercase labels in primary blue with white text and {rounded.xs} (4px). Three variants exist: default (blue), sale (red #e02b27), and new (orange #ff5501). **`product-price`** — The current price uses 20px bold Open Sans in #222222. Sale prices render in #e02b27 with the original price struck through in #676767.

### Navigation
**`nav-bar`** — A full-width dark header at 64px height with #222222 background and white uppercase nav links. On scroll, it compresses to 56px. **`nav-link-item`** — Uppercase 14px bold links with 0.5px letter spacing. Active items get a 10% white overlay background; hover items get 5%. **`nav-dropdown`** — A white dropdown panel with {rounded.sm} and 8px vertical padding, appearing below the nav bar on hover or click. **`category-strip`** — A horizontal scrollable strip of category tabs on #f8f8f8 background. **`category-tab`** — Individual tabs in muted gray that switch to filled primary blue when active, with {rounded.sm} corners.

### Forms
**`text-input`** — Standard text input at 44px height with 1px #e5e5e5 border and {rounded.sm}. On focus, the border thickens to 2px #006bb4. Error state uses 2px #e02b27. **`select-input`** — Matches text-input styling for visual consistency. **`search-bar`** — A pill-shaped search input with {rounded.full}, 44px height, and a magnifying glass icon in #676767. On focus, the border becomes 2px primary blue. **`quantity-selector`** — A compact horizontal control with decrement/increment buttons flanking a central number display, all within a 44px high container with {rounded.sm} and 1px hairline border.

### Footer
**`footer`** — A dark section at 48px top padding with #222222 background. Links render in #c6c6c6 and shift to white on hover. Section headings use 16px bold white text. The footer typically contains 4-5 columns of links plus social icons and legal text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; category strip becomes horizontal scroll; footer stacks to single column; hero reduces to 40px padding; product cards use full width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only; category strip remains scrollable; footer shows 2 columns; hero at 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; category strip shows all tabs; footer shows 4 columns; hero at 64px padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; all layouts centered; hero may feature larger typography |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44px height
- Nav links have 8px horizontal padding with 44px minimum touch area
- Quantity selector buttons are 44px × 44px minimum
- Pagination items have 44px touch targets with 8px padding
- Category tabs have 44px minimum height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid collapses from 3 columns → 2 columns → 1 column
- Footer columns collapse from 4 → 2 → 1
- Category strip becomes horizontally scrollable below 744px
- Hero banner text reduces from display-xl to display-lg on mobile
- Product card badges stack vertically on narrow screens
- Search bar collapses to icon-only on mobile, expanding on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover/focus/active state colors for all interactive elements could not be reliably extracted from the live site; some states are inferred from common patterns
- Dark mode variant is not present on the live site; all extracted colors are from light mode
- Sub-brand palettes (Toughpower, Level 20, etc.) may have distinct accent colors not captured in the global extraction
- Error message styling (background, border, icon) was not extractable from the static HTML
- Loading states (spinners, skeleton screens) are not documented
- Animation timing and easing curves are not extracted
- The exact font stack order and weight availability for Open Sans and Roboto may vary; the listed stacks combine all found declarations
- Shopify checkout widget colors (green, blue, etc.) appear in the extracted hex list but are not part of the brand's design system — they have been excluded
- Social media icon colors and brand-specific swatches (YouTube red, Twitter blue) are not captured
- The accent-orange (#ff5501) appears infrequently and may be a legacy or campaign-specific color rather than a core token
