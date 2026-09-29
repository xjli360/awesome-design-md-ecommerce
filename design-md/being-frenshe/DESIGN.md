---
version: alpha
name: "Being Frenshe"
source_url: "https://www.beingfrenshe.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bath-and-body brand that wraps itself in a deep, almost-black ink (#121212) and a single electric blue accent (#146ff8) that feels more like a charged promise than a corporate logo. The palette is deliberately sparse — near-black, warm gray (#dedede), soft canvas (#f3f3f3), and two darker anchors (#242833, #334fb4) — leaving the products themselves to supply all the color. Assistant, set at a clean 16px with generous line-height, carries the entire typographic system without a second face; the brand trusts weight and size alone to create hierarchy. Buttons are pill-shaped (`{rounded.full}`) in that signature blue, sitting on a white or near-white canvas that reads as a clean bathroom shelf. The nav bar stays transparent until scroll, then snaps to white with a thin hairline — a small but deliberate reveal that signals the brand knows when to step back. Product photography is the real palette: amber bottles, sage-green caps, rose-gold pumps. The design system is a frame, not a filter.

colors:
  primary: "#146ff8"
  primary-active: "#0f5cd4"
  primary-disabled: "#a0c4ff"
  ink: "#121212"
  body: "#242833"
  muted: "#334fb4"
  muted-soft: "#6a7ab5"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f3f3f3"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#146ff8"
  accent-dark-blue: "#334fb4"
  badge-new: "#146ff8"

typography:
  display-xl:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  collection-grid:
    gap: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill in the brand's electric blue (#146ff8). Used for "Add to Cart", "Shop Now", and primary checkout actions. On hover, darkens to `{colors.primary-active}` (#0f5cd4). Disabled state uses `{colors.primary-disabled}` (#a0c4ff) with no border, signaling the action is unavailable. Text is always white, weight 600, with 0.3px letter spacing for legibility at small sizes.

**`button-secondary`** — A white pill with a 2px `{colors.hairline}` border and `{colors.ink}` text. Used for "Learn More", "View Details", and secondary actions alongside the primary button. Hover state darkens the border to `{colors.muted}`. Disabled state uses `{colors.hairline-soft}` border and `{colors.muted-soft}` text.

**`button-tertiary`** — A text-only button with no background or border, using `{colors.primary}` text. Used for "Cancel", "Skip", and inline actions within forms or modals. Hover state adds a subtle underline.

### Navigation
**`nav-bar`** — A fixed top navigation bar, 64px tall, with white background and uppercase nav links in `{typography.nav-link}`. On scroll, a 1px `{colors.hairline-soft}` bottom border appears. The logo sits left-aligned, links are center-aligned, and the cart icon sits right. Mobile collapses to a hamburger menu with a slide-out drawer.

**`nav-link`** — Uppercase, 14px, weight 600, with 0.5px letter spacing. Active state uses `{colors.primary}` text. Hover state adds a 2px bottom border in `{colors.primary}`.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners, containing a square product image and text below. The image has `{rounded.md}` corners and a 1:1 aspect ratio. Title uses `{typography.title-sm}` in `{colors.ink}`, price uses `{typography.body-md}` in `{colors.body}`. On hover, the card lifts with a subtle box-shadow and the image may zoom slightly.

**`badge-new`** — A small pill badge in `{colors.badge-new}` (blue) with white uppercase text. Used to flag new arrivals. Positioned absolutely over the top-left corner of product images.

**`badge-sale`** — A small pill badge in `{colors.ink}` (near-black) with white uppercase text. Used to flag sale items. Positioned absolutely over the top-left corner of product images.

### Forms
**`text-input`** — A standard text input field with 48px height, 12px padding, `{rounded.sm}` (8px) corners, and a 1px `{colors.hairline}` border. Background is white, text is `{colors.ink}`. On focus, the border switches to `{colors.primary}` (blue). Placeholder text uses `{colors.muted-soft}`.

**`search-bar`** — A pill-shaped search input with `{rounded.full}`, 44px height, and a `{colors.surface-soft}` background. Used in the header and on search pages. On focus, the background switches to white with a `{colors.hairline}` border.

### Footer
**`footer-section`** — A full-width footer with `{colors.canvas}` (#f3f3f3) background, `{colors.body}` text, and `{spacing.section}` (64px) vertical padding. Links are `{typography.link}` in `{colors.body}`. The footer typically includes columns for "Shop", "About", "Help", and social links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, hero reduced to 32px padding |
| Tablet | 744–1128px | Two-column product grid, full nav with condensed links, two-column footer |
| Desktop | 1128–1440px | Three-column product grid, full nav, three-column footer, hero at full padding |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 40px tap area
- Product card tap targets at least 48px
- Search bar at 44px height for comfortable tapping

### Collapsing Strategy
- Primary nav links collapse into hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns stack: 3 → 2 → 1
- Hero section padding reduces from 64px to 32px on mobile
- Search bar shrinks from full-width to icon-only on mobile, expanding on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are limited to 6 values, with #146ff8 (blue) and #121212 (near-black) as the most distinctive. The palette may include additional brand-specific tones (e.g., product photography colors, accent hues) that could not be extracted from the limited sample.
- Hover and active states for secondary and tertiary buttons are inferred from common patterns; exact extracted values are not available.
- Error states for form inputs (border color, error text color) are not extracted.
- Dark mode styling is not present on the live site and is not defined.
- The font-family extraction returned only "Assistant"; fallback stacks are inferred from common web patterns.
- Typography scale (font sizes, weights, line heights) is estimated from the single extracted font and typical e-commerce patterns; exact values may vary.
- Spacing and rounded values are estimated from common design system patterns; the brand may use different values.
- Component padding and height values are estimated from typical button and input sizes; exact values may vary.
- The brand's sub-brand or collection-specific styling (e.g., limited edition packaging) is not captured.
- The extracted colors may include Shopify or platform-default colors that are not part of the brand's intentional design system.
