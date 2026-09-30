---
version: alpha
name: "Ohana Ukuleles"
source_url: "https://www.ohana-music.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A monochrome stage for instrument craft, where #121212 ink on #dedede canvas reads less as minimalism and more as a deliberate silence — the kind that lets a koa wood grain or a mother-of-pearl rosette speak at full volume. The brand's Shopify storefront uses no decorative color beyond the product itself; every button, badge, and nav bar is rendered in near-black on near-white, with the sole exception of a warm amber accent (#c87a2b) that appears on sale badges and limited-edition callouts, borrowed directly from the honey tone of a well-aged acacia top. Typography runs a single sans-serif stack at modest weights — display headlines sit at 24px weight 600, body text at 15px weight 400 — and the brand trusts high-resolution product photography over typographic hierarchy. Cards use a soft 12px radius (`{rounded.md}`) that echoes the gentle curve of a ukulele body, while the primary CTA button is a flat 48px-high rectangle (`{rounded.sm}`) in #121212 with white text, a quiet invitation rather than a shout. The checkout flow inherits Shopify's default widget colors, but the brand's own canvas remains resolutely neutral, letting the instruments — sopranos, concerts, tenors, and the occasional pineapple-shaped novelty — provide all the warmth.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#6a6a6a"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#5a5a5a"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#c87a2b"
  accent-amber-soft: "#f0d6b0"
  sale-badge-bg: "#c87a2b"
  sale-badge-text: "#ffffff"
  stock-badge-bg: "#e0e0e0"
  stock-badge-text: "#121212"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-amber}"

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
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid #d32f2f"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  stock-badge:
    backgroundColor: "{colors.stock-badge-bg}"
    textColor: "{colors.stock-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    color: "{colors.on-primary}"
    opacity: 1
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 28px"
    height: 48px
    width: "100%"
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the storefront, rendered in near-black (#121212) with white text and a subtle 8px radius (`{rounded.sm}`). On hover, the background deepens to pure black (`{colors.primary-active}`). The disabled state shifts to a muted gray (`{colors.primary-disabled}`) with reduced opacity. Used for "Add to Cart", "Checkout", and primary navigation actions.

**`button-secondary`** — An outlined alternative with a white background, black text, and a 1px hairline border (`{colors.hairline}`). On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Used for "View Details", "Compare", and secondary actions where visual hierarchy is needed without full black.

**`button-tertiary-text`** — A text-only button with no background or border, using `{typography.button-md}` in `{colors.ink}`. Used for "Cancel", "Clear Filters", and other low-emphasis actions. Hover state adds a subtle underline.

**`button-amber`** — The sole accent-colored button, using `{colors.accent-amber}` (#c87a2b) as background with white text. Reserved for limited-edition drops, pre-order campaigns, and seasonal promotions. The warm amber echoes the honey tone of aged acacia and mahogany ukulele bodies.

### Cards
**`product-card`** — A clean white card with a 12px radius (`{rounded.md}`) and no border, relying on the product image and whitespace for structure. The image occupies the top portion with matching top-radius corners (`{rounded.md} {rounded.md} 0 0`). Below, the product title uses `{typography.title-sm}` and the price uses `{typography.price}` in bold 18px. Sale prices render in `{colors.accent-amber}` via `{typography.price-sale}`.

**`sale-badge`** — A small uppercase badge with an amber background (`{colors.sale-badge-bg}`) and white text, using 4px radius (`{rounded.xs}`). Positioned at the top-left of product images. The badge text reads "SALE" or a discount percentage.

**`stock-badge`** — A neutral badge with a light gray background (`{colors.stock-badge-bg}`) and black text, used for "SOLD OUT", "BACK IN STOCK", or "NEW" labels. Same dimensions and radius as the sale badge.

### Navigation
**`nav-bar`** — A 64px-tall white bar with a soft bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — 13px uppercase with 0.5px letter spacing. The active link is underlined with a 2px black border (`{colors.ink}`), while inactive links render in `{colors.muted}`. The logo sits left-aligned, with the cart icon and search icon right-aligned.

**`breadcrumb`** — A secondary navigation element using `{typography.caption}` in `{colors.muted}`. The active breadcrumb (current page) uses `{colors.ink}`. Separators are a simple "/" in `{colors.muted-soft}`.

### Forms
**`text-input`** — A 48px-tall input field with white background, 8px radius (`{rounded.sm}`), and a 1px hairline border (`{colors.hairline}`). On focus, the border switches to `{colors.ink}`. Error state uses a red border (#d32f2f). Placeholder text uses `{colors.muted-soft}`.

**`select-input`** — Matches the text-input dimensions and styling, used for dropdown menus (size, quantity, sort order). The dropdown arrow is rendered in `{colors.muted}`.

**`quantity-selector`** — A compact 40px-tall input for product quantities, with a hairline border and centered text. Plus/minus buttons flank the numeric value.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and hairline border. On focus, the border switches to `{colors.ink}`. The search icon sits inside the left padding. Used in the header and on the search results page.

### Footer
**`footer-section`** — A full-width black section (`{colors.primary}`) with white text. Links render in white at 80% opacity, increasing to full opacity on hover. The footer contains columns for customer service, about us, and social links. Social icons are rendered in white.

### Pagination
**`pagination-button`** — A small button with white background, black text, and a hairline border. The active page uses `{colors.primary}` as background with white text. Used on collection and search results pages.

### Accordion
**`accordion-header`** — A clickable row with a bottom border, using `{typography.title-sm}`. The header includes a chevron icon that rotates on open. Content below uses `{typography.body-sm}` in `{colors.body}`.

### Tabs
**`tab-active`** — An underlined tab with a 2px black bottom border and `{typography.button-sm}`. Inactive tabs use `{colors.muted}` with no underline. Used on product detail pages for "Description", "Specifications", "Reviews".

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero section reduces padding to 32px; search bar moves to full-width below nav; footer columns stack vertically; buttons become full-width |
| Tablet | 744–1128px | Nav bar shows condensed links (no text labels, only icons for cart/search); product cards display in 2-column grid; hero section uses 48px padding; footer shows 2-column layout |
| Desktop | 1128–1440px | Full nav bar with text labels; product cards in 3-column grid; hero section uses 64px padding; footer shows 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product cards in 4-column grid; hero section uses 80px padding; all elements remain centered |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav bar hamburger icon uses 48px tap target
- Quantity selector plus/minus buttons use 40px tap target
- Product card tap target covers the entire card area
- Footer links use 44px minimum tap target

### Collapsing Strategy
- Primary nav collapses to hamburger menu at < 744px, with a slide-in drawer from the left
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer columns collapse from 4-column to 2-column at tablet, to single column at mobile
- Product image gallery collapses from thumbnail strip to swipeable dots on mobile
- Accordion sections remain collapsed by default on all breakpoints
- Search bar collapses from inline to full-width overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the typography block uses a generic sans-serif stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`) as a best-guess placeholder. The actual brand font may differ.
- Only two hex colors were extracted from the live site (#dedede, #121212). The accent amber (#c87a2b) was inferred from sale badge imagery and should be verified against the brand's actual design tokens.
- Hover and focus states for most components were not extractable from static HTML/CSS; the active states defined above are reasonable defaults but may not match the live site's exact implementation.
- Error styling for forms (red border) is a standard convention, not a confirmed brand token.
- Dark mode is not supported and no dark mode tokens were found.
- The Shopify checkout flow uses default Shopify widget colors (blue, green) that are not part of the Ohana brand palette.
- Social media icon colors (Facebook blue, Instagram gradient, YouTube red) are standard platform colors and not brand tokens.
- No animation or transition durations were extractable; standard 200-300ms ease-in-out is assumed.
- The brand's sub-brand or collection-specific color variations (e.g., "Pineapple Series", "Mahogany Series") could not be determined.
