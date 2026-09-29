---
version: alpha
name: "Patrick Ta Beauty"
source_url: "https://patrickta.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Patrick Ta Beauty is a professional makeup brand that lives at the intersection of editorial glamour and everyday wearability, built on a canvas of soft, muted neutrals and punctuated by a signature sage green (#aaccaa) that feels both fresh and grounded. The brand's visual language is deliberately restrained — a palette of warm grays (#3a3a3a, #333333, #242424) and cool silvers (#e1e3e4, #c7c7c7, #cccccc, #dedede, #efefef) creates a sophisticated backdrop that lets product textures and the human face take center stage. A crisp accent blue (#1990c6) and its deeper active state (#136f99) provide the only real color voltage, used sparingly for interactive elements and wayfinding. The typography is clean and unassuming — Arial and Helvetica in standard weights — never competing with the photography, while generous whitespace and soft corners ({rounded.sm} for buttons, {rounded.md} for cards) keep the experience approachable. This is a brand that trusts its product shots and video content to do the heavy lifting, using the design system as a quiet, elegant frame rather than a loud voice.

colors:
  primary: "#aaccaa"
  primary-active: "#8fb88f"
  primary-disabled: "#d4e8d4"
  ink: "#121212"
  body: "#242424"
  muted: "#3a3a3a"
  muted-soft: "#6a6a6a"
  hairline: "#cccccc"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#efefef"
  surface-card: "#ffffff"
  on-primary: "#121212"
  accent-blue: "#1990c6"
  accent-blue-active: "#136f99"
  badge-new: "#aaccaa"
  badge-sale: "#1990c6"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.29
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  button-text-active:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  button-icon-circle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.accent-blue}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 40px 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-swatches:
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 500px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "1px solid {colors.hairline-soft}"
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature sage green ({colors.primary}) with dark text ({colors.on-primary}) for contrast. Uses uppercase, 600-weight type at 14px with 0.5px letter-spacing. On hover/active, shifts to a deeper green ({colors.primary-active}); disabled state fades to a pale sage ({colors.primary-disabled}) with muted text. All variants share a soft 8px corner radius ({rounded.sm}) and consistent 44px height.

**`button-secondary`** — An outlined alternative for less prominent actions, built on a white canvas with a 1px hairline border ({colors.hairline}). Active state inverts the border to {colors.ink} and adds a soft background ({colors.surface-soft}). Typography matches the primary button's uppercase, 600-weight style, maintaining visual hierarchy without competing for attention.

**`button-text`** — A borderless, background-free option for tertiary actions like "Cancel" or "Learn More." Hover/active state introduces the accent blue ({colors.accent-blue}) as a subtle signal. Used primarily in forms, modals, and inline contexts where visual weight must be minimized.

**`button-icon-circle`** — A 40px circular icon button for utility actions (search, cart, close, menu). The default state uses a soft gray background ({colors.surface-soft}); active state fills with the brand green ({colors.primary}) for clear feedback. The full border radius ({rounded.full}) keeps the shape friendly and tactile.

### Cards
**`product-card`** — The core shopping unit, a white card with a 12px corner radius ({rounded.md}) containing a square product image, title in 16px/600 weight, price in 14px/400 weight, and optional color swatches. The image uses a top-only radius ({rounded.md} {rounded.md} 0 0) to create a clean break between photography and text content. No shadow or border — the card relies on the white canvas against the soft page background for separation.

**`product-card-swatches`** — A row of 24px circular color swatches ({rounded.full}) with a soft hairline border. The selected swatch gains a 2px ink border for clear indication. Swatches are spaced at 4px ({spacing.xs}) and sit below the price, allowing shoppers to see available shades without navigating to the product page.

### Navigation
**`nav-bar`** — A fixed 72px white header with a subtle bottom border ({colors.hairline-soft}). Navigation links use 13px uppercase, 600-weight type with 0.5px letter-spacing. Active links are indicated by a 2px bottom border in {colors.ink}; inactive links render in {colors.muted}. The bar contains the brand logo, category links, search icon, cart icon, and account icon.

**`nav-link-active`** / **`nav-link-inactive`** — The two states for top-level navigation items. Active state uses {colors.ink} with a 2px underline; inactive state uses {colors.muted} with no underline. Both share the same uppercase, 600-weight typography to maintain consistent rhythm across the nav bar.

### Forms
**`text-input`** — A standard 48px input field with a 1px hairline border ({colors.hairline}) and 8px corner radius ({rounded.sm}). On focus, the border shifts to {colors.ink} for clear visual feedback. Error state uses the accent blue ({colors.accent-blue}) as the border color — a deliberate choice to avoid red, keeping the error state within the brand's cool, composed palette.

**`select`** — A dropdown variant of the text input, with additional 40px right padding to accommodate a custom chevron icon. Shares the same dimensions, border, and focus behavior as the text input, maintaining consistency across form elements.

**`quantity-selector`** — A compact 40px control for adjusting product quantities, with a 1px hairline border and 8px corner radius. Contains a minus button, the current quantity, and a plus button, all in 16px body type. Used exclusively on product detail pages and cart line items.

### Badges
**`badge-new`** — A small, uppercase label in the brand green ({colors.badge-new}) with dark text, signaling new arrivals. Uses 10px/700 weight type with 0.5px letter-spacing and a 4px corner radius ({rounded.xs}). Positioned at the top-left of product card images.

**`badge-sale`** — A similar label in the accent blue ({colors.badge-sale}) with white text, used for promotional pricing. Shares the same typography and dimensions as the new badge but uses the brand's secondary color to differentiate the message type.

### Footer
**`footer`** — A dark section anchored in {colors.ink} with white text, providing a visual bookend to the light, airy page. Links render in white with a hover state that shifts to the brand green ({colors.primary}). The footer contains newsletter signup, navigation columns, social links, and legal text, all in 14px/400 weight type.

### Tabs
**`tab-active`** / **`tab-inactive`** — Used for product category filtering and content sections. Active tabs use {colors.ink} with a 2px bottom border; inactive tabs use {colors.muted} with no border. Both share the same uppercase, 600-weight nav-link typography, ensuring the active state is communicated through color and underline alone, not font weight changes.

### Accordion
**`accordion`** — A collapsible section used on product detail pages (for ingredients, how-to-use, etc.) and the footer. Each item has a 16px/600 weight title with a soft hairline bottom border ({colors.hairline-soft}). The content area uses 14px/400 weight body type and appears with a 12px top padding when expanded.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, hero height reduces to 300px, footer stacks vertically, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, nav links show as condensed text, hero height at 400px, footer uses two-column layout, search bar remains full-width |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, hero height at 500px, footer uses four-column layout, search bar in nav |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero height at 550px, all elements use max-width constraints |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons use 40px minimum dimensions with adequate padding
- Color swatches are 24px with 4px spacing, meeting touch target recommendations when grouped
- Product card tap targets include the entire card surface, not just text links
- Accordion headers are 48px minimum for easy tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer for category links
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer navigation columns stack vertically below 744px, with accordion-style expansion for each column
- Hero banners reduce image height and stack text below the image on mobile
- Product image galleries switch from thumbnail grid to swipeable carousel on touch devices
- Search transitions from inline input to full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components were inferred from common patterns rather than extracted from the live site
- Error state styling for forms (colors, icons, message placement) was not reliably observed
- Dark mode or high-contrast mode specifications are absent
- Sub-brand or collection-specific palette variations (e.g., limited edition drops) were not captured
- Animation and transition timing values (durations, easing curves) were not extractable
- Modal, tooltip, and popover component specifications are missing
- Loading states (skeleton screens, spinners) and their dimensions were not observed
- Typography line-height and letter-spacing values were estimated based on standard Arial rendering
- Specific padding and margin values for many components were inferred from common e-commerce patterns
- The exact border radius for product cards was estimated; the live site may use a different value
- Color swatch border styles and selection indicators were inferred from industry standards
- The accent blue (#1990c6) usage was observed but its exact role (links, badges, errors) was partially inferred
