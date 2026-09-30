---
version: alpha
name: "BAPE"
source_url: "https://bape.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Seven achromatic values — the complete extracted palette — carry the entire BAPE digital shell, from deepest-black #121212 navigation ground through #dedede hairlines to near-white #eeeeee surface lifts. All chromatic energy is deliberately exiled into the product imagery: ABC Camo in acid-washed pastels, Shark Full-Zip olive, and BAPESTA chrome arrive as eruptions against a cold neutral frame that never competes with the UI layer. The single font detection resolves to monospace, a signal that reads as military stencil and urban brutalism simultaneously — type that feels like a classified requisition form rather than a lifestyle catalog. Every letterform runs uppercase across buttons, nav labels, and product copy, a blanket refusal to soften toward the consumer. Buttons carry zero border-radius ({rounded.none}), hard black rectangles stamped on white or inverted, with no softening corner anywhere in the interface — a visual policy that holds from the Add to Cart CTA down to the size-selector grid. The nav sits at a compact 60px with a pure #121212 announcement bar above it, giving the brand ownership of the entire viewport crown. Product cards are flush and unpadded, relying entirely on APE HEAD silhouettes and camouflage print photography for visual differentiation — the card chrome contributes nothing beyond a monospace price line. On mobile the navigation collapses to a full-screen #121212 overlay rather than a slide-out drawer, a vault-door effect that preserves the brand's monolithic texture at every breakpoint. Spacing is tight and architectural: product grids run at minimal gutters, the section rhythm compressed compared to lifestyle brands, consistent with a drop-scarcity psychology that frames each product page as an inventory transaction rather than an aspiration.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#777777"
  ink: "#191919"
  body: "#555555"
  muted: "#777777"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-medium: "#e2e2e2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "monospace"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-lg:
    fontFamily: "monospace"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "monospace"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 2px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
    width: 100%
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    iconColor: "{colors.ink}"
    iconSize: 20px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 36px
    textAlign: center
    padding: 0 {spacing.base}
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    imageFit: cover
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-lg}"
    salePriceColor: "{colors.body}"
    originalPriceColor: "{colors.muted}"
    padding: 0
    gap: "{spacing.sm}"
    hoverEffect: image-scale-1.03
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imageOverlay: "rgba(0,0,0,0.3)"
    ctaComponent: button-primary
  camo-swatch:
    size: 24px
    rounded: "{rounded.none}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "2px solid {colors.hairline}"
    gap: "{spacing.xs}"
    tooltipTypography: "{typography.caption}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    backgroundSelected: "{colors.ink}"
    textColorSelected: "{colors.on-primary}"
    backgroundSoldOut: "{colors.surface-soft}"
    textColorSoldOut: "{colors.muted}"
    height: 40px
    padding: 0 12px
    gap: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-limited:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 3px 6px
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    borderFocus: "1px solid {colors.ink}"
    height: 44px
    padding: 0 {spacing.base}
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    headingTypography: "{typography.label-sm}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.surface-medium}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: none
    columnGap: "{spacing.xxl}"
  mobile-menu-overlay:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    transition: opacity 200ms ease
    width: 100vw
    height: 100vh
    padding: "{spacing.lg} {spacing.base}"
    subitemTypography: "{typography.body-md}"
  product-grid:
    columns-mobile: 2
    columns-tablet: 3
    columns-desktop: 4
    gap: "{spacing.sm}"
    padding: 0 {spacing.base}

## Components

### Buttons

**`button-primary`** — Full-width, zero-radius black rectangle at 48px height, uppercase monospace tracking set at 1px. Hover transitions to pure #000000; disabled state flattens to {colors.primary-disabled} with `not-allowed` cursor. Applied to Add to Cart, Checkout, and all primary conversion CTAs — the absence of any radius is the signature, distinguishing BAPE from every rounded-corner streetwear competitor.

**`button-secondary`** — White fill with a 1px {colors.ink} border, same monospace uppercase spec as primary. Hover introduces a {colors.surface-soft} background tint while preserving the border. Used for secondary actions like Save to Wishlist or Continue Shopping.

**`button-primary-disabled`** — {colors.primary-disabled} fill with {colors.on-primary} text, visually muted but retaining the hard rectangle shape and uppercase label. Never softens to a rounded state even when inactive.

### Text Inputs

**`text-input`** — No border-radius, 1px {colors.hairline} border at rest, upgrading to 1px {colors.ink} on focus. Placeholder in {colors.muted}. Used in search, checkout fields, and newsletter forms. The sharp-cornered input reinforces the zero-softening policy established by the button system.

### Navigation Bar

**`nav-bar`** — 60px height on a white {colors.canvas} ground with a 1px {colors.hairline} bottom border. All link labels in {typography.nav-link} — 12px monospace, 1.5px letter-spacing, uppercase. Icon set (cart, search, account) rendered as thin 20px strokes in {colors.ink}. The compact height keeps vertical real estate minimal and avoids the generous nav padding common to lifestyle brands.

**`announcement-bar`** — 36px strip in {colors.primary} above the nav, {typography.label-sm} centered in {colors.on-primary}. Used for drop announcements, shipping promotions, and regional notices. The black-on-black layering of announcement bar over nav creates a bold viewport crown.

### Product Card

**`product-card`** — Zero padding, zero radius, 4:5 aspect-ratio product image with scale-to-1.03 hover effect on the image. Title in {typography.body-sm}, price in {typography.price-lg}. Sale price in {colors.body}, struck-through original in {colors.muted}. Cards carry no border or shadow — the product photography is expected to do all the work of visual separation against the white canvas grid.

### Hero Banner

**`hero-banner`** — Full-bleed image with a 30% black scrim overlay, headline in {typography.display-xl} set uppercase, body copy in {typography.body-md}. Padding scales at {spacing.section} vertical. CTA defers to `button-primary` centered or left-aligned depending on layout. Used for seasonal campaign launches and new collection drops.

### Camo Swatches

**`camo-swatch`** — 24px square tiles with zero radius, 2px border in {colors.hairline} at rest upgrading to {colors.ink} when selected. Tooltip reveals color name in {typography.caption}. The only chromatic element in the UI chrome: BAPE Camo pattern thumbnails appear here in forest green, blue, pink, and ABC colorways. Gap held at {spacing.xs} to keep the swatch row dense.

### Size Selector

**`size-selector`** — 40px-height hard-rectangle toggles in monospace uppercase. Unselected: {colors.canvas} fill, 1px {colors.hairline} border. Selected: {colors.ink} fill with {colors.on-primary} text — inverts to black. Sold-out sizes: {colors.surface-soft} fill with {colors.muted} text, no strikethrough line needed given the obvious contrast. Gap between tiles held at {spacing.xs}.

### Badges

**`badge-new`** — Solid {colors.primary} chip in {typography.label-sm}, no radius, 3px × 6px padding. Overlays the top-left corner of product card images on new arrivals.

**`badge-sold-out`** — Same shape as `badge-new` but {colors.muted} fill, used as an image overlay when stock hits zero.

**`badge-limited`** — Outlined variant: white fill with 1px {colors.ink} border. Used for limited-edition and collaboration pieces where the scarcity signal should read as premium rather than depleted.

### Search Bar

**`search-bar`** — Full-width {colors.surface-soft} rectangle at 44px height, no radius, no border at rest, 1px {colors.ink} border on focus. Magnifier icon in {colors.muted}. Appears as an inline bar in the header on desktop; expands to full-viewport on mobile with the same sharp-corner treatment.

### Footer

**`footer`** — {colors.primary} ground with all text in {colors.on-primary}. Section headings in {typography.label-sm} uppercase, links in {typography.caption}. Multi-column layout on desktop (four columns at {spacing.xxl} gap) collapsing to stacked accordions on mobile. No hairline separator at top — the black ground creates a hard floor transition from the page.

### Mobile Menu Overlay

**`mobile-menu-overlay`** — Full-viewport #121212 takeover triggered by hamburger tap. Primary nav items in {typography.title-md} uppercase, subcategory items in {typography.body-md}. No slide-in animation — the overlay fades in at 200ms opacity transition, preserving the vault-door opening feel. Close button is a white × glyph in the top-right corner at 24px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product hero; 2-column product grid; nav collapses to full-screen overlay; size selectors wrap to full width; announcement bar truncates to single line |
| Tablet | 744–1128px | 3-column product grid; nav retains top bar but drops secondary category row; hero shifts to 50% text / 50% image split |
| Desktop | 1128–1440px | 4-column product grid; full horizontal nav with category flyouts; product detail layout switches to 50/50 image-stack / info-panel split |
| Wide | > 1440px | Max-width container at 1440px, centered on {colors.canvas}; product grid stays at 4 columns with expanded gutters; hero image allowed to bleed full viewport width behind contained text |

### Touch Targets

- All interactive size swatches minimum 40×40px tap surface even when rendered at 24px visual size
- Size selector tiles minimum 40px height, minimum 44px width
- Nav icons (cart, search, account) padded to 44×44px tap zones
- Footer accordion headers minimum 44px height on mobile
- Camo swatch tiles padded to 32×32px minimum tap zone

### Collapsing Strategy

- Secondary navigation categories collapse into mobile menu overlay, not into a bottom sheet or drawer
- Product filtering panel collapses to a full-screen modal overlay on mobile, not an inline expand
- Footer multi-column layout collapses to stacked accordions, with headings as tappable expand triggers
- Search collapses from inline header bar to full-screen input on mobile, with overlay scrim at {colors.scrim} 40% opacity
- Product image galleries collapse from side-scroll thumbnails on desktop to swipe carousel on mobile with dot indicators in {colors.muted}

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) was not present in the extracted palette; it is inferred from standard Shopify defaults and is widely observable as the page background — flag for manual verification
- Only "monospace" was detected in font stacks; BAPE likely uses a custom or licensed display typeface for large editorial headlines that loads via JavaScript after extraction — the actual font name is unconfirmed
- No chromatic brand accent was present in the extracted palette; BAPE product camo colorways (forest green, baby blue, pink, red, ABC multi) exist only inside product imagery and are not represented as UI tokens here
- Meta theme-color was absent; likely set dynamically via Shopify theme JS or not configured — canonical app chrome color is unverifiable
- Hover and focus animation durations were not captured; 200ms ease is assumed as a reasonable default
- Mobile menu overlay behavior (fade vs. slide) inferred from brand character rather than extracted animation values
- Any custom icon set or glyph font (BAPE uses branded iconography in some markets) could not be detected through extraction
