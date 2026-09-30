---
version: alpha
name: "Janji"
source_url: "https://janji.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A running brand that paints its gear in the colors of the places it comes from — #108474 (a deep teal pulled from Costa Rican jungle canopy) and #c8c6c5 (a weathered stone gray) set the tone, while accents like #ea3d26 (volcanic red) and #f6f1a0 (high-altitude yellow) flash across product details and CTAs. The palette reads like a field notebook: #90a7a3 (mossy sage), #899379 (dry earth), #485354 (basalt), and #b45457 (clay brick) appear in patterns and linings, not just trim. Typography splits between PierSans-Bold for headlines — a sturdy, slightly condensed sans that stands up to trail grit — and Nunito Sans for body, a rounder, more approachable face that keeps the brand from feeling too severe. Buttons use {rounded.full} pills in that teal or red, while product cards sit in {rounded.sm} on a #f7f7f7 canvas, letting the photography — always of runners in real landscapes, not studios — carry the emotional weight. The nav bar is a thin strip of {colors.ink} (#29292d) with white text, a deliberate inversion that says "we're serious about performance." There's no hero carousel; instead, the homepage leads with a single full-bleed image and a bold PierSans statement, trusting the place and the runner to sell the gear.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d4c9"
  ink: "#29292d"
  body: "#485354"
  muted: "#90a7a3"
  muted-soft: "#c8c6c5"
  hairline: "#c8c6c5"
  hairline-soft: "#e0dede"
  canvas: "#f7f7f7"
  surface-soft: "#f0efef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ea3d26"
  accent-yellow: "#f6f1a0"
  accent-sage: "#899379"
  accent-clay: "#b45457"
  accent-teal-light: "#bde2e3"
  accent-maroon: "#672527"
  accent-navy: "#315772"
  accent-brown: "#7f5c55"
  accent-gold: "#c39a6c"
  accent-pink: "#ea088e"
  accent-lime: "#c5da3f"

typography:
  display-xl:
    fontFamily: "'PierSans-Bold', 'Andale Mono', 'Courier New', monospace"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'PierSans-Bold', 'Andale Mono', monospace"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'PierSans-Bold', 'Andale Mono', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', 'Trirong', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Trirong', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-yellow}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 600px
  hero-overlay:
    backgroundColor: "rgba(41, 41, 45, 0.4)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  collection-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
  collection-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  collection-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a full-pill in the brand's teal (#108474) with white PierSans-bold text. On hover, it shifts to `primary-active` (#0d6b5d); disabled state uses a washed-out teal (#a3d4c9). Used for "Add to Cart," "Shop Now," and primary checkout flows. **`button-secondary`** — An inverted pill with a white fill and ink (#29292d) text, bordered by a 1px hairline. Hover adds a subtle shadow. **`button-accent-red`** and **`button-accent-yellow`** — High-energy variants for limited drops, sale alerts, or "Explore" CTAs on hero sections. Red uses #ea3d26; yellow uses #f6f1a0 with ink text. **`button-tertiary-text`** — A plain text link styled as a button, used for "Learn More" or "View Details" in content-heavy areas.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners on a `{colors.canvas}` background. The product image sits flush within the card's `{rounded.sm}`. Title uses `{typography.title-sm}` in ink, price in `{typography.body-md}` in body. A **`product-card-badge`** — a small red pill with uppercase "NEW" or "SALE" — can overlay the top-left of the image. Cards have no border; separation comes from the canvas-to-card contrast.

### Navigation
**`nav-bar`** — A 64px-high strip in `{colors.ink}` (#29292d) with white uppercase nav links (`{typography.nav-link}`). The logo sits left-aligned; links (Men, Women, Accessories, Explore) are center or right. Active link turns `{colors.accent-yellow}`. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — A white input field with `{rounded.sm}`, 48px tall, using `{typography.body-md}`. On focus, it gains a 2px teal ring (`{colors.primary}`). Used for email signups, search, and checkout forms. **`search-bar`** — A full-pill variant of the text input, used in the site header or on search results pages.

### Footer
**`footer`** — A dark section in `{colors.ink}` with `{colors.muted-soft}` body text. Links are white (`{colors.canvas}`) and use `{typography.link}`. Section headings use `{typography.title-sm}` in white. The footer includes columns for "Shop," "About," "Support," and social links. A thin `{colors.hairline}` divider separates the top from the bottom copyright row.

### Collection Strip
**`collection-strip`** — A horizontal scrollable row of collection tabs (e.g., "Trail," "Road," "Travel"). Active tabs use `{colors.primary}` fill with white text in a pill shape; inactive tabs use `{colors.surface-soft}` with `{colors.body}` text. Used on collection pages and the homepage to filter by activity.

### Product Detail
**`size-selector`** — A small square or rounded button (40px) for size options. Active state inverts to `{colors.ink}` fill with white text. **`quantity-selector`** — A compact row with minus/plus buttons and a number display, all in `{colors.surface-soft}` with `{rounded.sm}`. **`accordion`** — Used for product descriptions, materials, and shipping info. Each section has a `{typography.title-sm}` header and `{typography.body-sm}` content, separated by a `{colors.hairline}` divider.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero height reduces to 400px; collection strip becomes a vertical accordion; footer stacks into single column |
| Tablet | 744–1128px | Nav links show as text (no icons); product cards in 2-column grid; hero height at 500px; collection strip remains horizontal but scrollable |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero at 600px; collection strip shows all tabs without scroll |
| Wide | > 1440px | Max-width container (1440px) centered; hero may use full-bleed; product cards in 4-column grid; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements: minimum 44px height
- Nav links: 44px tap area (even if text is smaller)
- Size selectors: 40px minimum, with 8px gap between options
- Quantity selector buttons: 44x44px tap area
- Collection tabs: 44px height with 12px horizontal padding

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; drawer slides from left
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer columns stack vertically on mobile, with accordion-style expand/collapse for each section
- Collection strip tabs collapse to a dropdown or accordion on mobile
- Hero text overlay reduces font size and may stack vertically

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, text inputs, and nav links could not be reliably extracted from the static CSS; the above uses reasonable defaults (subtle shadow, border color change)
- Error styling for form inputs (red border, error message typography) is not present in the extracted data
- Sub-brand or collection-specific palettes (e.g., "Costa Rica," "Iceland," "Patagonia" collections) may have their own accent colors not captured here
- Dark mode is not implemented on the live site; no dark-mode tokens exist
- The extracted font list includes "JudgemeStar" (a review widget icon font) and "Trirong" (possibly a secondary serif for editorial content) — these are noted but not used in core components
- The extracted hex list is unusually large (30 colors), suggesting many are from product photography, social icons, or Shopify checkout widgets (e.g., #0064a5, #0054a5 are likely Klarna/Afterpay blues; #d81f2d is likely a social icon). The true brand palette is distilled from the most frequent and distinctive non-widget colors
- Animation durations, easing curves, and transition properties are not documented
- Focus-visible styles for keyboard navigation are not extracted
- Print stylesheet behavior is unknown
