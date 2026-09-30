---
version: alpha
name: "Belkin"
source_url: "https://www.belkin.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand that sells the physical infrastructure of digital life — cables, docks, screen protectors, chargers — and its design system reads as engineered reliability first, with a single neon accent of #6ffb38 (lime green) that appears only in moments of active connection: a cable plugged in, a device charging, a firmware update succeeding. The canvas is #ffffff, the ink is #222222, and the body text sits at #444444 — a clean, legible hierarchy that never competes with the product photography. But the real story is in the greys: #777777 for muted labels, #e6e6e6 for hairline borders, #f2f2f2 for soft surfaces, and #b9bbbe for disabled states — a full spectrum of neutral tones that create depth without color. The extracted palette includes #ab2117 (a deep crimson) and #ffcc58 (a warm amber), which appear as stock-photo accents and badge backgrounds respectively, not brand primaries. The typography stack is system-native — -apple-system, Helvetica Neue, Arial — suggesting a pragmatic, cross-platform approach where legibility and performance trump typographic personality. Buttons use {rounded.sm} (8px) — a subtle softening of what could be purely rectangular — and the primary CTA (#222222 on white) is an inverted button that reads as "confirm your selection" rather than "buy now." The brand's design voice is: the hardware is the hero, the UI is just the manual.

colors:
  primary: "#222222"
  primary-active: "#000000"
  primary-disabled: "#b9bbbe"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#979797"
  hairline: "#e6e6e6"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#6ffb38"
  accent-green-active: "#4bfa06"
  accent-red: "#ab2117"
  accent-amber: "#ffcc58"
  badge-green: "#3a831d"
  badge-blue: "#0870ea"
  badge-amber-bg: "#ffe9b7"
  badge-red-bg: "#e0afab"
  link-blue: "#0870ea"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-green-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
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
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.muted}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-badge:
    backgroundColor: "{colors.badge-amber-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-green:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-red:
    backgroundColor: "{colors.badge-red-bg}"
    textColor: "{colors.accent-red}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  price-display-sale:
    textColor: "{colors.accent-red}"
    typography: "{typography.title-sm}"
  price-display-original:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: "line-through"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-green}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.hairline}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.base}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-accent:
    color: "{colors.accent-green}"
    size: 24px
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a solid black (#222222) rectangle with 8px rounded corners and white uppercase text at 14px/600 weight. Used for "Add to Cart," "Checkout," and "Shop Now" actions. On hover, it shifts to pure black (#000000). The disabled state uses #b9bbbe, a mid-grey that signals non-interactivity without ambiguity. **`button-secondary`** — An outlined variant with a 2px solid black border on a white background. The text remains black uppercase. Used for "Learn More," "View Details," and secondary navigation actions. **`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel," "Clear Filters," and inline links within product descriptions. **`button-accent-green`** — A small, high-energy button using the brand's neon green (#6ffb38) on black text. Reserved exclusively for active connection states: "Connected," "Charging," "Syncing." On hover, it brightens to #4bfa06.

### Cards
**`product-card`** — A white card with a 1px #e6e6e6 border and 8px rounded corners. Contains a square product image (1:1 aspect ratio) with 8px rounding, followed by the product title (body-sm), price (title-sm), and optional badges. On hover, the border shifts to #777777 — a subtle depth cue that doesn't rely on shadow. **`product-card-image`** — The image container within a product card, using 8px rounding and a 1:1 aspect ratio to ensure consistent grid alignment. **`product-badge`** — A small uppercase label (11px/700) with a warm amber (#ffe9b7) background and black text. Used for "Sale," "New," "Best Seller." **`product-badge-green`** — A green badge (#3a831d) with white text for "In Stock" or "Eco-Friendly." **`product-badge-red`** — A red-tinted badge (#e0afab background, #ab2117 text) for "Low Stock" or "Discontinued."

### Navigation
**`nav-bar`** — A 64px white bar with a 1px bottom border (#e6e6e6). Contains the Belkin logo, nav links, and a search icon. The nav links use 14px/500 weight text. **`nav-link-active`** — The active nav link has a 2px solid black underline, matching the primary color. **`nav-link-inactive`** — Inactive links render in #777777 with no underline. **`search-bar`** — A pill-shaped (full rounding) search input with a light grey background (#f2f2f2) and 1px #e6e6e6 border. The placeholder text uses body-md (16px). Used in the nav bar and on search result pages.

### Forms
**`text-input`** — A white input field with 8px rounding, 1px #e6e6e6 border, and 16px body text. On focus, the border becomes 2px solid black. On error, the border becomes 2px solid #ab2117 (the brand's accent red). **`select-dropdown`** — Matches the text-input styling but includes a dropdown arrow icon. Used for product filters (category, sort by) and address forms.

### Footer
**`footer`** — A full-width black (#222222) section with white text at body-sm (14px). Contains columnar link lists, social icons, and legal text. Footer links use 14px/400 weight and turn neon green (#6ffb38) on hover — the only place outside of active states where the accent green appears. **`footer-link-hover`** — The hover state for footer links, using the brand's neon green to create a subtle "live connection" metaphor even in the footer.

### Hero
**`hero-banner`** — A full-width section with a light grey background (#f2f2f2) and large display text (32px/700). Used for category landing pages and promotional campaigns. The CTA button inside the hero uses the primary button style. **`hero-banner-cta`** — The call-to-action button within the hero, matching `button-primary` styling.

### Misc
**`accordion-header`** — A white row with 16px padding and a 1px bottom border. Used for FAQ sections and product details (specs, features). The header uses title-sm (18px/600). **`accordion-content`** — The expandable content area below the header, using body-sm (14px/400) with 12px top padding and 24px bottom padding. **`tab-bar`** — A horizontal tab strip with a 1px bottom border. Active tabs have a 2px black underline and black text; inactive tabs use #777777. Used on product detail pages (Overview, Specs, Reviews). **`loading-spinner`** — A 24px black (#222222) circular spinner. An accent variant uses #6ffb38 for loading states during connection/sync operations. **`tooltip`** — A small black box with white text and 4px rounding, used for hover hints on icon buttons and product features. **`divider`** — A 1px horizontal line in #e6e6e6. **`divider-soft`** — A 1px horizontal line in #f2f2f2, used in dense lists or cards to reduce visual noise.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner reduces to 24px display text; footer links stack vertically; search bar moves to full-width below nav. |
| Tablet | 744–1128px | Two-column product grid; nav links visible but truncated (top 4 items); hero banner uses 28px display text; footer uses 2-column layout. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar visible; hero banner uses 32px display text; footer uses 4-column layout. |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero banner may include full-bleed imagery; footer remains 4-column but with increased padding. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (button-primary, button-secondary, text-input, select-dropdown).
- Icon buttons (icon-button) are 40px × 40px, exceeding the 44px touch target recommendation for mobile.
- Nav links in mobile hamburger menu are 48px tall for easy tapping.
- Product card tap targets (image, title, price) are each at least 44px tall within the card layout.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu. The search bar moves below the nav as a full-width element.
- The product filter sidebar (desktop) collapses into a "Filter" button that opens a bottom sheet or modal on mobile and tablet.
- The footer's multi-column link layout collapses to a single vertical stack on mobile, with each category as an accordion.
- Product detail page tabs (Overview, Specs, Reviews) collapse into an accordion on mobile.
- The hero banner's secondary text and CTA may stack vertically on mobile, with the image moving below the text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The brand's true primary color is ambiguous from extraction. The extracted list is dominated by greys (#222222, #444444, #777777, #e6e6e6, #f2f2f2) and a few accent colors (#6ffb38, #ab2117, #ffcc58). I've assigned #222222 as primary (most frequent dark color, used in nav and buttons), but the brand may use a different primary on its marketing pages (e.g., a blue or green not captured in the extraction). The neon green (#6ffb38) is distinctive but appears too infrequently to be primary — it's likely an accent for active/connected states.
- Hover states for buttons, cards, and links are inferred from common e-commerce patterns, not extracted from the live site. The specific hover colors (primary-active: #000000, accent-green-active: #4bfa06) are reasonable guesses.
- Error states (text-input-error, form validation) are not confirmed. The red #ab2117 is present in the extraction and is a natural choice for error, but the brand may use a different red or include helper text styling.
- Dark mode is not present in the extraction (meta theme-color is #000000, but that's likely a splash screen color, not a dark mode indicator). No dark mode tokens are defined.
- Font sizes and line heights are estimated from common system-font patterns. The extracted font declarations (-apple-system, Helvetica Neue, Arial) suggest a system-native approach, but specific sizes (32px for display-xl, 14px for button-md) are based on typical e-commerce hierarchies, not extracted values.
- The brand's sub-brands (e.g., Belkin BoostCharge, Belkin SoundForm) may have their own color accents or typography that are not captured in this system.
- The extraction includes colors from checkout widgets (Shopify Pay, Klarna, Afterpay) and social icons — these have been filtered out, but some may remain in the extracted list (e.g., #0870ea is likely a link blue, not a brand primary).
- The brand's use of the neon green (#6ffb38) is inferred from its presence in the extraction and its common association with "active/connected" states in tech products. The exact usage (buttons, indicators, loading spinners) is speculative.
