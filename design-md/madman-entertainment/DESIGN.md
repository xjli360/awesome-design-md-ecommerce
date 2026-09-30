---
version: alpha
name: "Madman Entertainment"
source_url: "https://www.madman.com.au"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep crimson #ff3333 pulses through the Madman Entertainment interface like a heartbeat, marking every primary action, badge, and category accent against a stark white #ffffff canvas. The palette reads like a collector's shelf — alongside the signature red sit a muted sage #7bdcb5, a warm amber #fcb900, and a slate gray #abb8c3 that together suggest the breadth of anime, cult cinema, and independent film the brand curates. The extracted colors are unusually varied for a single-brand site, likely reflecting a content-driven system where product packaging, film posters, and genre tags introduce their own chromatic identities; the brand trusts its visual content over rigid color architecture. Navigation is lean and utilitarian — a horizontal bar with dropdown menus for Shop, Genres, and Releases — while product cards stack in clean grids with the Madman red reserved for price tags, "Pre-order" flags, and "New Release" badges. The overall mood is that of a passionate specialty retailer: the red is loud enough to signal urgency but tempered by generous whitespace and a neutral body text in #0d0d0d that keeps the focus on cover art and synopses. No font-family declarations were found on the live site, so the system defaults to a sans-serif stack that reads cleanly across product listings and film descriptions.

colors:
  primary: "#ff3333"
  primary-active: "#cf2e2e"
  primary-disabled: "#f78da7"
  ink: "#0d0d0d"
  body: "#333333"
  muted: "#a2a2a2"
  muted-soft: "#abb8c3"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#7bdcb5"
  accent-amber: "#fcb900"
  accent-blue: "#0693e3"
  accent-purple: "#9b51e0"
  accent-orange: "#ff6900"
  badge-new: "#ff3333"
  badge-preorder: "#ff6900"
  badge-sale: "#00d084"
  star-rating: "#fcb900"
  footer-bg: "#0d0d0d"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-dropdown-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  nav-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.button-md}"
    color: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.footer-text}"
  footer-link-hover:
    color: "{colors.primary}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  breadcrumb-link:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link-active:
    color: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Madman red #ff3333 with white text and a subtle 8px corner radius. On hover and active states, the red deepens to #cf2e2e, providing clear tactile feedback. The disabled state softens to a pale pink #f78da7, signaling non-interactivity without visual noise. Used for "Add to Cart", "Pre-order Now", and "Subscribe" actions.

**`button-secondary`** — An outlined alternative for less prominent actions like "View Details" or "Cancel". The button carries a 1px hairline border on a white background, switching to a solid ink border on hover. Padding is intentionally 1px less than the primary button to account for the border, maintaining consistent 44px height.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Clear Filters" or "See All". Hover state adds a subtle background tint via the surface-soft color, but the component definition relies on the parent context for hover styling.

### Cards
**`product-card`** — The core content container for film and TV titles, built as a white card with a soft 8px radius and no internal padding at the root level. The image area takes a top-rounded shape via `product-card-image`, while the title and price sit below with their own padding tokens. Badges overlay the image area at the top-left corner, using the `product-card-badge` variants to indicate New Release (red), Pre-order (orange), or Sale (green) status.

### Navigation
**`nav-bar`** — A fixed-height 64px horizontal bar with a white background and a subtle bottom hairline. Navigation links use the `nav-link` typography at 14px weight 600 with 0.3px letter spacing. The bar supports dropdown menus via `nav-dropdown`, which appear on hover with a white background, soft shadow, and 8px radius. Dropdown items are 44px tall with 8px vertical padding and 16px horizontal padding, highlighting to surface-soft on hover.

### Forms
**`text-input`** — Standard text entry fields for search, login, and checkout forms. The default state shows a 1px hairline border with 12px internal padding and a 48px height. On focus, the border thickens to 2px and switches to Madman red, creating a clear active indicator. Error states also use a 2px red border, paired with an error message in the caption typography.

### Search
**`search-bar`** — A pill-shaped search input with a 44px height, placed in the nav bar or as a standalone component. The default state has a soft gray background with a 1px hairline border; on focus, the background turns white and the border becomes a 2px red ring. The full rounded shape (`{rounded.full}`) gives it a friendly, approachable feel.

### Footer
**`footer`** — A dark inversion of the main interface, with a near-black background (#0d0d0d) and white text. Links are white by default and shift to Madman red on hover, providing a clear interactive signal against the dark canvas. The footer uses 64px vertical padding and contains columns for customer service, about links, and social media icons.

### Filters
**`filter-chip`** — Used in category and genre filter strips, these pill-shaped buttons toggle between an outlined default state and a filled red active state. The 8px horizontal padding and 8px vertical padding create a compact 32px-tall chip that stacks well in horizontal scrollable rows.

### Pagination
**`pagination-button`** — Numbered page buttons with a 1px hairline border and 8px corner radius. The active page fills with Madman red, while inactive pages remain white. Buttons are 32px × 32px minimum, ensuring comfortable touch targets.

### Quantity Selector
**`quantity-selector`** — A compact input for adjusting cart quantities, styled with a 1px hairline border and 44px height. The component typically includes minus and plus buttons flanking the numeric value, all within the same bordered container.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner reduces to 48px padding; filter chips stack vertically; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav bar shows top-level links only (dropdowns require tap); hero banner maintains 64px padding; filter chips scroll horizontally |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns on hover; hero banner at full 64px padding; filter chips in a horizontal strip |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; all other desktop patterns scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain a minimum 44px × 44px touch target
- Product card images are tappable as a single unit, linking to the product detail page
- Filter chips are 32px tall with 16px horizontal padding, meeting the 44px minimum height requirement
- Nav bar dropdown items are 44px tall with 16px horizontal padding
- Pagination buttons are 32px × 32px minimum, with 44px spacing between buttons

### Collapsing Strategy
- Primary nav collapses to a hamburger icon at < 744px, revealing a full-screen overlay menu
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows
- Filter chip strip switches from horizontal scroll to vertical stack at < 744px
- Hero banner reduces vertical padding from 64px to 48px at < 744px
- Footer columns stack vertically at < 744px, with each column taking full width
- Search bar moves from the nav bar to a dedicated full-width row below the nav at < 744px
- Breadcrumb trail truncates at < 744px, showing only the current page and a "Back" link

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site; the typography block uses a standard sans-serif stack as a fallback. A custom typeface may be loaded via JavaScript or a third-party service not captured in the extraction.
- Hover and focus states for most components could not be reliably extracted; the active/disabled variants defined above are best estimates based on common patterns.
- Error styling for forms (error messages, validation icons) was not observed on the live site.
- Sub-brand or category-specific color palettes (e.g., anime vs. independent film) could not be determined.
- Dark mode support is not evident from the extracted data.
- The extracted color list includes 18 hex values, many of which appear to be from third-party widgets (payment buttons, social icons) rather than the brand's core palette. The primary red #ff3333 is the most distinctive and frequently occurring brand color.
- Spacing and sizing values are inferred from common e-commerce patterns rather than directly extracted from the live site.
- Animation and transition durations (e.g., button hover, dropdown reveal) were not captured.
- The checkout flow and cart drawer styling were not accessible during extraction.
