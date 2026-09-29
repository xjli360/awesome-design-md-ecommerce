---
version: alpha
name: "VR Cover"
source_url: "https://vr-cover.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue (#0045a6) and signal red (#bd2426) tension drives VR Cover's interface — not a playful consumer palette but a precision-hardware storefront that happens to sell foam facials and lens protectors. The extracted palette is dominated by blues (#0051c3, #2f7bbf, #003681) that read as industrial reliability, punctuated by a safety-orange (#f68b1f) and a lime-green (#9bca3e) that likely flag compatibility badges or size indicators. The gray scale runs from near-black (#313131) through mid-gray (#404040) to a warm silver (#dedede), suggesting a system that trusts high-contrast readability over atmospheric tint. No rounded-full pills or bubbly cards here — corners are likely crisp at `{rounded.sm}` for buttons and `{rounded.md}` for product cards, with the only softness coming from the foam-product photography itself. The font stack falls back through system sans-serifs (Roboto, Helvetica Neue, Arial) with no brand-specific typeface declared, which either means the site uses a web font loaded dynamically (and missed by extraction) or the brand deliberately avoids typographic personality in favor of utility. Given the VR-hardware category, expect dense spec tables, compatibility matrices, and add-to-cart flows that prioritize information density over editorial whitespace. The red (#bd2426) likely serves as the primary CTA voltage — "Buy Now" or "Add to Cart" — while the deep blue (#0045a6) anchors the header, footer, and secondary actions.

colors:
  primary: "#0045a6"
  primary-active: "#003681"
  primary-disabled: "#8ba8d3"
  ink: "#313131"
  body: "#404040"
  muted: "#6a6a6a"
  muted-soft: "#9e9e9e"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#bd2426"
  accent-orange: "#f68b1f"
  accent-green: "#9bca3e"
  accent-blue-light: "#2f7bbf"
  accent-blue-dark: "#003681"
  silver: "#dedede"
  dark-gray: "#313131"

typography:
  display-xl:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.25px
  link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.25px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "#a01e20"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "#e8a0a1"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.accent-blue-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary-outline-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: "{colors.accent-blue-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0, 69, 166, 0.12)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  badge-compatibility:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-gray}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.silver}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  section-divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "#a01e20"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in signal red (#bd2426) on white text. Uses `{typography.button-md}` at 15px/600 weight with 0.25px letter spacing for a slightly tightened, authoritative read. On hover, darkens to #a01e20; disabled state fades to #e8a0a1. Padding is 12px 24px with `{rounded.sm}` (4px) — crisp, industrial, no pill shapes.

**`button-secondary`** — Deep blue (#0045a6) variant for secondary actions like "Learn More" or "View Details". Active state drops to `{colors.accent-blue-dark}` (#003681). Same dimensions and typography as primary, maintaining visual weight parity.

**`button-tertiary-outline`** — Outlined variant with a 2px solid `{colors.primary}` border on a transparent background. Used for "Compare" or "Save for Later" actions. On hover, fills with `{colors.primary}` and flips text to white.

### Cards
**`product-card`** — White surface with a 1px `{colors.hairline}` (#d9d9d9) border and `{rounded.md}` (8px) corners. Contains a square product image with matching corner radius, product title in `{typography.title-sm}`, price in `{typography.body-md}`, and compatibility badges. On hover, the border shifts to `{colors.primary}` and a subtle blue-tinted shadow appears (0 2px 8px rgba(0, 69, 166, 0.12)). Padding is 16px.

### Navigation
**`nav-bar`** — Fixed-height 64px bar in deep blue (`{colors.primary}`). Navigation links use `{typography.nav-link}` — 14px/500 weight, uppercase with 0.25px tracking — for a technical, spec-sheet feel. Active links get a dark-blue (`{colors.accent-blue-dark}`) background pill with `{rounded.sm}`. The bar likely contains a logo lockup on the left and nav items on the right.

### Forms
**`text-input`** — Standard 44px input with 1px `{colors.hairline}` border and `{rounded.sm}`. On focus, the border thickens to 2px `{colors.primary}`. Error state swaps to 2px `{colors.accent-red}`. Padding is 10px 14px for comfortable cursor placement.

### Badges
Three badge variants share `{typography.badge}` (11px/700 weight, uppercase, 0.5px tracking) with `{rounded.xs}` (2px) and 2px 8px padding. **`badge-compatibility`** uses lime green (#9bca3e) for "Works with Quest 3" labels. **`badge-new`** uses safety orange (#f68b1f) for new arrivals. **`badge-sale`** uses signal red (#bd2426) for discounts.

### Search
**`search-bar`** — A 44px input with white background, 1px `{colors.hairline}` border, and `{rounded.sm}`. On focus, the border thickens to 2px `{colors.primary}`. Uses `{typography.body-md}` for placeholder and input text.

### Footer
**`footer`** — Dark gray (#313131) background with white text. Links render in silver (#dedede) and shift to full white on hover. Section padding is 48px top and bottom.

### Hero
**`hero-section`** — Full-width deep blue (#0045a6) section with white text using `{typography.display-xl}` (32px/700 weight). Section padding is 64px top and bottom. Likely contains a headline, subheadline in `{typography.display-md}`, and a primary CTA button.

### Quantity Selector
**`quantity-selector`** — A 44px input group with minus/plus buttons flanking a numeric display. Uses `{typography.body-md}`, 1px `{colors.hairline}` border, and `{rounded.sm}`. Common on product detail pages for accessory quantities.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 32px; filter chips stack vertically; product cards full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 48px padding; filter chips wrap in a horizontal strip |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full 64px padding; product cards show hover effects |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns; hero content centered with max-width |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain a minimum 44px height
- Filter chips are 32px tall with 16px horizontal padding for easy tapping
- Quantity selector buttons are 44px × 44px tap targets
- Nav links have 8px 16px padding for 44px minimum tap area
- Product card links span the full card for easy tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid collapses from 3 columns → 2 columns → 1 column
- Filter chips collapse from a horizontal strip to a vertical accordion below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile
- Footer links stack vertically on mobile
- Search bar may collapse to an icon-only trigger on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific web font could be extracted; the site may use a dynamically loaded font (Google Fonts, Typekit) that wasn't captured. The system font stack is documented as fallback.
- Hover and focus states for most components are inferred from common patterns; actual extracted hover colors are unavailable.
- Error states for forms (validation messages, error icons) are not extracted.
- Dark mode or high-contrast mode variants are unknown.
- The extracted color palette includes 13 hex values, but several (#0051c3, #2f7bbf, #f68b1f, #9bca3e) may be checkout-widget, social-icon, or stock-image dominant tones rather than brand colors. The primary (#0045a6) and accent-red (#bd2426) are the most distinctive and likely brand-owned.
- No typography scale could be extracted from computed styles; the scale is inferred from common e-commerce patterns for VR hardware stores.
- Spacing values are inferred from common grid systems; actual extracted spacing is unavailable.
- Animation durations, easing curves, and transition properties are unknown.
- The site returned a 522 timeout error during extraction, meaning the live DOM was not fully parsed. All component structures are inferred from the brand category and color palette.
