---
version: alpha
name: "CalDigit"
source_url: "https://www.caldigit.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003399 anchors CalDigit's digital presence with the confidence of a Thunderbolt dock that has nothing to prove — the color appears on primary buttons, navigation bars, and product badges, creating a consistent voltage across the shopping experience. The brand pairs this primary with a secondary #003388 for hover states and a warning red #ff0000 that signals sale badges and limited-time offers with unmistakable urgency. Typography runs Roboto at moderate weights — display headlines sit at 28px weight 500, body text at 16px weight 400, and captions at 14px weight 500 — prioritizing readability over typographic drama. Product cards use soft {rounded.sm} corners on images and {rounded.md} on card containers, while primary buttons adopt {rounded.sm} for a clean, professional finish that avoids the playfulness of pill shapes. The color palette extends to a warm accent set (#f78da7 pink, #fcb900 yellow, #00d084 green) used sparingly for category tags and feature highlights, while the neutral system (#222222 ink, #555555 body, #dcdcdc hairline) keeps the layout grounded. The brand's meta theme-color of #000 signals a dark-mode-aware approach, though the primary canvas remains #ffffff. CalDigit's design language communicates reliability through consistent blue dominance, restrained corner radii, and a typographic hierarchy that lets product specifications and pricing do the heavy lifting.

colors:
  primary: "#003399"
  primary-active: "#003388"
  primary-disabled: "#848484"
  ink: "#222222"
  body: "#555555"
  muted: "#848484"
  muted-soft: "#abb8c3"
  hairline: "#dcdcdc"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#ff0000"
  accent-pink: "#f78da7"
  accent-yellow: "#fcb900"
  accent-green: "#00d084"
  accent-blue: "#0693e3"
  accent-purple: "#9b51e0"
  accent-orange: "#ff6900"
  accent-lime: "#7bdcb5"
  accent-coral: "#cf2e2e"
  accent-teal: "#00a154"
  accent-berry: "#e2498a"
  accent-indigo: "#5636d1"
  accent-sky: "#8ed1fc"
  accent-cream: "#ffffb9"
  star-rating: "#fcb900"
  error: "#cf2e2e"
  success: "#00d084"

typography:
  display-xl:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  display-lg:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.36
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  micro-label:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    margin: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep blue #003399 with white text. On hover, the background shifts to #003388 for a subtle darkening effect. The disabled state uses #848484 gray to indicate inactivity. All primary buttons use 8px corner radii and 44px height for consistent touch targets.

**`button-secondary`** — An outlined variant with a white fill and blue border, used for secondary actions like "Learn More" or "Compare Models." The active state darkens the border to #003388 and adds a light gray background. Disabled state fades to gray border and text.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "View Details." The blue text provides clear affordance without visual weight.

**`button-sale`** — A high-urgency button using the red #ff0000 sale badge color, reserved for limited-time offers and promotional pricing. Smaller padding and font size keep it compact within product cards.

### Cards
**`product-card`** — The primary product display container, using a white background with a soft border and 12px corner radius. Each card contains a 4:3 aspect ratio image with 8px rounded corners, a title in 16px weight 500, pricing in 16px weight 400, and optional sale badges. Ratings use the yellow #fcb900 star color.

**`product-card-badge`** — A compact label overlaid on product images, using the red sale color with white text and 4px corner radius. Used for "Sale," "New," or "Limited Edition" flags.

### Navigation
**`nav-bar`** — A 72px sticky header with white background and a subtle bottom border. Navigation links use 16px weight 500 Roboto, with active links highlighted in the primary blue. The bar contains the brand logo, product category links, and a search icon.

**`nav-link-active` / `nav-link-inactive`** — Active nav links render in blue #003399, while inactive links use the body gray #555555. No background or border on individual links — the active state is communicated purely through color.

### Forms
**`text-input`** — Standard text input fields with 44px height, 8px corner radius, and a light gray border. On focus, the border thickens to 2px and turns blue. Error states use a 2px red border with the error color #cf2e2e.

**`select-input`** — Dropdown selectors matching the text input dimensions and styling, with a custom dropdown arrow in the primary blue.

**`search-bar`** — A dedicated search input with 44px height and 8px corner radius, used in the navigation and on search results pages. Focus state mirrors the text input pattern with a blue border.

### Footer
**`footer`** — A dark footer section using the ink color #222222 as background, with white text for headings and muted gray (#abb8c3) for links. Links lighten to full white on hover. The footer contains product categories, support links, company information, and social media icons.

### Tags & Badges
**`category-tag` / `category-tag-active`** — Pill-shaped tags (9999px radius) used for product category filtering. Inactive tags use a light gray background with gray text; active tags switch to the primary blue with white text. Compact padding (4px 12px) keeps them space-efficient.

### Accordion
**`accordion-header` / `accordion-content`** — Expandable sections used for product specifications and FAQ content. Headers use 16px weight 500 with a bottom border, and content sections use 14px weight 400 body text with generous padding.

### Breadcrumbs
**`breadcrumb`** — A secondary navigation pattern using small caption text in muted gray, with the current page rendered in ink color. Separators use the hairline color for visual distinction without weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero section reduces padding to 32px; product cards stack vertically; footer links stack in single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with dropdown; hero section uses 48px padding; search bar remains in nav but expands on focus |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories visible; hero section uses 64px padding; search bar in nav with autocomplete dropdown |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section centers content with max-width; product cards use larger images |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Product card tap targets are the full card area
- Category tags use 32px minimum height for touch accuracy
- Accordion headers are full-width with 44px tap target
- Nav links use 44px minimum tap area

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product category filter strip collapses to a horizontal scrollable row on mobile
- Footer link columns collapse to a single column below 744px
- Product image galleries collapse to single-image swipe on mobile
- Accordion sections collapse by default on all breakpoints
- Search bar collapses to icon-only on mobile, expanding to full-width on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow elevation, border color changes) could not be reliably extracted
- Error message styling for form validation (color, iconography, placement) is inferred from general patterns
- Dark mode styling is not confirmed despite the meta theme-color of #000 — the extracted palette suggests a light-mode-first approach
- Dropdown menu styling for navigation (background, shadow, animation) was not observable
- Modal/overlay styling for product quick-view or cart confirmation is unknown
- Loading states and skeleton screen patterns were not extracted
- The accent color palette (pink, yellow, green, etc.) appears in the extracted hex list but their specific usage contexts (category tags, feature highlights, icons) are inferred from common e-commerce patterns
- Sub-brand or product-line-specific color variations (e.g., Thunderbolt 4 vs. USB-C dock badges) could not be determined
- Animation timing and easing curves are not documented
- Focus ring styling for keyboard navigation (color, offset, width) is not confirmed
- The extracted hex list includes many colors that may be from third-party widgets (Klarna, Afterpay, Shopify Pay) — the brand's true accent palette may be more limited than documented
