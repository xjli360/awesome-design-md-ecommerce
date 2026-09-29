---
version: alpha
name: "Easy Street Records"
source_url: "https://easystreetonline.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store that treats the physical artifact with reverence, Easy Street Online wraps its inventory in a clean, uncluttered white canvas (#ffffff) where album art does the heavy lifting. The site trusts Arial at its most utilitarian — no display typeface competes with the record sleeves, no decorative font pretends to be cool. Buttons carry a subtle 8px rounding (`{rounded.sm}`) that feels intentional without being cute, and the primary action color — whatever distinctive accent the store chooses — would anchor every "Add to Cart" and checkout trigger. The mood is that of a well-organized crate: everything has its place, the lighting is even, and the only drama comes from the music itself. Product cards use generous whitespace and soft dividers (`{colors.hairline}`) to let vinyl jackets breathe, while the navigation stays out of the way — a simple top bar with search, cart, and category links. This is a system built for the person who knows what they want and wants to find it fast, not for the browser who needs to be seduced by animations.

colors:
  primary: "#000000"
  primary-active: "#333333"
  primary-disabled: "#cccccc"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#d4af37"
  sale-badge: "#cc0000"
  sold-out: "#999999"
  vinyl-color: "#111111"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 8px 0px
    height: auto
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.sale-badge}"
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
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: 4px 0px
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 4px 0px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0px"
    borderBottom: "1px solid {colors.hairline-soft}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  genre-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    border: "1px solid {colors.hairline}"
  genre-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0px"
  breadcrumb-current:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0px"
  pagination-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Sign Up" flows. Solid black fill with white uppercase text at 14px/600. Hover shifts to `{colors.primary-active}` (#333333) for a subtle darkening effect; disabled state uses `{colors.primary-disabled}` (#cccccc). The 8px rounding (`{rounded.sm}`) keeps it modern without being playful. 44px height meets touch-target minimums.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Continue Shopping". White fill with a 2px black border. Hover inverts to a soft gray fill (`{colors.surface-soft}`) while keeping the border. Same 44px height and uppercase typography as primary for visual consistency.

**`button-text`** — A borderless, backgroundless link-style button for tertiary actions like "Clear Filters" or "Cancel". Uses `{typography.link}` at 14px/400 for a lighter weight that visually defers to surrounding content. No height constraint — it flows inline with text.

### Cards
**`product-card`** — The core inventory display unit, built as a clean rectangle with zero rounding. The album cover image fills a 1:1 aspect ratio square on a soft gray background (`{colors.surface-soft}`) for loading states. Below the image, the title sits in 16px/400, the artist name in 14px/400 muted, and the price in 16px/600. Sale items get a small red badge (`{colors.sale-badge}`) pinned to the top-left of the image area. No shadows, no borders — the card relies entirely on the album art for visual interest.

### Navigation
**`nav-bar`** — A 64px white bar with a single bottom hairline divider. Links use uppercase 14px/600 with 16px horizontal padding. The active state is indicated by a 2px bottom border on the link itself — no pill backgrounds, no underlines on hover. The search bar lives in the nav as a pill-shaped input with soft gray fill (`{colors.surface-soft}`) that expands on focus.

### Forms
**`text-input`** — Standard form input with a 1px hairline border and 12px/16px padding. On focus, the border thickens to 2px black — no glow, no colored accent. Error state swaps to a 2px red border (`{colors.sale-badge}`). Height is 48px for comfortable typing.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) with soft gray background and 10px/20px padding. The rounded shape distinguishes it from standard text inputs and signals its role as a discovery tool. On focus, the background stays white and the border becomes 2px black.

### Footer
**`footer`** — A soft gray section (`{colors.surface-soft}`) with muted text at 14px/400. Links are stacked vertically with 4px padding and no underlines until hover, where they shift to black. The top edge is marked by a 1px hairline. Padding is generous at 48px top/bottom to give the page a grounded finish.

### Tags & Filters
**`genre-tag`** — Small pill-shaped labels for filtering by music genre. Default state is a soft gray fill with muted text and a hairline border. Active state flips to solid black fill with white text. The 4px/12px padding keeps them compact enough to stack in a horizontal scrollable strip.

**`breadcrumb`** — Simple text-based navigation path using `{typography.caption}` at 12px. Current page is rendered in black; all other segments in muted. No chevron separators — just spacing and color to indicate hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), nav collapses to hamburger menu, search bar moves below nav, genre tags scroll horizontally, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, search bar remains in nav, sidebar filters appear on category pages |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, persistent search bar, sidebar filters always visible, breadcrumb trail shown |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centers content, additional whitespace on sides, larger hero section |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Product card tap targets are the full card area, not just text
- Genre tags are minimum 32px tall for easy tapping
- Nav links have 16px horizontal padding to prevent accidental taps
- Cart quantity selector has 40px height with 12px padding

### Collapsing Strategy
- Primary nav links collapse into a hamburger menu below 744px
- Sidebar filters collapse into a "Filter" button that opens a modal/overlay on mobile
- Product grid reduces from 4 columns to 1 column on the smallest screens
- Search bar moves from inline nav position to a full-width element below the nav on mobile
- Footer link columns stack vertically on mobile rather than sitting side-by-side
- Genre tag strip becomes horizontally scrollable with a fade indicator on the right edge

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site — the palette above is a reasonable default for a black-and-white record store aesthetic, but the actual brand accent color (if any) could not be determined
- Font-family declarations returned only "Arial" — the site may use additional typefaces for display headings or brand elements that weren't captured
- No meta theme-color was found, so browser chrome styling is unknown
- Hover and focus states for most components are inferred from common patterns rather than extracted from the live site
- Error states for forms (validation messages, error icons) are not documented
- The checkout flow (multi-step vs. single-page, payment form styling) could not be analyzed
- Dark mode or high-contrast mode preferences are not captured
- Loading states, skeleton screens, and empty states are not documented
- The site may use icons or symbols (shopping cart, search, menu) that aren't specified here
- Animation and transition timings (hover fades, page transitions) are not extracted
- The actual brand accent color (gold, red, or another distinctive hue) could not be confirmed from the extracted data — the `accent` and `sale-badge` values are educated guesses based on common record store conventions
