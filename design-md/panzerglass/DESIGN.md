---
version: alpha
name: "PanzerGlass"
source_url: "https://www.panzerglass.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A protective-glass and accessory brand that operates in a world of high-contrast extremes — #121212 ink against #dedede silver-gray, with no color gradient to soften the statement. The brand’s visual language is industrial and precise: every product shot is a studio-lit object study, every CTA is a solid dark rectangle, and the only decorative flourish is the subtle sheen of the glass itself. The typography runs Acumin Pro and Acumin Pro Extra Condensed, a sans-serif family that feels equally at home on a military spec sheet and a tech unboxing video. Buttons are hard-cornered rectangles (`{rounded.none}`) with tight padding, echoing the cut edges of a screen protector. The navigation bar is a full-bleed dark strip (`{colors.ink}`) with white text — no hamburger, no transparency, no ambiguity. Product cards use a `{rounded.sm}` corner that suggests a chamfered edge rather than a friendly pill. The overall mood is one of engineered certainty: this is a brand that sells protection, not aspiration, and every pixel is calibrated to communicate durability, precision, and no-nonsense utility. The extracted palette is deliberately sparse — two colors, one type family, no pastels, no gradients — and that restraint is itself the brand signature.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#555555"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-silver: "#dedede"
  badge-new: "#121212"
  badge-sale: "#cc0000"

typography:
  display-xl:
    fontFamily: "'acumin-pro-extra-condensed', 'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'acumin-pro-extra-condensed', 'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'acumin-pro', 'Acumin Pro', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-silver:
    backgroundColor: "{colors.accent-silver}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.ink}"
  text-input-error:
    border: "2px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-bar-desktop:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 80px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    hoverColor: "{colors.accent-silver}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.muted}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — A solid dark rectangle (`{colors.primary}`) with white uppercase text (`{typography.button-md}`) and zero border radius. The lack of rounding is intentional: it echoes the cut edge of a tempered glass screen protector. On hover, the background deepens to `{colors.primary-active}` (#000000). Disabled state uses `{colors.primary-disabled}` (#555555) with full opacity — no transparency, no ambiguity. Padding is tight at 12px vertical, 24px horizontal, giving the button a compact, industrial footprint.

**`button-secondary`** — An outlined variant with a white fill, `{colors.ink}` text, and a 2px solid `{colors.ink}` border. On hover, the fill and text swap: the button becomes solid `{colors.ink}` with white text. This is used for secondary CTAs like "Learn More" and "View Details" where the primary button is already present.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.ink}` and `{typography.button-md}`. Used for dismiss actions, "Cancel" in modals, and inline links styled as buttons. Hover state adds a subtle underline.

**`button-silver`** — A `{colors.accent-silver}` (#dedede) filled button with `{colors.ink}` text, used on dark backgrounds (e.g., hero sections) where a white button would feel too stark and a dark button would disappear. Same `{rounded.none}` and uppercase treatment as the primary.

### Cards
**`product-card`** — A white card with `{rounded.sm}` (4px) corners, no shadow, and a clean borderless layout. The product image fills the top with `{rounded.sm} {rounded.sm} 0 0` — the bottom edge of the image is square where it meets the text block. Title uses `{typography.title-sm}` (16px, 600 weight) and price uses `{typography.body-md}` with 600 weight. No rating stars, no reviews count, no badges by default — the card is a pure product showcase.

**`product-badge`** — A small dark rectangle (`{colors.primary}`) with white uppercase text (`{typography.badge}`), placed at the top-left of the product image. Used for "NEW" or "BESTSELLER" labels. The `{rounded.none}` treatment keeps it consistent with the brand's hard-cornered aesthetic.

**`product-badge-sale`** — Same shape and typography as the standard badge, but with a `{colors.badge-sale}` (#cc0000) background for sale/discount indicators. The red is the only color accent in the entire system, used sparingly.

### Navigation
**`nav-bar`** — A full-bleed `{colors.ink}` strip, 64px tall on mobile/tablet, 80px on desktop. Navigation links use `{typography.nav-link}` (13px, 600 weight, 0.8px letter spacing, uppercase) in white. The logo is left-aligned, cart and search icons are right-aligned. No background transparency, no sticky-header blur — the bar is a solid dark anchor.

**`nav-bar-desktop`** — The desktop variant adds height (80px) and may include a secondary row for category links (Screen Protection, Cases, Accessories). The same dark background and white uppercase text persists.

### Forms
**`text-input`** — A white input field with `{rounded.none}`, a 1px `{colors.hairline}` border, and 12px/16px padding. On focus, the border thickens to 2px `{colors.ink}`. Error state uses a 2px `{colors.badge-sale}` border. The typography is `{typography.body-md}` (16px, 400 weight) — no placeholder styling beyond standard gray.

**`quantity-selector`** — A compact input with a 1px `{colors.hairline}` border, `{rounded.none}`, and 44px height. Used on product detail pages for cart quantity adjustment. The typography matches `{typography.body-md}`.

### Hero
**`hero-section`** — A full-width dark section (`{colors.ink}` background, white text) using `{typography.display-xl}` (48px, 700 weight, extra condensed) for the headline. The CTA is a `{colors.canvas}` button with `{colors.ink}` text — the inverse of the primary button pattern. The hero may include a product image or a split layout, but the background is always solid dark, never a gradient or image overlay.

### Footer
**`footer`** — A `{colors.ink}` background section with white text in `{typography.body-sm}` (14px, 400 weight). Links use `{typography.link}` and lighten to `{colors.accent-silver}` on hover. The footer is divided into columns (Support, Company, Legal, Social) with no background alternation — it's a single dark block.

### Dividers
**`divider`** — A 1px `{colors.hairline}` (#dedede) line used between sections on light backgrounds. **`divider-dark`** uses `{colors.muted}` (#666666) for use on the dark footer or dark hero sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero text reduces to `{typography.display-lg}` (36px); footer columns stack vertically; buttons become full-width |
| Tablet | 744–1128px | Nav bar shows 3-4 links; product cards in 2-column grid; hero uses split layout (text left, image right); footer columns in 2x2 grid |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3-column grid; hero at full width with extra-condensed display type; footer in 4-column layout |
| Wide | > 1440px | Max-width container (1440px) with centered content; nav bar and footer expand to full viewport width; product cards in 4-column grid; hero padding increases to `{spacing.section}` |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons are 40x40px with 20px icons, exceeding the 44px tap target recommendation by 4px.
- Product card tap targets (title, price, image) are the full card area — no separate "Add to Cart" button on mobile cards.
- Nav bar hamburger icon is 44x44px with 24px icon.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left.
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile.
- Footer columns stack vertically below 744px, with accordion-style expand/collapse for each column heading.
- Secondary navigation (category links below hero) collapses to a horizontal scrollable strip on mobile.
- Product description and specs collapse into accordion sections on mobile and tablet.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is extremely sparse (#dedede and #121212 only), which may indicate the brand uses primarily product photography for visual interest rather than a broad color system. The `{colors.badge-sale}` red (#cc0000) is inferred from common e-commerce patterns and may not match the brand's actual sale indicator color.
- No hover or focus state colors could be extracted beyond the primary button's active state. The `{colors.primary-active}` (#000000) is inferred as a logical darkening of `{colors.primary}` (#121212).
- Font weights and sizes for Acumin Pro are estimated based on common usage patterns — the brand may use different weights (e.g., 300 for body, 800 for display) than what is specified here.
- No border-radius values could be extracted from the live site CSS. The `{rounded.none}` for buttons and `{rounded.sm}` (4px) for cards are inferred from the brand's industrial aesthetic and common screen-protector product presentation patterns.
- No spacing scale could be reliably extracted. The values provided follow a standard 4px/8px/16px/24px/32px/48px/64px system common in e-commerce, but the brand may use a custom scale.
- No dark mode or high-contrast mode tokens are available. Given the brand's existing high-contrast palette (black on white), dark mode may simply invert the canvas and ink colors.
- No animation or transition timing values could be extracted. The brand likely uses fast, utilitarian transitions (150-200ms) rather than decorative animations.
- No error, success, or warning state colors beyond the inferred sale red. Form validation styling is speculative.
- The brand's Shopify platform may introduce checkout-specific colors (Shopify Pay button blue, Klarna pink, Afterpay black) that are not part of the brand's own design system. These have been excluded.
