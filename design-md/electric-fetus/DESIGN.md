---
version: alpha
name: "The Electric Fetus"
source_url: "https://www.electricfetus.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Minneapolis institution since 1968, The Electric Fetus wraps its counterculture roots in a clean, almost gallery-like white canvas (#ffffff) that lets the product — vinyl, CDs, posters, and oddities — do the shouting. The brand’s voice is quiet but knowing, trusting Arial at 16px for body copy and a restrained 14px for captions, with no display type to compete with the kaleidoscope of album art and T-shirt graphics that fill every shelf. Navigation is a simple horizontal strip of uppercase links in a soft gray (#666666) that turns black (#000000) on hover, a nod to the store’s no-fuss, no-markup ethos. Buttons are solid black rectangles with white text, using {rounded.sm} corners that feel deliberate without being precious — this is a store that sells music, not a brand that sells itself. The search bar is a full-width white field with a subtle {hairline} border and a magnifying-glass icon, sitting below the nav like a utility rather than a hero feature. Product cards are white rectangles with a 1px {hairline} border, a 4px {rounded.xs} corner, and generous 16px padding around the cover art, title, artist, and price. The footer is a dense block of links in 12px Arial, organized into columns, with a copyright line that reads “© 2025 The Electric Fetus” — no newsletter signup, no social icons, no brand story. The site feels like the store: a place where the inventory is the personality.

colors:
  primary: "#000000"
  primary-active: "#333333"
  primary-disabled: "#cccccc"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#000000"
  link-hover: "#666666"
  price: "#000000"
  sale-price: "#cc0000"
  badge-new: "#000000"
  badge-sale: "#cc0000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
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
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.link-hover}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 24px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.ink}"
  product-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-price:
    typography: "{typography.title-sm}"
    color: "{colors.price}"
    marginTop: "{spacing.xs}"
  product-sale-price:
    typography: "{typography.title-sm}"
    color: "{colors.sale-price}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.md}"
  footer-link-item:
    typography: "{typography.footer-link}"
    color: "{colors.muted}"
  footer-link-item-hover:
    color: "{colors.ink}"
  footer-copyright:
    typography: "{typography.caption}"
    color: "{colors.muted-soft}"
    marginTop: "{spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-current:
    color: "{colors.ink}"
  category-link:
    typography: "{typography.body-sm}"
    color: "{colors.link}"
  category-link-hover:
    color: "{colors.link-hover}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
    height: 36px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 44px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  page-section:
    padding: "{spacing.section} {spacing.xl}"
    maxWidth: 1200px
  product-grid:
    display: grid
    gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))"
    gap: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid black rectangle with white text and 8px corner radius. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, the background shifts to `{colors.primary-active}` (#333333). The disabled state uses `{colors.primary-disabled}` (#cccccc) with white text, signaling unavailability without ambiguity.

**`button-secondary`** — An outlined alternative with a white background, black text, and a 1px `{colors.hairline}` border. Used for "Continue Shopping", "View Details", and secondary actions. On hover, the background fills with `{colors.surface-soft}` and the border turns `{colors.ink}`.

**`button-text`** — A text-only button with no background or border, used for inline actions like "Clear Filters" or "Cancel". The text color is `{colors.link}` (black) and shifts to `{colors.link-hover}` (#666666) on hover. No rounded corners, no padding — just the text.

**`button-pill`** — A fully rounded pill button used for category filters and quick-add actions. Same black background and white text as `button-primary`, but with `{rounded.full}` and tighter padding (8px 20px). Uses `{typography.button-sm}` for a more compact footprint.

### Navigation
**`top-nav`** — A 48px-high horizontal bar with white background and a 1px `{colors.hairline-soft}` bottom border. Links are set in `{typography.nav-link}` — 13px Arial bold, uppercase, with 0.5px letter-spacing — and default to `{colors.muted}` (#666666). The active link uses `{colors.ink}` (#000000). No dropdowns, no mega-menus, no search inside the nav — just a clean row of department names.

**`nav-link-active`** — The active state for a top-nav link, distinguished only by color (`{colors.ink}`). No underline, no background change, no border — the brand trusts the user to know where they are.

### Cards
**`product-card`** — A white rectangle with a 1px `{colors.hairline}` border and 4px `{rounded.xs}` corners. Contains the product image (full-width, aspect-ratio 1:1), the title in `{typography.title-sm}` (14px bold), the artist name in `{typography.body-sm}` (14px regular, `{colors.muted}`), and the price in `{typography.title-sm}` (14px bold, `{colors.price}`). On hover, the border changes to `{colors.ink}`. Padding is 16px on all sides.

**`badge-new`** — A small black rectangle with white text, 4px rounded corners, and 2px 8px padding. Uses `{typography.badge}` — 11px Arial bold, uppercase, 0.5px letter-spacing. Positioned at the top-left of the product image.

**`badge-sale`** — Identical in shape to `badge-new`, but with a red background (`{colors.badge-sale}` — #cc0000). Used to mark discounted items.

### Forms
**`search-bar`** — A full-width white input field with a 1px `{colors.hairline}` border, no rounded corners, and 16px Arial text. Padding is 10px 16px, height is 44px. On focus, the border changes to `{colors.ink}` (#000000). No icon inside the field by default — the magnifying glass sits as a separate button to the right.

**`quantity-selector`** — A compact 36px-high input with a 1px `{colors.hairline}` border and 4px rounded corners. Used on product detail pages for adjusting item count. Contains the current quantity (center) with minus and plus buttons on either side.

### Footer
**`footer-section`** — A light gray background (`{colors.surface-soft}` — #f5f5f5) with muted text (`{colors.muted}` — #666666) in 12px Arial. Organized into columns with `{typography.title-sm}` (14px bold, `{colors.ink}`) headings. Links are `{typography.footer-link}` (12px regular) and turn `{colors.ink}` on hover. The copyright line sits at the bottom in `{typography.caption}` (12px regular, `{colors.muted-soft}` — #999999).

**`footer-heading`** — A column heading in the footer, set in `{typography.title-sm}` (14px bold, `{colors.ink}`) with 16px bottom margin. No uppercase, no decoration — just a clear label for the link group below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), top-nav collapses to hamburger menu, search bar moves below nav, footer columns stack vertically, padding reduces to 16px |
| Tablet | 744–1128px | Two-column product grid, top-nav remains horizontal but may wrap, search bar stays in header, footer columns in 2x2 grid |
| Desktop | 1128–1440px | Three-to-four-column product grid, full top-nav visible, search bar in header, footer columns in 4-column layout |
| Wide | > 1440px | Four-to-five-column product grid, max-width container (1200px) centers content, no layout changes beyond wider gutters |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Product cards have a minimum 200px width to ensure tap targets are large enough
- Search bar height is 44px on all breakpoints
- Quantity selector buttons are 36px × 36px minimum

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, revealing a full-screen overlay menu on tap
- Product grid collapses from 4 columns to 1 column below 744px
- Footer columns collapse from 4 to 2 at tablet, then to 1 at mobile
- Search bar moves from inline in the header to a full-width row below the nav on mobile
- Breadcrumbs are hidden on mobile, replaced by a "Back" link

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site — the palette above is inferred from the brand's known identity (black, white, gray) and common e-commerce patterns. The true primary color may differ.
- Font-family declarations returned only "Arial" — no custom or web fonts were detected. The site may use a self-hosted font or a system font stack that wasn't captured.
- Hover and focus states for all components are inferred from common patterns, not extracted from the live site.
- Error styling (form validation, out-of-stock messages, 404 pages) was not observed and is not represented.
- Dark mode, high-contrast mode, and reduced-motion preferences are not accounted for.
- The site may use a Shopify or other e-commerce platform — the extracted hint says `platform-shopify: False`, but the component structure (add-to-cart, quantity selector, product grid) is designed to be platform-agnostic.
- Sub-brand or seasonal color palettes (e.g., Record Store Day, holiday promotions) are not documented.
- The meta theme-color and page title were empty — the site may use JavaScript to set these dynamically.
