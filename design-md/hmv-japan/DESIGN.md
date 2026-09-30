---
version: alpha
name: "HMV Japan"
source_url: "https://www.hmv.co.jp"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store's digital storefront that feels like a mid-2000s Japanese web portal translated into a shopping engine, anchored on a deep primary blue (#109ad7) that appears on every primary button, navigation link, and category header. The brand's second voltage is a sharp accent red (#df191a) used sparingly — on sale badges, limited-edition flags, and the cart icon — creating a stop-sign urgency against the blue system. The canvas is pure white (#ffffff) with a soft surface (#f7f7f7) for product-card backgrounds, while the body text runs a cool medium gray (#444444) rather than true black, giving the dense product listings a slightly softer read. The typography system is absent of custom fonts in the extracted data, suggesting a system-ui stack that prioritizes legibility over personality — a pragmatic choice for a site that lists thousands of CDs, DVDs, books, and games across dozens of categories. The search bar is a full-width rectangle (`{rounded.none}`) with a blue border, not a pill, and the top navigation is a dense horizontal strip of category links in `{colors.primary}` that scrolls horizontally on mobile. Product cards are compact rectangles with `{rounded.xs}` corners, a thumbnail on the left, and truncated text on the right — optimized for scanning rather than dwelling. The overall mood is utilitarian but not cold: the blue injects a sense of active browsing, the red flags urgency, and the dense information architecture rewards the patient browser who knows what they want.

colors:
  primary: "#109ad7"
  primary-active: "#0086b3"
  primary-disabled: "#7dcce8"
  ink: "#000000"
  body: "#444444"
  muted: "#656565"
  muted-soft: "#a3a3a3"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#df191a"
  accent-red-active: "#b81414"
  accent-blue: "#0000cc"
  accent-green: "#009900"
  link-blue: "#0000ff"
  badge-sale: "#df191a"
  badge-new: "#109ad7"
  badge-limited: "#0000cc"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.46
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  price:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
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
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.primary}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 44px
    border-bottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "10px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-card-thumbnail:
    rounded: "{rounded.xs}"
    width: 80px
    height: 80px
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.accent-red}"
  product-card-old-price:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  category-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    padding: "16px 0"
    border-bottom: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  cart-icon:
    textColor: "{colors.accent-red}"
    height: 24px
    width: 24px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a solid blue rectangle (`{colors.primary}`) with white text, zero border-radius, and 14px semibold type. On hover it darkens to `{colors.primary-active}` (#0086b3). The disabled state uses `{colors.primary-disabled}` (#7dcce8) — a washed-out blue that still reads as active but unclickable. **`button-secondary`** — An outlined variant with a white fill, blue text, and a 1px blue border. Used for "Add to Wishlist" and "View Details" actions where the primary button is reserved for cart-add. **`button-accent-red`** — The urgency button, using `{colors.accent-red}` (#df191a) for "Limited Edition" purchase flows, flash sales, and pre-order confirmations. On hover it deepens to `{colors.accent-red-active}` (#b81414). **`button-ghost`** — A text-only button with no background or border, used for "Cancel", "Back to Results", and inline filter toggles. The text remains `{colors.primary}` blue.

### Cards
**`product-card`** — A compact rectangle with a white background, 4px corner radius, and a soft hairline border (`{colors.hairline-soft}`). The layout is horizontal: an 80px square thumbnail on the left, and a text block on the right containing the title (`{typography.title-md}`), artist/format line (`{typography.body-sm}`), and price in red (`{typography.price}`). On hover, the border switches to `{colors.primary}` blue. **`product-card-title`** — The product name, set in 16px semibold, truncated to two lines. **`product-card-price`** — The current price in 14px bold red, with an optional strikethrough old-price in muted gray. **`badge-sale`**, **`badge-new`**, **`badge-limited`** — Small rectangular tags (4px radius) positioned at the top-left of the thumbnail. Sale is red, New is blue, Limited is a darker blue (#0000cc). Each uses 11px bold white type.

### Navigation
**`nav-bar`** — A 44px horizontal strip of category links (CD, DVD, Books, Games, etc.) scrolling left-to-right on mobile. The background is white, the links are `{colors.primary}` blue, and a 1px hairline border sits at the bottom. **`nav-link`** — Each link has 10px/12px padding and uses 13px semibold type. The active state drops a 2px blue underline and switches the text to black. **`breadcrumb`** — A secondary navigation row in 12px regular type, with muted gray text for the current page and blue links for ancestors. Separators are ">" in `{colors.muted-soft}`.

### Forms & Search
**`text-input`** — A standard 40px-tall input with a white fill, 1px hairline border, and 14px body type. On focus, the border turns `{colors.primary}` blue. **`search-bar`** — The primary search field, identical to `text-input` but with a persistent blue border and a 40px square blue submit button (`{colors.primary}`) attached to the right. The submit button contains a white magnifying-glass icon. There is no rounded search pill — the brand uses sharp rectangles throughout.

### Footer
**`footer`** — A full-width section with a soft gray background (`{colors.surface-soft}`), 13px body text, and a 1px hairline top border. Links are `{colors.primary}` blue. The footer contains columns for "Help", "About HMV", "International", and "Follow Us", each with a 16px semibold title in `{colors.ink}`.

### Pagination
**`pagination`** — A row of page-number buttons below the product grid. The active page uses a solid blue background (`{colors.primary}`) with white text, while inactive pages are transparent with blue text. Each button is a compact rectangle with 4px/8px padding and no border-radius. Previous/Next arrows are text links in `{colors.primary}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to a hamburger menu; search bar becomes full-width; product cards stack vertically with thumbnail above text; footer columns stack; category header font drops to 18px |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows first 6 categories with a "More" dropdown; search bar is 60% width; product cards remain horizontal; footer shows 2 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar visible; search bar is 40% width centered; product cards show 3 per row; footer shows 4 columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; search bar max-width 400px; product cards show 4 per row |

### Touch Targets
- All buttons and links have a minimum touch target of 44px x 44px
- Nav-bar links have 10px/12px padding, meeting the 44px height requirement
- Product card tap area is the full card (80px+ height)
- Pagination buttons are 32px x 32px minimum, with 4px padding on each side

### Collapsing Strategy
- Top nav-bar collapses to a hamburger menu below 744px, revealing a full-screen overlay with all categories
- Product grid collapses from 4 columns to 1 column below 744px
- Footer columns collapse from 4 to 1 below 744px
- Search bar collapses from centered 40% to full-width below 744px
- Breadcrumb truncates to "Home > ... > Current Page" below 744px
- Category headers lose their bottom border on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font-family declarations were extracted; the system-ui stack is an assumption based on common practice for Japanese e-commerce sites. The actual brand may use a Japanese-specific font like "Noto Sans JP" or "Hiragino Kaku Gothic".
- Hover states for product cards, buttons, and links are inferred from common patterns, not extracted from the live site.
- The exact border-radius values for product cards (4px) and buttons (0px) are inferred from the extracted color data and common Japanese e-commerce patterns, not directly extracted.
- No extracted data for error states (form validation, 404 pages, empty search results).
- No extracted data for dark mode or high-contrast mode.
- The brand may have a sub-brand palette for HMV&BOOKS (the combined store format) that wasn't captured.
- The extracted hex list includes several blues (#0000cc, #0000ff) and a green (#009900) that may be social-media icon colors or checkout-widget colors rather than brand colors. The primary blue (#109ad7) and accent red (#df191a) are the most distinctive and likely brand colors.
- No extracted data for loading states, skeleton screens, or animation timing.
- The brand's logo and icon set (HMV dog, etc.) were not analyzed.
- No extracted data for print stylesheets or email templates.
