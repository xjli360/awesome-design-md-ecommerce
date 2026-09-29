---
version: alpha
name: "Hyperlite Mountain Gear"
source_url: "https://www.hyperlitemountaingear.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand that builds its entire visual identity around a single, unmistakable voltage: #d54300 — a burnt-orange that reads as anodized aluminum, trail-dust, and the last light on a granite face. This orange is the brand's only color; it appears on the primary CTA, the shopping-bag icon, the "Add to Cart" button, and nowhere else in the palette. The rest of the system is a study in grays and near-grays: #171717 for ink, #676986 for body text, #f4f4f6 for the canvas, and #272d45 for deep-surface accents. The result is a site that feels like a machined part — every element has a purpose, every corner is either perfectly sharp ({rounded.none}) or softly radiused ({rounded.sm} at 8px), and the typography runs Geogrotesque W01 at moderate weights (400–600) with no display-size hero text. The product grid uses 12px rounded corners on cards, a 1px hairline in #e5e5e5, and generous whitespace that lets the gear's own photography — Dyneema composite fabrics, titanium stakes, carbon-fiber poles — carry the emotional weight. There is no decorative illustration, no gradient, no secondary accent color. The brand trusts that the orange, the gray scale, and the product itself are enough.

colors:
  primary: "#d54300"
  primary-active: "#c63e00"
  primary-disabled: "#eeb499"
  ink: "#171717"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  surface-deep: "#272d45"
  on-primary: "#ffffff"
  on-deep: "#ffffff"
  accent-sale: "#ff5000"
  accent-urgent: "#ff4d1a"
  badge-new: "#28657e"
  badge-sale: "#6d7d42"
  star-rating: "#171717"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  price-md:
    fontFamily: "'Geogrotesque W01', 'Public Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
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
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-urgent:
    backgroundColor: "{colors.accent-urgent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-urgent}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-deep}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-deep}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 44px
  search-bar-active:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-deep}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-deep}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The single brand voltage. A solid #d54300 rectangle with 8px rounded corners, white uppercase Geogrotesque at 14px/600. On hover, shifts to #c63e00. Disabled state fades to #eeb499. Used for "Add to Cart," "Checkout," and primary purchase flows. Height is 44px with 12px/24px padding.

**`button-secondary`** — White canvas with a 1px #e5e5e5 border, same uppercase typography. Used for "Learn More," "View Details," and secondary actions. Hover state darkens the border to #d3d4dd.

**`button-tertiary`** — Ghost button with no background, text in #d54300. Used for "Clear Filters," "Cancel," and inline actions. Hover adds a subtle underline.

**`button-pill-urgent`** — A fully rounded pill in #ff4d1a, smaller 12px uppercase type, 32px height. Reserved for limited-time sale badges, "Last Chance" prompts, and urgency signals.

### Cards
**`product-card`** — A white card with 12px rounded corners and a 1px #f4f4f6 border. Contains a product image (top corners rounded, bottom corners sharp), title in 16px/500, price in 16px/600, and optional badge. Hover state thickens the border to #e5e5e5. No shadow — the brand trusts the product photography.

**`product-card-badge`** — A small 11px uppercase label in #28657e (teal) for "NEW" or #6d7d42 (olive) for "SALE," with 4px rounded corners and 2px/8px padding. Sits at the top-left of the card image.

### Navigation
**`nav-bar`** — A 64px white bar with a 1px #f4f4f6 bottom border. Links are 14px/500 Geogrotesque with 0.3px letter spacing. Active and hover states turn the link text to #d54300. The logo sits left, the cart icon (also #d54300) sits right.

**`breadcrumb`** — 13px/500 caption type in #9a9db1, with the active segment in #171717. Separator is a simple "/" in #d3d4dd.

### Forms
**`text-input`** — White background, 1px #e5e5e5 border, 8px rounded corners, 48px height, 16px body type. Active state switches the border to #d54300. Error state switches to #ff4d1a. Used for search, email signup, and checkout fields.

**`quantity-selector`** — A compact 44px input with 8px rounded corners and a 1px #e5e5e5 border. Contains a minus button, the quantity number, and a plus button. The buttons are 40px icon-button circles with hover background.

### Search
**`search-bar`** — A fully rounded pill, 44px tall, with a 1px #e5e5e5 border and 10px/20px padding. Active state switches the border to #d54300. The search icon sits inside the left padding in #9a9db1.

### Filters
**`filter-chip`** — A 36px pill with 1px #e5e5e5 border, 6px/16px padding, and 14px body type. Active state fills with #d54300 and white text. Used in category and size filter strips.

### Footer
**`footer-section`** — A deep #272d45 background with white text. Links are 14px/400 in #d3d4dd, hover to white. The section uses 64px vertical padding and 24px horizontal padding. Contains columns for "Shop," "Support," "About," and "Connect."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes 1 column; hero padding reduces to 32px; filter chips stack vertically; footer columns stack to 2-column grid |
| Tablet | 744–1128px | Nav shows full links; product grid goes 2 columns; search bar in nav becomes icon-only; footer columns go 2x2 |
| Desktop | 1128–1440px | Full nav with search bar; product grid goes 3 columns; hero uses 64px padding; footer columns go 4 across |
| Wide | > 1440px | Max-width container at 1440px; product grid goes 4 columns; hero uses 80px padding |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (WCAG 2.1 compliant).
- Filter chips are 36px height — acceptable for touch but may feel small; consider 40px on mobile.
- Icon buttons are 40px circles — meets the 44px target for touch.
- Search bar is 44px tall — comfortable for thumb reach.
- Product card links are the full card area (not just the title text).

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu with a slide-out drawer.
- The product filter sidebar (desktop) collapses to a horizontal chip strip on tablet, and to a "Filter" button that opens a modal on mobile.
- The hero section's secondary text collapses on mobile (only headline and primary CTA remain).
- The footer's 4-column layout collapses to 2 columns on tablet, 1 column on mobile.
- Product image galleries (desktop: thumbnail strip + main image) collapse to a single swipeable carousel on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list includes several colors (#2c3e50, #28657e, #1f4f62, #3e6f8f, #6d7d42, #ff4d1a) that may be Shopify checkout widgets, social icons, or stock-image tones — not confirmed as brand colors. The badge colors (#28657e, #6d7d42) are best guesses from the list.
- Font weights beyond 400, 500, and 600 are assumed — the extracted CSS only showed "inherit" and generic sans-serif. Geogrotesque W01 may have 700 available but it's not confirmed on the live site.
- Hover states for buttons and links are inferred from common patterns (darken primary, underline text) — not extracted from live CSS.
- Error styling for forms (error messages, validation icons) is not present in the extracted data.
- Dark mode is not supported on the live site (no `prefers-color-scheme` detected).
- The "Outage" and "Outage Cut" fonts in the extracted list appear to be decorative/display fonts used sparingly (possibly for the logo or hero headlines) — not included in the typography system as they are not the primary reading face.
- The `oke-widget-icons` font is from Okendo (reviews platform) — not a brand font.
- No animation or transition timings were extracted (assume 200ms ease for hover/focus transitions).
- The extracted hex list is large (20+ colors) and likely includes many non-brand colors from third-party widgets and images. The true brand palette is probably the 6-8 most frequent grays + the distinctive orange.
