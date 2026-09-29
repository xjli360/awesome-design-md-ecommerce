---
version: alpha
name: "Reel Paper"
source_url: "https://reelpaper.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A paper-goods brand that builds its visual identity around a deep teal-navy (#243f50) — the color of a forest canopy at dusk — used as the primary anchor for buttons, headlines, and the site's persistent top bar. The palette is deliberately restrained: a warm off-white (#f0e9e7) serves as the canvas, while a sage-green (#b6cfaf) and a dusty blue (#79abc9) appear as secondary accents, often in product imagery or decorative blocks. The typography runs AvenirLTPro-Heavy for display and button text, a weight that reads as confident and slightly retro, paired with lighter sans-serif weights for body copy. Product cards use generous white space and soft corners ({rounded.md} ~12px), with the primary CTA rendered as a solid teal pill ({rounded.full}) that contrasts sharply against the pale canvas. The checkout flow inherits Shopify's standard widget colors (PayPal blue, Klarna pink, Afterpay black), which sit uneasily next to the brand's muted earth tones — a known compromise of the platform. The overall mood is calm, domestic, and slightly Scandinavian: clean lines, matte finishes, and a trust in natural materials that the color palette reinforces without ever showing a literal tree.

colors:
  primary: "#243f50"
  primary-active: "#1a2e3c"
  primary-disabled: "#a0b4c0"
  ink: "#121212"
  body: "#395261"
  muted: "#5d7975"
  muted-soft: "#79abc9"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f0e9e7"
  surface-soft: "#f3e9e8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#b6cfaf"
  accent-dusty-blue: "#79abc9"

typography:
  display-xl:
    fontFamily: "'AvenirLTPro-Heavy', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'AvenirLTPro-Heavy', 'Avenir', sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'AvenirLTPro-Heavy', 'Avenir', sans-serif"
    fontSize: 20px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'AvenirLTPro-Heavy', 'Avenir', sans-serif"
    fontSize: 16px
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'AvenirLTPro-Heavy', 'Avenir', sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'AvenirLTPro-Heavy', 'Avenir', sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.29
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a solid teal pill with heavy uppercase type. On hover, the background deepens to `{colors.primary-active}` (#1a2e3c). The disabled state uses `{colors.primary-disabled}` (#a0b4c0) with reduced opacity. Used for "Add to Cart", "Subscribe", and "Checkout" flows.
**`button-secondary`** — An outlined variant on the warm canvas background, with teal text and a 2px border. Hover inverts to solid teal with white text. Used for secondary actions like "Learn More" or "View Details".
**`button-tertiary-text`** — A text-only link styled as a button, using the primary teal color. No background or border. Used for "Cancel" or "Skip" actions in forms.

### Cards
**`product-card`** — A white card with soft 12px corners containing a product image, title, price, and a "Quick Add" button. The image sits flush to the top with the same corner radius. On hover, a subtle shadow lifts the card 4px. The badge component overlays the top-left corner for "New" or "Best Seller" labels.
**`badge`** — A small pill-shaped label in sage green, used to flag product attributes. Text is dark ink for readability. Positioned absolutely over the product image.

### Navigation
**`nav-bar`** — A solid teal bar spanning the full viewport width, containing the brand logo (left), navigation links (center), and cart icon (right). Links use heavy uppercase type in white. The bar is 72px tall on desktop, collapsing to a hamburger menu on mobile. The cart icon shows a badge count in `{colors.accent-sage}`.

### Forms
**`text-input`** — A simple input field with a warm canvas background and a light gray border. On focus, the border transitions to `{colors.primary}` with a 2px stroke. Placeholder text uses `{colors.muted}` (#5d7975). Error states use a red border (#c13515) with an error message below in `{colors.body}`.

### Footer
**`footer`** — A full-width teal section containing links, social icons, and legal text. Links are white and use `{typography.body-sm}`. Social icons (Font Awesome) are rendered in white with 24px sizing. The footer includes a newsletter signup form with an inline `{typography.button-sm}` CTA.

### Hero
**`hero-section`** — A full-width section on the warm canvas background, featuring a large headline, a subheading, and a primary CTA button. The background may include a subtle pattern or product image at 50% opacity. Padding is 64px top/bottom with 24px sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero text reduces to 24px; buttons become full-width |
| Tablet | 744–1128px | Nav links visible; product cards in 2-column grid; hero maintains 28px headline |
| Desktop | 1128–1440px | Full nav; 3-column product grid; hero at 36px display-xl |
| Wide | > 1440px | Max-width container at 1440px; content centered; nav bar stretches full width |

### Touch Targets
- All buttons and links maintain a minimum 44px tap target height.
- Search bar and text inputs have 48px height for comfortable touch interaction.
- Nav links have 48px tap area even when text is smaller.

### Collapsing Strategy
- The top nav collapses to a hamburger menu below 744px, with a slide-in drawer from the left.
- Product filters collapse into a "Filter" button that opens a modal on mobile.
- The footer's multi-column layout stacks into a single column below 744px.
- Hero sections reduce padding from 64px to 32px on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary button hover is confirmed.
- Error styling for forms (border color, icon placement, message typography) is inferred from common Shopify patterns, not extracted.
- The brand's secondary palette (sage, dusty blue) is inferred from product imagery and decorative blocks; exact usage rules (e.g., "sage only for badges") are speculative.
- Font weights for body text (Avenir Regular vs. Medium) are estimated; only AvenirLTPro-Heavy was explicitly found.
- Dark mode is not supported; no extracted tokens for dark canvas or inverted text.
- The extracted hex list includes Shopify checkout widget colors (e.g., PayPal blue, Klarna pink) that are not part of the brand system; these have been excluded.
- Sub-brand or seasonal color palettes (e.g., holiday collections) are unknown.
- Animation durations, easing curves, and shadow values are not extracted.
