---
version: alpha
name: "Rasputin Music"
source_url: "https://www.rasputinmusic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003388 anchors a storefront that has been keeping the Bay Area bumping since 1971 — the same blue that wraps the header, fuels primary buttons, and gives the brand a weighty, no-nonsense presence that refuses to fade into the background. The palette reads as a record crate pulled from a well-loved collection: the ink-black #1d2327 of vinyl sleeves, the muted #444444 of worn shelf labels, the warm #f6f7f7 of a listening-room wall, and the occasional flash of #b94a48 red that signals a sale or a "NEW ARRIVAL" badge. Typography runs a stack of system sans-serifs — Roboto, Segoe UI, Ubuntu — at moderate weights, letting the album art and the deep blue do the heavy lifting. The layout is utilitarian and generous: wide search bars with {rounded.sm} corners, product cards that stack in clean grids, and a footer that packs links, hours, and social icons into a dense, information-rich block. There is no decorative flourish here — every pixel earns its place by helping a customer find the next record, CD, or cassette. The brand's voice is direct, slightly gruff, and deeply local: "KEEP'N THE BAY AREA BUMP'N" is not a tagline but a mission statement, and the design follows suit with high-contrast text on light canvases, bold blue CTAs, and a layout that prioritizes browsability over brand theater.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#99b3d6"
  ink: "#1d2327"
  body: "#444444"
  muted: "#555555"
  muted-soft: "#646970"
  hairline: "#bfc3c8"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f6f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#b94a48"
  accent-orange: "#ff6900"
  accent-pink: "#f78da7"
  accent-blue: "#3582c4"
  sale-badge: "#cf2e2e"
  star-rating: "#ff6900"

typography:
  display-xl:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

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
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  category-link:
    color: "{colors.primary}"
    typography: "{typography.link}"
    fontWeight: 500
  category-link-active:
    color: "{colors.ink}"
    fontWeight: 600
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Sign Up" flows. Rendered in the brand's deep blue {colors.primary} with white text and {rounded.sm} corners. On hover, shifts to {colors.primary-active} (#002266). Disabled state uses {colors.primary-disabled} (#99b3d6) with white text. Height is 44px with 12px 24px padding for comfortable tap targets.

**`button-secondary`** — An outlined alternative for less prominent actions like "View Details" or "Cancel." White background with a 2px solid {colors.primary} border and blue text. Hover state fills the background with a 10% opacity blue tint. Same 44px height as primary for visual consistency.

**`button-accent-red`** — A compact, high-urgency button reserved for sale items, clearance events, and limited-time offers. Uses {colors.accent-red} (#b94a48) background with white text, {rounded.sm} corners, and a smaller 36px height. Typically paired with a {sale-badge} on product cards.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 56px height, filled with {colors.primary} blue. Contains the brand logo, main navigation links, and a search icon. Links use {typography.nav-link} at 15px weight 600 with white text. Active state is indicated by an underline or slightly brighter white. On mobile, the nav collapses into a hamburger menu.

**`nav-link`** — Individual navigation items with transparent background and white text. Padding of 0 16px. Hover state adds a subtle white underline or 10% opacity white background. Active state uses a solid underline.

### Cards
**`product-card`** — The primary content container for album, CD, and merchandise listings. White background with {rounded.sm} corners and 8px padding. On hover, gains a subtle box-shadow (0 2px 8px rgba(0,0,0,0.1)). Contains a square aspect-ratio image with {rounded.xs} corners, followed by the title in {typography.title-sm} and price in {typography.body-md} with {colors.body} text.

**`sale-badge`** — A small, uppercase badge pinned to the top-left corner of product cards for sale items. Uses {colors.sale-badge} (#cf2e2e) background with white text, {rounded.xs} corners, and 2px 8px padding. Rendered in {typography.badge} at 11px weight 700.

### Forms
**`text-input`** — Standard text input for search, email signup, and checkout forms. White background with a 1px {colors.hairline} (#bfc3c8) border, {rounded.sm} corners, and 44px height. On focus, the border switches to {colors.primary} blue. Padding of 10px 14px for comfortable cursor placement.

**`search-bar`** — A dedicated search input styled identically to `text-input` but with 0 horizontal padding and a search icon inside the field. Used in the header and on search results pages. Focus state matches `text-input-focus`.

### Footer
**`footer`** — A dense, dark footer at {colors.ink} (#1d2327) with white text. Contains columns for store hours, locations, genres, customer service, and social media links. Padding of 48px 24px. Links use {colors.muted-soft} (#646970) and lighten to white on hover.

**`footer-link`** — Footer navigation links in {colors.muted-soft} (#646970) at 14px weight 400. Hover state transitions to {colors.canvas} (#ffffff).

### Hero
**`hero-banner`** — A full-width promotional banner at the top of the homepage or category pages. Uses {colors.surface-soft} (#f6f7f7) background with {colors.ink} text in {typography.display-md}. Contains a headline, optional subtitle, and a {hero-banner-cta} button. Padding of 64px 24px.

**`hero-banner-cta`** — The primary button within the hero banner, styled identically to `button-primary` but with wider 12px 32px padding and a 24px top margin for visual separation from the headline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), nav collapses to hamburger, hero banner reduces padding to 32px 16px, footer stacks vertically, search bar moves below nav |
| Tablet | 744–1128px | Two-column product grid (3-4 columns), nav links remain visible but condensed, hero banner uses 48px padding, footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid (4-5 columns), full nav with all links, hero banner at full 64px padding, footer uses four-column layout |
| Wide | > 1440px | Max-width container at 1440px centered, product grid expands to 6 columns, hero banner content centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (Apple HIG compliant)
- Nav links have minimum 44px tap area even when text is smaller
- Product card tap targets cover the entire card surface
- Search bar and text inputs maintain 44px height for comfortable tapping
- Footer links have 36px minimum tap area

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid reduces from 5-6 columns on wide screens to 1-2 columns on mobile
- Footer columns collapse from four on desktop to two on tablet to a single stack on mobile
- Hero banner reduces vertical padding by 50% on mobile
- Search bar moves from inline in the nav to a full-width element below the nav on mobile
- Category/subcategory filters collapse into a dropdown select on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for many components (buttons, links, cards) are inferred from common patterns rather than extracted from the live site
- Error states for form inputs (validation, error messages) are not documented — no extracted data available
- The exact font stack is inferred from CSS declarations found on the site; the brand may use a custom font that wasn't loaded in the extracted sample
- Dark mode is not supported or documented
- The extracted color list includes many generic web palette colors (blues, grays, reds) — the brand's true primary (#003388) is the most distinctive blue in the list, but the palette may include additional brand-specific colors not captured
- Sub-brand or seasonal color variations are unknown
- Animation and transition durations are not specified (default to 200ms ease where not defined)
- Focus ring styles for keyboard navigation are not documented
- Loading states (spinners, skeletons) are not captured
- The site may use a grid system with specific breakpoints not fully extracted
- Checkout flow styling (Shopify Pay, Klarna, Afterpay widgets) is not documented due to framework-default color filtering
