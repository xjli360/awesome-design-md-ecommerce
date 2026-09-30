---
version: alpha
name: "HobbySearch"
source_url: "https://www.1999.co.jp/eng/"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dense, information-rich catalog marketplace for hobbyists and collectors, built on a stark white canvas and a single dark anchor — #313131 — that appears in every header bar, footer block, and primary text element. The site reads like a well-organized warehouse: rows of product thumbnails in tight grids, each card carrying a price tag, a stock indicator, and a small cart icon, all packed within a 960px centered column. Navigation is a horizontal strip of category links (Plastic Models, Diecast, Figures, etc.) in a compact 14px system font, with a prominent search bar and a "New Items" tab that acts as the default landing. The color palette is almost entirely achromatic — white backgrounds, gray borders, black text — with the exception of small red sale badges and blue link underlines that appear in product descriptions. There are no hero images, no full-bleed photography, no decorative illustrations; every pixel is devoted to product density and scannability. The typography stack is the browser's native sans-serif fallback chain, meaning HobbySearch deliberately avoids custom typefaces in favor of maximum rendering speed and system familiarity. Buttons are rectangular with sharp corners (`{rounded.none}`), and the overall feel is that of a functional database dressed in a clean, no-nonsense monochrome shell.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#999999"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#cc0000"
  link-blue: "#0066cc"
  stock-green: "#2e7d32"
  stock-orange: "#e65100"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
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
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 32px
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
    padding: 7px 15px
    height: 32px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 6px 10px
    height: 32px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 40px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 12px
  nav-bar-link-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.none}"
    height: 160px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  product-card-stock:
    typography: "{typography.caption}"
    textColor: "{colors.stock-green}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 6px 10px
    height: 32px
    border: "1px solid {colors.hairline}"
  search-submit-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    height: 32px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 36px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 0 12px
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 12px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.link-blue}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The standard action button, rendered as a solid dark rectangle (`{colors.primary}`) with white text. Used for "Add to Cart", "Search", and primary form submissions. On hover/active, the background shifts to `{colors.primary-active}` for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` with no border, signaling the button is non-interactive. All buttons use `{rounded.none}` — there are no rounded corners anywhere in the system.

**`button-secondary`** — An outlined variant with a white background and dark text, used for secondary actions like "View Details" or "Cancel". The border is a single 1px `{colors.hairline}` stroke. Hover state adds a 1px `{colors.primary}` border for visual distinction.

**`button-tertiary-text`** — A text-only link styled as a button, using `{colors.link-blue}` for the text color. Used for inline actions like "See more" or "Read reviews". No background, no border.

### Navigation
**`nav-bar`** — The primary top navigation, a 40px dark bar (`{colors.primary}`) that spans the full width. Links are white, 14px bold, with 12px horizontal padding. The active tab uses a darker background (`{colors.primary-active}`). The bar contains category links, a search input, and a login/account link.

**`category-strip`** — A secondary navigation bar below the main nav, 36px tall with a light gray background (`{colors.surface-soft}`). Contains subcategory tabs. The active tab is a solid dark rectangle matching the primary nav, while inactive tabs are muted gray text.

**`breadcrumb`** — A small, muted text row showing the current page path (e.g., Home > Plastic Models > Aircraft). Links use `{colors.link-blue}` for clickability, while the current page is rendered in `{colors.muted-soft}`.

### Cards
**`product-card`** — The core content unit: a white rectangle with a 1px soft gray border, 8px padding, and no rounded corners. Contains a 160px product image, a bold 14px title, a 14px price in `{colors.primary}`, and a stock status indicator in green or orange. A red sale badge (`{colors.sale-badge}`) overlays the top-left corner of the image when applicable. Cards are arranged in a multi-column grid with 8px gaps.

### Forms
**`text-input`** — A standard 32px input field with a 1px `{colors.hairline}` border and no border-radius. On focus, the border switches to `{colors.primary}`. Used for search queries, login forms, and checkout fields.

**`search-bar`** — A dedicated search input paired with a `search-submit-button`. The input is 32px tall with a 1px border, and the submit button is a solid dark rectangle to its right. The combined unit sits in the top nav or as a standalone element on category pages.

### Footer
**`footer`** — A full-width dark bar (`{colors.primary}`) at the bottom of every page, containing company links, help sections, and legal text in white 12px type. Links are white and underlined on hover.

### Pagination
**`pagination-button`** — Small square buttons (4px padding) with a 1px `{colors.hairline}` border, used to navigate between product listing pages. The active page button uses `{colors.primary}` background with white text. Inactive buttons have a white background with dark text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; category strip hidden; search bar moves below nav; product cards stack vertically with full-width images |
| Tablet | 744–1128px | Two-column product grid; nav bar shows top-level categories only; subcategories in a scrollable horizontal strip; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all categories visible; breadcrumbs shown; pagination at bottom |
| Wide | > 1440px | Four-column product grid; max-width container (1200px) centered; extra whitespace on sides; no layout changes beyond column count |

### Touch Targets
- All buttons and links: minimum 44x44px tap target (enforced via padding and height)
- Nav bar links: 40px height, full tap area
- Product card: entire card is tappable, linking to product detail page
- Category tabs: 36px height, full width of text area
- Pagination buttons: 32x32px minimum

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger icon; a slide-out drawer reveals all categories
- The category strip is hidden on mobile; categories are accessed via the hamburger menu
- Product images reduce to a 1:1 aspect ratio on mobile to fit narrower columns
- The footer collapses to a single column on mobile, with links stacked vertically
- Breadcrumbs are hidden on mobile; only the current page title is shown

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is extremely limited (only `#313131` was reliably identified from the live site). Additional colors (sale badge red, link blue, stock indicators) are inferred from common e-commerce patterns on similar Japanese hobby sites, not extracted directly.
- No hover, focus, or active states were extractable for most components beyond the primary button.
- Font sizes and line heights are estimated based on typical system-font usage at 14px body copy; the live site may use different values.
- No spacing or rounded values could be extracted; the system uses 0px border-radius (sharp corners) and standard 8px grid increments based on visual inspection.
- No dark mode or high-contrast mode styles are defined.
- The brand may use a secondary color for promotional banners or seasonal campaigns that was not captured.
- Error states for forms (validation, required fields) are not documented.
- The checkout flow (cart page, payment forms) was not analyzed and may have its own sub-palette.
- No iconography or illustration style was extracted; the site appears to use standard Unicode characters and simple CSS arrows for navigation.
