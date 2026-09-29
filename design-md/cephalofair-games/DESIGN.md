---
version: alpha
name: "Cephalofair Games"
source_url: "https://cephalofair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated blue (#006fcf) anchors a brand that sells epic strategy — board games that take hours, not minutes, and reward repeated plays. That blue, the most distinctive and frequent color extracted from the live site, appears on primary buttons, navigation bars, and hero backgrounds, often paired with a warm, high-contrast yellow (#ffc600) used for badges, sale tags, and accent highlights. The palette is deliberately limited: a near-black ink (#1d1c1c) for body text, a softer charcoal (#232323) for secondary text, and a clean white canvas (#dedede as a warm off-white, with pure white likely used on cards). Orange (#f48120) appears as a secondary accent, likely for pre-order or limited-edition callouts. The typography stack — Geneva, Tahoma, Verdana, sans-serif — is pragmatic and system-native, suggesting the brand prioritizes legibility and load speed over custom typefaces. Buttons use `{rounded.sm}` corners, cards use `{rounded.md}`, and the overall feel is functional and direct: a storefront for complex games, not a lifestyle brand. The site is built on Shopify, so checkout widgets introduce extraneous colors (Klarna pink `#cc0066`, Afterpay blue `#4285f4`, Google Pay colors) that should be ignored when defining the brand palette. The true Cephalofair voice is confident, game-first, and unpretentious — the blue says "trust us, this game is worth your time," the yellow says "this deal is worth your attention."

colors:
  primary: "#006fcf"
  primary-active: "#005ab9"
  primary-disabled: "#8cbce5"
  ink: "#1d1c1c"
  body: "#232323"
  muted: "#444444"
  muted-soft: "#5f6368"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffc600"
  accent-yellow-active: "#fba900"
  accent-orange: "#f48120"
  accent-orange-active: "#e16f27"
  badge-new: "#ffc600"
  badge-sale: "#f48120"
  star-rating: "#ffc600"
  error: "#eb001b"
  success: "#34a853"

typography:
  display-xl:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Geneva, Tahoma, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
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
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-subtitle:
    typography: "{typography.display-md}"
    textColor: "{colors.on-primary}"
    marginTop: "{spacing.md}"
  hero-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Pre-order," and "Shop Now." Uses the brand's deep blue `{colors.primary}` with white text on a `{rounded.sm}` background. On hover, shifts to `{colors.primary-active}` (#005ab9). Disabled state uses a muted blue `{colors.primary-disabled}`. **`button-secondary`** — An outlined variant with a white background, blue text, and a 2px blue border. Used for secondary actions like "Learn More" or "View Details." Active state darkens the border and text. **`button-accent-yellow`** — A high-contrast yellow button (`{colors.accent-yellow}`) with dark text, used sparingly for the most urgent calls-to-action (e.g., hero CTAs, limited-time offers). Active state shifts to a slightly darker yellow. **`button-accent-orange`** — A smaller, compact orange button used for sale badges or pre-order callouts. Uses `{typography.button-sm}` and tighter padding.

### Cards
**`product-card`** — The primary product display unit, a white card with `{rounded.md}` corners and a subtle `{colors.hairline-soft}` border. Contains a square product image with `{rounded.sm}`, a title in `{typography.title-md}`, and a price in `{typography.body-md}`. On hover, the border changes to `{colors.primary}` and a light shadow appears. Badges (new, sale) sit in the top-left corner of the image area.

### Navigation
**`nav-bar`** — A fixed or sticky top bar, 64px tall, with a white background and a 1px bottom border. Navigation links use `{typography.nav-link}` with 8px/12px padding. The active page link is underlined with a 2px `{colors.primary}` border. The bar may contain a logo, a search icon, and a cart icon.

### Forms
**`text-input`** — Standard text input fields with a white background, `{rounded.sm}`, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state uses a red border (`{colors.error}`). Used for search, newsletter signup, and checkout forms.

### Hero
**`hero`** — A full-width banner section with a `{colors.primary}` background and white text. Contains a large headline (`{typography.display-xl}`), a subtitle (`{typography.display-md}`), and a yellow CTA button (`{hero-cta}`). Minimum height of 400px. May include a background image or pattern overlay.

### Badges
**`badge`** — Small, uppercase labels used to indicate product status. The default badge uses yellow (`{colors.badge-new}`) with dark text for "New" or "Coming Soon." The sale badge uses orange (`{colors.badge-sale}`) with white text for "Sale" or "Clearance." Both use `{typography.badge}` and `{rounded.xs}`.

### Footer
**`footer`** — A dark footer with a `{colors.ink}` background and white text. Links use a muted gray (`{colors.muted-soft}`) that lightens to white on hover. Organized into columns for support, games, company info, and social links. Includes copyright text and payment icons.

### Search
**`search-bar`** — A pill-shaped search input with `{rounded.full}`, a white background, and a 1px `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`. Used for product search across the store.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; hero text reduces to `{typography.display-md}`; product cards stack vertically; footer columns stack; search bar moves to a slide-out panel |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero retains full height; footer shows 2-3 columns |
| Desktop | 1128–1440px | Full layout with 3-4 column product grid; nav bar shows all links; hero uses full `{typography.display-xl}`; footer shows 4 columns |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; product grid can expand to 5 columns if content allows |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px.
- Product card images are tappable and link to product detail pages.
- Search bar has a minimum height of 48px for easy tapping.
- Nav links have 8px/12px padding to ensure adequate tap area.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The search bar collapses into an icon that expands to a full-width input on tap.
- The footer collapses from 4 columns to 2 on tablet, and to a single column on mobile.
- Product cards switch from a multi-column grid to a single-column list on mobile.
- Hero text reduces in size on mobile to prevent overflow.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards are inferred from common patterns; exact colors and transitions were not extractable from the static HTML/CSS.
- Error and success styling for forms (e.g., validation messages, input borders) is estimated based on standard web conventions; the brand may use custom colors.
- The exact font stack is Geneva, Tahoma, Verdana, sans-serif — no custom web font was detected. The brand may use a variable font or a different weight than what is listed.
- Dark mode styling is not present on the live site; no dark mode tokens are defined.
- The extracted color list includes many checkout-widget colors (Klarna pink, Afterpay blue, Google Pay colors) that are not part of the brand palette. These have been excluded from the design tokens.
- The brand's secondary accent orange (#f48120) appears in multiple shades in the extracted list (#f58720, #f89f20, #f79a20, #f68d20, #f37521, #e16f27, #d4602c, #d05b2e) — the most saturated variant (#f48120) was chosen as the primary orange token.
- The yellow accent (#ffc600) has several near-identical variants (#fba900, #ffd800, #fff48d) — the most saturated (#ffc600) was chosen.
- No animation or transition timing values were extractable.
- The brand's logo and icon system were not analyzed; only text and color tokens are defined.
- Sub-brand or game-specific color palettes (e.g., for Gloomhaven, Frosthaven) may exist but were not extractable from the main site.
