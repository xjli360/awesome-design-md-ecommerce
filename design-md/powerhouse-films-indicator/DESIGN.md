---
version: alpha
name: "Powerhouse Films (Indicator)"
source_url: "https://www.powerhousefilms.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A collector's-grade film label that wraps its deep-catalog releases in a near-monastic black-and-charcoal shell — `#121211` for the page background, `#231f20` for the primary brand mark, `#dedede` for body text that reads like fine print on a Criterion booklet. The site is a study in restraint: no hero carousel, no auto-playing trailers, no pillowy search bars. Instead, a fixed top nav in `#121212` carries the Indicator logo and a sparse row of links (Shop, Collections, Sale, Journal), each set in what appears to be a geometric sans-serif at modest weight — the brand trusts its cover art and spine photography to do the selling. Product cards are flat rectangles with `{rounded.none}` corners, a single product image, and a price block in `#444444`; there is no badge, no star rating, no "sale" flag unless the title is genuinely discounted. The checkout flow, powered by Shopify, introduces `#dedede` hairline borders and a `#ffffff` canvas that feels like stepping from a darkroom into daylight. The entire experience reads as a physical archive translated to screen — black backgrounds, white type, and the occasional accent of a film-still color that belongs to the artwork, not the UI.

colors:
  primary: "#231f20"
  primary-active: "#121211"
  primary-disabled: "#444444"
  ink: "#121212"
  body: "#dedede"
  muted: "#444444"
  muted-soft: "#666666"
  hairline: "#444444"
  hairline-soft: "#333333"
  canvas: "#121211"
  surface-soft: "#1a1a1a"
  surface-card: "#121212"
  on-primary: "#dedede"
  on-dark: "#dedede"
  sale-accent: "#c0392b"
  preorder-accent: "#8e44ad"
  out-of-stock: "#7f8c8d"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.primary}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-disabled}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.body}"
  button-secondary-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.body}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "1px solid {colors.body}"
    outline: "none"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  nav-link-active:
    textColor: "{colors.canvas}"
    borderBottom: "2px solid {colors.canvas}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.muted}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.sale-accent}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.sale-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-preorder-badge:
    backgroundColor: "{colors.preorder-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-out-of-stock-badge:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  search-bar-focus:
    border: "1px solid {colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.body}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.body}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.xl} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  collection-title:
    typography: "{typography.display-md}"
    textColor: "{colors.body}"
  collection-description:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  filter-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} 0"
  pagination-active:
    textColor: "{colors.body}"
    fontWeight: 700
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.md} {spacing.lg}"
  breadcrumb-link:
    textColor: "{colors.muted}"
    hoverTextColor: "{colors.body}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: "none"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-item-title:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
  cart-item-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  cart-total:
    typography: "{typography.title-lg}"
    textColor: "{colors.body}"
    padding: "{spacing.md} 0"
    borderTop: "1px solid {colors.hairline}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 24px"
    height: 48px
    width: "100%"
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
  checkout-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a solid `#231f20` rectangle with zero corner radius. Text is set in uppercase `{typography.button-md}` at `#dedede`, with `12px 24px` padding and a matching `1px` border. On hover or active state (`{colors.primary-active}`), the background shifts to `#121211` with no border change, creating a subtle darkening effect. Disabled state uses `#444444` background and `#666666` text, signaling an unavailable action without harsh contrast.

**`button-secondary`** — An outlined variant used for less prominent actions (e.g., "Clear Filters", "Cancel"). The button is transparent with a `1px solid #dedede` border and `#dedede` text. On hover, the background fills with `#dedede` and text inverts to `#121211`, a classic darkroom-reversal gesture that fits the brand's photographic sensibility.

**`checkout-button`** — Full-width primary button reserved for the cart and checkout flow. Identical visual treatment to `button-primary` but spans the container width and uses `14px 24px` padding for a taller hit area. Active and disabled states mirror the primary button pattern.

### Cards
**`product-card`** — A flat, border-defined rectangle on `#121212` surface with `1px solid #444444` stroke and zero rounding. Each card contains a single product image (typically the Blu-ray cover art) that bleeds edge-to-edge, followed by the title in `{typography.title-md}` and price in `{typography.body-sm}` at `#444444`. On hover, the border lightens to `#666666`, a barely perceptible lift that rewards exploration without visual noise. Sale items show `{colors.sale-accent}` price text and an optional `{product-card-badge}` in the top-left corner.

**`product-card-badge`** — A small, unrounded label pinned to the top-left of the product image. Uses `#c0392b` background for sale items, `#8e44ad` for pre-orders, and `#7f8c8d` for out-of-stock. Text is `{typography.badge}` in `#ffffff` with `2px 6px` padding — minimal, informational, never decorative.

### Navigation
**`nav-bar`** — A fixed `60px` bar at `#121212` containing the Indicator logo (left) and navigation links (right). Links use `{typography.nav-link}` — `13px`, `500` weight, `1px` letter-spacing, uppercase — in `#dedede`. The active page link shifts to `#ffffff` with a `2px` bottom border, the only underline in the entire navigation system. No dropdowns, no mega-menus, no search icon until the user scrolls to the product grid.

**`footer`** — A `#121212` band with `#444444` hairline top border, containing legal text, social links, and newsletter signup in `{typography.body-sm}` at `#666666`. Links are underlined on hover only, preserving the clean baseline. Padding is generous (`{spacing.xxl}` vertical) to match the breathing room of the product pages above.

### Forms
**`text-input`** — A rectangular input field on `#121212` surface with `1px solid #444444` border, `#dedede` text, and `#666666` placeholder. Focus state swaps the border to `#dedede` with no outline — the only visual cue is the border brightening. Height is `44px` for comfortable touch targeting, with `10px 12px` internal padding.

**`filter-dropdown`** — Used in collection and search result pages to sort by title, release date, or price. Identical visual treatment to `text-input` but with a `40px` height and `{typography.body-sm}` text. The dropdown arrow is rendered as a `#666666` SVG chevron, not a browser-native arrow.

**`quantity-selector`** — A compact `44px` input with increment/decrement buttons on either side, used on the product detail page and cart. The input field matches `text-input` styling; the buttons are transparent with `{typography.button-sm}` text and no border, relying on the container's `1px solid #444444` boundary.

### Search
**`search-bar`** — A standalone input on product listing pages, styled identically to `text-input` but with a magnifying-glass icon (SVG, `#666666`) placed inside the left padding. On focus, the border brightens to `#dedede` and the icon shifts to `#ffffff`. No autocomplete dropdown — search results load as a filtered product grid below.

### Footer
**`footer-link`** — Standard inline link within the footer block, set in `{typography.link}` at `#666666`. Hover state shifts to `#dedede` and adds underline. Used for "About Us", "Shipping Info", "Contact", and social media handles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), nav collapses to hamburger menu, filter bar stacks vertically, hero section reduces padding to `{spacing.lg}`, product card badges reposition to top-center |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but reduce font size to `12px`, filter bar uses horizontal scroll for dropdowns, hero padding at `{spacing.xl}` |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links, filter bar inline, hero section at full `{spacing.section}` padding, product cards show hover border effect |
| Wide | > 1440px | Four-column product grid, max-width container at `1440px` centered, nav bar expands to full width with increased letter-spacing on links, hero content max-width at `1128px` |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain a minimum `44px` height for touch accessibility.
- Product card tap targets are the entire card surface, not just the title or price text.
- Filter dropdowns and quantity selectors use `40px` minimum height with `12px` internal padding.
- Nav links on mobile (hamburger menu) expand to full-width `48px` tap targets.

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger icon (left) with the logo centered; the menu panel slides in from the left on `#121212` background.
- The filter bar collapses to a single "Filter" button that opens a modal overlay with all filter options stacked vertically.
- Product card badges are hidden on mobile to reduce visual clutter; sale indicators are shown only in the price text.
- The footer newsletter signup collapses to a single input with a submit button below it (inline on desktop).
- Breadcrumbs are hidden on mobile; the page title serves as the sole navigation cue.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found during extraction. The typography block uses a `'Helvetica Neue', Helvetica, Arial, sans-serif` fallback stack — the actual brand font (likely a geometric sans-serif like Akzidenz-Grotesk or Univers) could not be confirmed.
- Hover, active, and focus states for most components are inferred from the brand's dark-background aesthetic and may differ from the live implementation.
- Error styling for form validation (red borders, error messages) was not observed and is not defined.
- The checkout flow is powered by Shopify's default theme; custom styling for checkout-specific elements (payment icons, shipping options) could not be extracted.
- Dark mode is not applicable — the site already uses a dark canvas as its default state.
- Sub-brand palettes for limited editions or special collections (e.g., "Indicator #2", "Box Set X") may introduce accent colors not captured in the top hex extraction.
- The extracted hex list (`#231f20`, `#444444`, `#121211`, `#dedede`, `#121212`) appears to be the brand's true palette — no generic blues or bright accents were found, suggesting a deliberate monochrome approach. The `#231f20` value (a very dark brown-black) is the most distinctive and is used as the primary brand color.
