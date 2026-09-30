---
version: alpha
name: "Kingston"
source_url: "https://www.kingston.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, industrial #313131 ink anchors Kingston's entire interface — not as a secondary or accent but as the primary color, a rare choice for a consumer electronics brand that signals reliability over flash. The single extracted hex from the live site tells a story of restraint: no bright CTA color, no gradient hero, no brand mark in a signature hue. Instead, the brand trusts its dark charcoal to carry every button, every headline, and every navigation element, creating a uniform, almost architectural presence. Type runs through the system font stack — -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif — with no custom typeface, a pragmatic decision that prioritizes legibility across global markets and device types. The interface reads as a technical catalog: dense product grids, specification tables, and comparison charts sit on a white canvas with hairline-thin borders, letting the hardware photography provide the only color. There are no pill-shaped buttons or soft rounded cards; corners stay tight at {rounded.sm} for buttons and {rounded.md} for cards, reinforcing a precision-tool aesthetic. The brand's voice is informational, not aspirational — every pixel exists to help a buyer compare storage speeds, capacities, and form factors without visual distraction. This is a design system built for the B2B and enthusiast buyer who values spec sheets over splash pages.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#0056b3"
  link-hover: "#003d7a"
  success: "#2e7d32"
  warning: "#f57c00"
  error: "#d32f2f"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
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
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-row:
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.link}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.link-hover}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Buy Now", "Add to Cart", and "Find a Retailer". Rendered in the brand's signature {colors.primary} with white text, a compact {rounded.sm} corner, and system font at 14px weight 600. On hover, the background shifts to {colors.primary-active} (#1a1a1a) for a subtle darkening effect. The disabled state uses {colors.primary-disabled} (#a0a0a0) to signal non-interactivity without introducing a new color.
**`button-secondary`** — An outlined variant for secondary actions like "Compare" or "Learn More". Uses a white background with a 1px {colors.primary} border and matching text color. Active state fills the background with {colors.surface-soft} and darkens the border to {colors.primary-active}. Height and typography match the primary button for consistent row alignment.
**`button-tertiary`** — A text-only button for inline actions within product cards or spec tables. No background or border, only {colors.primary} text at 14px weight 600. Used for "View Details" links that shouldn't compete with primary CTAs.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px {colors.hairline} border and {rounded.md} corners. Contains a square product image with {rounded.sm} corners, product name in {typography.title-sm}, specs in {typography.body-sm}, and a price or badge. On hover, the border switches to {colors.primary} and a subtle box shadow appears, creating a selection state without changing the card's background.
**`product-badge`** — Small uppercase labels that appear on product cards for "New", "Best Seller", or "Limited Edition". Uses {colors.primary} background with white text at 11px weight 700 and tight {rounded.xs} corners. A success variant ({colors.success}) is reserved for "In Stock" badges, and a warning variant ({colors.warning}) for "Low Stock" or "Backorder" indicators.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height with a white background and a 1px {colors.hairline} bottom border. Navigation links use {typography.nav-link} at 14px weight 600 with 0.3px letter spacing. The active link is indicated by a 2px {colors.primary} bottom border and matching text color, while inactive links render in {colors.muted}. The bar contains the Kingston logo on the left, primary nav links in the center, and a search icon with a support link on the right.
**`breadcrumb`** — A secondary navigation pattern used on product detail and category pages. Links render in {colors.muted} at 12px weight 400, with the current page in {colors.ink}. Chevron separators between items use the same muted tone.

### Forms
**`text-input`** — Standard single-line text input for search, newsletter signup, and contact forms. White background with a 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border thickens to 2px and switches to {colors.primary}. Error state uses a 1px {colors.error} border. Height is 40px to match button heights for inline form layouts.
**`select-input`** — Dropdown select for filtering product lists (by capacity, form factor, interface). Same dimensions and border treatment as text-input, with a custom dropdown arrow in {colors.muted}.

### Tables
**`spec-table`** — The signature data display component for Kingston's technical audience. A bordered table with {colors.surface-soft} header rows using {typography.title-sm} and body rows in {typography.body-sm}. Each row has a 1px {colors.hairline-soft} bottom border. Used extensively on product detail pages to compare speeds, capacities, dimensions, and compatibility across the SSD, RAM, and flash memory product lines.

### Search
**`search-bar`** — A dedicated search input for the product catalog, distinct from the general site search. Same dimensions as `text-input` but with a search icon inset on the left and a clear button on the right when text is entered. Focus state uses the same 2px {colors.primary} border treatment.

### Footer
**`footer`** — A full-width footer on {colors.surface-soft} background with {colors.body} text. Contains columns for product categories, support links, company information, and legal notices. Links use {colors.link} (#0056b3) with a hover state of {colors.link-hover} (#003d7a). Padding is {spacing.xxl} (48px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, full-width cards |
| Tablet | 744–1128px | Two-column product grid, visible top nav with dropdowns, two-column footer |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, three-column footer, spec tables at full width |
| Wide | > 1440px | Max-width container at 1440px, four-column product grid, additional whitespace on hero |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 40px height for touch accuracy
- Product card tap targets extend to the full card area, not just text links
- Nav links have 48px minimum tap height on mobile
- Search bar and form inputs maintain 40px height across all breakpoints

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with the logo centered and search icon on the right
- Product grids reduce columns from 4 to 1 on mobile, with cards becoming full-width
- Footer columns stack vertically on mobile, with accordion-style expandable sections for each category
- Spec tables convert to a stacked label-value layout on mobile, with each row becoming a two-line block
- Hero banners reduce padding and font size on mobile, with {typography.display-lg} replacing {typography.display-xl}

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extractable from the live site; additional brand colors (link blue, success green, warning orange, error red) are inferred from common web patterns and may not match Kingston's actual palette
- No custom font family was detected; the system font stack is used throughout but Kingston may license a proprietary typeface for marketing materials
- Hover and focus states for all components are estimated based on common accessibility patterns, not extracted from the live site
- Error, success, and warning color values are generic and may not match Kingston's actual semantic palette
- Dark mode styling is not documented as no dark mode was detected on the live site
- Animation and transition durations, easing curves, and micro-interaction patterns are not captured
- Iconography style (line weight, corner radius, stroke width) is not documented
- The brand's secondary palette for sub-brands (Kingston IronKey, Kingston FURY, etc.) is not captured
- Product comparison tool styling and multi-select patterns are not documented
- Loading states, skeleton screens, and empty states are not captured
- Print stylesheet behavior is not documented
