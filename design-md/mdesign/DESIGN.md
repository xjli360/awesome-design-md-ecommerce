---
version: alpha
name: "mDesign"
source_url: "https://mdesignhomedecor.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bright, orderly home organization brand that uses #e9be33 — a warm, almost buttery yellow — as its primary voltage, a color choice that signals energy and optimism rather than the muted beiges or cool grays typical of the category. The palette pivots on a crisp #eaeaea canvas and #cccccc hairline, creating a clean, almost clinical grid that lets product photography and that yellow pop. Typography defaults to Arial and Helvetica Neue at moderate weights — there is no custom brand typeface, so the system relies on generous spacing and clear hierarchy: titles sit at 22px weight 600, body at 15px weight 400, and captions at 12px. Buttons use the full {rounded.sm} radius, while product cards and modals use {rounded.md} — the brand avoids hard corners but stops short of the pill-shaped extremes found in marketplace design. The nav bar is a fixed 64px strip of {colors.canvas} with a subtle {colors.hairline} bottom border, and the search bar sits as a full-width field with a {colors.primary} accent border on focus. Category badges appear as small {rounded.xs} pills in {colors.primary} with white text, and sale tags use a darker #31373d ink on a yellow field. The overall effect is a system that feels like a well-organized closet: everything has its place, the yellow draws the eye to what matters, and the white space breathes.

colors:
  primary: "#e9be33"
  primary-active: "#d4a91f"
  primary-disabled: "#f0d47a"
  ink: "#31373d"
  body: "#6c6c6c"
  muted: "#8a8a8a"
  muted-soft: "#a0a0a0"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#eaeaea"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#31373d"
  sale-badge-bg: "#e9be33"
  sale-badge-text: "#31373d"
  category-badge-bg: "#479ccf"
  category-badge-text: "#ffffff"
  error: "#c0392b"
  success: "#27ae60"
  link: "#479ccf"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
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
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    fontWeight: 600
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.error}"
    fontWeight: 600
  category-badge:
    backgroundColor: "{colors.category-badge-bg}"
    textColor: "{colors.category-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.on-primary}"
    marginTop: "{spacing.md}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
    fontWeight: 600
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "0 12px"
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with {colors.primary} yellow and dark {colors.on-primary} text. On hover, it shifts to {colors.primary-active} for a subtle darkening effect. The disabled state uses {colors.primary-disabled} to maintain the yellow family while signaling inactivity. All primary buttons use {rounded.sm} and 44px height for comfortable tapping.

**`button-secondary`** — An outlined alternative with a {colors.canvas} background and a 1px {colors.hairline} border. On active state, the border thickens to {colors.ink} for clear feedback. Use for secondary actions like "Cancel" or "Save for Later" alongside primary buttons.

**`button-tertiary-text`** — A text-only button with no background or border. Uses {colors.ink} text and the same {typography.button-md} sizing. Reserved for inline actions like "Clear filters" or "View all" where visual weight should be minimal.

**`button-pill-primary`** — A fully rounded variant of the primary button, using {rounded.full} for a softer, more approachable look. Used for filter chips, category tags, or promotional badges. The smaller {typography.button-sm} keeps it compact.

**`button-pill-outline`** — The outlined counterpart to the pill primary, with a 1px {colors.hairline} border. Used for filter options that are not currently selected, or for secondary tags in a category strip.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.md} corners and 12px padding. The image area uses {rounded.sm} and a 1:1 aspect ratio for consistent product shots. On hover, a subtle box shadow lifts the card. The title uses {typography.title-sm} in {colors.ink}, and the price uses {typography.body-md} with 600 weight. Sale prices render in {colors.error}.

**`category-badge`** — A small, compact badge using {colors.category-badge-bg} (#479ccf) blue with white text. Uses {rounded.xs} for a tight, precise look. Applied to category labels on product cards or navigation filters.

**`sale-badge`** — A promotional badge using the brand's {colors.primary} yellow with dark text. Same {rounded.xs} and {typography.badge} sizing as the category badge, but with the brand's signature yellow to draw immediate attention to discounts.

### Navigation
**`nav-bar`** — A fixed 64px header strip on {colors.canvas} with a 1px {colors.hairline} bottom border. Navigation links use {typography.nav-link} — 14px weight 600 with 0.5px letter spacing and uppercase transformation. Active links render in {colors.primary}, inactive in {colors.muted}. The bar stays pinned at the top on all viewports.

**`breadcrumb`** — A secondary navigation path using {typography.caption} in {colors.muted}. The active (current) breadcrumb segment uses {colors.ink} with 600 weight. Segments are separated by a "/" or ">" character in {colors.hairline}.

### Forms
**`text-input`** — A standard input field with a white background, 1px {colors.hairline} border, and {rounded.sm}. On focus, the border becomes a 2px {colors.primary} yellow. Error states use a 2px {colors.error} red border. Height is 44px with 10px 14px padding for comfortable typing.

**`search-bar`** — A wider, more prominent input at 48px height, designed for the site's search functionality. Same styling as text-input but with additional padding for the search icon. On focus, the 2px {colors.primary} border activates.

**`quantity-selector`** — A compact input group for adjusting product quantities. The container has a 1px {colors.hairline} border and {rounded.sm}. Plus/minus buttons sit flush on either side with no background, using {typography.button-md} for the symbol. The central value uses {typography.body-md}.

### Footer
**`footer`** — A dark footer section on {colors.ink} background with {colors.canvas} text. Links use {colors.muted-soft} and shift to {colors.primary} on hover. The footer includes link columns, a newsletter signup, and social icons. Padding uses {spacing.section} (64px) top and bottom for generous breathing room.

### Hero
**`hero-banner`** — A full-width banner on {colors.primary} yellow with dark text. Uses {typography.display-lg} for the headline and {typography.body-md} for the subtitle. The yellow background creates a high-energy entry point that aligns with the brand's optimistic tone.

### Accordion
**`accordion-header`** — A clickable header on {colors.canvas} with a 1px {colors.hairline} bottom border. Uses {typography.title-sm} for the label. The expanded state typically includes a rotated chevron icon. Content panels use {colors.surface-card} with {typography.body-sm} for readable product details or FAQ answers.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), nav collapses to hamburger menu, hero banner reduces to {typography.display-md}, search bar moves below nav, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero banner at full width with {typography.display-lg}, search bar in nav row |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero banner with max-width container, search bar centered in nav |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) for content, hero banner constrained to container width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and badges are at least 36px tall
- Quantity selector buttons are 40px tall with 12px horizontal padding
- Nav links have 48px tap targets within the 64px nav bar
- Product card tap targets span the full card width

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer
- Product grids reduce columns from 4 → 3 → 2 → 1 as viewport shrinks
- Footer link columns stack vertically on mobile, with each column taking full width
- Hero banner text reduces in size on mobile to prevent overflow
- Search bar moves from inline in the nav to a full-width row below the nav on mobile
- Category badges in filter strips wrap to multiple rows on smaller screens
- Accordion sections remain collapsed by default on all viewports

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The live site was unavailable during extraction, so the hex palette is derived from a limited crawl of cached CSS and HTML. Hover states, focus rings, and active states for all components are inferred from common patterns rather than observed.
- No meta theme-color was found, so the browser chrome color is unknown.
- The site appears to not be on Shopify, but the exact e-commerce platform is unconfirmed.
- Font stack is limited to Arial/Helvetica — no custom brand typeface was detected. The brand may use a web font that wasn't loaded during extraction.
- Dark mode styling is not present in the extracted data.
- Error page styling, 404 layouts, and empty state designs are not documented.
- Checkout flow components (cart drawer, payment forms, shipping selectors) are not extracted.
- Modal/dialog overlay styling and animation timing are unknown.
- Star rating or review component styling is not present in the extracted data.
- Newsletter signup form styling (email input, submit button in footer) is inferred from general input patterns.
- Social media icon colors and hover states are not documented.
- The exact spacing scale for product grid gaps is estimated from common e-commerce patterns.
- Mobile nav drawer animation, overlay opacity, and close button styling are not extracted.
