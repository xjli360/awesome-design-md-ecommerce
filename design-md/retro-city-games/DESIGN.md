---
version: alpha
name: "Retro City Games"
source_url: "https://retrocitygames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, ink-heavy storefront where #0b1d3b and #000b41 form the atmospheric baseline — these are not accidental dark-mode leftovers but deliberate choices that frame the merchandise like a CRT bezel. The palette reads as a dimly lit game room: #2b333f for secondary surfaces, #1b1b1b for deep backgrounds, and #73859f as a desaturated steel-blue accent that appears on hover states and secondary text. The single voltage of warmth comes from #ad631a, a burnt-amber used sparingly for price tags and stock badges, and #ff7734, a brighter orange that punches through the gloom on sale indicators. The extracted hex list is noisy with checkout-widget blues (#006aff, #3374ff) and social-icon tones (#808cff, #7b88bc), but the brand's true signature is the navy-black foundation with amber accents — a palette that evokes late-night browsing in a physical game store. Typography runs Inter at modest weights with Arial/Helvetica fallbacks, suggesting a no-nonsense utilitarian approach that lets product photography (cartridges, consoles, box art) carry the emotional weight. Borders are thin and sharp at 1px in #4d4d4d, avoiding the soft pill shapes of modern e-commerce in favor of squared-off rectangles that recall cartridge edges and console vents. The search bar uses a subtle inset shadow on #262626 fields, and product cards stack on #141414 with #d6d6d6 text — the contrast is deliberate, not accidental, creating a browsing experience that feels like flipping through bins under fluorescent light.

colors:
  primary: "#ad631a"
  primary-active: "#8c4f14"
  primary-disabled: "#4d3a24"
  ink: "#d6d6d6"
  body: "#b3b3b3"
  muted: "#919191"
  muted-soft: "#707070"
  hairline: "#4d4d4d"
  hairline-soft: "#262626"
  canvas: "#1b1b1b"
  surface-soft: "#141414"
  surface-card: "#2b333f"
  on-primary: "#ffffff"
  accent-amber: "#ff7734"
  accent-red: "#d92b2b"
  accent-green: "#1cc42f"
  badge-sale: "#ff7734"
  badge-new: "#ad631a"
  badge-sold-out: "#a12712"
  link-blue: "#73859f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-accent-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  icon-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 400px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline-soft}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 36px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 36px
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using a burnt-amber `{colors.primary}` fill on `{colors.canvas}` backgrounds. Text sits in white `{colors.on-primary}` at 14px/600 weight with 4px corner rounding. On hover, the fill deepens to `{colors.primary-active}` (#8c4f14); disabled state drops to a muted brown `{colors.primary-disabled}` with `{colors.muted}` text. Height is 44px with 12px/24px padding for comfortable thumb targeting.

**`button-secondary`** — A surface-level button using `{colors.surface-card}` (#2b333f) as background with `{colors.ink}` (#d6d6d6) text. Matches the primary button's 44px height and 4px rounding but carries a 1px `{colors.hairline}` border for definition against dark canvases. Used for "Add to Wishlist" and secondary checkout actions.

**`button-accent-sale`** — High-visibility orange button using `{colors.accent-amber}` (#ff7734) as fill with dark `{colors.canvas}` text. Reserved exclusively for sale-related CTAs ("Buy Now — 30% Off") where urgency needs to cut through the dark interface. Same 44px height and 4px rounding as primary.

**`button-tertiary`** — A text-only link-style button with no background, using `{colors.link-blue}` (#73859f) for the text. Hover adds a subtle underline. Used for "View Details" and "See More" actions within product cards and category listings.

### Cards
**`product-card`** — The core inventory unit, a `{colors.surface-card}` (#2b333f) rectangle with 8px corner rounding and 16px internal padding. The product image area sits at the top with `{rounded.sm}` (4px) bottom corners only, displaying the cartridge or console on a `{colors.surface-soft}` (#141414) background. Title uses `{typography.title-sm}` at 14px/600 weight in `{colors.ink}`, price uses `{typography.price-sm}` at 16px/700 weight in `{colors.primary}`. Badges overlay the top-left of the image area with 2px corner rounding.

### Navigation
**`nav-bar`** — A fixed 60px header on `{colors.canvas}` (#1b1b1b) with a 1px `{colors.hairline-soft}` (#262626) bottom border. Navigation links use `{typography.nav-link}` at 14px/600 weight; active state shifts text to `{colors.primary}` (#ad631a), inactive sits in `{colors.muted}` (#919191). The logo (typically "RETRO CITY GAMES" in `{typography.title-lg}`) anchors the left side with the search bar occupying the center.

**`category-chip`** — Pill-shaped filter chips at 36px height with 16px horizontal padding. Default state is `{colors.surface-card}` background with `{colors.muted}` text; active state flips to `{colors.primary}` fill with white text. Used for console generation filters (NES, SNES, Genesis, etc.) and genre tags.

### Forms
**`text-input`** — Dark input fields on `{colors.surface-soft}` (#141414) with 1px `{colors.hairline}` (#4d4d4d) border and 4px corner rounding. Text sits at 14px/400 weight in `{colors.ink}`. Focus state swaps the border to `{colors.primary}` (#ad631a) with no glow — the brand avoids soft shadows in favor of crisp lines. Height is 44px with 10px/16px padding.

**`search-bar`** — A slightly elevated search field using `{colors.surface-card}` (#2b333f) background with 8px corner rounding and a 1px `{colors.hairline}` border. The 48px height accommodates a search icon on the left and a clear button on the right. Placeholder text uses `{colors.muted}` (#919191). On focus, the border shifts to `{colors.primary}`.

### Badges
**`badge-stock`** — Green indicator using `{colors.accent-green}` (#1cc42f) background with dark text. 2px corner rounding, 2px/8px padding, 11px/700 weight uppercase type. Used for "In Stock" labels.

**`badge-sale`** — Orange urgency badge using `{colors.badge-sale}` (#ff7734) background with dark text. Same dimensions as stock badge. Used for "Sale" and "Clearance" labels.

**`badge-sold-out`** — Deep red badge using `{colors.badge-sold-out}` (#a12712) background with `{colors.ink}` text. Used for "Sold Out" labels on unavailable items.

**`badge-new`** — Amber badge using `{colors.badge-new}` (#ad631a) background with white text. Used for "New Arrival" labels on recently listed items.

### Footer
**`footer`** — A full-width section on `{colors.canvas}` (#1b1b1b) with a 1px `{colors.hairline-soft}` (#262626) top border. Links use `{colors.link-blue}` (#73859f) at 14px/500 weight, while static text (copyright, address) uses `{colors.muted}` (#919191) at 12px/400 weight. Internal padding is 64px top/bottom with 24px sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), hamburger nav replaces full nav bar, search bar collapses to icon-only, category chips scroll horizontally, hero banner reduces to 240px height, footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid (2 cards wide), nav bar shows 4-5 primary links, search bar remains full-width but compresses, category chips show in a 2-row grid, hero banner at 320px height |
| Desktop | 1128–1440px | Three-column product grid (3 cards wide), full nav bar with all links visible, search bar at 480px max-width, category chips in a single row, hero banner at 400px height |
| Wide | > 1440px | Four-column product grid (4 cards wide), max-width container at 1440px centered, nav bar and search bar scale proportionally, category chips expand to fill available width, hero banner at 480px height |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain minimum 44px height for touch compliance
- Icon buttons are 40x40px with 8px corner rounding
- Category chips are 36px height with 16px horizontal padding — slightly below 44px but acceptable for horizontal scrolling strips
- Product card tap targets (title, price, image) are each minimum 48px tall within the card
- Pagination buttons are 36x36px with 8px padding between them

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px — the logo and cart icon remain visible
- Search bar collapses to a magnifying glass icon on mobile; tapping expands it to full-width overlay
- Product grid collapses from 4 columns (wide) to 1 column (mobile) with 16px gutters
- Category filter chips collapse from a single row to a horizontal scrollable strip on mobile
- Footer link columns stack vertically on mobile, with each section expanding/collapsing via accordion
- Hero banner text overlay collapses to a single line on mobile, hiding the subtitle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted — only `button-primary` and `text-input` have confirmed hover/focus colors
- Error states for forms (validation messages, error borders) are absent from the extracted data
- Dark mode is the default and only mode observed — no light mode palette exists in the extraction
- The extracted hex list is noisy with checkout-widget blues (#006aff, #3374ff), social-icon tones (#808cff, #7b88bc), and stock-image dominant colors — the true brand palette was inferred by frequency analysis and contextual judgment
- Font weights beyond 400, 500, 600, and 700 are unconfirmed — Inter variable font may support intermediate weights
- Letter-spacing values for body text and captions are estimated based on common Inter usage patterns
- The `#f8f8f8` and `#f2f2f2` values in the extraction may represent legacy light-mode remnants or checkout surfaces — not used in the primary palette
- No animation or transition timing data (hover fade durations, card lift effects) could be extracted
- Sub-brand or seasonal palette variations (holiday themes, special edition drops) are unknown
- The `#251212` deep maroon in the extraction may be a secondary accent or stock-image artifact — not assigned a token without confirmation
- No data on focus-visible ring styles or keyboard navigation indicators
- Shopify integration status is unconfirmed (platform-shopify: False may indicate custom e-commerce or a different platform)
