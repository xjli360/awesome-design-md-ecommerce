---
version: alpha
name: "Mogix"
source_url: "https://www.mogixaccessories.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The product is a USB-C cable coiled inside a retail blister pack — Mogix lives entirely in the utility tier of phone accessories, where specs (cable gauge, wattage, compatibility chip) do more selling than visual style. That pragmatic honesty should shape the entire design system: a single assertive action color against a clean white canvas, dense product grids that echo an online tech shelf, and trust signals — compatibility badges, warranty callouts, certification marks — surfaced prominently rather than buried in footers. No live site tokens were extractable (the site appears to serve tokens via JavaScript or is behind bot-detection), so the palette and type stack below are inferred from the brand's public product presence rather than confirmed source CSS. The blue-forward primary (#0055aa, inferred) belongs to the family of colors tech-utility brands historically reach for — legible on white, assertive enough for CTAs, neutral enough not to clash with product photography on matte black, gray, or stark white backgrounds. Type is expected to run on a system sans-serif or clean geometric grotesque at weights 400–600; no custom display typeface has been documented. Layout follows a mobile-first grid where search and category filters compress into a bottom-sheet drawer below 744px, since most accessory discovery happens on the very phone being accessorized. Rounded corners stay conservative — `{rounded.sm}` for cards, `{rounded.md}` for modals — functional rather than playful. Cart and quick-add interactions should feel instantaneous: tap, brief confirmation micro-animation, done. A trust band placed beneath the hero, showing shipping-threshold callouts, secure-checkout icons, and return-policy copy, is the brand's primary purchase-anxiety reducer and must remain visible above the fold on desktop. The canvas is white (#ffffff) with a barely-tinted surface (#f5f6f8) for card wells and alternating section backgrounds. Ink (#1a1a1a) anchors all body copy.

colors:
  primary: "#0055aa"
  primary-active: "#003d80"
  primary-disabled: "#99c2e8"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#e2e4e8"
  hairline-soft: "#f0f1f3"
  canvas: "#ffffff"
  surface-soft: "#f5f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#22844a"
  warning: "#d97706"
  error: "#dc2626"
  badge-sale: "#e53e3e"
  badge-new: "#0055aa"
  star: "#f59e0b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 48px
    iconLeft: cart-icon
  button-buy-now:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 14px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.md}"
    shadow: "0 1px 4px rgba(0,0,0,0.08)"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  badge-compatibility:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 360px
    layout: split-image-right
  trust-band:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    iconColor: "{colors.primary}"
  star-rating:
    starColor: "{colors.star}"
    countColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  filter-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    activeChipBackground: "{colors.primary}"
    activeChipTextColor: "{colors.on-primary}"
    chipRounded: "{rounded.full}"
  pagination:
    textColor: "{colors.body}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — The primary action button uses `{colors.primary}` (#0055aa, inferred) fill with `{colors.on-primary}` text at `{typography.button-md}` weight 600, height 44px, and `{rounded.sm}` corners. Hover shifts background to `{colors.primary-active}` (#003d80); disabled state falls back to the pale `{colors.primary-disabled}`. Flat, no shadow — directness over decoration.

**`button-secondary`** — Ghost variant with a 1.5px `{colors.primary}`-colored border and matching text on a `{colors.canvas}` background. Typically paired with `button-primary` on product pages for secondary actions like "Save for Later" or "Add to Wishlist." Border radius and height match primary for clean row alignment.

**`button-add-to-cart`** — A tall 48px button in `{colors.primary}` with a leading cart icon and `{typography.button-md}` label. The dominant CTA on every product detail page. Spans full width on mobile and pins to the bottom viewport edge when the product form scrolls out of view.

**`button-buy-now`** — `{colors.ink}` (#1a1a1a) fill, `{colors.on-primary}` text, same geometry as add-to-cart. Stacked directly below add-to-cart on PDP, offering a one-tap checkout shortcut without competing for primary CTA hierarchy.

### Navigation

**`nav-bar`** — 60px tall `{colors.canvas}` bar with a 1px `{colors.hairline}` bottom border. Logo sits left at roughly 120px wide; search bar occupies the center 40% on desktop; cart icon with numeric badge sits at far right. Below 744px the bar collapses to logo + hamburger icon + cart only.

**`nav-bar-top-strip`** — A 36px announcement stripe in `{colors.primary}` with `{colors.on-primary}` text at `{typography.caption}` weight. Carries shipping thresholds ("Free shipping on orders over $25") or active promotional codes. Stacks above the main nav, disappears on mobile or collapses to a marquee.

**`search-bar`** — 40px input with `{colors.surface-soft}` background at rest; border sharpens to 1.5px `{colors.primary}` on focus. A magnifier icon sits inside the leading edge. Autocomplete dropdown surfaces product name matches and top category shortcuts. Rounded at `{rounded.xs}` for a tight, utilitarian feel.

### Product Cards

**`product-card`** — Square 1:1 image well at top, followed by a `star-rating` row, product title in `{typography.title-sm}`, device-compatibility caption in `{typography.body-sm}` and `{colors.muted}`, then price in `{typography.price-display}`. Card carries a 1px `{colors.hairline}` border, `{rounded.sm}` corners, and a soft 0 1px 4px shadow that intensifies slightly on hover. A quick-add icon button overlays the image on desktop hover only.

**`badge-sale`** — `{colors.badge-sale}` (#e53e3e) pill anchored top-left on the product card image. Uppercase `{typography.badge}` text, 3px vertical / 7px horizontal padding, `{rounded.xs}`. Used for percentage-off promotions.

**`badge-new`** — Same structure as badge-sale but in `{colors.badge-new}` (#0055aa). Applied to recently listed products, positioned adjacent to badge-sale when both conditions apply.

**`badge-compatibility`** — A hairline-bordered, `{colors.surface-soft}` background chip listing device compatibility (e.g., "For iPhone 15 / 14"). Rendered as a horizontal scroll row beneath the product title on PDP, or as a filter chip in the grid filter rail.

### Hero & Trust Sections

**`hero-banner`** — Split layout: headline and CTA left, product photography right, on a `{colors.surface-soft}` background. Headline at `{typography.display-xl}`, supporting text at `{typography.body-md}`. Minimum height 360px on desktop. On mobile the image moves above the text block, CTA becomes full-width `button-add-to-cart`.

**`trust-band`** — A horizontal band of four icon+text trust signals (Free Shipping · 30-Day Returns · Secure Checkout · 12-Month Warranty) separated by vertical `{colors.hairline}` dividers. Background `{colors.surface-soft}`, icons in `{colors.primary}`, copy in `{typography.body-sm}` and `{colors.muted}`. Appears directly below the hero and again above the footer to bracket purchase intent zones.

### Filtering & Rating

**`filter-rail`** — On desktop, a 240px left-rail panel with checkbox groups for device compatibility, cable type, wattage, and color variant. Selected filters appear as `{colors.primary}` fill chips with `{colors.on-primary}` text at `{rounded.full}`. On mobile the panel slides up from a bottom sheet triggered by a "Filter & Sort" button at the top of the product grid.

**`star-rating`** — Five stars in `{colors.star}` (#f59e0b) amber, numeric review count in `{colors.muted}` at `{typography.caption}`. Appears on every product card and prominently on PDP directly beneath the product title. The full row is tappable and anchors to the reviews section.

**`breadcrumb`** — Small `{typography.caption}` path (Home / Cables / USB-C to USB-C) in `{colors.muted}` with a right-angle separator in `{colors.hairline}`. Current page segment renders in `{colors.ink}`. Sits flush with the page left edge, above the product title on PDP.

### Footer

**`footer`** — Full-width `{colors.ink}` (#1a1a1a) band with `{colors.on-primary}` text. Four-column link grid on desktop, collapsing to single-column accordion toggles on mobile. Column headings at `{typography.title-sm}` weight 600; links at `{typography.body-sm}` in `{colors.hairline-soft}` for sufficient contrast on dark. A newsletter sign-up row with a `text-input` and `button-primary` Submit sits in a dedicated bottom stripe above legal copy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter rail moves to bottom-sheet drawer; nav collapses to logo + hamburger + cart; hero stacks image above headline; add-to-cart CTA pins to bottom viewport edge |
| Tablet | 744–1128px | Two-column product grid; filter rail remains left-side but icon-collapsed at 48px wide; hero maintains split layout with reduced side padding |
| Desktop | 1128–1440px | Three-column product grid; full 240px left filter rail; four-column footer; trust band shows all four signals inline |
| Wide | > 1440px | Content max-width 1400px centered; grid may expand to four columns; hero image scales but headline column caps at 600px |

### Touch Targets

- All interactive elements minimum 44 × 44px on mobile
- Add-to-cart and buy-now buttons expand to full width on mobile viewports
- Filter chips minimum 36px tall with 12px horizontal padding
- Hamburger menu nav links minimum 48px tall
- Star rating row tappable as a full unit, linking to the reviews anchor on PDP

### Collapsing Strategy

- Nav: logo + hamburger + cart only below 744px; mega-menu or category links replaced by a full-screen slide-in drawer
- Filter panel: hidden behind "Filter & Sort" bottom-sheet trigger below 744px; icon-only collapsed sidebar at 744–1128px; full labeled panel above 1128px
- Hero: image moves above text block on mobile; CTA spans full width; min-height reduces to 280px
- Footer: four columns collapse to single-column accordion with disclosure toggles below 744px
- Trust band: four items remain inline at tablet and desktop; wraps to 2×2 icon grid on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All color values are inferred** — no hex colors were extractable from the live site (likely JS-rendered tokens or bot-detection active). Primary blue (#0055aa) and every palette entry are educated approximations, not confirmed brand values.
- **Font family unknown** — no font-family stacks were detected by extraction. System UI sans-serif stack is used as a safe neutral placeholder; the brand may use a purchased geometric grotesque such as Inter, DM Sans, or Nunito.
- **Brand-specific accent colors unconfirmed** — badge red, star amber, and success green are category conventions, not extracted brand decisions.
- **Logo and iconography system not analyzed** — icon style (outline vs. filled, stroke weight, corner treatment) could not be determined from extraction data.
- **Dark mode** — no evidence one way or the other; not specified in this file.
- **Animation and motion tokens** — no transition timing or easing curves were inferrable without live CSS access.
- **Platform** — flagged as non-Shopify; underlying e-commerce platform unknown, which may affect cart component naming and checkout flow conventions.
- **Product detail page layout** — image gallery behavior (zoom, swipe, thumbnail strip) is unconfirmed and not specified above.
