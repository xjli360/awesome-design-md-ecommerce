---
version: alpha
name: "Applied Industrial Technologies"
source_url: "https://www.applied.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every pixel on applied.com earns its keep by reducing the distance between a part number and a purchase order — the entire layout is a compressed search instrument, not a storefront. The lone confirmed extraction, #313131, is the ink that anchors headers, part numbers, and facet labels in an industrial-weight charcoal that resists the softness consumer brands favor. Because the live site is guarded by bot-mitigation (the page title returned "Just a moment…"), palette recovery was minimal; brand-knowledge fills the gap conservatively. Applied's corporate red — a saturated #c8102e visible in their printed catalogs, trade-show materials, and legacy CSS artifacts — functions as the primary action color, appearing on Add to Cart buttons, promotional callouts, and the search submit trigger. The typographic stack is pure system: Arial leads at every weight, pushed to bold 700 at display sizes rather than using a custom variable font, which produces a blunt, high-legibility hierarchy that engineers scanning a 200-row spec table can parse at a glance. Corner radii sit near zero — `{rounded.xs}` at most on form fields and cards — reinforcing a grid-governed aesthetic where straight edges signal precision over approachability. The dense product grid (twelve-column at Wide breakpoint) accommodates the browsing pattern of a maintenance buyer who already knows they need a 6205-2RS bearing and just wants quantity pricing. Catalog pages lead with a specification table before photography; descriptions are secondary to dimensional data, load ratings, and compatibility flags. Horizontal hairline rules in `{colors.hairline}` divide facet categories in the left rail, and `{colors.surface-soft}` alternates with `{colors.canvas}` in striped spec rows. A narrow announcement bar above the nav carries freight pricing thresholds and will-call locations in `{typography.caption}` on a `{colors.primary}` background — industrial commerce's equivalent of a front-page banner, built for buyers who skip straight to fulfillment logistics.

colors:
  primary: "#c8102e"
  primary-active: "#a10d24"
  primary-disabled: "#e8a0aa"
  primary-hover: "#b00e27"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#9b9b9b"
  hairline: "#d1d1d1"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-alt: "#f0f0f0"
  on-primary: "#ffffff"
  promo-banner: "#c8102e"
  on-promo: "#ffffff"
  success: "#2e7d32"
  warning: "#f5a623"
  danger: "#c8102e"
  link: "#005b9a"
  link-hover: "#003f6b"
  price-primary: "#313131"
  price-sale: "#c8102e"
  badge-new: "#005b9a"
  badge-on: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  nav-link-sub:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  facet-label:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
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
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 44px
    width: "100%"
  button-quote:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    width: 64px
    height: 38px
    border: "1px solid {colors.hairline}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "2px solid {colors.primary}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.none}"
      padding: 0 20px
  announcement-bar:
    backgroundColor: "{colors.promo-banner}"
    textColor: "{colors.on-promo}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 {spacing.base}
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 40px
    accountIconColor: "{colors.ink}"
    cartIconColor: "{colors.primary}"
  mega-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.nav-link-sub}"
    linkColor: "{colors.link}"
    borderTop: "3px solid {colors.primary}"
    boxShadow: "0 4px 8px rgba(0,0,0,0.15)"
    padding: "{spacing.lg} {spacing.xl}"
    columns: 4
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    nameTypography: "{typography.body-md}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.price-primary}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-grid:
    gap: "{spacing.md}"
    columns:
      mobile: 2
      tablet: 3
      desktop: 4
      wide: 6
  facet-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 240px
    borderRight: "1px solid {colors.hairline}"
    headingTypography: "{typography.facet-label}"
    headingColor: "{colors.ink}"
    optionTypography: "{typography.body-sm}"
    divider: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  facet-checkbox:
    accentColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.body}"
    checkedLabelColor: "{colors.ink}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    rowEven: "{colors.surface-soft}"
    rowOdd: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    cellPadding: "{spacing.sm} {spacing.md}"
  breadcrumb:
    textColor: "{colors.link}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-on}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-instock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
    minWidth: 36px
  footer:
    backgroundColor: "#1a1a1a"
    textColor: "#cccccc"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    linkColor: "#cccccc"
    linkHoverColor: "{colors.canvas}"
    dividerColor: "#444444"
    padding: "{spacing.xxl} 0"
  order-form-row:
    backgroundColor: "{colors.canvas}"
    hoverBackgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
    partNumberTypography: "{typography.part-number}"
    qtyInputWidth: 64px
  hero-banner:
    minHeight: 360px
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    overlayOpacity: 0.45
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat `{colors.primary}` red (#c8102e) fill with white uppercase text at `{typography.button-md}` (14px/700, 0.5px tracking) and a minimal `{rounded.xs}` radius that keeps the corner nearly square, signaling catalog-precision over consumer warmth. Hover transitions to `{colors.primary-hover}`, active darkens to `{colors.primary-active}`, disabled washes to `{colors.primary-disabled}` — all states maintain the same geometry, no shadow effects. The Add to Cart variant (`button-add-to-cart`) stretches full-width on mobile and reaches 44px height for reliable touch targeting.

**`button-secondary`** — White fill with `{colors.ink}` (#313131) text and a 1px `{colors.hairline}` border; hover thickens the border to `{colors.ink}` and fills `{colors.surface-soft}`. Used for secondary actions like "Request Quote" when displayed alongside a primary CTA.

**`button-quote`** — White fill with a 2px `{colors.primary}` border and red text; this outline-red treatment is the standard pairing with `button-add-to-cart` on product detail pages for users who need contract pricing.

**`button-ghost`** — Transparent with `{colors.link}` blue text; handles tertiary actions like "View Details", "Compare", and pagination links within dense grid contexts.

### Search Bar

**`search-bar`** — A full-width form at 44px height with a bold 2px `{colors.primary}` border distinguishing it from ordinary inputs. The submit button is a solid red block flush to the right edge, containing a white search icon; no radius is applied to the join, creating a single compound shape. Autocomplete drops below the field in a white `{colors.surface-card}` panel with `{rounded.xs}` on the bottom corners only.

### Navigation

**`announcement-bar`** — 36px `{colors.primary}` band above everything; ships freight thresholds, branch hours, and promotional deadlines in `{typography.caption}` white. Collapses to an expandable row on mobile to preserve header height.

**`nav-bar`** — 60px white bar carrying the Applied logo at left (40px height), a full-width search bar spanning the center column, and cart/account icons at right. A bottom `{colors.hairline}` rule separates it from the mega-nav trigger row below. Cart icon accent in `{colors.primary}` provides the only color element in the top chrome outside the announcement bar.

**`mega-nav`** — Drops from the category trigger row on hover, 4-column layout with a 3px `{colors.primary}` top rule acting as an anchor line. Category headings in `{typography.title-sm}` bold, child links in `{typography.nav-link-sub}` at `{colors.link}` blue. Box shadow at 8px blur prevents edge loss against white-background pages.

### Product Cards & Grid

**`product-card`** — 1px `{colors.hairline}` border on white `{colors.surface-card}` background with `{rounded.xs}` corners. Part number renders in `{typography.part-number}` monospace at `{colors.muted}` above the product name in `{typography.body-md}`. Price in `{typography.price-sm}` bold at `{colors.price-primary}`. On hover the border upgrades to `{colors.primary}` and a subtle shadow lifts the card — no transform, just color and elevation change. The image block uses a 1:1 aspect ratio with object-fit contain and a `{colors.surface-soft}` background to handle mixed image sizes gracefully.

**`product-grid`** — Gap at `{spacing.md}` across all breakpoints. Columns scale: 2 on mobile, 3 on tablet, 4 on desktop, 6 on wide. The dense 6-column wide layout is the signature of the MRO catalog context — buyers compare rows visually and need maximum density.

### Facet Rail

**`facet-rail`** — 240px fixed sidebar with `{colors.hairline}` right border. Each facet category opens with a `{typography.facet-label}` uppercase heading (11px, 700, 0.5px tracking), followed by checkbox options in `{typography.body-sm}`. `{colors.hairline-soft}` rules separate categories. The checkbox accent color is `{colors.primary}` red so selected filters have brand visibility. On mobile the rail converts to a modal drawer triggered by a "Filter" button.

### Spec Table

**`spec-table`** — Two-column zebra table: odd rows at `{colors.canvas}`, even at `{colors.surface-soft}`. Headers in `{typography.spec-label}` uppercase muted; values in `{typography.body-sm}` ink. Cell padding `{spacing.sm} {spacing.md}`. The table is the primary content element on product detail pages — it appears above product descriptions and often contains 20–40 rows of dimensional, load, and compatibility data.

### Badges

**`badge-new`** — `{colors.badge-new}` blue pill in `{typography.caption-bold}` white, `{rounded.xs}`. **`badge-promo`** — `{colors.primary}` red for percentage-off and clearance callouts. **`badge-instock`** — `{colors.success}` green for immediate availability confirmation, appearing inline with lead time data.

### Order Form Row

**`order-form-row`** — Horizontal row used in list/table views to enable line-item ordering without navigating to PDP. Carries part number in `{typography.part-number}`, description in `{typography.body-sm}`, a 64px `quantity-input` field, and `button-add-to-cart` compressed to a 36px row height. Hover fills the row `{colors.surface-soft}`.

### Footer

**`footer`** — Near-black #1a1a1a background (Applied's standard footer treatment, separate from `{colors.ink}`) with four link columns, heading in `{typography.title-sm}` white, links in `{typography.body-sm}` at #cccccc. `{spacing.xxl}` vertical padding. A compliance/legal strip below carries certifications, terms links, and copyright in `{typography.caption}` muted on a slightly darker rule.

### Hero Banner

**`hero-banner`** — 360px minimum height with a dark scrim (0.45 opacity) over photography or illustration. Heading at `{typography.display-xl}`, subhead at `{typography.body-md}` white, single `button-primary` CTA. On product-category landing pages the hero may compress to 240px with a tighter copy column. No carousel animation — Applied's hero is a static confidence statement, not a slideshow.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product grid 2-column; facet rail becomes modal drawer via "Filter" button; search bar full-width below logo row; announcement bar collapses to single line; nav becomes hamburger menu |
| Tablet | 744–1128px | Product grid 3-column; facet rail appears inline at 200px; mega-nav renders as 2-column dropdown; hero banner compresses to 280px |
| Desktop | 1128–1440px | Full facet rail at 240px; product grid 4-column; mega-nav 4-column; hero at full 360px; content max-width 1280px centered |
| Wide | > 1440px | Product grid expands to 6-column in catalog views; content area stays at 1280px max-width; side whitespace increases proportionally |

### Touch Targets

- All buttons minimum 44px height on mobile (Add to Cart, Quote, Search submit)
- Quantity inputs 44px touch target; tap increment/decrement controls flank the field at 44×44px each
- Facet checkboxes have 32px minimum tap height with full-row hit target
- Nav hamburger and icon buttons 44×44px
- Pagination controls minimum 36px, expanded to 44px on mobile

### Collapsing Strategy

- Mega-nav collapses to slide-in hamburger drawer with accordion category expansion
- Facet rail collapses to fullscreen modal drawer; active filter count shown as red badge on the trigger button
- Spec table scrolls horizontally within a constrained container on mobile; row labels remain sticky
- Footer columns stack vertically; each column becomes a tappable accordion on mobile
- Announcement bar truncates to single most-important message on mobile with a right-chevron link to full promotions page
- Order form rows stack price and quantity below product name; CTA becomes full-width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette severely limited**: only one hex color (#313131) was extracted — the site returned "Just a moment…" (Cloudflare bot challenge) and no CSS variables were parsed. All colors other than #313131 are inferred from brand-knowledge (corporate catalogs, trade materials) and should be validated against the live computed styles once accessible.
- **Primary red unverified**: #c8102e is a widely cited Applied Industrial corporate red but was not confirmed by pixel extraction from the live site. Actual value may differ slightly (some sources show #d32f2f or #bf0d23).
- **No custom font detected**: font-family stacks are entirely system fonts (Arial, system-ui). It is possible Applied uses a licensed typeface loaded via JS or a third-party CDN that was blocked during extraction. Verify whether a brand typeface (e.g., a condensed sans) exists in the live CSS.
- **Link blue (#005b9a) unverified**: derived from common Applied web materials; actual anchor color not extractable.
- **Footer background (#1a1a1a) unverified**: based on common dark-footer convention for industrial distributors; not confirmed.
- **Icon set unknown**: Applied likely uses a proprietary or licensed industrial icon set; no SVG sprite or icon font was extracted.
- **Animation and transition values**: zero motion data recovered; all transitions in this spec are inferred from industrial-site convention (fast, functional, no decorative easing).
- **Authenticated/account UI**: my account, order history, and punch-out procurement UI were not accessible for extraction.
