---
version: alpha
name: "UP1.co.uk"
source_url: "https://www.up1.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A catalogue site that reads like a well-worn paper stock-list, anchored on a singular, unapologetic parchment wash: `#ffffd0` — a pale butter-cream that replaces the usual white canvas and sets every page in a warm, slightly nostalgic glow. There is no hero image, no brand mark, no decorative illustration; the visual load is carried entirely by dense tables of product listings, each row a compact block of title, format, price, and stock status. The typography is absent of declared font-family, suggesting a system fallback stack that renders in the user-agent default — a deliberate or inherited austerity that prioritizes information density over brand polish. Buttons are minimal rectangles with hard corners (`{rounded.none}`), likely using a muted gray or the canvas tone as background, and text links in a standard blue (`#0000ee` or similar) provide the primary navigation. The single extracted hex, `#ffffd0`, is so pervasive it functions as both background and brand identifier — a dusty, library-like warmth that distinguishes UP1.co.uk from every glossy, white-space-heavy competitor in the movies-and-TV category. The site feels like a database given a gentle patina, where the design gesture is not layout or color-blocking but the sheer weight of structured data presented without apology.

colors:
  primary: "#ffffd0"
  primary-active: "#e6e6b8"
  primary-disabled: "#ffffe8"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0d0"
  canvas: "#ffffd0"
  surface-soft: "#f5f5c0"
  surface-card: "#ffffe0"
  on-primary: "#000000"
  link-blue: "#0000ee"
  link-visited: "#551a8b"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 8px 16px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    height: 36px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px
  product-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 6px 12px
  product-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 6px 12px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    height: 36px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: 16px 0
  badge-stock:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  link-inline:
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  link-visited:
    textColor: "{colors.link-visited}"
    typography: "{typography.link}"

## Components

### Buttons
**`button-primary`** — A flat, hard-cornered rectangle in the signature `#ffffd0` wash, with black text and minimal padding. Used for primary catalogue actions like "Add to Basket" or "View Details". The active state darkens the wash to `#e6e6b8`, while the disabled state lightens to `#ffffe8` with muted text. No hover shadow or border — the button is a pure block of color, consistent with the site's no-frills information design.

**`button-secondary`** — Identical shape and size to the primary button, but rendered on the canvas background with black text. Functions as a cancel or secondary action, visually recessive against the pervasive `#ffffd0` backdrop.

### Navigation
**`nav-bar`** — A 48px-high strip at the top of the page, filled with `{colors.primary}` and carrying text links in the system-ui fallback. Links use `{colors.link-blue}` for unvisited and `{colors.link-visited}` for visited, following classic web convention. No logo or brand mark — the nav is purely functional, likely containing "Home", "Catalogue", "Contact" and similar text entries.

**`search-bar`** — A simple text input with `{rounded.none}`, set against `{colors.surface-card}` (`#ffffe0`), slightly lighter than the canvas. The placeholder text and typed input use `{typography.body-md}`. No icon or decorative treatment — the search bar is a plain rectangle, aligned with the site's data-first ethos.

### Product Listings
**`product-table-row`** — The core content unit: a single row in a dense table, with cells for title, format, price, and stock status. Background alternates between `{colors.canvas}` and `{colors.surface-soft}` (`#f5f5c0`) for legibility. Text is `{typography.body-sm}` at 13px, maximizing the number of products visible without scrolling.

**`product-card`** — An alternative layout block, likely used for featured or grid-based product displays. Uses `{colors.surface-card}` (`#ffffe0`) background with `{rounded.none}` and minimal 8px padding. The card contains the product image (if any), title, and key metadata.

**`badge-stock`** — A small inline label indicating "In Stock", rendered in `{colors.primary}` background with black text. The `{badge-out-of-stock}` variant uses `{colors.muted-soft}` to signal unavailability. Both are hard-cornered rectangles with 2px vertical padding.

### Forms
**`text-input`** — A standard text entry field with `{rounded.none}`, `{colors.surface-card}` background, and `{typography.body-md}`. Used for search, login, and checkout forms. No border-radius, no shadow — just a functional rectangle.

### Footer
**`footer`** — A full-width strip at the page bottom, colored with `{colors.primary}` and containing copyright, contact, and policy links in `{typography.caption}`. The text is muted (`#666666`), keeping the footer visually subordinate to the product data above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product table collapses to single-column card layout; nav-bar stacks vertically; search-bar spans full width; font sizes reduce by 1-2px |
| Tablet | 744–1128px | Product table shows 2-3 columns; nav-bar remains horizontal but compresses; search-bar width reduces to 60% |
| Desktop | 1128–1440px | Full product table with 4-5 columns; nav-bar at 48px height; search-bar at 400px max-width; standard font sizes |
| Wide | > 1440px | Product table expands to 6+ columns; nav-bar and search-bar remain at desktop sizes; content area max-width at 1440px |

### Touch Targets
- All buttons and links maintain minimum 44x44px tap target on mobile
- Search-bar height increases to 44px on touch devices
- Product table rows have 44px minimum height for tap accuracy

### Collapsing Strategy
- Product table collapses to stacked cards below 744px
- Nav-bar links collapse into a hamburger menu below 600px
- Footer links collapse into a single column below 480px
- Search-bar placeholder text truncates on narrow screens

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the typography block uses a generic system-ui fallback stack. The actual brand font (if any) could not be determined.
- Only one hex color (`#ffffd0`) was reliably extracted. All other colors in the palette are inferred from common web defaults (link blue, visited purple, muted grays) and may not match the live site's actual choices.
- No hover, focus, or active states could be extracted for buttons, links, or inputs beyond basic color shifts.
- No border, shadow, or gradient values were found; all components assume flat, borderless styling.
- No image or icon assets were analyzed; the site may use product thumbnails or decorative elements not captured here.
- No dark mode or high-contrast mode styling is defined.
- No animation or transition durations were extracted.
- The site's checkout flow, payment forms, and error states are not represented in this design system.
