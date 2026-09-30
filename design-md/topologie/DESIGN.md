---
version: alpha
name: "Topologie"
source_url: "https://www.topologie.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A climbing-gear aesthetic translated into phone accessories, Topologie runs on a palette anchored by the deep, near-black #121212 and the warm, almost-burnt-orange #f92300 — a signal of technical restraint punctuated by a single climber's-carabiner accent. The site's canvas is a cool off-white #f7f7f7, not pure white, giving it the feel of unbleached paper or raw webbing. A secondary blue-gray #4b556c and muted steel #3c3c3c handle body copy and secondary text, while the hairline #dedede keeps cards and sections defined without visual weight. The typography stack defaults to Arial, inherit, and serif, suggesting a system-first approach or a site that hasn't loaded its custom typeface — the brand's voice comes through in the spacing and the raw, unpolished product photography rather than in bespoke letterforms. Buttons are sharp-cornered rectangles (`{rounded.none}`) with the #f92300 accent, echoing the functional, no-frills geometry of climbing hardware. Product cards use a subtle `{rounded.sm}` and a soft shadow, letting the gear — carabiners, straps, lanyards — sit as the hero. The nav bar is a thin, fixed strip at the top, #121212 on #f7f7f7, with a small cart icon and a hamburger menu, keeping the interface as minimal as a chalk bag. The overall feel is that of a mountaineering supply catalog that happens to sell phone cases: utilitarian, honest, and built around the idea that your everyday carry should be as dependable as your climbing rack.

colors:
  primary: "#f92300"
  primary-active: "#d91c01"
  primary-disabled: "#ffa278"
  ink: "#121212"
  body: "#3c3c3c"
  muted: "#595959"
  muted-soft: "#979797"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#f7f7f7"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#4b556c"
  accent-blue-light: "#9ebadc"
  accent-slate: "#2c2a41"
  sale-red: "#ac1800"
  star-rating: "#222222"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  mobile-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "8px 0 4px"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.sale-red}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  product-detail-section:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "24px 16px"
  product-detail-title:
    typography: "{typography.display-md}"
    padding: "0 0 8px"
  product-detail-price:
    typography: "{typography.title-md}"
    textColor: "{colors.muted}"
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    lineHeight: 1.6
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "16px 28px"
    height: 52px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "48px 16px 24px"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    textTransform: uppercase
    letterSpacing: 0.5px
  social-icon:
    textColor: "{colors.muted-soft}"
    height: 24px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "16px 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 16px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    padding: "80px 16px"
  hero-banner-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.surface-card}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-banner-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 28px"
  collection-grid:
    gap: "{spacing.base}"
  collection-title:
    typography: "{typography.display-lg}"
    padding: "0 0 24px"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  error-state:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "48px 16px"
  empty-state:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    padding: "48px 16px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature #f92300 on a white background. Sharp corners (`{rounded.none}`) reinforce the climbing-hardware aesthetic. On hover, the background shifts to `{colors.primary-active}` (#d91c01). In a disabled state, it becomes `{colors.primary-disabled}` (#ffa278) with no pointer events. The label is set in uppercase with 0.5px letter spacing, consistent with the brand's technical, utilitarian voice.

**`button-secondary`** — An outlined alternative with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. On hover, the border becomes `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Used for "View All" links, secondary checkout actions, and filter resets.

**`button-tertiary`** — A text-only button with no background or border. Uses `{colors.ink}` and the uppercase `{typography.button-md}` style. Reserved for navigation links like "Shop All" in the footer or "Learn More" in product descriptions.

**`button-pill-accent`** — A pill-shaped variant (`{rounded.full}`) of the primary button, used sparingly for promotional badges, sale callouts, and sticky add-to-cart bars on mobile. Smaller padding and font size (`{typography.button-sm}`) keep it compact.

### Cards
**`product-card`** — The core product display unit. A white card with `{rounded.sm}` corners, no border, and a subtle box shadow. The image area occupies a 1:1 aspect ratio with a `{colors.surface-soft}` background for loading states. Below the image, the title uses `{typography.title-sm}`, the price uses `{typography.body-sm}` in `{colors.muted}`, and sale prices appear in `{colors.sale-red}`. Badges (sale, sold out, new) are sharp-cornered rectangles positioned at the top-left of the image area.

**`product-card-badge`** — A small, sharp-cornered label (`{rounded.none}`) overlaid on the product image. Uses `{colors.primary}` background for "NEW" or "SALE" badges, `{colors.sale-red}` for clearance, and `{colors.ink}` for "SOLD OUT". Text is uppercase with tight tracking (`{typography.badge}`).

### Navigation
**`nav-bar`** — A fixed top bar at 64px height with a white background and a 1px `{colors.hairline}` bottom border. Contains the brand logo (left), navigation links (center, hidden on mobile), and a cart icon with a badge (right). Links use `{typography.nav-link}` — uppercase, 14px, weight 600 — with the active state highlighted in `{colors.primary}`.

**`mobile-menu`** — A full-screen overlay triggered by the hamburger icon. White background with `{colors.ink}` links set in `{typography.body-md}`. Includes a close button, primary navigation, and a "Shop All" CTA at the bottom.

### Forms
**`text-input`** — A standard input field with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.ink}`. Error states use a `{colors.primary}` border. Height is 48px with 12px/16px padding.

**`select-dropdown`** — Matches the text-input styling but includes a custom chevron icon in `{colors.muted}`. Used for sorting (Price, Newest, Best Sellers) and variant selection (Size, Color).

**`quantity-selector`** — A compact 44px-high control with minus/plus buttons flanking a central number display. Bordered with `{colors.hairline}`, no rounding. Used on product detail pages.

### Footer
**`footer-section`** — A dark section with `{colors.ink}` background and white text. Contains columns for customer service, about links, and social icons. Headings are uppercase with 0.5px letter spacing (`{typography.caption}`). Links are `{colors.muted-soft}` and turn white on hover. Social icons are 24px and match the link color.

### Hero
**`hero-banner`** — A full-width promotional section with a `{colors.ink}` background and white text. The title uses `{typography.display-xl}` (32px, weight 700), and the subtitle uses `{typography.body-md}` in `{colors.muted-soft}`. A `{colors.primary}` button anchors the bottom. Used for seasonal collections and new arrivals.

### Search
**`search-bar`** — A standard input field matching the text-input pattern, with a search icon (20px, `{colors.muted}`) positioned on the left. On focus, the border becomes `{colors.ink}`. Results appear in a dropdown below with product thumbnails and names.

### Filters
**`filter-chip`** — A pill-shaped filter toggle (`{rounded.full}`) with a white background and `{colors.hairline}` border. Active chips invert to `{colors.ink}` background with white text. Used on collection pages for size, color, and price range.

### Loading & Empty States
**`loading-spinner`** — A 32px circular spinner in `{colors.primary}`, centered in the content area. Used during product list loading and checkout processing.

**`empty-state`** — A centered block with `{colors.muted}` text and a 48px padding top and bottom. Used for empty search results, empty cart, and no matching filters. Includes a `{colors.ink}` "Shop All" link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), hamburger menu replaces nav links, hero banner padding reduces to 48px, footer stacks vertically, filter chips collapse into a "Filter" button that opens a drawer, product detail page stacks image above description |
| Tablet | 744–1128px | Two-column product grid (3 columns), nav links visible but condensed, hero banner at 64px padding, footer splits into two rows, filter chips visible inline, product detail page shows image and description side by side |
| Desktop | 1128–1440px | Three-column product grid (4 columns), full nav links visible, hero banner at 80px padding, footer in full four-column layout, filter chips with clear all option, product detail page with sticky add-to-cart |
| Wide | > 1440px | Max-width container at 1440px centered, product grid expands to 5 columns, hero banner content max-width at 1200px, additional whitespace around sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile.
- Cart icon and hamburger menu have a 48px touch area.
- Filter chips are 36px tall with 16px horizontal padding.
- Quantity selector buttons are 44px x 44px.
- Product card images link to the product page with a minimum 48px tap area.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu, and the search bar moves to a dedicated icon that opens a full-screen search overlay.
- The product filter strip collapses to a single "Filter" button that opens a bottom sheet drawer.
- The footer's four-column layout collapses to a single column with accordion-style sections.
- The hero banner's image and text stack vertically on mobile, with the image above the text.
- Product detail page sections (description, specs, reviews) collapse into an accordion on mobile and tablet.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font stack (Arial, inherit, serif) appears to be a fallback or system default — the brand's actual custom typeface could not be reliably identified. A future audit should inspect the site's @font-face declarations or Google Fonts integration.
- Hover and focus states for most components (beyond buttons and inputs) were not extractable from static HTML/CSS analysis.
- Error styling for forms (validation messages, error icons) was not observed in the extracted data.
- Dark mode or high-contrast mode variants are not present in the extracted palette.
- The extracted hex list includes many near-identical grays (#e6e6e6, #ebebeb, #f2f2f2, #f7f7f7) — the exact usage of each in the design system (e.g., which gray is used for hover vs. disabled vs. surface) is inferred from common patterns and may not match the live site's exact implementation.
- Sub-brand or seasonal color palettes (e.g., for collaborations or limited editions) were not captured.
- The extracted colors include some that may be Shopify default widget colors (e.g., Klarna/Afterpay badges) — these have been excluded from the primary palette.
- Animation and transition durations/easings were not extractable from static analysis.
- The site's iconography (beyond the cart and search icons) was not captured — the brand may use custom climbing-themed icons that are not represented in the CSS.
- The meta theme-color is #000000, which may indicate a dark mode or a specific browser chrome color — this was not used in the palette as it likely doesn't reflect the site's primary background.
