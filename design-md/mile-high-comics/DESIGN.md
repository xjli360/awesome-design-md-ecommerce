---
version: alpha
name: "Mile High Comics"
source_url: "https://www.milehighcomics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A comic-book emporium that wears its love of the medium on its sleeve, Mile High Comics uses a palette that reads like a spinner rack exploded onto a web page. The primary red `#ff0000` is pure, unmodulated, the same red as a Superman cape or a Marvel logo — it appears on every primary CTA, every price badge, every key navigational element, demanding attention with the confidence of a direct-market veteran. That red is backed by a supporting cast of high-saturation accents: `#66ff00` (a neon lime that could be Green Goblin's grin), `#ffff00` (a yellow as bright as a first-print Wolverine cover), and `#00ff00` (a digital green used for in-stock indicators). The body text sits on a deep navy `#000033` background in many sections — a bold choice for a retail site, making the white `#fffccc` and `#faebd7` (antique white) text areas feel like comic panels floating in space. The typography is utilitarian: Arial and Verdana at standard weights, no custom typefaces, no letter-spacing theatrics — the brand trusts its inventory photography and price tags to do the selling. The overall effect is a site that feels built by collectors for collectors: dense, information-rich, and unapologetically loud.

colors:
  primary: "#ff0000"
  primary-active: "#cc0000"
  primary-disabled: "#ff6666"
  ink: "#000033"
  body: "#110033"
  muted: "#888888"
  muted-soft: "#444444"
  hairline: "#ccccff"
  hairline-soft: "#ccccff"
  canvas: "#000033"
  surface-soft: "#23238e"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#66ff00"
  accent-yellow: "#ffff00"
  accent-green: "#00ff00"
  accent-gold: "#ffd700"
  accent-orange: "#ffa500"
  accent-blue: "#0674b5"
  accent-darkblue: "#00008b"
  antique-white: "#faebd7"

typography:
  display-xl:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 8px 16px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.primary}"
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  in-stock-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  out-of-stock-badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xl} {spacing.base}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 28px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 28px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 28px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 28px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in pure red `{colors.primary}` with white text. Used for "Add to Cart", "Buy Now", and primary navigation actions. On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}`. Height is 36px with `{rounded.sm}` corners.

**`button-secondary`** — A white button with dark text, used for secondary actions like "View Details" or "Continue Shopping". Same dimensions as primary but with a white background and `{colors.ink}` text. Border is `{colors.hairline}`.

**`button-ghost`** — Transparent background with white text, used on dark backgrounds like the hero banner or footer. Same dimensions as primary. No border.

### Cards
**`product-card`** — The core product display unit. A white card with `{rounded.sm}` corners and `{spacing.sm}` padding. Contains a product image, title in `{typography.title-md}`, and price in `{typography.price-lg}` colored `{colors.primary}`. The image area uses `{colors.surface-soft}` as a placeholder background.

**`price-badge`** — A small red badge (`{colors.primary}`) with white text, used to display sale prices or discounts. `{rounded.xs}` corners with minimal padding.

**`in-stock-badge`** — A green badge (`{colors.accent-green}`) indicating availability. Same dimensions as price-badge.

**`out-of-stock-badge`** — A gray badge (`{colors.muted}`) for unavailable items. Same dimensions.

### Navigation
**`nav-bar`** — The primary navigation bar, fixed at 48px height on a deep navy background (`{colors.canvas}`). Links use `{typography.nav-link}` in white. Active links get a `{colors.primary}` background.

**`nav-link`** — Standard navigation link with transparent background and white text. Active state uses `{colors.primary}` background.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) on a white background with `{colors.hairline}` border. 40px height with `{spacing.sm}` padding. Uses `{typography.body-md}` for input text.

### Category Chips
**`category-chip`** — Pill-shaped filter chips (`{rounded.full}`) on a dark blue background (`{colors.surface-soft}`) with white text. 28px height. Active state uses `{colors.primary}` background.

### Pagination
**`pagination-button`** — Small square buttons (`{rounded.sm}`) for page navigation. White background with dark text. Active page uses `{colors.primary}` background with white text.

### Loading
**`loading-spinner`** — A 24px spinning indicator in `{colors.primary}`. Used during AJAX loads and page transitions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav-bar, search bar collapses to icon, category chips scroll horizontally, price badges stack vertically |
| Tablet | 744–1128px | Two-column product grid, nav-bar shows top-level links only, search bar remains full-width, category chips wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid, full nav-bar visible, search bar with autocomplete, category chips in single row |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, additional whitespace on sides |

### Touch Targets
- All buttons and links: minimum 44x44px tap target
- Category chips: 28px height with 12px padding (effective 52px tap width)
- Search bar: 40px height with full width
- Product card: entire card is tappable (minimum 200x200px)
- Pagination buttons: 28x28px with 8px padding (effective 44x44px)

### Collapsing Strategy
- Navigation: On mobile, full nav-bar collapses to hamburger menu. Top-level links (New Arrivals, Back Issues, Graphic Novels, etc.) become accordion items.
- Product grid: Collapses from 4 columns to 1 column on mobile. Images scale proportionally.
- Search: On mobile, search bar collapses to a magnifying glass icon that expands to full-width input on tap.
- Category chips: On mobile, horizontal scroll with snap points replaces the full grid.
- Footer: On mobile, multi-column footer collapses to single column with accordion sections.
- Sidebar filters: On mobile, filters collapse to a "Filter" button that opens a modal overlay.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components beyond primary button (secondary, ghost, nav links) were not extractable from the live site.
- Focus states and keyboard navigation styling are not documented.
- Error states for forms (validation, error messages) are not available.
- Dark mode is not supported; the site uses a dark canvas by default.
- The exact font sizes for body text and headings are estimated based on common Arial/Verdana usage; the site may use relative units (em/rem) that scale differently.
- The `{colors.hairline}` and `{colors.hairline-soft}` values are identical (`#ccccff`) — this may indicate a single hairline color is used throughout.
- The extracted color list includes several high-saturation accents (`#66ff00`, `#ffff00`, `#00ff00`, `#ffd700`, `#ffa500`) whose exact usage (badges, borders, backgrounds) could not be confirmed from the extraction alone.
- The `{colors.antique-white}` (`#faebd7`) appears in the extraction but its specific role (text background, card background, or decorative element) is unclear.
- No custom font declarations were found beyond Arial and Verdana; the site may use system fonts with specific weights that were not captured.
- The `{colors.surface-soft}` value (`#23238e`) is a very dark blue — its contrast ratio against white text should be verified for accessibility.
- No animation or transition durations were extractable.
- The site may use a different color for visited links (not captured).
- The `{colors.accent-blue}` (`#0674b5`) may be used for links or secondary CTAs, but this is speculative.
