---
version: alpha
name: "Oldies.com"
source_url: "https://www.oldies.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-catalog nostalgia marketplace where the primary voltage is a dusty rose #e0b4b4 — not a soft pink, but the color of a faded concert tee washed a hundred times, carried through every secondary badge, sale tag, and category-chip background. The brand's true anchor is #9f3a38, a dried-cranberry red that powers primary CTAs, the top nav's active state, and the "Add to Cart" button, while #db2828 (a sharper stop-sign red) punctuates sale percentages and clearance flags. The canvas is #fff6f6, a barely-there blush tint that keeps the white from feeling sterile — a warm, papery backdrop for product grids. Typography runs Lato at 400/700 for body and Arial Black at 900 for display headlines, a pairing that reads as utilitarian but earnest: the Arial Black weight gives category headers ("DVDs", "Vinyl", "Blu-ray") a loud, poster-shop confidence, while Lato body copy at 14–16px keeps product descriptions legible and unpretentious. Search bars and filter chips use {rounded.sm} (8px) — not pill-shaped, not sharp — a middle ground that says "we're not fancy, but we're not sloppy." Product cards sit on {surface-card} (#ffffff) with a soft {hairline} (#eeeeee) border, and the footer is a dense, link-heavy column grid in #555555 on #f7f7f7, the kind of information-dense bottom that signals "we've been doing this since 1995." The overall mood is a record store's website from 2005 that has been gently modernized — the reds are louder than contemporary DTC convention, the type is heavier, and the blush canvas is the one genuinely unexpected design choice.

colors:
  primary: "#9f3a38"
  primary-active: "#7a2b2a"
  primary-disabled: "#e7bdbc"
  ink: "#1b1c1d"
  body: "#555555"
  muted: "#767676"
  muted-soft: "#c0c1c2"
  hairline: "#eeeeee"
  hairline-soft: "#f3f4f5"
  canvas: "#fff6f6"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#e0b4b4"
  accent-rose-soft: "#da9796"
  accent-sale: "#db2828"
  accent-blue: "#1e70bf"
  accent-blue-soft: "#85b7d9"
  accent-green: "#21ba45"
  accent-green-soft: "#a8ff16"
  link-blue: "#4183c4"
  link-blue-hover: "#3875d7"
  badge-new: "#2185d0"
  badge-sale: "#cc0000"
  star-rating: "#003399"
  footer-text: "#555555"
  footer-bg: "#f7f7f7"

typography:
  display-xl:
    fontFamily: "'Arial Black', 'Arial Black', Gadget, sans-serif"
    fontSize: 32px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Arial Black', Gadget, sans-serif"
    fontSize: 26px
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Arial Black', Gadget, sans-serif"
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "Lato, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-sale}"

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.accent-rose-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 4px 0
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  category-chip:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-sale}"
  badge-new:
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
  badge-free-shipping:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
    minHeight: 300px
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
  filter-option:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  filter-option-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-section-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in dried-cranberry {colors.primary} (#9f3a38) with white text and 8px rounded corners. On hover, it deepens to {colors.primary-active} (#7a2b2a). The disabled state fades to {colors.primary-disabled} (#e7bdbc) with muted text, signaling the button is inert without removing it from layout. Used for "Add to Cart", "Checkout", and "Sign Up" actions.

**`button-secondary`** — An outlined variant with a white background, {colors.primary} text, and a 2px solid border in the same red. On hover, the background fills with {colors.accent-rose-soft} (#da9796) for a subtle warmth. Used for "View Details", "Wishlist", and secondary checkout flows.

**`button-sale`** — A compact, urgent button in {colors.accent-sale} (#db2828) with white text and smaller padding. Used exclusively for clearance pricing actions, "Shop Sale", and limited-time offers. The bright red creates visual hierarchy against the deeper primary red.

**`button-link`** — A text-only button styled as a blue link ({colors.link-blue} #4183c4), matching the site's anchor styling. No background or border. Used for "Learn More", "See All", and inline navigation within product descriptions.

### Cards
**`product-card`** — A white card on {colors.surface-card} (#ffffff) with a 1px {colors.hairline} (#eeeeee) border and 8px rounded corners. Contains product image, title in {typography.title-sm} (#1b1c1d), price in {typography.price} (#1b1c1d), and optional sale price in {colors.accent-sale}. On hover, the border shifts to {colors.primary} and a subtle box shadow appears. Padding is 12px on all sides.

**`product-card-sale-price`** — The sale price variant uses {colors.accent-sale} (#db2828) to draw immediate attention to discounts. Always paired with a strikethrough original price in {colors.muted} (#767676).

### Navigation
**`top-nav`** — A 64px-high bar on {colors.canvas} (#fff6f6) with a 1px bottom border in {colors.hairline}. Navigation links use {typography.nav-link} (Lato 700, 15px) in {colors.ink} (#1b1c1d). The active state inverts to {colors.primary} background with white text, used for the current category page. The nav includes dropdown menus for media format (DVD, Blu-ray, Vinyl, CD) and a search bar.

**`search-bar`** — A 44px-high input on white background with 8px rounded corners and a 1px {colors.hairline} border. On focus, the border thickens to 2px and turns {colors.primary}. Placeholder text uses {colors.muted-soft} (#c0c1c2). The search icon sits at the left edge in {colors.muted}.

### Badges
**`badge-new`** — A compact label in {colors.badge-new} (#2185d0) with white uppercase text at 11px/700. Used to flag newly added inventory. 4px rounded corners and 2px/8px padding.

**`badge-sale`** — A high-contrast label in {colors.badge-sale} (#cc0000) — a slightly cooler red than {colors.accent-sale} — with white text. Used for percentage-off badges and clearance tags.

**`badge-free-shipping`** — A green badge in {colors.accent-green} (#21ba45) signaling free shipping eligibility. Appears on product cards and category filter results.

### Filters & Categories
**`category-chip`** — A pill-like chip in {colors.accent-rose} (#e0b4b4) with {colors.primary} text, 8px rounded corners, and 6px/14px padding. Used for genre and format filters (e.g., "Rock", "Jazz", "Blu-ray"). The active state fills with {colors.primary} and white text.

**`filter-option`** — A white bordered box for multi-select filters (price range, format, decade). Active state fills with {colors.primary} and white text. 8px rounded corners.

### Footer
**`footer-link`** — Standard link in {colors.footer-text} (#555555) on {colors.footer-bg} (#f7f7f7). On hover, turns {colors.primary}. The footer is a dense, multi-column layout with section titles in {typography.title-sm} and links for customer service, account, and media categories.

### Pagination
**`pagination-button`** — A white bordered square (8px rounded) for page numbers. The active page uses {colors.primary} background with white text. Previous/Next arrows use the same styling with icon-only content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger nav replaces top-nav, category chips stack vertically, search bar collapses to icon-only, footer links collapse into accordion, hero banner reduces to 200px min-height |
| Tablet | 744–1128px | Two-column product grid, top-nav shows 4-5 primary links with "More" dropdown, category chips wrap to 2 rows, search bar remains full-width, footer shows 3 columns |
| Desktop | 1128–1440px | Three-column product grid, full top-nav with all categories visible, category chips in single horizontal scrollable row, search bar with autocomplete dropdown, footer shows 5 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, additional whitespace on sides, hero banner expands to 400px min-height with background image |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain minimum 44x44px tap target
- Product card CTAs are at least 44px tall
- Category chips are 32px tall with 14px horizontal padding for comfortable tapping
- Mobile hamburger menu icon is 48x48px
- Filter checkboxes are 24x24px with 12px touch padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces columns from 4 to 1 on mobile
- Category filter strip collapses to a single "Filters" button that opens a modal
- Footer link groups collapse to accordion panels on mobile
- Hero banner text reduces from display-lg to display-md on mobile
- Search bar collapses to a search icon that expands on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only for product cards and footer links; button hover states inferred from primary-active color. No data on dropdown hover or submenu behavior.
- **Error styling**: No form validation states (error borders, error messages) could be extracted from the live site.
- **Loading states**: No skeleton screens, spinners, or loading animations were observed.
- **Dark mode**: The site does not appear to support dark mode; no dark palette tokens exist.
- **Sub-brand palettes**: The site may have seasonal or promotional color schemes (e.g., holiday sales) that were not captured.
- **Typography scale**: Font sizes for display-xl through caption were inferred from common patterns on the site; exact values may vary across pages. The Arial Black usage at 900 weight is confirmed in category headers but may not be used for all display text.
- **Component spacing**: Padding and height values for components are best estimates based on visual inspection; exact pixel values may differ in production CSS.
- **Iconography**: No custom icon set was extracted; the site appears to use standard UI icons (search, cart, hamburger) in {colors.muted} (#767676).
- **Checkout flow**: The extracted colors included several Shopify-adjacent blues and greens (#1e70bf, #21ba45) that may belong to payment widgets rather than the brand itself. These have been noted as accent tokens but may not be core brand colors.
- **Animation**: No transition durations, easing functions, or animation keyframes were extracted. The site appears to use minimal animation (simple hover color shifts).
