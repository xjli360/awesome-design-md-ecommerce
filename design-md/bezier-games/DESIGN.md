---
version: alpha
name: "Bezier Games"
source_url: "https://beziergames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A board game publisher whose visual system is built on a near-monochrome palette of #dedede and #121212 — a deliberate, almost architectural reduction that lets the saturated game art on every product card do all the emotional work. The brand's Shopify storefront reads as a gallery: white canvas (#ffffff) with a single hairline-thin gray separator, product imagery floating in generous whitespace, and a single typeface — Ssw Fontello — handling both display and body copy. There are no decorative flourishes, no gradient hero sections, no brand illustrations; the design trusts that a well-photographed game box with its own internal color story is more compelling than any brand-applied pattern. Buttons and inputs use a soft 8px radius ({rounded.sm}) that feels approachable without being playful, and the navigation bar stays fixed at the top with a clean white background and dark ink text — no background color shifts, no mega-menus. The checkout flow inherits Shopify's default styling, which means the brand's true design voice is strongest on the product and collection pages: a centered grid of cards, each with a uniform aspect ratio, a title set in Ssw Fontello at 16px, and a price in the same weight. The #dedede color appears as a subtle background on secondary surfaces and as a border on product cards, while #121212 anchors all body text and primary headings. The result is a system that feels less like a brand identity and more like a neutral frame — the game is the hero, and Bezier Games simply provides the cleanest possible vitrine.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#8a8a8a"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-game: "#dedede"
  price: "#121212"
  sale: "#cc0000"
  badge-new: "#121212"

typography:
  display-xl:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  product-title:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  product-price:
    fontFamily: "'Ssw Fontello', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
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
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.product-title}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: 0px
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.product-title}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.product-price}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.ink}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} 0"
    borderBottom: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.base} 0"
  breadcrumb-link:
    textColor: "{colors.muted}"
  breadcrumb-link-hover:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "{spacing.base} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the storefront, used for "Add to Cart", "Checkout", and primary form submissions. Rendered as a solid dark square with uppercase white text at 14px/600 weight. On hover, the background deepens to true black (`{colors.primary-active}`). The disabled state uses a medium gray (`{colors.primary-disabled}`) to signal inactivity without ambiguity. Padding is generous at 12px vertical / 24px horizontal to create a substantial tap target.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Cancel". Uses a white background with a `{colors.hairline}` border that darkens to `{colors.ink}` on hover. Typography matches the primary button's uppercase weight and size, ensuring visual parity in the button group. The 1px border is thin enough to feel refined but thick enough to be visible on any background.

**`button-ghost`** — A text-only button for tertiary actions such as "Clear Filters" or "Learn More". No background or border, relying solely on `{colors.ink}` text at `{typography.button-md}`. Hover state adds a subtle background tint from `{colors.surface-soft}` to provide feedback without introducing a full button shape.

### Cards
**`product-card`** — The core content unit on collection and search pages. A white card with a soft `{rounded.sm}` corner and a near-invisible `{colors.hairline-soft}` border that becomes `{colors.hairline}` on hover. The card contains a square aspect-ratio image at the top (with rounded top corners only), followed by the product title and price in `{typography.product-title}` and `{typography.product-price}` respectively. No box shadow in the default state — the design relies on the border alone for separation. On hover, a subtle `0 2px 8px rgba(0,0,0,0.08)` shadow lifts the card slightly.

**`badge-new`** and **`badge-sale`** — Small, uppercase labels pinned to the top-left corner of product images. The "New" badge uses `{colors.badge-new}` (black) for a clean, authoritative look, while the "Sale" badge uses `{colors.sale}` (red) for urgency. Both are set in `{typography.badge}` with tight padding and `{rounded.xs}` corners.

### Navigation
**`nav-bar`** — A fixed-position top bar at 64px height with a white background and a single `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` — uppercase, 14px, 600 weight — with a 2px underline on the active state. The bar contains the brand logo on the left, primary links in the center, and utility icons (search, cart, account) on the right. No background color changes or dropdown indicators — the navigation is intentionally flat and minimal.

**`nav-link-active`** and **`nav-link-inactive`** — Active links are distinguished by a 2px bottom border in `{colors.ink}` and full opacity text. Inactive links use `{colors.muted}` and no underline. The hover state for inactive links transitions to `{colors.ink}` without the underline, keeping the active state visually unique.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. A white background with a `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border switches to `{colors.ink}` for a clear active state. Error states use `{colors.sale}` for the border color. Padding is 12px vertical / 16px horizontal to match the button heights and create a consistent vertical rhythm.

**`search-bar`** — A dedicated search input that lives in the navigation bar or on collection pages. Slightly shorter than the standard text input at 44px height, with the same `{rounded.sm}` corners and `{colors.hairline}` border. The search icon sits inside the input on the left, and a clear button appears on the right when text is entered.

### Footer
**`footer`** — A full-width section at the bottom of every page with a light gray background (`{colors.surface-soft}`) and a `{colors.hairline}` top border. Links are set in `{typography.link}` at `{colors.muted}` and transition to `{colors.ink}` on hover. The footer contains three columns: company information, customer support, and legal links. Padding is generous at 48px vertical and 64px horizontal to give the footer breathing room.

### Collection Header
**`collection-header`** — The top section of collection pages, containing the collection title in `{typography.display-lg}` and a `{colors.hairline}` bottom border. Below the title, a `{breadcrumb}` component shows the navigation path (e.g., Home > Board Games > Worker Placement). The breadcrumb uses `{typography.caption}` at `{colors.muted}` with hover transitions to `{colors.ink}`.

### Quantity Selector
**`quantity-selector`** — A compact input group for adjusting product quantities on the product page or cart. Uses the same `{rounded.sm}` and `{colors.hairline}` border as other form elements, with minus and plus buttons flanking a centered numeric display. The component is 44px tall to match the button height, ensuring a consistent baseline across the add-to-cart row.

### Divider
**`divider`** and **`divider-soft`** — Horizontal rules used throughout the site to separate sections. The standard divider is a 1px `{colors.hairline}` line, while the soft variant uses `{colors.hairline-soft}` for subtler separation within cards or between related content blocks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav bar collapses to hamburger menu, footer stacks vertically, collection header reduces to `{typography.display-md}`, search bar moves to a full-width overlay |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but reduce font size to 12px, footer columns collapse to 2-column layout, collection header uses `{typography.display-lg}` |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links visible, footer in 3-column layout, standard spacing and typography apply |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered on screen, additional whitespace on sides, no typography changes |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height to meet WCAG touch target recommendations
- Product cards are fully tappable, with the entire card linking to the product page
- Navigation links have a minimum 48px tap area (including padding) on mobile
- Quantity selector buttons are 44px x 44px to prevent mis-taps
- Search bar and text inputs are 48px tall on mobile for easier interaction

### Collapsing Strategy
- On mobile (< 744px), the navigation bar collapses to a hamburger menu with a slide-out drawer containing all links
- The product grid collapses from 3–4 columns to 1 column, with full-width cards
- The footer collapses from 3 columns to a single stacked column
- Breadcrumbs are hidden on mobile, replaced by a simple "Back" button
- The collection header reduces font size and removes the border on mobile
- Search transitions from an inline input to a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is extremely limited (#dedede and #121212 only), which may not represent the full brand system — secondary accents, hover states, and error colors were inferred from common e-commerce patterns rather than extracted from the live site
- Font family "Ssw Fontello" was the only declaration found; fallback stacks and specific weights (400, 600, 700) were assumed based on typical usage — actual font weights on the site may vary
- No button hover, focus, or active states could be extracted; these were designed to be consistent with the brand's minimal aesthetic
- Checkout flow colors and components were not extracted — Shopify's default checkout styling may override the brand system during payment
- No data on form validation styling (success, error messages, helper text) — error states use a generic red (#cc0000) as a placeholder
- No information on loading states, skeleton screens, or spinner designs
- No extracted data for modal, drawer, or overlay components
- The brand may use additional typography scales for editorial content, blog posts, or game rulebooks that were not present on the extracted pages
- No information on dark mode or high-contrast mode support
- The extracted colors may include Shopify default elements (e.g., checkout buttons, social icons) that are not part of the brand's intentional design system
- No data on animation durations, easing curves, or transition behaviors
- The brand's logo and icon system were not analyzed — all references to logo placement are based on common e-commerce patterns
