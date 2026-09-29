---
version: alpha
name: "Fingerprints Music"
source_url: "https://www.fingerprintsmusic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Long Beach independent record store that wears its two-tone identity on its sleeve: a deep, assertive crimson (#dd3333) for the primary brand mark and a complementary navy (#3a5795) that surfaces in navigation and footer blocks, creating a collegiate-clubhouse tension rather than a single-brand monolith. The site reads as a digital storefront built by people who love records more than they love design trends — the crimson appears in the header background, primary buttons, and sale badges, while the navy anchors the footer and secondary navigation panels. A third accent, a warm safety-orange (#fe4600), cuts through for urgency elements like limited-stock indicators and newsletter signup triggers. The typography stack pairs Raleway (headings, navigation) with Source Sans Pro (body copy), both geometric sans-serifs that keep the interface legible and unpretentious — this is a store that wants you to browse, not to admire the chrome. Product cards use soft corners ({rounded.sm}) and generous whitespace ({spacing.base} padding), while the search bar sits as a full-width field with a crimson submit button, echoing the in-store experience of asking a clerk for recommendations. The overall mood is warm, slightly retro, and deeply functional — a digital crate-digging experience that prioritizes inventory discovery over visual polish.

colors:
  primary: "#dd3333"
  primary-active: "#b4282e"
  primary-disabled: "#db7c83"
  ink: "#2c4270"
  body: "#444444"
  muted: "#3d5b9c"
  muted-soft: "#78bdf1"
  hairline: "#cee3f8"
  hairline-soft: "#d7e8f9"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#fe4600"
  accent-orange-active: "#ff4d09"
  navy: "#3a5795"
  navy-dark: "#2f4678"
  navy-light: "#53abed"
  crimson-dark: "#8a1f23"
  crimson-light: "#d25c65"
  star-rating: "#ff4d09"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Raleway', 'Source Sans Pro', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Source Sans Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Source Sans Pro', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Source Sans Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Raleway', 'Source Sans Pro', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 10px
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
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 4px 8px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-circle-crimson:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px {spacing.md}"
    rounded: "{rounded.xs}"
  top-nav-link-active:
    backgroundColor: "{colors.crimson-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px {spacing.md}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  search-submit-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.lg}"
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    height: 200px
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.navy-light}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.md}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.md}"
    height: 42px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 42px
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  category-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: "{spacing.xs} {spacing.md}"
    rounded: "{rounded.xs}"
  category-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    padding: "{spacing.xs} {spacing.md}"
    rounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 300px
  hero-banner-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-banner-subtext:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  hero-banner-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
    height: 48px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} 0"
  pagination-page:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    minWidth: 36px
  pagination-page-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    minWidth: 36px
  pagination-arrow:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.md} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "1px 6px"
    minWidth: 20px
    height: 20px

## Components

### Buttons
**`button-primary`** — The workhorse call-to-action across the site, rendered in the brand's signature crimson (#dd3333) with white text. Used for primary actions like "Add to Cart", "Checkout", and "Submit". On hover, the background deepens to `{colors.primary-active}` (#b4282e). The disabled state fades to a muted pink `{colors.primary-disabled}` (#db7c83) with reduced opacity.

**`button-secondary`** — An outlined variant with a white background and navy (#2c4270) text, bordered by a 2px solid navy line. Used for secondary actions like "View Details" or "Cancel". Active state fills with `{colors.surface-soft}`. Provides visual hierarchy alongside the primary button without competing for attention.

**`button-accent-orange`** — A smaller, high-urgency button in safety-orange (#fe4600) for limited-time offers, flash sales, and newsletter signups. The active state brightens slightly to `{colors.accent-orange-active}` (#ff4d09). Typically paired with a badge or countdown indicator.

**`button-text-link`** — A minimal, borderless button styled as an inline link using `{typography.link}`. Used for "Learn More", "Read Reviews", and "View All" actions within card layouts. No background, no border — just text with a hover underline effect.

### Navigation
**`top-nav`** — The primary navigation bar, a full-width crimson (#dd3333) strip at 60px height. Navigation links are set in uppercase Raleway at 15px weight 600, white on crimson. Active or hovered links gain a darker crimson background (`{colors.crimson-dark}`) with 8px horizontal padding and 2px corner radius. The bar includes the store logo, main category links (Vinyl, CDs, Merch, Events), and a cart icon with a badge count.

**`category-nav`** — A secondary navigation strip below the hero, with a light gray background (`{colors.surface-soft}`). Links are styled as `{typography.link}` in muted navy (#3d5b9c). The active category link inverts to a crimson pill with white text, signaling the current browse section. Used for genre filters (Rock, Jazz, Hip-Hop, Electronic, etc.).

**`breadcrumb`** — A simple, text-only breadcrumb trail using `{typography.caption}` in muted navy. Separators are soft blue (`{colors.muted-soft}`) dots or slashes. The final breadcrumb (current page) is rendered in `{colors.ink}` (#2c4270) with no link styling.

### Cards
**`product-card`** — The core inventory display unit: a white card with a 1px soft hairline border, 6px corner radius, and 16px padding. Each card contains a product image (200px height, cropped to cover), the album/artist title in `{typography.title-sm}` navy, the format and condition in `{typography.body-sm}` gray, and the price in bold `{typography.body-md}`. On hover, the border shifts to crimson and a subtle shadow lifts the card. Badges (Sale, New Arrival, Exclusive) sit in the top-left corner of the image area.

**`product-card-badge`** — Small uppercase labels (11px, weight 700, 0.5px letter spacing) in crimson, orange, or navy backgrounds depending on the badge type. Sale badges use `{colors.accent-orange}`, new arrivals use `{colors.navy}`, and standard badges use `{colors.primary}`. All badges have 2px horizontal padding and 2px corner radius.

### Forms
**`search-bar`** — A full-width text input with a white background, 1px hairline border, and 6px corner radius. The input uses `{typography.body-md}` in `{colors.body}` (#444444). On focus, the border thickens to 2px and turns crimson. A crimson submit button (`{colors.primary}`) sits to the right, labeled "Search" in `{typography.button-sm}` white text.

**`newsletter-input`** — A compact email input (42px height) with a white background and 1px hairline border, paired with an orange submit button (`{colors.accent-orange}`). Used in the footer and on the hero banner. The input placeholder reads "Your email address" in `{colors.muted-soft}`.

### Footer
**`footer`** — A deep navy (#3a5795) full-width footer with white text. Contains three columns: Store Info (address, hours, phone), Customer Service (shipping, returns, contact), and Connect (social links, newsletter signup). Links are rendered in `{colors.navy-light}` (#53abed) for contrast against the dark background. Section headings use `{typography.title-sm}` in white with 24px bottom margin.

### Hero
**`hero-banner`** — A full-width crimson (#dd3333) banner at the top of the homepage and category pages, minimum 300px height. Contains a large heading in `{typography.display-xl}` white, a subtext paragraph in `{typography.body-md}` white at 90% opacity, and a white CTA button with crimson text. The banner may feature a subtle background pattern or gradient overlay.

### Pagination
**`pagination`** — A centered row of page number buttons below the product grid. Each page button is a 36px square with light gray background (`{colors.surface-soft}`) and 2px corner radius. The active page inverts to crimson with white text. Previous/Next arrows sit at the ends with no background, using `{colors.ink}` text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack in single column (2 columns on larger mobile); hero banner reduces to 200px min-height with smaller heading; category nav becomes a horizontal scrollable strip; footer columns stack vertically; search bar becomes full-width with reduced padding; product card images reduce to 150px height |
| Tablet | 744–1128px | Top nav remains full but with condensed link spacing; product cards display in 2-3 column grid; hero banner at 250px min-height; category nav shows as scrollable pills; footer displays in 2 columns; search bar maintains full-width but with compact submit button |
| Desktop | 1128–1440px | Full top nav with all links visible; product cards in 3-4 column grid; hero banner at 300px min-height; category nav as horizontal row of pills; footer in 3 columns; search bar at 600px max-width centered |
| Wide | > 1440px | All desktop behaviors plus max-width container at 1440px centered; product cards in 4-5 column grid; hero banner at 350px min-height with larger heading; additional whitespace around content sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons (cart, search, menu toggle) are 36px minimum with 44px touch area via padding
- Product card tap targets (title, price, add-to-cart) have minimum 44px touch zones
- Pagination page buttons are 36px with 44px touch area via padding
- Category nav pills have 44px height on mobile

### Collapsing Strategy
- Top navigation collapses to a hamburger menu icon on mobile (< 744px), revealing a full-screen overlay menu with crimson background
- Product grid collapses from 4-5 columns on wide desktop to single column on mobile
- Category navigation collapses from horizontal row to a scrollable horizontal strip on tablet and mobile
- Footer collapses from 3 columns to single column on mobile
- Hero banner reduces height and font sizes on mobile
- Search bar collapses from centered max-width to full-width on tablet and mobile
- Breadcrumbs may truncate on mobile, showing only the current and parent page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns; actual extracted hover colors were not available from the static HTML analysis
- Error state styling for form inputs (validation errors, required field indicators) could not be extracted
- Active/selected states for navigation items were inferred from the crimson-dark color in the extracted palette
- Dark mode or high-contrast mode styles were not present in the extracted data
- The exact spacing scale (padding, margin values) was inferred from common e-commerce patterns; the extracted CSS did not provide a definitive spacing system
- The typography scale (font sizes, line heights, letter spacing) was estimated based on the extracted font families and common record store site patterns; exact values may differ from the live site
- Button hover animations, transitions, and micro-interactions (e.g., cart icon bounce, badge animations) were not extractable
- The checkout flow (cart page, payment form, order confirmation) was not present in the extracted data
- Social media icon colors and hover states were not reliably extractable from the static HTML
- The extracted color list contained many similar crimson and navy variants; the primary and accent colors were selected as the most distinctive and frequently occurring values
- No extracted data for loading states, skeleton screens, or empty state illustrations
- The exact border radius values for cards and buttons were estimated; the extracted CSS showed minimal rounding
- Font weights and line heights were inferred from common Raleway/Source Sans Pro usage patterns
- The brand's logo and icon system (SVG, custom icons) was not extractable from the static analysis
- No extracted data for print stylesheets or accessibility-focused styles (skip links, focus outlines)
