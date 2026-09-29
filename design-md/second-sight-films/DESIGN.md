---
version: alpha
name: "Second Sight Films"
source_url: "https://secondsightfilms.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, cinematic red #aa1c07 — the meta-theme-color and the brand's primary voltage — anchors a site that feels like a collector's edition Blu-ray slipped from its slipcase. The palette is a study in contrast: near-black #231f20 and #1d1c1c form the ink and body text, while a cool, archival blue #006fcf surfaces for links and secondary accents, pulling the eye toward pre-order buttons and film-detail CTAs. The extracted hex list reveals a surprising density of warm oranges (#f48120, #f58720, #f79a20) and a single, sharp yellow (#ffd800) — these are not decorative; they are the brand's badge and price-sticker language, used sparingly to signal "limited edition" or "sale" without breaking the restrained, boutique tone. Cards and containers sit on a clean white canvas (#ffffff) with soft hairlines (#dedede, #ebebeb), letting the film posters — often dark, high-contrast imagery — dominate. There are no hard edges: buttons use a moderate {rounded.sm}, while larger promotional panels and search fields take {rounded.md} to soften the interface. The typography is absent from extracted hints, so a neutral, highly-legible system font stack is assumed — the kind that steps back and lets the cover art and the deep red CTA do the talking. The overall mood is that of a serious, passionate film archive: respectful of the source material, unafraid of darkness, and precise with its accents.

colors:
  primary: "#aa1c07"
  primary-active: "#791405"
  primary-disabled: "#ea5353"
  ink: "#231f20"
  body: "#1d1c1c"
  muted: "#444444"
  muted-soft: "#637381"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#006fcf"
  accent-blue-active: "#005ab9"
  accent-orange: "#f48120"
  accent-yellow: "#ffd800"
  badge-sale: "#f48120"
  badge-limited: "#aa1c07"
  star-rating: "#fba900"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
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
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-blue-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "12px 16px"
    height: 48px
  search-bar-focus:
    border: "1px solid {colors.accent-blue}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.link}"
  hero-panel:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, saturated in the brand's deep red `#aa1c07`. Used for "Pre-order", "Add to Cart", and "Subscribe". On hover, it deepens to `#791405`. The disabled state fades to a muted pink `#ea5353`. All primary buttons use uppercase, 14px/600 weight type with 0.3px letter spacing for a sharp, authoritative tone.

**`button-secondary`** — An outlined variant on a white canvas with a 1px hairline border. Used for "View Details" or "Learn More" actions that should not compete with the primary. The text remains in near-black `#231f20`. Hover state introduces a subtle shadow or border darkening (not extracted, noted in gaps).

**`button-accent-blue`** — A secondary accent button in the brand's cool blue `#006fcf`, used for "Shop All" or "Browse Collection" links within content sections. Active state shifts to `#005ab9`. This button provides a visual alternative to the dominant red, useful for differentiating action types on the same page.

**`button-pill-orange`** — A small, fully rounded pill in `#f48120` for promotional or sale-related actions like "Shop Sale". Uses smaller uppercase type (12px) and compact padding. This is a high-energy, limited-use component reserved for clearance or flash events.

### Cards
**`product-card`** — The primary unit for displaying a film title. A white card with a soft border and `{rounded.sm}` corners. The image occupies the top with matching top-radius corners. Below, the title sits in `{typography.title-sm}` with `{spacing.base}` padding, followed by the price in bold 18px. On hover, the border transitions from `{colors.hairline-soft}` to `{colors.hairline}`. The card is designed to let the film's cover art — often dark and atmospheric — remain the focal point.

### Badges
**`badge-sale`** — A compact, high-contrast badge in `#f48120` with white text. Used to flag discounted titles. The orange is a deliberate departure from the red/blue system, signaling urgency without clashing. Rounded `{rounded.xs}` with tight padding.

**`badge-limited`** — A badge in the primary red `#aa1c07` for "Limited Edition" or "Collector's Set" indicators. Uses the same compact dimensions as the sale badge but communicates exclusivity rather than discount.

### Navigation
**`nav-bar`** — A fixed or sticky white header at 64px height. Navigation links use uppercase 14px/600 weight type. The active link or current section is indicated by the primary red `#aa1c07`. The nav is intentionally minimal — no mega-menus or complex dropdowns — reflecting the brand's focused catalog.

### Forms
**`text-input`** — Standard input fields with a white background, 1px hairline border, and `{rounded.sm}`. On focus, the border switches to the accent blue `#006fcf`. Used for search, newsletter signup, and checkout forms. Height is 48px for comfortable touch interaction.

### Search
**`search-bar`** — A dedicated search component with a soft gray background (`{colors.surface-soft}`) and a slightly larger `{rounded.md}`. The focus state uses the blue accent border. This is the primary discovery tool for the film catalog, placed prominently in the header or on the homepage.

### Footer
**`footer`** — A dark footer anchored in `#231f20` with white text. Links are rendered in a lighter gray (`#dedede`) for legibility. The footer contains navigation, social links, and legal text. Padding is generous at `{spacing.section}` vertical and `{spacing.xl}` horizontal.

### Hero
**`hero-panel`** — A large promotional panel with a dark background (`#231f20`) and white text, used for featured releases or announcements. The panel has `{rounded.md}` corners and substantial padding. The primary CTA within the hero uses `hero-cta`, which is the same as `button-primary` but with wider horizontal padding for visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero panel reduces padding; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but may condense; search bar reduces width |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar at full width; hero panel at max width |
| Wide | > 1440px | Max-width container (1440px) centered; product grid may expand to four columns; whitespace increases |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 44px (buttons, inputs, nav links).
- Badges and small tags are at least 24px tall with 8px horizontal padding.
- Product card images are tappable and link to the product detail page.
- Search bar is 48px tall for easy tapping on mobile.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The search bar remains visible but may be represented by an icon that expands on tap.
- The product grid collapses from 3–4 columns on desktop to 2 on tablet and 1 on mobile.
- The footer links stack vertically on mobile, with each section becoming a collapsible accordion.
- Hero panels reduce their padding and font sizes on mobile to avoid overwhelming the viewport.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography system assumes a neutral sans-serif stack (Inter, Helvetica Neue, Arial) as a reasonable default. The actual brand font may differ.
- Hover and focus states for secondary buttons, text inputs, and product cards are inferred from common patterns; exact extracted values are unavailable.
- Error states for forms (e.g., invalid email, missing field) were not extracted. A red border using `#aa1c07` or `#eb001b` is a safe assumption but unconfirmed.
- Dark mode is not present on the live site and has not been designed.
- The extracted hex list contains many warm oranges and yellows that appear to be badge/price-sticker colors. Their exact usage context (e.g., "Sale" vs. "New Release") is inferred from common e-commerce patterns.
- The brand's sub-brand or limited-edition color palettes (e.g., for specific film collections) are not captured.
- Checkout flow components (Shopify Pay, cart drawer, payment buttons) were not extracted and may use default Shopify styling.
- Spacing values for specific components (e.g., exact padding on product cards) are estimated from common e-commerce patterns and the extracted color frequencies.
