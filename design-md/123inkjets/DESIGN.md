---
version: alpha
name: "123inkjets"
source_url: "https://www.123inkjets.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The price point comes first. Every surface on 123inkjets resolves to a value signal — a compatibility guarantee, a bulk-tier callout, or a clearance badge — anchored by an emphatic #ff5501 orange that handles every primary CTA against an otherwise monochromatic infrastructure of neutral grays. The platform is Magento (magento-icons and boilerplate-theme-icons surface in the font stack), and the design defers to Luma-era conventions: a utility top bar for account links and mini-cart count, a search-dominant masthead, and a category-tree sidebar on listing pages. This is a catalog environment designed for a purchasing agent or IT manager who arrives with a model number and expects friction-free navigation to the correct cartridge.

  Open Sans runs the entire typographic system — 400 weight for body and specs copy, 700 for price figures and CTAs — without any custom display typeface. The choice matches the brand's register: legible, neutral, familiar, with no ornamental weight to slow scan-reading of product rows. Ink sits at near-black #111111 and #303030, muted details at #555555 and #777777, while grid separators and card borders cycle through a sequence of near-identical grays (#d1d1d1, #c2c2c2, #e4e4e4, #e8e8e8) that creates density without visual noise.

  The blue layer — #1979c3 for links, #006bb4 for darker hover states, #68a8e0 for supporting interactive elements — runs the navigation chrome and account action links, keeping the Magento-conventional brand color intact while the orange handles conversion pressure. A secondary warm-amber system (#fdf0d5 field, #c07600 accent, #6f4400 text anchors) appears in free-shipping callouts and promotional strips, reading as deal energy without triggering the alarm of full red. Error states and out-of-stock warnings claim #e02b27 for themselves alone.

  Corner radii are minimal throughout: product cards and form inputs use {rounded.sm} or {rounded.md}, buttons use {rounded.sm}, and the overall grid trusts structure over softness. The result is a dense, scannable storefront that puts model compatibility and price-per-page economics in front of the customer before any brand sentiment is asked for.

colors:
  primary: "#ff5501"
  primary-active: "#c94300"
  primary-disabled: "#ffb899"
  brand-blue: "#1979c3"
  brand-blue-dark: "#006bb4"
  brand-blue-light: "#68a8e0"
  ink: "#111111"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#777777"
  hairline: "#d1d1d1"
  hairline-soft: "#e4e4e4"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-warm: "#fdf0d5"
  on-primary: "#ffffff"
  error: "#e02b27"
  sale-text: "#6f4400"
  sale-accent: "#c07600"
  sale-bg: "#fdf0d5"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  breadcrumb:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 3px
  md: 4px
  lg: 8px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.brand-blue}"
    border: "1px solid {colors.brand-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.brand-blue-dark}"
    border: "1px solid {colors.brand-blue-dark}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 38px
    typography: "{typography.body-md}"
  text-input-focus:
    border: "1px solid {colors.brand-blue}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.brand-blue}"
    typography: "{typography.nav-link}"
    height: 100px
    borderBottom: "1px solid {colors.hairline}"
  nav-top-strip:
    backgroundColor: "{colors.brand-blue-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
    typography: "{typography.body-md}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
    imageAspect: "1/1"
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.brand-blue}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-sm}"
      rounded: "{rounded.sm}"
  compatibility-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  sale-banner:
    backgroundColor: "{colors.sale-bg}"
    textColor: "{colors.sale-text}"
    accentColor: "{colors.sale-accent}"
    border: "1px solid {colors.sale-accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  free-shipping-strip:
    backgroundColor: "{colors.brand-blue-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
    textAlign: center
  breadcrumb:
    textColor: "{colors.brand-blue}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    borderRight: "1px solid {colors.hairline}"
    linkColor: "{colors.brand-blue}"
    linkTypography: "{typography.nav-link}"
    activeLinkColor: "{colors.primary}"
    activeLinkFontWeight: 700
    padding: "{spacing.sm}"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  error-message:
    textColor: "{colors.error}"
    typography: "{typography.caption}"
    iconColor: "{colors.error}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.brand-blue-light}"
    typography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.base}"

## Components

### Buttons

**`button-primary`** — The conversion workhorse of the entire catalog, rendered in #ff5501 orange with white text at 14px/700 Open Sans, 40px tall, minimal 3px radius. On hover the field deepens to `{colors.primary-active}` (#c94300); disabled state bleaches to #ffb899. The orange appears on exactly one element type per page — "Add to Cart," "Buy Now," and checkout actions — preserving its signal value by being absent from all navigation and informational chrome.

**`button-secondary`** — White-field outlined button with #1979c3 border and matching text, used for secondary actions: Save to List, Compare, printer-model toggles. Hover shifts the field to `{colors.surface-soft}` and darkens the border to `{colors.brand-blue-dark}`. Shares height (40px) and radius ({rounded.sm}) with the primary so the two can sit side by side on a product detail page without optical mismatch.

### Search

**`search-bar`** — The masthead's dominant element: a rectangular input with no border radius at 40px height, occupying roughly half the header width. A flush-right submit button in `{colors.primary}` orange mirrors the primary button treatment — no radius, same height, white icon. Placeholder text sits in `{colors.muted}`. Given that customers arrive with a specific cartridge SKU in mind, the search bar functions as the primary navigation instrument; the category sidebar is secondary.

### Navigation

**`nav-bar`** — A two-tier masthead. The upper `nav-top-strip` is a 32px band in #006bb4 carrying account links, a phone support number, and a cart summary in 12px white caption type. Below it, a 68px white bar holds the logo left, the search bar center, and cart/account icons right, with a `{colors.hairline}` bottom border separating it from page content. The combined assembly is 100px. No mega-menu animations — category navigation lives in the left sidebar on listing pages.

**`nav-top-strip`** — The utility layer above the main header: #006bb4 background, white 12px caption text, housing "Sign In / Create Account," order tracking, and customer service phone number. Collapses entirely on mobile to preserve vertical space.

**`category-sidebar`** — A `{colors.surface-soft}` left-rail panel with a `{colors.hairline}` right border, displaying the brand → model → cartridge-type hierarchy in 13px Open Sans nav-link style. The active category link switches to `{colors.primary}` orange at weight 700, the only orange that appears outside a button context. Width is approximately 220px at desktop.

### Product Card

**`product-card`** — A hairline-bordered (#d1d1d1) white tile arranged in a 4-column grid at desktop. Content stacks vertically: square product image (1:1 aspect), product title as a `{colors.brand-blue}` link in 14px/400, a `compatibility-tag` in muted gray, price in 22px/700 (`{typography.price-display}`), and an orange `{colors.primary}` CTA button. No border radius anywhere. The card's density is tuned for scanning across many SKUs, not for dwelling on photography.

**`compatibility-tag`** — A rectangular label (no radius, 2px top/bottom, 6px sides) in `{colors.surface-soft}` with a `{colors.hairline-soft}` border and `{colors.muted}` text at 12px. Reads "Compatible with HP LaserJet Pro M404dn..." and appears below the product title, directly above the price. Critical wayfinding for a catalog organized by printer model.

**`price-badge`** — An #ff5501 rectangular flag (no radius, 2px/6px padding) with white text at 11px/700 uppercase. Pins to the top-left corner of product images to flag savings percentages, new arrivals, or multi-pack bundles. The only element besides primary buttons that uses the orange.

### Promotional

**`sale-banner`** — A warm-cream `{colors.sale-bg}` band bordered by a 1px `{colors.sale-accent}` (#c07600) stroke, with `{colors.sale-text}` (#6f4400) body copy and `{colors.sale-accent}` emphasis text. Used for free-shipping thresholds ("Free shipping on orders over $35"), coupon code announcements, and seasonal promotions. The warm amber reads as deal energy without the alarm quality of red.

**`free-shipping-strip`** — A slim ~30px `{colors.brand-blue-dark}` band pinned above the nav-top-strip as a persistent brand-level promise ("Free Shipping on Orders Over $35"). Distinct from the `sale-banner` in register — blue signals policy, amber signals promotion.

### Trust & Utility

**`trust-badge`** — Small white card with `{colors.hairline}` border and 4px radius carrying an icon plus caption for "Secure Checkout," "Satisfaction Guarantee," or "Fast Shipping" in 12px `{colors.muted}` text. Arranged horizontally below the cart summary on the product detail page and repeated in a footer trust rail.

**`breadcrumb`** — 12px Open Sans links in `{colors.brand-blue}`, separated by `>` in `{colors.muted-soft}`. The current page segment displays in `{colors.muted}` as non-linked text. Sits 8px below the nav bottom border.

**`error-message`** — Inline text in `{colors.error}` (#e02b27) at 12px/400, appearing below form fields that fail validation. The enclosing input border also shifts to `{colors.error}` on failure. Used for address form errors, login failures, and out-of-stock alerts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category sidebar collapses to a horizontal filter chip bar above listings; search bar stacks above logo in masthead; nav-top-strip hidden; cart icon and hamburger remain fixed |
| Tablet | 744–1128px | 2-column product grid; sidebar may appear as a collapsible off-canvas drawer; search bar full-width in masthead; trust badges collapse to icon-only |
| Desktop | 1128–1440px | 4-column product grid with category sidebar at ~220px; full two-tier masthead; sale-banner and free-shipping-strip full-width above fold |
| Wide | > 1440px | Content constrained to ~1440px max-width centered in a `{colors.surface-soft}` page gutter; grid stays at 4 columns; masthead side padding increases |

### Touch Targets

- All CTA buttons minimum 40px height; 44px target area on mobile via padding extension
- Category sidebar links minimum 44px tap height on mobile drawer
- Search submit button expands to 44×44px tap area on mobile
- Cart, account, and hamburger icon buttons minimum 44×44px
- Compatibility filter chips minimum 36px height on mobile filter bar

### Collapsing Strategy

- Category tree sidebar converts to a horizontal filter chip row pinned above the product grid on mobile and tablet
- `nav-top-strip` hidden on mobile to recover ~32px of vertical space
- Product card CTA button expands to full card width on single-column mobile layout
- Breadcrumb truncates middle segments with ellipsis on viewports under 480px
- Footer multi-column link grid stacks to single accordion-style sections on mobile
- Trust badge row switches from horizontal to a 2×2 grid on tablet, single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display typeface confirmed — Open Sans appears to be the sole web font; webfont delivery via a CDN or JS loader not captured in static extraction may add weight variants not visible here
- True page canvas color not directly extracted — #ffffff is assumed; #f2f2f2 and #f0f0f0 both appear in the palette and may serve as the actual page background in some template zones
- Exact masthead height and logo dimensions unconfirmed; values above are derived from Magento Luma defaults rather than live measurement
- Magento Page Builder block styling (hero carousel overlay opacity, slide controls, video blocks) not extractable without full JS execution
- Mobile breakpoint values inferred from Magento Luma defaults; custom theme overrides may shift them
- Sale countdown timer and flash-sale overlay styling not captured
- Icon design (magento-icons, boilerplate-theme-icons) is an icon-font stack — no SVG geometry or sizing tokens available from extraction
- Dark mode or high-contrast mode not detected; site appears to be light-only with no prefers-color-scheme handling
