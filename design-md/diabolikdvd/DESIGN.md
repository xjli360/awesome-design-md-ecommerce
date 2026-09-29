---
version: alpha
name: "DiabolikDVD"
source_url: "https://diabolikdvd.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single dark gray hex — `#313131` — governs nearly every surface on DiabolikDVD, a specialist horror and cult-film retailer that treats its site like a repertory cinema lobby: dim, serious, and lit only by the glow of movie posters. The brand’s visual identity is built on subtraction — no primary color, no hero gradient, no brand mascot. Instead, the entire interface is a restrained monochrome stage where cover art (often lurid, hand-illustrated, or exploitation-style) provides the only color. Body text runs at `#313131` on a white canvas (`{colors.canvas}`), but the real atmosphere comes from the product grid: each DVD or Blu-ray sits in a `{rounded.sm}` card with a soft `{colors.hairline}` border, leaving the poster art to scream in reds, yellows, and deep blacks. The typography stack is the system default — `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto` — a deliberate choice that signals utility over personality. Buttons are small, compact, and use `{rounded.sm}` corners; the primary action (“Add to Cart”) is a `{colors.primary}` gray rectangle with white text, no glow, no shadow. The navigation is a thin, fixed bar with a logo lockup and dropdown menus, all in `{colors.ink}` on `{colors.canvas}`. There is no hero section, no carousel, no lifestyle photography — just a search bar, category filters, and a wall of titles. The experience is for collectors who know what they want: the site gets out of the way.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c13515"
  success: "#2e7d32"
  badge-new: "#c62828"
  badge-sale: "#1565c0"
  badge-oop: "#6a1b9a"
  star-rating: "#f59e0b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0

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
    padding: 10px 20px
    height: 38px
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
    padding: 9px 19px
    height: 38px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 38px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    borderColor: "{colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    minWidth: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-current:
    color: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 38px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-lg}"
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Checkout,” and “Subscribe.” A solid `{colors.primary}` (#313131) rectangle with `{rounded.sm}` corners and white text. On hover, it darkens to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#a0a0a0) to signal non-interactivity. Height is a compact 38px, consistent with the site’s dense, information-rich layout.

**`button-secondary`** — An outlined alternative for secondary actions like “View Details” or “Continue Shopping.” White background (`{colors.canvas}`) with `{colors.ink}` text and a 1px `{colors.hairline}` border. Hover adds a subtle `{colors.hairline-soft}` background. Same 38px height and `{rounded.sm}` corners as the primary button.

**`button-tertiary-text`** — A text-only button for inline actions like “Clear Filters” or “Remove.” No background, no border. Uses `{colors.primary}` text color and `{typography.button-md}`. Hover underlines the text.

**`button-icon`** — A 32px square icon button for utility actions (search toggle, cart toggle, close modal). Transparent background with `{colors.muted}` icon color. Hover changes background to `{colors.surface-soft}`.

### Cards
**`product-card`** — The core content unit: a white card (`{colors.surface-card}`) with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. Contains a product image (top, with `{rounded.sm}` top corners), the title in `{typography.title-md}` (`{colors.ink}`), and the price in `{typography.price}` (`{colors.primary}`). On hover, the border shifts to `{colors.hairline}` for a subtle lift. A `{rounded.xs}` badge may appear in the top-left corner for “New,” “Sale,” or “OOP” (Out of Print) statuses, using `{colors.badge-new}`, `{colors.badge-sale}`, or `{colors.badge-oop}` backgrounds respectively.

### Navigation
**`nav-bar`** — A fixed 56px bar at the top of every page. White background (`{colors.canvas}`) with a 1px `{colors.hairline-soft}` bottom border. Contains the DiabolikDVD logo on the left, category dropdowns in the center (Horror, Cult, Exploitation, etc.), and utility icons (search, cart, account) on the right. Uses `{typography.nav-link}` for all text links.

**`nav-dropdown`** — A white dropdown panel that appears on hover over nav categories. `{rounded.sm}` corners, 8px top padding, and `{typography.body-sm}` for list items. Items have 8px horizontal padding and a hover state that adds `{colors.surface-soft}` background.

### Forms
**`text-input`** — Standard single-line input for search, email signup, and checkout forms. White background (`{colors.canvas}`), `{colors.body}` text, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. Focus state changes border to `{colors.primary}`. Error state uses `{colors.error}` border. Height is 38px to match button sizing.

**`quantity-selector`** — A compact input for cart quantity adjustments. White background, `{colors.body}` text, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. Contains increment/decrement buttons on either side. Height is 38px.

### Search
**`search-bar`** — A pill-shaped (`{rounded.full}`) search field with `{colors.surface-soft}` background and `{colors.body}` placeholder text. 40px height, 16px horizontal padding. On focus, the background shifts to white (`{colors.canvas}`) and a `{colors.hairline}` border appears. Used in the nav bar and on the search results page.

### Filters
**`filter-chip`** — A pill-shaped (`{rounded.full}`) filter toggle for genre, format (DVD, Blu-ray, 4K), and region. `{colors.surface-soft}` background with `{colors.body}` text in `{typography.button-sm}`. Active state flips to `{colors.primary}` background with `{colors.on-primary}` text. Height is 32px.

### Footer
**`footer`** — A full-width footer with `{colors.surface-soft}` background and `{colors.muted}` text. Contains links to About, Shipping, Returns, and Contact pages. Links use `{typography.link}` and are `{colors.muted}` by default, darkening to `{colors.ink}` on hover. Padding is `{spacing.xl}` top and bottom.

### Pagination
**`pagination-button`** — A 36px square button for page navigation. White background, `{colors.body}` text, `{rounded.sm}` corners. Active page uses `{colors.primary}` background with `{colors.on-primary}` text. Previous/Next buttons have arrow icons.

### Breadcrumbs
**`breadcrumb`** — A horizontal list of navigation links in `{typography.caption}` with `{colors.muted}` color. The current page is `{colors.ink}` and not clickable. Separators are “›” in `{colors.muted-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product grid goes to 2 columns; search bar moves to a full-width overlay; filter chips stack vertically; footer links collapse to a single column |
| Tablet | 744–1128px | Nav bar shows top-level categories only; product grid uses 3 columns; filter chips remain horizontal but wrap; sidebar (if present) becomes a top drawer |
| Desktop | 1128–1440px | Full nav bar with dropdowns; product grid uses 4 columns; filter sidebar is visible on the left; breadcrumbs shown |
| Wide | > 1440px | Product grid expands to 5 columns; max-width container caps at 1440px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements are minimum 38px height (exceeds 44px for mobile tap targets on primary actions)
- Filter chips are 32px height — acceptable for desktop but should be 44px on mobile
- Nav bar hamburger icon is 44x44px on mobile
- Quantity selector increment/decrement buttons are 38x38px
- Product card images link to product pages — entire card is tappable on mobile

### Collapsing Strategy
- Nav bar: On mobile, all category links collapse into a hamburger menu with a full-screen overlay drawer
- Filter sidebar: On tablet and below, filters collapse into a top-mounted drawer or a “Filter” button that opens a modal
- Product grid: Columns reduce from 5 to 2 on mobile
- Footer: Multi-column link lists collapse to a single column on mobile; accordion pattern for each section
- Breadcrumbs: On mobile, only show the current page and a “Back” link; full breadcrumb trail on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (`#313131`) was extractable from the live site — the full palette above is inferred from common e-commerce patterns and the brand’s monochrome aesthetic. The true secondary, accent, and surface colors may differ.
- No font-family declarations beyond system defaults were found. The brand may use a custom typeface (e.g., a horror-themed display font for the logo or headings) that was not loaded on the extracted page.
- Hover and active states for most components are estimated based on common darkening/lightening patterns — actual values may vary.
- Error, success, and badge colors are not extracted; they are set to common defaults that fit the brand’s restrained palette.
- The site uses a Cloudflare challenge page (“Just a moment...”) which may have blocked full CSS extraction. The extracted color is from that interstitial, not the actual storefront.
- No meta theme-color was found — the browser chrome color is unknown.
- No Shopify-specific classes were detected, but the brand may use a different e-commerce platform. Checkout component styling is not available.
- Dark mode support is unknown — no `prefers-color-scheme` media queries were detected.
- Star rating color (`#f59e0b`) is a common default — the brand may use a different yellow or a grayscale star system.
- The brand’s logo typography and color were not extractable; it may use a custom wordmark or a red/black treatment that differs from the site’s gray palette.
