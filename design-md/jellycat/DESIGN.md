---
version: alpha
name: "Jellycat"
source_url: "https://www.jellycat.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single dark charcoal hex #313131 anchors Jellycat's entire digital presence — not as a background but as the typographic ink for product names, descriptions, and navigation, creating a deliberate contrast against the soft, almost powdery white canvas that surrounds each plush creature. The brand's visual language is one of careful restraint: product photography does the emotional work while the interface steps back into a minimal grid of generous whitespace and rounded corners that never exceed {rounded.md}. There are no bright accent colors competing with the toys; instead, the system relies on a muted gray scale (#6a6a6a for secondary text, #dddddd for hairline borders) to maintain hierarchy without introducing visual noise. Buttons appear as simple outlined rectangles with {rounded.sm} corners, their typography set in the system's default sans-serif stack at a modest 14px — the brand trusts the plush itself, not the button, to drive conversion. Product cards use a clean white surface with a subtle shadow, the creature's name set in a weight 600 title that sits just above a muted price. The overall effect is that of a gallery: each Jellycat animal is an artwork on a white wall, the interface a discreet label beside it.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#c13515"
  sold-out-badge: "#6a6a6a"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 0"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "12px 16px 4px"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "0 16px 12px"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  sold-out-badge:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
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
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Bag" and checkout initiation. Rendered as a solid dark charcoal rectangle with white text, 8px corner radius, and 44px height. On hover, the background deepens to `#1a1a1a`. The disabled state uses a medium gray background with reduced opacity text. The button carries no icon — just centered label text in 14px medium weight.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping." Uses a white background with a 1px hairline border and dark charcoal text. On hover, the border switches to the primary color and the background shifts to the soft surface tone. Height and typography match the primary button for visual alignment in forms.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px corner radius and a subtle drop shadow (1px offset, 3px blur, 8% opacity black). The card contains a full-width product image with rounded top corners, followed by the product name in 16px semibold and the price in 14px muted gray. No hover state changes the card itself — the image may swap to an alternate view, but the card remains static to keep focus on the plush.

**`product-card-title`** and **`product-card-price`** — Internal spacing tokens for the card's text block. The title sits 12px from the image bottom and 16px from the card edge; the price follows 4px below with 12px bottom padding.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a 1px soft hairline bottom border. Contains the brand logo on the left, a centered search bar, and right-aligned links (Account, Wishlist, Bag). The nav uses 14px medium weight type and collapses to a hamburger menu on mobile.

**`nav-link`** and **`nav-link-active`** — Inline navigation items with transparent background. The active state is indicated by a 2px solid primary-color bottom border. No rounded corners — the underline is the only indicator.

### Badges
**`sale-badge`** — A small red-orange badge (`#c13515`) with uppercase 11px semibold white text, 4px corner radius, and 4px/8px padding. Used to flag discounted items on product cards and listing pages.

**`sold-out-badge`** — A medium gray badge with the same dimensions and typography as the sale badge. Indicates out-of-stock items without removing them from the grid.

### Forms
**`text-input`** — Standard 44px text input with 8px corner radius, 1px hairline border, and 12px/16px padding. On focus, the border switches to the primary color. Used for email signup, search queries, and address forms.

**`quantity-selector`** — A compact 44px input for adjusting item quantities in the bag or on the product page. Uses 16px body type, 8px corner radius, and a hairline border. Typically paired with minus/plus buttons on either side.

### Search
**`search-bar`** — A pill-shaped (full radius) 44px search field with a soft gray background. On focus, the background turns white and a primary-color border appears. The search bar sits in the center of the nav bar on desktop and expands to full width on mobile.

### Footer
**`footer`** — A soft gray section with 48px vertical padding and 16px horizontal padding. Contains link columns in 14px regular weight, social icons, and legal text in 12px caption. Links are muted gray by default and darken to ink on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; search bar expands to full width below logo; footer stacks vertically; quantity selector becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar remains centered; footer columns in two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar at 400px max-width; footer in four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav and footer remain centered within container |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height
- Product card tap targets are the entire card surface, not just text
- Quantity selector plus/minus buttons are 44x44px tap areas
- Nav hamburger icon is 44x44px
- Search bar is 44px tall with full-width tap target

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns collapse from 4 to 2 to stacked single column
- Search bar moves from nav center to full-width below logo on mobile
- Secondary navigation (category links) collapses to a horizontal scrollable strip on mobile
- Breadcrumbs truncate with ellipsis on mobile, showing only current page and parent

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site; the remaining colors in the palette are inferred from common e-commerce patterns and the brand's visual tone. The true secondary accent, if any, could not be determined.
- No custom font family was found — the site uses the system font stack. A custom typeface (e.g., a proprietary Jellycat font) may exist but was not detected in the extracted CSS.
- Hover and focus states for most components are inferred from standard web patterns, not extracted from the live site.
- Error states for form inputs (validation colors, error messages) were not observed.
- The brand's mobile navigation pattern (hamburger vs. bottom tab bar) is assumed based on common practice; actual implementation may differ.
- Dark mode or high-contrast mode styles, if they exist, were not captured.
- Sub-brand or seasonal color palettes (e.g., holiday collections, licensed characters) are not represented.
- The exact shadow values for product cards are estimated; the live site may use different blur/spread values.
