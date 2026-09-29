---
version: alpha
name: "Deathwish Inc"
source_url: "https://www.deathwishinc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label and shop that wears its hardcore-punk lineage in a single blood-red hex — #d54d4d — deployed sparingly against a near-black #121212 canvas and a secondary deep-teal #1d2727 that reads like ink on newsprint. The brand does not shout; it lets the red do the work: a primary CTA button, a sale badge, a cart count, nothing more. Everything else is monochrome — #f8f7f7 for body text on dark backgrounds, #dedede for hairline borders, and the full white #ffffff canvas for product photography and editorial spreads. The typography stack is a defensive system-ui fallback chain (system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu) with no custom brand font declared — a pragmatic choice that prioritizes legibility over personality, letting the music and merchandise carry the voice. Buttons are sharp-cornered rectangles (`{rounded.none}`) with generous padding, a deliberate anti-softness that distinguishes Deathwish from the pill-button ecommerce default. The nav bar is a full-bleed black strip with white text, the logo sits left in a bold sans-serif wordmark, and the search icon is a simple outline — no orb, no glow. Product cards use a white surface (`{surface-card}`) with a thin `{hairline}` border, the price set in `{body-md}` weight 600, the band name in `{caption}` weight 400. The overall feel is that of a zine layout translated to web: high contrast, minimal ornament, and a trust that the content — album art, tour dates, merch photos — will provide all the texture the page needs.

colors:
  primary: "#d54d4d"
  primary-active: "#b33a3a"
  primary-disabled: "#e8a0a0"
  ink: "#121212"
  body: "#f8f7f7"
  muted: "#dedede"
  muted-soft: "#c0c0c0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f8f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f8f7f7"
  accent-teal: "#1d2727"
  badge-sale: "#d54d4d"
  badge-new: "#121212"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 11px
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
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    borderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: 1px solid "{colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  cart-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, always rendered in `{colors.primary}` (#d54d4d) with white text and zero border radius. Used for "Add to Cart", "Pre-Order", and "Subscribe" actions. On hover, shifts to `{colors.primary-active}` (#b33a3a). Disabled state uses `{colors.primary-disabled}` (#e8a0a0). Text is uppercase weight 600 with tight letter-spacing.
**`button-secondary`** — A white button with `{colors.ink}` text, used for secondary actions like "View Details" or "Continue Shopping". Outline variant (`button-secondary-outline`) uses a transparent background with a 1px `{colors.ink}` border. All buttons share the same 44px height and `{rounded.none}` sharp corners.
**`button-ghost`** — A text-only button with no background or border, used for navigation links within content areas (e.g., "Read More", "Shop All"). Hover state adds a subtle underline.

### Navigation
**`nav-bar`** — A full-bleed black (`{colors.ink}`) strip at 64px height. The brand logo sits left-aligned, navigation links are uppercase weight 600 with 0.5px letter-spacing. Active link uses `{colors.primary}` for the text color. The cart icon sits right-aligned with a `{cart-count}` badge in `{colors.primary}`.
**`nav-link`** — Inline navigation items with 8px horizontal padding. Hover state adds a 1px bottom border in `{colors.primary}`.

### Cards
**`product-card`** — A white card with a 1px `{colors.hairline}` border and no border radius. Contains a full-width product image, the band/artist name in `{title-md}`, and the price in `{body-md}` weight 600. Sale items display a `{badge-sale}` in the top-left corner. Cards stack in a responsive grid with `{spacing.base}` gap.
**`product-card-title`** — The product name, set in `{typography.title-md}` (16px weight 600). Truncates to one line on mobile.
**`product-card-price`** — The price, set in `{typography.body-md}` with weight 600. Sale prices are shown in `{colors.primary}`.

### Forms
**`text-input`** — A simple white input field with no border radius. Focus state adds a 2px `{colors.ink}` border. Used for email signup, search, and checkout fields. Height is 44px to match button height for alignment.

### Badges
**`badge-sale`** — A small red (`{colors.primary}`) badge with white uppercase text, used to flag sale items on product cards and collection pages. No border radius, 4px padding.
**`badge-new`** — A black (`{colors.ink}`) badge with white text, used for new arrivals or pre-order items.

### Footer
**`footer`** — A full-width black (`{colors.ink}`) section with white text. Contains links to label info, tour dates, privacy policy, and social icons. Links use `{typography.link}` (14px weight 400). Padding is `{spacing.section}` top/bottom, `{spacing.base}` left/right.

### Hero
**`hero-section`** — A full-width black section used on the homepage and collection landing pages. Contains a large `{display-xl}` headline, optional supporting text in `{body-md}`, and a single `{hero-cta}` button in `{colors.primary}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu. Product cards stack single-column. Hero text reduces to `{display-md}`. Footer links stack vertically. |
| Tablet | 744–1128px | Nav links visible but condensed. Product cards in 2-column grid. Hero maintains `{display-lg}`. |
| Desktop | 1128–1440px | Full nav with all links. Product cards in 3- or 4-column grid. Hero uses `{display-xl}`. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility.
- Nav links have 48px minimum touch area (8px padding + text height).
- Cart icon has 44x44px touch target.
- Product card images link to product page with full card tap area.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger icon with a slide-out drawer menu.
- The product grid collapses from 4 columns (desktop) to 2 columns (tablet) to 1 column (mobile).
- The footer link columns collapse from 4 columns (desktop) to 2 columns (tablet) to a single vertical stack (mobile).
- Hero sections reduce font size and may stack CTA below text on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font was detected; the site relies on system-ui fallback chain. A custom typeface (e.g., a bold grotesk or gothic) may be used in the logo but is not declared in CSS.
- Hover and focus states for text inputs and secondary buttons were not fully extracted — assumed to use `{colors.ink}` border or underline.
- Error styling (form validation, 404 pages) was not observed.
- Dark mode is not supported; the site uses a fixed light canvas with black nav/footer.
- Sub-brand or collection-specific color palettes (e.g., for specific band merch drops) were not captured.
- The extracted hex list included #1d2727 (a deep teal) which appears as a secondary accent in some sections (e.g., footer backgrounds on certain pages) but its usage is inconsistent — it may be a legacy color or a sub-brand token.
- Social icon colors (e.g., Instagram gradient, YouTube red) were filtered out but may appear in the footer.
- Checkout flow (Shopify-powered) may introduce additional colors (e.g., Shopify green for payment buttons) that are not part of the brand system.
- The `!important` flag in font-family declarations suggests some overrides in the CSS — the exact cascade priority is unclear.
