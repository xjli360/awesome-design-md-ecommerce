---
version: alpha
name: "Morrow Soft Goods"
source_url: "https://morrowsoftgoods.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Morrow Soft Goods is a bedding brand that speaks in hushed, earthy tones and tactile textures, where every piece feels like a quiet invitation to rest. The palette is anchored by deep, warm browns like {colors.primary} (#423432) and {colors.primary-active} (#5c3d38), which ground the brand in a sense of natural, unpretentious luxury. These are balanced by a range of soft, sun-bleached neutrals—{colors.canvas} (#f7f3ee), {colors.surface-soft} (#e6dcd0), and {colors.surface-card} (#dedede)—that evoke the feel of well-worn linen and aged plaster. Accents of muted gold ({colors.accent-gold} #bcaa75), sage green ({colors.accent-sage} #8ba985), and dusty blue ({colors.accent-blue} #6c8fa3) appear sparingly, like faded threads in a vintage tapestry, while a deeper wine tone ({colors.accent-wine} #542a30) adds a touch of richness. The typography, built on the clean, geometric Brown and the elegant serif freight-big-pro, feels both modern and timeless—display sizes are generous but never shout, and body text is set in a warm, readable weight. Corners are softly rounded ({rounded.sm} 8px for buttons, {rounded.md} 12px for cards), reinforcing a tactile, approachable feel. The overall effect is one of deliberate calm: a brand that trusts the weight of its materials and the quiet power of a well-made bed.

colors:
  primary: "#423432"
  primary-active: "#5c3d38"
  primary-disabled: "#e6dcd0"
  ink: "#121212"
  body: "#423432"
  muted: "#5c3d38"
  muted-soft: "#9f6b18"
  hairline: "#dedede"
  hairline-soft: "#e4d7b7"
  canvas: "#f7f3ee"
  surface-soft: "#e6dcd0"
  surface-card: "#dedede"
  on-primary: "#f7f3ee"
  accent-gold: "#bcaa75"
  accent-gold-light: "#dfca9a"
  accent-sage: "#8ba985"
  accent-sage-soft: "#afaf83"
  accent-blue: "#6c8fa3"
  accent-blue-light: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-wine: "#542a30"
  accent-warm: "#e4d7b7"
  star-rating: "#bcaa75"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'freight-big-pro', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'freight-big-pro', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'freight-big-pro', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'freight-big-pro', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.01px
  body-md:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01px
  caption-sm:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02px
  badge:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.05px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08px
    textTransform: uppercase
  button-md:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05px
    textTransform: uppercase
  link:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Brown', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05px
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
  section: 80px

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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
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
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    border: "1px solid {colors.accent-wine}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-wine}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-sage}"
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
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.accent-gold-light}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  review-card-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-item-title:
    typography: "{typography.title-sm}"
  cart-item-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  cart-item-quantity:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  cart-summary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  cart-summary-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep brown {colors.primary} (#423432) with soft cream text {colors.on-primary} (#f7f3ee). Uses the uppercase Brown font at 14px with 0.05px letter-spacing. On hover, it deepens to {colors.primary-active} (#5c3d38); when disabled, it fades to {colors.primary-disabled} (#e6dcd0) with muted text. The 8px corner radius ({rounded.sm}) keeps the button feeling tactile and approachable.
**`button-secondary`** — A ghost-like alternative with a white canvas background, dark brown text, and a subtle hairline border. Active state swaps the border to {colors.primary-active}. Ideal for "Learn More" or "View Details" actions that need less visual weight.
**`button-ghost`** — A fully transparent button with only text, used for tertiary actions like "Cancel" or "Skip". Maintains the same uppercase Brown typography and 44px height for alignment.
**`button-pill`** — A compact, fully rounded variant used for filters, tags, or quick-actions. Available in filled and outline styles. The outline version uses a transparent background with a hairline border, perfect for category pills or size selectors.

### Cards
**`product-card`** — The core product display unit, featuring a 3:4 aspect ratio image with rounded top corners ({rounded.md}) and a clean white background. The title uses {typography.title-sm} (Brown 500 at 16px) and the price uses {typography.body-sm}. Color swatches are rendered as 20px circles ({rounded.full}) for quick visual selection. The card has no padding—the image bleeds to the top edge, and text is typically padded by the parent grid.
**`review-card`** — A testimonial card with a soft border, light background, and generous padding. The author's name is set in {typography.title-sm} with the brand's primary brown, while the review body uses {typography.body-sm}. Star ratings are rendered in the muted gold {colors.star-rating} (#bcaa75).

### Navigation
**`nav-bar`** — A fixed 72px header with a clean white background. Navigation links use uppercase Brown at 14px with 0.05px letter-spacing. The active link is underlined with a 2px solid {colors.primary} bar. The logo (typically set in freight-big-pro) sits on the left, with links and a search icon on the right. On mobile, the nav collapses into a hamburger menu.
**`footer`** — A deep brown footer ({colors.primary}) with cream text. Links are set in the lighter gold accent ({colors.accent-gold-light} #dfca9a) for contrast. The footer is divided into columns for navigation, customer service, and social links, with generous section padding (80px).

### Forms
**`text-input`** — A standard input field with a white background, 1px hairline border, and 8px corner radius. On focus, it gains a {colors.primary} border and a subtle 2px shadow ring in {colors.primary-disabled}. Error states use a wine-colored border ({colors.accent-wine} #542a30). The 48px height ensures comfortable touch targets.
**`select-input`** — A dropdown selector matching the text-input styling. The dropdown arrow is typically rendered in {colors.body} (#423432).
**`textarea`** — A multi-line input with the same base styling as text-input, but without a fixed height. Used for contact forms or product reviews.
**`quantity-selector`** — A compact, bordered control with a central number and +/- buttons on either side. Each button is 44px wide to meet touch-target requirements. The whole control is 44px tall with 8px corner radius.

### Badges
**`badge-new`** — A small, gold-background badge used to flag new arrivals. Uses uppercase Brown at 11px with 600 weight and 0.05px letter-spacing. The 4px corner radius ({rounded.xs}) keeps it subtle.
**`badge-sale`** — A wine-colored badge for sale or clearance items. Same typography as badge-new.
**`badge-eco`** — A sage-green badge for sustainable or eco-friendly products. Same typography as badge-new.

### Other Components
**`hero-banner`** — A full-width section with a soft background ({colors.surface-soft} #e6dcd0) and large serif typography. The headline uses {typography.display-xl} (48px freight-big-pro) and is paired with a primary CTA button. The banner typically includes a full-bleed background image or pattern.
**`search-bar`** — A pill-shaped search input with a hairline border and a search icon on the left. On focus, the border changes to {colors.primary}. The 48px height and full rounding make it feel friendly and inviting.
**`accordion`** — A bordered, collapsible section used for FAQs or product details. The header uses {typography.title-sm} with an arrow icon that rotates on open. Content is padded with {spacing.base} on top and {spacing.lg} on the sides.
**`divider`** — A simple 1px horizontal line in {colors.hairline} (#dedede). A softer variant uses {colors.hairline-soft} (#e4d7b7) for less visual weight.
**`color-swatch`** — A 32px circular swatch with a hairline border. When selected, the border thickens to 2px and turns {colors.primary}. Used in product detail pages for color selection.
**`cart-item`** — A bordered row in the shopping cart, showing the product image, title, price, and a quantity selector. The title uses {typography.title-sm} and the price uses {typography.body-sm}. Each item is separated by a hairline divider.
**`cart-summary`** — A soft-background panel showing the order subtotal, shipping, and total. The total is emphasized with {typography.title-md}. Used in the cart drawer or checkout sidebar.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; hero banner text reduces to 28px; footer columns stack; search bar becomes full-width; cart drawer overlays full screen |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero banner uses 36px display; footer shows 2-column layout; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero banner at 48px; footer in 4-column layout; search bar in nav with icon |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero banner centered with max-width; all elements maintain comfortable whitespace |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 44px and minimum width of 44px on mobile and tablet.
- Quantity selector buttons are 44px x 44px to meet WCAG touch-target guidelines.
- Color swatches are 32px with 44px tap areas (via padding or invisible hit area).
- Nav links have 44px tap areas even when text is smaller.
- Search bar is 48px tall for easy tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The logo remains centered, and the cart/search icons are moved to the right.
- The product grid collapses from 3-4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- The footer collapses from 4 columns on desktop to 2 columns on tablet and a single column on mobile.
- The hero banner collapses from a side-by-side layout (image + text) to a stacked layout on mobile, with text above the image.
- Accordion components are used on mobile to collapse long lists of product details or FAQs that would otherwise be displayed inline on desktop.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) were inferred from the brand's color palette and common patterns, but exact hover colors (e.g., button-secondary hover) could not be extracted from the live site.
- Error styling for forms (text-input-error, select-input-error) was inferred from the accent-wine color, but actual error messages, icons, and validation patterns were not observed.
- Dark mode is not supported by the brand; all colors assume a light theme.
- Sub-brand or collection-specific palettes (e.g., "Linen Collection" vs. "Cotton Collection") were not observed.
- Focus-visible styles for keyboard navigation (e.g., outline rings) were not extracted and should be implemented with standard accessibility patterns.
- Animation and transition durations (e.g., button hover, accordion open/close) were not specified; a default of 200ms ease-in-out is recommended.
- The exact font weights for freight-big-pro (e.g., 300, 400, 600) were not fully confirmed; only 400 was observed for display sizes.
- Shopify-specific components (e.g., cart drawer, product form, variant selector) were inferred from common patterns but not directly observed.
- The brand's icon set and icon sizes were not extracted; a consistent 24px icon size with 20px for smaller contexts is assumed.
