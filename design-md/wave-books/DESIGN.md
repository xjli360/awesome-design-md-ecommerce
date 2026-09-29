---
version: alpha
name: "Wave Books"
source_url: "https://www.wavepoetry.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A poetry publisher whose visual identity is built on the tension between a deep, almost-black ink (#0c0c0c) and a cool, atmospheric slate blue (#7796a8) that reads like a winter sky over a Pacific Northwest harbor. The site uses a near-white canvas (#f3f3f3) rather than pure white, giving the reading surface a soft, paper-like warmth that distinguishes it from the sterile white of commercial publishing. Assistant, a clean geometric sans, carries the body text at modest sizes, while Open Sans Condensed appears in navigation and section headers, its condensed letterforms creating a dense, bookish rhythm. The palette is restrained — grays from #121212 through #767676 to #dedede — with a single unexpected jolt of cobalt (#334fb4) used sparingly for links and accent elements, a color that recalls the blue of a poet's ink cartridge or the spine of a library book. Product cards use generous whitespace and minimal borders, letting the cover art and typography do the work. The checkout flow, powered by Shopify, introduces a separate visual system with payment-widget blues and greens, but the core site maintains its monochrome-plus-cobalt discipline. This is a brand that trusts its content — the poetry — to provide the color, and designs the container to be quiet, serious, and slightly cool.

colors:
  primary: "#7796a8"
  primary-active: "#5c7a8c"
  primary-disabled: "#c4d4de"
  ink: "#0c0c0c"
  body: "#121212"
  muted: "#767676"
  muted-soft: "#8f9cb5"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f3f3f3"
  surface-soft: "#eeeeee"
  surface-card: "#f1f0f0"
  on-primary: "#ffffff"
  accent-blue: "#334fb4"
  accent-blue-hover: "#2a3f8f"

typography:
  display-xl:
    fontFamily: "'Open Sans Condensed', 'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans Condensed', 'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
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
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans Condensed', 'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
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
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.link}"
    padding: 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    borderColor: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 8px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and key checkout flows. Rendered on the cool slate blue (#7796a8) with white text, with a subtle 8px rounding. On hover, the background deepens to `{colors.primary-active}` (#5c7a8c). The disabled state uses `{colors.primary-disabled}` (#c4d4de), a washed-out version of the primary. **`button-secondary`** — An outlined or ghost variant on the warm canvas background, with dark ink text. Used for secondary actions like "View Details" or "Learn More". **`button-text-link`** — A text-only button styled as a link, using the cobalt accent (#334fb4) for inline actions within product descriptions or editorial content.

### Cards
**`product-card`** — The core inventory unit for displaying poetry books. Uses a near-white surface (`{colors.surface-card}`) with soft 8px rounding. The card contains a product image with matching rounding, a title in `{typography.title-md}`, and a price in `{typography.body-md}` set in the muted gray. No border or shadow — the card relies on the contrast between `{colors.surface-card}` and the `{colors.canvas}` background for separation. **`product-card-image`** — The book cover image, cropped with `object-fit: contain` to preserve the cover's aspect ratio without distortion.

### Navigation
**`nav-bar`** — A fixed 64px header on the warm canvas background. Navigation links use Open Sans Condensed in uppercase with 0.8px letter-spacing, creating a dense, editorial feel. The nav bar contains the Wave Books logo, primary section links, and a search icon. On mobile, the nav collapses into a hamburger menu. **`footer`** — A dark footer on the near-black ink (#0c0c0c) with white text and muted-soft (#8f9cb5) links. Contains copyright, social links, and newsletter signup.

### Forms
**`text-input`** — Standard input fields for search, newsletter signup, and checkout forms. Uses the surface-card background with a hairline border (#dedede). On focus, the border shifts to the primary slate blue. **`search-bar`** — A pill-shaped search input with full rounding, used in the header and on search result pages. Uses the same surface-card background with a hairline border.

### Badges
**`badge`** — Small, tightly padded labels using the cobalt accent (#334fb4) with white text. Used for "New", "Signed Edition", or "Staff Pick" indicators on product cards. The 4px rounding and compact padding (2px 8px) keep them unobtrusive.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 24px; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero section uses 28px display text; search bar in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero section uses 32px display text; search bar in nav |
| Wide | > 1440px | Max-width container at 1440px; three-column grid with increased whitespace; hero section centered with 36px display text |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Search bar and text inputs have 44px height
- Nav bar links have 48px touch targets
- Product card tap targets cover the full card area

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid collapses from three columns to two at tablet, to one at mobile
- Footer links collapse from three columns to two at tablet, to single column at mobile
- Hero section reduces font size and padding at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes several Shopify checkout widget colors (likely blues and greens from payment buttons) that could not be reliably filtered out — the true brand palette may be even more restrained than what's listed here
- Font sizes and line heights for body and display text are inferred from common Assistant and Open Sans Condensed usage patterns; actual site values may vary
- Hover states for secondary buttons, text inputs, and navigation links could not be extracted
- Error states for forms (validation colors, error messages) are not present in the extracted data
- Dark mode is not supported on the live site
- The accent blue (#334fb4) usage pattern (links vs. badges vs. other elements) is inferred from common design patterns, not extracted
- Product card spacing and padding values are estimated based on typical e-commerce layouts
- The footer's exact link structure and newsletter signup form styling could not be extracted
- No extracted data for modal dialogs, dropdown menus, or tooltip styling
- The site uses Shopify's default checkout flow, which has its own design system separate from the brand's core site
