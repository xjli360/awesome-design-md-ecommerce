---
version: alpha
name: "Thames & Kosmos"
source_url: "https://www.thamesandkosmos.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A blue-and-white laboratory of curiosity, where #0044cc acts as the primary voltage — a deep, authoritative blue that appears on every product badge, CTA button, and category header, signaling trust in a space where children build real circuits and chemistry sets. The palette is surprisingly restrained for a toy brand: #e6e6e6 and #fbfbfb form a clean, almost clinical canvas, while #2bbaf4 and #0088cc provide bright accent notes that feel like the glow of a working LED. The brand uses #bd362f sparingly — a single red accent that appears only on "sale" badges and error states, never competing with the blue hierarchy. Type is set in Arial and Helvetica — utilitarian system fonts that prioritize legibility over personality, a deliberate choice that says "this is serious learning, not cartoon entertainment." Product cards use soft rounded corners ({rounded.sm} ~8px), while buttons and badges use tighter radii ({rounded.xs} ~4px), creating a subtle distinction between interactive elements and informational ones. The overall effect is that of a well-organized science textbook come to life — generous whitespace, clear information hierarchy, and a color system that guides the eye from primary action (#0044cc) to secondary information (#444444) to tertiary details (#a2a2a2). The extracted palette includes several generic web blues (#003399, #002a80) that likely represent hover states and link colors, forming a coherent blue family from deep navy to bright cyan.

colors:
  primary: "#0044cc"
  primary-active: "#003399"
  primary-disabled: "#d1e3fb"
  ink: "#222222"
  body: "#444444"
  muted: "#a2a2a2"
  muted-soft: "#bfbfbf"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  canvas: "#fbfbfb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#2bbaf4"
  accent-blue-deep: "#0088cc"
  accent-orange: "#f89406"
  accent-red: "#bd362f"
  accent-green: "#51a351"
  accent-teal: "#2f96b4"
  sale-badge: "#bd362f"
  star-rating: "#fbb450"
  link-default: "#0088cc"
  link-hover: "#0044cc"
  badge-new: "#2bbaf4"
  badge-sale: "#bd362f"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px
  price-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
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
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
  button-icon-square:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 40px
  button-icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price-md}"
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  product-card-new-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
    padding: "{spacing.xs} {spacing.base} {spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 320px
  hero-banner-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 360px
  hero-banner-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} {spacing.lg}"
    minHeight: 280px
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-card-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.primary}"
  category-card-icon:
    color: "{colors.primary}"
    fontSize: 32px
    marginBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
    letterSpacing: 1px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.link-default}"
    textDecoration: none
  breadcrumb-current:
    color: "{colors.body}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    color: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.primary}"
  filter-chip-hover:
    border: "1px solid {colors.primary}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-sm:
    color: "{colors.primary}"
    size: 16px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-count:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "1px 5px"
    minWidth: 18px
    height: 18px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep blue (#0044cc) with white text and tight 4px corner rounding. Used for "Add to Cart," "Shop Now," and primary form submissions. On hover, it shifts to a darker navy (#003399) for clear state feedback. The disabled state uses a pale blue fill (#d1e3fb) with muted text, signaling non-interactivity without visual noise. Height is a compact 40px, appropriate for both desktop and mobile contexts.

**`button-secondary`** — An outlined variant that inverts the primary relationship: white background, blue text, and a 1px solid blue border. Used for "Learn More," "View Details," and secondary actions alongside primary buttons. Active state fills the background with soft gray (#f5f5f5) and darkens the border to navy. The outline maintains the same 40px height and 4px corner radius as the primary button, ensuring visual consistency in button groups.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel," "Clear Filters," or "See All." The text sits in primary blue with 10px horizontal padding. On hover or active, a soft gray background appears to indicate tappability without competing with primary or secondary buttons.

**`button-icon-square`** — A 40x40px square button with a soft gray background, used for icon-only actions like search toggles, cart icons, or menu hamburgers. The icon sits centered in the square with 4px rounding. No border — the background alone defines the hit area.

**`button-icon-circle`** — A fully round 40x40px button filled with primary blue, used for floating actions, scroll-to-top, or promotional call-to-action icons. The circular shape creates visual distinction from the square/rectangular button system, drawing attention to high-priority icon actions.

### Text Inputs & Forms
**`text-input`** — Standard single-line text input with white background, 1px hairline border, and 4px corner rounding. The placeholder text renders in muted gray (#a2a2a2). On focus, the border thickens to 2px and turns primary blue, with the native outline removed. Error state swaps the border to red (#bd362f) while maintaining the same padding and height.

**`select-input`** — Dropdown select element matching the text-input dimensions and styling: 40px height, white background, hairline border, 4px rounding. The down-arrow indicator uses primary blue as its accent color. The dropdown menu itself inherits the same border and rounding when expanded.

**`search-input`** — A slightly taller (44px) input with 8px corner rounding, distinguishing it from standard form inputs. Used in the site header and search results page. The wider rounding and extra height accommodate the search icon and make the input feel more inviting. On focus, the border doubles to 2px primary blue.

### Navigation
**`nav-bar`** — A 64px fixed-height navigation bar with white background and a single 1px hairline bottom border. Navigation links use 14px semibold type with 0.25px letter spacing. The active link state adds a 2px primary blue underline. On scroll, the bar gains a subtle box shadow (0 2px 8px rgba(0,0,0,0.08)) for visual depth against page content.

**`nav-dropdown`** — Flyout menus that appear on hover or click of nav links. White background with 8px corner rounding and a soft box shadow (0 4px 16px rgba(0,0,0,0.12)). Links inside use body-sm typography (14px regular weight) with adequate padding for touch targets. The dropdown sits flush against the nav bar bottom edge with no gap.

**`breadcrumb`** — A horizontal list of navigation links using 12px caption type in muted gray. Each link uses the accent-blue (#0088cc) for unvisited states, while the current page label renders in body gray (#444444). Links are separated by a ">" character in muted gray. No background or border — the breadcrumb floats cleanly above page content.

### Product Cards
**`product-card`** — The core content unit for the product grid, a white card with 8px rounding and a soft hairline border. The card contains a square aspect-ratio image at the top (with top-only rounding), followed by the product title in 14px semibold, the price in 16px bold, and optional star rating in gold (#fbb450). On hover, the card lifts with a subtle box shadow and the border darkens slightly. Badges (New, Sale, or category tags) position at the top-left corner of the image area.

**`product-card-badge`** — A small uppercase label (11px bold, 0.5px letter spacing) with 4px rounding, sitting over the product image. The standard badge uses primary blue fill with white text. Sale badges switch to red (#bd362f), while "New" badges use the bright accent blue (#2bbaf4). Padding is tight (2px vertical, 8px horizontal) to keep the badge compact against the image edge.

### Hero & Category
**`hero-banner`** — A full-width promotional section with soft gray background, 28px bold heading, and generous vertical padding (48px top/bottom). The primary variant uses the deep blue background with white text for high-impact promotions. An accent variant uses the bright blue (#2bbaf4) for secondary campaigns. Minimum heights range from 280px to 360px depending on variant, ensuring consistent visual weight across page sections.

**`category-card`** — A clickable card for browsing product categories, using a white background with 8px rounding and a soft border. Each card contains a 32px primary-blue icon and a 16px bold category name. On hover, the background shifts to soft gray and the border turns primary blue, providing clear interactive feedback. Padding is generous (24px) to accommodate both icon and text comfortably.

### Footer
**`footer`** — A dark section with deep ink (#222222) background and white text, using 14px body type for links and 12px uppercase headings with 1px letter spacing. Links render in a muted light gray (#bfbfbf) and brighten to white on hover. The footer uses the same 48px vertical padding as section spacing, creating visual rhythm with the page content above. No rounding — the footer spans full width with a clean edge.

### Interactive Elements
**`accordion`** — Collapsible content sections with a 14px semibold header and a soft bottom border. The header includes a chevron icon that rotates on expand. Content area uses 14px regular body type in body gray (#444444) with 12px vertical padding. The accordion maintains a clean white background with no rounding, fitting seamlessly into product description pages and FAQ sections.

**`filter-chip`** — A pill-shaped filter toggle with 14px bold type, white background, and a 1px hairline border. Active state fills the chip with primary blue and white text, while hover state changes the border to blue. The pill shape (full rounding) provides a tactile, friendly appearance that contrasts with the square buttons and cards elsewhere in the system.

**`pagination`** — A horizontal row of page numbers using 14px body type. The active page gets a primary blue background with white text in a 4px rounded rectangle. Inactive pages show no background but gain a soft gray fill on hover. The pagination sits centered below product grids and search results, with previous/next arrows flanking the number list.

**`tooltip`** — A small information popup with dark background (#222222), white text, and 4px rounding. Uses 12px caption type with 4px horizontal and 8px vertical padding. The tooltip appears on hover of icons, truncated text, or informational badges, providing context without cluttering the interface.

**`loading-spinner`** — A 24px circular spinner in primary blue, used for asynchronous loading states. A smaller 16px variant appears inside buttons during form submission. The spinner uses a simple rotating arc animation rather than a full circle, keeping the visual footprint minimal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), hamburger nav replaces full nav bar, hero banners stack vertically, filter chips collapse to horizontal scroll strip, footer links stack in single column, search input collapses to icon-only, accordions always expanded |
| Tablet | 744–1128px | Two-column product grid (2 cards), nav bar shows top-level links only, hero banners maintain full width with reduced padding, filter chips show as horizontal scroll, footer uses 2-column grid, search input shows full width |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full nav bar with dropdowns, hero banners at full height, filter chips display in grid layout, footer uses 4-column grid, search input in nav bar with autocomplete dropdown |
| Wide | > 1440px | Four-column product grid (4 cards) on category pages, max-width container (1440px) centers content, hero banners use max-width with centered content, product cards maintain consistent sizing with increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 40px height for touch accessibility
- Icon buttons use 40x40px hit areas regardless of icon size
- Filter chips use 32px minimum height with 14px horizontal padding
- Product card links have 44px minimum tap targets for "Add to Cart" and "View Details"
- Accordion headers provide 44px touch targets for expand/collapse
- Pagination numbers use 36x36px minimum tap areas
- Nav links in mobile hamburger menu use 48px height for easy tapping

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with full-height overlay drawer
- Product filters collapse to a modal or bottom sheet on mobile, with "Apply Filters" primary action
- Product image galleries collapse from thumbnail strip to single-image swipe carousel
- Footer link columns collapse to single-column accordion on mobile
- Category cards collapse from grid to horizontal scroll strip on mobile
- Hero banners reduce from 360px to 240px minimum height on mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay on tap
- Breadcrumb navigation truncates to show only current and parent page on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns rather than extracted from the live site; the extracted palette includes several blue variants (#003399, #002a80) that likely represent hover and active states, but exact mappings are unconfirmed
- Error state styling for forms (red borders, error message typography) is assumed based on the presence of #bd362f in the palette; actual error message placement and animation are unknown
- Dark mode is not present on the live site; no dark mode colors or components are defined
- The extracted font stack is limited to Arial and Helvetica; the brand may use a custom web font for headings that wasn't captured in the extraction
- Button loading states, disabled secondary/ghost variants, and focus-visible ring styles are not documented from the live site
- The extracted palette includes several near-duplicate grays (#e6e5e5, #e1e0e0, #e8e8e8, #d9d9d9) that may represent different surfaces or borders; the system uses the most distinct values but exact mappings are uncertain
- Checkout flow components (cart, payment forms, shipping selectors) were not extracted; Shopify Pay and other widget colors may appear in the palette but are not part of the brand design system
- Animation timing, easing curves, and transition durations are not documented from the live site
- The brand may use a secondary typeface for product names or educational content that wasn't captured in the extraction
- Sub-brand or collection-specific color variations (e.g., "Science Kits" vs "Craft Kits") are not documented
- Print stylesheets and email template designs are outside the scope of this extraction
