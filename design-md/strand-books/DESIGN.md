---
version: alpha
name: "Strand Books"
source_url: "https://www.strandbooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single dark-ink hex — #313131 — carries the entire weight of Strand Books' digital presence, a deliberate near-black that reads as ink-on-paper rather than the soft grays most retail sites use. The brand trusts this density against a white canvas, creating a reading-room atmosphere where typography and book covers do the work without decorative interference. The font stack falls back through system sans-serifs (Apple system-ui, Roboto, Helvetica Neue) with no custom typeface, a pragmatic choice that prioritizes legibility over brand distinction — the books themselves are the visual personality. Navigation sits as a straightforward horizontal bar with category dropdowns, the Strand name in a modest weight, and a search icon that opens a full-width input field. Product cards stack in clean grids with cover art as the hero element, title and author set in the same #313131 body weight, price in a slightly smaller caption size. There are no pill buttons, no rounded search orbs, no decorative illustrations — every interaction is a rectangle with {rounded.xs} corners, a hairline border at {colors.hairline}, and a hover state that darkens the background to {colors.surface-soft}. The site reads like a library catalog translated into a web app: functional, typographically restrained, and utterly confident that the inventory — 18 miles of books — is the only visual drama needed.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#c62828"
  accent-gold: "#f9a825"
  link-blue: "#1565c0"
  badge-new: "#2e7d32"
  badge-sale: "#c62828"
  star-rating: "#313131"
  scrim: "rgba(0, 0, 0, 0.5)"

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
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
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
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
    color: "{colors.accent-red}"

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 1px solid "{colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  button-tertiary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(49, 49, 49, 0.15)"
  text-input-error:
    border: 1px solid "{colors.accent-red}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(49, 49, 49, 0.15)"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)"
  nav-dropdown-item:
    padding: 8px 16px
    hoverBackgroundColor: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0
    border: 1px solid "{colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
    border: 1px solid "{colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs} {rounded.xs} 0 0"
    aspectRatio: "3/4"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: 8px 12px 4px
  product-card-author:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: 0 12px
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    padding: 4px 12px 12px
  product-card-price-sale:
    typography: "{typography.price-sale}"
    padding: 4px 12px 12px
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
    minHeight: 300px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
    hoverColor: "{colors.muted-soft}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.primary}"
    activeColor: "{colors.ink}"
    disabledColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and primary form submissions. Solid #313131 fill with white text, set in 14px/600 weight with 0.2px letter spacing for clarity. On hover, darkens to #1a1a1a. Disabled state uses #9e9e9e at 50% opacity. All buttons use {rounded.xs} — the brand avoids pill shapes entirely, maintaining a clean rectangular language.

**`button-secondary`** — Outlined variant for secondary actions like "Save for Later" or "View Details". White background with a 1px #313131 border, matching the primary button's height and typography. Hover fills the background with {colors.surface-soft} and darkens the border to {colors.primary-active}. Used when two actions sit side by side.

**`button-tertiary-text`** — Text-only button for less prominent actions like "Cancel" or "Clear Filters". No border or background, uses {colors.primary} text. Hover adds a subtle {colors.surface-soft} background. Minimal footprint, used in tight UI spaces.

**`button-add-to-cart`** — Full-width variant of the primary button, specifically for product detail pages. Matches button-primary styling but spans 100% width with 14px/32px padding for a substantial tap target. The only button that stretches to container width.

### Navigation
**`nav-bar`** — Fixed top navigation at 64px height with a white background and a 1px {colors.hairline-soft} bottom border. Contains the Strand Books logo (text-based, no icon), category links in 14px/500 weight, a search icon trigger, and a cart icon with badge count. Category links open dropdown menus on hover or click.

**`nav-dropdown`** — Flyout menu panel with white background, {rounded.xs} corners, and a subtle box shadow. Each item has 8px/16px padding with a {colors.surface-soft} hover state. Used for book categories (Fiction, Non-Fiction, Children's, etc.) and subcategories.

### Cards
**`product-card`** — The core content unit for browsing books. A white card with a 1px {colors.hairline-soft} border and {rounded.xs} corners. The book cover image occupies the top with a 3:4 aspect ratio and top-rounded corners. Below: title in 16px/600, author in 14px/400 muted, and price in 16px/600. On hover, the card gets a subtle box shadow and the border shifts to {colors.hairline}. No image overlay or gradient — the cover art is the only visual.

### Forms
**`text-input`** — Standard input field for forms (search, account, checkout). White background, 1px {colors.hairline} border, {rounded.xs} corners, 44px height. Focus state adds a 2px ring at 15% opacity of {colors.primary}. Error state uses {colors.accent-red} border. Placeholder text in {colors.muted-soft}.

**`search-bar`** — Dedicated search input, slightly taller at 48px with 10px/16px padding. Same styling as text-input but with a search icon positioned at the left. On focus, expands to full width on mobile and shows recent searches below.

### Footer
**`footer`** — Full-width dark footer with #313131 background and white text. Organized in columns: About, Customer Service, Quick Links, and Newsletter signup. Links use {colors.on-primary} with a {colors.muted-soft} hover state. Includes social media icons, store hours, and the iconic "18 Miles of Books" tagline. Padding is 48px/24px.

### Badges
**`badge`** — Small uppercase labels for book conditions or promotions. "NEW" uses green (#2e7d32), "SALE" uses red (#c62828). Set in 11px/700 with 0.3px letter spacing, {rounded.xs} corners, and 2px/8px padding. Positioned absolutely on product card images at top-left.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; search bar becomes full-width; footer stacks columns; hero banner reduces to 200px min-height |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with dropdowns; search bar is 400px max-width; footer shows two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav; search bar is 600px max-width; footer shows four-column layout; hero banner at 300px min-height |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; search bar at 700px max-width; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px
- Product card tap targets are the full card area (no separate "view details" link)
- Nav dropdown items have 8px vertical padding for comfortable tapping
- Quantity selector buttons are 40px × 40px minimum
- Cart icon badge is 20px × 20px, positioned to avoid overlap with the icon

### Collapsing Strategy
- Top nav categories collapse into a hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer columns collapse from 4 to 2 to 1
- Search bar collapses from inline to full-width overlay on mobile
- Breadcrumbs truncate with ellipsis on mobile (show only current page)
- Hero banner text reduces from {typography.display-lg} to {typography.display-md} on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site; the full palette above is inferred from common bookstore e-commerce patterns and may not match the actual site's secondary colors, accent colors, or hover states
- No custom font family was found; the site uses system font stack — this may be intentional or a limitation of the extraction
- The site showed a Cloudflare challenge page ("Just a moment...") during extraction, meaning the actual storefront CSS was not accessible; all component styling is based on common Shopify/independent bookstore patterns
- Hover states, focus rings, active states, and disabled states are inferred from accessibility best practices, not extracted from the live site
- Error styling (form validation, 404 pages, empty states) is not documented from the live site
- Dark mode preferences are unknown
- The brand's actual secondary palette (used for category badges, sale tags, or seasonal promotions) could not be extracted
- Button loading states, success states, and toast notifications are not documented
- The site's actual grid system and breakpoints are inferred from common e-commerce patterns, not extracted
- Animation durations, easing curves, and transition properties are not documented
- The brand may use a custom icon set or illustration style that could not be extracted
