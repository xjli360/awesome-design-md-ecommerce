---
version: alpha
name: "MK Professional"
source_url: "https://mkprofessional.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A sophisticated, professional-grade haircare brand that speaks to stylists and discerning consumers through a palette of warm neutrals and deliberate accents. The system rests on a canvas of {colors.canvas} (#faf9f7), a soft off-white that feels warmer and more tactile than pure white, paired with a secondary surface of {colors.surface-soft} (#e9e9e9) that creates gentle depth without harsh contrast. The brand's primary voltage comes from {colors.primary} (#d77e6a), a dusty terracotta-rose that appears in key CTAs and accent elements, supported by {colors.primary-active} (#e2a192) for hover states — a lighter, more airy version that keeps interactions feeling soft rather than aggressive. Typography relies on Lato and Outfit, two clean geometric sans-serifs that balance professionalism with approachability; Lato carries body copy at {typography.body-md.fontSize} with generous {typography.body-md.lineHeight} leading, while Outfit handles display sizes with a slightly more modern, condensed feel. The system uses {rounded.sm} (8px) for buttons and inputs, {rounded.md} (12px) for cards, and {rounded.full} for pill-shaped search bars and badges, creating a friendly but not overly playful interface. A secondary blue accent of {colors.accent-blue} (#1990c6) appears in links and informational badges, providing a cool counterpoint to the warm primary palette. The overall mood is elevated yet approachable — think salon reception area rather than clinical lab — with generous whitespace, soft hairlines of {colors.hairline} (#dedede), and a muted text hierarchy that uses {colors.ink} (#121212) for headlines, {colors.body} (#53575a) for body copy, and {colors.muted} (#9b9b9b) for secondary information. The brand's Shopify foundation means components are built for e-commerce conversion: prominent product cards with clear pricing, sticky navigation with search, and trust signals like ratings and badges rendered in the system's warm accent palette.

colors:
  primary: "#d77e6a"
  primary-active: "#e2a192"
  primary-disabled: "#f0d0c8"
  accent-blue: "#1990c6"
  accent-blue-active: "#136f99"
  ink: "#121212"
  body: "#53575a"
  muted: "#9b9b9b"
  muted-soft: "#c6c6c6"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#faf9f7"
  surface-soft: "#e9e9e9"
  surface-card: "#ffffff"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  star-rating: "#d77e6a"
  badge-new: "#d77e6a"
  badge-sale: "#53575a"
  error: "#c13515"
  success: "#2e7d32"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Outfit', 'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Outfit', 'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Outfit', 'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Outfit', 'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    objectFit: "contain"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-rating:
    typography: "{typography.caption}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.sm}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 44px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  rating-stars-small:
    color: "{colors.star-rating}"
    size: 12px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  cart-icon:
    textColor: "{colors.ink}"
    size: 24px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in {colors.primary} (#d77e6a) with white text and {rounded.sm} corners. On hover, it shifts to {colors.primary-active} (#e2a192) for a lighter, airier feel. The disabled state uses {colors.primary-disabled} (#f0d0c8) to visually communicate inactivity while maintaining brand consistency. **`button-secondary`** — An outlined variant with a white background, {colors.ink} text, and a {colors.hairline} border. Active state darkens the border to {colors.ink} and adds a subtle {colors.surface-soft} background. **`button-tertiary-text`** — A text-only button in {colors.primary} for less prominent actions like "View details" links. **`button-pill-primary`** and **`button-pill-outline`** — Fully rounded pill buttons used for filters, tags, and secondary CTAs, with the outline variant featuring a hairline border.

### Cards
**`product-card`** — The core product display component, a white card with {rounded.md} corners containing an image, title, price, and optional rating. The image uses `object-fit: contain` to preserve product photography proportions. A **`product-card-badge`** overlays the top-left corner in {colors.primary} for "New" or "Featured" labels, while **`product-card-sale-badge`** uses {colors.badge-sale} for discount indicators. Cards stack in responsive grids with {spacing.base} gaps between them.

### Navigation
**`top-nav`** — A fixed-position header at 72px height with a white background and a subtle bottom border in {colors.hairline-soft}. Navigation links use {typography.nav-link} at 15px weight 500, with active and hover states transitioning to {colors.primary}. The **`cart-icon`** sits at the right with a **`cart-count-badge`** — a small pill in {colors.primary} showing the item count. **`search-bar`** uses {rounded.full} with a hairline border that switches to {colors.primary} on focus.

### Forms
**`text-input`** — Standard input fields at 44px height with {rounded.sm} corners and a {colors.hairline} border. Active state highlights the border in {colors.primary}, while error state uses {colors.error} (#c13515). **`select-input`** follows the same styling for dropdown menus. **`textarea`** extends the input pattern for multi-line content like review forms. **`quantity-selector`** combines a text input with increment/decrement buttons in {colors.surface-soft} for cart quantity adjustments.

### Footer
**`footer`** — A dark section using {colors.ink} (#121212) background with white text for maximum contrast. Links render in {colors.muted-soft} (#c6c6c6) and lighten to {colors.canvas} on hover. The footer contains brand information, navigation links, and social icons arranged in a multi-column layout that collapses to single column on mobile.

### Badges & Tags
**`badge-new`** and **`badge-sale`** — Pill-shaped badges in {rounded.full} using uppercase {typography.badge} at 11px weight 700. The "New" badge uses {colors.primary} while "Sale" uses {colors.badge-sale} for visual distinction. **`rating-stars`** render in {colors.star-rating} (#d77e6a) at 16px for product cards and 12px for compact views.

### Accordion
**`accordion`** — Collapsible sections with a white background and bottom border separation. Headers are clickable with padding on all sides, and content panels slide open with smooth transitions. Used for product descriptions, FAQ sections, and filter panels.

### Breadcrumbs & Pagination
**`breadcrumb`** — Navigation trails in {colors.muted} with {colors.muted-soft} separators, with the active page in {colors.ink}. **`pagination`** — Page number links in {colors.body} with the active page highlighted in {colors.primary} with {rounded.sm} corners and white text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav links, footer collapses to stacked layout, hero banner reduces padding to {spacing.xl}, search bar collapses to icon-only, product cards use full width |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links with "More" dropdown, footer uses two-column layout, hero banner uses {spacing.xxl} padding |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, footer uses four-column layout, hero banner at full {spacing.section} padding |
| Wide | > 1440px | Max-width container at 1440px with centered content, four-column product grid, all components at maximum spacing |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons use 40px × 40px touch targets
- Quantity selector buttons are 44px × 44px
- Product card CTAs are minimum 44px tall
- Search bar maintains 48px height across all breakpoints
- Navigation links have minimum 44px tap areas

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces columns from 4 → 3 → 2 → 1 as viewport narrows
- Footer columns collapse from 4 → 2 → 1
- Hero banner reduces padding and font size on mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay
- Product card badges stack vertically on narrow screens
- Accordion panels remain collapsed by default on mobile for space efficiency

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text links could not be fully extracted — assumed standard opacity transitions
- Error state styling for forms (beyond border color) is inferred from common e-commerce patterns
- Focus ring styles (outline, offset, color) were not present in extracted CSS
- Dark mode color overrides are not defined — the brand appears to use light mode exclusively
- Sub-brand or collection-specific color palettes (e.g., "MK Pro Color", "MK Repair") may exist but were not detected
- Loading states (skeleton screens, spinners) were not found in the extracted data
- Dropdown menu styling for navigation and filters is assumed based on common patterns
- Tooltip and popover styling is not present in the extracted CSS
- Animation timing and easing curves were not extracted
- Print stylesheet overrides are not defined
- Accessibility focus indicators beyond basic outline are not confirmed
- The exact font weights for Lato and Outfit beyond 400, 500, 600, 700 are assumed based on common availability
- Letter-spacing values for body text are assumed at 0 unless otherwise specified in extracted data
- The `object-fit: contain` declaration was found but its application context is inferred for product images
