---
version: alpha
name: "Ezpz"
source_url: "https://ezpzfun.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A feeding brand that builds its entire visual world around a single, unexpected color: #aaccaa — a muted sage-green that appears nowhere in the baby-product aisle's usual pastel-pink-and-blue vocabulary. This sage serves as the brand's primary voltage, appearing on buttons, badges, and the signature silicone mats that define the product line. The palette is anchored by a warm off-white canvas (#f6f6f6) and a secondary teal (#73bec4) that echoes the meta-theme-color and adds a watery, calming counterpoint. Typography runs DM Sans at moderate weights — display headlines sit at 500–600 weight rather than the heavy 700+ common in e-commerce, letting the product photography and the brand's distinctive rounded forms carry the visual weight. Every corner is soft: buttons use `{rounded.sm}`, product cards use `{rounded.md}`, and the brand's signature Happy Mat and Mini Mat feature `{rounded.full}` pill-shaped elements that mirror the silicone's actual physical curves. The result is a system that feels less like a feeding-supply store and more like a pediatrician's waiting room designed by a ceramicist — clean, reassuring, and unexpectedly sophisticated. The accent red (#fb8077) appears sparingly on sale badges and error states, providing just enough tension against the sage-and-teal calm.

colors:
  primary: "#aaccaa"
  primary-active: "#8fb88f"
  primary-disabled: "#d4e6d4"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e1e3e4"
  canvas: "#f6f6f6"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#73bec4"
  accent-red: "#fb8077"
  accent-red-active: "#e0665e"
  accent-sage: "#aaccaa"
  badge-sale: "#fb8077"
  badge-new: "#73bec4"
  star-rating: "#494949"

typography:
  display-xl:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  badge:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill-sage:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 4px
  product-card-price:
    typography: "{typography.body-md}"
    padding: 0px 12px 12px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 48px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0px
  accordion-body:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0px 0px 16px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with sage green (#aaccaa) and white text. Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#8fb88f). Disabled state uses `{colors.primary-disabled}` (#d4e6d4) with white text at 50% opacity. All primary buttons use `{rounded.sm}` (8px) for a soft, approachable feel that mirrors the silicone products.

**`button-secondary`** — An outlined variant on white canvas with ink text, used for secondary actions like "Learn More" or "View Details". Hover state adds a thin sage border. The `button-secondary-outline` variant uses a transparent background with a sage border and text, ideal for placement over product imagery.

**`button-accent-teal`** — A secondary CTA variant using the brand's teal accent (#73bec4), deployed for "Subscribe & Save" flows and loyalty-program signups. Same sizing and radius as primary.

**`button-pill-sage`** — A fully pill-shaped (`{rounded.full}`) button used for filter tags, category pills, and mobile navigation chips. Smaller typography and tighter padding than full-size buttons.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners containing a product image, title, and price. The image itself is also rounded (`{rounded.md}`), creating a double-radius effect that softens the product presentation. Cards sit on the `{colors.canvas}` (#f6f6f6) background, creating subtle separation. On hover, a thin sage border appears and a subtle shadow lifts the card 2px.

**`badge-sale`** — A small red (#fb8077) badge with uppercase white text, placed at the top-left corner of product cards. Uses `{rounded.xs}` (4px) for a tight, precise look. `badge-new` uses teal (#73bec4) for new arrivals, and `badge-sage` uses the primary sage for bestsellers or award-winners.

### Navigation
**`nav-bar`** — A 72px white bar with uppercase nav links in `{typography.nav-link}` (14px, weight 500). The logo sits left-aligned, with links centered or right-aligned. Active links use sage text; inactive links use muted gray. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link-active`** — Active navigation items use the brand's primary sage color, creating a clear wayfinding signal against the white header.

### Forms & Inputs
**`text-input`** — A white input field with `{rounded.sm}` (8px) corners and 48px height. On focus, a 2px sage border appears. Placeholder text uses `{colors.muted}` (#777777). Error state uses a 2px red (#fb8077) border with red caption text below.

**`search-bar`** — A fully pill-shaped search input (`{rounded.full}`) with a magnifying glass icon in sage. Used in the header and on collection pages. 48px height with generous padding for touch targets.

**`quantity-selector`** — A compact 40px control with minus/plus buttons flanking a numeric display. Sage accent on the buttons, white background, `{rounded.sm}` corners.

### Footer
**`footer-section`** — A dark footer on `{colors.ink}` (#121212) with white text. Links use `{typography.link}` (14px, weight 500) and are white. The footer includes columns for support, shop, about, and social links. A thin hairline (#3a3a3a) separates sections.

### Accordion
**`accordion-header`** — Used for product descriptions, FAQs, and shipping details. A title-sm weight with a chevron icon that rotates on open. No background, full-width tap target. `accordion-body` uses body-sm typography with 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, full-width buttons, reduced hero padding (24px) |
| Tablet | 744–1128px | Two-column product grid, visible top nav with condensed links, 32px hero padding |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, 48px hero padding, sidebar filters on collection pages |
| Wide | > 1440px | Max-width container at 1440px, centered layout, four-column product grid, expanded hero with larger typography |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card tap targets cover the full card area, not just the title or price
- Accordion headers have full-width tap targets at 48px minimum height
- Quantity selector buttons are 40px × 40px minimum
- Mobile nav links have 48px tap targets

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack vertically on mobile, with accordion-style expand/collapse for each section
- Hero section reduces padding and stacks CTA below headline on mobile
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Filter sidebar collapses to a horizontal scroll strip on tablet and a bottom sheet on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and outline buttons could not be reliably extracted from the live site — the `button-secondary-outline` hover is inferred from brand patterns
- Error and success form states (beyond the red border noted) are not documented from live extraction
- Dark mode is not present on the live site and has not been designed
- Sub-brand or collection-specific palette variations (e.g., holiday, limited edition) are not captured
- The exact font-weight mapping for DM Sans across all typography tokens is inferred from common usage — the live site may use slightly different weights
- Animation durations and easing curves (hover transitions, page loads, accordion open/close) were not extractable
- The star-rating component's exact sizing and spacing between stars is inferred from typical e-commerce patterns
- Shopify-specific checkout button colors (Shopify Pay, Afterpay, Klarna) are not included as they are platform defaults, not brand decisions
