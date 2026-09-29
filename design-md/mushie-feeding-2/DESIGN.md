---
version: alpha
name: "Mushie"
source_url: "https://mushie.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A muted, earth-toned feeding and baby brand that builds its visual identity on a warm off-white canvas of {colors.canvas} (#fcfaf7) and a deep, almost-black ink of {colors.ink} (#0f0f0f), creating a quiet, grounded atmosphere that feels more like a natural-fiber boutique than a plastic-heavy baby aisle. The brand's primary accent, a soft terracotta {colors.primary} (#d2815f), appears sparingly but deliberately — on add-to-cart buttons, sale badges, and select product swatches — while a deeper burnt-orange {colors.primary-active} (#c35121) provides hover-state voltage without ever feeling aggressive. Supporting tones of dusty rose {colors.surface-soft} (#f3ece7), warm sand {colors.surface-card} (#f8f0e7), and a slate blue {colors.accent-blue} (#748cab) suggest a palette drawn from natural pigments rather than digital primaries. Typography relies on a single system font stack (the site's only declared font-family is `swiper-icons`, indicating a reliance on native system fonts for body copy), keeping the interface clean and unadorned. Buttons use a soft {rounded.sm} radius (8px) that feels approachable without being pill-shaped, while product cards and image containers adopt a slightly more generous {rounded.md} (12px) to frame photography gently. The overall impression is one of restraint — the brand trusts its product photography and earthy color story to do the emotional work, letting the UI recede into a warm, tactile background.

colors:
  primary: "#d2815f"
  primary-active: "#c35121"
  primary-disabled: "#eecba5"
  ink: "#0f0f0f"
  body: "#4e4e50"
  muted: "#575757"
  muted-soft: "#747477"
  hairline: "#dedede"
  hairline-soft: "#e7e7e7"
  canvas: "#fcfaf7"
  surface-soft: "#f3ece7"
  surface-card: "#f8f0e7"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  accent-blue: "#748cab"
  accent-blue-active: "#3f6493"
  accent-warm: "#e4d8ce"
  badge-sale: "#ff2a00"
  star-rating: "#24242d"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
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
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
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
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.badge-sale}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} 0"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.canvas}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 28px
    width: 28px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's terracotta {colors.primary} (#d2815f) with white text and a soft 8px radius. On hover, it deepens to {colors.primary-active} (#c35121). The disabled state uses a pale peach {colors.primary-disabled} (#eecba5) with muted text, signaling unavailability without visual noise.

**`button-secondary`** — A ghost-style button with a white background, dark text, and a thin {colors.hairline} border. On hover, the background shifts to {colors.surface-soft} (#f3ece7) and the border darkens to {colors.ink}, providing a subtle elevation cue. Used for "View All" links, secondary cart actions, and filter resets.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Clear" or "Cancel." The text color matches {colors.body} (#4e4e50) and inherits the button-md typography.

**`button-pill-primary`** — A fully rounded variant of the primary button, used sparingly for promotional badges or sticky mobile CTAs. Uses smaller button-sm type and tighter padding to fit compact spaces.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px radius. The image container occupies a 1:1 aspect ratio with matching rounded corners. The title uses title-md weight 500, while the price sits in body-md weight 400. Sale prices are rendered in {colors.badge-sale} (#ff2a00). Cards stack in a responsive grid with {spacing.lg} (24px) gaps.

**`product-card-image`** — The image wrapper within a product card, maintaining a square aspect ratio. Images are clipped to {rounded.md} (12px) and typically show lifestyle or flat-lay photography against the warm {colors.canvas} background.

### Navigation
**`top-nav`** — A fixed-position header at 72px height, white background, with uppercase nav links in 14px weight 500. Active links are underlined with a 2px {colors.primary} bar. The nav collapses to a hamburger menu below 744px.

**`nav-link-active`** / **`nav-link-inactive`** — Active links use {colors.ink} (#0f0f0f) with a primary underline; inactive links are {colors.muted} (#575757) with no underline. Both use nav-link typography (14px, uppercase, 0.3px letter-spacing).

### Forms
**`text-input`** — Standard input fields with a white background, 8px radius, and a 1px {colors.hairline} border. On focus, the border switches to {colors.primary}. Error states use a red border matching {colors.badge-sale}. Padding is 12px vertical, 16px horizontal, with body-md type.

**`quantity-selector`** — A compact input group for cart quantities, featuring a bordered container with increment/decrement buttons. The buttons are 28px squares with no border radius, while the container uses 8px radius and 44px height.

### Badges
**`badge-sale`** — A small, uppercase red badge (#ff2a00) with white text, 4px radius, and tight 2px/8px padding. Appears as an overlay on product card images or next to sale prices.

**`badge-new`** — Uses the brand's terracotta primary as background, signaling new arrivals. Same dimensions and typography as the sale badge.

**`badge-sold-out`** — A neutral gray badge (#747477) for out-of-stock items. Uses the same badge structure but communicates unavailability without alarm.

### Footer
**`footer`** — A dark footer with {colors.ink} background and white text. Links are rendered in {colors.muted-soft} (#747477) and shift to white on hover. The footer typically contains navigation columns, social links, and legal text in body-sm type.

### Hero
**`hero-banner`** — A full-width banner section with a {colors.surface-soft} (#f3ece7) background, large display-xl type, and generous section padding (64px vertical). The primary CTA within the hero uses a larger 48px height button with 14px/32px padding.

### Accordion
**`accordion-header`** — Used for product descriptions, shipping details, and FAQ sections. Headers are white with a bottom hairline border, using title-md type. Content panels collapse/expand with smooth transitions, using body-md type in {colors.body}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger; product grid goes single-column; hero padding reduces to 32px vertical; buttons become full-width; search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero uses 48px vertical padding; side-by-side product detail layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero at full section padding; multi-column footer layout |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns; hero content centered with max-width constraint |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and swatches are at least 32px with adequate tap spacing
- Quantity selector buttons are 28px — slightly below ideal but acceptable for paired increment/decrement layout
- Mobile hamburger menu toggle is 44px square

### Collapsing Strategy
- Top nav: primary links collapse into hamburger menu below 744px; search icon remains visible, expanding to full input on tap
- Product filters: slide-in drawer on mobile; persistent sidebar on tablet and above
- Footer: multi-column layout collapses to single-column stacked on mobile
- Hero: side-by-side text/image layout stacks vertically below 744px
- Accordion: always collapsed by default on mobile; can be expanded on desktop for persistent visibility of key info

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font-family list only returned `swiper-icons` (a carousel icon font), meaning the site relies on system font stacks for all body and heading text. The specific system font fallback order is inferred from common Shopify patterns but not confirmed.
- Hover and focus states for most components are inferred from the primary-active color and common patterns; actual extracted hover colors were not available.
- Error state styling (form validation, error messages) is assumed based on the presence of #ff2a00 in the palette but not confirmed from live interaction.
- Dark mode is not supported; all extracted colors assume a light theme.
- The extracted color list includes several generic grays (#4f4f4f, #4f4b48, #606062, #8c8c8d, #ababab, #121212, #007aff) that may belong to third-party widgets (Shopify Pay, Klarna, Apple Pay) rather than the brand itself. The primary palette above focuses on the most distinctive and frequently occurring brand tones.
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured.
- Typography scale (font sizes, weights, line heights) is estimated from common Shopify patterns and the brand's visual tone; actual values may vary across pages.
- Animation durations, easing curves, and transition properties are not extracted.
- Spacing values for specific components (e.g., accordion padding, card gaps) are inferred from the brand's visual density rather than measured from live CSS.
