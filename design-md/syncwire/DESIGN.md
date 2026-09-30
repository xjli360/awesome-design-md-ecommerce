---
version: alpha
name: "Syncwire"
source_url: "https://www.syncwire.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A utilitarian, high-trust electronics accessories brand built on a near-monochrome palette anchored by #2c2d2e — a deep, almost-black charcoal that reads as industrial and serious — and lifted by a single, unapologetic accent: #ffaa47, a warm marigold that appears on sale badges, promotional banners, and the occasional CTA, injecting urgency without breaking the technical mood. The canvas is #f5f5f5, a cool off-white that avoids the sterile glare of pure white, while #dadce0 and #dedede form the hairline and surface-soft layers that organize dense product grids. Syncwire’s typography runs Poppins at 400–600 weight, a geometric sans-serif with open apertures that keep spec tables and bullet-point feature lists legible at small sizes. The brand’s signature design move is the product card: a white rectangle (`{rounded.sm}`) with a centered hero image, a thin #dadce0 border, and a two-line title in `{typography.title-md}` — no badges, no overlays, just the product, its name, and a price. The top nav is a full-bleed #2c2d2e strip with white Poppins nav links and a search icon, suggesting a warehouse-like catalog where findability matters more than editorial curation. Buttons are flat and rectangular (`{rounded.xs}`), filled with #5f85c1 — a muted slate-blue that serves as the primary CTA across add-to-cart and checkout flows, a color that feels more like a functional affordance than a brand statement. The footer collapses into a dense #1a1c1d column of legal links and payment icons, reinforcing the brand’s no-frills, infrastructure-first posture. Syncwire does not decorate; it organizes.

colors:
  primary: "#5f85c1"
  primary-active: "#0047ba"
  primary-disabled: "#d3d3d3"
  ink: "#1a1c1d"
  body: "#2c2d2e"
  muted: "#6d6b6b"
  muted-soft: "#868d94"
  hairline: "#dadce0"
  hairline-soft: "#dedede"
  canvas: "#f5f5f5"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffaa47"
  accent-red: "#c62a32"
  accent-green: "#279a4b"
  accent-orange: "#e97f32"
  accent-blue-dark: "#003996"
  accent-blue-light: "#338fb1"
  accent-blue-mid: "#3f72e5"
  dark-bg: "#1b1b1c"
  dark-hairline: "#252f35"
  dark-muted: "#aaaeb6"
  dark-body: "#787c80"
  dark-surface: "#121212"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  price-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 40px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-bar-link:
    textColor: "{colors.surface-card}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-bar-link-active:
    textColor: "{colors.accent-marigold}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    margin: "{spacing.sm} 0 {spacing.xs} 0"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.body}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-out-of-stock:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.dark-muted}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  filter-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  rating-stars:
    color: "{colors.accent-marigold}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  review-date:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart" and "Shop Now" actions. A flat, rectangular button in slate-blue `{colors.primary}` with white Poppins 500 text. On hover, it shifts to `{colors.primary-active}` (#0047ba), a deeper, more authoritative blue. The disabled state drops to `{colors.primary-disabled}` (#d3d3d3) with `{colors.muted}` text, signaling unavailability without ambiguity.

**`button-secondary`** — An outlined variant used for "View Details" and secondary product-page actions. White background, `{colors.primary}` text, and a 1px `{colors.primary}` border. Active state inverts to filled `{colors.primary}` with white text. Used where the primary button would overwhelm — in filter panels, review sections, and cart summaries.

**`button-accent-marigold`** — A high-visibility promotional button reserved for limited-time offers, clearance sales, and banner CTAs. Filled `{colors.accent-marigold}` (#ffaa47) with dark `{colors.ink}` text. This is the only warm color in the button system, creating a deliberate visual spike that draws the eye to deals.

**`button-accent-red`** — A compact, urgent button used for "Clearance" and "Last Chance" badges. Small format (`{typography.button-sm}`, 32px height) in `{colors.accent-red}` (#c62a32) with white text. Appears as a floating badge on product cards or as a standalone CTA in promotional strips.

### Cards
**`product-card`** — The core inventory unit of the Syncwire catalog. A white rectangle with `{rounded.sm}`, a 1px `{colors.hairline-soft}` border, and `{spacing.base}` padding. The product image sits at the top with `{rounded.xs}`, followed by the title in `{typography.title-md}` (16px Poppins 500, `{colors.ink}`), then the price in `{typography.price-sm}` (14px Poppins 500, `{colors.body}`). A `{colors.accent-marigold}` sale badge can overlay the image top-left when a discount is active. Out-of-stock items display a gray badge instead. Cards are arranged in a responsive grid — 2 columns on mobile, 3 on tablet, 4 on desktop — with `{spacing.base}` gaps.

**`review-card`** — A customer review block with the same white-background, thin-border treatment as the product card. Contains the reviewer's name (`{typography.title-sm}`), a date (`{typography.caption}`, `{colors.muted}`), a star rating rendered in `{colors.accent-marigold}` 16px stars, and the review body in `{typography.body-sm}`. No avatar or decorative elements — just structured data.

### Navigation
**`nav-bar`** — A full-width, 56px strip in `{colors.ink}` (#2c2d2e) with white nav links in Poppins 500. The brand logo sits left-aligned, search icon right-aligned, and category links (Cables, Chargers, Mounts, etc.) spread across the center. Active or hovered links shift to `{colors.accent-marigold}`. On mobile, the category links collapse into a hamburger menu; the search icon remains visible.

**`search-bar`** — A pill-shaped input (`{rounded.full}`) with a white background, `{colors.hairline}` border, and `{colors.body}` placeholder text. The search icon button sits inside the pill on the right, rendered in `{colors.muted}`. On focus, the border shifts to `{colors.primary}`. The bar expands to full width on mobile and sits within the nav-bar on desktop.

### Forms
**`text-input`** — A standard form input for checkout, account creation, and newsletter signup. White background, `{colors.hairline}` border, `{rounded.xs}`, 40px height. Focus state swaps the border to `{colors.primary}`. Error state (not extracted, see Known Gaps) would likely use `{colors.accent-red}`.

**`quantity-selector`** — A compact, three-part control for cart quantity adjustment. A decrement button, a numeric display, and an increment button, all within a single `{rounded.xs}` container with `{colors.hairline}` border. The buttons use `{colors.primary}` for their +/- symbols. The numeric display uses `{typography.body-md}`.

### Footer
**`footer`** — A dense, dark footer in `{colors.dark-bg}` (#1b1b1c) with `{colors.dark-muted}` (#aaaeb6) body text and white section headings (`{typography.title-sm}`). Links are `{typography.link}` in `{colors.dark-muted}`. The footer is organized into columns (About, Support, Legal, Social) on desktop, collapsing into a single stacked column on mobile. Payment icons (Shopify Pay, Klarna, Afterpay, etc.) sit at the bottom in a row, rendered in grayscale.

### Badges & Indicators
**`product-card-sale-badge`** — A small, uppercase badge (`{typography.badge}`, 10px Poppins 600) in `{colors.accent-marigold}` with `{colors.ink}` text. Used to flag discounted items. Positioned absolutely over the product card image top-left.

**`trust-badge`** — A subtle, low-contrast badge in `{colors.surface-soft}` (#ededed) with `{colors.muted}` text. Used for "Free Shipping", "1-Year Warranty", and "30-Day Returns" indicators on product detail pages and cart summaries.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product grid goes to 2 columns; search bar becomes full-width below nav; footer stacks to single column; filter panel becomes a slide-out drawer. |
| Tablet | 744–1128px | Nav-bar shows all category links in condensed font; product grid at 3 columns; filter panel sits as a left sidebar on category pages; footer shows 2-column layout. |
| Desktop | 1128–1440px | Full nav-bar with expanded category links; product grid at 4 columns; filter panel as persistent left sidebar; footer at 4 columns; hero banner uses full-width layout. |
| Wide | > 1440px | Max-width container (1440px) centers content; product grid remains at 4 columns but with larger cards; hero banner uses constrained width with generous side margins. |

### Touch Targets
- All buttons and interactive elements are at least 40px tall (primary, secondary, text-input, quantity-selector).
- Nav-bar links have a minimum 44px tap area on mobile.
- Search icon button is 36px — slightly below the 40px recommendation but acceptable for an icon-only target.
- Product card tap target is the entire card surface, not just the title or button.

### Collapsing Strategy
- Nav-bar category links collapse into a hamburger drawer below 744px.
- Filter panel collapses into a slide-out drawer on mobile, triggered by a "Filters" button.
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks.
- Product card grid reduces columns from 4 to 3 to 2.
- Hero banner reduces font size and padding on mobile, and may hide secondary text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for buttons, links, and cards were not reliably extracted from the live site CSS. The `primary-active` color (#0047ba) is inferred from the extracted palette but may not be the exact hover target.
- **Error and validation styling** for form inputs (red borders, error messages) was not observed. The `accent-red` (#c62a32) is a candidate but unconfirmed.
- **Focus ring styling** (outline, box-shadow) for keyboard navigation was not extracted. Likely uses `{colors.primary}` or `{colors.accent-marigold}` but unknown.
- **Dark mode** is not present on the live site. The `dark-*` colors in the palette are extracted from footer and nav elements, not from a system-level dark theme.
- **Sub-brand or variant palettes** (e.g., Syncwire Pro, Syncwire Home) were not detected. The palette above represents the main storefront only.
- **Typography scale** is inferred from Poppins usage patterns. Exact font sizes, weights, and line heights for `display-xl`, `display-md`, etc., are best-guess based on common e-commerce patterns and the extracted font-family. The live site may use different values.
- **Spacing system** is a standard 4px/8px scale. The `section` value (64px) is an estimate for consistent vertical rhythm.
- **Rounded corner values** are inferred from common patterns. The `rounded.xs` (4px) for buttons is a strong signal from the extracted CSS, but `rounded.sm` (8px) for cards and `rounded.full` for search bars are assumptions.
- **Checkout flow** uses Shopify's default checkout, which has its own design system (Shopify Pay buttons, Klarna/Afterpay widgets). These are not part of Syncwire's brand system and are noted as external dependencies.
- **Animation and transition timing** (hover fades, page transitions, loading states) were not extracted. Likely uses 150–300ms ease-in-out but unconfirmed.
- **Iconography style** (line weight, stroke width, color) was not extracted. The search icon is the only visible icon; its style is unknown.
