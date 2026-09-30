---
version: alpha
name: "Blue Note Shop"
source_url: "https://www.bluenote.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue anchor at #0b427a — the color of a midnight session in a basement club — sets the emotional temperature for Blue Note Shop, while a sharper cyan accent at #2098d1 provides the voltage that pulls the eye to add-to-cart buttons, sale badges, and the search icon. The palette is overwhelmingly monochrome: #262626 for ink, #1a1a1a for near-black surfaces, #4d4d4d and #949494 for muted text, and a stack of grays (#e1e1e1, #d9d9d9, #f0f0f0) that build clean card hierarchies without competing with album art. The typography system relies on HelveticaNeueLTStd-BdEx for display moments — a condensed, authoritative bold that echoes the iconic Blue Note logo — and HelveticaNeueLTStd-LtEx for lighter headlines, while Open Sans handles body copy with a more neutral, readable cadence. Buttons are sharp-cornered rectangles (`{rounded.none}`) or softly rounded (`{rounded.sm}`), never pill-shaped; the brand trusts rectangular geometry to communicate precision and heritage. Product cards use `{rounded.xs}` (4px) — a subtle nod that says "we care about edges" without softening the grid. The shop feels like a record crate: dense, browsable, with high information density and a restrained color story that lets the album covers — Blue Note's true visual system — do all the emotional work.

colors:
  primary: "#0b427a"
  primary-active: "#003388"
  primary-disabled: "#aaaaaa"
  ink: "#262626"
  body: "#4d4d4d"
  muted: "#949494"
  muted-soft: "#aaaaaa"
  hairline: "#d9d9d9"
  hairline-soft: "#e1e1e1"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#2098d1"
  accent-red: "#fa4d5a"
  accent-gold: "#ff9900"
  accent-green: "#00d084"
  badge-sale: "#fa4d5a"
  badge-new: "#2098d1"
  star-rating: "#ff9900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'HelveticaNeueLTStd-LtEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'HelveticaNeueLTStd-BdEx', 'Helvetica Neue', Helvetica, Arial, sans-serif"
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-cyan}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 44px
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  category-tab-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — A sharp-cornered rectangle in deep blue `{colors.primary}` with white uppercase text. Used for primary checkout and add-to-cart actions. On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with no border change. **`button-secondary`** — White canvas background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Used for secondary actions like "View Details" or "Cancel". **`button-accent-cyan`** — Cyan `{colors.accent-cyan}` background for promotional CTAs and featured actions. **`button-accent-red`** — Red `{colors.accent-red}` background reserved for clearance or urgency actions. All buttons use `{rounded.none}` and `{typography.button-md}` (14px uppercase bold).

### Cards
**`product-card`** — A white card with `{rounded.xs}` (4px) corners and no shadow — the brand relies on `{colors.hairline}` borders for separation. The image sits flush to the top with `{rounded.xs}` corners. Title uses `{typography.title-sm}` (14px bold condensed), price uses `{typography.price}` (16px bold condensed). Badges (`badge-sale`, `badge-new`) overlay the top-left of the image with `{rounded.none}` and uppercase 11px text.

### Navigation
**`nav-bar`** — A 72px white bar with `{colors.ink}` text in `{typography.nav-link}` (13px uppercase bold condensed). Active links get a 2px `{colors.primary}` bottom border. The nav includes a logo (typically the Blue Note wordmark), category links, and a search icon. On mobile, the nav collapses to a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — A white rectangle with `{rounded.none}`, 1px `{colors.hairline}` border, and `{typography.body-md}`. On focus, the border becomes 2px `{colors.accent-cyan}`. Used for email signups, search queries, and checkout fields. **`filter-dropdown`** — Same shape as text-input but 40px tall, used for sorting and filtering product lists. **`quantity-selector`** — A compact 40px input with `{rounded.none}` and hairline border, used in cart and product detail pages.

### Footer
**`footer`** — A dark `{colors.ink}` section with white text. Links use `{colors.muted-soft}` and `{typography.link}` (14px Open Sans, underlined). Organized in columns for About, Help, and Social links. Padding is `{spacing.xxl}` vertical, `{spacing.lg}` horizontal.

### Hero
**`hero-section`** — A full-width dark `{colors.ink}` section with white `{typography.display-xl}` (36px bold condensed) headline. The `hero-cta` button uses `{colors.accent-cyan}` with white uppercase text. The hero may feature a featured album or artist as background imagery, with the text overlaid.

### Badges
**`badge-sale`** — Red `{colors.badge-sale}` background, white uppercase 11px bold text, `{rounded.none}`. **`badge-new`** — Cyan `{colors.badge-new}` background, same typography. Both sit at the top-left of product card images with 2px horizontal padding.

### Pagination
**`pagination-button`** — White canvas with `{colors.ink}` text, `{rounded.none}`, 36px tall. Active page uses `{colors.primary}` background with white text. Used at the bottom of product listing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger, hero text reduces to `{typography.display-md}`, footer stacks vertically, search bar moves to top of page |
| Tablet | 744–1128px | Two-column product grid (2 col), nav shows category links but no sub-navigation, hero uses `{typography.display-lg}`, filter dropdowns become horizontal scroll |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav with all links, hero at full `{typography.display-xl}`, sidebar filters visible |
| Wide | > 1440px | Four-column product grid (4 col), max-width container at 1440px, hero full-width with max-width content |

### Touch Targets
- All buttons and interactive elements: minimum 44px height
- Nav links: minimum 44px tap area (even if text is smaller)
- Product card tap target: entire card is clickable
- Filter dropdowns: 40px height, minimum 44px on mobile
- Quantity selector buttons: 44px x 44px on mobile

### Collapsing Strategy
- Nav bar: collapses to hamburger menu below 744px; slide-out drawer replaces horizontal links
- Product grid: reduces columns from 4 to 1 as viewport shrinks
- Footer: 4-column layout collapses to 2 columns at tablet, 1 column at mobile
- Hero: full-width background remains, but text padding reduces at mobile
- Search bar: moves from nav to a dedicated top bar on mobile
- Filter sidebar: becomes a horizontal scroll strip on tablet, a dropdown on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links beyond primary-active (secondary hover, accent hover) could not be reliably extracted — assumed to use a darker shade of the background color or a border change
- Error styling for form inputs (red border, error message typography) not observed in extracted data
- Dark mode variant not present on the live site
- Sub-brand or collection-specific palettes (e.g., Blue Note Re:imagined, Blue Note 80) not captured
- Loading states and skeleton screen patterns not extracted
- Modal/dialog styling (overlay opacity, close button, padding) not observed
- Dropdown menu styling (sub-nav, mega-menu) not present in extracted data
- The extracted hex list includes many generic blues (#0693e3, #0757fe, #0a7aff, #4280ff, #1778f2) that are likely social-icon colors or framework defaults — the brand's true primary is #0b427a, with #2098d1 as the accent cyan
- Font stack for body text assumes Open Sans as the primary readable face, but HelveticaNeueLTStd-LtEx may also appear in body contexts — exact pairing not confirmed
- Animation durations and easing curves not extracted
- Focus-visible ring styling not observed
- Checkout-specific components (shipping form, payment form) not captured
