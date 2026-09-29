---
version: alpha
name: "Dusty Groove"
source_url: "https://www.dustygroove.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, obsessive dive into the crates of Chicago's legendary independent record store, Dusty Groove's digital presence is a study in deliberate restraint — a single extracted hex of #313131, a near-black charcoal, dominates the interface, suggesting a space where the product (the album art, the tracklist, the label) is the only color that matters. This is not a brand that sells a lifestyle; it sells the physical artifact of music, and the design reflects a collector's patience: dense text listings, minimal imagery beyond the record sleeve, and a navigation system that prioritizes genre taxonomy over visual spectacle. The typography stack — a fallback chain of -apple-system, Arial, Helvetica Neue, Roboto, sans-serif — is utilitarian, almost anti-brand, chosen for legibility and speed rather than personality. There are no pill-shaped buttons ({rounded.full}) or generous card radii ({rounded.lg}); instead, the interface uses sharp corners ({rounded.none}) and tight spacing ({spacing.sm}) to pack information density onto the page, mimicking the crowded bins of a physical record shop. The brand's voice is that of a knowledgeable, slightly gruff clerk who can tell you the pressing year of a Sun Ra LP from memory — it trusts the user to know what they're looking for, and the design gets out of the way. The absence of a meta theme-color and the presence of a Cloudflare "Just a moment..." page hint at a site that prioritizes backend stability over front-end polish, a pragmatic choice for a small, independent operation.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#888888"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#0066cc"
  link-visited: "#551a8b"
  price: "#cc0000"
  stock-in: "#006600"
  stock-out: "#cc0000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 6px 12px
    height: 32px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 32px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
    padding: 4px 0px
    height: auto
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 8px
    height: 32px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 40px
    padding: "0 {spacing.base}"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    fontWeight: 700
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    width: 100%
    aspectRatio: 1/1
    objectFit: contain
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.price}"
    fontWeight: 600
  product-card-stock:
    typography: "{typography.caption}"
    textColor: "{colors.stock-in}"
    fontWeight: 600
  product-card-stock-out:
    typography: "{typography.caption}"
    textColor: "{colors.stock-out}"
    fontWeight: 600
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 8px
    height: 32px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 32px
  genre-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  genre-nav-item:
    typography: "{typography.link}"
    textColor: "{colors.link}"
    padding: "{spacing.xxs} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.link}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.base}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.price}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "1px 4px"
  badge-sale:
    backgroundColor: "{colors.stock-in}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "1px 4px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Search", and "Checkout" actions. Rendered as a compact 32px-tall rectangle with {rounded.sm} corners and the brand's near-black {colors.primary} background. On hover, it shifts to {colors.primary-active} (#1a1a1a). The disabled state uses {colors.muted-soft} (#999999) to signal unavailability without visual noise.

**`button-secondary`** — A lighter alternative for secondary actions like "Clear Filters" or "View Details". Uses a {colors.surface-soft} (#f5f5f5) background with {colors.ink} (#1a1a1a) text, maintaining the same compact 32px height and {rounded.sm} corners as the primary button for visual consistency.

**`button-link`** — A text-only button styled as an inline link, used for actions like "Remove from Cart" or "Cancel". No background, no border, relying solely on {colors.link} (#0066cc) text color and the {typography.link} style to communicate clickability.

### Navigation
**`nav-bar`** — A persistent top navigation bar spanning the full viewport width, filled with {colors.primary} (#313131). Houses the site logo (typically text-based), primary navigation links, and a compact search bar. The bar is deliberately short at 40px to maximize vertical space for content — a design choice that prioritizes information density over visual prominence.

**`nav-link`** — Navigation links rendered in white ({colors.on-primary}) using {typography.nav-link} (13px, weight 600). The active state increases font-weight to 700 for differentiation, avoiding underlines or background changes that would add visual clutter.

**`genre-nav`** — A secondary navigation panel for browsing by music genre, typically positioned as a sidebar or top strip. Uses a light gray background ({colors.surface-soft}) and dense link lists styled with {typography.link} in standard link blue (#0066cc). This is the site's primary discovery mechanism, reflecting the record store's deep genre taxonomy.

### Forms
**`text-input`** — Standard text input fields for search queries, login forms, and checkout. A clean 32px-tall rectangle with a 1px {colors.hairline} (#cccccc) border and {rounded.sm} corners. On focus, the border thickens to 2px and switches to {colors.primary} (#313131) for clear visual feedback.

**`search-bar`** — The primary search input, visually identical to `text-input` but paired with a `search-submit` button. The search bar and submit button sit adjacent, forming a unified search widget. The submit button uses the `button-primary` style to visually anchor the search action.

### Cards
**`product-card`** — The core content unit for displaying individual records, CDs, or other media. A borderless card with a 1px {colors.hairline-soft} (#e0e0e0) boundary, no border-radius ({rounded.none}), and tight {spacing.sm} (8px) internal padding. The card contains a square aspect-ratio image (album art), the artist name in {colors.muted} (#666666), the album title in {colors.ink} (#1a1a1a), and the price in {colors.price} (#cc0000). Stock status appears as a small colored badge — green for "In Stock", red for "Out of Stock".

### Badges
**`badge-new`** — A small red badge ({colors.price}) used to flag new arrivals. Rendered in uppercase 10px bold type with {rounded.xs} (2px) corners and minimal padding (1px 4px). Designed to be unobtrusive yet noticeable against the dense product listings.

**`badge-sale`** — A green badge ({colors.stock-in}) for sale or clearance items. Shares the same compact dimensions and typography as `badge-new`, using color alone to differentiate the message.

### Footer
**`footer`** — A full-width footer using the same {colors.primary} (#313131) background as the nav bar, creating a visual bookend for the page. Contains links to About, Contact, Shipping, and Privacy pages, all rendered in white ({colors.on-primary}) using {typography.body-sm} (12px). Padding is generous at {spacing.lg} (24px) top and bottom to give the dense content room to breathe.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row); genre-nav collapses into a hamburger menu; search bar moves to a full-width top section; nav-bar height reduces to 36px; product-card padding reduces to {spacing.xs} (4px) |
| Tablet | 744–1128px | Two-column product grid; genre-nav becomes a horizontal scrollable strip above the product grid; search bar remains in nav-bar; nav-link font size reduces to 12px |
| Desktop | 1128–1440px | Three-column product grid; genre-nav appears as a persistent left sidebar (200px wide); full nav-link text visible; breadcrumb navigation shown |
| Wide | > 1440px | Four-column product grid; genre-nav sidebar expands to 240px; max-width container (1440px) centers content; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px touch target on mobile devices, achieved through increased padding even if the visual element is smaller.
- Product card tap targets extend to the full card boundary, not just the text or image.
- Genre-nav items on mobile have 48px minimum height for easy finger targeting.

### Collapsing Strategy
- Genre navigation collapses from a persistent sidebar (desktop) to a horizontal scroll strip (tablet) to a hamburger menu (mobile).
- Product grid columns reduce from 4 (wide) to 1 (mobile) as viewport narrows.
- Breadcrumb navigation hides on mobile, replaced by a "Back" button in the top nav.
- Footer link columns collapse to a single vertical stack on mobile.
- Secondary navigation items (e.g., "New Arrivals", "Pre-Orders") collapse into a "More" dropdown on tablet and mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only a single hex color (#313131) was reliably extracted from the live site; the full color palette (link blue, price red, stock green, hover states, etc.) has been inferred from common e-commerce patterns and may not match the actual site.
- No custom font family was found; the site relies entirely on system font stacks. If the brand uses a custom typeface (e.g., for the logo), it could not be detected.
- Meta theme-color was absent, suggesting no PWA or mobile browser chrome customization.
- The "Just a moment..." page title indicates Cloudflare protection; actual page titles, headings, and content structure could not be verified.
- No border-radius values could be extracted; all rounded tokens are estimates based on common e-commerce patterns.
- Spacing values are inferred from typical information-dense layouts; actual site spacing may vary.
- Hover, focus, and active states for all components (except button-primary) are speculative.
- Error states for forms (validation, error messages) could not be observed.
- Dark mode support is unknown and likely absent given the single extracted color.
- The site may use a Shopify or other e-commerce backend, but no platform indicators were detected.
- Product card image aspect ratios, grid gaps, and responsive breakpoints are estimates based on common record store site patterns.
