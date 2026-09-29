---
version: alpha
name: "Bull Moose"
source_url: "https://www.bullmoose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store’s website that feels like a record store — not a sterile e‑commerce shell — Bull Moose uses a near‑white canvas (#eeeeee) as its primary surface, letting the album art, movie posters, and product photography supply all the color. The brand’s sole extracted hex is this soft off‑white, which reads as a deliberate, paper‑like ground rather than a cold digital white. The typography is where the personality lives: the display face is kanedagothic‑extrabold, a heavy, slightly condensed gothic that echoes vintage punk flyers and indie‑label logos, while body copy defaults to system sans‑serifs. Buttons and interactive elements use a generous {rounded.sm} (8px) radius — not pill‑shaped, not sharp — a middle ground that feels approachable without being cute. The top navigation is a simple horizontal strip, and the search bar sits prominently, often with a {rounded.full} pill shape, inviting browsing over hunting. There are no hero carousels or full‑bleed imagery; instead, the layout is a dense, browsable grid of product cards, each with a thumbnail, title, artist, and price — the visual language of a physical bin dive translated into a responsive column system. The brand trusts its inventory to do the talking: the design steps back, provides clear hierarchy through weight and spacing, and gets out of the way. It’s a utility‑first, personality‑through‑type system that prioritizes discoverability over polish.

colors:
  primary: "#eeeeee"
  primary-active: "#d4d4d4"
  primary-disabled: "#f5f5f5"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#eeeeee"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#111111"
  accent: "#cc0000"
  badge-new: "#cc0000"
  badge-sale: "#cc0000"
  link: "#0066cc"
  link-visited: "#551a8b"
  star-rating: "#f5a623"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'kanedagothic-extrabold', 'Impact', 'Haettenschweiler', 'Arial Narrow Bold', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'kanedagothic-extrabold', 'Impact', 'Haettenschweiler', 'Arial Narrow Bold', sans-serif"
    fontSize: 28px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'kanedagothic-extrabold', 'Impact', 'Haettenschweiler', 'Arial Narrow Bold', sans-serif"
    fontSize: 22px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'kanedagothic-extrabold', 'Impact', 'Haettenschweiler', 'Arial Narrow Bold', sans-serif"
    fontSize: 20px
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  price-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-active:
    backgroundColor: "#990000"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-pill-search:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.ink}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.accent}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.accent}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    textColor: "{colors.accent}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
    border-bottom: "1px solid {colors.hairline}"
  category-tab-active:
    textColor: "{colors.accent}"
    typography: "{typography.button-sm}"
    border-bottom: "2px solid {colors.accent}"
  category-tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-link-hover:
    textColor: "{colors.accent}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 600

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Checkout,” and primary form submissions. It uses a solid black (`{colors.ink}`) fill with white (`{colors.canvas}`) text, creating maximum contrast against the near-white canvas. On hover/active, the fill shifts to `{colors.body}` (#333333) for a subtle darkening effect. The disabled state uses `{colors.muted-soft}` (#999999) to signal non-interactivity. All primary buttons use `{rounded.sm}` (8px) and a compact 10px 20px padding.

**`button-secondary`** — Used for less prominent actions like “View Details,” “Cancel,” or “Clear Filters.” It inverts the primary pattern: a white (`{colors.canvas}`) background with black (`{colors.ink}`) text and a 1px solid `{colors.hairline}` border. On hover/active, the background shifts to `{colors.surface-soft}` and the border darkens to `{colors.muted}`. The height and padding match the primary button for consistent vertical rhythm.

**`button-accent`** — Reserved for high-visibility, promotional, or urgency-driven actions such as “Pre-Order,” “Limited Edition,” or “Sale.” It uses a red (`{colors.accent}`) fill with white text, standing out against the otherwise monochrome palette. The active state darkens to #990000. This button is used sparingly to preserve its signaling power.

**`button-pill-search`** — A specialized pill-shaped button used exclusively within the search bar or as a search submit. It shares the accent red fill but uses `{rounded.full}` (9999px) to create a friendly, inviting entry point. The height is slightly taller (44px) than standard buttons to align with the search input field.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 56px height, using the canvas background (`{colors.canvas}`) with a single `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` (14px, weight 600, 0.3px letter spacing) for a clean, readable hierarchy. The active or hover state of a link shifts its color to `{colors.accent}`, providing a clear, low-contrast indicator of the current section.

**`category-strip`** — A secondary horizontal strip below the main nav, used for browsing by genre, format, or department. It uses smaller `{typography.button-sm}` type and `{colors.muted}` text for inactive categories. The active category tab is underlined with a 2px `{colors.accent}` border and uses the accent color for its text, making the current filter immediately visible.

**`breadcrumb-link`** — Breadcrumb navigation uses `{typography.caption}` (12px) in `{colors.muted}` for parent links, with a hover state that shifts to `{colors.accent}`. The current page is rendered in `{colors.ink}` with a weight of 600, distinguishing it from the navigable ancestors.

### Cards
**`product-card`** — The core content unit of the site, used for every product in grid and list views. It is a white (`{colors.surface-card}`) card with `{rounded.sm}` (8px) and `{spacing.sm}` (8px) internal padding. The product image fills the top with a `{rounded.xs}` (4px) corner and a 1:1 aspect ratio. Below the image, the title uses `{typography.title-sm}` (14px, weight 600), the artist name uses `{typography.caption}` (12px) in `{colors.muted}`, and the price uses `{typography.price-md}` (16px, weight 700). A `{product-card-badge}` can overlay the top-left of the image for “New,” “Sale,” or “Pre-Order” indicators, using `{colors.badge-new}` (#cc0000) background and white text in uppercase 11px.

### Forms
**`text-input`** — Standard text input for search, account forms, and checkout fields. It uses a white background (`{colors.surface-card}`), 44px height, `{rounded.sm}` (8px), and a 1px `{colors.hairline}` border. On focus, the border becomes a 2px solid `{colors.ink}`. Error states use a 2px `{colors.accent}` border. Internal padding is 10px 14px with `{typography.body-md}` (16px) for readability.

**`search-bar`** — The primary search input, distinguished from standard text inputs by its `{rounded.full}` pill shape and 44px height. It uses a white background with a 1px `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.ink}`. The search bar is often paired with the `{button-pill-search}` to its right, creating a cohesive, full-height search module.

### Footer
**`footer`** — A full-width footer with a black (`{colors.ink}`) background and white (`{colors.canvas}`) text. It uses `{typography.body-sm}` (14px) for body content and `{typography.link}` for link items. Links are initially `{colors.muted-soft}` (#999999) and shift to white on hover. The footer has generous vertical padding (`{spacing.xxl}`) and horizontal padding (`{spacing.base}`) to create a grounded, weighty base for the page.

### Pagination
**`pagination-button`** — Used for page navigation on search results and category listings. Each button is a 40px square-ish element with `{rounded.sm}`, a 1px `{colors.hairline}` border, and `{typography.button-sm}`. The active page uses a solid `{colors.ink}` fill with white text, while inactive pages use the canvas background. This creates a clear, scannable pagination strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves below nav; footer stacks vertically; category strip becomes a horizontal scrollable row |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but may truncate links; search bar is full-width below nav; footer columns wrap to two |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav; search bar is a prominent pill in the header; footer displays in four columns |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to five columns; all elements use increased whitespace and larger type at the upper end |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px × 44px on mobile and tablet.
- Product card images and titles are fully tappable, with a minimum 48px height for the title area.
- Category strip items have 48px minimum height and 44px minimum width.
- Pagination buttons are 44px × 44px minimum on touch devices.
- Hamburger menu icon is 48px × 48px.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu. The menu overlay is full-screen with a white background and a close icon.
- The category strip collapses to a horizontally scrollable row with a “fade” gradient on the right edge to indicate overflow.
- The footer collapses from a multi-column layout to a single vertical stack, with accordion-style expandable sections for link groups.
- Product grids collapse from multi-column to single-column, with images scaling to full width.
- The search bar moves from the header to a dedicated, full-width row below the navigation on mobile and tablet.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#eeeeee) was reliably extracted from the live site. The remaining colors in this palette (ink, body, muted, accent, etc.) are inferred from common patterns in independent record store e‑commerce and may not match the exact live values. A full visual audit is required to confirm the true secondary palette.
- The accent red (#cc0000) is a common choice for sale/badge elements in this category but was not extracted from the live site. Its exact hue, saturation, and usage frequency should be verified.
- Font stack for kanedagothic-extrabold is assumed; the exact fallback chain and any additional weights (e.g., regular, medium) were not extracted.
- No hover, focus, or active state colors were extracted for any component. All state colors in this file are inferred.
- Error, success, and warning color tokens are not defined and should be added after audit.
- Dark mode is not supported and no dark-mode tokens are defined.
- The extracted font list includes Font Awesome and spruce-icon-pack icons; these are used for UI icons (cart, search, menu, social links) but their exact usage and sizing are not documented here.
- No spacing or typography scale was extracted from the live site; all values are based on common e‑commerce patterns and should be validated against the actual CSS.
- The `meta theme-color` was not set on the live site; mobile browser chrome behavior is undefined.
