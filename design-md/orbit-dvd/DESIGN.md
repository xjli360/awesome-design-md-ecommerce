---
version: alpha
name: "Orbit DVD"
source_url: "https://www.orbitdvd.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cinema-obsessed retailer whose palette reads like a film-stock contact sheet — warm taupe-beiges (#e3dacc, #ddd3c2, #e8e1d6) dominate the backdrop, while a single burst of #ff580d (a safety-orange that could be a 35mm film canister or a 1970s Criterion spine) ignites every add-to-cart button, badge, and price highlight. The site runs on a near-monochrome skeleton of #dedede and #f9f9f9, with product cards floating on #f2f2f2 and text set in #121212 against those sandy neutrals. Typography leans on system fonts — Arial, Helvetica Neue, Roboto — at modest sizes, letting the movie-poster art and genre tags do the heavy lifting. Buttons are pill-shaped (`{rounded.full}`) in that orange, with secondary actions in a muted #baa98f that echoes aged paper. The nav bar is a thin strip of #34343d, dark but not black, carrying genre dropdowns and a search bar with a #777777 placeholder. There is no hero splash, no carousel — just a dense grid of covers, each a 1:1.4 portrait crop, with a "NEW" badge in #899df1 (a cool blue that breaks the warmth) and a stock-status badge in the orange. The checkout path swaps to a clean #ffffff canvas with #d8d8d8 dividers, but the orange persists on the confirm button. The overall effect is a video-store-turned-web-app: the warmth of a 1990s Blockbuster carpet, the precision of a boutique Blu-ray label.

colors:
  primary: "#ff580d"
  primary-active: "#f45213"
  primary-disabled: "#ffc9a3"
  ink: "#121212"
  body: "#34343d"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#d8d8d8"
  hairline-soft: "#e4e4e4"
  canvas: "#f9f9f9"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#e3dacc"
  accent-warm-mid: "#ddd3c2"
  accent-warm-light: "#e8e1d6"
  badge-blue: "#899df1"
  badge-beige: "#baa98f"
  badge-brown: "#ad9173"
  nav-bg: "#34343d"
  nav-text: "#dedede"
  star-rating: "#121212"

typography:
  display-xl:
    fontFamily: "Arial Black, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  price:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
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
    padding: 12px 28px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1.4"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-stock:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-format:
    backgroundColor: "{colors.badge-beige}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the signature safety-orange `{colors.primary}` (#ff580d) as a pill shape (`{rounded.full}`). On hover it deepens to `{colors.primary-active}` (#f45213); disabled state drops to a pale peach `{colors.primary-disabled}` (#ffc9a3). Used for "Add to Cart", "Checkout", and "Subscribe" actions. **`button-secondary`** — An outlined variant on a white background with `{colors.ink}` text and a `{colors.hairline}` border, also pill-shaped. Used for "View Details" and "Continue Shopping". **`button-tertiary`** — A text-only link in the primary orange, no background or border, for inline actions like "Clear Filters". **`button-ghost`** — A minimal button with no background and `{colors.body}` text, used for utility actions like "Cancel" in modals.

### Cards
**`product-card`** — The core product display unit: a soft gray (`{colors.surface-soft}`) background with `{rounded.sm}` corners, containing a 1:1.4 aspect-ratio image (mimicking a Blu-ray case) and a text block below. The title uses `{typography.title-sm}`, the price is set in `{typography.price}` and colored `{colors.primary}` to draw the eye. A stock-status line in `{typography.caption-sm}` and `{colors.muted}` sits beneath. Badges (new, sale, format) overlay the top-left corner of the image.

### Navigation
**`nav-bar`** — A dark (`{colors.nav-bg}` #34343d) horizontal strip at 56px height, carrying the brand logo (left), genre dropdowns (center), and a search bar plus cart icon (right). Nav links are `{typography.nav-link}` in `{colors.nav-text}` (#dedede). The search bar is a pill-shaped input (`{rounded.full}`) on a white background with `{colors.muted-soft}` placeholder text. The cart icon carries a `{rounded.full}` badge in `{colors.primary}` with a white count.

### Forms
**`text-input`** — Standard text input with a white background, `{colors.hairline}` border, `{rounded.sm}` corners, and `{typography.body-sm}`. On focus the border thickens to 2px and turns `{colors.primary}`. Placeholder text is `{colors.muted-soft}`. Used in search, checkout forms, and account pages.

### Badges
**`badge-new`** — A small pill in `{colors.badge-blue}` (#899df1) with uppercase white text, signaling newly added titles. **`badge-sale`** — Same shape but in `{colors.primary}` orange, used for discounted items. **`badge-format`** — A beige (`{colors.badge-beige}` #baa98f) badge indicating the media format (4K, Blu-ray, DVD). All badges use `{typography.badge}` (11px, bold, uppercase).

### Footer
**`footer`** — A dark band matching the nav bar (`{colors.nav-bg}`), containing links in `{colors.muted-soft}` (#aaaaaa) and copyright text in `{typography.body-sm}`. Links are spaced with `{spacing.sm}` and arranged in columns on desktop, stacking on mobile.

### Filters & Pagination
**`filter-chip`** — A pill-shaped toggle button on a white background with a `{colors.hairline}` border. Active state fills with `{colors.primary}` and white text. Used for genre, format, and price-range filtering. **`pagination-button`** — A small square button with `{rounded.sm}` corners, used in the page-number strip at the bottom of product grids. Active page uses `{colors.primary}` background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns max), nav collapses to hamburger menu, search bar becomes an icon toggle, footer stacks vertically, filter chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid, nav shows top-level genres only, search bar is full-width but collapses on scroll, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav with dropdowns, persistent search bar, footer in 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, nav remains full, additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements minimum 44px height (per Apple HIG)
- Filter chips and badge taps minimum 32px height
- Nav dropdowns open on tap (not hover) on mobile/tablet
- Cart icon and search icon minimum 44x44px tap area

### Collapsing Strategy
- Nav bar: genre dropdowns collapse into a hamburger menu at < 744px; secondary nav links (Account, About) move to a bottom drawer
- Product grid: columns reduce from 4 to 3 to 2 to 1 as viewport shrinks
- Footer: 4-column layout collapses to 2 columns at tablet, single column at mobile
- Search bar: full input collapses to a magnifying-glass icon on mobile, expanding to a full-screen overlay on tap
- Filter bar: horizontal chip strip becomes a scrollable row on mobile; on desktop it sits as a static row above the grid

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not extractable from static CSS; only `button-primary` hover was confirmed via extracted `#f45213`
- Error state styling (form validation, 404 page) could not be determined — no error hexes appeared in the extracted palette
- Dark mode: no evidence of a dark-mode variant in the extracted colors or CSS; the site appears light-mode only
- Typography scale is inferred from common e-commerce patterns and the extracted font stack; exact sizes and weights for `display-xl`, `display-md`, etc. are best-guess based on the brand's visual weight
- The extracted palette includes several beige/taupe tones (#e3dacc, #ddd3c2, #e8e1d6) that appear to be background or card surfaces, but their exact roles (e.g., which is the primary page background vs. a card surface) are uncertain — `{colors.accent-warm}` tokens are a best interpretation
- The blue `#899df1` appeared in the palette but its exact usage (badge, link, or accent) is inferred from context; it may also be a social-icon color from a third-party widget
- Checkout flow styling (Shopify checkout) was not extractable; the `surface-card` and `hairline` tokens for checkout are assumed from the general palette
- No animation or transition durations were extractable from the live site
- Sub-brand or seasonal palette variations (e.g., holiday themes) are unknown
