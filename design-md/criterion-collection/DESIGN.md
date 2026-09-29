---
version: alpha
name: "The Criterion Collection"
source_url: "https://www.criterion.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, scholarly reverence for cinema rendered in near-monochrome austerity — #313131 is the single extracted color, a charcoal that reads as archival ink on the white canvas of the site. The Criterion Collection does not sell movies; it sells the definitive edition, and the design language mirrors that: a stark, almost library-like grid of film posters against white, with typography that defaults to system-ui stacks, trusting the raw power of the cover art and the weight of the filmography over decorative type. There are no rounded corners on the primary grid — film posters sit flush in a hard {rounded.none} grid, a deliberate choice that evokes a gallery wall or a shelf of laserdiscs. The search bar, however, uses a soft {rounded.sm} to create a single point of entry, a subtle invitation into the collection. Navigation is a thin, persistent black bar — the only persistent dark element — that anchors the experience, while the product pages lean into generous whitespace, with a single column of information and a large, centered poster. The brand's voice is authoritative but not cold; it uses the language of curation ("Director-Approved," "Special Edition Features") as its primary UI copy, and the design defers entirely to the film stills and poster art as the emotional payload. The extracted palette is sparse — a single charcoal — which is honest to the site's minimalism; the brand trusts black, white, and the color of the films themselves.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#000000"
  body: "#313131"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#000000"
  link-hover: "#313131"
  badge-new: "#cc0000"
  badge-available: "#2e7d32"
  badge-preorder: "#1565c0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
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
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
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
    border: "1px solid {colors.primary}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 48px
    padding: "0 {spacing.lg}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 48px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-dark}"
  top-nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    height: 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-year:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  collection-hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  collection-hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.sm}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
    height: 36px
  filter-dropdown-active:
    border: "1px solid {colors.primary}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} 0"
  pagination-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination-hover:
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  footer-link-hover:
    textColor: "{colors.ink}"
  product-detail-hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.lg}"
  product-detail-poster:
    rounded: "{rounded.none}"
    width: 300px
  product-detail-title:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
  product-detail-director:
    typography: "{typography.title-md}"
    textColor: "{colors.muted}"
  product-detail-year:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    lineHeight: 1.6
  product-detail-specs:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.lg} 0"
    borderTop: "1px solid {colors.hairline-soft}"
  spec-item:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  spec-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    fontWeight: 600
  badge-director-approved:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  badge-4k:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  badge-blueray:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  badge-dvd:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px {spacing.xl}"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 48px
    padding: "0 {spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Pre-order," and "Shop Now." A solid charcoal fill with white uppercase text, using a subtle 4px corner radius. On hover, the fill deepens to near-black. The disabled state uses a muted gray fill, signaling unavailability without visual noise.

**`button-secondary`** — An outlined alternative for less prominent actions like "View Details" or "Learn More." White background with a thin hairline border. On hover, the background shifts to a soft surface tone and the border adopts the primary charcoal, maintaining the brand's restrained palette.

**`button-text`** — A ghost button for tertiary actions such as "Clear Filters" or "Cancel." No background or border, relying solely on the uppercase button typography. On hover, the text color shifts to the primary charcoal, providing a subtle state change.

### Navigation
**`top-nav`** — The persistent 48px black bar at the top of every page. Contains the Criterion logo, primary navigation links (The Collection, Shop, My Criterion, etc.), and a search icon. All text is white, uppercase, and tightly tracked. The active link is underlined with a 2px white border. Hover links fade to a soft gray.

**`top-nav-link`** — Individual navigation items within the top bar. Uppercase, 13px, weight 600, with 0.5px letter spacing. Active state shows a bottom border. Hover state shifts text color to `{colors.muted-soft}`.

### Search
**`search-bar`** — A compact, 40px search input with a soft gray background and thin hairline border. On focus, the background turns white and the border adopts the primary charcoal. The search icon sits to the left in muted gray. This is the only element with a rounded corner on the main grid, creating a subtle point of entry.

### Cards
**`product-card`** — The core collection grid item. A hard-cornered container holding a 2:3 aspect ratio film poster, the title in 16px semibold, the year in 13px muted, and the price in 14px primary charcoal. No shadows or borders — the poster art is the sole visual anchor. A small badge may appear in the top-left corner for "New," "4K," or "Director-Approved" editions.

**`product-card-badge`** — A small, uppercase label pinned to the top-left of the product card image. Uses a distinct color per category: red for new releases, blue for pre-orders, green for in-stock. The badge is tightly padded and uses a 2px corner radius.

### Collection Page
**`collection-hero`** — The header section for a collection or category page (e.g., "Janus Films," "Eclipse Series"). Large display typography with a subtitle in body-size muted text. Generous vertical padding creates a breathing room between the top nav and the filter bar.

**`filter-bar`** — A horizontal strip below the hero containing dropdown filters (Format, Director, Year, etc.) and a result count. Each dropdown is a 36px input with a hairline border and soft corner. The active filter dropdown adopts the primary charcoal border.

**`pagination`** — A simple, text-based pagination strip at the bottom of collection pages. Page numbers are muted gray, with the active page in black and weight 600. Hover states shift to the primary charcoal.

### Product Detail
**`product-detail-hero`** — The top section of a product page, featuring a large poster image on the left and product information on the right. The poster is 300px wide with no rounding. The title uses display-lg, the director name is in title-md muted, and the description runs in body-md with generous line-height.

**`product-detail-specs`** — A bordered section below the description listing technical details (Runtime, Aspect Ratio, Language, Subtitles, etc.). Each spec is a two-column row with a muted label and a body-colored value.

**`add-to-cart-button`** — The primary purchase action on the product page. A 48px tall charcoal button with uppercase text. On hover, the fill deepens. Sits next to a `quantity-selector` input for adjusting the purchase count.

**`quantity-selector`** — A bordered input for selecting the number of copies. Matches the height of the add-to-cart button for visual alignment. Uses body typography and a hairline border.

### Badges
**`badge-director-approved`** — A small, black badge indicating the film has been approved by its director. Uses uppercase 11px text on a black background. Applied to product cards and the product detail page.

**`badge-4k`** — A blue badge for 4K UHD editions. Uses the same typography as the director-approved badge but with a blue background.

**`badge-blueray`** — A charcoal badge for Blu-ray editions. Matches the primary color of the brand.

**`badge-dvd`** — A muted gray badge for DVD editions. Uses the same typography as the other format badges.

### Footer
**`footer`** — A soft gray section at the bottom of every page. Contains links to About, Support, Privacy Policy, and social media. All text is caption-sized and muted. Links hover to black. A thin hairline border separates it from the main content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu. Product grid switches to 2 columns. Filter bar becomes a single "Filter" button that opens a modal. Product detail hero stacks vertically (poster above text). Footer links stack in a single column. |
| Tablet | 744–1128px | Top nav remains full but may hide secondary links behind a "More" dropdown. Product grid uses 3 columns. Filter bar shows 2-3 visible dropdowns with a "+" for overflow. Product detail hero remains side-by-side but with reduced poster width (200px). |
| Desktop | 1128–1440px | Full top nav visible. Product grid uses 4 columns. Filter bar shows all dropdowns. Product detail hero uses 300px poster. Standard layout as described. |
| Wide | > 1440px | Max-width container (1440px) centered on screen. Product grid may expand to 5 columns. Additional whitespace on the sides of the product detail page. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile.
- Top nav hamburger icon is 48x48px.
- Filter dropdowns are 36px tall (below the 44px recommendation but consistent with desktop; on mobile, the filter modal uses full-width 48px buttons).
- Add-to-cart button is 48px tall.
- Quantity selector is 48px tall.

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (< 744px). The menu slides in from the left as an overlay.
- Filter bar collapses to a single "Filter" button on mobile. Tapping opens a full-screen modal with all filter options stacked vertically.
- Product grid reduces columns: 2 on mobile, 3 on tablet, 4 on desktop, 5 on wide.
- Footer links collapse to a single column on mobile, with expandable sections for "Shop," "Support," and "About."
- Product detail hero stacks vertically on mobile: poster first, then title/director, then description, then specs, then add-to-cart.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site. The full palette (active states, disabled states, badge colors, link colors, surface tones) has been inferred from common Criterion design patterns and general e-commerce best practices. These inferred colors should be verified against the actual site's CSS.
- No font-family declarations beyond the system-ui stack were found. The Criterion Collection may use a custom typeface (e.g., a licensed font for the logo or headings) that was not captured in the extraction. The typography block uses the extracted system stack as a fallback.
- Hover and focus states for all components are inferred. The actual site may use different transitions, shadows, or color shifts.
- Error states for forms (e.g., invalid email, out-of-stock messages) were not extracted. A generic red (#cc0000) has been assumed for error text.
- Dark mode is not supported by the extracted data. The site appears to be light-mode only.
- The meta theme-color was not present, suggesting no browser chrome theming.
- The extracted data may have been blocked by a Cloudflare challenge ("Just a moment..." page title), meaning the actual site CSS was not fully parsed. All design decisions should be treated as informed estimates until verified against the live, rendered site.
- Sub-brand palettes (e.g., Janus Films, Eclipse Series) may exist but were not captured.
- Animation and transition durations are not specified. The site likely uses subtle fades and slides, but exact values are unknown.
- The checkout flow (Shopify or custom) was not analyzed. Cart, checkout, and payment form styles are not included.
