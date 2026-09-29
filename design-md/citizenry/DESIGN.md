---
version: alpha
name: "The Citizenry"
source_url: "https://www.the-citizenry.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The Citizenry is a globally inspired home decor brand that feels like a curated journey through artisan workshops and sun-drenched markets. The palette is anchored by a warm, earthy olive (#7d7a56) that appears in everything from throw pillows to ceramic vases, evoking the patina of natural materials rather than synthetic dyes. This primary green-brown is tempered by a soft clay tone (#996c49) that reads like unfired terracotta, and a muted canvas (#f8f8f8) that keeps the overall feeling airy and approachable. The brand avoids harsh contrasts — even the ink (#121212) is a softened near-black, while body text rests at a comfortable {colors.body} gray. Signature design moves include generous use of {rounded.full} pill-shaped buttons and search bars, softly rounded product cards at {rounded.lg}, and a reliance on layered textures (linen, wood grain, hand-thrown ceramics) over heavy typography. The type system uses SF Pro Text at modest weights — display heads sit at 22–28px in weight 500 rather than the heavy 700+ that luxury brands often employ — letting the product photography and whitespace carry the emotional weight. Accent blues (#899df1, #1990c6, #136f99) appear sparingly in navigation elements and badges, adding a quiet confidence without competing with the earth tones. The overall feeling is one of intentional calm: a space where every object has a story, and the interface steps back to let the goods speak.

colors:
  primary: "#7d7a56"
  primary-active: "#6b6848"
  primary-disabled: "#c5c3b0"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#f8f8f8"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#899df1"
  accent-blue-active: "#1990c6"
  accent-blue-dark: "#136f99"
  terracotta: "#996c49"
  terracotta-light: "#b88a6a"
  star-rating: "#121212"
  scrim: "#000000"
  badge-new: "#7d7a56"
  badge-sale: "#996c49"

typography:
  display-xl:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: -0.1px
  display-sm:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.1px
  link:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px

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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 16px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-photo:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    height: 480px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 16px 0
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action uses the brand's olive (#7d7a56) as a solid fill with white text. On hover, it deepens to `{colors.primary-active}` (#6b6848), and in its disabled state it fades to a muted sage (#c5c3b0). The pill shape (`{rounded.full}`) and 44px height give it a tactile, friendly feel that echoes the handmade ethos of the brand. **`button-secondary`** — An outlined variant on a white canvas with ink text, used for secondary actions like "View Details" or "Add to Wishlist." It shares the same pill shape and height but uses a 1px hairline border (`{colors.hairline}`) that darkens on hover. **`button-tertiary-text`** — A text-only button with no background or border, used for subtle actions like "Cancel" or "Learn More." It relies on the ink color and inherits the button typography for consistency.

### Cards
**`product-card`** — The primary product display unit, rendered on a white surface with soft rounded corners (`{rounded.lg}` ~20px). The card contains a photo area (`{rounded.lg}`) that fills the top, followed by product title, price, and optional badges. On hover, a subtle shadow appears to lift the card from the canvas. **`product-card-badge`** — A small pill-shaped badge overlaid on the product photo, used for "New" or "Sale" indicators. It uses the brand's olive or terracotta as background, with white text in uppercase 11px weight 600.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, white background with ink text. The logo sits left-aligned, with category links (Shop, Collections, About) centered or right-aligned. Active links use the ink color, while inactive links are muted. On scroll, a subtle bottom border (`{colors.hairline}`) appears. **`category-strip`** — A horizontal scrollable strip of category tabs below the nav bar, used on collection pages. Tabs are text-only with a bottom border indicator for the active state.

### Forms
**`text-input`** — Standard text input fields use a white canvas background with a 1px hairline border (`{colors.hairline}`) and 8px rounded corners (`{rounded.sm}`). On focus, the border shifts to the primary olive. Error states use a terracotta border and include an error message below in caption size. **`search-bar-pill`** — A full-width pill-shaped search bar with a magnifying glass icon, used on the search page. It has a white background, ink text, and a subtle shadow on focus.

### Footer
**`footer-section`** — A soft gray background (`{colors.surface-soft}`) with body text in muted gray. Links are styled as `{typography.link}` and turn ink on hover. The footer includes columns for Customer Service, About, and Social links, with a copyright line at the bottom.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details. The header is a clickable row with title-sm typography and a chevron icon that rotates on expand. **`accordion-body`** — The expanded content area, with body-sm typography and no padding between items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero banner height reduces to 320px; category strip becomes horizontally scrollable; footer columns stack vertically; search bar becomes full-width below nav. |
| Tablet | 744–1128px | Nav bar shows condensed links (Shop, About); product cards in 2-column grid; hero banner at 400px; footer columns in 2x2 grid; search bar remains pill-shaped but narrower. |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3-column grid; hero banner at 480px; footer columns in 4-column layout; search bar centered in nav. |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero banner at 520px; all elements centered with generous whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px height.
- Icon buttons are 36px with 44px touch area via padding.
- Product card tap targets include the entire card surface.
- Accordion headers have 44px minimum height for easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer.
- Category tabs collapse into a horizontal scrollable strip.
- Footer columns stack vertically on mobile.
- Product detail accordions collapse by default on all breakpoints.
- Search bar collapses to an icon on mobile, expanding to full-width on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and links were not fully extracted; assumed darkening of border/text.
- Error styling for forms (border color, error message color) was inferred from brand palette; exact values not confirmed.
- Sub-brand palettes (e.g., for collections or collaborations) were not observed.
- Dark mode styles are not present; the brand uses a light-only theme.
- Focus ring styles (outline, color, offset) were not extracted; assumed 2px solid primary with 2px offset.
- Loading states (spinners, skeleton screens) were not observed.
- Animation durations and easing curves were not extracted; assumed 200ms ease-in-out for hover transitions.
- The exact font weight for body text (400 vs 500) was inferred from common SF Pro Text usage; not confirmed on all pages.
- Badge positioning (top-left, top-right) and z-index were not extracted.
- Hero banner overlay gradients or text positioning were not observed.
