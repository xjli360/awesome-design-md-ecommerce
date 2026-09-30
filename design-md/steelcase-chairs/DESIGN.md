---
version: alpha
name: "Steelcase (Chairs)"
source_url: "https://store.steelcase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dark charcoal at #272725 — not true black but the particular gray-brown of cold-rolled steel — anchors every primary action surface in the Steelcase store, pulling the interface toward industrial restraint at a moment when most furniture brands are racing toward warm whites and editorial photography. The full extracted palette runs almost entirely through neutral registers: body text at #555555, secondary labels at #676767, hairlines at #e3e3e3, and page wash at #f5f5f5. The single chromatic outlier is a muted brick-red at #b85455, appearing in alert states and promotional callouts — not a chosen accent so much as a safety signal borrowed from Bootstrap's color vocabulary. Typography makes no custom font investment: the entire site runs on Arial, Helvetica Neue, and system sans-serif stacks, a decision that reads as engineering-department specification-first rather than brand-department lifestyle-first. This is consistent with Steelcase's buyer profile — facilities managers, corporate procurement leads, and workplace designers who arrive with dimension requirements before they consider finish options. The button and card geometry uses conservative radius values ({rounded.xs} to {rounded.sm}), keeping edges close to square; nothing pill-shaped exists in the UI. Navigation is organized hierarchically by product category — seating, desks, storage, accessories — with sub-categories accessible via dropdown rather than editorial collection pages. Product cards lead with model name and price, and material/fabric configurator entry points are visible without hover, reflecting a customer who needs to specify before they can purchase. The overall interface tone is that of a well-maintained enterprise catalog: high information density, modest whitespace at {spacing.base} rhythm, and a grid that trusts structure over visual drama. Steelcase's digital presence matches its physical products — functional, durable, and designed to be used rather than admired.

colors:
  primary: "#272725"
  primary-active: "#080808"
  primary-disabled: "#9d9d9d"
  ink: "#272725"
  body: "#555555"
  muted: "#676767"
  muted-mid: "#777777"
  hairline: "#e3e3e3"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#337ab7"
  link-active: "#286090"
  link-dark: "#204d74"
  accent: "#b85455"
  accent-muted: "#f2dede"
  success: "#3c763d"
  success-surface: "#dff0d8"
  warning: "#8a6d3b"
  warning-surface: "#fcf8e3"
  info-surface: "#d9edf7"
  dark-navy: "#122b40"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  label-uppercase:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  breadcrumb:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
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
    padding: 8px 16px
    height: 36px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 7px 15px
    height: 36px
    border: "1px solid {colors.hairline}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
    padding: 0
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.link}"
    boxShadow: "inset 0 1px 1px rgba(0,0,0,0.075), 0 0 6px rgba(51,122,183,0.3)"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.base}"
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-md}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.12)"
    borderColor: "{colors.muted-mid}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 360px
    padding: "{spacing.xxl} {spacing.section}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
  hero-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 240px
    padding: "{spacing.xl} {spacing.xxl}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    headerTypography: "{typography.title-sm}"
    width: 240px
    padding: "{spacing.base}"
    borderRight: "1px solid {colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.sm}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "6px 40px 6px 12px"
    height: 34px
    iconColor: "{colors.muted}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "2px solid transparent"
  category-tab-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
    backgroundColor: transparent
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  product-badge-new:
    backgroundColor: "{colors.link}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  alert-info:
    backgroundColor: "{colors.info-surface}"
    textColor: "{colors.link-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.link-active}"
    padding: "{spacing.sm} {spacing.base}"
  alert-success:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.success}"
    padding: "{spacing.sm} {spacing.base}"
  alert-danger:
    backgroundColor: "{colors.accent-muted}"
    textColor: "{colors.accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.accent}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    headerTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"
    borderTop: none
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.link}"
    activeTextColor: "{colors.on-primary}"
    padding: "6px 12px"
  configurator-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.primary}"
    gap: "{spacing.xs}"

## Components

### Buttons

**`button-primary`** — A square-shouldered ({rounded.xs}) dark charcoal (#272725) button at 36px height, set in bold 14px Arial. The near-black fill provides strong contrast against the white canvas without introducing any brand-color surprise; on hover it deepens to #080808. Disabled state renders in #9d9d9d with the same geometry. Steelcase does not use pill-shaped CTAs — the squared edge signals specification-grade confidence rather than consumer-market softness.

**`button-secondary`** — White canvas with a 1px #e3e3e3 border and #272725 ink text, matching the primary button's fill color in text so both reads as belonging to the same system. Used for secondary configurator actions (Save to List, Compare, Download Spec Sheet) placed alongside a primary Add to Cart. The outline weight matches the text-input border, creating a coherent control family.

**`button-link`** — Bootstrap-style inline link (#337ab7, underline on hover) for contextual document actions like View Specs or Download PDF within product descriptions. No background or border — lives inline with body copy at 14px, same weight as surrounding text.

### Inputs

**`text-input`** — 34px height, 1px #e3e3e3 border, {rounded.xs} corners, 14px Arial body. On focus the border transitions to #337ab7 with a soft diffuse blue glow (Bootstrap default focus ring). Placeholder text in #676767. Applies to quantity selectors, search fields, and address inputs at checkout. The form aesthetic is explicitly Bootstrap 3 — no custom overrides to the focus style are evident.

**`search-bar`** — Shares the text-input geometry but adds a right-side magnifying-glass icon in #676767. Sits at the right end of the nav-bar at desktop widths; collapses to an icon-only toggle on tablet and below. No pill treatment — the bar is entirely functional.

### Navigation

**`nav-bar`** — 60px white bar with a 1px #e3e3e3 bottom border. Logo sits left, primary category links (bold 14px Arial) distribute center-to-right, utility icons (search, cart, account) anchor the far right. The overall structure is dense and information-first; no mega-menu imagery or lifestyle photography interrupts the link hierarchy.

**`nav-bar-top-strip`** — A 36px charcoal (#272725) utility band above the primary nav carrying account, dealer-portal, trade-program, and contact links in 12px white caption type. This two-layer nav structure is characteristic of B2B-adjacent retail: consumer buyers ignore the top strip; procurement managers read it first.

**`category-tab`** — Horizontal tab row below the hero for sub-category filtering (All Chairs, Task, Executive, Side, Stools, Lounge). Inactive tabs render in #676767; the active tab carries a 2px #272725 bottom-border underline with #272725 text. No background fill at any tab state — the underline performs all the selection signaling.

### Product Grid

**`product-card`** — White card with 1px #e3e3e3 border, {rounded.xs} corners, and 16px internal padding. A 4:3 image block sits at top, followed by the model name in bold 16px, a short descriptor in 14px #555555, and price in 20px bold. On hover, a `0 2px 8px rgba(0,0,0,0.12)` shadow lifts the card and the border darkens to #777777. No wishlist overlay, no Quick Add drawer — the card is a link to the PDP, consistent with a configured-purchase model rather than impulse buying.

**`product-badge`** — Flat-square badge ({rounded.none}) in charcoal (#272725) with 11px uppercase bold white label. Applied to outlet pricing or best-seller designations. The `product-badge-new` variant uses #337ab7 fill for newly introduced models, borrowing Bootstrap's link blue as a mild distinction signal.

**`filter-sidebar`** — 240px left panel in #f5f5f5 with a 1px #e3e3e3 right border. Section headers in bold 16px ink, filter options in 14px body weight with checkbox controls at standard touch-target spacing. Applied selections surface as `filter-chip-active` tokens — charcoal fill, white text — giving the buyer a visible inventory of active constraints above the grid. On mobile, the sidebar moves to a bottom sheet triggered by a Filter & Sort button.

### Hero

**`hero`** — Full-width charcoal (#272725) band, minimum 360px tall. A bold 32px display headline and 14px supporting paragraph run in white; CTAs use `button-secondary` (white border, charcoal text inverted against the dark fill via the white canvas background on the button itself) for legibility. No parallax, no video loop — the hero is static, reinforcing a performance-conscious B2B context where page weight matters.

**`hero-secondary`** — Reduced-height variant (minimum 240px) in #f5f5f5 for interior category pages. Headline at 24px bold #272725, body at 14px #555555. Used for section intros (Task Seating, Lounge & Collaborative) where photography is secondary to navigation efficiency.

### Alerts and Feedback

**`alert-info`**, **`alert-success`**, **`alert-danger`** — Standard Bootstrap 3 alert blocks: light tinted backgrounds (#d9edf7, #dff0d8, #f2dede) with matching 1px border and text in #204d74, #3c763d, or #b85455 respectively. {rounded.xs} corners, 16px horizontal padding. Appear for form validation messages, cart warnings, and order confirmation notices. The brick-red #b85455 extracted from the site most likely originates here rather than as a deliberate brand accent.

### Footer

**`footer`** — Full-width charcoal (#272725) footer, mirroring the nav-bar-top-strip color to close the page with the same dark slab that opened it. Column-grouped links in 13px #eeeeee hairline-soft type, section headers in bold 16px white. Four-column layout: Products, Support, Company, Connect. A social icon row sits at the base using FontAwesome glyphs. No gradient break or secondary color interrupts the flat charcoal.

### Pagination

**`pagination`** — Bootstrap-style numbered row: each page button has a 1px #e3e3e3 border, white background, and #337ab7 link text. The active page button fills with #337ab7 and switches to white text. {rounded.xs} on each individual button. Appears below the product grid on all product-listing pages.

### Configurator Swatches

**`configurator-swatch`** — 24px circular swatches ({rounded.full}) for fabric and finish selection on the chair PDP. The inactive swatch carries a 2px transparent border; the selected swatch displays a 2px #272725 ring that clearly marks the current selection. Swatches are arranged in a horizontally scrollable row on mobile with {spacing.xs} gaps, keeping the full option set reachable without vertical stack growth.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter-sidebar becomes bottom sheet drawer; nav collapses to hamburger + logo + cart icon; hero height reduces to 240px; nav-bar-top-strip hidden |
| Tablet | 744–1128px | Two-column product grid; filter-sidebar visible as collapsible left panel with toggle; nav shows logo, search icon, and cart icon with primary links in hamburger |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all category links visible; 240px filter-sidebar pinned left; hero at full 360px minimum height |
| Wide | > 1440px | Four-column product grid; content max-width 1400px centered; hero content constrained to 1200px column; increased section-level padding at {spacing.section} |

### Touch Targets

- All buttons expand to minimum 44px tap height on mobile via increased vertical padding
- Filter checkboxes padded to 44×44px effective touch zone with generous label click area
- Hamburger and cart nav icons minimum 44×44px
- Configurator swatches expand from 24px to 36px diameter on touch viewports
- Pagination buttons minimum 44px height on mobile
- Category tabs increase vertical padding to meet 44px tap height at mobile breakpoint

### Collapsing Strategy

- nav-bar-top-strip hidden below 744px; dealer and trade links fold into the hamburger menu as a secondary group
- Category tabs below the hero collapse to a horizontal scroll strip on mobile — no line-wrapping, with fade-out edge indicating overflow
- filter-sidebar becomes a full-height bottom sheet on mobile, triggered by a "Filter & Sort" button carrying an applied-count badge
- Product cards maintain {spacing.base} internal padding and 4:3 image aspect ratio at all breakpoints
- Footer four-column layout collapses to single-column accordion on mobile; each section header becomes an expand/collapse toggle
- Search bar always visible inline in nav at desktop; collapses to icon-only toggle at tablet and below, expanding to a full-width overlay input on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected — the entire store runs on system Arial/Helvetica stacks; a proprietary Steelcase typeface (if one exists in the offline design system) is either loaded via JavaScript or absent from the storefront entirely
- Extracted palette is dominated by Bootstrap 3 framework defaults (#337ab7, #3c763d, #8a6d3b, #a94442, #d9edf7, #dff0d8, #f2dede, #fcf8e3); reliably brand-curated colors beyond #272725 are difficult to isolate
- The brick-red #b85455 may be a Bootstrap alert-danger override rather than an intentional brand accent — its role as a deliberate accent color is uncertain
- Canvas white (#ffffff) was not present in the extracted color list; inferred from standard page-background convention and may vary by section
- No meta theme-color declared; primary brand color inferred from the most distinctive extracted hex (#272725)
- No CSS custom property or design token system detected in extraction; suggests the storefront predates a formal token layer
- Chair configurator UI (3D viewer, material selector panels, dimension options) not captured in extraction depth — PDP configurator component structure is estimated from conventions
- Exact breakpoint pixel values not confirmed from source CSS; responsive breakpoints are inferred from Bootstrap 3 grid defaults
- Animation timing and easing values not extractable; hover transition durations for cards, sidebar drawers, and dropdown menus are estimated at Bootstrap defaults (~200–300ms ease)
- Icon assignments within FontAwesome and Glyphicons Halflings sets per UI function (cart, search, account, filters) not individually documented
