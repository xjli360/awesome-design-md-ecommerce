---
version: alpha
name: "Goal Zero"
source_url: "https://www.goalzero.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A #cad618 lime-green voltage cuts across a charcoal-and-stone palette — the brand's primary is not a cautious safety green but a charged, almost citrus chartreuse that signals energy rather than hazard. This single hex carries every primary CTA, add-to-cart button, and power-indicator accent across a site built on a #efefef canvas and #212121 ink. The typography stack is a curious hybrid: Galaxie Polaris (a sharp, condensed geometric sans) for display and navigation, paired with system fallbacks that suggest the brand hasn't fully committed to a single type system — the condensed book weight appears in product titles while body copy defaults to -apple-system. Product cards use {rounded.sm} corners and sit on a #ffffff surface-card with a #e8e9eb hairline, creating a clean but utilitarian grid that prioritizes spec readability over lifestyle photography. The search bar is a full-width {rounded.full} pill in #f3f3f3, and the primary button uses a full-height {rounded.sm} rectangle in the signature lime — no gradient, no shadow, just flat color on a white canvas. A secondary #1c9ad6 blue appears in link text and informational badges, likely inherited from a legacy Shopify or utility palette, while #d20000 red marks sale prices and error states. The overall feel is industrial but approachable: a tool brand that trusts its product photography to sell, using color as a functional signal rather than a decorative flourish.

colors:
  primary: "#cad618"
  primary-active: "#bfd22b"
  primary-disabled: "#e8e9eb"
  ink: "#212121"
  body: "#3d4246"
  muted: "#6b6a6b"
  muted-soft: "#acacac"
  hairline: "#e8e9eb"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#231f20"
  link: "#1c9ad6"
  sale: "#d20000"
  badge-green: "#145623"
  badge-blue: "#003f84"
  badge-teal: "#0b545f"
  badge-amber: "#846403"
  badge-red: "#721b23"
  meta-theme: "#7796a8"

typography:
  display-xl:
    fontFamily: "'Galaxie Polaris Condensed', 'GalaxiePolaris-Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Galaxie Polaris Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Galaxie Polaris Book', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Galaxie Polaris Book', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Galaxie Polaris Book', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  price-sale:
    fontFamily: "'Galaxie Polaris', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
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
    textColor: "{colors.muted}"
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
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.sale}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.sale}"
  product-card-compare-price:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  rating-stars:
    color: "{colors.primary}"
    fontSize: 16px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the signature #cad618 lime on a #231f20 dark text. Uses {rounded.sm} corners and a compact 44px height. On hover, shifts to the slightly warmer #bfd22b variant. Disabled state drops to #e8e9eb with muted text — the button disappears into the canvas rather than signaling unavailability with a red or gray. **`button-secondary`** — An outlined variant with a 2px #212121 border on white canvas, same 44px height and {rounded.sm}. Active state fills the background with #f3f3f3. **`button-ghost`** — Text-only with transparent background, used for tertiary actions like "Learn more" or "Cancel". **`button-pill-primary`** and **`button-pill-outline`** — Pill-shaped variants ({rounded.full}) used in filter strips and category navigation, with smaller 13px type and tighter padding.

### Text Inputs & Forms
**`text-input`** — Standard 44px input with 1px #e8e9eb border and {rounded.sm}. Focus state gains a 2px #cad618 border — the lime green acts as a focus indicator rather than a blue or teal. Error state uses a 2px #d20000 border. **`select-dropdown`** — Matches text-input dimensions and border styling, used for product filters and quantity selection. **`search-bar`** — A full-width {rounded.full} pill in #f3f3f3 with a 1px hairline border, 48px height, and body-md type. The search icon sits in the left padding, and the placeholder text reads in the brand's body gray.

### Navigation
**`nav-bar`** — A 64px white bar with a 1px #e8e9eb bottom border. Logo sits left-aligned, nav links are uppercase 14px Galaxie Polaris with 0.5px letter-spacing. The active link state underlines with a 2px #cad618 border. Secondary navigation (account, cart) sits right-aligned with icon buttons. **`nav-link`** — Uppercase, 14px, weight 600, with 12px horizontal padding. Active state inherits the primary lime underline.

### Product Cards
**`product-card`** — A white card with 1px #e8e9eb border and {rounded.sm}. The image area uses {rounded.sm} on top corners only. Below the image: product title in title-sm, price in 18px Galaxie Polaris weight 600, and a small badge for stock status or promotion. **`product-card-badge`** — Small uppercase label in #145623 green on white, using {rounded.xs} and 2px/8px padding. Sale prices render in #d20000 with the original price struck through in #acacac.

### Hero & Sections
**`hero-section`** — Full-width section on a #f3f3f3 background with 64px vertical padding. Uses display-xl (36px condensed) for the headline and a single primary CTA button. Product hero variants may swap the background for a product image with a dark scrim overlay. **`accordion-header`** — Product detail accordions (specs, features, manuals) use a title-sm type on white with a bottom hairline. Content area drops to body-sm in #3d4246.

### Footer
**`footer`** — A dark #212121 background with white text. Links render in #acacac body-sm. The footer is divided into columns for product categories, support, and company info, with a newsletter signup form using the standard text-input pattern inverted on dark background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 32px; buttons go full-width; accordions replace tabbed content |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 28px display-lg; search bar remains full-width |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero uses 36px display-xl; search bar constrained to 640px max-width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with 1200px inner max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Product card tap targets (add to cart, quick view) are minimum 44x44px
- Nav hamburger icon is 48x48px on mobile
- Quantity selector +/- buttons are 44x44px
- Accordion headers are minimum 48px tall for tap targets

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer columns collapse to a single-column accordion below 744px
- Product image galleries collapse from thumbnails to dot indicators on mobile
- Tabbed content (specs, features, reviews) collapses to accordion below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from static CSS — only primary button active state was confirmed
- Error state styling for forms (beyond the red border) is inferred; actual error message typography and iconography were not visible
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or collection-specific color palettes (e.g., Yeti, Boulder, Sherpa product lines) may exist but were not extracted
- The Galaxie Polaris font family appears in multiple weights (Book, Condensed, Condensed Book, Medium) but exact weight-to-style mappings are inferred from common usage patterns
- Animation and transition durations (button hover, card lift, nav dropdown) were not extractable
- The #7796a8 meta-theme color appears in the page head but its usage in the UI is unclear — may be a legacy or placeholder value
- Shopify-specific checkout and cart drawer styling was not analyzed; those components may use a different color palette
- Accessibility contrast ratios between #cad618 on white and #231f20 on #cad618 have not been verified against WCAG standards
