---
version: alpha
name: "Frigidaire"
source_url: "https://www.frigidaire.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep cobalt blue — the same shade stamped on refrigerator nameplates since mid-century — anchors every interactive surface on a site built to sell large appliances the way an automotive configurator sells cars. The primary (#003da5) saturates CTAs, sticky "Add to Cart" bars, and comparison-tool headers while the rest of the page breathes on a near-white canvas (#ffffff) broken only by cool gray surface bands (#f4f4f4) that section off spec tables and lifestyle photography. Typography leans on a geometric sans-serif stack close to Helvetica Neue / Arial, set at restrained weights — product titles hit 600 but rarely 700, body copy stays at 400 — trusting product imagery and generous padding (`{spacing.section}`) to carry visual weight. Cards use a subtle `{rounded.sm}` radius (8px), buttons land at `{rounded.xs}` (4px), and the overall language is squared-off and engineered: no pill shapes, no playful curves. A persistent comparison tray slides up from the bottom of the viewport holding up to four product thumbnails, reinforcing the research-heavy purchase journey. Product cards pack a "Quick View" overlay, an energy-star badge, and a price block with strikethrough sale logic — dense information architecture kept legible by disciplined use of `{colors.muted}` (#6b6b6b) for secondary text and `{colors.hairline}` (#d9d9d9) for dividers. The palette stays monochromatic outside of the primary blue: no accent hue competes for attention, letting that single cobalt carry 100% of the brand signal against an otherwise neutral stage.

colors:
  primary: "#003da5"
  primary-active: "#002d7a"
  primary-disabled: "#99b3d9"
  accent-promo: "#c8102e"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#2e7d32"
  warning: "#f9a825"
  error: "#c8102e"
  star-rating: "#f9a825"
  energy-badge: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  button-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  price-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-strike:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.8px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 2px solid {colors.primary}
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.hairline}
    hoverShadow: 0 2px 8px rgba(0,0,0,0.06)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1/1
    objectFit: contain
    padding: "{spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-md}"
    textColor: "{colors.accent-promo}"
  product-card-original-price:
    typography: "{typography.price-strike}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  comparison-tray:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    height: 80px
    position: fixed
    bottom: 0
    boxShadow: 0 -4px 16px rgba(0,0,0,0.15)
  comparison-tray-thumbnail:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 56px
    width: 56px
    objectFit: contain
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-banner-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-banner-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
  promo-badge:
    backgroundColor: "{colors.accent-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  energy-badge:
    backgroundColor: "{colors.energy-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
    iconSize: 16px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  sticky-buy-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.lg}"
    height: 72px
    borderTop: 1px solid {colors.hairline}
    boxShadow: 0 -2px 8px rgba(0,0,0,0.06)
    position: sticky
    top: 0
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-dark}"
    opacity: 0.8
    hoverOpacity: 1
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 44px
    height: 48px
    iconColor: "{colors.muted}"

---

## Components

### Buttons

**`button-primary`** — Solid cobalt blue (#003da5) rectangle with 4px radius and white text set in 16px weight-600. Hover darkens to `primary-active` (#002d7a) with no scale transform. Disabled state drops to `primary-disabled` (#99b3d9) with cursor-not-allowed. Focus ring is a 2px offset outline in `primary` at 50% opacity.

**`button-secondary`** — White fill with a 2px cobalt border and blue text. Hover fills `surface-soft` and darkens the border to `primary-active`. Maintains the same 48px height and 4px radius as primary, ensuring alignment when buttons sit side by side in product detail actions.

**`button-tertiary`** — Text-only link-style button with underline, no background or border. Used for "View Details", "See All Features" inline actions. Hover removes underline and shifts color to `primary-active`.

**`button-add-to-cart`** — Full-width variant of primary at 52px height, used in the product detail page and sticky buy bar. Identical styling to `button-primary` but wider padding and full container width to emphasize purchase intent.

### Navigation

**`nav-bar`** — 64px-tall white bar with a single-pixel bottom border. Logo sits left, category links center-aligned in 14px weight-500, utility icons (search, account, cart) right-aligned. On hover, category links gain a 2px bottom border in `primary` that animates in from center.

**`nav-bar-mega-menu`** — Drops below the nav on category hover, full viewport width with a subtle box-shadow. Contains a three-column grid: product subcategories left, featured product card center, promotional banner right. Background is white with generous `spacing.lg` internal padding.

### Product Cards

**`product-card`** — Vertical card with contained product image on a light gray background (`surface-soft`), followed by title, star rating, and price stack. Border is `hairline-soft` at rest, strengthening to `hairline` on hover with a faint lift shadow. The 8px radius keeps it geometric. A "Quick View" overlay appears on hover as a semi-transparent dark scrim with a centered white button.

**`product-card-image`** — Square aspect ratio container with `object-fit: contain` and internal padding so the appliance floats with breathing room. Background is `surface-soft` to differentiate from the white card body.

**`product-card-price`** — Bold 20px price in ink. When on sale, the current price renders in `accent-promo` red alongside the original price struck through in `muted`.

### Comparison Tray

**`comparison-tray`** — Fixed to viewport bottom, dark background (`surface-dark`) holding up to four product thumbnails in white rounded containers. A "Compare Now" primary button sits at the right edge. Slides up with a spring animation when the first product is added, collapses when emptied. Shadow projects upward to separate from page content.

### Hero Banner

**`hero-banner`** — Full-width section with lifestyle photography background (laundry room scenes, kitchen vignettes) and overlaid text block. Headline uses `display-xl` at 36px bold, subhead in `body-lg`. A primary CTA button sits below with `spacing.lg` gap. Minimum height 480px ensures impact even on wide viewports.

### Badges

**`promo-badge`** — Small red (#c8102e) rectangle with white uppercase text at 11px, used for "SALE", "NEW", "LIMITED TIME" callouts. Positioned absolutely at the top-left corner of product cards with 4px radius.

**`energy-badge`** — Green (#2e7d32) badge variant for Energy Star certification indicators. Same sizing and radius as promo badges but with a leaf icon preceding the label text.

### Specification Table

**`spec-table`** — Alternating-row table for product specifications (capacity, dimensions, energy rating). Header cells use `spec-label` (14px weight-600), value cells use `spec-value` (14px weight-400). Rows separated by 1px `hairline-soft` borders. No zebra striping — relies on vertical rhythm and padding alone.

### Filter & Search

**`filter-chip`** — Small rectangular chip (4px radius) with 1px border for faceted navigation (brand, capacity, color). Active state fills with `primary` blue and white text. Chips sit in a horizontally scrollable row on mobile.

**`search-bar`** — Light gray input with a magnifying glass icon inset left. 48px height, 4px radius, placeholder text in `muted`. On focus, border transitions to 2px `primary` blue.

### Sticky Buy Bar

**`sticky-buy-bar`** — Appears on product detail pages once the main "Add to Cart" button scrolls out of view. White background, top border, upward shadow. Contains product name (truncated), price, and a condensed primary button. 72px height keeps it compact.

### Footer

**`footer`** — Dark background (`surface-dark` / #1a1a1a) with white text organized in a four-column grid: product categories, support links, about links, and a newsletter signup input. Headings use `title-sm` weight-600, links at 80% opacity rising to full on hover. Bottom row contains legal links and copyright in `caption` size.

### Breadcrumb

**`breadcrumb`** — Muted-color path trail using `caption` typography with chevron separators. Sits below the nav bar with `spacing.md` vertical padding. Final crumb is `ink` color and non-linked.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + slide-out drawer. Product grid goes single-column. Comparison tray shows 2 thumbnails max with horizontal scroll. Hero banner stacks text above image. Sticky buy bar always visible. Filter chips scroll horizontally. |
| Tablet | 744–1128px | Product grid shifts to 2-column. Nav keeps hamburger but mega-menu becomes a full-screen overlay. Hero banner maintains side-by-side layout at reduced image width. Comparison tray shows 3 items. |
| Desktop | 1128–1440px | Full nav with category links visible. Product grid at 3–4 columns. Mega-menu drops down as flyout panel. Comparison tray shows all 4 slots. Spec tables render full-width with comfortable column spacing. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Additional whitespace in hero sections. Product grid remains 4 columns with larger card images. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap target on mobile and tablet
- Filter chips expand vertical padding to 12px on touch devices
- Close/dismiss buttons on overlays are 48×48px with generous hit area
- Comparison tray thumbnails are 56px but tap target extends to 64px with invisible padding

### Collapsing Strategy

- Navigation categories collapse into a hamburger drawer with accordion sub-menus
- Product specification tables collapse into expandable accordion sections on mobile
- Multi-column footer stacks into single-column with collapsible category groups
- Comparison tray reduces visible items and adds horizontal scroll with pagination dots
- Hero banner text overlay shifts from absolute positioning to stacked block flow
- Filter sidebar becomes a bottom-sheet modal triggered by a "Filter" button

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors could be extracted from the live site — likely loaded via JavaScript bundles or CSS-in-JS at runtime. The primary blue (#003da5) is based on widely-documented Frigidaire brand guidelines (visible on packaging, print materials, and the logo itself), but exact digital token values may differ.
- No font-family stacks were extracted. The specified Helvetica Neue stack is inferred from the brand's typical web presence; the actual site may use a licensed or custom typeface loaded via JS.
- Exact border-radius values, spacing scale, and animation timing could not be confirmed from static extraction.
- Promotional red (#c8102e) is inferred from common Electrolux/Frigidaire sale treatments; actual implementation may vary seasonally.
- The comparison tray interaction pattern is based on observed behavior in appliance retail sites in this family; exact dimensions and transitions are approximate.
- No meta theme-color or manifest data available to confirm mobile browser chrome color.
