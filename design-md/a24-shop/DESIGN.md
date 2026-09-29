---
version: alpha
name: "A24 Shop"
source_url: "https://shop.a24films.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A24 Shop is a film-merchandise storefront that treats its products like props from the movies themselves, set against a near-black canvas (#121212) that makes every item feel like it’s under a spotlight. The brand’s primary voltage is a warm, almost sunburned coral (#fc8259) that appears on add-to-cart buttons, sale badges, and the occasional accent line — a color that reads as urgent without being aggressive, like a neon sign in a dark room. The secondary palette is almost entirely achromatic: a mid-gray (#dedede) for borders and secondary text, with white (#ffffff) reserved for product cards and the checkout surface. The site uses a single sans-serif typeface (likely Inter or a similar geometric) at moderate weights — display headlines sit at 24–32px in weight 500, trusting the dark background and generous whitespace to do the heavy lifting rather than bold typography. Product cards are softly rounded (`{rounded.md}` ~12px), buttons are pill-shaped (`{rounded.full}`), and the persistent top nav is a thin, translucent bar that blurs the content behind it — a cinema-foyer gesture that signals “you’re in the lobby, not the theater.” The overall mood is restrained and cinematic: muted tones, high contrast, and a single accent color that never overwhelms.

colors:
  primary: "#fc8259"
  primary-active: "#e06a3f"
  primary-disabled: "#fcccb8"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#dedede"
  muted-soft: "#e8e8e8"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-sale: "#fc8259"
  badge-new: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: 1px solid "{colors.hairline}"
  top-nav:
    backgroundColor: "rgba(255, 255, 255, 0.85)"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    backdropFilter: blur(8px)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 {spacing.base} 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xxs} {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s coral (#fc8259) with white text and a pill shape (`{rounded.full}`). Used for “Add to Cart,” “Checkout,” and primary form submissions. On hover, it darkens to `{colors.primary-active}` (#e06a3f). The disabled state uses a lighter coral (`{colors.primary-disabled}`) and reduced opacity.

**`button-secondary`** — A dark, high-contrast alternative for secondary actions like “View Details” or “Continue Shopping.” Uses the near-black `{colors.ink}` background with white text, same pill shape and height as the primary. Hover state shifts to a slightly lighter black (not defined here, but likely #2a2a2a).

**`button-tertiary-text`** — A text-only button for subtle actions like “Cancel” or “Clear.” No background, inherits `{colors.ink}` text, and uses the same `{typography.button-md}` size. Hover adds an underline.

**`button-pill-outline`** — An outlined pill button for filter toggles or secondary navigation. Transparent background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Hover fills with `{colors.surface-soft}`.

### Cards
**`product-card`** — The primary product display unit, a white card (`{colors.surface-card}`) with `{rounded.md}` corners. The product image sits at the top with rounded top corners only, creating a subtle visual break. Below, the title (`{typography.title-sm}`) and price (`{typography.body-md}`) stack with minimal padding. On hover, the card may lift slightly (a box-shadow transition, not captured in tokens). Badges like `badge-sale` or `badge-new` overlay the image at the top-left.

### Navigation
**`top-nav`** — A fixed-position, translucent white bar (85% opacity) with `backdrop-filter: blur(8px)` for a frosted-glass effect. Contains the A24 logo (left), navigation links (center), and cart icon (right). Height is 60px. On scroll, the bar gains a subtle bottom border (1px `{colors.hairline-soft}`). Nav links use `{typography.nav-link}` — 14px, weight 500, with letter-spacing for a slightly spaced-out, editorial feel.

### Forms
**`text-input`** — Standard text input with a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border becomes a 2px `{colors.primary}` stroke. Used for email signups, search queries, and checkout fields. Height is 48px for comfortable touch targeting.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search field with a soft gray background (`{colors.surface-soft}`) and a 1px `{colors.hairline}` border. Shorter than the text input (40px), it sits in the top nav or a dedicated search page. Placeholder text uses `{colors.muted}`.

### Badges
**`badge-sale`** — A small, uppercase coral badge (`{colors.badge-sale}`) with white text, `{rounded.xs}` corners, and tight padding. Used to flag discounted items. The `badge-new` variant uses the near-black `{colors.badge-new}` for new arrivals or limited drops.

### Footer
**`footer`** — A dark footer section (`{colors.ink}`) with muted gray text (`{colors.muted}`). Contains links to support, privacy, and social channels. Links use `{typography.link}` and hover to white. Padding is generous (`{spacing.xxl}` vertical) to create breathing room.

### Hero
**`hero-section`** — A full-width hero banner with a dark background (`{colors.ink}`) and white headline text. Used for collection launches or seasonal promotions. The headline uses `{typography.display-xl}` (32px, weight 500) and the subheadline uses `{typography.body-md}` in muted gray. May include a single `button-primary` CTA.

### Cart
**`cart-item`** — A row in the cart or mini-cart, showing product image, title, quantity selector, and price. Uses a white background with a soft bottom border (`{colors.hairline-soft}`). The `quantity-selector` is a small, soft-gray pill with `{rounded.sm}` corners and 40px height.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 columns), top-nav collapses to hamburger menu, hero text reduces to `{typography.display-md}`, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, top-nav shows all links (no hamburger), hero uses full-width image with centered text |
| Desktop | 1128–1440px | Three-column product grid, top-nav at full height (60px), hero may include left-aligned text with image on right |
| Wide | > 1440px | Max-width container (1440px) centered, product grid may expand to 4 columns, hero uses larger `{typography.display-xl}` |

### Touch Targets
- All buttons and interactive elements are at least 44px tall (buttons, inputs, nav links).
- Product card tap targets (title, price, image) are the full card width.
- Cart item rows are at least 48px tall for easy deletion/quantity adjustment.
- Search bar and text inputs are 40–48px tall, meeting WCAG touch guidelines.

### Collapsing Strategy
- On mobile (< 744px), the top-nav collapses to a hamburger icon; the full menu appears as a slide-in drawer from the left.
- Product filters (if present) collapse into a “Filter” button that opens a modal or bottom sheet.
- The footer’s multi-column link sections stack into a single column on mobile.
- Hero sections may reduce image height and stack text below the image on small screens.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found in the extracted CSS; the typeface is assumed to be Inter (or a similar geometric sans-serif) based on common Shopify usage and the brand’s aesthetic. This should be verified against the live site’s CSS.
- Hover states for buttons and cards are inferred from common patterns; exact colors (e.g., button-secondary hover) were not extracted.
- Error states for form inputs (red borders, error text) were not observed and are not defined.
- The top-nav’s backdrop-filter blur value (8px) is an estimate; the actual value may differ.
- Dark mode is not supported; the site uses a light canvas with dark ink throughout.
- The extracted hex list (#fc8259, #dedede, #121212) is sparse; the brand may use additional accent colors (e.g., for limited-edition drops or seasonal collections) that were not captured.
- Shopify checkout widget colors (e.g., for payment buttons) are not included; they follow Shopify’s default palette.
- Animation durations and easing curves (e.g., for hover transitions, card lifts) were not extracted.
- The product card’s hover state (shadow lift) is assumed; exact shadow values are unknown.
- The badge positioning (top-left overlay on product images) is inferred from common e-commerce patterns.
- The footer’s social icon colors (e.g., Instagram, Twitter) were not extracted and may use brand-specific hues.
