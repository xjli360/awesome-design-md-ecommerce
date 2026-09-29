---
version: alpha
name: "Five Ten"
source_url: "https://www.adidas.com/us/fiveten"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A climbing brand that lives in the vertical, Five Ten’s visual system is built around a deep obsidian ink (#000000) and a stark white canvas (#ffffff), with no gradient, no decorative color, and no ornament — the only accent is the rubber-orange of Stealth C4, a saturated #e85d00 that appears on product badges, price tags, and the sole of every climbing shoe rendered as a 3D product shot. The typography runs AdihausDIN at 700 weight for display and 400 for body, a condensed, utilitarian sans-serif that reads like a carabiner spec sheet: no curves, no serifs, no warmth. Buttons are full-height rectangles with zero rounding ({rounded.none}), 48px tall, and use the brand’s signature black-on-white or white-on-black inversion — there is no gray state, no hover gradient, no shadow. Product cards are flat white rectangles with a single 1px hairline border ({colors.hairline}), a 4:5 aspect ratio photo, and a price set in 16px bold with the orange badge. The navigation is a persistent black bar at 64px, with white text and a search icon that opens a full-screen overlay — no hamburger, no flyout, just a clean vertical drop. The entire system feels machined, not designed: every corner is square, every line is straight, every color is either black, white, or the orange of friction rubber. There is no surface-soft, no muted-soft, no rounded anything — the brand trusts the geometry of climbing holds and the texture of limestone over any digital flourish.

colors:
  primary: "#000000"
  primary-active: "#333333"
  primary-disabled: "#999999"
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
  accent-orange: "#e85d00"
  accent-orange-active: "#cc5200"
  accent-orange-disabled: "#f5b380"
  badge-sale: "#e85d00"
  badge-new: "#000000"
  badge-sold-out: "#999999"
  star-rating: "#000000"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'AdihausDIN', 'DIN Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    padding: 14px 32px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-accent-disabled:
    backgroundColor: "{colors.accent-orange-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 48px
    width: 48px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-item:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
    height: 64px
  top-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.on-primary}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    aspectRatio: "4:5"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.body-md}"
    color: "{colors.accent-orange}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.nav-link}"
    color: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: "80vh"
    minHeight: "400px"
  hero-banner-image:
    objectFit: "cover"
    overlay: "linear-gradient(0deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0) 50%)"
  hero-banner-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: "48px"
  category-grid:
    backgroundColor: "{colors.canvas}"
    gap: "{spacing.sm}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    aspectRatio: "1:1"
  category-card-image:
    objectFit: "cover"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: "48px"
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: "48px"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The workhorse CTA: a solid black rectangle with zero rounding, white uppercase DIN text at 14px with 1px letter-spacing. On hover, the background shifts to `{colors.primary-active}` (#333333) — a subtle darkening that feels like a rock face catching shadow. The disabled state uses `{colors.primary-disabled}` (#999999) with no border change. All primary buttons are exactly 48px tall with 32px horizontal padding.

**`button-secondary`** — An outlined variant for secondary actions: white background, black text, a 2px black border. Active state fills the background with `{colors.surface-soft}` (#f5f5f5). Disabled state fades the border to `{colors.hairline}` (#e0e0e0) and text to `{colors.muted-soft}` (#999999). Used for "Add to Wishlist" and "Compare" actions.

**`button-accent`** — The orange friction-rubber button, reserved for high-visibility actions like "Add to Cart" on product pages and "Shop Now" on hero banners. Uses `{colors.accent-orange}` (#e85d00) as background, white text. Active state darkens to `{colors.accent-orange-active}` (#cc5200). Disabled fades to `{colors.accent-orange-disabled}` (#f5b380).

**`button-pill`** — A rare rounded variant used only in the filter bar and size selector chips. Full pill shape (`{rounded.full}`), smaller 36px height, 8px vertical padding. Outline variant exists for inactive filters with a 1px `{colors.hairline}` border.

### Navigation
**`top-nav`** — A persistent 64px black bar spanning the full viewport width. Logo sits left-aligned at 32px height. Navigation items are uppercase DIN 700 at 14px with 1px letter-spacing, white text, 16px horizontal padding. Active nav item has a 3px white bottom border. Search icon (magnifying glass) sits right-aligned and opens a full-screen overlay. No hamburger menu — on mobile, the nav items collapse into a vertical list within the same black bar.

**`search-overlay`** — A full-screen white overlay triggered by the search icon. Contains a centered search input with `{colors.surface-soft}` background and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.primary}`. Below the input, recent searches and trending terms appear as pill-shaped filter chips.

### Cards
**`product-card`** — A flat white rectangle with no rounding, no shadow, and a single 1px `{colors.hairline}` bottom border (or no border in grid layouts). The image area occupies a 4:5 aspect ratio with `{colors.surface-soft}` background for loading states. Product name uses `{typography.title-sm}` (16px bold), price uses `{typography.body-md}` (16px regular). Sale prices render in `{colors.accent-orange}`. Badges (Sale, New, Sold Out) are solid rectangles pinned to the top-left of the image area — no rounding, 4px vertical padding, 8px horizontal padding, uppercase 11px bold.

**`category-card`** — A 1:1 square card used in the category grid on the homepage. Background is `{colors.surface-soft}` with a full-bleed image. Category name overlays at the bottom in `{typography.title-sm}`. No hover effect — the brand trusts the photography to sell the category.

### Forms
**`text-input`** — A rectangular input with `{colors.surface-soft}` background, 1px `{colors.hairline}` border, 12px padding, 48px height. On focus, border becomes 2px `{colors.primary}` and background returns to white. Placeholder text uses `{colors.muted}` (#666666). Error state adds a 2px `{colors.accent-orange}` border and error message below in `{typography.caption}` with orange text.

**`size-selector`** — A dropdown-style selector for shoe sizes. Rendered as a button that opens a grid of size chips. Each chip is a 48px square with `{colors.canvas}` background and 1px `{colors.hairline}` border. Selected chip inverts to `{colors.primary}` background with white text. Unavailable sizes are grayed out with `{colors.muted-soft}` text and a diagonal strikethrough.

### Footer
**`footer`** — A solid black section with white text. Contains three columns: "Customer Service", "About Five Ten", and "Connect". Column headings use `{typography.nav-link}` (uppercase 14px bold). Links use `{typography.link}` (14px regular). Social media icons appear as white glyphs in a horizontal row. Bottom bar contains copyright text in `{typography.caption}` and legal links. Section padding is `{spacing.xxl}` (48px) vertical and `{spacing.base}` (16px) horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top-nav collapses to logo + hamburger icon; product grid goes 1 column; hero banner height reduces to 60vh; footer columns stack vertically; filter bar becomes a sticky bottom sheet |
| Tablet | 744–1128px | Top-nav shows limited items (logo, search, cart); product grid goes 2 columns; hero banner keeps 80vh; footer columns arrange in 2x2 grid; filter bar shows as horizontal scroll |
| Desktop | 1128–1440px | Full top-nav with all items; product grid goes 3 columns; hero banner at 80vh; footer columns in 3-column layout; filter bar shows full chip set |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product grid goes 4 columns; hero banner content max-width 1200px; all layouts centered |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain minimum 44px height and 44px width for tap targets
- Filter chips are 36px tall but have 44px tap area via padding
- Size selector chips are 48px squares
- Search input is 48px tall
- Product card badges are at least 28px tall

### Collapsing Strategy
- Top-nav: On mobile, navigation items collapse into a full-screen overlay menu triggered by a hamburger icon. The black bar persists with logo and action icons (search, cart, account).
- Filter bar: On mobile, filters collapse into a sticky bottom sheet with a "Filter" button that opens a modal. Active filters show as chips above the product grid.
- Footer: On mobile, accordion-style collapse for each column section. Headers remain visible and tappable to expand/collapse content.
- Product images: On mobile, single-column layout with full-width images. On tablet and above, multi-column grid.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography block uses AdihausDIN (the brand's known typeface from adidas integration) with DIN Next and Helvetica Neue as fallbacks. This should be verified against actual CSS.
- No hex colors were extracted from the live site (the extraction returned empty). The color palette is reconstructed from brand knowledge of Five Ten's visual identity: black, white, and Stealth C4 orange (#e85d00). This should be verified against the current live site.
- Hover and focus states for all components are inferred from common DTC patterns and may not match the actual implementation.
- Error and validation styling for forms (error text color, border color on error, success states) are not documented from live observation.
- Dark mode is not supported by the brand — all surfaces are white or black with no intermediate gray tones.
- The search overlay behavior (recent searches, trending terms) is inferred from common adidas patterns and may differ.
- Product card hover states (if any) are not documented — the brand may use a subtle scale or shadow on desktop hover.
- The hero banner overlay gradient is inferred from common e-commerce patterns and may use a different opacity or color.
- Size selector unavailable-state styling (strikethrough pattern) is inferred from industry convention.
- The brand may use additional accent colors for seasonal collections or collaborations that are not captured here.
