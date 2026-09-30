---
version: alpha
name: "Zia Records"
source_url: "https://www.ziarecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep indigo anchor at #222299 — not a friendly blue but a midnight cobalt that reads as serious, archival, and slightly mysterious, the color of a record-store crate in shadow. Paired with a secondary navy #223355 and a near-white canvas #eeeeee, the palette strips away warmth to let album art and movie posters supply all the color. The brand name itself, Zia Records, appears in a bold, condensed sans-serif that feels lifted from a 1970s marquee — no softening, no decorative descenders. Navigation is a dense, information-rich strip: genre dropdowns, format filters (Vinyl / CD / Cassette / Blu-ray), and a search bar that feels more like a database query than a friendly prompt. Product cards stack tightly with minimal whitespace, favoring thumbnail density over breathing room — this is a store for collectors who scan, not browsers who linger. The checkout flow, likely powered by a third-party widget, introduces a sudden shift to generic blues and grays, a known gap between the brand's distinctive identity and the transactional layer. But within the catalog, the design language is consistent: sharp corners ({rounded.none} on cards), high-contrast text on dark backgrounds, and a typographic hierarchy that prioritizes artist name and format badge over price. It feels less like a lifestyle brand and more like a well-organized archive — the digital equivalent of a shop where the owner knows exactly where every used copy of *Bitches Brew* is shelved.

colors:
  primary: "#222299"
  primary-active: "#1a1a7a"
  primary-disabled: "#8888bb"
  ink: "#111111"
  body: "#222222"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#223355"
  badge-vinyl: "#222299"
  badge-cd: "#223355"
  badge-cassette: "#555555"
  badge-bluray: "#111111"
  sale-red: "#cc3333"
  star-rating: "#222299"

typography:
  display-xl:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Font Awesome 5 Free', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 30px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
  product-card-image:
    rounded: "{rounded.none}"
    height: 200px
  format-badge:
    backgroundColor: "{colors.badge-vinyl}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  format-badge-cd:
    backgroundColor: "{colors.badge-cd}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  format-badge-cassette:
    backgroundColor: "{colors.badge-cassette}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  format-badge-bluray:
    backgroundColor: "{colors.badge-bluray}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
    borderColor: "{colors.hairline}"
  search-bar-focus:
    borderColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    height: 300px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  sale-price:
    typography: "{typography.title-md}"
    textColor: "{colors.sale-red}"
  original-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  rating-stars:
    color: "{colors.star-rating}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary action button, filled with the deep indigo `{colors.primary}` (#222299) and white text. Used for add-to-cart, checkout initiation, and primary form submissions. On hover, shifts to `{colors.primary-active}` (#1a1a7a). Disabled state uses `{colors.primary-disabled}` (#8888bb). Height is 40px with `{rounded.sm}` corners — compact enough for dense product listings.
**`button-secondary`** — An outlined or light-filled alternative, using `{colors.canvas}` (#eeeeee) background with `{colors.ink}` (#111111) text. Used for secondary actions like "View Details" or "Add to Wishlist." Maintains the same 40px height and `{rounded.sm}` as the primary button for visual consistency.
**`button-sale`** — A compact, high-contrast button for sale items, using `{colors.sale-red}` (#cc3333) background. Height is 30px with smaller typography `{typography.button-sm}`, designed to sit alongside price displays without overwhelming the product card.

### Cards
**`product-card`** — The core catalog unit: a white `{colors.surface-card}` background with zero rounding (`{rounded.none}`), creating a sharp, grid-aligned appearance. Contains a product image (200px tall, also sharp-cornered), format badge, artist name, album title, and price. On hover, the background shifts to `{colors.surface-soft}` (#f5f5f5). No shadow or elevation — the card relies on the contrast between white and the `{colors.canvas}` (#eeeeee) page background for separation.
**`format-badge`** — A small uppercase label identifying the media format (Vinyl, CD, Cassette, Blu-ray). Each format has a distinct background color: `{colors.badge-vinyl}` (#222299) for vinyl, `{colors.badge-cd}` (#223355) for CD, `{colors.badge-cassette}` (#555555) for cassette, and `{colors.badge-bluray}` (#111111) for Blu-ray. Badges use `{rounded.xs}` (2px) for a subtle but present corner.

### Navigation
**`nav-bar`** — A 56px-tall bar filled with `{colors.primary}` (#222299), containing the brand logo on the left and navigation links in white. Links use `{typography.nav-link}` (14px, weight 600). The bar is fixed or sticky at the top, providing persistent access to genre dropdowns and search.
**`nav-dropdown`** — A dropdown menu that appears on hover or click of a nav link. Uses `{colors.canvas}` (#eeeeee) background with `{colors.ink}` (#111111) text, `{rounded.sm}` corners, and a subtle shadow for depth. Contains genre listings, format filters, and subcategories.
**`category-strip`** — A horizontal scrollable strip below the nav bar, listing product categories (e.g., "New Arrivals", "Vinyl", "CD", "Movies"). Inactive tabs use transparent background with `{colors.body}` text; active tabs use `{colors.primary}` background with white text and `{rounded.sm}`.

### Forms
**`text-input`** — A standard input field with `{colors.canvas}` background, `{colors.body}` text, and a `{colors.hairline}` (#cccccc) border. Height is 40px with `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}` (#222299). Used for search queries, account forms, and checkout fields.
**`search-bar`** — A dedicated search input, slightly taller at 44px with 16px horizontal padding. Shares the same visual language as `text-input` but is typically placed prominently in the nav bar or hero area. Focus state uses `{colors.primary}` border.

### Footer
**`footer`** — A dark footer with `{colors.ink}` (#111111) background and `{colors.muted-soft}` (#888888) text. Contains links to store policies, contact information, and social media icons. Links use `{typography.link}` (13px, weight 400) and match the muted-soft color. The footer is dense with information, reflecting the brand's archival nature.

### Hero
**`hero-banner`** — A full-width banner at the top of the homepage, using `{colors.primary}` (#222299) background with white text. Height is 300px, featuring a large headline in `{typography.display-lg}` (28px, weight 700). May include a promotional message, featured release, or seasonal callout. No background image — the solid indigo is the canvas.

### Pagination
**`pagination`** — A row of page-number buttons at the bottom of search results or category listings. Inactive buttons use `{colors.canvas}` background with `{colors.body}` text and `{rounded.sm}`. The active page button uses `{colors.primary}` background with white text. Buttons are compact (32px x 32px) to fit within the dense grid layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero banner height reduces to 200px; category strip becomes a horizontal scroll; search bar moves below nav; format badges stack vertically on cards |
| Tablet | 744–1128px | Nav bar shows limited links (Logo, Search, Cart, Menu); product cards display in 2-3 columns; hero banner at 250px; category strip remains horizontal but with fewer visible tabs |
| Desktop | 1128–1440px | Full nav bar with all genre dropdowns; product cards in 4-5 columns; hero banner at 300px; search bar prominent in nav; category strip fully visible |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 5-6 columns; additional whitespace on sides; hero banner may extend full width with content centered |

### Touch Targets
- All buttons and interactive elements maintain minimum 40px height for touch accessibility
- Nav bar links have 44px touch targets (height + padding)
- Search bar has 44px height for easy tapping
- Category strip tabs have 36px minimum height with 8px padding
- Product card images are tappable with 200px height
- Format badges are small (10px font) but wrapped in a tappable card area

### Collapsing Strategy
- Nav bar collapses to a hamburger menu on mobile, revealing a full-screen overlay with genre links, search, and account options
- Category strip collapses to a single "Categories" dropdown on mobile
- Product card grid collapses from multi-column to single-column on mobile
- Hero banner text reduces in size and may truncate to a single headline on mobile
- Footer links collapse into accordion-style sections on mobile
- Search bar moves from inline in the nav to a dedicated full-width bar below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family declarations extracted were limited to Font Awesome icon fonts and a custom "spruce-icon-pack" — the actual body and heading fonts could not be reliably identified from the extracted data. The typography block uses Font Awesome as a placeholder; the real brand likely uses a different primary typeface.
- Only three hex colors were extracted from the live site (#222299, #223355, #eeeeee). These appear to be the brand's primary palette, but secondary colors (sale red, badge colors, hover states, link colors) were inferred based on common e-commerce patterns and may not match the actual site.
- The extracted colors (#222299, #223355, #eeeeee) form a limited palette of blues and a light gray. While #222299 is distinctive as a deep indigo, the overall palette is narrow. The brand may use additional accent colors (e.g., a warm tone for sales or highlights) that were not captured.
- No meta theme-color was found, suggesting the brand may not have set a browser chrome color.
- The site appears to use a third-party checkout widget (likely Shopify or similar), which introduces generic blues and grays that conflict with the brand's distinctive indigo palette. These checkout colors were excluded from the design system.
- Hover states for buttons and cards were inferred from common patterns; actual hover transitions (duration, easing) could not be extracted.
- Error states for forms (validation colors, error messages) were not observed.
- Dark mode is not supported and was not detected.
- Sub-brand or seasonal color variations (e.g., Record Store Day promotions) were not captured.
- The exact font sizes and line heights in the typography block are estimates based on common e-commerce scales; the actual site may use different values.
- The "spruce-icon-pack" font suggests a custom icon set, but the specific icons and their usage could not be documented.
- The platform-shopify flag is False, indicating the site may use a custom or alternative e-commerce platform, but the checkout flow's visual design remains a gap.
