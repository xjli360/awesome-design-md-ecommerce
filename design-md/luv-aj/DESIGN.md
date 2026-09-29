---
version: alpha
name: "Luv Aj"
source_url: "https://luvaj.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Freight Big Pro in condensed italic at large display weights — a long-descender editorial serif that evokes runway lookbooks rather than jeweler's catalogues — is the single loudest typographic decision on Luv Aj's site, and it sets the tone immediately. This is an LA-rooted brand that treats chain layering and ear-cuff stacking as wardrobe attitude, not occasion accessorizing. The color system resolves almost entirely to two poles: a near-black primary (#121212) that does double duty as ink, CTA fill, announcement bar background, and footer ground, and a clean white (#ffffff) canvas with a single gray hairline (#dedede) drawing zone boundaries without visual weight. No warm accent punctuates the grid — the #1199ff that surfaces in extraction is an ambient Shopify system artifact, not a brand signal, and the editorial photography carries all the warmth the palette omits. Typography pairs freight-big-pro at light or book weights (often italic) with acumin-pro-wide running navigation and button labels in all-caps tracked at 0.08–0.12em; the long-descender serif against the compressed grotesque creates the brand's core visual tension: glamour in the headline, precision in the label. Every structural edge is hard — buttons carry `{rounded.none}`, product cards share the same zero-radius treatment, and inputs are unrounded boxes with a single bottom-rule focus state. Softness is excluded from the structural layer entirely. The announcement bar is a 36px strip of white-on-black tight caps, the only horizontal interruption to the canvas. Product photography holds a strict 4:5 portrait crop — either the jewel isolated on skin or a close editorial frame — keeping the grid clean and letting stacking combinations read clearly at thumbnail size. Quick-add overlays surface as a full-width black fill on card hover, typography reversed to white, consistent with the brand's preference for binary contrast over gradient softening. Campaign hero blocks use freight-big-pro italic at display-xl scale against full-bleed dark or photograph backgrounds, delivering the editorial-magazine energy that connects Luv Aj's product photography to its broader cultural positioning between streetwear editorial and accessible fine jewelry.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#aaaaaa"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#888888"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  system-link: "#1199ff"

typography:
  display-xl:
    fontFamily: "'freight-big-pro', Georgia, serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
    fontStyle: italic
  display-md:
    fontFamily: "'freight-big-pro', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'freight-big-pro', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  editorial-italic:
    fontFamily: "'freight-big-pro', Georgia, serif"
    fontSize: 50px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.4px
    fontStyle: italic
  title-md:
    fontFamily: "'acumin-pro-wide', 'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  title-sm:
    fontFamily: "'acumin-pro-wide', 'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price:
    fontFamily: "'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'acumin-pro-wide', 'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'acumin-pro-wide', 'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'acumin-pro-wide', 'acumin-pro', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase

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
    padding: 14px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    height: 36px
    textAlign: center
    padding: 0 {spacing.lg}
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    padding: 0
  product-card-quick-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 40px
    position: absolute
    bottom: 0
    width: 100%
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    minHeight: 70vh
    textAlign: center
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.editorial-italic}"
    bodyTypography: "{typography.body-md}"
    layout: split-50-50
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
    textAlign: center
  size-swatch:
    defaultBackgroundColor: "{colors.canvas}"
    defaultBorder: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.canvas}"
    selectedBorder: "1px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    height: 36px
    padding: "0 {spacing.md}"
  metal-swatch:
    shape: circle
    size: 20px
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
    rounded: "{rounded.full}"
  search-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayScrim: "rgba(0,0,0,0.3)"
    inputBorder: "1px solid {colors.hairline}"
    resultsTypography: "{typography.body-sm}"
    resultsPriceTypography: "{typography.price}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    hairlineColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Entirely square (`{rounded.none}`), 44px tall, black fill (#121212) with reversed white text in acumin-pro-wide all-caps at 0.12em tracking. Hover deepens to pure #000000. Disabled renders in #aaaaaa, same square form. The hard edge is non-negotiable — rounding is absent across all interactive controls.

**`button-secondary`** — Same square geometry, white fill with a 1px black border and matching typography. Hover fills lightly with `{colors.surface-soft}`. Used for secondary CTAs like "Add to Wishlist" or email capture variants where the primary black block would compete with adjacent content.

**`button-ghost`** — Transparent background, black text, underline, no border or padding. Used for inline text links within product descriptions and editorial blocks where a boxed control would interrupt flow.

### Text Input

**`text-input`** — Rectangular with hard corners (`{rounded.none}`), 44px height, 1px hairline (#dedede) border at rest. Focus state sharpens the border to full ink (#121212) with no shadow or glow — a minimal system that keeps form fields from drawing attention away from imagery. Placeholder text renders in #888888.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline bottom rule. Category links render in acumin-pro-wide 12px uppercase at 0.08em tracking, spaced generously across the center or left-aligned. Logo anchors left. Cart/search icons sit right. No mega-menu depth — categories drop or navigate directly, keeping the nav layer thin.

**`announcement-bar`** — 36px black strip pinned above the nav, white acumin-pro-wide caps in `{typography.title-sm}`. Carries free-shipping thresholds, new-arrival callouts, or sitewide promotion codes. Single line, centered, no close button on most configurations.

### Product Card

**`product-card`** — Zero-radius portrait frame at 4:5 ratio, no border, white background. Product name in acumin-pro 13px, price in acumin-pro 14px below. Hover surfaces **`product-card-quick-add`**: a full-width 40px black overlay pinned to the bottom of the image with white all-caps button text — the card stays clean until interaction, then the dark band appears cleanly without animation jitter.

**`product-badge`** — Flat black rectangle (0px radius), white acumin-pro-wide caps at 11px/0.12em tracking, 4×8px padding. Positioned top-left over the card image for "New Arrival," "Best Seller," or sale signals.

### Hero

**`hero`** — Full-bleed, minimum 70vh, black background with reversed typography. Headline runs freight-big-pro at 60px light italic, conveying editorial campaign energy. Subhead in acumin-pro-wide uppercase title-md. CTA is `button-primary` in reversed form (white fill, black text) or omitted in favor of scroll-down behavior.

**`hero-editorial`** — Split 50/50 layout on desktop: photography left, text right on white canvas. Headline in `{typography.editorial-italic}`, body in acumin-pro 15px. Used for brand story and campaign narrative sections mid-page.

### Collection Banner

**`collection-banner`** — Light gray (`{colors.surface-soft}`) background strip at the top of collection pages. Title in freight-big-pro 38px, subtitle in acumin-pro 15px, centered, generous vertical padding. Not photographic — text-only breathing zone before the product grid.

### Swatches

**`metal-swatch`** — 20px circle showing the metal finish (gold, silver, rose gold). Selected state adds a 2px ink ring with 2px offset gap, giving a clear selection halo without obscuring the swatch color. No label text; tooltip or accessible `aria-label` carries the name.

**`size-swatch`** — Flat rectangular pill at 36px height with hairline border at rest, ink border when selected. Used for ring sizes and adjustable-length selectors. Typography in acumin-pro caption 12px.

### Search

**`search-panel`** — Full-width or side-drawer panel, white background, 30% dark scrim over page content behind it. Input uses the standard `text-input` spec. Results grid shows product thumbnail, name, and price in body-sm and price scales; no rounded treatment on result rows.

### Footer

**`footer`** — Full-bleed black footer mirroring the announcement bar's color inversion. Column headings in acumin-pro-wide title-sm, link lists in acumin-pro body-sm reversed to white. Muted (#888888) hairlines separate columns on wide layouts. Email capture input inverts to white-on-black with ink border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero min-height drops to 55vh; display-xl reduces to ~36px; announcement bar wraps to two lines if needed |
| Tablet | 744–1128px | Two-column product grid; split hero-editorial stacks to single column; nav links may abbreviate or collapse to icon-only |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav; hero at full 70vh; collection banner at full typography scale |
| Wide | > 1440px | Max-width container (~1440px) centered; grid stays at four columns; hero expands image but caps text column width for readability |

### Touch Targets

- All buttons and inputs hold 44px minimum height on mobile
- Metal swatches scale to 28px on touch viewports to meet 44px tap area with spacing
- Nav hamburger and icon targets padded to 44×44px touch area
- Quick-add overlay on mobile is triggered by a dedicated tappable strip rather than hover

### Collapsing Strategy

- Navigation: horizontal link row collapses to hamburger drawer at < 744px; drawer slides from left, links stack vertically with generous padding
- Footer columns: four-column grid stacks to single accordion-style column on mobile, headings become expand/collapse triggers
- Product filters: sidebar filter panel on desktop retracts to a "Filter & Sort" bottom-sheet modal on mobile
- Hero editorial split: 50/50 column layout stacks to image-above, text-below on tablet and mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex values extracted (#dedede, #121212, #1199ff); no mid-tone accent, sale-price red, or promotional color confirmed from live extraction — sale state color assumed to follow a conventional red but is unverified
- #1199ff is almost certainly a Shopify system default for hyperlinks, not a Luv Aj brand color; excluded from primary palette
- Font weights for freight-big-pro and exact pixel sizes for each breakpoint were not extractable — weights assumed from fashion editorial convention (300–400 range for display)
- No confirmed border-radius value for any element; all `{rounded.none}` assignments inferred from brand aesthetic and common Shopify fashion theme patterns
- Hover animation timing, transition easing curves, and micro-interaction specs unavailable from static extraction
- No confirmed color for sale pricing, loyalty/rewards program states, or error messaging
- Exact nav height and announcement-bar height unconfirmed; values are estimates within typical Shopify theme ranges
