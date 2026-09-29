---
version: alpha
name: "Baseus"
source_url: "https://www.baseus.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A utilitarian tech-essentials brand that uses #282828 as its anchor — a near-black ink that appears on every product page, nav bar, and spec sheet, giving the interface the same industrial precision as the docking stations it sells. The primary voltage is #fdbc00, a warm marigold that punches through the dark palette on CTAs, badge highlights, and sale tags, reading as functional optimism rather than playful whimsy. Type runs DM Sans across the system at modest weights — display sits at 24px weight 500, body at 14px weight 400, and buttons at 15px weight 600 — a restrained hierarchy that lets product photography and spec tables carry the information load. The brand uses #f5f5f5 as its default canvas, not pure white, which softens the high-contrast product shots and makes the #fdbc00 accents feel warmer by comparison. Cards and inputs use {rounded.sm} (8px) corners — a slight softening of the otherwise rectilinear grid — while badges and notification dots use {rounded.full} for quick visual scanning. The footer is a dense information grid with #282828 background and #888888 link text, signaling that Baseus treats technical specifications and support documentation as core content, not afterthoughts. The overall mood is that of a well-organized tool drawer: dark, clean, every element has a place, and the yellow accent is the one thing that says "press here."

colors:
  primary: "#fdbc00"
  primary-active: "#e5a800"
  primary-disabled: "#fef0b3"
  ink: "#282828"
  body: "#464646"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#f5f5f5"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#282828"
  accent-blue: "#0078ff"
  accent-cyan: "#00aeef"
  accent-green: "#05d92d"
  error: "#dd2c00"
  badge-new: "#ff9600"
  badge-sale: "#dd2c00"
  dark-bg: "#1e2132"
  dark-surface: "#121212"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
    boxShadow: "0 2px 8px rgba(40,40,40,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.badge-sale}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0 {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-row:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    fontWeight: 600
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "4px"
    height: 36px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 28px
    width: 28px
  add-to-cart-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "{spacing.base}"
    borderTop: "1px solid {colors.hairline-soft}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.base} 0"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 500

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with #fdbc00 marigold and dark #282828 text. Used for "Add to Cart," "Buy Now," and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#e5a800) with no scale or shadow change — the color darkens just enough to signal interactivity without animation. Disabled state uses `{colors.primary-disabled}` (#fef0b3) with `{colors.muted}` text, making the button feel faded but still legible.

**`button-secondary`** — An outlined variant on the `{colors.canvas}` background with a `{colors.hairline}` border. Used for "Learn More," "Compare," and secondary product actions. Active state darkens the border to `{colors.muted}`. No fill on hover — the brand avoids ghost-button confusion by keeping secondary buttons visibly bounded.

**`button-ghost`** — A text-only button with no border or background, used in navigation dropdowns and filter panels. Active state adds a `{colors.surface-soft}` background. The brand uses ghost buttons sparingly, preferring the clarity of bordered secondary buttons for most non-primary actions.

### Cards
**`product-card`** — The core product display unit, a white card on `{colors.canvas}` with `{rounded.sm}` corners and no shadow — Baseus relies on the contrast between the white card and the light gray canvas for separation. The image area occupies the top half at a 1:1 aspect ratio, with the title and price stacked below. Sale pricing renders in `{colors.badge-sale}` (#dd2c00) with the original price struck through in `{colors.muted-soft}`.

**`spec-table`** — A bordered table with alternating row lines, used on product detail pages to display technical specifications. Labels use `{colors.muted}` in caption weight, values use `{colors.body}` in body-sm. The table has `{rounded.sm}` corners and a `{colors.hairline-soft}` border, matching the card system.

### Navigation
**`nav-bar`** — A 64px fixed bar on `{colors.canvas}` with a subtle bottom border in `{colors.hairline-soft}`. Navigation links use `{typography.nav-link}` at 14px weight 500 with 0.2px letter spacing. The logo sits left-aligned, category links center-aligned, and utility icons (search, cart, account) right-aligned. On scroll, the bar compresses to 56px with a light box-shadow.

**`search-bar`** — A pill-shaped input field (`{rounded.full}`) with a white background and `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` (#fdbc00). The search bar lives in the nav bar on desktop and expands to full width on mobile.

### Forms
**`text-input`** — Standard form input with `{rounded.sm}` corners, white background, and `{colors.hairline}` border. Focus state uses `{colors.primary}` border. Error state uses `{colors.error}` (#dd2c00) border with error text below. The brand does not use floating labels — placeholder text in `{colors.muted}` is the standard approach.

**`quantity-selector`** — A compact horizontal control with decrement and increment buttons flanking a numeric display. The container has `{rounded.sm}` and a `{colors.hairline}` border, while the buttons have `{rounded.xs}` and a white background. Used on product detail pages and cart line items.

### Badges
**`badge`** — Small uppercase labels in #fdbc00 with dark text, using `{rounded.full}` for a pill shape. Used for "Best Seller," "Top Rated," and category tags. **`badge-new`** uses #ff9600 orange for "New Arrival" indicators. **`badge-sale`** uses #dd2c00 red for discount labels. All badges share the same `{typography.badge}` sizing at 11px weight 700 with 0.3px letter spacing.

### Footer
**`footer`** — A dense information footer on `{colors.ink}` (#282828) background. Link text uses `{colors.muted-soft}` (#aaaaaa) on hover and `{colors.muted}` (#888888) by default. Column headings use `{colors.surface-card}` (#ffffff) in `{typography.title-sm}`. The footer includes four columns (Support, Products, Company, Legal) plus a bottom bar with payment icons and copyright text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, full-width search bar, hamburger menu replaces category nav, footer collapses to stacked columns, quantity selector becomes full-width |
| Tablet | 744–1128px | Two-column product grid, condensed nav with dropdowns, search bar shrinks to icon + expand, footer shows two-column layout |
| Desktop | 1128–1440px | Three-to-four-column product grid, full nav with category links, persistent search bar, four-column footer |
| Wide | > 1440px | Max-width container at 1440px, product grid expands to four columns, hero banners use full bleed with content constrained to container |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons in the nav bar are 40px × 40px with 8px padding around the icon
- Quantity selector buttons are 28px × 28px — below the 44px recommendation but acceptable for the compact control pattern
- Product card tap targets (title, price, image) use the full card area as a link

### Collapsing Strategy
- The primary navigation collapses to a hamburger menu at < 744px, with a slide-out drawer for category links
- The search bar collapses to a magnifying-glass icon that expands to a full-width overlay on tap
- The product grid collapses from 4 columns to 2 columns at tablet, then to 1 column at mobile
- The footer collapses from 4 columns to 2 columns at tablet, then to a single stacked column at mobile
- The spec table converts to a stacked label-value layout at mobile, with each row becoming a two-line block

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While primary button hover was inferred from the active color, hover states for secondary buttons, ghost buttons, and text inputs could not be reliably extracted from the live site. The system assumes a simple color darkening pattern consistent with the primary button.
- **Error states**: Error text styling, error iconography, and form validation patterns were not observed. The error border color (#dd2c00) was extracted from the color palette but its application context is inferred.
- **Dark mode**: The extracted palette includes #1e2132 and #121212, suggesting a dark mode exists, but no dark-mode-specific component tokens or typography adjustments could be verified.
- **Animation and transition**: No timing values, easing curves, or animation patterns were extracted. The brand appears to use minimal animation (no hover scale, no fade transitions on cards).
- **Typography scale**: Font sizes were inferred from common e-commerce patterns and the DM Sans typeface. The exact display, title, and body sizes used on the live site may vary. The extracted font-family was "DM Sans, sans-serif" — the fallback stack is an assumption.
- **Sub-brand palettes**: Baseus may have sub-brand or product-line-specific color variations (e.g., for gaming, audio, or charging accessories) that were not captured in the top-level extraction.
- **Checkout flow**: Shopify checkout styling (Shopify Pay buttons, Klarna badges, Afterpay widgets) was filtered from the extracted colors, but the brand's custom checkout components could not be isolated.
- **Spacing scale**: The spacing tokens follow a standard 4px/8px/12px/16px/24px/32px/48px/64px progression, which is a best-guess for the brand rather than an extracted value.
