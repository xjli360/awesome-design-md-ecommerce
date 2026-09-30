---
version: alpha
name: "Presto"
source_url: "https://www.gopresto.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  That saturated lawn-green (#6fa237) pushing through every primary button on gopresto.com reads less like a tech brand and more like the power-indicator light glowing on the front panel of a countertop pressure cooker — functional proof that something is on and ready. The palette never strays far from a gray continuum: deep near-blacks (#1b1b1b, #222222) for headline ink, a warm mid-gray (#555555) for body copy, and a graduated ladder of silvers (#767676, #a6a6a6, #aaaaaa) for captions and placeholders, all sitting on a stack of barely-there off-whites (#f5f5f5, #f2f2f2, #fafafa) that feel like the brushed-aluminum finish on a Presto electric skillet. There is no custom typeface in the build — the entire typographic system runs on Arial and Helvetica, system fonts with zero download cost, which gives the site the same utilitarian directness as an instruction manual folded inside the box. Display headings hit 32–36px at weight 700, bold enough to anchor a product hero without borrowing the editorial gravitas of a serif. A secondary green spectrum (#368a55, #43ac6a, #3a945b) handles success states, in-stock indicators, and promotional callouts, while a loud signal-red (#ec0000) and its darker sibling (#bd0000) mark sale prices and error validation — the same red you'd see on a stovetop burner ring. An informational blue (#00bbff) and a softer sky-blue (#61b6d9, #a0d3e8) appear sparingly for links and tooltip accents. Corners stay conservative: buttons and inputs use a modest `{rounded.sm}` (8px), product cards round to `{rounded.md}` (12px), and nothing on the page reaches for a pill shape — the geometry is squared-off and appliance-like, as if every container were stamped from sheet metal. Spacing is generous at the section level (`{spacing.section}` = 64px between major content blocks) but tightens inside product grids and spec tables, reflecting a catalog that prioritizes density of information — wattage, dimensions, capacity — over lifestyle storytelling.

colors:
  primary: "#6fa237"
  primary-active: "#368a55"
  primary-disabled: "#b8d4a0"
  ink: "#222222"
  ink-deep: "#1b1b1b"
  body: "#555555"
  muted: "#767676"
  muted-soft: "#a6a6a6"
  placeholder: "#aaaaaa"
  hairline: "#d8d8d8"
  hairline-soft: "#e2e2e2"
  border-strong: "#969696"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-mid: "#f2f2f2"
  surface-card: "#ffffff"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#43ac6a"
  success-dark: "#3a945b"
  sale-red: "#ec0000"
  sale-red-dark: "#bd0000"
  accent-blue: "#00bbff"
  accent-blue-soft: "#61b6d9"
  accent-blue-pale: "#a0d3e8"
  accent-orange: "#cf6e0e"
  accent-orange-light: "#f08a24"
  highlight-yellow: "#ffff00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
  nav-link-sm:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  product-price:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  product-sale-price:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  spec-value:
    fontFamily: "Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, 'Liberation Mono', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.border-strong}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  top-nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link-sm}"
    padding: "{spacing.sm} {spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-blue}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.sale-red}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md} {rounded.md} 0 0"
    padding: "{spacing.base}"
  product-card-content:
    padding: "{spacing.md} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    color: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.product-sale-price}"
    color: "{colors.sale-red}"
  product-card-badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.35)"
    textColor: "{colors.on-dark}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-card-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.on-dark}"
    textTransform: uppercase
  badge-in-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  badge-clearance:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  notification-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 28px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, rendered in Presto's signature green (#6fa237) with white uppercase text and 8px rounding (`{rounded.sm}`). Used for "Shop Now," "Add to Cart," and primary form submissions. On hover/active, the background deepens to #368a55 (`{colors.primary-active}`), and the disabled state fades to a washed-out sage (#b8d4a0) that reads as clearly inactive. The squared-off shape — no pill radii anywhere — mirrors the rectilinear geometry of the appliances themselves.

**`button-secondary`** — A white-background button with dark ink text and a 1px hairline border, used for "Learn More," "Compare," and secondary actions that sit alongside green primaries. On hover, the background fills with the surface-strong gray (`{colors.surface-strong}`) and the border darkens to `{colors.border-strong}` for subtle depth without competing with the primary action.

**`button-tertiary-text`** — A borderless, background-free text button colored in the brand green (`{colors.primary}`) for inline actions like "View All," "Clear Filters," or "See Details." The uppercase label and bold weight maintain button identity without adding container clutter to dense product listing pages.

**`button-sale`** — A high-urgency variant in signal red (#ec0000) for clearance CTAs and limited-time promotional banners. Shares dimensions and typography with the primary button but substitutes the green for the same red used on sale price text, creating a direct visual link between the discount and the action.

**`button-add-to-cart`** — A slightly taller (48px) variant of the primary button with larger label typography (`{typography.button-lg}`), dedicated to the product detail page's main purchase action. The extra 4px of height and wider padding (32px horizontal) give it more visual gravity than standard primary buttons used elsewhere.

### Navigation
**`top-nav`** — A white navigation bar at 72px height with a 1px bottom border (`{colors.hairline}`) that separates it from page content without adding shadow weight. The clean white background lets the green accents in active links and the logo carry all the brand signal. The bar spans full width and houses the logo, primary navigation links, search, and utility icons.

**`top-nav-link`** — Navigation links in bold 14px sans-serif (`{typography.nav-link}`) with dark ink color. The active state swaps to green text with a 3px bottom border in the primary color (`{colors.primary}`), creating an underline indicator that aligns with the bottom edge of the nav bar. This anchored-underline pattern gives the navigation a catalog-index feel.

**`top-nav-dropdown`** — Flyout menus that appear on hover, surfaced with a white background and a subtle box shadow for depth. Links inside use the lighter nav-link-sm typography and the softer body-gray color (`{colors.body}`), stepping back in visual weight from the parent nav links.

### Search
**`search-bar`** — A standard-height input (44px) with 8px rounding and a hairline border that blends into the nav bar. On focus, the border thickens to 2px and shifts to the informational blue (`{colors.accent-blue}`) for clear focus indication. Placeholder text uses `{colors.placeholder}` to distinguish it from user input without disappearing entirely on low-contrast displays.

### Cards
**`product-card`** — The primary catalog container with a white surface, 12px rounding (`{rounded.md}`), and no outer padding. The image area occupies the full card width with a soft gray background (`{colors.surface-soft}`) and top-only rounding, providing a consistent neutral backdrop for product photography regardless of the image's own background. The content zone below uses `{spacing.md}` top padding, `{spacing.base}` horizontal, and `{spacing.lg}` bottom for comfortable text spacing.

**`product-card-badge-sale`** — A compact red badge (#ec0000) overlaid on the product image to flag clearance or sale items. Uses uppercase 11px bold type (`{typography.badge}`) with minimal 4px rounding to keep it sharp and utilitarian. The green variant (`product-card-badge-new`) marks new arrivals using the brand primary.

**`category-card`** — A larger navigational card with a soft gray background (`{colors.surface-soft}`), 12px rounding, and `{spacing.lg}` internal padding, used on the homepage and category landing pages to route users to product families — "Pressure Cookers," "Electric Griddles," "Deep Fryers." The active state fills with the primary green and flips text to white.

### Spec Table
**`spec-table`** — A striped data table purpose-built for product specifications (wattage, dimensions, capacity, model number). Header rows use a darker surface (`{colors.surface-strong}`) with bold spec-label typography, while alternating body rows cycle between white and `{colors.surface-soft}` for scanability. Each row uses `{spacing.sm}` vertical and `{spacing.base}` horizontal padding for a dense, information-rich layout that prioritizes data over decoration.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px hairline border, and 8px rounding (`{rounded.sm}`). The 48px height provides ample space for the 16px body type. Focus shifts the border to 2px blue (`{colors.accent-blue}`), and error states use the sale red (`{colors.sale-red}`) for clear, accessible validation feedback.

**`quantity-selector`** — A horizontally arranged control for adjusting order quantities, with a central numeric display flanked by increment/decrement buttons. The buttons use small rounded squares (`{rounded.xs}`) with a soft gray background, and the entire control is wrapped in a 1px border to visually unify the three elements.

### Accordion
**`accordion-header`** — Collapsible section headers used for product descriptions, care instructions, and FAQ content. A soft gray background (`{colors.surface-soft}`) with bold title typography creates clear visual separation between sections. Content panels open beneath in white with body typography, maintaining readable line lengths at `{spacing.lg}` horizontal padding.

### Footer
**`footer`** — A full-width dark footer in near-black (#1b1b1b) with white heading text and muted-soft gray links. Section headings use uppercase caption typography for hierarchical clarity. The footer houses sitemap links, customer service information, warranty details, and social media icons — the kind of dense information architecture expected from a legacy appliance brand.

### Badges & Notifications
**`badge-in-stock`** — A green availability indicator using the success color (#43ac6a) for in-stock confirmation on product pages and search results. **`badge-clearance`** — An orange badge (#cf6e0e) for clearance and end-of-line products, visually distinct from both the green in-stock and red sale badges. Both use the same compact uppercase badge typography with 4px rounding.

**`notification-bar`** — A slim 40px banner in the primary green that spans full width above the navigation, used for site-wide promotional messages ("Free Shipping on Orders Over $50") and seasonal announcements. White body-sm text keeps the message legible without fighting the navigation below.

### Pagination
**`pagination-button`** — Standard page-number buttons with hairline borders and 8px rounding, used at the bottom of product listing pages. The active page fills with the primary green and switches to white text, providing an immediate location indicator within long catalogs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu with slide-out drawer; hero banner stacks headline over image; search bar moves into expandable icon; spec tables scroll horizontally; footer links collapse to single-column accordion; notification bar text truncates with ellipsis |
| Tablet | 744–1128px | Two-column product grid; top-nav shows condensed link set with "More" dropdown; hero banner uses side-by-side layout at reduced padding; category cards display 2-across; spec tables remain full-width; footer uses two-column layout |
| Desktop | 1128–1440px | Three-to-four column product grid; full top-nav with all category links visible; hero banner at full section padding (64px); search bar at full width in nav bar; spec tables show all columns; footer uses three-column layout with newsletter signup |
| Wide | > 1440px | Max-width container (1440px) centered; four-column product grid with additional whitespace at edges; hero banner constrained to max-width; all components scale proportionally within the centered frame |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target height on mobile
- Top-nav links use 16px horizontal padding for comfortable tap areas
- Product card tap targets extend to the full card surface, not just the title or image
- Quantity selector buttons maintain 28px minimum height with adequate spacing between controls
- Pagination buttons use at least 36px height with 8px gaps between numbers
- Search bar and text inputs use 44–48px height across all breakpoints

### Collapsing Strategy
- Top navigation collapses from full link set to hamburger menu at < 744px
- Product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Category cards collapse from 4-across to 2-across to single-column stacked
- Spec tables become horizontally scrollable on mobile with a fixed first column for labels
- Footer collapses from 3 columns to accordion-style expandable sections on mobile
- Hero banner image shifts from side-by-side to stacked above headline on mobile
- Notification bar remains single-line; text truncates rather than wrapping on narrow viewports
- Breadcrumbs truncate with ellipsis on mobile, showing only current and parent page

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web fonts detected — the site runs entirely on system stacks (Arial, Helvetica); if a branded typeface loads via JS or is gated behind authentication, it was not captured
- Meta theme-color is absent; mobile browser chrome color is unknown
- Exact box-shadow values for dropdowns, cards, and elevated components were not extracted
- Hover and focus transition timing (duration, easing curves) are unavailable
- Dark mode palette does not appear to exist on the current site
- Icon system could not be identified — Font Awesome 5 classes were detected but the specific icon subset and any custom SVG icons are unknown
- Loading state designs (skeleton screens, spinners, progress bars) were not captured
- Modal and dialog component styling (overlay opacity, close button position, animation) is unknown
- Z-index hierarchy for navigation dropdowns, modals, and notification bar was not extracted
- Exact product image aspect ratios and zoom interaction behavior are undocumented
- Newsletter signup form styling and validation states were not captured
- The site is not on Shopify; the underlying platform and any platform-specific component constraints are unknown
- Several orange and yellow accent colors (#cf6e0e, #f08a24, #ffff00) appear in the extraction but their precise usage contexts could not be confirmed — they may be seasonal or promotional
