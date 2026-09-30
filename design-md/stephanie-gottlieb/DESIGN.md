---
version: alpha
name: "Stephanie Gottlieb"
source_url: "https://www.stephaniegottlieb.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hot pink—#fe3981—used as the permanent CTA voltage on a fine jewelry site is a deliberate aesthetic rupture: where the sector defaults to pearl-cream or champagne reserve, Stephanie Gottlieb deploys this saturated rose as the full interaction infrastructure, carrying every primary button, cart action, and editorial focal point against near-black (#121212) ink on a white canvas. ChromaticGeometricLight handles display-register headlines at thin weights (300), its circular letterforms and open counters structurally echoing the round-brilliant diamonds the brand specializes in — at 60px the strokes reduce to pure geometric silhouette, engineered to recede behind product photography rather than compete with it. Jost covers the functional layer: navigation, button labels, filter chips, and category markers all set uppercase in tracked Jost 400–500, introducing clean mechanical contrast that distinguishes interaction affordances from the ChromaticGeometric editorial voice. MinSansBook grounds body copy and price display in book-weight legibility.

  The surface architecture is spare minimalism anchored at two close gray values — #e6e6e6 as the primary hairline, #dedede as a secondary divider — that create card separation and section rhythm without adding visual mass. No decorative shadows, no ornamental rules; whitespace and type-scale steps carry all hierarchy. Corner geometry is applied deliberately: filter chips and search fields use {rounded.full} pill shapes, while product cards and primary CTAs hold {rounded.none} square edges that suggest gemological precision rather than generic consumer softness. A secondary red (#e32c2b) appears narrowly: promotional flags, sale badges, and low-stock indicators, warm enough to read as urgency rather than error state.

  The personalization equity — bespoke commissions, engraving, custom stacking — surfaces as a full-bleed #fe3981 editorial band that uses the primary color as a section background rather than a button fill, making the brand's CTA signal double as identity broadcast. At every breakpoint, photography is the layout engine; the entire typographic and color system exists to amplify stone and light, with the hot pink doing the singular job of telling the viewer exactly where to act.

colors:
  primary: "#fe3981"
  primary-active: "#d4195f"
  primary-disabled: "#fca8c2"
  accent-red: "#e32c2b"
  ink: "#121212"
  body: "#3d3d3d"
  muted: "#8a8a8a"
  hairline: "#e6e6e6"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-muted: "#eeeeee"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'ChromaticGeometricLight', 'ChromaticGeometricRegular', sans-serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ChromaticGeometricLight', 'ChromaticGeometricRegular', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.14
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'ChromaticGeometricRegular', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.22
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'MinSansBook', 'Jost', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'MinSansBook', 'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  price:
    fontFamily: "'MinSansBook', 'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  label-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.10em
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
    rounded: "{rounded.none}"
    padding: "13px 32px"
    height: 46px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: "12px 31px"
    height: 46px
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.canvas}"
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.canvas}"
    padding: "12px 31px"
    height: 46px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: "1px"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    placeholderColor: "{colors.muted}"
    focusBorderColor: "{colors.ink}"
    errorBorderColor: "{colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    logoPlacement: center
    activeAccentColor: "{colors.primary}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    categoryTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    quickshopBarBackgroundColor: "{colors.primary}"
    quickshopBarTextColor: "{colors.on-primary}"
    quickshopBarTypography: "{typography.button-sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    minHeight: "600px"
    layout: "split image-left text-right"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-bespoke:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.canvas}"
    activeBorder: "1px solid {colors.ink}"
  search-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    inputBorderColor: "{colors.hairline}"
    inputRounded: "{rounded.none}"
    resultTitleTypography: "{typography.body-sm}"
    resultPriceTypography: "{typography.price}"
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.3
  personalization-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.canvas}"
    ctaTextColor: "{colors.ink}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  swatch-selector:
    size: "22px"
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.canvas}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Flat #fe3981 fill, no border-radius, uppercase Jost tracked at 0.12em. Hover shifts to `primary-active` (#d4195f); disabled washes to `primary-disabled` (#fca8c2) with `not-allowed` cursor. Powers every Add to Cart, Book Appointment, and checkout-forward action across the site.

**`button-secondary`** — 1px ink-bordered outline on white canvas. On hover, inverts to full ink fill with canvas text, signaling equal-weight alternative actions. Appears in dual-CTA hero rows and product-detail supplementary links.

**`button-secondary-on-dark`** — Reversed outline treatment for use over the pink `personalization-strip` and the dark footer; canvas border and text on a transparent background, same uppercase Jost geometry.

**`button-text-link`** — 11px Jost underlined, no fill or border. Used for low-priority secondary actions and inline editorial navigation where a full button would add visual weight.

### Text Input

**`text-input`** — Sharp-cornered (no radius), single 1px `#e6e6e6` border that sharpens to full `#121212` on focus. Placeholder copy rendered in `#8a8a8a`. Error state swaps the border to `#e32c2b`. Applied uniformly across newsletter signup, checkout address fields, and search input.

### Navigation

**`nav-bar`** — White 68px bar with the brand wordmark centered, uppercase Jost 12px links left-aligned, and a 1px `#e6e6e6` bottom rule. Active or hovered nav items receive a `{colors.primary}` underline accent rather than a background fill — the pink appears functionally without dominating chrome. Collapses to hamburger-left / logo-center / cart-right icon layout on mobile.

**`category-nav`** — Secondary horizontal 48px strip below the main bar on collection pages. Muted Jost nav labels (#8a8a8a) activate to full ink with a 2px `{colors.primary}` bottom border on hover/selection. Overflows to horizontal scroll on mobile rather than wrapping.

### Product Card

**`product-card`** — Full-bleed portrait image at 4:5 aspect ratio, no card shadow, no border-radius. Product title in MinSansBook 13px beneath the image, price in the same typeface 14px. On hover, a quick-add bar translates up from the card's bottom edge in `{colors.primary}` fill with white uppercase Jost CTA text. Badge overlays (`badge-sale`, `badge-new`, `badge-bespoke`) float top-left, all sharp-cornered.

### Hero Banner

**`hero-banner`** — Split composition at 55% image / 45% text on desktop, ChromaticGeometricLight display headline at 60px weight 300 carrying the right column. CTA is `button-primary`. Minimum 600px height; on mobile the layout stacks to full-width image above text, with heading scaling down to `{typography.display-md}`.

### Badges

**`badge-sale`** — Sharp red (#e32c2b) label, 10px uppercase Jost, 3px/8px padding. Positioned over the product image top-left corner for immediate scannability in grid view.

**`badge-new`** — Identical geometry as `badge-sale`, filled in brand pink (#fe3981) for new-arrival callouts.

**`badge-bespoke`** — Ink-filled version marking custom, one-of-a-kind, and made-to-order pieces; white text on #121212 ground.

### Filter Chips

**`filter-chip`** — Full-radius pill bordered in `#e6e6e6` on white. On selection, inverts to full ink background with canvas text and an ink border. Used in collection sidebar and mobile filter drawer for metal type, stone color, price band, and ring size.

### Search

**`search-drawer`** — Overlay panel from top-right on desktop, full-width on mobile. Square-cornered input with hairline border; predictive results list product thumbnail, title in `body-sm`, and price. Background scrim behind drawer at `#121212` 30% opacity.

### Personalization Strip

**`personalization-strip`** — Full-bleed #fe3981 editorial section using the primary as a background fill rather than a button accent. ChromaticGeometricRegular white headline, MinSansBook body paragraph, `button-secondary-on-dark` CTA. Appears once per homepage between product grid rows to signal bespoke service offerings.

### Swatch Selector

**`swatch-selector`** — 22px circular swatches for metal color (yellow gold, rose gold, white gold, platinum). Inactive state: 1px `#e6e6e6` ring. Active state: 2px `#121212` ring with a 2px transparent offset gap, creating a clear selection halo.

### Footer

**`footer`** — Full-width #121212 dark footer, four-column link grid on desktop. Column headings in uppercase Jost 13px 500-weight (canvas color); links in 11px Jost 400, `#8a8a8a` muted default with canvas on hover. Collapses to single-column stacked accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger (left) + centered logo + cart icon (right); hero stacks image-top / text-below; product grid 2-col; `category-nav` scrolls horizontally; filter drawer replaces sidebar |
| Tablet | 744–1128px | Horizontal nav fits in bar; hero transitions to side-by-side at ≥ 900px; product grid 3-col; filter sidebar appears at ≥ 960px |
| Desktop | 1128–1440px | Full nav with all category links visible; 4-col product grid on collection pages; hero at full 600px min-height |
| Wide | > 1440px | Content constrained to ~1440px max-width centered; hero photography scales, text column holds max-width ~560px |

### Touch Targets

- All button heights minimum 44px
- Nav items span the full 68px nav-bar height as tap zone
- Filter chips minimum 36px height with 8px vertical padding
- Swatch selectors: 22px visual, 36px touch target via negative margin
- Quick-add bar spans full card width for reliable mobile tap across the image
- Breadcrumb links minimum 36px tap height via padding

### Collapsing Strategy

- Desktop sidebar filters become a full-screen bottom-sheet drawer on mobile
- Four-column footer collapses to stacked accordion at < 744px (one column, headings as toggle triggers)
- `category-nav` scrolls horizontally on mobile rather than wrapping to multiple lines
- Hero split layout stacks image-first / text-second at < 744px; ChromaticGeometric headline scales to `{typography.display-md}`
- Main nav condenses to icon bar at < 744px; full link tree lives in an off-canvas left drawer

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- White canvas (#ffffff) was not in the top-6 extracted colors but is an obvious inference; consistent with Shopify theme defaults
- `surface-soft` (#f5f5f5) and `surface-muted` (#eeeeee) are derived values — no lighter surface tokens appeared in the extraction
- `body` text color (#3d3d3d) is derived; not present in extracted palette
- `primary-active` (#d4195f) and `primary-disabled` (#fca8c2) are computed from extracted primary #fe3981; exact brand hover/disabled spec unconfirmed
- ChromaticGeometric is a custom or licensed display typeface; exact OpenType feature set, weight axis range, and optical sizing breakpoints not determinable without font file access
- MinSansBook specifics (numeric weight, precise letter-spacing values) unconfirmed — treatment derived from stack position in extracted font list
- Exact product-card border-radius not confirmed from extraction; {rounded.none} assumed based on the overall angular design language
- Animation and transition durations for quick-add hover, search overlay, and filter drawer slide are not extractable via static scrape
- Bespoke and custom-order multi-step flow UI (stone selection, engraving configurator) not accessible from public page scrape
- Mega-nav depth and sub-category structure unconfirmed
- Meta theme-color not set; no dark-mode color mapping defined
- Social proof UI (review stars, UGC grid) styling not confirmed
