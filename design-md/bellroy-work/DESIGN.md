---
version: alpha
name: "Bellroy (Work)"
source_url: "https://bellroy.com/products/category/accessories"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  GTUltra — Bellroy's house display face, drawn with high-contrast ink strokes and sharp inkwell terminals — is the opening signal that this is not a standard accessories catalog. The work range (pouches, pencil cases, leather desk organizers in the $75–140 band) earns its price point by refusing visual noise: the singular brand voltage is #cd4c20, a burnt-clay orange closer to kiln-fired terracotta than traffic-cone amber, reserved exclusively for add-to-cart buttons, active navigation states, and sale callouts. Every other color in the system is either neutral or recessive. Type moves through three layers without drama — GTUltra anchors hero headers at 48px/400 weight, GTUltraFine drops to editorial subheads at 24px with a lighter optical cut, and Lato at 16px carries all body copy and UI labels with flat, steady clarity. The page ground is #f7f7f7, warm enough to push white-background product photography forward without a perceptible contrast gap. Ink lands at #1d1d1b — a whisker away from pure black that preserves organic warmth. Hairlines at #d0d1d0 define product card edges without shadow-lifting; the grid reads more like a precision manufacturer's specification sheet than a scroll-jacked funnel. Button corners land at {rounded.sm} — a 4px trim echoing the stitched-edge exactness of the physical products themselves. Blue (#2279a9) appears only in hyperlinks and pagination controls; no interactive affordance uses blue — the burnt orange is sovereign for all action states. The filter panel is a left-column checklist with checkboxes and no visual gloss: material, color, size, price range, arranged plainly. Product photography is either editorial overhead or three-quarter shots on clean #f7f7f7 fields, never staged lifestyle. Wide spacing — {spacing.section} between page sections — enforces a slow-scroll catalog cadence appropriate for buyers spending $100 on a pencil case.

colors:
  primary: "#cd4c20"
  primary-active: "#b85021"
  primary-disabled: "#e8a88e"
  ink: "#1d1d1b"
  body: "#222222"
  muted: "#4a4a4a"
  muted-soft: "#9b9b9b"
  hairline: "#d0d1d0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#efefef"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#2279a9"
  link-active: "#1e6a93"
  link-deep: "#154c69"
  error: "#eb340a"
  sale-badge: "#eb340a"

typography:
  display-xl:
    fontFamily: "'GTUltra', 'Georgia', 'Frank Ruhl Libre', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'GTUltra', 'Georgia', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'GTUltraFine', 'GTUltra', 'Georgia', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  product-name:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  tag-label:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  filter-label:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    placeholderColor: "{colors.muted-soft}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    height: 64px
  breadcrumb:
    textColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    borderColor: "{colors.ink}"
    borderWidth: 1px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 420px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-sm}"
    labelTypography: "{typography.filter-label}"
    activeColor: "{colors.primary}"
    width: 240px
    gap: "{spacing.md}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    selectedBorderWidth: 2px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
    typography: "{typography.nav-label}"
    padding: "{spacing.sm} {spacing.base}"
  pagination:
    textColor: "{colors.link}"
    activeTextColor: "{colors.ink}"
    activeBg: "{colors.surface-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — The add-to-cart and primary checkout action. Burnt clay #cd4c20 fill, white uppercase Lato label at 14px/700 with 0.5px tracking, 4px corner crop ({rounded.sm}), 44px tall. On hover, deepens to #b85021 (`button-primary-active`). Disabled state uses the derived light-tint #e8a88e and should suppress pointer events.

**`button-secondary`** — White fill with a 1px #1d1d1b border and matching uppercase label. Mirrors primary geometry (44px height, {rounded.sm}) so the two sit at equal visual weight in add-to-cart + save-for-later pairings.

**`button-ghost`** — No border or fill; label text adopts #cd4c20 with uppercase tracking. Used for in-page text actions like "See all reviews" or color-filter resets where a bordered element would add too much chrome.

### Text Input

**`text-input`** — 1px #d0d1d0 border at rest, transitions to 1px #cd4c20 on focus. 42px height, {rounded.sm}, Lato 16px/400 for entered text. Placeholder is #9b9b9b. Applied to search, quantity fields, and subscriber email entry.

### Navigation

**`nav-bar`** — White canvas, 64px tall, 1px #d0d1d0 bottom border. Navigation labels are Lato 13px/600 with 0.3px tracking. Active section is underlined or colored #cd4c20. The cart icon and account icon sit right-aligned with 24px icon targets. On scroll, the bar remains fixed without visual state change.

**`breadcrumb`** — Lato 12px/400, muted gray #9b9b9b for ancestor nodes, #1d1d1b for current page. Separator is a right-angle chevron in #d0d1d0. Sits in {spacing.xs} gaps. Used above the category header on all PLP and PDP pages.

**`category-tab`** — Horizontal tab strip beneath the hero on category pages. Lato 13px/600, #4a4a4a at rest, #1d1d1b active. Active indicator is a 2px solid #cd4c20 underline flush with the strip bottom. Tabs for material (leather, fabric, nylon) or subcategory filter.

### Product Card

**`product-card`** — Flat bordered card, 1px #d0d1d0, no border radius, no drop shadow. Image area fills a 4:3 container on a #f7f7f7 field. Product name is Lato 15px/600 below the image; price is Lato 15px/400 on the next line. Hover state sharpens the border to 1px #1d1d1b with no elevation change — the transition stays in-plane. Sale and New badges (`badge-sale`, `badge-new`) overlay the top-left image corner as flat sharp-cornered chips.

### Hero Banner

**`hero-banner`** — #f7f7f7 background panel; title in GTUltra 48px/400 at -0.5px letter-spacing; subtitle in GTUltraFine 24px/400. Body copy drops to Lato 16px/400. Minimum height 420px on desktop. No full-bleed photography — the hero is typographic with a restrained product image to the right, not a cinematic background treatment.

### Filter Sidebar

**`filter-sidebar`** — 240px wide left column, white fill, 1px #d0d1d0 right border. Section headings are Lato 12px/700 uppercase with 0.8px tracking. Filter items are 13px/400 checkboxes with #cd4c20 checked fill. Color filter row uses `color-swatch` chips (20px circles, {rounded.full}, 2px #1d1d1b selection ring). On mobile the sidebar converts to a bottom sheet triggered by a "Filter" pill button.

### Badges

**`badge-new`** — #1d1d1b fill, white uppercase Lato 10px/700 label, no border radius, 3px 6px padding. Overlays image top-left.

**`badge-sale`** — #eb340a fill, white label, same geometry as `badge-new`. Never appears simultaneously with `badge-new`.

### Pagination

**`pagination`** — Page number links in Lato 12px/700 uppercase, #2279a9 at rest. Active page number shows white text on #f7f7f7 background with 2px corner ({rounded.xs}). Previous/Next use the same typography with chevron icons.

### Footer

**`footer`** — Deep #1d1d1b fill, near-black on-dark. Section headings are Lato 12px/700 uppercase/0.8px tracked in #ffffff. Link columns use Lato 14px/400 in #9b9b9b with no underline at rest, #ffffff on hover. Padding is {spacing.xxl} vertical and {spacing.section} horizontal. A fine 1px #4a4a4a hairline separates the link columns from the legal/copyright row below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar converts to bottom-sheet modal triggered by sticky "Filter + Sort" bar; nav collapses to hamburger; hero stacks text above image; buttons go full-width on PDP |
| Tablet | 744–1128px | Two-column product grid; filter bar moves inline above the grid as a horizontal chip row; hero shows 50/50 split layout; nav remains horizontal but secondary links collapse |
| Desktop | 1128–1440px | Three-column product grid; filter sidebar visible at 240px left; standard nav fully expanded; hero at full 420px min-height |
| Wide | > 1440px | Content constrained to 1440px max-width with auto horizontal margins; product grid expands to four columns; hero padding increases proportionally |

### Touch Targets

- All tappable elements minimum 44×44px (buttons, swatches, nav links, filter checkboxes)
- Color swatches (20px visual) expand tap area to 36px via invisible padding
- Pagination numbers have minimum 36px touch height

### Collapsing Strategy

- Filter sidebar collapses to a full-screen bottom sheet on mobile, preserving all filter options without truncation
- Navigation items reduce to icon-only on tablet if viewport is near the lower breakpoint, with labels on hover
- Product name truncates to two lines with CSS line-clamp; price and badge always fully visible
- Footer columns stack vertically on mobile in the order: Products, About, Support, Legal

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white `#ffffff` canvas was not observed in the extracted palette — implied from standard layout conventions but not confirmed; #f7f7f7 is used as the documented page background
- `primary-disabled` (#e8a88e) is a manually derived lighter tint of #cd4c20 — not observed directly in the extracted color list
- Exact font weights for GTUltra and GTUltraFine could not be confirmed from extraction; 400/regular is assumed based on the high-contrast nature of the face
- GTUltraFine may only appear in select editorial contexts (campaign pages, lookbooks) and may not be served on the accessories category page specifically
- Hover and focus transition timing (duration, easing curve) not captured
- Bellroy's custom SVG icon set design and sizing not captured — icon style inferred as minimal single-stroke
- Frank Ruhl Libre font stack inclusion is unexplained — likely a CMS fallback or internationalization artifact, not an intended brand typeface
- Mobile-specific breakpoint values not confirmed from extraction; the breakpoints listed are inferred from observed layout behavior
- Animation/scroll behavior (sticky add-to-cart bar on PDP, filter panel scroll sync) not captured
