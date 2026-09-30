---
version: alpha
name: "Bosch"
source_url: "https://www.bosch-home.com/us"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Bosch logotype sits inside a perfect crimson circle — #EA0016, a red sharp enough to read as a warning signal against a white-on-white product page — and that geometry sets the tone for everything downstream. Engineering precision runs through the layout: columns align to a hard grid, product specs render in tabular rows with fine hairlines, and surface hierarchy moves in three steps (white card → soft gray section → near-black footer) with almost no decorative variation between. Bosch Sans, the brand's proprietary typeface confirmed loading on the live site, carries text at modest weight; body copy sits at 400/16px with open leading that lets specification-dense pages breathe. No display weight exceeds 700, and letter-spacing stays near zero — the type reads as mechanical clarity rather than editorial warmth. CTAs inherit the same #EA0016 as the logomark, maintaining button-to-brand continuity across every page; hover darkens to #C90012 without morphing the shape. Corner rounding is minimal throughout: cards clip at 4px, the primary button at 4px, filter chips at `{rounded.full}` — the pill exists only for taxonomy chips, never for CTAs or cards. Navigation is wide and clean: a 72px top bar holds the Bosch crimson-circle mark on the left, category mega-menu triggers in the center, and icon buttons (search, wishlist, cart, account) on the right, separated from page content by a single 1px `{colors.hairline}` stroke. Product cards lead with large white-background cutout photography at a 4:3 ratio flush to the card edge, then a tight metadata stack — series badge, title, star rating in red (not gold), price, and a full-width red CTA — below. The spec table is a first-class UI element rather than an afterthought: two-column, alternating `{colors.surface-soft}` rows, cell padding at 12×16px, and label/value weight contrast doing the hierarchy work. The overall effect is a site that reads more like a precision instrument catalog than a lifestyle shop: confident, systematic, and cold in the best engineering sense.

colors:
  primary: "#EA0016"
  primary-active: "#C90012"
  primary-disabled: "#F4A0A8"
  primary-light: "#FFF0F1"
  ink: "#1A1A1A"
  body: "#3C3C3C"
  muted: "#6B6B6B"
  hairline: "#D9D9D9"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F4F4F4"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  star-rating: "#EA0016"
  link: "#EA0016"

typography:
  display-xl:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Bosch Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    pointerEvents: none
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoMarkDiameter: 40px
    logoMarkColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 0 16px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    borderHover: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  series-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  rating-stars:
    activeColor: "{colors.star-rating}"
    inactiveColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowStripedBackground: "{colors.surface-soft}"
    cellPadding: 12px 16px
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    imagePosition: right
    imageSplit: "45%"
    minHeight: 520px
    padding: "{spacing.section} 0"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    border: "1px solid {colors.hairline-soft}"
    borderHover: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1/1"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  tag-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  comparison-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    height: 56px
    position: sticky
    bottom: 0
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.label-upper}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    columns: 4

## Components

### Buttons

**`button-primary`** — A solid #EA0016 rectangle with 4px corner rounding (`{rounded.xs}`), 48px height, and Bosch Sans semibold at 16px in white. Hover transitions to `{colors.primary-active}` (#C90012) without shape change. Disabled state renders `{colors.primary-disabled}` (#F4A0A8) fill with no pointer events. The button accepts a right-arrow glyph for "Shop Now," "Configure," and "Add to Cart" labels but carries no icon by default.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and red label text at `{typography.button-md}`; mirrors primary at 48px height. On hover, fill shifts to `{colors.primary-light}` and border darkens to `{colors.primary-active}`. Used for "Learn More" and secondary actions where a primary red CTA already occupies the page.

**`button-text`** — Transparent background, `{colors.primary}` label at `{typography.button-sm}`, underline decoration. Appears inline for "View All" links in category grids, spec-sheet download prompts, and filter-clear controls.

**`button-sm`** — A compact 36px version of `button-primary` at 14px Bosch Sans semibold. Used inside product cards on hover-reveal overlays and inside `comparison-bar` where vertical space is constrained.

### Inputs

**`text-input`** — Canvas white with a 1px `{colors.hairline}` border and 4px radius; border sharpens to `{colors.ink}` on focus with no color flash. 48px height matches button height for inline search-submit pairings. Placeholder text at `{colors.muted}` clears on first keypress with no floating label animation.

**`search-bar`** — `{colors.surface-soft}` fill with no visible border at rest, 44px height, and a `{colors.muted}` search glyph on the left interior. On mobile, tapping the nav search icon expands to a full-screen overlay with a larger input and recent-search suggestions. Used in both global nav and category filter sidebars.

### Navigation

**`nav-bar`** — 72px white bar with the Bosch crimson-circle logomark (40px diameter) on the left, category mega-menu triggers at `{typography.nav-link}` in the center, and icon buttons (search, wishlist, cart, account) on the right. A 1px `{colors.hairline}` bottom stroke separates the bar from content. On scroll past the hero, a soft drop-shadow appears without height change.

**`nav-dropdown`** — Full-width mega-panel at zero corner rounding (`{rounded.none}`), white fill, 1px `{colors.hairline}` top stroke, and internal columns of category links at `{typography.body-sm}`. A right column shows featured product thumbnails with title and series badge. Display is immediate (no fade) on hover; dismissed on mouse-leave.

### Product Display

**`product-card`** — 1px `{colors.hairline-soft}` border at rest (sharpens to `{colors.hairline}` on hover), 4px rounding, white fill. Image occupies the top ~60% at a 4:3 ratio flush to card edges with zero internal padding. Below the image a tight metadata column runs: `series-badge`, product title at `{typography.title-sm}`, `rating-stars`, price at `{typography.price-display}`, and a full-width `button-primary` pinned to the card bottom. No hover-reveal overlay — all information is always visible.

**`spec-table`** — Two-column table with 1px `{colors.hairline}` borders on all cells, alternating `{colors.surface-soft}` row fills (even rows), and 12×16px cell padding. Labels render at `{typography.spec-label}` (weight 400) and values at `{typography.spec-value}` (weight 600). This is the primary display vehicle for refrigerator capacity, interior dimensions, energy star rating, door configuration, and Wi-Fi connectivity.

**`series-badge`** — Small all-caps label (e.g., "500 Series," "800 Series") at `{typography.label-upper}`, `{colors.surface-soft}` fill, zero rounding. Appears above the product title on cards and PDPs. No per-tier color differentiation — series hierarchy is communicated through number alone.

**`rating-stars`** — Five star glyphs in `{colors.star-rating}` (red) for filled, `{colors.hairline}` for empty. Review count follows in `{typography.caption}`. The red-star convention keeps the rating row inside the primary brand palette rather than introducing a secondary gold accent.

### Hero & Promotions

**`hero`** — `{colors.surface-soft}` section background, left text column (headline at `{typography.display-xl}`, subhead at `{typography.body-md}`, `button-primary` CTA), right product image at 45% of the section width. Images are always white-background cutouts so they read cleanly against the soft gray field. Minimum height 520px. On mobile the text stacks above the image.

**`promo-banner`** — Full-bleed `{colors.primary}` section with white headline at `{typography.display-sm}` and a `button-secondary` (white-fill, white border) CTA. Used for seasonal promotions and financing offers. The red saturation is exactly the logomark red — no tint or lightened variant.

**`category-tile`** — Square 1:1 image tile (white-background cutout) with a white card below holding the category name at `{typography.title-md}`. 1px `{colors.hairline-soft}` border at rest, sharpens to `{colors.primary}` on hover. Used on the homepage to surface major appliance categories.

### Utility

**`tag-filter`** — Pill-shaped (`{rounded.full}`) filter chips in white with a 1px `{colors.hairline}` border and `{typography.button-sm}` labels. Active state flips to `{colors.primary}` fill with `{colors.on-primary}` text and a matching border. Used in category listing pages to filter by series, finish, configuration, and feature set.

**`comparison-bar`** — Sticky bottom bar in `{colors.surface-dark}` (near-black) that appears when 2–4 products are selected. Holds small product thumbnails, selected count, a "Compare" CTA, and a dismiss control, all in `{colors.on-dark}` white. Disappears when selection drops to zero.

**`breadcrumb`** — `{colors.muted}` text at `{typography.caption}`, "/" separators, current page at `{colors.ink}`. Appears below `nav-bar` on category listing and product detail pages.

**`footer`** — Full-bleed `{colors.surface-dark}` footer in four columns: product links, support, legal, and the Bosch circle logomark at reduced size. Column headings at `{typography.label-upper}` in white; links at `{typography.body-sm}` in `{colors.hairline}`. Social icons in white at 24px. On mobile collapses to a stacked accordion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger drawer + logomark + cart icon; hero stacks text above image; product grid 1-up; spec table horizontal scroll; search expands full-screen overlay; comparison bar full width |
| Tablet | 744–1128px | Product grid 2-up; nav shows logomark + condensed icon row (no text labels); hero image shrinks to 45% width; category tile grid 3-up; footer 2 columns |
| Desktop | 1128–1440px | Full mega-menu nav at 72px; product grid 3-up; hero at full 520px min-height; spec table at 60% page width; footer 4 columns |
| Wide | > 1440px | Content maxes at 1440px with auto side margins; product grid 4-up; hero image crops to maintain aspect ratio |

### Touch Targets
- Primary and secondary buttons are 48px tall, meeting WCAG 2.5.5 AA target size
- Nav icon buttons (search, cart, account) are 44×44px minimum tap area on mobile
- Filter chips are 36px tall with 8px horizontal gaps and no target overlap
- Product card CTA spans full card width on mobile for easy tap
- Breadcrumb links have 8px vertical padding added on mobile to widen tap zones

### Collapsing Strategy
- Navigation: full mega-menu (desktop) → icon-only row (tablet) → hamburger drawer (mobile)
- Hero: side-by-side 55/45 split → stacked text-above-image (mobile)
- Product grid: 4-up (wide) → 3-up (desktop) → 2-up (tablet) → 1-up (mobile)
- Spec table: full-width (desktop/tablet) → horizontal scroll container (mobile)
- Footer columns: 4-column (desktop) → 2-column (tablet) → stacked accordion (mobile)
- Promo banners: side-by-side text+CTA (desktop) → stacked (mobile), CTA full width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#007aff) was extracted from the live site. This value is Apple's system blue — a browser/OS UI default (focus ring, scrollbar) — and was not used as a brand color. Bosch Red #EA0016 is sourced from Bosch's widely published corporate identity guidelines instead.
- Font extraction confirmed "Bosch Sans" is loaded on the site, but no specific weight variants, optical sizes, or numerical weight values were extracted. The weight scale (400/600/700) is inferred from the visual style typical of Bosch's published brand assets.
- No dark-mode palette detected; Bosch Home US does not appear to ship a dark-mode theme variant.
- Exact button border-radius values could not be confirmed from CSS extraction — 4px (`{rounded.xs}`) is inferred from the squared visual style observable on the live site.
- No motion or animation tokens extracted; transition durations and easing curves for hover states and dropdown reveals are unknown.
- Precise CSS breakpoint values not confirmed; breakpoints in the Responsive Behavior table are inferred from visual inspection of the live site at common viewport widths.
- Product image treatment (cutout vs. lifestyle photography ratio, aspect ratio enforcement) not verified from CSS — 4:3 and white-background cutout inferred from visible product cards.
