---
version: alpha
name: "Omi Woods"
source_url: "https://www.omiwoods.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dusty rose-mauve (#8c7e7e) stretched across product flatlay shadows — that warm, almost-skin neutral — signals before a word of copy loads that Omi Woods is working in a different register than the sterile white of conventional fine jewelry retail. The entire typographic system runs on Raleway alone, deployed from 40px editorial display at weight 300 down to 11px uppercase product tags at weight 700; its geometric skeleton stays legible at the lightest weights and gains authority at 600 without ever needing a second family. Color divides into two clear orbits — a warm-earth core of deep burgundy (#603a3a), dusty rose-mauve (#8c7e7e, #916c6c), layered blush tones (#d8d1d1, #d9c0c0, #c6a0a0), and near-black grounds (#090808, #211b1b) that carry all permanent UI; and a promotional layer of fire-red (#c50000, #e81000) against blush-tinted surface (#ffeae8) that marks sale events without overwhelming the brand register. A third accent — deep green (#007f5f) on pale mint (#e5fff8) — signals ethical sourcing credentials and in-stock availability, creating a three-tier signal hierarchy of brand warmth, commercial urgency, and environmental trust. Component shapes favor {rounded.none} and a restrained {rounded.xs} throughout — no pill forms, no bubbly radii — aligning the digital surface with the composed, editorial posture of contemporary fashion publishing rather than marketplace jewelry. Product cards lead with tight lifestyle photography shot against warm-neutral backgrounds, with price, material, and variant metadata rendered in body-sm Raleway below the frame. The overall system reads as a deliberate set of omissions: one font family, a narrow warm palette, minimal decoration — betting that photography and material quality carry conviction that UI embellishment cannot.

colors:
  primary: "#603a3a"
  primary-active: "#571f1f"
  primary-disabled: "#d9c0c0"
  ink: "#090808"
  body: "#211b1b"
  muted: "#777777"
  hairline: "#d5d5d5"
  hairline-soft: "#dcdcdc"
  canvas: "#f5f5f5"
  surface-soft: "#f2f2f2"
  surface-card: "#eeeeee"
  surface-strong: "#d6d6d6"
  on-primary: "#f5f5f5"
  brand-mauve: "#8c7e7e"
  brand-rose: "#916c6c"
  brand-blush: "#d8d1d1"
  brand-blush-soft: "#d9c0c0"
  brand-blush-muted: "#c6a0a0"
  sale: "#c50000"
  sale-active: "#e81000"
  sale-coral: "#ff6d6d"
  sale-surface: "#ffeae8"
  sale-surface-hover: "#ffc5c5"
  eco: "#007f5f"
  eco-surface: "#e5fff8"
  scrim: "#090808"

typography:
  display-xl:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 0
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.brand-mauve}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    height: 36px
    padding: 0 {spacing.base}
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.body}"
    salePriceColor: "{colors.sale}"
    originalPriceColor: "{colors.muted}"
    hoverEffect: image-scale-subtle
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    imagePosition: right
    minHeight: 600px
    padding: "{spacing.section} {spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    padding: "{spacing.xxl} 0 {spacing.xl}"
    textAlign: center
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  sale-surface-badge:
    backgroundColor: "{colors.sale-surface}"
    textColor: "{colors.sale}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  eco-badge:
    backgroundColor: "{colors.eco-surface}"
    textColor: "{colors.eco}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-gallery:
    backgroundColor: "{colors.surface-card}"
    thumbnailBorder: "1px solid {colors.hairline}"
    thumbnailBorderActive: "1px solid {colors.primary}"
    thumbnailSize: 72px
    rounded: "{rounded.none}"
    mainImageAspectRatio: "1/1"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    lineItemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    ctaComponent: button-primary
    subtotalTypography: "{typography.title-sm}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    width: 120px
  swatch-button:
    size: 24px
    borderRadius: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.brand-blush}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.brand-mauve}"
    padding: "{spacing.section} 0 {spacing.xl}"
    borderTop: "none"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    inputBorder: "none"
    inputBorderBottom: "1px solid {colors.hairline}"
    resultItemTypography: "{typography.body-md}"
    resultPriceTypography: "{typography.price-sm}"
    overlay: "rgba(9,8,8,0.4)"

## Components

### Buttons

**`button-primary`** — Filled deep-burgundy (#603a3a) block with uppercase Raleway at 14px/weight 600, 0.1em tracking, zero radius on all corners. Height 48px with 14px vertical and 32px horizontal padding. On hover transitions to `primary-active` (#571f1f); disabled state renders `primary-disabled` (#d9c0c0) fill with muted text to preserve spatial presence. Used exclusively for primary purchase actions: Add to Cart, Checkout, Proceed to Payment.

**`button-secondary`** — Transparent fill with a 1px `primary` (#603a3a) border and matching text, same uppercase Raleway and zero radius. On hover the border fills with the same burgundy and text inverts to `on-primary` — a deliberate reversal rather than a separate color. Deployed for secondary CTAs: Save to Wishlist, Shop Collection, Continue Shopping.

**`button-ghost`** — No border, no background; text-color ink with a 1px bottom border underline only. Used for tertiary navigation-adjacent actions like "View All," "Learn More," and filter reset links where a full button would add visual weight.

### Navigation

**`nav-bar`** — 64px-tall bar on `canvas` (#f5f5f5) with a 1px `hairline` bottom stroke. Logo renders in `display-sm` Raleway weight 400, left-aligned. Nav links in `nav-link` (14px weight 500, 0.04em tracking) centered horizontally between logo and utility icons. Utility row: search icon, wishlist count, cart icon with item count badge in `sale` (#c50000). No dropdown mega-menu signal in extracted data — assume flyout panels with collection links. Sticky on scroll with `canvas` background maintained.

**`announcement-bar`** — 36px stripe anchored above the nav in `primary` (#603a3a) with `on-primary` text in `label-upper` (11px, weight 700, uppercase, 0.08em spacing). Carries site-wide promotions, free shipping thresholds, and ethical sourcing messaging. Dismissible on mobile; persistent on desktop.

### Product Cards

**`product-card`** — Portrait 3:4 image on `surface-card` (#eeeeee) with zero radius. Below the image: product name in `body-sm` Raleway, current price in `price-sm` weight 400. On sale items show strike-through original price in `muted` (#777777) beside a sale price in `sale` (#c50000); a `sale-badge` chip overlays the top-left image corner. Hover triggers a subtle image scale (1.03×) within the card bounds rather than a shadow lift — no hard shadow appears anywhere in the component set.

### Hero Banner

**`hero-banner`** — Asymmetric two-column layout: editorial copy left (headline in `display-xl` weight 300, subhead in `body-md`), lifestyle image right filling the column to bleed. Minimum height 600px on `surface-soft` (#f2f2f2). CTA uses `button-primary`. Headline weight 300 is a deliberate low-contrast choice — the image carries the visual energy. Section padding `spacing.section` top and bottom.

### Badges

**`sale-badge`** — Flat zero-radius chip in `sale` (#c50000) with white text in `label-upper`. Sits in the top-left corner of product card images and on PDP near the price. **`sale-surface-badge`** uses the same label-upper spec but reverses to `sale-surface` (#ffeae8) fill and `sale` text — used in promotional banners and announcement strips where the solid red would compete. **`eco-badge`** uses `eco-surface` (#e5fff8) fill with `eco` (#007f5f) text; appears on products flagged for recycled metals or ethical sourcing, and in the footer sustainability section.

### Product Gallery

**`product-gallery`** — Main image at 1:1 aspect ratio on `surface-card` background, zero radius. Thumbnail strip below or to the left (desktop) at 72px squares with 1px `hairline` border; active thumbnail gains 1px `primary` border. No lightbox-style zoom signal — assumes standard Shopify zoom-on-hover behavior.

### Cart Drawer

**`cart-drawer`** — 400px right-side panel sliding over a scrim (`rgba(9,8,8,0.4)`), left-bordered 1px `hairline`. Title "Your Cart" in `title-md`. Each line item shows thumbnail, product name in `body-sm`, variant in `caption` muted, and price in `price-sm`. Quantity selector (`quantity-selector`) is inline. Subtotal row in `title-sm` weight 500 separates visually from the item list. Single `button-primary` full-width CTA: "Checkout."

### Footer

**`footer`** — Full-width on near-black `ink` (#090808). Column headings in `label-upper` weight 700 at `brand-mauve` (#8c7e7e) — the one place the mauve appears as active typography rather than surface color. Body links in `body-sm` at `brand-blush` (#d8d1d1), transitioning to `on-primary` on hover. Four columns: Shop, About, Help, Stay Connected. Social icon row in `brand-mauve`. Eco/ethics statement appears as a small `caption` block above the copyright line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo + cart icon; product grid switches to 2-up 3:4 cards; hero becomes stacked (image top, copy below); cart drawer full-width 100vw; announcement bar stays persistent |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + condensed links + icons; hero maintains two-column split at reduced image proportion; footer collapses to 2-column |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar with all links visible; hero at full 50/50 split; cart drawer at fixed 400px |
| Wide | > 1440px | Max-width container centered (1440px); product grid stays at 4-up; hero image column gains extra bleed; footer content centered with wider gutter |

### Touch Targets

- All interactive elements minimum 44×44px on mobile; quantity selector expands to 48px height
- Swatch buttons scale from 24px desktop to 32px touch to meet minimum tap area
- Nav icons (search, wishlist, cart) padded to 44px tap zones regardless of icon size
- Cart drawer close button minimum 44×44px in top-right corner

### Collapsing Strategy

- Navigation: hamburger menu at < 744px; full horizontal nav at ≥ 744px
- Hero: stacks vertically on mobile (image above fold, copy + CTA below); side-by-side at ≥ 744px
- Product grid: 2-up mobile → 3-up tablet → 4-up desktop
- Footer: 1-column mobile → 2-column tablet → 4-column desktop
- Announcement bar: single line centered on all breakpoints; text truncates with ellipsis if needed below 375px
- Product gallery thumbnails: horizontal scroll strip on mobile; vertical side rail on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed exact logo typeface weight or size from extraction — `display-sm` Raleway 400 is an inference from the single-family system
- No confirmed border-radius values from live CSS; `rounded.none` assumed from brand posture but Shopify theme defaults could introduce xs/sm radii on some elements
- No confirmed base canvas color — site may use pure #ffffff rather than the extracted #f5f5f5; both appear in extracted palette
- No motion/animation timing tokens extracted (transition durations, easing curves)
- No confirmed font-size scale from CSS — all sizes inferred from category conventions and single-family Raleway deployment
- Mega-menu or flyout nav structure not confirmed from extraction
- No confirmed grid column count or gutter widths from CSS
- Wishlist and account icon styling not extracted
- No confirmed spacing between announcement bar and nav; 0px gap vs 1px separator unknown
