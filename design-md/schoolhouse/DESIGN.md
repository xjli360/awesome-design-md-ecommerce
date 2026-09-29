---
version: alpha
name: "Schoolhouse"
source_url: "https://www.schoolhouse.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Schoolhouse is a decor brand that feels like a warm, well-edited living room rather than a sterile showroom. The palette is grounded in a deep, almost charcoal ink (`#2c2c2c`) and a soft, approachable body gray (`#707070`), with a canvas (`#f5f5f5`) that leans slightly warm — not a cold, clinical white. This foundation is punctuated by a singular, confident accent: a rich, heritage red (`#ce2525`) that appears on primary CTAs, sale badges, and key product callouts, acting as the brand's voltage. Supporting this are muted tones like `#9ca3af` and `#dcdcdc` for hairline borders and soft surfaces, creating a layered, tactile feel. The typography, anchored by Inter and system fonts, is clean and utilitarian, favoring readability over display. The brand's signature move is the use of generous, soft rounding — `{rounded.sm}` (8px) for buttons and `{rounded.md}` (12px) for cards — which, combined with the warm canvas and restrained palette, makes the site feel friendly and curated, not coldly minimalist. The overall mood is one of quiet confidence: the design gets out of the way of the product photography, letting the decor speak for itself.

colors:
  primary: "#ce2525"
  primary-active: "#a81e1e"
  primary-disabled: "#f0b0b0"
  ink: "#2c2c2c"
  body: "#707070"
  muted: "#9ca3af"
  muted-soft: "#dcdcdc"
  hairline: "#d9d9d9"
  hairline-soft: "#e5e7eb"
  canvas: "#f5f5f5"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#5a31f4"
  accent-blue: "#007aff"
  badge-sale: "#ce2525"
  badge-new: "#5a31f4"
  star-rating: "#2c2c2c"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.md}"
    padding: 48px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 32px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 16px
  accordion-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's signature red (`{colors.primary}`) on a white background (`{colors.on-primary}`). It has a soft 8px rounding (`{rounded.sm}`) and is 44px tall, making it easy to tap. On hover, it shifts to a deeper red (`{colors.primary-active}`), and in its disabled state, it uses a lighter, muted red (`{colors.primary-disabled}`). The text is set in `{typography.button-md}` with 0.5px letter-spacing for a clean, intentional feel.

**`button-secondary`** — A ghost button with a white background (`{colors.canvas}`) and dark ink text (`{colors.ink}`). It shares the same dimensions and rounding as the primary button but uses a 1px hairline border (`{colors.hairline}`) to define its shape. This is used for less prominent actions, like "View Details" or "Cancel."

**`button-tertiary-text`** — A text-only button with no background or border. It uses the same typography as the primary button but relies on the ink color (`{colors.ink}`) for its visual weight. Used for inline actions like "Learn More" or "Add to Wishlist."

**`button-pill`** — A compact, fully rounded (`{rounded.full}`) button used for filters, tags, or quick actions. It is 36px tall and uses a smaller typography (`{typography.button-sm}`). The default state uses the primary red, but it can also be used in a secondary style with a white background and ink text.

### Cards
**`product-card`** — The core product display component. It features a white surface (`{colors.surface-card}`) with a 12px rounding (`{rounded.md}`). The card contains a product image with the same rounding, a title in `{typography.body-sm}`, and a price in `{typography.body-md}`. Sale prices are rendered in the primary red (`{colors.primary}`). Badges (e.g., "SALE" or "NEW") are positioned on the top-left of the image, using `{rounded.xs}` and the appropriate badge color.

### Navigation
**`nav-bar`** — A fixed top navigation bar, 64px tall, with a white background (`{colors.canvas}`). It contains the brand logo, navigation links, and a search bar. Links use `{typography.nav-link}` and are either active (ink color) or inactive (muted color). The search bar is a pill-shaped input (`{rounded.full}`) with a soft background (`{colors.surface-soft}`).

### Forms
**`text-input`** — A standard text input field with a white background, 1px hairline border (`{colors.hairline}`), and 8px rounding (`{rounded.sm}`). On focus, the border changes to the ink color (`{colors.ink}`). The input is 44px tall with 12px horizontal padding.

### Footer
**`footer`** — A dark footer section with an ink background (`{colors.ink}`) and white text. It contains links in a muted tone (`{colors.muted-soft}`) and uses `{typography.body-sm}`. The footer has generous padding (48px) and is divided into columns for navigation, support, and social links.

### Accordion
**`accordion`** — A collapsible content panel used for FAQs or product details. It has a white background, 8px rounding, and 16px padding. The header uses `{typography.title-md}` and toggles the visibility of the body content below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero banner padding reduces to 24px; footer columns stack. |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar shows limited links; search bar collapses to icon; hero banner uses 32px padding. |
| Desktop | 1128–1440px | Full multi-column grid; nav-bar shows all links; search bar is fully expanded; hero banner uses standard padding. |
| Wide | > 1440px | Max-width container (1440px) centered; content remains at standard widths; hero banner may use a wider image. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet accessibility guidelines.
- Icon buttons are 40px x 40px with a 24px icon inside.
- Product card images are tappable and link to the product detail page.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, hiding all links except the logo and cart icon.
- The search bar collapses from a full input to a search icon on mobile and tablet.
- Product grids collapse from 4 columns on desktop to 2 on tablet and 1 on mobile.
- Footer columns stack vertically on mobile, with each section becoming an accordion.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons were not fully extracted; assumed standard darkening or underline.
- Error states for form inputs (e.g., red border, error message styling) were not observed.
- Sub-brand or promotional palettes (e.g., seasonal colors, sale-specific accents) were not captured.
- Dark mode styling is not present on the live site.
- Specific animation and transition durations (e.g., button hover, card lift) were not extracted.
- The exact font-weight for Inter in different contexts (e.g., 400 vs 500 vs 600) was inferred from common usage.
- The `star-rating` color is assumed to match the ink color based on typical decor site patterns.
- The `scrim` color for overlays is assumed to be a near-black (`#121212`) based on common practice.
