---
version: alpha
name: "iDesign"
source_url: "https://idesignlive.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Clear acrylic bins and white wire shelving define iDesign's physical catalog, and that same logic — reveal what's inside, remove the unnecessary — extends to their digital surfaces. The site runs on a bright white canvas with a confident corporate blue (estimated ~#1660D8) anchoring all primary actions, producing a palette that reads closer to a professional storage-systems specifier than a lifestyle home décor brand. Navigation is categorical and functional: drawers, shelving, bath, kitchen — the product taxonomy mirrors the grid you'd actually build in a closet. Type defaults to clean, neutral sans-serif stacks with modest weights, letting product photography carry visual weight rather than display type. Components lean into utility: category tile grids, filter-heavy product listings, and cart-forward CTAs with none of the editorial looseness common in adjacent home brands. Rounded corners are conservative — `{rounded.sm}` on cards and buttons keeps the brand efficient without reading cold. The organization proposition relies on visible density: showing many products at once in tight rows signals depth of assortment, a cue that this is a complete system rather than a curated edit. Badges and category labels carry uppercase weight to help shoppers navigate product type — tension mount, suction, mesh, wire — rather than lifestyle aspiration. On mobile, the grid collapses to a single column with a sticky add-to-cart bar, keeping purchasing friction low for someone already standing in their pantry measuring shelf gaps. Promotional pricing speaks through a sharp `{colors.badge-promo}` orange-red, the one moment of heat against an otherwise cool-neutral field. The brand communicates in the language of the label maker rather than the mood board: every UI element is a container waiting to be filled.

colors:
  primary: "#1660D8"
  primary-active: "#0F4AAD"
  primary-disabled: "#A8C4EF"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6B6B6B"
  hairline: "#D8D8D8"
  hairline-soft: "#EDEDED"
  canvas: "#FFFFFF"
  surface-soft: "#F5F6F8"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  accent-teal: "#00A89D"
  badge-promo: "#E8320A"
  badge-sale-text: "#FFFFFF"
  star-rating: "#F5A623"
  success: "#2E8B57"
  error: "#D0021B"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  category-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px

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
    height: 48px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm}"
    imageAspectRatio: 1/1
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-grid:
    columns: 4
    gap: "{spacing.base}"
    backgroundColor: "{colors.canvas}"
  product-collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    imageOverlay: "rgba(0,0,0,0.18)"
    labelTypography: "{typography.category-label}"
    textPosition: bottom-center
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  badge-promo:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaStyle: button-primary
    layout: split-image-right
    padding: "{spacing.xxl} {spacing.xl}"
  sticky-atc-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    height: 72px
    priceTypography: "{typography.price-display}"
    boxShadow: "0 -2px 8px rgba(0,0,0,0.08)"
  rating-stars:
    fillColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    buttonWidth: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The main conversion surface in `{colors.primary}` blue with white text at `{typography.button-md}`, 48px tall with `{rounded.sm}` corners. Hover darkens to `{colors.primary-active}`; disabled washes out to `{colors.primary-disabled}` and blocks pointer interaction. Appears on search submission, navigation CTAs, and newsletter enrollment.

**`button-secondary`** — White background with a 1.5px `{colors.primary}` border and matching text, matching the primary button's 48px height. Signals an alternative action — Save to List, Compare, View Details — without competing with the add-to-cart CTA. Active state shifts the background to `{colors.surface-soft}` for visible depression.

**`button-add-to-cart`** — Full-width variant of the primary button at 52px, with wider padding for prominence on product detail pages and inside the `sticky-atc-bar`. The taller height and width-100% rule make it unmistakable as the page's primary conversion target.

### Navigation

**`nav-utility-bar`** — A 36px strip above the main header in `{colors.surface-soft}` carrying shipping threshold messaging, promotions, and account shortcuts in `{typography.caption}` `{colors.muted}`. Hidden on mobile to recover vertical space; its messaging is redistributed into banner slots below.

**`nav-bar`** — 64px white header with the iDesign wordmark at 36px height, primary category links in `{typography.nav-link}`, and icon buttons for search, account, and cart. A `{colors.hairline}` bottom border separates it cleanly from page content without adding visual mass. On desktop, category links trigger mega-menu overlays; on mobile they collapse to a hamburger drawer with accordion expansion per category.

**`breadcrumb`** — Lightweight wayfinding in `{typography.caption}` with hairline separator characters. Ancestor nodes render in `{colors.muted}`; the active (current page) node in `{colors.ink}`. No underline until hover, keeping it subordinate to product content above.

### Product Discovery

**`product-card`** — Square 1:1 image above a compact metadata block: product name in `{typography.body-sm}`, price in `{typography.price-sm}`, and an optional `badge-promo` or `badge-new` overlay pinned to the image top-left. Border is `{colors.hairline-soft}` at rest; hover adds `{colors.hairline}` border and a soft drop shadow, lifting the card without animation. Cards carry no secondary CTA — the click target is the full card.

**`product-grid`** — Four-column grid at desktop with `{spacing.base}` gutter. Dense column count is intentional: organizational products need side-by-side dimension and capacity comparison, which a three-column layout sacrifices. Collapses to two columns on tablet and one on mobile.

**`product-collection-header`** — Sits above the product grid: collection name in `{typography.display-md}`, optional descriptor in `{typography.body-md}` `{colors.muted}`, separated from the grid by a `{colors.hairline}` bottom border. Result count and sort selector share the same baseline at desktop.

**`category-tile`** — Square or rectangular image tiles with a dark rgba overlay and centered title in `{typography.title-md}`. Used on the homepage to route shoppers into Closet, Kitchen, Bath, and Office verticals. The `{typography.category-label}` uppercase label above the title names the product system type (e.g. "DRAWER ORGANIZERS"). Minimal copy keeps the tile navigational rather than promotional.

**`filter-chip`** — `{rounded.full}` pill buttons for product type, mounting method, material, and size filters. Inactive state: white fill, `{colors.hairline}` border. Active state: solid `{colors.primary}` fill with white text. Multiple chips may be active simultaneously for AND-style filtering. On mobile they sit in a horizontal scroll rail rather than wrapping to preserve density.

**`search-bar`** — 44px input in `{colors.surface-soft}` with a leading search icon in `{colors.muted}`, `{rounded.sm}` corners consistent with form fields. Deployed inside the nav search overlay. Expands to full-width on mobile.

### Badges

**`badge-promo`** — `{colors.badge-promo}` orange-red rectangle with `{rounded.xs}` corners and white text in `{typography.badge}` uppercase. The one warm note in an otherwise cool-neutral palette; its heat signals urgency without requiring copy to say "sale." Pinned to the image corner on product cards.

**`badge-new`** — Identical geometry to `badge-promo` but in `{colors.primary}` blue. Used for catalog additions and recently launched SKUs. Differentiating it from the promo badge by hue alone lets shoppers parse "new vs. discounted" at grid scan speed.

### Product Detail Page

**`sticky-atc-bar`** — Appears at viewport bottom once the above-fold add-to-cart button scrolls out of view. White background, 72px tall, `0 -2px 8px` upward shadow to separate from content scroll. Contains a truncated product name, price in `{typography.price-display}`, and the full-width `button-add-to-cart`. Stays visible throughout the PDP scroll so purchase intent is never blocked by content depth.

**`quantity-selector`** — Decrement/increment control flanking a number in `{typography.title-md}`, boxed in a `{colors.hairline}` border at 40px height with `{rounded.xs}`. Icon buttons equal in width to the number field keep the control symmetrical and touch-friendly.

**`rating-stars`** — Five-star row in `{colors.star-rating}` amber with empty stars in `{colors.hairline}`. Review count sits inline in `{typography.caption}` `{colors.muted}`. Appears in compressed form on product cards and in expanded form with a linked count on PDP.

### Footer

**`footer`** — Dark `{colors.ink}` footer on a four-column link grid (Rooms, Products, Company, Support) in `{typography.body-sm}`. Column headings use `{typography.title-sm}` in `{colors.canvas}`. The dark background gives the page a definitive bottom edge and allows legal and payment mark content to recede at reduced opacity. Social icons render as simple outlines in `{colors.hairline}`.

### Heroes and Banners

**`hero-banner`** — Split layout at desktop with headline and CTA on the left, product or room photography on the right, on a `{colors.surface-soft}` ground. Headline at `{typography.display-xl}`, body copy at `{typography.body-md}`. One primary `button-primary` CTA and an optional text link secondary. On mobile the layout stacks image above copy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; utility bar hidden; nav collapses to hamburger + logo + cart icon; filters open in a bottom-sheet modal; sticky ATC bar active on PDP; hero stacks image above copy |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline with overflow menu; hero shifts to stacked layout; utility bar visible |
| Desktop | 1128–1440px | Four-column product grid; full nav with hover mega-menu overlays; filter sidebar inline left of grid; utility bar and full footer visible |
| Wide | > 1440px | Max-width container (~1440px) centered; hero image can bleed to viewport edges with constrained text column |

### Touch Targets

- All interactive controls minimum 44×44px on mobile: buttons, filter chips, nav icons, quantity selectors
- Filter chips rendered in a horizontal scroll rail on mobile rather than wrapping, to preserve access to all options without vertical overflow
- Product cards in 2-column grid on small phones — single column only appears below ~375px — preserving comparative context for dimensional products

### Collapsing Strategy

- Mega-menu navigation collapses to a hamburger drawer with per-category accordion expansion on mobile and tablet
- Utility bar (shipping thresholds, promotions) hidden below 744px; messaging absorbed into hero or announcement banner slots
- Product filters move from inline left sidebar to a bottom-sheet modal triggered by a persistent "Filter & Sort" pill above the grid on mobile
- Footer four-column link grid collapses to accordion-style stacked columns on mobile; legal row and payment marks remain visible at bottom

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: idesignlive.com returned zero hex values from live extraction — likely JS-rendered design tokens or anti-bot protection on the CDN. All palette values are estimated from brand observation and must be verified against the live site or source Figma files before production use.
- **Primary blue unconfirmed**: `#1660D8` is an estimate; the actual brand blue may be lighter, darker, or carry a different hue angle entirely.
- **No fonts extracted**: `'Helvetica Neue', Arial, sans-serif` is a conservative system-font fallback. The actual typeface is unknown and may be a licensed grotesque loaded via JavaScript or a hosted CSS variable.
- **No meta theme-color**: The site did not expose a `theme-color` meta tag, which would otherwise anchor the primary hue with confidence.
- **Accent teal unconfirmed**: `{colors.accent-teal}` (#00A89D) is speculative; verify whether iDesign uses a secondary hue in practice or if this token should be removed.
- **Promotional palette**: Sale badge color `{colors.badge-promo}` (#E8320A) is a common e-commerce convention, not extracted from the live site.
- **Icon library**: Nav and UI icon style — outlined vs. filled, stroke weight, corner rounding — could not be determined from extraction and may differ significantly from the generic fallback.
- **Spacing scale**: Grid gutter and section padding values are based on common DTC conventions; actual values may be tighter or looser than specified here.
