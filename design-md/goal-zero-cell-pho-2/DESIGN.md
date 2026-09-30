---
version: alpha
name: "Goal Zero"
source_url: "https://www.goalzero.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The charge indicator on a Yeti power station glows the same high-voltage chartreuse as every primary CTA on goalzero.com — #cad618, a color that functions less as brand identity and more as a live readout: power available, action possible. The entire design system is organized around this signal color sitting against deep near-black infrastructure (#212121, #231f20), creating a contrast vocabulary borrowed from instrument panels rather than consumer storefronts. Galaxie Polaris, Goal Zero's primary typeface, is a geometric sans-serif that carries a precision-tool character; its Condensed variant handles campaign headers and product names at tight line-heights and compressed widths, while Galaxie Polaris Book runs body copy at relaxed 1.5 spacing. Button labels are uppercase and tracked — a convention from outdoor gear labeling, where every call-to-action reads more like a toggle switch than a soft invitation. A secondary tier of steel blues (#7796a8, #1c9ad6, #003f84) manages informational hierarchy: spec callouts, informational links, and availability notices occupy the blue register while all purchase-intent surfaces hold `{colors.primary}` chartreuse. Cards are nearly square-cornered — `{rounded.xs}` throughout — with #d2d3d3 hairline borders giving the product grid a technical-catalog rigor. The promo bar above the nav and CTA overlays on hero images share the same `{colors.primary}` fill, keeping commercial pressure visible and consistent without bleeding into the interface chrome. Error and alert states step to #d20000 against white, isolating urgency from promotional voltage. Deep `{colors.dark-surface}` footers absorb the page into darkness, with `{colors.light-gray}` navigation links providing quiet exit paths while `{colors.on-dark}` text anchors legal and support content.

colors:
  primary: "#cad618"
  primary-active: "#bfd22b"
  primary-disabled: "#e8ec9d"
  ink: "#212121"
  body: "#3d4246"
  muted: "#788188"
  hairline: "#d2d3d3"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#efefef"
  on-primary: "#212121"
  on-dark: "#ffffff"
  steel-blue: "#7796a8"
  info-blue: "#1c9ad6"
  navy: "#003f84"
  sky-blue: "#9ecdff"
  alert-red: "#d20000"
  forest-green: "#145623"
  dark-surface: "#231f20"
  mid-gray: "#6b6a6b"
  light-gray: "#acacac"
  charcoal: "#383c41"
  scrim: "#1b1e21"

typography:
  display-xl:
    fontFamily: "'Galaxie Polaris Condensed', 'Galaxie Polaris', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Galaxie Polaris Condensed', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Galaxie Polaris Condensed', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  title-md:
    fontFamily: "'GalaxiePolaris-Medium', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'GalaxiePolaris-Medium', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Galaxie Polaris Book', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Galaxie Polaris Book', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Galaxie Polaris', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'GalaxiePolaris-Medium', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GalaxiePolaris-Medium', 'Galaxie Polaris', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Galaxie Polaris', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "'Galaxie Polaris Condensed Book', 'Galaxie Polaris Condensed', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  badge-label:
    fontFamily: "'Galaxie Polaris', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Galaxie Polaris Condensed', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  button-outline-light:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.surface-card}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    minHeight: 580px
    overlayScrim: "linear-gradient(to right, {colors.scrim} 40%, transparent)"
  spec-badge:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  power-indicator:
    fillColor: "{colors.primary}"
    trackColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.ink}"
    height: 8px
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.info-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.mid-gray}"
  alert-banner:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  info-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderLeft: "3px solid {colors.info-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    alternateBackground: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.light-gray}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.light-gray}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Filled chartreuse (`{colors.primary}`) with dark ink text (`{colors.on-primary}`) and uppercase tracked label (`{typography.button-md}`), height 48px, `{rounded.xs}` corners. Active state shifts to `{colors.primary-active}` (#bfd22b); disabled state bleaches to `{colors.primary-disabled}` with muted label. This is the sole high-energy surface in the system — it appears on product CTAs, cart add buttons, and checkout flows.

**`button-secondary`** — Solid `{colors.ink}` (#212121) fill with white `{colors.on-dark}` text. Used alongside `button-primary` on hero banners where two actions must coexist without competing — "Shop Now" (chartreuse) plus "Learn More" (ink). Same 48px height and `{rounded.xs}` geometry.

**`button-outline`** — Transparent fill with a 2px `{colors.ink}` border and `{colors.ink}` text. Appears in product configuration flows, secondary filter actions, and light-canvas contexts where both filled buttons would overload. `button-outline-light` mirrors the same structure with `{colors.on-dark}` border and text for use over dark or photographic backgrounds.

### Navigation

**`nav-bar`** — Full-width `{colors.ink}` header at 64px, with `{typography.nav-link}` labels in `{colors.on-dark}`. Active or hovered nav items shift to `{colors.primary}` to signal the charged state. Logo anchors the left; a cart icon, search trigger, and account link occupy the right. On scroll, the bar stays fixed with no transparency shift — the dark ground persists at all scroll depths.

**`promo-bar`** — A slim 40px band above the nav filled solid `{colors.primary}` with centered `{typography.caption}` in `{colors.on-primary}`. Carries shipping thresholds, seasonal offers, and product launch announcements. The sole above-nav surface.

### Product Card

**`product-card`** — White canvas with `{colors.surface-card}` image well, `{rounded.xs}` corners, and a 1px `{colors.hairline}` border. Product name uses `{typography.title-sm}`, price uses `{typography.price-display}` in Galaxie Polaris Condensed at 24px, and short spec copy drops to `{typography.body-sm}`. Badge overlays for sale (`sale-badge`, red) or category (`category-badge`, chartreuse) sit in the top-left corner of the image well. No hover elevation — border darkens slightly on hover to acknowledge interaction without theatrical lift.

### Badges & Labels

**`spec-badge`** — Dark charcoal fill (`{colors.charcoal}`) with chartreuse `{colors.primary}` uppercase text (`{typography.spec-label}`), zero radius. Used directly on product image overlays and spec comparison rows to surface wattage, capacity, and weight in technical shorthand.

**`category-badge`** — Chartreuse fill with `{colors.on-primary}` ink text, `{rounded.xs}`, small uppercase label. Tags products by collection (Yeti, Nomad, Flip) at listing level.

**`sale-badge`** — `{colors.alert-red}` fill, white `{colors.on-dark}` text. Appears alongside `category-badge` when a promotion is active; the two never share the same corner position.

### Hero Banner

**`hero-banner`** — Full-bleed photographic panel, minimum 580px tall, with a left-anchored `{colors.scrim}` gradient fading from 40% opacity to transparent. `{typography.display-xl}` headline in `{colors.on-dark}` stacks above a `{typography.display-sm}` subhead, followed by a CTA row pairing `button-primary` and `button-outline-light`. The gradient ensures legibility over high-key outdoor photography without cropping or darkening the image globally.

### Power Indicator

**`power-indicator`** — A horizontal progress bar representing charge state or output capacity. `{colors.primary}` fill on a `{colors.hairline}` track, 8px tall, `{rounded.xs}`. Accompanied by a `{typography.caption}` percentage label in `{colors.ink}` aligned right. This component echoes the physical LED ring on Goal Zero hardware, grounding digital UI in product reality.

### Search

**`search-bar`** — `{colors.surface-soft}` background, `{rounded.xs}`, 44px height, with a magnifier icon in `{colors.mid-gray}`. Focus ring shifts border to `{colors.info-blue}`. Used in the nav flyout and on the products listing page.

### Alerts & Callouts

**`alert-banner`** — `{colors.alert-red}` strip with white text (`{colors.on-dark}`) and `{typography.body-sm}`. Appears for out-of-stock notices, shipping cutoff warnings, and inventory alerts.

**`info-callout`** — Light `{colors.surface-soft}` background with a 3px `{colors.info-blue}` left border. Carries compatibility notes, solar charging estimates, and environmental specs. Not an error surface — purely informational.

### Spec Table

**`spec-table-row`** — Alternating white and `{colors.surface-soft}` rows. Label column in `{typography.spec-label}` uppercase, value column in `{typography.body-sm}`. 1px `{colors.hairline}` bottom border. Used extensively on product detail pages to expose watt-hours, output ports, dimensions, and weight.

### Footer

**`footer`** — `{colors.dark-surface}` (#231f20) ground, matching the darkest nav states. Column headings in `{colors.on-dark}` with `{typography.title-sm}`; links in `{colors.light-gray}` with `{typography.body-sm}`, shifting to `{colors.primary}` on hover. Deep dark footer creates a distinct close to the page that mirrors the product hardware's dark chassis aesthetic.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen dark drawer; hero text drops to `{typography.display-md}`; `spec-table-row` labels stack above values; `power-indicator` labels drop below bar |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline, secondary items in dropdown; hero uses two-column layout (text left, image right) |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu dropdowns; hero at full 580px height with wide gradient scrim |
| Wide | > 1440px | Max content width locked at 1440px with centered layout; hero scales image fill only, text block width capped to prevent over-wide lines; four-column product grid on collection pages |

### Touch Targets

- All buttons minimum 48px height, matching `button-primary` and `button-secondary` spec
- Nav icons (cart, search, account) minimum 44×44px tap area with padding
- `spec-badge` and `category-badge` are display-only; interactive equivalents padded to 44px where tappable
- `power-indicator` not interactive; read-only display element

### Collapsing Strategy

- Mega-menu navigation collapses to an icon drawer on mobile; `{colors.ink}` full-screen overlay with `{colors.primary}` active indicators
- Spec tables on mobile scroll horizontally or collapse to label-above-value stacks depending on column count
- Hero CTAs stack vertically (primary above secondary) below 744px
- `promo-bar` text truncates with ellipsis on narrow viewports; never wraps to two lines
- Product card image wells maintain square aspect ratio at all breakpoints; card body below image flexes to content

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No design tokens extracted from CSS custom properties or JS-injected theme objects; color list is derived from computed page scan only
- Exact button border-radius values not confirmed from source CSS — `{rounded.xs}` (4px) is inferred from visual inspection of the catalog-utilitarian aesthetic
- Galaxie Polaris weight variants (Book, Medium, Condensed Book) not confirmed to all be loaded — some weights may fall back to the base stack
- Exact nav height (64px) and promo bar height (40px) are estimated; not extracted from layout metrics
- Dark mode or high-contrast variant not observed — unknown whether a theme toggle exists
- Animation and transition tokens (hover durations, skeleton loading behavior) not extractable from static scan
- Icon system (likely Font Awesome 5 Pro based on font stack) not catalogued; glyph selection and sizing conventions undocumented
- Exact `letter-spacing` values for `{typography.button-md}` and `{typography.spec-label}` are estimated — not parsed from computed styles
