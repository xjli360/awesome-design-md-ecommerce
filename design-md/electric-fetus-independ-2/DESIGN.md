---
version: alpha
name: "Electric Fetus"
source_url: "https://www.electricfetus.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, dark storefront of possibility, Electric Fetus uses a black canvas (#000000) as its primary gesture — not as a background convenience but as the deliberate, enveloping atmosphere of a record store’s interior where every album sleeve, poster, and fixture becomes the focal point. The brand’s single voltage is a vivid, saturated magenta (#c6007e) that appears in primary CTAs, sale badges, and category highlights, cutting through the darkness like a neon sign in a basement window. With only Arial as the declared typeface, the site leans on weight contrast — bold, condensed headings at 28px sit above light-weight body copy at 14px — creating a utilitarian, no-nonsense hierarchy that lets product photography and album art do the emotional work. Search is a full-width, pill-shaped field (`{rounded.full}`) with a dark background and white text, suggesting the brand trusts discovery over navigation. Product cards use a soft white surface (`{colors.surface-card}`) against the black page, with thin, 1px hairlines (`{colors.hairline}`) separating items in grid and list views. The overall mood is that of a late-night crate-digging session: low light, high signal, and the occasional fluorescent burst of magenta.

colors:
  primary: "#c6007e"
  primary-active: "#a00066"
  primary-disabled: "#e699cc"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#000000"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#c6007e"
  new-arrival-badge: "#000000"
  vinyl-icon: "#333333"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
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
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.new-arrival-badge}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
  category-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  category-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.link}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a solid magenta (#c6007e) rectangle with no border radius, using uppercase 14px bold Arial. On hover, it shifts to a darker shade (#a00066). The disabled state uses a lighter tint (#e699cc) to signal inactivity. Used for "Add to Cart," "Checkout," and primary form submissions.

**`button-secondary`** — An inverted button with a black background and white text, used for secondary actions like "View Details" or "Continue Shopping." The active state inverts to a light gray background with black text. No border radius maintains the brand's utilitarian edge.

**`button-sm`** — A compact version of the primary button, using 12px uppercase bold text, used for inline actions like "Quick Add" or filter resets. Same color states as `button-primary`.

### Navigation
**`nav-bar`** — A fixed 60px black bar at the top of the page, containing the brand logo and navigation links set in 14px uppercase Arial. Links are white by default and switch to magenta (#c6007e) on hover or active state. The bar has no border or shadow, blending into the dark canvas.

**`nav-link`** — Navigation items use uppercase 14px Arial with 0.5px letter-spacing. The active state is indicated by the magenta primary color. No underline or other decoration is used, keeping the interface clean and direct.

### Forms
**`text-input`** — A white rectangular input field with no border radius, using 16px Arial for user-entered text. On focus, a 2px magenta border appears. Used for search queries, email signups, and checkout forms. Padding is 12px top/bottom and 16px left/right.

**`search-bar`** — A full-width pill-shaped search field with a light gray background (#f2f2f2) and dark text, contrasting with the black canvas. The pill shape (`{rounded.full}`) is the only rounded element in the system, signaling the search function as a distinct, friendly entry point. On focus, the border shifts to magenta.

### Cards
**`product-card`** — A white rectangular card with no border radius, containing album art, title, artist, price, and action buttons. On hover, a subtle drop shadow (`0 4px 12px rgba(0,0,0,0.15)`) lifts the card from the page. Padding is 16px on all sides. Used in grid and list views for vinyl, CDs, and merchandise.

**`badge-sale`** — A small magenta rectangle with white uppercase 10px text, placed in the top-left corner of product cards or category headers. No border radius. Signals discounted items.

**`badge-new`** — A small black rectangle with white text, used to denote new arrivals. Same dimensions and placement as the sale badge.

### Footer
**`footer`** — A black section at the bottom of the page with muted gray (#666666) 14px Arial text. Contains links to store policies, social media, and contact information. Padding is 48px top/bottom and 24px left/right. Links turn magenta on hover.

### Hero
**`hero-section`** — A full-width black section with white 28px bold Arial headings, used for promotional banners, featured releases, and seasonal campaigns. Padding is 80px top/bottom and 24px left/right. The hero may include a single magenta CTA button for primary actions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, stacked product cards, hamburger menu replaces nav links, hero padding reduced to 48px, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid, nav links visible, search bar full-width, hero padding at 64px |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, search bar in header, hero at full padding |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero content constrained to 1200px |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 44px and width of 44px for touch accessibility.
- Nav links have a tap area of at least 48px height.
- Search bar has a minimum height of 48px for easy tapping.
- Badges are at least 20px tall, with text sized for readability at 10px.

### Collapsing Strategy
- On mobile, the navigation bar collapses to a hamburger menu icon, with the full menu appearing as a slide-in overlay from the left.
- The search bar collapses to a magnifying glass icon on mobile, expanding to full width on tap.
- Product grids collapse from 4 columns on wide screens to 1 column on mobile.
- The footer collapses from a multi-column layout to a single column on mobile, with links stacked vertically.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (Arial) was extracted from the live site; the brand may use additional web fonts for headings or decorative elements that were not captured.
- No meta theme-color was found; the browser chrome color on mobile devices is unknown.
- No specific hex colors were extracted from the live site's HTML and CSS; the palette above is inferred from the brand's known visual identity (black background, magenta accent) and common record store design patterns. A full audit of the live site's CSS is needed to confirm exact values.
- Hover, focus, and active states for all components are speculative, based on common accessibility patterns and brand color logic.
- Error states for forms (validation, error messages) were not extracted and are not included.
- Dark mode support is not confirmed; the brand's black canvas may serve as a de facto dark mode.
- Sub-brand or seasonal color palettes (e.g., for Record Store Day, holiday promotions) are not documented.
- The brand's logo color and treatment (e.g., white logo on black background) is assumed but not extracted.
- Spacing values are based on common e-commerce patterns; exact padding and margin values from the live site are unknown.
