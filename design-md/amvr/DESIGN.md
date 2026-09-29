---
version: alpha
name: "AMVR"
source_url: "https://amvrshop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A VR-accessory brand that wraps its hardware in a dark, almost automotive palette — #1f2021 and #141414 dominate the canvas, not white, giving the storefront the feel of a cockpit interior rather than a consumer-gadget shop. The single voltage is #44b5ed, a cyan-blue accent that appears on add-to-cart buttons, hover states, and the glowing ring around product photography, reading as the LED of a headset powering on. Type runs Inter at 400/600 weight for body and Sora at 600 for display headlines, with Space Grotesk appearing in badge and price contexts for a slightly more technical, monolinear feel. Product cards use {rounded.md} corners on a #222222 surface, with a hairline border at #383838 that barely separates card from canvas — the brand trusts darkness and density over whitespace. The top nav is a fixed bar at #1f2021 with a search icon and cart badge, and the hero section pushes a single hero product against a gradient from #141414 to #1f2021, with the cyan CTA floating at {rounded.full}. Badges for "NEW" and "SALE" appear in #ec0101 and #ffc23d respectively, creating two additional signal colors that break the dark field with urgency. The overall effect is a brand that sells accessories for a device you wear on your face, and the site itself feels like the inside of that device: dark, precise, lit by a single bright indicator.

colors:
  primary: "#44b5ed"
  primary-active: "#3b9ce0"
  primary-disabled: "#a3d8f5"
  ink: "#141414"
  body: "#1f2021"
  muted: "#878787"
  muted-soft: "#a3a3a3"
  hairline: "#383838"
  hairline-soft: "#545454"
  canvas: "#141414"
  surface-soft: "#1f2021"
  surface-card: "#222222"
  on-primary: "#141414"
  badge-new: "#ec0101"
  badge-sale: "#ffc23d"
  star-rating: "#ffc23d"
  success: "#428445"
  error: "#eb001b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Sora', Inter, 'Space Grotesk', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Sora', Inter, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.2px
  price:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
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
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-section:
    backgroundColor: "{colors.canvas}"
    gradient: "linear-gradient(180deg, {colors.canvas} 0%, {colors.surface-soft} 100%)"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 52px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill with the brand's cyan-blue (#44b5ed) fill and dark ink text. On hover, shifts to `{colors.primary-active}` (#3b9ce0). Disabled state drops to a pale cyan `{colors.primary-disabled}` with dark text, signaling the action is unavailable without visual noise. Used for "Add to Cart", "Buy Now", and hero CTAs.

**`button-secondary`** — An outlined pill on a dark card surface, with cyan text and a subtle hairline border. On hover, the border shifts to the active cyan and the background lightens slightly. Used for "Learn More", "View Details", and secondary checkout flows.

**`button-ghost`** — A text-only button with no background or border, rendered in muted gray. Used for "Cancel", "Close", and tertiary navigation actions. Hover state not yet extracted — likely shifts to `{colors.body}`.

### Text Inputs
**`text-input`** — A dark card background (#222222) with a hairline border (#383838) and 12px padding. On focus, the border swaps to `{colors.primary}` cyan. Used in search, newsletter signup, and checkout forms. Placeholder text is `{colors.muted}` (#878787). Error state not yet extracted — likely uses `{colors.error}` border.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, using the darkest canvas (#141414) with a subtle bottom hairline. Navigation links are muted gray at 500 weight, with the active page or hover state shifting to `{colors.primary}`. The search icon is a `{rounded.full}` ghost button, and the cart icon carries a `{rounded.full}` cyan badge with a count.

### Product Cards
**`product-card`** — A dark card (#222222) with 12px rounded corners and a hairline border. On hover, the border turns cyan. The product image sits in a top region with rounded top corners, and the price is rendered in Space Grotesk at 18px/600 weight in muted gray. Badges for "NEW" (red) or "SALE" (amber) appear in the top-left corner as small uppercase labels.

### Badges
**`badge-new`** — A small uppercase label in red (#ec0101) with dark text, 4px rounded corners, and tight padding. Used to flag newly released accessories.
**`badge-sale`** — Same shape as the new badge but in amber (#ffc23d) with dark ink. Used for discounted items.

### Hero Section
**`hero-section`** — A full-width section with a dark gradient from #141414 to #1f2021, containing a single hero product image, a headline in Sora display-xl, and a large `{rounded.full}` cyan CTA button. The hero uses generous vertical padding (64px) and centers its content. The product image often has a subtle cyan glow or halo effect.

### Footer
**`footer`** — A dark canvas section with a hairline top border, containing link columns in muted gray. Links hover to cyan. The footer uses 48px vertical padding and a 16px grid for link columns. Social icons (not yet extracted) likely use `{colors.muted}` with cyan hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards go single-column; hero reduces to 32px padding; search becomes a full-width overlay; footer links stack vertically. |
| Tablet | 744–1128px | Nav bar shows condensed links (icons + labels); product cards in 2-column grid; hero maintains 48px padding; footer in 2-column layout. |
| Desktop | 1128–1440px | Full nav bar with text links; product cards in 3- or 4-column grid; hero at 64px padding; footer in 4-column layout. |
| Wide | > 1440px | Max-width container at 1440px; product cards may show 4-5 columns; hero content centered with larger display text. |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (48px standard).
- Cart badge is 20px minimum — acceptable for desktop, but on mobile the touch target is the parent icon (40px).
- Search icon button is 40px — meets touch target minimum.
- Nav links on mobile are 48px tap targets in the hamburger menu.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger icon and a slide-out drawer.
- Product cards collapse from multi-column to single-column, with images stacking vertically.
- The hero section reduces vertical padding from 64px to 32px, and the CTA button shrinks to full-width.
- Footer links collapse from 4 columns to a single vertical stack.
- Search transforms from an inline icon to a full-screen overlay with a text input.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for ghost buttons, text inputs, and footer links are inferred from brand patterns but not extracted from the live site.
- **Error and success states** for forms (red/green borders, error messages) are not extracted — the error hex (#eb001b) and success hex (#428445) are present in the color list but their usage context is unconfirmed.
- **Dark mode** is not applicable — the brand already uses a dark canvas as default.
- **Sub-brand palettes** (e.g., for AMVR Pro or AMVR Lite product lines) are not extracted.
- **Typography scale** for mobile (smaller font sizes) is not extracted — the values above are desktop defaults.
- **Animation and transition** timing (hover fades, card entrance, nav slide) are not extracted.
- **Social icon colors** (YouTube, Instagram, etc.) are present in the extracted hex list but their specific usage is unconfirmed — they may be brand-specific or platform defaults.
- **Checkout flow** colors (Shopify Pay, Klarna, Afterpay widgets) are likely present in the extracted list but are not part of the brand's core design system.
- **The extracted color list is large (27 hexes)** and includes many generic web colors (grays, blues, greens) that may be framework defaults or stock-image tones. The brand's true primary is identified as #44b5ed (cyan-blue), but secondary accents like #5b69c3 (purple-blue) and #fc9d01 (orange) may also be brand-significant — their usage is unconfirmed.
