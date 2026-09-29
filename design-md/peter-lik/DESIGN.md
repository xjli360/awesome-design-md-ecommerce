---
version: alpha
name: "Peter Lik"
source_url: "https://lik.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every viewport loads against a void — #070707, the near-absolute black that replicates Lik's physical galleries in Las Vegas, Maui, and Manhattan, spaces where controlled darkness makes each panoramic print appear to emit its own luminescence. Against that darkness, a single warm bronze at #88744a does the structural work that primary colors do in softer e-commerce systems: it marks the add-to-cart CTA, illuminates edition number labels in the manner of museum nameplates, and traces the active state of the gallery location selector; a brighter sibling at #c9a45d handles price display and promotional highlights, the range from deep bronze to warm gold reading like varying angles of light on a physical gilt frame rather than a designed color scale. DIN 2014, the sole typeface, was engineered for signage and wayfinding — optimized for legibility at distance, mapping directly onto a storefront built around prints that routinely exceed 60 inches — and at {typography.display-xl} sizes it carries the panoramic sweep of a canyon or aurora image without competing with it. Wide letter-spacing across {typography.edition-label} and {typography.nav-label} (0.10–0.14em) gives navigational text the sparse, placard quality of a white-cube gallery wall. Buttons and cards hold at {rounded.none} universally; this brand makes no concession to consumer-soft rounding — even text inputs are sharp-cornered. Product cards present images at nearly full bleed against the {colors.canvas} void, withholding price and edition count until hover reveals a translucent overlay, an editorial restraint that treats the photograph as artwork first and commerce second. The PDP splits into an image column held on pure {colors.canvas} and a detail column on {colors.surface-soft} (#121212), with a structured edition-availability block — edition size, remaining prints, bronze-bordered CTA — and a gallery-location selector that bridges digital purchase and physical gallery pickup inline, a dual-channel architecture unique to Lik's gallery-and-web model.

colors:
  primary: "#88744a"
  primary-active: "#7b6943"
  primary-light: "#c9a45d"
  primary-disabled: "#585749"
  gold-warm: "#b08e4e"
  edition-gold: "#8e7b53"
  ink: "#f4f4f4"
  body: "#e0e0e0"
  muted: "#8f8f8f"
  muted-dark: "#636363"
  warm-off-white: "#e7e4df"
  hairline: "#2b2b2b"
  hairline-soft: "#222222"
  canvas: "#070707"
  surface-soft: "#121212"
  surface-card: "#1f1f21"
  surface-raised: "#222222"
  on-primary: "#f8f8f8"

typography:
  display-xl:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: 0.04em
  display-md:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.03em
  display-sm:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.06em
  title-sm:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05em
  body-md:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0.02em
  caption:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  edition-label:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-label:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  price-display:
    fontFamily: "'din-2014', 'DIN 2014', sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-dark}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.on-primary}"
    accentColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    paddingBottom: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary-light}"
    editionTypography: "{typography.edition-label}"
    editionColor: "{colors.primary}"
    hoverOverlay: "rgba(7,7,7,0.45)"
  hero-panoramic:
    backgroundColor: "{colors.canvas}"
    imageOverlay: "linear-gradient(to bottom, rgba(7,7,7,0) 55%, rgba(7,7,7,0.88) 100%)"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 90vh
    paddingX: "{spacing.xxl}"
    paddingBottom: "{spacing.section}"
  edition-badge:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.edition-label}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  sold-out-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.edition-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  gallery-locator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.edition-label}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  search-overlay:
    backgroundColor: "rgba(7,7,7,0.97)"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    resultTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.none}"
    backdropBlur: none
    border: "none"
  lightbox-panel:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.canvas}"
    textColor: "{colors.body}"
    metaTypography: "{typography.caption}"
    titleTypography: "{typography.title-md}"
    closeButtonColor: "{colors.muted}"
    overlay: "rgba(7,7,7,0.96)"
  pdp-layout:
    backgroundColor: "{colors.canvas}"
    imageColumnBackground: "{colors.canvas}"
    detailColumnBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary-light}"
    editionBlockBorder: "1px solid {colors.hairline}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.xxl}"
  edition-availability-block:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.edition-label}"
    labelColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.caption}"
    navTypography: "{typography.nav-label}"
    accentColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A flat, sharp-cornered rectangle in bronze #88744a carrying uppercase DIN 2014 at 0.14em tracking, 48px tall. No border-radius anywhere on the system; the corners are as hard as a gallery frame. On hover the fill deepens to the `primary-active` value (#7b6943); disabled state uses #585749 with muted text to signal unavailability without visual noise.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and `{colors.ink}` label. Used for secondary gallery actions such as "View Gallery" alongside a primary "Add to Cart." The bronze outline maintains brand warmth without the filled weight of the primary, creating a clear but subordinate hierarchy.

**`button-ghost`** — Transparent fill, `{colors.hairline}` border (#2b2b2b), muted text. Appears in filter panels, sorting controls, and less-prominent navigation actions. It recedes visually against the dark canvas while remaining accessible.

### Text Input

**`text-input`** — Sharp-cornered, `{colors.surface-card}` fill (#1f1f21), 1px `{colors.hairline}` border that transitions to `{colors.primary}` on focus. Placeholder text in `{colors.muted-dark}` (#636363) against the near-black surface maintains adequate contrast. Used in email subscription, gallery location search, and newsletter forms.

### Navigation

**`nav-bar`** — 72px tall, `{colors.canvas}` background, with a 1px `{colors.hairline}` bottom rule that separates it from the hero image below. Nav links use `{typography.nav-label}` (12px uppercase DIN, 0.10em tracking), creating a sparse, typographic stillness across the top of every page. The logo sits centered or left-aligned; a cart icon and gallery-finder link anchor the right end. On scroll, the bar remains pinned without changing background opacity — the darkness is already absolute.

### Product Card

**`product-card`** — Full-bleed image at a 4:5 aspect ratio, no border, no shadow. Title and price appear below the image in a minimal two-line block; edition status (`{typography.edition-label}` in `{colors.primary}`) appears below price. On hover, a semi-opaque dark overlay (rgba 7,7,7, 0.45) fades in over the image and a secondary CTA — "Quick View" or "Add to Cart" — appears centered in `{typography.button-md}`. Sold-out cards show the `sold-out-badge` in `{colors.muted}` and suppress the hover CTA.

### Hero

**`hero-panoramic`** — Full-viewport-width image (min-height 90vh) with a gradient overlay that fades from transparent at 55% to near-black at the bottom, anchoring the headline and CTA without obscuring the sky or upper image field. Title runs at `{typography.display-xl}` (56px, weight 300) in `{colors.on-primary}`; subtitle at `{typography.title-md}`. The CTA uses `button-primary` inline at the bottom of the hero column. No carousel indicators, no auto-rotation — a single commanding image per hero.

### Edition Badge and Availability Block

**`edition-badge`** — A 1px `{colors.primary}` bordered label using `{typography.edition-label}` uppercase tracking, reading "LIMITED EDITION" or "1/950". Appears on product cards and at the top of the PDP detail column. When an edition is sold out, it converts to `sold-out-badge` with `{colors.hairline}` border and `{colors.muted}` text.

**`edition-availability-block`** — A structured panel inside the PDP detail column. Three rows: edition total, prints remaining, and a "Request Information" link for near-sold-out editions. Uses `{typography.edition-label}` for keys and `{typography.body-sm}` for values. The block sits above the `button-primary` CTA and below the price, making edition scarcity legible before purchase.

### Gallery Locator

**`gallery-locator`** — A surface panel in `{colors.surface-soft}` with a 1px `{colors.hairline}` top rule. Presents a list of physical gallery cities (Las Vegas, Maui, Key West, etc.) as selectable locations with a "Visit a Gallery" CTA in `button-secondary`. This component bridges digital browse and in-person acquisition — a structural element with no direct analogue in other photography print shops. Labels use `{typography.edition-label}` uppercase, values use `{typography.body-sm}`.

### Search Overlay

**`search-overlay`** — A near-full-screen overlay at rgba(7,7,7,0.97) that slides down from the nav on search icon activation. The input field renders at `{typography.display-md}` size (36px) rather than a typical 16px, making query typing feel like composing a title rather than filling a form. Results appear below as a two-column grid of matching prints. No border-radius, no shadow cards — just image thumbnails, titles, and edition labels on the black field.

### Lightbox Panel

**`lightbox-panel`** — A full-screen dark overlay (rgba 7,7,7, 0.96) that presents the selected print at maximum viewport size. A slim right drawer shows title (`{typography.title-md}`), medium and size options, price in `{typography.price-display}`, and the `button-primary` CTA. Metadata (location, capture date, edition) appears in `{typography.caption}` below. Close button is a minimal × in `{colors.muted}` at the top right.

### Footer

**`footer`** — `{colors.surface-soft}` background (#121212) with a 1px `{colors.hairline}` top rule. Navigation columns use `{typography.nav-label}` for headings, `{typography.caption}` for links. The bronze `{colors.primary}` appears only on hover states for footer links, not as static color. Newsletter input uses `text-input` inline with a `button-primary` submit. Legal copy runs at `{typography.caption}` in `{colors.muted}`, maximum restraint.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 1-col product grid; nav collapses to hamburger + centered logo + cart icon; hero text centers, display-xl scales to 32px; edition-availability-block stacks below full-width image; gallery-locator moves to a dedicated section below PDP |
| Tablet | 744–1128px | 2-col product grid; nav shows logo + 3 primary links + icons; PDP image and detail stack vertically with detail column at full width; hero title at 44px |
| Desktop | 1128–1440px | 3-col product grid; full nav with all categories; PDP splits 58/42 image/detail side-by-side; hero at full 56px display-xl |
| Wide | > 1440px | 4-col product grid within a max-width container; canvas fills edge-to-edge beyond container; hero image scales with object-fit cover at full bleed |

### Touch Targets

- All nav icons and hamburger minimum 44×44px tap area
- Product card hover states convert to tap-to-reveal on mobile (one tap shows overlay CTA, second tap activates)
- Gallery locator city selection items minimum 48px height
- Edition badge and availability block text sized ≥ 11px with sufficient spacing to avoid mis-tap

### Collapsing Strategy

- Typography scales: `{typography.display-xl}` steps from 56px desktop → 44px tablet → 32px mobile
- PDP layout transitions from two-column side-by-side (desktop) to stacked single-column (tablet/mobile), detail column rising to full width beneath the image
- Gallery locator collapses from inline sidebar widget to full-width accordion section below primary purchase CTA on mobile
- Search overlay remains full-screen at all breakpoints; input font size reduces from 36px to 22px on mobile to prevent zoom
- Footer columns (4-col desktop) collapse to 2-col tablet, single-col accordion on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weight set licensed for din-2014 (light/300, regular/400, medium/500, bold/700 availability unconfirmed from extraction)
- Animation and transition timing for hero parallax, product card hover overlays, and lightbox open/close — no motion spec extractable from static scrape
- Grid column counts and gutter widths for the collection grid — 3-col and 4-col values above are inferred from convention, not extracted
- Mobile navigation pattern (drawer vs. full-screen overlay vs. bottom sheet) not confirmed
- Lazy-loading treatment for high-resolution panoramic images — skeleton screen color and shimmer pattern unknown
- Cart interaction model (slide-out drawer vs. dedicated cart page) could not be confirmed
- Exact breakpoints used internally by the Shopify theme — the responsive table above uses standard DTC breakpoints, not extracted values
- Whether any pill-shaped (`{rounded.full}`) elements exist anywhere in the system (no evidence found, but cannot rule out promo banners or cookie consent)
- Video autoplay behavior on hero sections (some Peter Lik gallery pages use cinemagraph or video hero)
