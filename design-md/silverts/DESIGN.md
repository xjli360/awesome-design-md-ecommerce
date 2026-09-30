---
version: alpha
name: "Silverts"
source_url: "https://silverts.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the quiet dignity of adaptive clothing, Silverts uses a deep navy anchor (#15234a) that reads as trustworthy and institutional, not medical or sterile. The palette is dominated by near-blacks (#191919, #262626, #121212) and warm off-whites (#fafafa, #f8f8f8, #f3f3f3) that create a high-contrast, legible environment for an older audience. Two red accents — a bright, urgent #d72c0d and a softer #e8144b — serve as the primary action signals, appearing on CTAs, sale badges, and critical navigation elements. A surprising inclusion of #e0b5b2, a dusty rose, and #fff4fa, a blush white, softens the otherwise utilitarian palette, hinting at the brand's care-focused mission. Typography relies on AGaramondPro for display headings, lending a classic, almost editorial weight to category titles, while Assistant and Figtree handle body and interface copy in clean sans-serif. The site is a Shopify storefront, so checkout flows inherit Shopify's native button and form styling, but the brand's own components favor generous padding, clear hierarchy, and high-contrast text on soft surfaces. Cards use a subtle {rounded.sm} radius, while CTAs and badges use {rounded.md} — never fully pill-shaped, preserving a sense of grounded reliability over trendiness. The overall mood is one of calm authority: a place where function is foregrounded, but the warm rose and cream tones remind you that the user is always a person, not a patient.

colors:
  primary: "#15234a"
  primary-active: "#0f1a36"
  primary-disabled: "#8a94a8"
  ink: "#191919"
  body: "#262626"
  muted: "#5e5e5e"
  muted-soft: "#8a8a8a"
  hairline: "#cbcbcb"
  hairline-soft: "#dedede"
  canvas: "#fafafa"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d72c0d"
  accent-red-soft: "#e8144b"
  accent-rose: "#e0b5b2"
  accent-blush: "#fff4fa"
  badge-sale: "#d72c0d"
  badge-new: "#13a165"
  badge-new-bg: "#e0faef"
  star-rating: "#fbcd0a"
  link: "#2c6ecb"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'AGaramondPro', 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'AGaramondPro', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'AGaramondPro', 'Georgia', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Assistant', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Assistant', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Figtree', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Figtree', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Figtree', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Assistant', 'Figtree', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', 'Assistant', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Assistant', 'Figtree', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Figtree', 'Assistant', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Figtree', 'Assistant', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Assistant', 'Figtree', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Figtree', 'Assistant', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-accent-red-active:
    backgroundColor: "#b8230a"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-accent-red-disabled:
    backgroundColor: "#f0a090"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: "400px"
  hero-banner-alt:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: "400px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.hairline}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    minHeight: "120px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: "40px"
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and checkout initiation. Rendered in the deep navy {colors.primary} with white text, 12px rounded corners, and 48px height for comfortable tapping. On hover, shifts to {colors.primary-active} (#0f1a36). Disabled state uses {colors.primary-disabled} (#8a94a8) with reduced opacity on the text.

**`button-accent-red`** — Used for urgent actions like "Sale" collections, clearance items, and limited-time offers. Uses the bright {colors.accent-red} (#d72c0d) to create visual urgency. Hover state darkens to #b8230a. Disabled state fades to #f0a090.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More." Uses a white background with a 2px solid {colors.ink} border. On hover, fills with a light tint of {colors.primary}.

**`button-tertiary-text`** — A text-only button for less prominent actions like "Cancel" or "Clear Filters." Uses {colors.primary} text with no background or border. On hover, adds a subtle underline.

### Cards
**`product-card`** — The core product display unit, featuring a square aspect-ratio image with {rounded.sm} top corners and a white background. The title uses {typography.title-sm} in {colors.ink}, while the price uses {typography.body-md} at 600 weight. Sale badges appear as absolute-positioned red rectangles in the top-left corner using {colors.badge-sale}. New-arrival badges use a green-on-light-green treatment ({colors.badge-new-bg} background, {colors.badge-new} text).

**`category-tile`** — A navigational card for browsing product categories (e.g., "Men's Adaptive Clothing," "Women's Adaptive Clothing"). Uses a soft gray background ({colors.surface-soft}) with {rounded.sm} corners and centered title text. On hover, the background shifts to a light tint of {colors.primary}.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 72px tall with a white background and a subtle bottom border in {colors.hairline-soft}. Active nav links are indicated by a 2px bottom border in {colors.primary}. Inactive links use {colors.muted} text. The nav includes a search icon that expands into the `search-bar` component on click.

**`breadcrumb`** — A secondary navigation aid for product category pages and search results. Uses {typography.caption} in {colors.muted}, with the current page rendered in {colors.ink} for orientation.

### Forms
**`text-input`** — Standard form input for search, account forms, and checkout fields. Uses a white background with a 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border thickens to 2px and switches to {colors.primary}. Error states use a 2px {colors.accent-red} border.

**`select-input`** — Dropdown selectors for filtering (size, color, price range) and form fields. Matches the `text-input` styling for visual consistency.

**`search-bar`** — A full-rounded pill-shaped search input used in the nav bar and on search results pages. Uses a white background with a 1px {colors.hairline} border and 48px height. On focus, the border switches to {colors.primary}.

### Badges & Tags
**`product-card-badge`** — Sale and discount badges positioned absolutely on product card images. Uses {colors.badge-sale} background with white text, {rounded.xs} corners, and uppercase {typography.badge} font.

**`product-card-badge-new`** — New-arrival badges using a green-on-light-green scheme. Background is {colors.badge-new-bg} (#e0faef), text is {colors.badge-new} (#13a165).

**`filter-chip`** — Interactive filter tags on category pages. Uses a soft gray background with a 1px {colors.hairline} border and full-rounded corners. Active chips switch to {colors.primary} background with white text.

### Other Components
**`hero-banner`** — Full-width promotional banners on the homepage and campaign pages. Primary variant uses {colors.primary} background with white text and {typography.display-xl}. An alternate variant uses {colors.accent-rose} (#e0b5b2) background with {colors.ink} text for softer, more lifestyle-oriented messaging.

**`footer`** — Site-wide footer with a dark background ({colors.ink}) and light text ({colors.canvas}). Links use {colors.hairline} for readability against the dark background. Organized into columns for customer service, company info, and social links.

**`accordion-header`** / **`accordion-content`** — Used for FAQ sections and product description expandable sections. Headers use {typography.title-sm} with a bottom border. Content uses {typography.body-sm} with padding.

**`pagination-button`** — Page navigation buttons on collection and search results pages. Uses a white background with a 1px {colors.hairline} border. Active page uses {colors.primary} background.

**`quantity-selector`** — A compact input for adjusting product quantities on the product page and cart. Uses a white background with a 1px {colors.hairline} border and 40px height.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero banner reduces to 300px min-height; filter chips wrap to two rows; footer stacks vertically; search bar moves to full-width below nav |
| Tablet | 744–1128px | Nav bar shows top-level links only; product cards display in 2-column grid; hero banner uses 350px min-height; filter chips show in a horizontal scrollable strip; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav bar with dropdowns; product cards in 3-column grid; hero banner at 400px min-height; filter sidebar visible on collection pages; footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero banner content centered with max-width; all components scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44x44px touch target (WCAG AAA)
- Nav bar links have 48px tap height
- Filter chips have 36px minimum tap height with 8px gap between chips
- Quantity selector buttons are 40x40px
- Product card images are tappable with no minimum size requirement (image fills card)

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px, with a full-screen overlay menu
- Product filters collapse to a "Filter" button that opens a slide-in panel on mobile
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections
- Breadcrumbs truncate on mobile, showing only the current page and a "Back" link
- Hero banner text and CTAs stack vertically on mobile, with reduced padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from the static HTML/CSS analysis; the values above are inferred from common patterns and should be validated against the live site's CSS
- Error styling for form inputs (error messages, validation icons) was not observed in the extracted data
- Dark mode is not present on the live site and has not been designed
- The extracted font list includes "object-fit: contain" which is a CSS property, not a font family; the actual font stack may include additional fallbacks not captured
- Shopify checkout styling (Shopify Pay button, cart drawer, checkout form) inherits Shopify's default theme and is not part of Silverts' custom design system
- The extracted color list includes several likely Shopify widget colors (#008060, #108474 for Shopify Pay; #fbcd0a for star ratings; #2c6ecb for link defaults) that should be verified against the brand's actual design tokens
- Sub-brand or seasonal color palettes (e.g., holiday promotions, clearance events) were not captured
- Animation and transition timing values (ease-in-out durations, hover transitions) were not extractable from the static analysis
- The exact AGaramondPro font weight variants used (regular, semibold, bold) could not be determined; the weights above are best estimates based on typical usage
