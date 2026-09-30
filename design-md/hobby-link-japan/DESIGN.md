---
version: alpha
name: "Hobby Link Japan"
source_url: "https://www.hlj.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dense, inventory-first import shop where #0066c8 — a saturated corporate blue pulled straight from a Bandai catalog header — governs every primary action, while #ea345d, a sharp Japanese-flag accent, marks sale badges and urgent notifications against a #f0f0f0 canvas that reads more warehouse than boutique. The site stacks thousands of product SKUs in a tight, monochrome grid of #4d4d4d body text on white cards, with #c5c5c5 hairline borders and #979797 muted labels that keep visual noise low despite the sheer volume of data. Montserrat-Regular at 14–16px drives the reading experience, but the real typographic signature is the 11px uppercase badge — #ea345d on white or #fffa90 on #777620 — that screams "Preorder" or "Sale" in a language every hobbyist understands. Navigation is a two-tier affair: a dark #232323 utility bar for account and cart, then a #0066c8 mega-menu bar that fans out into categories like "Plastic Model Kits" and "Action Figures" with #1e82c0 hover states. The search bar, a full-width #ffffff pill with #d2d2d2 border, sits under the logo like a command line — this is a site built for people who know exactly what they want. Product cards use {rounded.xs} corners, just enough to soften the hard stock-photo edges, and the footer collapses into a #2b2b2b slab with #dad55e links that echo the yellow of Gundam packaging tape. Every design decision defers to the catalog: the blue is the brand's handshake, the pink is the urgent tap on the shoulder, and the gray is the shelf.

colors:
  primary: "#0066c8"
  primary-active: "#1e82c0"
  primary-disabled: "#c2c2c2"
  ink: "#232323"
  body: "#4d4d4d"
  muted: "#979797"
  muted-soft: "#c5c5c5"
  hairline: "#d2d2d2"
  hairline-soft: "#e9e9e9"
  canvas: "#f0f0f0"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#ea345d"
  accent-warning: "#e87613"
  accent-yellow: "#dad55e"
  accent-yellow-bg: "#fffa90"
  accent-yellow-text: "#777620"
  nav-dark: "#232323"
  nav-dark-muted: "#454545"
  footer-bg: "#2b2b2b"
  footer-link: "#dad55e"
  stock-green: "#6cc6c4"
  preorder-purple: "#4d07e6"
  link-blue: "#0da2df"
  scrim: "#11263d"

typography:
  display-xl:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-md:
    fontFamily: "'Montserrat-Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-utility-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 36px
  main-nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 44px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    lineClamp: 2
  product-card-price:
    typography: "{typography.price-md}"
    color: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-md}"
    color: "{colors.accent-sale}"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-preorder:
    backgroundColor: "{colors.preorder-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-warning:
    backgroundColor: "{colors.accent-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-yellow:
    backgroundColor: "{colors.accent-yellow-bg}"
    textColor: "{colors.accent-yellow-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    color: "{colors.footer-link}"
    typography: "{typography.link}"
    hoverColor: "{colors.accent-yellow}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 32px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 36px
  breadcrumb-link:
    color: "{colors.link-blue}"
    typography: "{typography.caption}"
    hoverColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, filled with {colors.primary} blue and white text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to {colors.primary-active} (#1e82c0). Disabled state uses {colors.primary-disabled} (#c2c2c2) with white text, signaling an out-of-stock or invalid action. Height is 40px with {rounded.xs} corners — compact enough to stack in dense product grids.

**`button-secondary`** — Outlined variant with a white fill, {colors.primary} text, and a 1px {colors.primary} border. Used for "View Details", "Wishlist", and secondary actions alongside primary buttons. Hover state fills the background with a 10% opacity blue tint. Disabled state uses {colors.hairline} border and {colors.muted-soft} text.

**`button-sale`** — Compact 32px-high button using {colors.accent-sale} (#ea345d) for urgent actions like "Preorder Now" or "Sale Items". Uses {typography.button-sm} to fit alongside price tags and badges. Hover darkens to #d42b52.

### Badges
**`badge-sale`** — Red (#ea345d) badge with white uppercase text at 11px. Marks discounted items, flash sales, and clearance. Positioned top-left on product card images. Uses {rounded.xs} for a sharp, no-nonsense look.

**`badge-preorder`** — Purple (#4d07e6) badge for upcoming releases. Signals that an item is available for reservation but not yet shipped. Same sizing and typography as sale badge.

**`badge-stock`** — Teal (#6cc6c4) badge indicating "In Stock" or "Available". Used sparingly to highlight items with immediate availability.

**`badge-warning`** — Orange (#e87613) badge for "Low Stock", "Limited Edition", or "Last Chance" messaging. Creates urgency without the alarm of the red sale badge.

**`badge-yellow`** — High-contrast yellow badge (#fffa90 on #777620 text) for "Backorder", "Special Order", or "Price Match" labels. The yellow stands out against the blue-heavy palette and echoes the caution-tape aesthetic of hobby packaging.

### Navigation
**`top-utility-bar`** — A 36px dark strip (#232323) spanning the full viewport. Contains account links, cart icon with item count badge, currency selector, and language toggle. Text is {colors.muted-soft} (#c5c5c5) at {typography.caption} size. Cart count uses {colors.accent-sale} as a dot or pill.

**`main-nav-bar`** — A 44px bar filled with {colors.primary} (#0066c8). Contains top-level category links in uppercase {typography.nav-link} at 13px. Each link has a white chevron indicator for dropdown availability. Hover state uses a lighter blue (#1e82c0) background on the link cell. Active category gets a white underline or bottom border.

**`nav-dropdown`** — White panel with {rounded.xs} and subtle box-shadow. Lists subcategories in {typography.body-md} with 8px vertical padding per item. Hover state uses {colors.surface-soft} (#eeeeee) background. Columns are used for large categories like "Plastic Model Kits" (Gundam, Military, Ships, etc.).

### Product Cards
**`product-card`** — White card with {rounded.xs} corners and 8px padding. Contains a square aspect-ratio image with {rounded.xs}, a two-line title in {typography.title-sm}, and pricing in {typography.price-md}. Sale prices render in {colors.accent-sale}. Badges overlay the top-left of the image. Cards sit in a responsive grid with 8px gap on mobile, 12px on desktop.

**`product-card-image`** — Square container with {rounded.xs}. Uses object-fit: cover for product photography. On hover, may swap to a secondary image or show a quick-add overlay.

### Forms & Search
**`text-input`** — Standard 40px input with white background, {colors.hairline} border, and {rounded.xs}. Focus state uses {colors.primary} border with a 2px width. Placeholder text in {colors.muted-soft}. Error state uses {colors.accent-sale} border.

**`search-bar`** — Full-width pill-shaped input with {rounded.full} and 44px height. White background with {colors.hairline} border. Contains a magnifying glass icon in {colors.muted} on the left. On focus, expands to show recent searches or popular categories in a dropdown panel below.

### Category & Filtering
**`category-chip`** — Pill-shaped filter chip at 32px height. Uses {colors.surface-soft} background and {colors.body} text. Active state fills with {colors.primary} and white text. Used in horizontal scrollable strips for brand, scale, and price-range filtering.

### Pagination
**`pagination-button`** — 36px square-ish button with white background, {colors.hairline} border, and {rounded.xs}. Active page uses {colors.primary} fill. Disabled prev/next arrows use {colors.muted-soft}. Used at the bottom of search results and category pages.

### Footer
**`footer-section`** — Dark slab (#2b2b2b) with {colors.muted-soft} body text. Contains columns for "Help", "Company Info", "Community", and "Follow Us". Links render in {colors.footer-link} (#dad55e) — a warm yellow that provides the only color relief in the dark footer. Hover brightens to #f0e68c. Social icons use their respective brand colors.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns). Top utility bar collapses to icon-only. Main nav becomes hamburger menu. Search bar moves below logo. Category chips scroll horizontally. Footer stacks into single column. |
| Tablet | 744–1128px | Two-column product grid. Top utility bar shows text labels for key items (cart, account). Main nav shows top-level categories with dropdown on tap. Search bar sits beside logo. Category chips show in a 2-row wrap. |
| Desktop | 1128–1440px | Three to four-column product grid. Full top utility bar with all links. Main nav shows all categories. Search bar is prominent in header. Category chips show in a multi-row grid. Footer shows 4-column layout. |
| Wide | > 1440px | Four to five-column product grid. Max-width container (1440px) centers content. Additional whitespace on sides. Category sidebar may appear on left for large screens. |

### Touch Targets
- All buttons and links: minimum 44x44px tap target (buttons already 40px+ with padding).
- Category chips: 32px height with 14px horizontal padding — meets 44px tap target with surrounding spacing.
- Product card tap target: entire card is clickable, minimum 120x120px.
- Nav dropdown items: 36px minimum height with 8px padding.
- Pagination buttons: 36x36px minimum — adjacent spacing ensures 44px effective target.

### Collapsing Strategy
- Top utility bar: collapses to icon-only at < 744px. Cart icon retains count badge. Account icon shows dropdown on tap.
- Main navigation: collapses to hamburger menu at < 744px. Menu slides in from left with full category tree.
- Search bar: collapses from full-width to icon-only at < 744px, expanding to full-width on tap.
- Product grid: reduces columns from 4-5 to 2 on mobile. Single column on very small screens (< 480px).
- Footer: collapses from 4 columns to 1 on mobile. Accordion pattern for each section.
- Category chips: horizontal scroll on mobile, wrap to grid on tablet+.
- Breadcrumbs: truncate with "..." on mobile, showing only current page and parent.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links beyond primary/active are inferred from common patterns — exact opacity values or color transitions not extracted.
- Error states for form inputs (border color, helper text styling) not observed in extraction.
- Focus ring styles (color, width, offset) not present in extracted data — likely uses browser default or {colors.primary} outline.
- Loading states (skeleton screens, spinner colors, pulse animations) not captured.
- Modal/dialog styling (overlay scrim opacity, close button placement, animation) not observed.
- Tooltip and popover styling (background, arrow, delay) not extracted.
- Star rating component (filled vs empty color, size) not present in extracted data.
- Quantity selector (stepper button styling, input width) not observed.
- Image placeholder / broken image styling not captured.
- Dark mode or high-contrast mode not supported — site appears light-mode only.
- Sub-brand or seasonal palette variations (e.g., holiday themes, collaboration-specific colors) not extracted.
- Checkout flow styling (payment form, address entry, order summary) not fully observed — may use third-party iframe.
- Animation timing and easing curves (transitions, hover effects, page loads) not extracted.
- Icon library details (icomoon icons referenced in fonts but specific glyphs not mapped).
- Print stylesheet behavior not observed.
