---
version: alpha
name: "Zia Records"
source_url: "https://www.ziarecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep indigo #222299 — the color of a desert night sky just after dusk — serves as the brand's primary voltage, a deliberate departure from the warm earth tones typical of Southwestern retail. This blue anchors a system built around high-contrast legibility: pure white `{colors.canvas}` backgrounds against dense navy `{colors.ink}` body text, with a secondary navy #223355 used for navigation bars and section headers that feel weighty without being heavy. The palette is intentionally restrained — no accent colors, no gradients, no decorative flourishes — because Zia Records trusts the visual noise of album art, concert posters, and merchandise photography to supply all the color the page needs. Typography runs through Font Awesome icon packs for utilitarian navigation symbols and category badges, while body copy relies on system fonts for maximum readability across the sprawling inventory of used and new vinyl, CDs, and collectibles. The interface reads like a well-organized record bin: clean, browsable, and built for the kind of patient exploration that crate-digging demands. Every button uses `{rounded.sm}` corners — soft enough to feel approachable, square enough to avoid frivolity. Search is the primary interaction pattern, surfaced as a full-width bar with a magnifying-glass icon, reflecting the reality that customers come hunting for specific pressings, artists, or formats. The footer collapses into a dense information grid of store locations, hours, policies, and social links — Zia is a regional chain with six stores, and the site must serve both locals checking in-store inventory and online shoppers browsing the web catalog. The overall mood is utilitarian warmth: no marketing copy, no lifestyle photography, just the raw inventory of a record store that has been doing this since 1980.

colors:
  primary: "#222299"
  primary-active: "#1a1a7a"
  primary-disabled: "#9999cc"
  ink: "#223355"
  body: "#334466"
  muted: "#667788"
  muted-soft: "#99aabb"
  hairline: "#ccccdd"
  hairline-soft: "#ddddee"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#222299"
  link-hover: "#1a1a7a"
  badge-new: "#ff6600"
  badge-sale: "#cc0000"
  star-rating: "#ffcc00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
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
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
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
  caption-strong:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
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
    lineHeight: 1.4
    letterSpacing: 0
  icon-font:
    fontFamily: "'Font Awesome 5 Free', 'Font Awesome 5 Brands', sans-serif"
    fontSize: 16px
    fontWeight: 900
    lineHeight: 1
    letterSpacing: 0

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
    padding: 10px 20px
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
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.icon-font}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 7px 11px
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-item:
    padding: 8px 12px
    rounded: "{rounded.sm}"
  nav-bar-item-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    padding: 7px 11px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 200px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  store-locator-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  store-locator-card-active:
    border: "2px solid {colors.primary}"
  cart-icon:
    typography: "{typography.icon-font}"
    textColor: "{colors.on-dark}"
    height: 36px
    width: 36px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Subscribe." Rendered in the brand's deep indigo `{colors.primary}` with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#1a1a7a) for a subtle darkening. Disabled state uses `{colors.primary-disabled}` (#9999cc) to signal non-interactivity while maintaining brand coherence.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later." Uses a white background with `{colors.primary}` text and a 1px solid border. Active state fills the background with `{colors.surface-soft}` and darkens the border to `{colors.primary-active}`. Provides a lighter visual weight than primary while maintaining the same 40px height and `{rounded.sm}` corners.

**`button-ghost`** — A text-only button for tertiary actions such as "Clear Filters" or "Cancel." No background or border, relying solely on `{colors.primary}` text. Hover state adds a subtle `{colors.surface-soft}` background. Matches the height and corner radius of other button variants for alignment consistency.

**`button-icon`** — Icon-only buttons for utility actions like search toggle, menu toggle, or cart access. Uses Font Awesome glyphs at 16px. Transparent background with `{colors.ink}` text, 36px square dimensions, and `{rounded.sm}` corners. Hover adds a light background tint.

### Navigation
**`nav-bar`** — The primary site navigation, a 56px bar with `{colors.ink}` (#223355) background and white text. Contains store location links, genre/category menus, and utility icons (search, cart). Navigation items use `{rounded.sm}` hover states. Active or current-section items render with `{colors.primary}` background and white text for clear wayfinding.

**`nav-bar-item`** — Individual navigation links with 8px horizontal and 12px vertical padding. Hover state adds a subtle background tint. Active state uses the primary indigo background with white text, creating a pill-like appearance within the nav bar.

### Forms
**`text-input`** — Standard text input for search fields, newsletter signup, and account forms. White background, `{colors.ink}` text, 40px height, and `{rounded.sm}` corners with a `{colors.hairline}` border. Focus state thickens the border to 2px and switches to `{colors.primary}` for clear visual feedback. Error state uses a red border (`{colors.badge-sale}`) without changing the background.

**`select-input`** — Dropdown selectors for filtering by format (vinyl, CD, cassette), condition (new, used), or price range. Matches the `{text-input}` dimensions and styling for visual consistency. Uses native browser dropdown affordances.

**`search-bar`** — The primary search interface, a 44px tall input with a magnifying-glass icon (Font Awesome) on the left. White background with `{colors.hairline}` border and `{rounded.sm}` corners. Focus state mirrors `{text-input-focus}` with a 2px primary border. Positioned prominently in the nav bar and also available as a full-width element on the homepage.

### Cards
**`product-card`** — The core inventory display component, used for vinyl records, CDs, cassettes, and merchandise. A white card with `{rounded.sm}` corners and 12px padding. Contains a 1:1 aspect ratio product image (album art), title, artist name, format badge, price, and condition indicator. Hover state adds a subtle shadow or border highlight. Badges overlay the top-left corner of the image for new arrivals, sale items, or out-of-stock status.

**`store-locator-card`** — Used on the locations page to display individual store information. White background with `{colors.hairline}` border, `{rounded.sm}` corners, and 16px padding. Contains store name, address, phone number, hours, and a "Get Directions" link. Active/selected state uses a 2px `{colors.primary}` border.

### Badges & Chips
**`badge-new`** — Orange (#ff6600) badge for new arrivals, rendered in uppercase 11px bold type with `{rounded.xs}` corners and 2px/6px padding. Positioned as an overlay on product card images.

**`badge-sale`** — Red (#cc0000) badge for sale or clearance items. Same typography and dimensions as `{badge-new}` but with a high-visibility red background to signal discounts.

**`badge-out-of-stock`** — Gray (`{colors.muted-soft}`) badge for unavailable items. Uses the same structure as other badges but with muted colors to de-emphasize the item.

**`filter-chip`** — Pill-shaped filter toggles for browsing by genre, format, or condition. Light gray background (`{colors.surface-soft}`) with `{colors.body}` text, `{rounded.full}` corners, and a `{colors.hairline}` border. Active state fills with `{colors.primary}` and white text.

### Footer
**`footer-section`** — The site footer, a full-width section with `{colors.ink}` background and white text. Contains store information, customer service links, policies, and social media icons. Links render in `{colors.muted-soft}` (#99aabb) and lighten to white on hover. Organized in a multi-column grid with section headers in bold.

### Hero & Sections
**`hero-banner`** — Full-width promotional banner on the homepage, used for featured releases, seasonal sales, or new arrivals. `{colors.ink}` background with white text, large display typography, and generous padding. Minimum height of 200px. May include a background image or pattern overlay.

**`section-header`** — Section dividers for category rows, featured collections, and browse areas. Uses `{typography.display-md}` in `{colors.ink}` with a `{colors.hairline}` bottom border and `{spacing.lg}` vertical padding.

### Pagination
**`pagination-button`** — Page navigation buttons for search results and browse pages. White background with `{colors.ink}` text, `{rounded.sm}` corners, and a `{colors.hairline}` border. Active/current page uses `{colors.primary}` background with white text. Includes previous/next arrows and numbered page links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves below nav; filter chips stack vertically; footer collapses to single column; product cards use full width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with dropdowns for subcategories; search bar remains in nav; filters display as horizontal scrollable row; footer uses two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; search bar in nav with expanded width; filters display as inline chips; footer uses three columns; store locator shows map sidebar |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; additional whitespace on sides; larger hero banner; expanded footer with four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target size on mobile
- Filter chips are 36px tall with 14px horizontal padding, exceeding minimum touch target
- Product card images are tappable, linking to product detail pages
- Nav hamburger menu icon is 44x44px with adequate spacing from other elements
- Cart icon and search icon maintain 44x44px touch targets

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with a slide-out drawer for full navigation
- Secondary navigation (genre/category links) collapses to a select dropdown on mobile
- Product filters collapse to a "Filter" button that opens a modal or bottom sheet
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections
- Store locator map collapses below the store list on mobile, rather than beside it
- Search bar collapses to an icon button on mobile, expanding to full-width when activated

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to three hex values (#222299, #223355, #eeeeee). The secondary navy (#223355) and light gray canvas (#eeeeee) are used as described, but hover states, focus states, error colors, and accent colors (badge-new, badge-sale, star-rating) are inferred from common e-commerce patterns rather than extracted from the live site. A full accessibility audit and color token inventory from the production CSS would be needed to validate these inferred values.
- No font-family declarations were found beyond Font Awesome icon packs. The system font stack used in this design system is a best-guess based on common e-commerce patterns; the actual body and heading fonts may differ. The site may use a custom typeface that was not captured in the extraction.
- Button hover states, focus rings, and active/pressed states are inferred from standard web patterns. The actual implementation may use different transitions, shadows, or color shifts.
- Spacing values (padding, margins, gaps) are estimated based on common grid systems and may not match the production site's exact spacing scale.
- The site's responsive breakpoints are assumed based on common e-commerce patterns (744px, 1128px, 1440px). The actual breakpoints used in production may differ.
- No dark mode styling was detected; the design system assumes light mode only.
- Error states for forms (validation messages, error icons) are not documented as they were not present in the extraction.
- The site may use a Shopify or other e-commerce platform that provides its own component library; this design system documents the brand-specific overrides rather than the full platform UI.
- Animation and transition timings (hover transitions, page loads, modal animations) are not documented as they were not extractable from static HTML/CSS.
- The extracted colors may include checkout-widget colors or social-icon colors that are not part of the core brand palette. The three extracted colors appear to be genuine brand colors, but a full design token audit would confirm this.
