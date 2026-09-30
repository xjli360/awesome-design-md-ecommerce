---
version: alpha
name: "Innersloth Shop"
source_url: "https://shop.innersloth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A marigold-yellow #e9be33 anchors this indie merch storefront — the same saturated, slightly warm yellow that signals the Among Us crewmate's iconic suit, here used as the primary brand voltage across CTAs, badges, and accent elements. The palette reads as a deliberate contrast to the game's dark, paranoia-soaked spaceship interiors: #31373d ink provides a near-black counterweight, while #6c6c6c muted and #eaeaea canvas keep the shopping experience airy and approachable. What makes the system feel distinctly Innersloth is the tension between playful yellow and serious dark gray — a #479ccf blue appears as a secondary accent, perhaps echoing the game's admin-room terminals or the cyan crewmate, but never overpowers the marigold. Typography defaults to Arial and Helvetica Neue at standard weights, a pragmatic choice that lets the color system and product photography carry personality rather than a custom typeface. The storefront appears temporarily unavailable, but the extracted palette suggests a system built on generous white space, high-contrast buttons, and a restrained two-accent color architecture that avoids the over-designed trap of most gaming merch stores.

colors:
  primary: "#e9be33"
  primary-active: "#d4a92e"
  primary-disabled: "#f4d98a"
  ink: "#31373d"
  body: "#4a4f55"
  muted: "#6c6c6c"
  muted-soft: "#9a9a9a"
  hairline: "#c4c4c4"
  hairline-soft: "#d8d8d8"
  canvas: "#eaeaea"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#31373d"
  accent-blue: "#479ccf"
  accent-blue-active: "#3b87b5"
  badge-red: "#d94f4f"
  badge-green: "#4caf50"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    textColor: "{colors.muted}"
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
    border: 2px solid "{colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 2px solid "{colors.ink}"
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 2px solid "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 2px solid "{colors.badge-red}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: 1:1
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: 0 "{spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 2px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, filled with marigold-yellow `{colors.primary}` and dark `{colors.on-primary}` text for high contrast. On hover and active states, the background deepens to `{colors.primary-active}` (#d4a92e). When disabled, the button shifts to `{colors.primary-disabled}` (#f4d98a) with `{colors.muted}` text, signaling unavailability without visual noise. The 44px height and `{rounded.sm}` corners keep the button compact and friendly, suitable for both product pages and cart actions.

**`button-secondary`** — An outlined alternative with a transparent `{colors.canvas}` background and a 2px `{colors.ink}` border. This button sits alongside primary CTAs for less emphasized actions like "Cancel" or "View Details." On active state, the background fills with `{colors.surface-soft}` to provide hover feedback while maintaining the border structure. Same 44px height and `{rounded.sm}` corners as the primary for visual consistency.

**`button-accent-blue`** — A secondary accent button using `{colors.accent-blue}` (#479ccf) as background, reserved for contextual actions like "Chat Support" or "Browse More." The text reads in `{colors.canvas}` white, creating a distinct third tier of interaction that doesn't compete with the primary yellow. This button follows the same sizing and corner radius as the other button variants.

### Cards
**`product-card`** — A clean white card with `{rounded.md}` corners and no background fill beyond the image. The product image sits flush to the top with `{rounded.md} {rounded.md} 0 0` corner treatment, while the title and price stack below with `{spacing.base}` padding. The card relies on the contrast between `{colors.surface-card}` and the surrounding `{colors.canvas}` page background for separation rather than shadows or borders.

**`product-card-image`** — Maintains a 1:1 aspect ratio for consistent grid alignment across product listings. The image fills the top of the card with the same corner radius as the card itself on top edges, creating a seamless visual flow from image to text content.

### Badges
**`badge-new`** — A pill-shaped marigold badge for new arrivals, using `{typography.badge}` (11px, 700 weight, uppercase) with tight 4px 10px padding. The `{rounded.full}` shape and high-contrast `{colors.on-primary}` text make it read as a playful announcement rather than a system notification.

**`badge-sale`** — A red pill badge (`{colors.badge-red}` #d94f4f) for discounted items, using the same typography and shape as the new badge. The red provides immediate visual urgency against the otherwise restrained palette.

**`badge-sold-out`** — A muted gray pill badge (`{colors.muted}` #6c6c6c) for unavailable inventory, using white text for legibility. The gray signals finality without the negative emotional weight of red, appropriate for limited-run indie merch.

### Navigation
**`nav-bar`** — A 64px white header with a subtle `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` at 15px with 0.2px letter spacing for readability. Active links shift to `{colors.primary}` yellow, while inactive links sit in `{colors.muted}` gray. The bar remains fixed at the top of the viewport for persistent access to cart, search, and category navigation.

**`nav-link-active`** — The active navigation state uses `{colors.primary}` yellow text on a transparent background, creating a color-coded indicator for the current section without underlines or heavy visual weight.

**`nav-link-inactive`** — Inactive links sit in `{colors.muted}` gray, providing clear visual hierarchy between the current page and available destinations. The transparent background keeps the nav bar clean and uncluttered.

### Forms
**`text-input`** — A standard input field with white background, `{colors.ink}` text, and a `{colors.hairline}` border. The 44px height matches button sizing for aligned form layouts. On focus, the border thickens to 2px and shifts to `{colors.primary}` yellow, providing clear keyboard focus indication. Error states use a 2px `{colors.badge-red}` border for immediate visual feedback.

**`search-bar`** — A pill-shaped search input with `{rounded.full}` corners, white background, and a `{colors.hairline}` border. The 44px height matches other interactive elements. On focus, the border transitions to 2px `{colors.primary}` yellow, maintaining the brand's signature color association with active states.

### Footer
**`footer`** — A dark footer section using `{colors.ink}` (#31373d) background with `{colors.canvas}` white text for primary content. Links appear in `{colors.muted-soft}` (#9a9a9a) to reduce visual weight while remaining legible against the dark background. The footer uses `{spacing.xl}` vertical padding with `{spacing.base}` horizontal padding for comfortable content breathing room.

**`footer-link`** — Footer navigation links use `{typography.link}` at 14px with `{colors.muted-soft}` gray, creating a clear hierarchy where primary footer text (copyright, brand name) reads in white while navigation options recede into the gray.

### Cart & Quantity
**`cart-badge`** — A small circular badge (20px height, minimum 20px width) using `{colors.primary}` yellow background with `{colors.on-primary}` dark text. The `{rounded.full}` shape creates a pill that expands horizontally with multi-digit counts while maintaining visual consistency. Positioned at the top-right of the cart icon.

**`quantity-selector`** — A compact 36px control group with `{colors.surface-soft}` background and `{rounded.sm}` corners. The increment/decrement buttons sit flush within the selector, each 36px square, using transparent backgrounds and `{typography.button-sm}` for the +/- labels. The central quantity display uses `{typography.body-md}` for clear readability.

### Hero
**`hero-banner`** — A full-width promotional banner using `{colors.ink}` background with white text at `{typography.display-xl}` (32px, 700 weight). The `{spacing.section}` vertical padding creates dramatic breathing room for campaign messaging, product launches, or seasonal promotions.

**`hero-banner-accent`** — An inline accent block within the hero, using `{colors.primary}` yellow background with `{colors.on-primary}` dark text at `{typography.display-md}` (24px, 700 weight). The `{rounded.sm}` corners and `{spacing.base}` / `{spacing.lg}` padding create a highlighted callout that draws immediate attention within the dark hero canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, stacked nav with hamburger menu, full-width hero, reduced padding to `{spacing.base}` |
| Tablet | 744–1128px | Two-column product grid, visible top nav with condensed links, hero maintains `{spacing.section}` padding |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, max-width container at 1128px centered |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44px height for touch accessibility
- Cart badge and quantity selector buttons at 36px minimum — acceptable for secondary controls but should be reviewed for accessibility compliance
- Nav links use minimum 44px tap area even when text is smaller
- Search bar maintains 44px height across all breakpoints

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with full-height overlay drawer
- Product grid collapses from 4 columns to 1 column on mobile, with 2 columns on tablet
- Footer link columns stack vertically on mobile, maintaining `{spacing.base}` between items
- Hero banner text reduces from `{typography.display-xl}` to `{typography.display-md}` on mobile
- Cart summary moves below product listings on mobile, side-by-side on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The live site returned "This store is unavailable" — extracted colors may include Shopify default UI elements rather than intentional brand colors. The marigold yellow (#e9be33) is the most distinctive and likely brand-primary, but its exact usage (buttons, badges, backgrounds) is inferred from gaming merch conventions rather than observed behavior.
- No font-family declarations beyond Arial/Helvetica Neue were found — the brand may use a custom typeface (e.g., a game-themed font) that isn't loaded on the unavailable storefront page.
- Hover, focus, and active states for all components are estimated based on standard darkening/lightening patterns rather than extracted values.
- Error states, loading states, and empty states are entirely speculative.
- Dark mode preferences and alternate color schemes are unknown.
- The accent-blue (#479ccf) role is inferred — it may be a secondary brand color, a link color, or a Shopify default.
- Badge colors (red, green) are estimated — the brand may use different colors for sale/sold-out/new indicators.
- No spacing or typography scale could be extracted from the unavailable page — values are set to standard e-commerce conventions.
- The site may use illustrations, patterns, or game assets that significantly alter the visual system beyond the extracted color palette.
