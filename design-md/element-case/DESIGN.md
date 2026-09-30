---
version: alpha
name: "Element Case"
source_url: "https://www.elementcase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Machined aluminum has a color of its own — a blue-grey that tends toward the oceanic — and Element Case's palette arrives at the same destination by hex: #226d7a as the load-bearing structural hue anchoring every primary CTA and active UI state, with #22b8d1 introducing a brighter aqua for hover surfaces and accent moments. The brand builds protective cases for premium devices from aerospace-grade materials; the digital interface mirrors that engineering logic through a compressed type stack (Open Sans at weight 400 for reading copy, 700 for display and button labels), no decorative illustration, and a background progression through calibrated near-whites — #e4f5fa as the softest surface, #b0e0e9 as a mid-register teal tint for elevated cards and section divisions. Corners are firm: primary buttons and product cards hold a 4px radius maximum, signaling hard-goods precision over consumer-app softness. The entire brand voltage concentrates into the single teal family — no secondary accent hue from a contrasting family intrudes — which gives #226d7a genuine contrast weight against the pale canvas without requiring an aggressive dark background. Horizontal rules and input borders run in a cooler hairline that retains chromatic discipline rather than drifting into warm beige. Product photography occupies maximum real estate with minimal chrome framing; specification callouts (material grade, drop protection rating, device compatibility marks) appear in uppercase label type at elevated letter-spacing, signaling precision measurement rather than feature marketing. The net effect is closer to a technical instrument's interface than a lifestyle storefront: everything present is structurally load-bearing, nothing is ambient decoration.

colors:
  primary: "#226d7a"
  primary-active: "#1a5560"
  primary-hover: "#22b8d1"
  primary-disabled: "#b0e0e9"
  teal-accent: "#22b8d1"
  surface-teal: "#b0e0e9"
  ink: "#1a1a1a"
  body: "#2d2d2d"
  muted: "#5f6368"
  hairline: "#d8e8ec"
  hairline-soft: "#eef6f9"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#f8fbfc"
  on-primary: "#ffffff"
  error: "#c0392b"
  success: "#1e7a5a"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  label-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: none
    padding: 8px 0
  button-primary-inverted:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(34,109,122,0.10)"
    borderBottom: none
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.surface-card}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    subtitleTypography: "{typography.caption}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.primary}"
    hoverShadow: "0 4px 16px rgba(34,109,122,0.12)"
  product-card-image:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.surface-teal}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
    ctaComponent: button-primary-inverted
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  device-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.muted}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBackground: "{colors.surface-soft}"
    selectedTextColor: "{colors.primary}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"
    selectedRingOffset: 2px
    border: "1px solid {colors.hairline}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.surface-teal}"
  badge-new:
    backgroundColor: "{colors.teal-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    height: 40px
    padding: "0 {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  material-callout:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.surface-teal}"
    rounded: "{rounded.md}"
    headlineTypography: "{typography.label-sm}"
    headlineColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    padding: "{spacing.base} {spacing.lg}"
    iconColor: "{colors.teal-accent}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    buttonColor: "{colors.primary}"
    height: 40px
    buttonWidth: 40px
  rating-stars:
    starColor: "{colors.teal-accent}"
    emptyStarColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-teal}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    headingColor: "{colors.surface-teal}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid #226d7a fill with white uppercase-tracked text at 14px/700, height 48px, 4px radius. Hover state transitions to the brighter aqua #22b8d1; pressed state drops to the deeper #1a5560. Disabled state applies the powder-blue #b0e0e9 fill with muted label text, communicating unavailability without full opacity collapse.

**`button-secondary`** — White fill with a 2px solid #226d7a border and matching teal uppercase label. On hover the fill lifts to #e4f5fa and the border shifts to #1a5560, keeping the interaction strictly within the teal spectrum. Pairs with `button-primary` on PDPs for secondary actions such as Add to Wishlist or Compare.

**`button-ghost`** — No fill, no border, teal label at 13px/600 with letter-spacing. Used for inline navigation actions, "view all" links at the bottom of collection grids, and low-priority filter controls where additional visual weight would compete with product imagery.

**`button-primary-inverted`** — White fill with teal primary label text, employed exclusively on dark #226d7a hero backgrounds where the standard primary CTA would disappear. Maintains the same 4px radius and uppercase tracking for visual consistency across surface contexts.

### Navigation

**`nav-bar`** — White canvas at 64px height with a 1px #d8e8ec bottom border at rest. The Element Case wordmark renders in #226d7a. On scroll the border dissolves and a teal-tinted box shadow (`0 2px 8px rgba(34,109,122,0.10)`) indicates elevation. Category links at 14px/600 in ink color; hover drops to the teal primary. Search and cart icons occupy the right rail with 44×44px touch areas.

### Product Cards

**`product-card`** — White card with 1px #d8e8ec border and 4px radius. The image region uses #f8fbfc to float case renders against a near-white surface. On hover the border upgrades to #226d7a and a teal-tinted shadow lifts the card (`0 4px 16px rgba(34,109,122,0.12)`). Title renders in 16px/600 ink; price in 16px/700 teal primary; device compatibility line in 13px muted caption. When multiple colorways exist, `color-swatch` dots cluster immediately below the product name with a 28px visual diameter and full-radius ring indicator on active.

### Device Selector

**`device-selector`** — A tile-grid or structured dropdown for filtering by phone model, functioning as the primary catalog navigation mechanism. Unselected tiles sit on #f8fbfc with a 1px hairline border. Selection upgrades to a 2px #226d7a border, #e4f5fa fill, and teal-colored option label text. A `label-sm` uppercase label floats above the selector. On mobile this collapses to a full-width native select control; on desktop it appears as a persistent sidebar or above-grid tile row. Because every case SKU is anchored to a specific device model, this component drives page-level content filtering more than any other UI element.

### Hero Banners

**`hero-banner`** — Full-bleed #226d7a teal with white headline at display-xl (36px/700) and a lighter #b0e0e9 subline paragraph. The inverted white CTA button (`button-primary-inverted`) maintains brand consistency without introducing a third color family. Minimum height 480px; product renders are positioned on the right half against the dark teal for maximum contrast.

**`hero-banner-light`** — #e4f5fa near-white with ink headline and muted subline. Used for secondary promotions, seasonal callouts, and category landing pages where multiple product SKUs benefit from a neutral background rather than the full teal immersion.

### Spec & Material Callouts

**`spec-badge`** — Small teal-on-surface-soft pill in uppercase 11px/600 label type with 10px horizontal padding and a 1px #b0e0e9 border. Communicates protection ratings (MIL-SPEC drop height), material identifiers (aerospace aluminum, titanium), and compatibility marks alongside the product title.

**`material-callout`** — Full-width or sidebar panel on #e4f5fa with a 1px #b0e0e9 border and 8px radius. Headline in uppercase teal `label-sm`, body copy in 14px/400. Icon glyphs (shield, drop, lattice) in #22b8d1 anchor each specification row. Deployed on PDPs between the image gallery and add-to-cart region to enumerate drop protection, material sourcing, and warranty terms.

### Badges

**`badge-new`** — #22b8d1 bright teal fill, white uppercase 11px/700 label, 2px radius. Applied to recently launched SKUs in collection grids, positioned top-left over the card image.

**`badge-sale`** — Error red (#c0392b) fill, white label. Used for markdown events and seasonal price reductions.

**`badge-sold-out`** — Muted gray fill, white label. Overlays sold-out colorway swatches and desaturates the card image region to signal unavailability without removing the card from the grid.

### Filters

**`filter-pill`** / **`filter-pill-active`** — Full-radius pills for case type (slim, folio, wallet), material, and price range. Inactive state: 1px hairline border, white fill, body-color uppercase label. Active state fills with #226d7a and inverts text to white. On mobile the pill row scrolls horizontally beneath the search bar.

### Footer

**`footer`** — #226d7a dark teal fill, white body text. Section headings in uppercase `label-sm` at #b0e0e9. Links rest at #b0e0e9 and elevate to full white on hover. A secondary legal strip below the main content holds copyright and policy links at 12px muted caption — the only zone where the ink-on-white hierarchy inverts to white-on-dark.

### Supporting Components

**`search-bar`** — #f8fbfc fill, 1px hairline border upgrading to #226d7a on focus, 40px height, 4px radius. Muted placeholder text; a clear icon appears at the right edge on active input.

**`rating-stars`** — Filled stars render in #22b8d1 accent; empty stars in hairline gray. Count and summary text in 13px muted caption alongside the star row.

**`quantity-selector`** — Decrement/increment buttons in #226d7a against a white center field, each 40×40px. The composite container holds a 1px hairline border and 4px radius; the numeric display uses 16px/600 title-sm.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; device selector collapses to full-width dropdown; hero stacks text above image; nav collapses to hamburger with slide-over drawer; filter pills scroll horizontally; footer stacks into single accordion column |
| Tablet | 744–1128px | Two-column product grid; device selector renders as inline tile row; hero splits 50/50 text and image render; nav shows top-level categories only; filter panel becomes a slide-over drawer triggered by a filter icon |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu dropdowns; device selector appears as persistent left sidebar on collection pages; hero shows full three-panel layout with large product render |
| Wide | > 1440px | Content locked to 1440px max-width and centered on canvas; product grid optionally expands to four columns; hero gains proportional horizontal padding; no new layout zones introduced |

### Touch Targets

- All interactive controls (buttons, swatches, filter pills, nav icons) maintain 44×44px minimum tap area on mobile even when visually smaller
- Color swatches at 28px visual diameter expand to 44px tap area via transparent padding
- Quantity selector buttons hold 40px square with an additional 4px invisible tap expansion
- Device selector tiles use 48px minimum row height in mobile dropdown variant
- Nav links in the hamburger drawer sit at 48px row height with full-width tap zone

### Collapsing Strategy

- Navigation collapses to hamburger at 744px; search bar moves into the drawer header; cart icon persists in the top-right corner
- Device selector transitions from tile grid (desktop) → segmented row (tablet) → full-width native select (mobile)
- Spec badges on PDPs stack vertically below the price line on mobile rather than wrapping inline alongside the title
- Material callout panels shift from sidebar column (desktop) to full-width section between image gallery and add-to-cart on mobile
- Multi-column footer collapses to single-column accordion sections with expand/collapse per link group

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned HTTP 403 during extraction; all color and font data derives from a partial static render rather than the live theme — additional neutral or dark tones used in overlays, modals, or dark-mode surfaces may not be captured
- Font stack (Open Sans, Arial, Roboto) is likely a browser-default fallback chain; the actual brand typeface may be a licensed or custom font loaded via JavaScript that was blocked at extraction time
- No dark-mode token set could be derived; `prefers-color-scheme` behavior and any alternate surface palette are unconfirmed
- Motion tokens (transition duration, easing curves, scroll-triggered animation timing) are inferred from category norms rather than measured from live interactions
- Exact border-radius values for nav mega-menu panels, modal overlays, and tooltip bubbles are estimated from the brand tone rather than measured pixel values
- Pricing display conventions (sale strikethrough weight, compare-at color, currency symbol sizing) not confirmed from live DOM
- Logo lockup proportions, wordmark weight, and minimum clearance zone are inferred; no SVG or raster asset was accessible for measurement
