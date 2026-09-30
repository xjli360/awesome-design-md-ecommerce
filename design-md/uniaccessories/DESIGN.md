---
version: alpha
name: "UniAccessories"
source_url: "https://www.uniaccessories.io"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A sharp, monochrome accessory marketplace where #eb1256 — a precise, unapologetic magenta — acts as the single voltage point against a near-black #121212 ink and a #ffffff canvas. The brand trusts high-contrast product photography and generous whitespace over decorative typography, using a system font stack that keeps load times fast and the interface invisible. Every primary CTA, sale badge, and cart indicator carries that magenta charge, while the secondary palette stays in the gray spectrum — #e5e5e5 for soft surfaces, #dedede for hairlines, #808080 and #777777 for muted text. The visual language is deliberately uncluttered: pill-shaped search bars (`{rounded.full}`) and softly rounded product cards (`{rounded.md}` ~12px) create a friendly, approachable feel, while the near-black ink on white canvas delivers maximum readability. There are no decorative flourishes — no gradients, no illustrations, no secondary brand colors — just a tight system of two values (magenta and gray) doing all the work. The result is a storefront that feels both premium and utilitarian, where the product is the hero and the interface steps aside.

colors:
  primary: "#eb1256"
  primary-active: "#c40e48"
  primary-disabled: "#f5a3b8"
  ink: "#121212"
  body: "#212222"
  muted: "#808080"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#eb1256"
  stock-badge: "#121212"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  product-card-add-to-cart:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-stock:
    backgroundColor: "{colors.stock-badge}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-icon-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the storefront, used for "Add to Cart," "Checkout," and "Subscribe" actions. Rendered in the brand's magenta `{colors.primary}` with white text, it sits on a soft 8px radius (`{rounded.sm}`) at 44px height. On hover, it shifts to `{colors.primary-active}` (#c40e48); disabled state uses `{colors.primary-disabled}` (#f5a3b8). The `button-pill-primary` variant uses `{rounded.full}` for a friendlier, more promotional feel, often seen in sale banners or sticky CTAs.

**`button-secondary`** — A white button with a thin `{colors.hairline}` border, used for less prominent actions like "View Details" or "Continue Shopping." Active state darkens the border to `{colors.ink}` and adds a `{colors.surface-soft}` background. The `button-pill-outline` variant mirrors this in pill form for secondary promotional actions.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Clear Filters." Hover state adds a subtle `{colors.surface-soft}` background.

### Navigation
**`top-nav`** — A fixed 64px white bar with uppercase nav links in `{typography.nav-link}`. The active page link uses `{colors.primary}` magenta; inactive links are `{colors.ink}`. The cart icon sits on the right with a magenta count badge (`{rounded.full}`) showing item quantity. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Cards
**`product-card`** — A white card with 12px rounded corners (`{rounded.md}`) containing a product image, title in `{typography.title-sm}`, and price in `{typography.body-md}`. Sale prices render in `{colors.primary}`. An "Add to Cart" pill button (`{rounded.full}`) in near-black `{colors.ink}` sits at the bottom of the card, appearing on hover on desktop and always visible on mobile. Cards have no shadow — the brand relies on the white-on-white contrast and the `{colors.hairline}` grid to define boundaries.

### Badges
**`badge-sale`** — A small magenta badge (`{colors.sale-badge}`) with uppercase white text, placed on the top-left corner of product images. Uses `{rounded.xs}` (4px) for a crisp, intentional look. `badge-stock` uses near-black `{colors.stock-badge}` for "Low Stock" or "New" indicators.

### Forms
**`text-input`** — A 44px white input with a `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}`. Error state also uses `{colors.primary}` border with an error message in `{colors.primary}` text below.

**`search-bar`** — A pill-shaped (`{rounded.full}`) 48px search field with a `{colors.surface-soft}` background. On focus, it expands to a white background with a `{colors.primary}` border, often revealing a dropdown of recent searches or suggestions.

### Footer
**`footer`** — A full-width near-black (`{colors.ink}`) section with white body text and muted gray links (`{colors.muted}`). Links hover to white. The footer contains brand info, navigation columns, and social links, all set in `{typography.body-sm}` with generous `{spacing.xxl}` padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; search bar moves to sticky header; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar in header; footer in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; search bar in center; footer in four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav remains unchanged |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card "Add to Cart" buttons are always visible on mobile (not hover-dependent)
- Search bar expands to full width on mobile with a prominent tap target
- Nav hamburger icon is 44x44px minimum
- Cart icon and count badge combined tap target is 44x44px

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a full-screen overlay drawer
- Product grid collapses from 4 columns to 1 column on mobile
- Footer navigation collapses from 4 columns to a single vertical stack
- Search bar collapses from centered desktop position to full-width sticky bar on mobile
- Secondary navigation (category strip) collapses to a horizontal scrollable strip on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- The extracted color list is dominated by grayscale tones (#e5e5e5, #dedede, #808080, #777777, #212222, #121212) with a single magenta accent (#eb1256). While #eb1256 is clearly the brand's primary, the secondary palette may include additional accent colors not captured in the extraction (e.g., for seasonal promotions or category badges).
- No custom font family was detected — the site uses the system font stack. The brand may use a custom typeface on non-extracted pages (e.g., marketing landing pages, blog).
- Hover states for buttons and links are inferred from common ecommerce patterns; actual hover colors may differ.
- Error states for forms (validation messages, error icons) were not extracted.
- Dark mode support is unknown; the extracted theme-color is #ffffff, suggesting light mode only.
- Checkout flow colors (Shopify Pay, Klarna, Afterpay widgets) were filtered out but may introduce additional brand-adjacent colors.
- Spacing values are estimated based on common ecommerce patterns; actual spacing may vary.
- The site may use a secondary brand color for specific categories or promotions that wasn't captured in the extraction.
