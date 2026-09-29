---
version: alpha
name: "Zebra Pen"
source_url: "https://www.zebrapen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The pen barrel itself is the color system — Zebra's product lines span highlighters in seventeen shades, gel inks across forty, and marker tips from .3mm to brush, so the UI architecture on zebrapen.com is engineered to display color as inventory rather than decoration. A thin strip of product ink color runs flush across the top edge of every card, rendered with {rounded.none} at the top corners and {rounded.sm} at the bottom, isolating each hue against a neutral card field without competing with the product photo. The brand's primary voltage is #ed1846, a red pulled slightly toward magenta that stamps the header wordmark accent, sale badges, and mobile browser chrome via meta theme-color before any content loads. It reads more energetic than red-orange and less corporate than pure red — appropriate for writing instruments positioned between office commodity and creative tool.

  Typography is more layered than a standard Shopify storefront: bely-display anchors editorial headlines with its high-contrast serif stroke; mr-eaves-modern carries body prose in a humanist sans; Jost handles buttons, badges, and UI labels in tracked all-caps; sofia-pro runs navigation links at weight 600. The four-family stack signals a brand with distinct product lines — fine-point technical pens, broad-tip markers, and specialty instruments — each needing a slightly different editorial register within the same grid. The neutral spine is decisive: #222222 ink against #f6f6f8 surface-soft, with mid-grays #878787 and #b1b1b1 holding borders and secondary labels. No warm greige, no softened cream — the palette reads as a professional desk, not a lifestyle shelf.

  Accent cyan (#56cfe1) and deep teal (#007e91) form a secondary chromatic layer for filter chips, informational badges, and hover confirmation, separating functional interaction states from the primary red purchase signal. Orange (#e67e22) surfaces in promotional strips as a contrast voltage that registers urgency without competing with the primary. Rounded values stay modest — {rounded.xs} on buttons, {rounded.sm} on cards — the geometry is precise rather than playful, mirroring the instruments being sold.

colors:
  primary: "#ed1846"
  primary-active: "#c0102e"
  primary-disabled: "#f5a0b2"
  ink: "#222222"
  body: "#444444"
  muted: "#878787"
  hairline: "#b1b1b1"
  hairline-soft: "#d8d8d8"
  canvas: "#ffffff"
  surface-soft: "#f6f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#56cfe1"
  accent-teal: "#007e91"
  accent-blue: "#44aaee"
  accent-promo: "#e67e22"
  error: "#ff0001"

typography:
  display-xl:
    fontFamily: "'bely-display', 'bely', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'bely-display', 'bely', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'bely-display', 'bely', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'sofia-pro', 'Jost', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'sofia-pro', 'Jost', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'mr-eaves-modern', 'mr-eaves-sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'mr-eaves-modern', 'mr-eaves-sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'sofia-pro', 'Jost', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  category-label:
    fontFamily: "'Jost', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 1.2px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAccentColor: "{colors.primary}"
    promoBarBackgroundColor: "{colors.primary}"
    promoBarTextColor: "{colors.on-primary}"
    promoBarHeight: 40px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
    headingTypography: "{typography.category-label}"
    headingColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    strikePriceTypography: "{typography.price-sm}"
    strikePriceColor: "{colors.muted}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  product-card-color-strip:
    height: 6px
    roundedTopLeft: "{rounded.sm}"
    roundedTopRight: "{rounded.sm}"
    roundedBottomLeft: "{rounded.none}"
    roundedBottomRight: "{rounded.none}"
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge-featured:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.hairline}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.accent-promo}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    height: 40px
    padding: "0 {spacing.base}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: "0 {spacing.base}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  color-swatch-lg:
    size: 36px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    gap: "{spacing.sm}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  ink-type-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    borderLeft: "3px solid {colors.accent-cyan}"
    padding: "4px 10px"
  product-spec-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    accentBarColor: "{colors.primary}"
    accentBarHeight: 3px
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA uses #ed1846 fill with white type set in Jost 700 tracked uppercase at 14px, giving the button a precision-instrument quality rather than a soft consumer feel. Corner radius is {rounded.xs} (4px), slightly sharper than most e-commerce peers. Hover darkens to #c0102e; disabled bleaches to #f5a0b2.

**`button-secondary`** — Canvas background with a 1px solid #222222 border, matching type in Jost uppercase. On hover the background shifts to {colors.surface-soft}, communicating state without softening the visual weight. Used primarily for "Add to Wishlist" and secondary filter actions.

**`button-ghost`** — Transparent fill with #ed1846 type, no border. Used for inline text-link CTAs like "View All" at the end of product-grid rows. Typography drops to `button-sm` (12px tracked uppercase) to visually recede behind the primary action.

### Navigation

**`nav-bar`** — Sticky at 64px height, white background with a 1px {colors.hairline} border-bottom. The Zebra wordmark uses the #ed1846 accent. Left-heavy category links run in sofia-pro 600 at 14px. A top promo bar (40px, #ed1846 fill, white Jost body-sm type) sits above the nav and collapses on scroll on mobile. Mega-menu panels open with a 3px {colors.primary} top border to ground the expanded panel within the nav system.

### Product Cards

**`product-card`** — White card with {rounded.sm} corners and a 1px {colors.hairline-soft} border. The signature feature is `product-card-color-strip`: a 6px tall block flush to the top edge, rounded only on top-left and top-right, carrying the product's ink or barrel color. This device lets the product color read instantly without requiring the user to parse SKU metadata. Title in sofia-pro 600 at 15px; price in Jost 700 at 20px; secondary spec text in Jost 400 at 12px with {colors.muted}. Cards lift with a soft box-shadow on hover.

**`product-badge-sale`** — #ed1846 fill, Jost 700 10px tracked uppercase, {rounded.xs}. Positioned top-left over the product image. **`product-badge-new`** — Same geometry, {colors.accent-cyan} fill, white type. **`product-badge-featured`** — {colors.accent-teal} fill, white type. Three badge tiers that escalate from informational (cyan) to preferred (teal) to commercial (red).

### Hero

**`hero`** — Full-bleed section on {colors.surface-soft} with bely-display headlines at 48px. Subhead in mr-eaves-modern 16px at {colors.body}. A primary CTA button sits below. Dark-variant (`hero-dark`) uses {colors.ink} fill with canvas headline type for product-launch moments. Minimum height 480px on desktop.

### Color Swatches

**`color-swatch`** / **`color-swatch-lg`** — Circular swatches (24px and 36px diameter) with a transparent default border that activates to 2px {colors.ink} on selection. The inner fill is the product's actual ink or barrel hex, passed dynamically. Gap between swatches is {spacing.xs} / {spacing.sm} respectively. This pattern appears on PDPs and inside product cards on hover.

### Filters and Pills

**`category-pill`** — {rounded.full} pill with {colors.surface-soft} fill, 1px hairline border, Jost category-label type (11px uppercase, 1.2px tracking). Active state swaps to {colors.primary} fill with white type. Used in the top-of-grid filter row for product-type filtering (Gel, Ballpoint, Highlighter, etc.).

**`filter-chip`** — More compact than category-pill; {rounded.sm} corners, {colors.surface-soft} fill, Jost caption at 12px. Active inverts to {colors.ink} fill with canvas type. Used for attribute filters: tip size, color family, ink type.

### Ink Type Label

**`ink-type-label`** — A left-bordered tag ({colors.accent-cyan} 3px left border) on {colors.surface-soft}, Jost caption at 12px in {colors.muted}. Used inline within product detail rows to categorize ink chemistry (water-based, pigment, oil-based). The cyan border references the accent-cyan secondary palette without using it as a fill, keeping legibility against the light background.

### Product Spec Row

**`product-spec-row`** — A two-column key-value row separated by a {colors.hairline-soft} bottom border. Label in Jost caption at 12px, muted; value in mr-eaves-modern body-sm at 14px, ink. Used in the PDP specifications accordion for tip size, ink color count, refillable status, and line width.

### Footer

**`footer`** — {colors.ink} fill with a 3px {colors.primary} accent bar at the very top edge. Column headings in sofia-pro 600 at 15px, canvas color. Link text in mr-eaves-modern 14px, {colors.hairline} at rest, canvas on hover. Social icon row uses circular icon-buttons at 36px with hairline borders.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; promo bar stays visible at 36px; hero min-height drops to 320px; color swatches use `color-swatch` (24px) only; filter row becomes horizontally scrollable pills |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline, mega-menu still available; hero text scales to display-md (32px); category-pill filter row wraps to two rows if needed |
| Desktop | 1128–1440px | Three- or four-column product grid; full sticky nav with mega-menus; hero at display-xl (48px) with side-by-side text and image layout; product spec rows appear in-page without accordion collapse |
| Wide | > 1440px | Grid max-width capped ~1440px, centered; hero padding expands but headline stays at 48px; side margins fill with canvas background |

### Touch Targets

- All interactive buttons minimum 44px height
- Color swatches on mobile expand to `color-swatch-lg` (36px) for reliable tap targeting
- Filter chips minimum 36px height on mobile, horizontally scrollable container with 16px side padding
- Nav hamburger tap target minimum 44×44px
- Footer links spaced minimum 36px vertical rhythm on mobile

### Collapsing Strategy

- Product specification table collapses to an accordion on mobile and tablet; expanded state uses full-width `product-spec-row` rows
- Mega-menu becomes a full-screen slide-in drawer on mobile with back-navigation breadcrumb
- Color swatch row truncates at 8 swatches on product card mobile view with "+N more" caption link
- Promo banner collapses from 40px to 36px on mobile; text shortens to fit single line
- Hero image moves below the text block on mobile rather than side-by-side

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav-bar height on mobile not confirmed — 64px desktop assumed, mobile may be 56px
- Font loading hierarchy unclear: whether bely-display or sofia-pro is self-hosted vs Adobe Fonts CDN affects FOUT behavior; fallback serif/sans ordering is an assumption
- Precise button border-radius not pixel-confirmed from live DOM; {rounded.xs} (4px) inferred from visual extraction
- Color swatch selected-state treatment (ring, checkmark overlay, or border offset) not confirmed — 2px ink border assumed
- Exact grid column counts per breakpoint not confirmed from DOM inspection; 3-up vs 4-up on desktop depends on sidebar filter presence
- gopher, metallophile-sp8, and raleway appear in the font stack but their specific typographic roles (section labels, specialized product lines, promotional headers) could not be mapped from extraction alone
- Dark hero background color — assumed {colors.ink} (#222222) but a deep navy or product-specific color may be used instead
- Pricing display for multi-variant SKUs (e.g., sets vs single units) and whether a strikethrough sale pattern is implemented were not confirmed
- Exact footer column count and newsletter signup treatment not confirmed from extraction
