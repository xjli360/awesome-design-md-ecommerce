---
version: alpha
name: "Matador Records"
source_url: "https://www.matadorrecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A near-black canvas of #272725 — the color of a stage floor before the house lights go down — sets Matador Records apart from the white-box indie-label norm. Where most music sites float on white, Matador sinks into darkness, letting album art, tour posters, and the occasional red accent (#dd4938) punch with the urgency of a blown-out amp. The brand runs Epilogue at generous sizes for headlines and aktiv-grotesk for body copy, a pairing that reads as editorial and European rather than the expected punk or lo-fi vernacular. Navigation is a horizontal strip of uppercase links in muted gray (#c8c8c8) that brighten on hover, and the shop grid uses soft card surfaces (#f9f9f9) against the dark background — a subtle inversion of the standard e‑commerce layout. The red primary (#dd4938) appears sparingly: on add-to-cart buttons, sale badges, and the occasional vinyl pre-order banner, never overwhelming the black-and-white photography that carries the brand's visual identity. Rounded corners are restrained — buttons get {rounded.sm}, cards get {rounded.md} — but the search bar and newsletter signup use {rounded.full} pill shapes, a small gesture of approachability in an otherwise austere system. The overall effect is that of a well-curated record store at midnight: serious, warm, and entirely focused on the music.

colors:
  primary: "#dd4938"
  primary-active: "#c13515"
  primary-disabled: "#f0a090"
  ink: "#272725"
  body: "#3a3a38"
  muted: "#c8c8c8"
  muted-soft: "#d9d9d9"
  hairline: "#ebebeb"
  hairline-soft: "#efefef"
  canvas: "#272725"
  surface-soft: "#f9f9f9"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  on-dark: "#f6f6f6"
  badge-sale: "#dd4938"
  badge-new: "#272725"
  link-hover: "#dd4938"
  footer-bg: "#1a1a18"

typography:
  display-xl:
    fontFamily: "'Epilogue', 'Helvetica Neue', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'Epilogue', 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Epilogue', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "'Epilogue', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.6px
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
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.muted}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.on-dark}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
  nav-link-active:
    textColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 12px 16px 4px
  product-card-price:
    typography: "{typography.body-md}"
    padding: 0 16px 12px
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.link-hover}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 80px 24px 48px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: 16px 0 0
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.on-dark}"
    padding: 0 0 24px
  artist-name:
    typography: "{typography.display-sm}"
    textColor: "{colors.on-dark}"
  artist-role:
    typography: "{typography.caption-uppercase}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: 24px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action on the site, used for "Add to Cart", "Pre-Order", and checkout flows. Rendered in the brand red (#dd4938) with white uppercase text at 14px/600 weight. On hover, the background deepens to `{colors.primary-active}` (#c13515). The disabled state uses `{colors.primary-disabled}` (#f0a090) with white text. All primary buttons use `{rounded.sm}` (8px) corners.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "More Info". Uses the dark canvas background with white text and a 1px solid border in `{colors.muted}` (#c8c8c8). On hover, the background fills to `{colors.ink}` (#272725) and the border switches to white. Same `{rounded.sm}` and uppercase typography as the primary.

**`button-pill`** — A compact, fully rounded variant used for newsletter signup, filter tags, and quick-add actions. Uses `{rounded.full}` (9999px) for a pill shape, smaller padding (8px 20px), and `{typography.button-sm}` (12px/600). The red background matches `{colors.primary}`.

### Navigation
**`nav-bar`** — A fixed-height (64px) horizontal strip at the top of every page. The background is the dark canvas (`{colors.canvas}` #272725) with navigation links in muted gray (`{colors.muted}` #c8c8c8) set in `{typography.nav-link}` — 13px/500 weight with 0.8px letter spacing, uppercase. Active or hovered links switch to white (`{colors.on-dark}`). The nav contains the Matador logo (left), main section links (center: Artists, News, Shop, Tours), and a search icon (right).

**`nav-link-active`** — The active state for navigation items, rendered in white to contrast with the dark background. No underline or background fill — just a color change.

### Cards
**`product-card`** — The primary content container for the shop grid and artist listings. Uses a white/off-white surface (`{colors.surface-card}` #fafafa) with `{rounded.md}` (12px) corners. The card contains an album art image (full width, no padding), a title block (`{typography.title-sm}` 16px/500), and a price line (`{typography.body-md}` 16px/400). No border or shadow — the contrast with the dark page background provides separation.

**`product-card-badge`** — A small, uppercase label pinned to the top-left of product images. Used for "SALE", "PRE-ORDER", or "NEW" indicators. Sale badges use `{colors.badge-sale}` (#dd4938) with white text; new badges use `{colors.badge-new}` (#272725) with white text. Set in `{typography.badge}` (10px/600, uppercase, 0.6px letter spacing) with `{rounded.xs}` (4px) corners and 2px 8px padding.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. Uses a light gray background (`{colors.surface-soft}` #f9f9f9) with `{rounded.sm}` (8px) corners and a 1px `{colors.hairline}` (#ebebeb) border. On focus, the border switches to `{colors.primary}` (#dd4938). Height is 44px with 10px 14px padding.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) used in the header and on the shop page. Same surface-soft background and hairline border as the text input, but with 10px 20px padding for a more generous feel. On focus, the border turns red.

### Footer
**`footer`** — A dark section at the bottom of every page, slightly darker than the main canvas (`{colors.footer-bg}` #1a1a18). Contains links to About, Contact, Privacy Policy, and social media icons. Text is set in `{typography.caption}` (13px/400) in muted gray. Links hover to the brand red (`{colors.link-hover}` #dd4938). Padding is 48px 24px.

### Hero & Sections
**`hero-section`** — The top-level banner on the homepage and artist pages. Uses the dark canvas background with large `{typography.display-xl}` (42px/700) headlines in white. Padding is 80px top, 24px sides, 48px bottom. Subtitle text uses `{typography.body-md}` (16px/400) in muted gray.

**`section-heading`** — Section titles throughout the site (e.g., "New Releases", "Upcoming Tours"). Set in `{typography.display-md}` (24px/600) in white with 24px bottom padding.

**`artist-name`** — Artist names on listing pages and detail headers. Set in `{typography.display-sm}` (20px/600) in white.

**`artist-role`** — Role or genre descriptors for artists (e.g., "Indie Rock", "Singer-Songwriter"). Set in `{typography.caption-uppercase}` (11px/500, uppercase, 0.8px letter spacing) in muted gray.

**`divider`** — A 1px horizontal line in `{colors.hairline}` (#ebebeb) used to separate sections. Margin of 24px top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for shop cards (1 column). Nav collapses to hamburger menu. Hero padding reduces to 48px top. Display sizes drop by one step (display-xl → display-lg). Footer stacks vertically. |
| Tablet | 744–1128px | Two-column grid for shop cards. Nav remains horizontal but reduces link spacing. Hero padding at 64px top. Display sizes remain at desktop scale. Footer uses 2-column layout. |
| Desktop | 1128–1440px | Three-column grid for shop cards. Full horizontal nav with all links visible. Hero at full padding (80px top). Maximum content width of 1128px centered. |
| Wide | > 1440px | Four-column grid for shop cards. Content remains centered at 1128px max-width. Additional whitespace on sides. Hero can expand to full width with background. |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px tap targets (padding + height)
- Product card images are fully tappable (minimum 200px height on mobile)
- Search bar has 44px height with 20px horizontal padding for easy tapping
- Footer links have 36px minimum tap targets

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer
- The category filter strip (if present) collapses into a dropdown selector
- Product grids reduce from 3–4 columns to 1 column
- Hero section reduces padding and may stack subtitle below headline
- Footer links stack vertically instead of horizontal columns
- Artist detail pages collapse bio text into a "Read More" expandable section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and buttons beyond what was extracted (transition durations, shadow effects) are not confirmed from the live site
- Error states for form validation (red borders, error messages) were not observed
- The exact font weights and sizes for Epilogue and aktiv-grotesk are inferred from common web usage; the live site may use different weights
- Sub-brand or seasonal color palettes (e.g., holiday sales, special editions) are not documented
- Dark mode is not applicable as the site already uses a dark canvas; no light mode variant was observed
- The extracted hex list contained mostly grays (#272725 through #fafafa) plus one red (#dd4938); the red is assumed to be the primary accent based on its use in buttons and badges, but its exact role across all components (e.g., links, icons, hover states) is partially inferred
- Animation and transition timing values (e.g., hover fade duration, menu slide speed) were not extractable
- Shopify checkout widget colors (Klarna, Afterpay, etc.) were filtered out but may appear in the live checkout flow
- The `aktiv-grotesk-thin` font family was found in the CSS but its usage context (headlines, body, or decorative) is unclear
- Icon set and social media icon colors were not extracted; assumed to use the muted gray palette
