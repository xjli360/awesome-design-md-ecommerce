---
version: alpha
name: "Books of Wonder"
source_url: "https://booksofwonder.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sky-blue #00aeef header bar, the color of a clear New York morning, anchors a children's bookstore that has been a Chelsea landmark since 1988. The brand's visual system is a cheerful, high-contrast playground where a warm red #d44047 and a bright orange #f07c29 act as secondary voltage for sale badges and category markers, while a soft yellow #fec94a appears sparingly as a highlight accent. The canvas is a clean white #ffffff with a subtle gray #f6f6f6 for soft surfaces, and the body text runs in Lato at a comfortable 16px on a #3a3a3a ink. Product cards use a gentle {rounded.sm} corner, while the primary CTA button — a solid #00aeef pill with white text — uses a {rounded.full} shape that feels approachable and friendly, like a librarian's smile. The top navigation is a simple, horizontal strip with category links in Montserrat, and the search bar is a rounded rectangle with a #e5e5e5 border. The overall mood is one of warm, unpretentious invitation: the colors are saturated but not aggressive, the typography is clean and readable, and the layout prioritizes book covers and author names over dense text blocks. The brand's signature move is the use of #00aeef as a unifying element — it appears in the header, primary buttons, and link underlines, creating a consistent visual thread that says "you're in the right place."

colors:
  primary: "#00aeef"
  primary-active: "#1773b0"
  primary-disabled: "#23c3ff"
  ink: "#3a3a3a"
  body: "#444444"
  muted: "#989898"
  muted-soft: "#bbbbbb"
  hairline: "#e5e5e5"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d44047"
  accent-orange: "#f07c29"
  accent-yellow: "#fec94a"
  accent-pink: "#f29afa"
  sale-badge: "#c00000"
  success: "#008060"
  error: "#dd1d1d"
  dark: "#212121"
  darker: "#111111"
  border-strong: "#dedede"
  footer-bg: "#303030"
  footer-text: "#606060"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Montserrat', 'inherit', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Montserrat', 'inherit', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Montserrat', 'inherit', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Montserrat', 'inherit', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "'Lato', 'Montserrat', 'inherit', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Lato', 'inherit', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
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
    padding: 12px 24px
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
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 15px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    fontWeight: 600
    marginTop: "{spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.lg}"
  category-tab:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.full}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 300px
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.on-primary}"
    marginTop: "{spacing.base}"
  hero-banner-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    marginTop: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid #00aeef pill with white Montserrat text. Used for "Add to Cart", "Shop Now", and "Subscribe". On hover, it shifts to a deeper #1773b0. The disabled state uses a lighter #23c3ff to signal inactivity while maintaining brand consistency. **`button-secondary`** — An outlined variant with a white fill and a #e5e5e5 border. Used for "Learn More" and secondary actions. On hover, the border deepens to #3a3a3a. **`button-accent-red`** and **`button-accent-orange`** — Solid pills using the brand's accent colors for sale events, clearance, or seasonal promotions. They share the same shape and typography as the primary button but swap the background color for visual urgency.

### Cards
**`product-card`** — A white card with a gentle {rounded.sm} corner, containing a 3:4 aspect ratio book cover image, the title in Montserrat 16px/600, the author name in Lato 14px/400 in #989898, and the price in Lato 16px/600. On hover, a subtle box shadow lifts the card. **`sale-badge`** — A small red #c00000 badge with white uppercase text, pinned to the top-left corner of product cards for discounted items. **`new-badge`** — A yellow #fec94a badge for new arrivals, using the same shape and typography as the sale badge but with a warm, attention-grabbing background.

### Navigation
**`nav-bar`** — A solid #00aeef bar, 64px tall, containing the brand logo on the left and uppercase Montserrat 14px/600 navigation links in white. The active link is underlined with a 2px white border. The nav is full-width and sticky on desktop. **`category-strip`** — A secondary navigation bar below the main header, with a light gray #f6f6f6 background. Category tabs are pills: inactive tabs have muted text, while the active tab fills with #00aeef and white text. This strip collapses into a horizontal scrollable row on mobile.

### Forms
**`text-input`** — A white input field with a #e5e5e5 border and {rounded.sm} corners. On focus, the border becomes a 2px #00aeef stroke. The error state uses a 2px #dd1d1d border. **`search-bar`** — A pill-shaped search field with a full {rounded.full} radius, used in the header and on search results pages. On focus, the border becomes a 2px #00aeef stroke.

### Footer
**`footer`** — A dark #303030 section with #606060 text, using Lato 14px/400 for links and body copy. Links turn #00aeef on hover. The footer contains columns for customer service, about us, and social links, with generous {spacing.xxl} padding on top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; category-strip becomes horizontally scrollable; product cards stack in 2-column grid; hero banner reduces padding and font size; search bar moves to a toggleable overlay |
| Tablet | 744–1128px | Nav-bar remains horizontal but with reduced link padding; product cards in 3-column grid; hero banner maintains full width with adjusted typography |
| Desktop | 1128–1440px | Full layout with 4-column product grid; nav-bar at 64px with full link set; hero banner at full height with 32px display text |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 5 columns; hero banner may include additional decorative elements |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Nav-bar links have 48px tap areas.
- Product card tap targets extend to the full card area.
- Category strip tabs have 40px minimum height.

### Collapsing Strategy
- Main navigation collapses to a hamburger menu below 744px.
- Category strip collapses to a horizontal scrollable row below 744px.
- Footer columns stack vertically below 744px.
- Search bar collapses to an icon that opens an overlay on mobile.
- Product grid reduces from 4 columns to 2 columns on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors.
- Error states for text inputs (beyond border color) and form validation messages are not documented.
- The exact font weights for Lato and Montserrat in use (e.g., 300, 400, 600, 700) are inferred from common web usage; the live site may use additional weights.
- The brand's sub-brand or seasonal color palettes (e.g., holiday themes, author events) are not captured.
- Dark mode is not supported and was not detected on the live site.
- The extracted color list is heavily weighted toward generic web and Shopify defaults; the brand's true primary (#00aeef) and accent colors (#d44047, #f07c29, #fec94a) are the most distinctive and are used as the core palette. Other grays and blues may be framework artifacts.
- The exact spacing scale (e.g., 8px grid) is inferred from common practice; the live site may use a different base unit.
- The hero banner's exact min-height and padding are estimated based on typical bookstore hero layouts; the live site may vary.
- The `font-family` declarations found include "Lato", "Montserrat", "inherit", and "sans-serif"; the exact fallback stack and font loading strategy are not confirmed.
