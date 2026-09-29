---
version: alpha
name: "Solawave"
source_url: "https://www.solawave.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-burgundy (#290217) and rosewood (#7c1c2f) brand that sells red-light therapy devices, Solawave stakes its visual identity on a medical-adjacent seriousness softened by a warm, almost cosmetic pink (#e6c4c7) and a cyan accent (#00bbff) that reads as clinical precision. The palette is dominated by dark, saturated reds and browns — #290217 appears as the primary ink, #7c1c2f as the primary brand color, and #6d1929 as a secondary variant — creating a mood that is both luxurious and therapeutic, closer to a dermatologist's office than a beauty counter. Typography runs on TWKLausanne and Inter, with Brown and Helvetica as fallbacks, suggesting a clean, Swiss-influenced sans-serif system. Buttons use full-pill rounding ({rounded.full}) and generous padding, while product cards likely employ soft corners ({rounded.md}) to balance the clinical edge. The brand's signature move is the contrast between its dark, wine-like primary and the bright, almost electric cyan (#00bbff) used for accents — a pairing that signals both efficacy and innovation. The canvas is a warm off-white (#faf3f4) rather than pure white, and the surface cards sit on #f4f4f6, maintaining a soft, approachable feel. The overall impression is of a brand that wants to be taken seriously as a medical device company while still feeling accessible and feminine.

colors:
  primary: "#7c1c2f"
  primary-active: "#6d1929"
  primary-disabled: "#cba4ac"
  ink: "#290217"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9da1a0"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5e5"
  canvas: "#faf3f4"
  surface-soft: "#f4f4f6"
  surface-card: "#f7f7f8"
  on-primary: "#ffffff"
  accent-cyan: "#00bbff"
  accent-orange: "#e8420d"
  accent-red: "#ff5742"
  accent-green: "#4efac0"
  star-rating: "#0018ff"
  error-text: "#c13515"

typography:
  display-xl:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'TWKLausanne', 'Brown', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'TWKLausanne', 'Brown', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'TWKLausanne', 'Brown', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'TWKLausanne', 'Brown', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Inter', 'TWKLausanne', 'Brown', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'TWKLausanne', 'Inter', 'Brown', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
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
    padding: 13px 31px
    height: 52px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-pill-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.error-text}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-best-seller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep rosewood (#7c1c2f) with white text and full-pill rounding. On hover, it shifts to the darker `primary-active` (#6d1929). The disabled state uses `primary-disabled` (#cba4ac), a muted pink that signals unavailability without visual noise. The large 52px height and 32px horizontal padding give it a substantial, confident presence.

**`button-secondary`** — An outlined or ghost-like alternative on the warm canvas background (#faf3f4) with ink text (#290217). Uses the same full-pill shape and height as primary, but with a 1px hairline border from `hairline` (#dbdde4) when needed. Active state fills with `surface-soft` (#f4f4f6).

**`button-ghost`** — A text-only button that inherits the primary color for its text, with no background. On hover, it gains a subtle `surface-soft` background. Used for secondary actions like "Learn More" or "View Details" within product cards.

**`button-accent-cyan`** — A high-energy variant using the brand's cyan accent (#00bbff) as background. Used sparingly for promotional CTAs, limited-time offers, or to draw attention to a specific action. Same pill shape and height as primary.

**`button-pill-sm`** — A smaller, 40px-tall pill button for inline use, such as in product filters, tag-like actions, or compact CTAs. Uses `button-sm` typography and the primary color scheme.

### Cards
**`product-card`** — The primary product display component, sitting on a `surface-card` (#f7f7f8) background with `rounded.md` (12px) corners. The card contains a product image (also rounded at `rounded.md`), a title in `title-sm`, a price in `title-sm` colored with the primary, and optional badges. The card has no visible border, relying on the subtle contrast between `surface-card` and the `canvas` (#faf3f4) background.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height, using the warm canvas background (#faf3f4). Navigation links use `nav-link` typography (15px, weight 500) and turn to the primary color when active. The bar likely contains the brand logo, main navigation links, a search icon, and a cart icon.

### Forms
**`text-input`** — Standard text input fields with a white background, 8px rounded corners, and 12px/16px padding. On focus, the border shifts to the primary color (#7c1c2f). Error states use a red border (#c13515) for validation feedback.

### Badges
**`badge-new`** — A small, uppercase pill badge in cyan (#00bbff) to denote new products or features. Uses 11px bold type with 0.5px letter spacing and 4px/10px padding.

**`badge-sale`** — An orange (#e8420d) badge for sale or promotional items. Same typography and shape as `badge-new`.

**`badge-best-seller`** — A rosewood (#7c1c2f) badge for best-selling products. Uses the primary brand color to signal authority and popularity.

### Footer
**`footer`** — A dark footer section using the ink color (#290217) as background, with white text for headings and `muted-soft` (#9da1a0) for links. Links use `link` typography (14px, weight 400) and likely have a hover state that brightens to the canvas color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger navigation, product cards stack vertically, hero text reduces to `display-lg`, buttons become full-width |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains two-column layout with reduced padding |
| Desktop | 1128–1440px | Full three- or four-column product grid, expanded navigation, hero uses full `display-xl` typography |
| Wide | > 1440px | Max-width container at 1440px, centered content with increased whitespace, product cards may show additional detail |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Primary buttons are 52px tall, exceeding the minimum.
- Search bar is 44px tall with full-pill rounding for easy thumb access.
- Product cards have a minimum tap area of 120x120px.

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px.
- Product grids collapse from 4 columns to 2 columns at tablet, to 1 column at mobile.
- Hero sections stack vertically on mobile, with text above imagery.
- Footer links collapse into accordion-style sections on mobile.
- Badges may reduce in size or stack vertically on very small screens.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components could not be fully extracted; active states are inferred from the extracted palette.
- Error styling for forms (beyond border color) is not confirmed — missing error message typography, iconography, and animation.
- Dark mode is not present on the live site; no dark theme tokens exist.
- The exact font weights and sizes for TWKLausanne and Inter are inferred from common usage patterns; the live site may use additional weights (e.g., 300, 700) not captured.
- The star rating color (#0018ff) is unusually bright blue — this may be a widget default rather than a brand choice; verify against actual product reviews.
- The accent green (#4efac0) appears only once in the extracted list and may be a stock-image artifact rather than a brand color.
- The extracted list includes many grays (#878787, #dedede, #b0b0b0, #b6b6b6) that may be used for borders, dividers, or disabled states — exact usage is unconfirmed.
- Shopify checkout widget colors (e.g., Afterpay, Klarna) may be present in the extracted list but could not be reliably filtered.
- The brand's sub-brand or seasonal color palettes are not captured.
