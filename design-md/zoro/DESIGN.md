---
version: alpha
name: "Zoro"
source_url: "https://www.zoro.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  An MRO site that treats typography as infrastructure — Zoro never commissioned a custom typeface or a bespoke icon set. Arial, Helvetica Neue, and Roboto carry every heading, button label, and spec row, and visual weight comes entirely from color density and data compression rather than letterform. The brand's tonal anchor is a tight family of dark teals: #092b34 on the top utility stripe, #0b485b on the primary nav band, #103a49 on hover fills — three shades that stack vertically into a single dark architectural shelf above the catalog. Below that shelf, products sit on a white-to-light-gray canvas with {rounded.xs} corners almost everywhere; there are no pill-shaped buttons, no generous radii, no ornamental detail that would compete with part numbers and SKU strings. Promotional urgency arrives in exactly two signals: a burnt orange (#d24600) reserved for sale pricing and clearance callouts, and an amber (#ffa81b) for featured-deal ribbons — both calibrated to punch loud against the neutral grid the way a warehouse shelf-tag must. Alert states follow Bootstrap's standard palette unchanged — #dff0d8 success greens, #f2dede error pinks, #fcf8e3 warning ambers — unmodified and unbranded, which suits a repeat-buyer base that reads alert copy rather than evaluates its finish. All interactive elements — "Add to Cart" buttons, text links, pagination controls — run in a medium blue (#2071a7) that drops to #286090 on press. Form controls sit at 36–40px height with a 1px border, no shadow, no focused ring flourish beyond a color change. In aggregate, Zoro's visual language is procurement-grade: {spacing.sm} and {spacing.base} dominate the rhythm, catalog grids are configured for maximum SKU density, and every design decision is subordinated to data legibility and CTA placement.

colors:
  primary: "#0b485b"
  primary-active: "#092b34"
  primary-disabled: "#3c6475"
  nav-dark: "#092b34"
  nav-mid: "#103a49"
  teal-deep: "#0e4051"
  teal-wash: "#ebf2f3"
  cta-action: "#2071a7"
  cta-action-active: "#286090"
  cta-action-info: "#5bc0de"
  promo-orange: "#d24600"
  promo-amber: "#ffa81b"
  success: "#428503"
  success-bg: "#dff0d8"
  success-text: "#3c763d"
  warning-bg: "#fcf8e3"
  warning-text: "#8a6d3b"
  error: "#dc2a2a"
  error-bg: "#f2dede"
  error-text: "#a94442"
  ink: "#222222"
  muted: "#696969"
  muted-mid: "#5f5f5f"
  hairline: "#f1f1f1"
  hairline-strong: "#dddddd"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#2071a7"
  link-active: "#286090"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
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
    padding: "10px 16px"
    height: 38px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.cta-action}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "10px 20px"
    height: 40px
  button-add-to-cart-active:
    backgroundColor: "{colors.cta-action-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.cta-action}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.cta-action}"
    padding: "9px 15px"
    height: 38px
  button-secondary-active:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.cta-action-active}"
    border: "1px solid {colors.cta-action-active}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    padding: "8px 12px"
    height: 36px
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.cta-action}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    padding: "8px 12px"
    height: 40px
    submitButton:
      backgroundColor: "{colors.cta-action}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.none}"
      padding: "0 16px"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 44px
    topStripe:
      backgroundColor: "{colors.nav-dark}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      height: 34px
    megaMenuBackground: "{colors.canvas}"
    megaMenuBorder: "{colors.hairline-strong}"
    megaMenuLinkColor: "{colors.ink}"
    megaMenuLinkTypography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.link}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    skuTypography: "{typography.caption}"
    skuColor: "{colors.muted}"
    hoverBorder: "1px solid {colors.hairline-strong}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.10)"
  sale-badge:
    backgroundColor: "{colors.promo-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  promo-badge:
    backgroundColor: "{colors.promo-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.promo-orange}"
    originalPriceTypography: "{typography.body-sm}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
    unitCaptionTypography: "{typography.caption}"
    unitCaptionColor: "{colors.muted}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    border: "1px solid {colors.success-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    border: "1px solid {colors.warning-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error-text}"
    border: "1px solid {colors.error-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.link}"
    separatorColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.muted}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.cta-action}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    accentColor: "{colors.promo-amber}"
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.teal-wash}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    headingColor: "{colors.on-primary}"
    borderTop: "3px solid {colors.primary}"
---

## Components

### Buttons

**`button-primary`** — Teal (#0b485b) background with white text, used for brand-level actions like "Shop All" category entries and promotional calls-to-action in the top-nav and hero zone. Active state deepens to #092b34; disabled state uses the muted teal {colors.primary-disabled}. Height sits at 38px with {rounded.xs} corners — no pill, no softness.

**`button-add-to-cart`** — The primary purchase action runs in the CTA blue (#2071a7), distinct from the brand teal to signal "this triggers a transaction." It drops to #286090 on press. Width is set by content with a 20px horizontal pad; on product detail pages it expands to full container width at mobile breakpoints.

**`button-secondary`** — Outlined blue on white canvas, 1px border matching the {colors.cta-action} fill. Used for "Compare," "Save," and secondary filter actions adjacent to a primary blue button. No fill on rest; {colors.teal-wash} wash on active to indicate selection without a full fill commit.

### Search

**`search-bar`** — A full-width input with a flush blue submit button ({colors.cta-action}) that carries no border radius of its own — it meets the input container edge squarely, forming one combined control. The input field uses a 1px {colors.hairline-strong} border; focus shifts that border to {colors.cta-action}. The search bar is the dominant element in the nav band, occupying approximately 60% of horizontal space on desktop.

### Navigation

**`nav-bar`** — Three horizontal bands form the header shell. The topmost stripe (#092b34, 34px) carries account links, cart, and utility actions in 12px caption text. The primary nav band (#0b485b, 44px) holds the logo, the search bar, and the primary category mega-menu trigger links in white 13px nav-link type. The mega-menu drops on a white canvas with {colors.hairline-strong} column separators and standard {typography.body-sm} link typography in {colors.ink}. On mobile, the entire structure collapses into a hamburger drawer anchored in the same #0b485b.

### Product Cards

**`product-card`** — White surface, 1px {colors.hairline} border, {rounded.xs} corner, {spacing.sm} inner padding. Product image sits in a white zone at the card top; title links appear in {colors.link} blue at 14px bold; SKU and model number render in {colors.muted} caption below the title. Price occupies the largest typographic weight in the card at 20px bold. Hover deepens the border to {colors.hairline-strong} and applies a 0 2px 8px shadow — no transform, no lift.

**`price-block`** — When an item is on sale, the current price renders in {colors.promo-orange} and the struck-through original sits beside it in {colors.muted} at {typography.body-sm}. The unit-of-measure label ("/ EA", "/ PK") renders in caption below at {colors.muted}. Non-sale price uses {colors.ink} throughout with no orange.

### Badges

**`sale-badge`** — Burnt orange (#d24600) background, white text, 11px uppercase bold, 3×6px padding, {rounded.xs}. Overlaid on the top-left corner of product card images. Reserved strictly for clearance and discount price callouts.

**`promo-badge`** — Amber (#ffa81b) background, {colors.ink} text, same type spec as sale-badge. Used for "Featured," "Top Seller," and brand-sponsored placement markers. The amber-on-white-grid contrast is softer than the orange, creating a visual tier between deal urgency and editorial curation.

### Alerts

**`alert-success` / `alert-warning` / `alert-error`** — Bootstrap 3 standard alert blocks applied verbatim with no brand modification: green (#dff0d8 bg, #3c763d text/border), amber (#fcf8e3 bg, #8a6d3b text/border), red (#f2dede bg, #a94442 text/border). All use {rounded.xs}, {typography.body-md}, and {spacing.sm} × {spacing.base} padding. These appear in cart flows, form validation, and availability messaging.

### Wayfinding

**`breadcrumb`** — Plain {typography.body-sm} links in {colors.link} separated by a muted chevron in {colors.muted}; the active (current) page renders in {colors.muted} without underline. No background, no pill, no container — raw inline text flush to the content edge.

**`category-tile`** — Light gray ({colors.surface-soft}) rectangular tiles with 1px {colors.hairline} border, {rounded.xs}, and {spacing.base} padding. Title text at 14px bold in {colors.ink}. On hover, the border color shifts to {colors.cta-action} blue to indicate selection. Laid out in a 4–6 column grid on desktop for the main category browsing surface.

### Hero

**`hero-banner`** — Deep teal (#0b485b) background with white display-xl heading and body-md subhead. Promotional accents use {colors.promo-amber} for inline highlights or ribbon text. The hero runs full-width with {spacing.xxl} vertical padding; CTA buttons inside it use {colors.promo-amber} text or a white-outlined secondary button variant rather than the standard blue, to maintain contrast on the dark field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer in brand teal; search bar moves below logo row and spans full width; breadcrumb truncates to one parent level |
| Tablet | 744–1128px | Two-column product grid; top utility stripe may be hidden; mega-menu replaced with slide-in category drawer; hero banner reduces vertical padding to {spacing.xl} |
| Desktop | 1128–1440px | Three- to four-column product grid; full three-band nav with mega-menu dropdowns; search bar at ~60% width centered in nav band |
| Wide | > 1440px | Content container caps at ~1400px and centers; product grid stays at four columns; extra whitespace absorbed by page margins, not the grid gaps |

### Touch Targets

- All nav links and icon buttons maintain a minimum 44×44px tap target even when the visible element is smaller
- "Add to Cart" button expands to full container width at mobile breakpoints, not a fixed 40px height — minimum 48px on touch
- Badge overlays on product cards do not function as interactive elements; tapping the card image activates the card link

### Collapsing Strategy

- The three-band header collapses top-to-bottom: utility stripe (#092b34) hides first at tablet, then the nav band compresses at mobile into a single-row logo + hamburger
- Category mega-menus convert to accordion panels inside the mobile drawer, preserving the full hierarchy without horizontal scroll
- Product filter sidebar collapses into a "Filter" button that opens a full-screen modal overlay on mobile; filter state persists between panel open/close
- Data-dense tables (specs, product attributes) scroll horizontally with a visible shadow cue on the right edge rather than collapsing columns

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; all type stacks are system fonts (Arial, Roboto, Helvetica Neue). It is possible a custom or licensed web font loads via JavaScript after extraction — none was captured.
- Body paragraph text color is likely #333333 or similar medium dark gray, but only #222222 was extracted from the dark end of the spectrum. The `{colors.ink}` token is set to #222222 as the closest available value.
- Exact button height specifications for desktop vs. mobile variants were not extractable; 38–40px estimates are based on standard Bootstrap 3 button metrics visible in the color palette.
- Icon set appears to use FontAwesome (detected in font stacks) but icon sizing, color, and usage rules were not captured.
- Hover and focus state animations (transition duration, easing) could not be extracted; no transition tokens are defined.
- Precise grid column counts and gutter widths for the product listing page were not captured; column counts in Responsive Behavior are estimated from typical MRO catalog layouts at those breakpoints.
- The `{colors.teal-mid}` (#3c6475) appears in the extracted set but its exact usage context (secondary nav state, tag background, filter chip) is unclear.
- Logged-in vs. guest states may alter nav-bar contents and color treatment; only the guest/unauthenticated header was available for extraction.
