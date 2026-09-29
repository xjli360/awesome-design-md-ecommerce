---
version: alpha
name: "SteelSeries"
source_url: "https://steelseries.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A gaming-peripheral brand that wraps its high-performance hardware in a deep, almost architectural purple — `#703cd3` — a primary that reads more like a pro-audio or design-tool accent than a typical esports red or neon cyan. The palette is deliberately restrained: `#383838` ink against a white canvas, with `#9a8be5` as a softer secondary purple that appears in hover states, badge fills, and product-card overlays. Typography defaults to the system stack — no custom brand font declared — which gives the interface a clean, utilitarian feel; the brand trusts its product photography and angular industrial design (the hex-patterned mouse shells, the OLED screens on keyboards) to carry the personality. Buttons are sharp-cornered rectangles (`{rounded.sm}`) with a solid purple fill, and the search bar follows the same rectilinear logic — no pill shapes, no soft orbs. The nav bar sits at 64px with a subtle bottom hairline, and product cards use a `{rounded.md}` corner that matches the chamfered edges of the hardware itself. The overall effect is a brand that presents its gear with the seriousness of a pro tool — the purple is the only concession to "gamer" aesthetics, and even that is applied with restraint.

colors:
  primary: "#703cd3"
  primary-active: "#5a2fb0"
  primary-disabled: "#b8a0e8"
  ink: "#383838"
  body: "#4a4a4a"
  muted: "#707070"
  muted-soft: "#a0a0a0"
  hairline: "#d0d0d0"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple-soft: "#9a8be5"
  accent-purple-light: "#c8bff0"
  badge-new: "#703cd3"
  badge-sale: "#e53935"
  rating-star: "#ffb300"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-icon-square:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.rating-star}"
    fontSize: 16px
    gap: "{spacing.xxs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 16px"
    height: 36px
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — Solid purple rectangle with white text, the primary call-to-action across the site. On hover, shifts to `{colors.primary-active}` (`#5a2fb0`). Disabled state uses `{colors.primary-disabled}` (`#b8a0e8`). Used for "Add to Cart", "Buy Now", and primary form submissions.

**`button-secondary`** — Outlined button with a white fill, `{colors.ink}` text, and a `{colors.hairline}` border. Hover state darkens the border to `{colors.ink}` and adds a `{colors.surface-soft}` background. Used for "Learn More", "Compare", and secondary actions.

**`button-tertiary-text`** — Text-only link styled as a button, using `{colors.primary}` for the text color. No background or border. Used for "View Details" and inline actions.

**`button-icon-square`** — 40x40px square icon button with a `{colors.surface-soft}` background and `{colors.ink}` icon. Used for cart, wishlist, and utility actions.

### Cards
**`product-card`** — White card with a `{rounded.md}` corner and a subtle `{colors.hairline-soft}` border. Contains a product image (4:3 aspect ratio, top-rounded), a title in `{typography.title-sm}`, and a price in bold `{typography.body-md}`. On hover, the border darkens to `{colors.hairline}` and a soft shadow lifts the card. Badges (`badge-new`, `badge-sale`) overlay the top-left corner of the image.

### Navigation
**`nav-bar`** — 64px white bar with a `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` (uppercase, 14px, weight 600). Active links are `{colors.primary}`, inactive links are `{colors.muted}`. The logo sits left-aligned, and utility icons (search, cart, account) sit right-aligned.

### Forms
**`text-input`** — Standard input field with a white background, `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}`. Error state uses `{colors.badge-sale}` (`#e53935`) for the border.

### Search
**`search-bar`** — A `{colors.surface-soft}` input with a `{colors.hairline-soft}` border and `{rounded.sm}` corners. On focus, the border becomes `{colors.primary}`. The search icon is `{colors.muted}`.

### Footer
**`footer`** — Full-width dark section with `{colors.ink}` background and white text. Links are `{colors.muted-soft}` and turn white on hover. Organized in columns with `{spacing.xxl}` padding and `{spacing.section}` top/bottom padding.

### Hero
**`hero-section`** — Dark section (`{colors.ink}` background) with white display text. The `hero-title` uses `{typography.display-xl}` (32px, weight 700) and the `hero-subtitle` uses `{typography.body-md}` in `{colors.muted-soft}`. Often paired with a large product image or video.

### Badges
**`badge-new`** — Small purple pill (`{colors.badge-new}`) with white uppercase text. Used to flag new product arrivals.
**`badge-sale`** — Small red pill (`{colors.badge-sale}`) with white uppercase text. Used for discount or sale items.

### Category Filters
**`category-filter`** — Small pill-shaped filter buttons (`{rounded.sm}`, 36px height) with a `{colors.surface-soft}` background and `{colors.muted}` text. Active state uses `{colors.primary}` background and white text. Used on product listing pages to filter by category (e.g., Mice, Keyboards, Headsets).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards go single-column; hero section reduces padding; category filters scroll horizontally |
| Tablet | 744–1128px | Nav bar shows condensed links; product cards in 2-column grid; hero section uses 50% image width |
| Desktop | 1128–1440px | Full nav bar; product cards in 3-column grid; hero section uses full-width image with text overlay |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; hero section uses larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px.
- Icon buttons are 40x40px minimum.
- Category filter pills are 36px tall with 16px horizontal padding.
- Nav links have 32px touch zones (padding + line-height).

### Collapsing Strategy
- Nav bar collapses to a hamburger menu on mobile (< 744px). The hamburger icon is a 40x40px `button-icon-square`.
- Product card grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Category filter strip scrolls horizontally on mobile with a fade-to-white gradient on the right edge.
- Footer columns stack vertically on mobile, with each column as a collapsible accordion.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and buttons were inferred from common patterns; exact transition durations and shadow values were not extractable.
- Error states (text-input-error, form validation) are assumed to use `#e53935` based on common ecommerce patterns; the actual error color was not found in the extracted palette.
- The brand's custom font (if any) was not declared in the extracted CSS; the system font stack is used as a fallback. SteelSeries may use a proprietary typeface for marketing materials that is not present on the product pages.
- Dark mode styling was not detected; the extracted palette assumes a light theme.
- Sub-brand or product-line-specific colors (e.g., Arctis, Apex, Rival) were not extractable from the general site CSS.
- The `#9a8be5` color appears in the extracted palette but its exact usage (hover states, secondary accents, or background overlays) is inferred from context.
- Rating star color (`#ffb300`) is a common default and may not be the brand's actual choice.
- The extracted colors are limited to three hex values; the full palette (including grays, whites, and blacks) was constructed to match the brand's apparent aesthetic but may not be pixel-perfect.
