---
version: alpha
name: "Hamilton Beach"
source_url: "https://www.hamiltonbeach.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hamilton Beach's #c82027 sits closer to tomato-paste crimson than fire-engine red — a food-adjacent color that has anchored every primary CTA, promotional badge, and header element for decades without apology. The site runs entirely on Arial and Helvetica (system fonts), a choice that directs design energy toward product photography and specification density rather than typeface investment; body text flows at 16px with weight 400, and heading scales rely on heavier 600–700 weights to create clear hierarchy on category-dense grids. The secondary surface is the extracted #eeeeee — a light warm-gray that appears beneath spec-comparison modules and section dividers, separating product-canvas zones from supporting content without introducing an additional hue. Rounded values stay conservative throughout: small radii on buttons ({rounded.xs}–{rounded.sm}) and product cards signal the practical, value-oriented home-appliance buyer rather than the lifestyle-premium shopper who expects pillowy, high-radius components. Font Awesome supplies iconography in place of a custom set, reinforcing the utility framing that runs through every navigation tier. Promotional labels — SALE, NEW, BEST SELLER — render in the primary crimson on white, yielding high-contrast callout badges that hold legibility at the small sizes demanded by dense product grids. Price figures earn deliberate scale and weight — larger than surrounding body text — so the value proposition registers before the product description. Hero banners feature a single appliance against a lifestyle background, with a solid crimson CTA anchored in the left copy block; no gradient, no glassmorphism, no textured overlay. The overall system is built around catalog trust: the red is an action signal and a brand marker, not a lifestyle aspiration, and every spacing and type decision supports efficient browsing rather than editorial dwell time.

colors:
  primary: "#c82027"
  primary-active: "#a01920"
  primary-disabled: "#e8a0a3"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-section: "#f5f5f5"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  badge-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  product-name:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    iconColor: "{colors.muted}"
    submitBackground: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.md}"
    productNameTypography: "{typography.product-name}"
    productNameColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    ratingColor: "{colors.primary}"
    ratingTypography: "{typography.caption}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaRounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    minHeight: 420px
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.title-md}"
    subheadColor: "{colors.body}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
    ctaTypography: "{typography.button-md}"
    imagePosition: right
    padding: "{spacing.xxl} {spacing.xl}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  sale-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    hoverBorder: "2px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  product-spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    alternateRowBackground: "{colors.surface-section}"
  rating-stars:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    size: 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#cccccc"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — Solid crimson (#c82027) with white uppercase text at 15px/700 weight and a conservative {rounded.xs} (4px) radius. Padding is 12px 24px, height 44px. On hover the background shifts to {colors.primary-active} (#a01920); the disabled state uses {colors.primary-disabled}, a pale rose that retains brand origin while conveying unavailability. Deployed on all primary actions: "Add to Cart", "Shop Now", "Find a Retailer".

**`button-secondary`** — White fill with a 2px crimson border and crimson uppercase label, matching {typography.button-md} style identically. Appears alongside button-primary in product-detail CTA pairs — "Shop Now" next to "Compare" — offering an alternative path without competing for visual hierarchy.

**`button-text-link`** — Transparent background with crimson text at {typography.body-sm} and underline decoration. Used inline in editorial copy, spec tables, and support flows where a full button weight would overwhelm surrounding content.

### Search Bar

**`search-bar`** — A hairline-bordered input at 40px height and {rounded.xs} corners, with a flush crimson submit button on the right edge using {rounded.none} to merge cleanly with the input field. Placeholder text appears in {colors.muted}. On desktop it sits in the utility bar beside the logo; on mobile it expands to a full-width overlay. The crimson submit control maintains brand presence at every search interaction.

### Navigation

**`nav-bar`** — 56px white bar with a 1px {colors.hairline} bottom border. Logo anchors left at 36px height; account, search, and cart (Font Awesome) icons cluster right. A secondary row of product-family labels renders in {typography.nav-link}. Hovering any label opens **`nav-mega-menu`**: a full-width drop panel with a 3px {colors.primary} top border, columns organized by appliance subcategory in {typography.body-sm}, with padding at {spacing.lg} {spacing.xl}.

### Product Card

**`product-card`** — White card with 1px {colors.hairline} border and {rounded.xs} corners. A square product image fills the top in a 1:1 ratio; a {spacing.md} padding zone below carries: product name in {typography.product-name}, star rating dots in {colors.primary} at {typography.caption} scale, price in {typography.price-display} (20px/700) with sale prices highlighted in the same crimson, and a compact crimson "Add to Cart" button at the card foot using {typography.button-sm}. A flat {promo-badge} overlay anchors to the top-left corner for sale, new, or featured items.

### Hero Banner

**`hero-banner`** — Full-width section with {colors.surface-soft} (#eeeeee) background at 420px minimum height. Headline in {typography.display-xl} (36px/700) and subhead in {typography.title-md} (18px/600) anchor the left copy block; product photography fills the right side. The CTA is a solid crimson button with white uppercase text. No gradients, overlays, or drop shadows — product photography and the gray-to-white contrast carry all visual weight.

### Promotional Badge

**`promo-badge`** — Flat crimson rectangle with {rounded.none} and white uppercase {typography.badge-label} text at 11px/700. Padding is tight at 3px 8px. Labels: SALE, NEW, BEST SELLER. The hard square corner is a deliberate signal — this is a value callout, not a decorative accent — and distinguishes it visually from the soft pill badges used by lifestyle or beauty brands.

### Sale Banner

**`sale-banner`** — Full-width crimson bar in {typography.title-sm}, white text centered. Used for time-limited promotions such as "Free Shipping on Orders Over $35". Single line by default; wraps at 375px viewport width. The banner sits above the nav-bar, ensuring the promotional message is the first element a visitor reads.

### Category Tile

**`category-tile`** — {colors.surface-soft} tile with {rounded.sm} corners, category image above a {typography.title-sm} label. On hover, a 2px {colors.primary} border frames the tile. Used in the homepage category navigation grid (Blenders, Coffee Makers, Microwaves, Toaster Ovens); reduces from five columns at desktop to three at tablet to two at mobile.

### Product Spec Table

**`product-spec-table`** — Two-column table with a {colors.surface-soft} header row, alternating {colors.surface-section} and white body rows, and 1px {colors.hairline} cell borders throughout. Header cells in {typography.title-sm}; body cells in {typography.body-sm}. Used on product detail pages for wattage, capacity, cord length, dimensions, and warranty data. Scrolls horizontally on mobile rather than reflowing into a stacked layout.

### Rating Stars

**`rating-stars`** — Filled stars in {colors.primary}, empty stars in {colors.hairline}, rendered at 16px with review count in {typography.caption}. Appears on product cards and at the top of product detail pages. The crimson star color ties ratings visually to the primary action color, reinforcing the connection between positive reviews and the purchase CTA.

### Footer

**`footer`** — Dark {colors.ink} full-width footer with a 4px {colors.primary} top border that brackets the white site body. Column headings in {typography.title-sm} at {colors.canvas}; body copy and links at #cccccc; social icons via Font Awesome. Four to five columns cover Product Support, About Us, social links, and legal notices. The crimson top border is the only color accent against the dark ground, creating a clean visual bracket between site content and footer territory.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger, logo, and cart icon; hero stacks copy above image; mega-menu becomes full-screen slide-over drawer; search expands to full-width overlay |
| Tablet | 744–1128px | Two-column product grid; top-level category labels visible in nav bar, mega-menu opens on tap; hero maintains side-by-side at reduced padding |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with mega-menu on hover; hero at full 420px height; spec tables visible without horizontal scroll |
| Wide | > 1440px | Content max-width ~1400px centered with side gutters; four-column grid unchanged; hero image scales without cropping |

### Touch Targets

- All buttons minimum 44px height per component height spec
- Nav icon cluster padded to 44×44px tap area on mobile via surrounding padding
- Product card entire surface is the tap target on mobile, not only the CTA button
- Category tiles minimum 48px height in mobile drawer navigation
- Search submit button minimum 44px width on mobile
- Breadcrumb links minimum 44px height via vertical padding

### Collapsing Strategy

- Mega-menu becomes a full-screen slide-over drawer at < 744px, triggered by hamburger icon in nav-bar
- Three-tier navigation drills down sequentially on mobile: top category → subcategory → product list, each level replacing the previous panel
- Product spec tables scroll horizontally on mobile rather than reflowing into stacked rows
- Sale banner wraps to two lines below 375px viewport; single line above
- Category tile grid reduces from five columns at desktop to three at tablet to two at mobile
- Hero banner copy and image stack vertically on mobile with copy above, image below

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only 2 hex colors extracted (#c82027, #eeeeee); mid-range neutrals, hover tints, disabled states, and surface variants are derived from appliance-retail conventions, not live extraction
- No web font detected beyond system stacks (Arial, Helvetica); Hamilton Beach may load a licensed or proprietary web font via JavaScript that static extraction did not capture
- No meta theme-color present; mobile browser chrome bar color is unconfirmed
- Exact border-radius values on buttons and product cards are estimated at {rounded.xs} (4px) based on brand-category norms; not measured from live DOM
- Font Awesome version confirmed as 5 Brands / 5 Free, but icon selection and pixel sizing per component not measured
- No dark mode palette detected or extracted
- Promotional badge color differentiation (clearance vs. new arrival vs. best seller) not confirmed from live data; all assumed to use {colors.primary}
- Rating star half-fill and empty-state rendering not confirmed beyond color
