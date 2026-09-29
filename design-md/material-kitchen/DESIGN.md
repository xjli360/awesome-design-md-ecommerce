---
version: alpha
name: "Material Kitchen"
source_url: "https://materialkitchen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, earthy cookware brand that feels like a well-loved cast-iron pan — warm, grounded, and built to last. Material Kitchen’s palette is drawn from the soil and the sea: a primary green of {colors.primary} (#1d423c) that reads as forest shadow, not minty freshness, supported by a secondary green {colors.primary-active} (#1d322d) that deepens into almost-black. The canvas is a soft, buttery off-white {colors.canvas} (#f8f8f5) that avoids clinical brightness, while the body text sits in a dark olive-charcoal {colors.body} (#3c454f) rather than pure black — a choice that softens the reading experience without sacrificing legibility. Accent colors arrive sparingly: a warm brass {colors.accent-gold} (#e3b052) for highlights and badges, a dusty sage {colors.accent-sage} (#9cc1c3) for secondary surfaces, and a terra-cotta {colors.accent-terracotta} (#d58552) that appears in product photography overlays and sale indicators. Typography leans on a refined serif voice: display headlines use Teodor or Garamond at generous sizes, while body copy runs Freight Text Pro and sofia-pro for a clean, editorial feel. Rounded corners are present but restrained — {rounded.sm} (8px) on buttons and {rounded.md} (12px) on cards — never cartoonishly pill-shaped. The overall effect is a brand that trusts materiality: the weight of a knife, the grain of a cutting board, the quiet confidence of a well-designed kitchen tool.

colors:
  primary: "#1d423c"
  primary-active: "#1d322d"
  primary-disabled: "#8aab9d"
  ink: "#10201c"
  body: "#3c454f"
  muted: "#666e73"
  muted-soft: "#9cc1c3"
  hairline: "#cbcac0"
  hairline-soft: "#dad6c5"
  border-strong: "#a86f5f"
  canvas: "#f8f8f5"
  surface-soft: "#fdfcee"
  surface-card: "#ffffff"
  surface-strong: "#ebe1d0"
  on-primary: "#fdfcee"
  on-dark: "#fdfcee"
  accent-gold: "#e3b052"
  accent-sage: "#9cc1c3"
  accent-terracotta: "#d58552"
  accent-rust: "#a86f5f"
  accent-clay: "#dbbea5"
  accent-slate: "#275259"
  accent-rose: "#dfbfb9"
  accent-lavender: "#cba3d8"
  accent-oak: "#d9b087"
  accent-umber: "#161010"
  star-rating: "#e3b052"
  scrim: "#10201c"
  error: "#d58552"
  success: "#1d423c"
  info: "#7ba4db"

typography:
  display-xl:
    fontFamily: "'Teodor', 'Garamond', 'Rom', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Teodor', 'Garamond', 'Rom', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Teodor', 'Garamond', 'Rom', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Teodor', 'Garamond', 'Rom', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'freight-text-pro', 'Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'freight-text-pro', 'Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'freight-text-pro', 'Garamond', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'sofia-pro', 'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'freight-text-pro', 'Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'freight-text-pro', 'Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-terracotta}"

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
    padding: 14px 28px
    height: 48px
    border: none
    cursor: pointer
    transition: background-color 0.2s ease
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid "{colors.primary}"
    cursor: pointer
    transition: background-color 0.2s ease, color 0.2s ease
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: none
    cursor: pointer
    textDecoration: underline
  button-tertiary-hover:
    textColor: "{colors.primary-active}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
    padding: 8px
    border: none
    cursor: pointer
  button-icon-hover:
    backgroundColor: "{colors.surface-soft}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
    border: none
    cursor: pointer
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 36px
    border: 1px solid "{colors.hairline}"
    cursor: pointer
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    outlineColor: "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
    boxShadow: "0 0 0 3px rgba(29, 66, 60, 0.15)"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: 1px solid "{colors.hairline}"
    minHeight: 120px
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: 2px solid "{colors.hairline}"
    rounded: "{rounded.xs}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "{colors.primary}"
    size: 20px
  radio:
    backgroundColor: "{colors.canvas}"
    border: 2px solid "{colors.hairline}"
    rounded: "{rounded.full}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "{colors.primary}"
    size: 20px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
    padding: "0 {spacing.xl}"
  top-nav-logo:
    height: 32px
    width: auto
  top-nav-link:
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    hoverTextColor: "{colors.primary}"
  top-nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: 2px solid "{colors.primary}"
  top-nav-icon:
    textColor: "{colors.body}"
    size: 20px
    hoverTextColor: "{colors.primary}"
  mobile-nav-toggle:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    size: 24px
    padding: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
    backgroundColor: "{colors.canvas}"
  search-icon:
    textColor: "{colors.muted}"
    size: 18px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: 1px solid "{colors.hairline-soft}"
    overflow: hidden
    transition: box-shadow 0.2s ease
  product-card-hover:
    boxShadow: "0 4px 20px rgba(16, 32, 28, 0.08)"
    border: 1px solid "{colors.hairline}"
  product-card-image:
    aspectRatio: "1 / 1"
    objectFit: cover
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-terracotta}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sold-out:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.canvas}"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    border: none
    cursor: pointer
    opacity: 0
    transition: opacity 0.2s ease
  product-card-hover-add-to-cart:
    opacity: 1
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 500px
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 28px"
    height: 48px
    marginTop: "{spacing.lg}"
  hero-image:
    objectFit: cover
    width: 100%
    height: 100%
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: 1px solid "{colors.hairline-soft}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
    hoverOpacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.sm}"
  footer-newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 40px
    border: none
    placeholderColor: "{colors.muted}"
  footer-newsletter-button:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: none
    cursor: pointer
  footer-social-icon:
    textColor: "{colors.on-primary}"
    size: 20px
    opacity: 0.8
    hoverOpacity: 1
  footer-bottom:
    borderTop: 1px solid "rgba(253, 252, 238, 0.2)"
    paddingTop: "{spacing.base}"
    marginTop: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    display: inline-flex
    alignItems: center
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.canvas}"
  badge-sold-out:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
  badge-best-seller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
    gap: 2px
  star-rating-empty:
    color: "{colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.hairline}"
    height: 40px
    padding: "0 {spacing.sm}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    size: 20px
    padding: "{spacing.xs}"
    border: none
    cursor: pointer
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: 1px solid "{colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    cursor: pointer
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    paddingTop: "{spacing.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    textColor: "{colors.body}"
    hoverTextColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.base} 0"
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 2px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    fontSize: 11px
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    maxWidth: 600px
    boxShadow: "0 10px 40px rgba(16, 32, 28, 0.15)"
  modal-overlay:
    backgroundColor: "rgba(16, 32, 28, 0.5)"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.body}"
    size: 24px
    position: absolute
    top: "{spacing.base}"
    right: "{spacing.base}"
    border: none
    cursor: pointer
  notification:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: 1px solid "{colors.hairline-soft}"
  notification-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    border: none
  notification-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.canvas}"
    border: none
  notification-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.canvas}"
    border: none
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.full}"
    width: 24px
    height: 24px
    animation: spin 0.8s linear infinite
  skeleton:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    animation: pulse 1.5s ease-in-out infinite

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and key conversion points. Renders as a solid forest-green rectangle with uppercase, letter-spaced type on a cream background. On hover, it deepens to {colors.primary-active} (#1d322d). Disabled state uses a muted sage {colors.primary-disabled} (#8aab9d) at 50% opacity. **`button-secondary`** — An outlined variant with a 2px solid border in the primary green, used for secondary actions like "View Details" or "Save for Later". The background is transparent canvas, and on hover the button fills with primary green and inverts the text. **`button-tertiary`** — A text-only underlined link styled as a button, used for less prominent actions like "Learn More" or "Cancel". **`button-icon`** — A 40x40px square icon button for actions like search, cart, or menu toggle. Transparent background with a subtle hover state on {colors.surface-soft}. **`button-pill`** and **`button-pill-outline`** — Pill-shaped compact buttons used for filters, tags, and category selection. The filled variant uses primary green, the outline variant uses a hairline border.

### Cards
**`product-card`** — The core product display component, a white card with a 1px soft hairline border and 12px rounded corners. Contains a square aspect-ratio product image, title in {typography.title-sm}, and price in {typography.price}. On hover, the card lifts with a subtle box shadow and reveals an "Add to Cart" button that fades in from the bottom. Badges overlay the top-left corner of the image, using {colors.accent-gold} for "Best Seller", {colors.accent-sage} for "New", {colors.accent-terracotta} for "Sale", and {colors.body} for "Sold Out". Sale prices render in {colors.accent-terracotta} to draw attention.

### Navigation
**`top-nav`** — A fixed 72px header with a white background and a soft bottom border. Contains the brand logo (32px height), navigation links in uppercase {typography.nav-link}, and icon buttons for search and cart. Active nav links are underlined with a 2px primary green border. On mobile, the navigation collapses into a hamburger menu with a slide-out drawer. **`breadcrumb`** — A secondary navigation pattern using muted caption type, with links in body color that shift to primary green on hover. Separators are hairline-colored slashes.

### Forms
**`text-input`** — Standard text input with a 1px hairline border, 8px rounded corners, and 48px height. On focus, the border switches to primary green with a subtle green box-shadow ring. Error state uses {colors.error} (#d58552) border. **`select-input`** and **`textarea`** follow the same styling conventions. **`checkbox`** and **`radio`** are 20px controls with a 2px hairline border, switching to primary green fill when checked. **`quantity-selector`** is a compact horizontal control with decrement/increment buttons flanking a centered numeric value, used on product detail pages.

### Footer
**`footer`** — A deep forest-green footer using {colors.primary} as background, with cream text at 80% opacity for links. Organized into columns with newsletter signup, navigation links, and social icons. The newsletter input is a white text field paired with a gold {colors.accent-gold} submit button. A subtle semi-transparent border separates the bottom legal section.

### Badges & Tags
**`badge`** — Small uppercase labels used for product attributes and promotions. The default badge uses gold background with dark ink text. Variants include "New" (sage), "Sale" (terracotta), "Sold Out" (body), and "Best Seller" (gold). All badges have 4px rounded corners and tight padding.

### Notifications & Feedback
**`notification`** — A soft surface-colored banner with a 1px hairline border for general messages. Success notifications invert to {colors.success} with cream text, error notifications use {colors.error} with white text, and info notifications use {colors.info} (#7ba4db) with white text. **`loading-spinner`** is a 24px circular spinner with a primary green arc. **`skeleton`** uses a pulsing soft-surface placeholder for content loading states.

### Modal & Overlay
**`modal`** — A centered dialog with 12px rounded corners, white background, and a soft shadow. The overlay uses a semi-transparent scrim at 50% opacity. A close button sits in the top-right corner. Used for quick-view product details, size guides, and confirmation dialogs.

### Accordion
**`accordion`** — Expandable sections with a bottom hairline border, used on product detail pages for "Description", "Care Instructions", and "Shipping & Returns". The header uses {typography.title-sm} and toggles open to reveal body-sm content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack in 2-column grid; hero section reduces padding; footer stacks vertically; search bar becomes full-width; accordions always expanded |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero uses 60/40 split; footer shows 2-column layout; search bar collapses to icon |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero uses 50/50 split with large imagery; footer shows 4-column layout; search bar expanded with placeholder text |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero uses 40/60 split; additional whitespace around content; product cards show hover add-to-cart by default |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile
- Icon buttons are 40x40px with 8px padding for comfortable tapping
- Quantity selector buttons are 36x36px minimum
- Accordion headers have 44px minimum tap height
- Product card "Add to Cart" button is 36px tall with full-width tap area on mobile

### Collapsing Strategy
- Top navigation links collapse into a hamburger menu below 744px, with a slide-out drawer from the left
- Product filters collapse into a "Filter" button that opens a bottom sheet on mobile
- Footer columns stack vertically below 744px, with accordion-style expandable sections
- Search bar collapses to an icon-only trigger on tablet and mobile
- Product image galleries switch from thumbnail strip to dot indicators on mobile
- Multi-column text sections (e.g., product descriptions) collapse to single column below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors
- Error styling for form validation (error messages, iconography) is inferred from the error color token but not confirmed
- Dark mode is not supported; all tokens assume a light theme
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured
- Animation durations and easing curves (transitions, loading spinner) are estimated based on common patterns
- Specific font weights for each typography token are inferred from the brand's editorial feel; actual weights may vary
- Dropdown and mega-menu patterns for navigation were not observed
- Tooltip and popover positioning logic (top, bottom, left, right) is not specified
- The exact border radius for product cards (12px) is inferred from the {rounded.md} token; actual site may vary slightly
- Star rating component sizing and spacing are estimated
- Modal max-width and overlay opacity are inferred from common patterns
- Skeleton loading animation details (duration, color stops) are not confirmed
- The brand's icon set and specific SVG assets are not documented
- Print styles and reduced-motion preferences are not captured
- The newsletter signup form's success/error states are not documented
- Accessibility focus indicators (outline styles) are not confirmed beyond the text-input focus state
