---
version: alpha
name: "Makeup by Mario"
source_url: "https://www.makeupbymario.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Makeup by Mario is a masterclass in quiet confidence. The brand speaks in a hushed, sophisticated tone, using a palette anchored by deep, almost-black charcoals like `#1f1d1d` and `#121212` against a pristine `#f9f9f9` canvas. This isn't a stark, clinical minimalism; it's a warm, tactile luxury. The primary action color, a muted slate blue (`#1f2a34`), avoids the typical cosmetic pink or red, signaling a focus on artistry over trend. Accents of a brighter, almost electric blue (`#1990c6`) and its deeper variant (`#136f99`) appear sparingly, like a flash of inspiration on a neutral eye. Typography is a deliberate mix: the clean, geometric `TradeGothicLT` for headlines and body copy provides a modern, editorial structure, while the occasional use of `Adelaila-Brush` introduces a hand-drawn, artisanal warmth, perhaps in product names or signature quotes. The overall feel is that of a high-end art studio—controlled, intentional, and deeply personal. Corners are softly rounded (`{rounded.sm}` to `{rounded.md}`), never harsh, and generous whitespace (`{spacing.section}`) gives every product room to breathe. The brand trusts its imagery and the weight of its founder's name, letting the design recede into a supporting role that feels both premium and approachable.

colors:
  primary: "#1f2a34"
  primary-active: "#136f99"
  primary-disabled: "#8a8585"
  ink: "#1f1d1d"
  body: "#1f1f1f"
  muted: "#8a8585"
  muted-soft: "#dedede"
  hairline: "#dedede"
  hairline-soft: "#f9f9f9"
  canvas: "#f9f9f9"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#f9f9f9"
  accent-blue: "#1990c6"
  accent-blue-deep: "#136f99"
  star-rating: "#1f1d1d"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'TradeGothicLT', 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 1px
    textTransform: uppercase
  script-display:
    fontFamily: "'Adelaila-Brush', 'TradeGothicLT', 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    padding: 14px 0
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
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid #c13515"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
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
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  product-card-rating:
    typography: "{typography.caption}"
    color: "{colors.star-rating}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "#c13515"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-best-seller:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Bag", "Checkout", and key conversion points. It features a deep slate blue (`{colors.primary}`) background with light text (`{colors.on-primary}`). On hover or active, it transitions to a brighter accent blue (`{colors.primary-active}`). When disabled, it fades to a muted gray (`{colors.muted}`). The button uses uppercase, letter-spaced typography (`{typography.button-md}`) and has a soft 8px corner radius (`{rounded.sm}`).
**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Save for Later". It has a transparent background with a subtle border (`{colors.hairline}`) and dark text (`{colors.ink}`). On active state, the border becomes solid ink (`{colors.ink}`) and the background shifts to the soft canvas (`{colors.surface-soft}`).
**`button-tertiary-text`** — A text-only button for subtle actions like "Clear" or "Cancel". It has no background or border, relying solely on the `{typography.button-md}` typography and `{colors.ink}` color. On hover, the text color shifts to `{colors.primary-active}`.

### Navigation
**`nav-bar`** — A clean, fixed-position top navigation bar with a white canvas background (`{colors.canvas}`) and a soft bottom border (`{colors.hairline-soft}`). It stands 72px tall and uses compact, uppercase nav links (`{typography.nav-link}`). The logo (likely a script or wordmark) sits on the left, with navigation links centered or right-aligned.
**`nav-link-active`** — The active navigation link is indicated by a 2px solid underline in `{colors.ink}`. The link text remains dark (`{colors.ink}`).
**`nav-link-inactive`** — Inactive navigation links are rendered in a muted gray (`{colors.muted}`) with no underline, receding into the background until hovered.

### Cards
**`product-card`** — The primary product display unit, used in grid and list views. It has a white background (`{colors.canvas}`) and a 12px corner radius (`{rounded.md}`). The card is clean and uncluttered, relying on high-quality product photography. It contains an image area, a product title (`{typography.title-sm}`), a price (`{typography.body-sm}`), and an optional rating.
**`product-card-image`** — The image area within a product card, maintaining a 1:1 aspect ratio. The top corners are rounded to match the card (`{rounded.md} {rounded.md} 0 0`), creating a seamless visual flow.

### Forms
**`text-input`** — Standard text input for forms, such as email, name, or address fields. It has a white background (`{colors.canvas}`), a subtle border (`{colors.hairline}`), and an 8px corner radius (`{rounded.sm}`). On focus, the border becomes solid ink (`{colors.ink}`). Error states use a red border (`#c13515`).
**`select-dropdown`** — A styled dropdown selector for options like size, shade, or quantity. It mirrors the `text-input` styling for visual consistency.
**`newsletter-input`** — A dedicated input for the email newsletter signup, typically found in the footer. It shares the same styling as `text-input` but is paired with a `newsletter-submit` button.
**`newsletter-submit`** — The submit button for the newsletter signup form. It uses the `{colors.primary}` background and `{typography.button-sm}` for a compact, action-oriented appearance.

### Badges
**`badge-new`** — A small, bright blue (`{colors.accent-blue}`) badge used to denote newly launched products. It uses uppercase, tightly tracked typography (`{typography.badge}`) and has a 4px corner radius (`{rounded.xs}`).
**`badge-sale`** — A red badge (`#c13515`) for sale or discounted items, following the same structural pattern as `badge-new`.
**`badge-best-seller`** — A dark badge (`{colors.ink}`) for best-selling products, providing a high-contrast, premium label.

### Search
**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) with a soft background (`{colors.surface-soft}`) and a subtle border (`{colors.hairline}`). It is designed to be inviting and unobtrusive. On focus, the background becomes white (`{colors.canvas}`) and the border becomes solid ink (`{colors.ink}`).

### Footer
**`footer-section`** — The site footer, which uses a deep, almost-black background (`{colors.ink}`) to create a strong visual anchor. It contains navigation links, social media icons, and a newsletter signup form. Text is rendered in light tones (`{colors.on-primary}` and `{colors.muted-soft}`).
**`footer-link`** — Footer navigation links are styled in a muted light gray (`{colors.muted-soft}`) and transition to full white (`{colors.on-primary}`) on hover.

### Product Detail
**`color-swatch`** — A circular swatch (`{rounded.full}`) for displaying product color options. It is 32x32px with a subtle border (`{colors.hairline}`). The selected state (`color-swatch-selected`) uses a 2px solid ink border (`{colors.ink}`) for clear indication.
**`quantity-selector`** — A compact input for selecting product quantity, with a white background and a subtle border. It is 40px tall with 8px internal padding.

### Accordion
**`accordion-header`** — Used for collapsible sections like product details, ingredients, or shipping information. It has no background, uses `{typography.title-sm}`, and is separated by a soft bottom border (`{colors.hairline-soft}`).
**`accordion-content`** — The expandable content area below the accordion header. It uses `{typography.body-sm}` and has padding to create a clear visual hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grids, hamburger menu replaces top nav, hero banners stack text and image, search bar collapses to icon-only, footer links stack vertically, product cards use full width. |
| Tablet | 744–1128px | Two-column product grids, top nav remains visible but may condense, hero banners use a 50/50 split, search bar is full-width, footer links in a 2-column layout. |
| Desktop | 1128–1440px | Three or four-column product grids, full top nav with all links visible, hero banners use a 60/40 split, search bar is a prominent pill, footer links in a 4-column layout. |
| Wide | > 1440px | Maximum content width is capped at 1440px, centered on the screen. Product grids may expand to 4 or 5 columns. All layouts remain consistent with desktop, with increased whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card images and swatches are tappable, with a minimum size of 48x48px.
- Accordion headers have a minimum height of 48px to ensure easy tapping.
- Navigation links have a minimum height of 44px and adequate padding.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The menu overlay uses a full-screen drawer with a scrim (`{colors.scrim}`) at 50% opacity.
- Product filters and sorting options collapse into a slide-out drawer or a modal on mobile.
- The footer's multi-column layout collapses into a single column, with accordion-style sections for each link group.
- Hero banners stack vertically on mobile, with the image taking full width and the text content below.
- Product image galleries switch from a thumbnail strip to a swipeable carousel on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover States**: While active and focus states are defined for primary and secondary buttons, hover states for many components (e.g., nav links, footer links, product cards) were not explicitly extracted from the live site and rely on inferred patterns.
- **Error Styling**: Only a basic error border color (`#c13515`) is defined for text inputs. Error message typography, iconography, and form-level error states are not specified.
- **Dark Mode**: No dark mode palette or behavior was detected. The brand's use of a light canvas (`#f9f9f9`) and dark ink (`#1f1d1d`) suggests a light-mode-first approach.
- **Sub-brand Palettes**: The brand may have specific palettes for collaborations or limited-edition collections (e.g., a "Mario Masterclass" series) that were not captured.
- **Animation & Transition**: No timing, easing, or animation properties were extracted. The brand likely uses subtle transitions (e.g., 0.2s ease-in-out for button hovers) but these are not defined.
- **Iconography**: The specific icon set (e.g., custom line icons vs. a library like Phosphor) and their styling (stroke width, size, color) were not extracted.
- **Typography Scale**: The `script-display` token for `Adelaila-Brush` is an inferred addition based on the font declaration. Its exact usage (e.g., in hero headlines or product titles) is not confirmed.
- **Spacing Scale**: The `section` spacing value of 80px is an estimate based on common luxury e-commerce patterns and may differ from the live site's exact implementation.
- **Component States**: Missing states include `:visited` for links, `:focus-visible` for all interactive elements, and `:disabled` for inputs and select dropdowns.
