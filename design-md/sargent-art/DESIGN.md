---
version: alpha
name: "Sargent Art"
source_url: "https://www.sargentart.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A vivid, no-nonsense art-supply brand that leads with a punchy #ff0375 accent — a hot pink that appears nowhere in the extracted grays, blues, and greens, yet is the single most distinctive color in the palette. This pink is the brand's voltage: it powers the primary CTA, the cart badge, and the sale flags, cutting through a mostly neutral canvas of #f1f1f1 and #ececf6. The typography stack is utilitarian — system fonts like Open Sans, Roboto, and Segoe UI — suggesting a brand that prioritizes legibility and fast loading over typographic personality. Buttons are softly rounded (`{rounded.sm}`), while product images sit in clean rectangles (`{rounded.none}`), letting the art itself provide the visual interest. The extracted hex list is heavy on Bootstrap alert colors (#116600, #004085, #155724, #0c5460, #856404, #721c24) and checkout-widget tones, indicating the site may use a framework base layer with the brand's true identity applied as an accent layer. The overall mood is functional and accessible — a tool brand that gets out of the way of the creative process, with the hot pink serving as the one moment of playful confidence.

colors:
  primary: "#ff0375"
  primary-active: "#cc025e"
  primary-disabled: "#ffb3d4"
  ink: "#111111"
  body: "#2f2f2f"
  muted: "#464a4e"
  muted-soft: "#818182"
  hairline: "#b9bbbe"
  hairline-soft: "#cfd2d6"
  canvas: "#f1f1f1"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#116600"
  info: "#004085"
  warning: "#856404"
  error: "#721c24"
  badge-hot-pink: "#ff0375"
  badge-sale: "#d39e00"
  star-rating: "#d39e00"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Roboto', 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.error}"
    fontWeight: 700
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.base}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  category-tile-hover:
    border: "2px solid {colors.primary}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action uses the brand's hot pink (#ff0375) with white text and 8px rounded corners. On hover, it darkens to `{colors.primary-active}` (#cc025e). The disabled state uses a lighter pink `{colors.primary-disabled}` (#ffb3d4) with white text. Height is 44px with 12px vertical and 24px horizontal padding. **`button-secondary`** — An outlined variant with a white background, dark ink text, and a 2px solid ink border. On hover, the background and text swap: the button becomes solid ink with white text. Same 44px height and 8px radius as primary. **`button-tertiary-text`** — A text-only button with no background or border, using the primary hot pink for the text color. Used for "View all" links, "Learn more" prompts, and secondary actions within cards.

### Cards
**`product-card`** — A white card with 8px rounded corners and 12px padding. The product image sits flush within the card (`{rounded.none}`) at a 1:1 aspect ratio. The title uses `{typography.title-sm}` (16px, 600 weight) with 8px top margin. The price uses `{typography.body-md}` (16px, 400 weight) with 4px top margin. Sale prices render in `{colors.error}` (#721c24) at 700 weight. **`category-tile`** — A white card with 8px radius, 24px padding, and a 1px hairline border. On hover, the border thickens to 2px and turns hot pink, signaling interactivity.

### Navigation
**`nav-bar`** — A white header bar at 64px height with a 1px bottom hairline border. Navigation links use `{typography.nav-link}` (15px, 600 weight). The active link is underlined with a 3px hot pink bottom border. The nav is sticky on desktop and collapses to a hamburger menu on mobile. **`search-bar`** — A pill-shaped input (`{rounded.full}`) at 44px height with 8px vertical and 16px horizontal padding. On focus, the border switches from 1px hairline to 2px hot pink.

### Badges
**`badge-sale`** — A yellow (#d39e00) badge with dark ink text, 4px radius, and 2px vertical / 8px horizontal padding. Uses 11px uppercase bold type. **`badge-new`** — A hot pink badge with white text, same dimensions. **`badge-stock`** — A green (#116600) badge with white text, used for "In Stock" indicators.

### Forms
**`text-input`** — A white input field at 44px height with 10px vertical and 16px horizontal padding, 8px radius, and a 1px hairline border. On focus, the border becomes 2px hot pink. On error, the border becomes 2px red (#721c24). **`quantity-selector`** — A compact 36px height input with 8px radius and a 1px hairline border, used for adjusting product quantities.

### Footer
**`footer`** — A dark section using `{colors.ink}` (#111111) background with white text. Links use `{colors.muted-soft}` (#818182) and lighten to white on hover. Padding is 64px vertical and 24px horizontal.

### Hero
**`hero-section`** — A full-width section on the light canvas background with 64px vertical padding. The heading uses `{typography.display-xl}` (32px, 700 weight) and the subheading uses `{typography.body-md}` (16px, 400 weight) in muted gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in 2-column grid; hero padding reduces to 32px; search bar moves below nav; footer stacks links vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 3-column grid; hero heading reduces to 28px; category tiles in 3-column grid |
| Desktop | 1128–1440px | Full nav with all links; product cards in 4-column grid; hero heading at 32px; category tiles in 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5-column grid; increased whitespace around hero and footer |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Search bar and text inputs at 44px height
- Nav links have 48px touch area (padding + height)
- Category tiles have 24px padding ensuring adequate tap targets
- Quantity selector at 36px height — consider increasing to 44px on mobile

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces columns from 5 to 2 on mobile
- Footer link columns stack vertically on mobile
- Hero section reduces vertical padding from 64px to 32px on mobile
- Category tiles reduce from 4 columns to 2 on tablet, 1 on mobile
- Search bar moves from inline in nav to full-width below nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components could not be reliably extracted from the live site; the primary-active (#cc025e) is an inferred darkening of the hot pink
- Error state styling for forms (text-input-error border color) is inferred from Bootstrap alert colors present in the extracted palette
- The exact font stack is assembled from extracted declarations; the brand may use a specific weight or subset of Open Sans or Roboto that wasn't visible in the CSS
- Dark mode styling is not present on the live site
- Sub-brand or product-line-specific color palettes (e.g., for Sargent Art's different product categories like acrylics, watercolors, or pencils) could not be determined
- The extracted hex list is heavily polluted with Bootstrap framework defaults and checkout-widget colors; the true brand palette likely has fewer than 10 colors, with #ff0375 being the only distinctive brand accent
- Star rating color (#d39e00) is inferred from the yellow alert color present in the palette
- The meta theme-color (#121212) suggests a dark browser chrome, but this may be a default or unrelated to the brand's design system
- Animation durations, easing curves, and transition properties were not extracted
- Iconography style and sizing conventions are unknown
- The site may use a custom font for headings that wasn't captured in the extracted font-family declarations
