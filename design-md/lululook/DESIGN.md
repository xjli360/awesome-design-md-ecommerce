---
version: alpha
name: "Lululook"
source_url: "https://www.lululook.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-black buttons on a snow-white canvas — Lululook's interface strips away every decorative impulse until all that remains is the product floating in space, much like the aluminum accessories it sells. The primary interaction color (#1c1c1c) is barely distinguishable from pure black, lending every CTA and nav element the weight of machined metal rather than ink on paper. Body text lives at #121212, a half-step lighter that only reveals itself when placed beside a primary button on a bright `{colors.canvas}` white field. Borders and dividers never exceed #dedede — thin hairlines that section content without competing with product photography. Card surfaces pull from #efefef, creating just enough lift against the white ground to define bounding boxes on product grids without resorting to drop shadows. Typography pairs Nunito Sans for display and heading hierarchy with Lato for body and UI text, both geometric sans-serifs whose open apertures echo the rounded aluminum bezels Lululook machines into its iPad stands and MagSafe mounts. Corner radii stay conservative — `{rounded.sm}` on buttons, `{rounded.md}` on cards — never reaching the pill shapes of lifestyle brands; the geometry communicates precision tooling. Spacing is generous at section level (`{spacing.section}` between feature blocks) but tightens inside product cards where spec lists demand density. The overall impression is a system designed to disappear: no gradient, no color accent, no textured background — just typographic hierarchy and whitespace serving as a frame for high-resolution product renders shot on neutral gray seamless paper.

colors:
  primary: "#1c1c1c"
  primary-active: "#000000"
  primary-disabled: "#9a9a9a"
  ink: "#121212"
  body: "#333333"
  muted: "#717171"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-elevated: "#efefef"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-sale: "#cc0000"
  badge-sale-bg: "#fff0f0"
  star-rating: "#ffc107"
  overlay-scrim: "rgba(0,0,0,0.45)"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link-active:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  spec-label:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-compare:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 48px
    height: 52px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "0 {spacing.xl}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 64px
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    hoverBorder: "1px solid {colors.hairline}"
    imageAspectRatio: "1:1"
    imageBackgroundColor: "{colors.surface-elevated}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.surface-elevated}"
    padding: "{spacing.section} {spacing.xl}"
    textAlign: center
    headingTypography: "{typography.display-xl}"
    headingColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
  collection-grid:
    columns: 4
    gap: "{spacing.lg}"
    padding: "0 {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 40px
    textAlign: center
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  spec-table:
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.body}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  image-gallery:
    backgroundColor: "{colors.surface-elevated}"
    rounded: "{rounded.md}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailBorderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.on-dark}"
    linkHoverOpacity: 0.75
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
    buttonWidth: 40px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    overlayBackground: "{colors.overlay-scrim}"
    inputHeight: 48px
    rounded: "{rounded.sm}"
  variant-swatch:
    size: 36px
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    padding: "{spacing.xxs}"

---

## Components

### Buttons

**`button-primary`** — Full-black rectangle with white uppercase tracking at 0.5px. The near-black fill (#1c1c1c) deepens to pure #000000 on hover/press, communicating a subtle but perceptible state shift. Disabled state fades to #9a9a9a, removing all visual authority from the label. Minimum width is 160px on desktop CTAs; on mobile product pages the Add to Cart variant stretches to full-width at 52px height.

**`button-secondary`** — White fill with a 1px primary border and matching uppercase label. On hover the background shifts to `{colors.surface-soft}` and the border tightens to `{colors.primary-active}`. Used for secondary actions like "View Details" or "Compare" where the primary action is already present on the same surface.

**`button-add-to-cart`** — An oversized primary button spanning full container width on product detail pages. Height increases to 52px and horizontal padding expands to 48px to create a prominent tap target. The uppercase label "ADD TO CART" uses `{typography.button-md}` with extra letter-spacing for legibility at larger widths.

### Navigation

**`nav-bar`** — A 64px-tall white bar pinned to the viewport top. Logo sits left, nav links center (Lato 14px regular), and cart/search icons right. A 1px `{colors.hairline-soft}` bottom border separates it from content. On scroll, the border is replaced by a shallow box-shadow for depth without color.

**`announcement-bar`** — A 40px-tall strip above the nav in solid `{colors.primary}` with white bold caption text, typically promoting free shipping thresholds or limited-time discounts. Dismissible via an × icon at the right edge.

### Product Display

**`product-card`** — A vertical card with 1:1 aspect-ratio product image on a #efefef background, followed by title (`{typography.title-sm}`), price (`{typography.price}`), and optional compare-at price in strikethrough muted text. The card has `{rounded.md}` corners and a `{colors.hairline-soft}` border that strengthens to `{colors.hairline}` on hover. No shadow — elevation is communicated purely through border contrast.

**`image-gallery`** — Main product image displayed on a neutral #efefef field with `{rounded.md}` corners. Thumbnail strip below (64px squares, `{rounded.xs}`) with a 2px primary border on the active thumbnail and a lighter 1px hairline on inactive ones. Thumbnails are spaced at `{spacing.sm}`.

**`spec-table`** — Two-column layout for product specifications (Compatibility, Material, Weight, etc.). Labels use `{typography.spec-label}` in body color, values use `{typography.spec-value}` in ink. Rows are separated by a 1px `{colors.hairline-soft}` border with `{spacing.sm}` vertical padding.

**`variant-swatch`** — 36px square selectors for color or model variants. Each swatch has `{rounded.xs}` corners, a neutral hairline border at rest, and a 2px primary border when selected. Small internal padding prevents the swatch content from touching the border.

### Layout & Sections

**`hero-banner`** — Full-width section with a `{colors.surface-elevated}` background, centered heading in `{typography.display-xl}`, and a body-weight subhead below. Vertical padding uses `{spacing.section}`. Typically features a large product render or lifestyle image beneath the text.

**`collection-grid`** — A 4-column grid on desktop with `{spacing.lg}` gaps, collapsing to 2 columns on tablet and 1 on mobile. Grid sits within `{spacing.xl}` horizontal page padding.

**`breadcrumb`** — Caption-sized text links in muted color separated by "/" or ">" glyphs in `{colors.muted-soft}`. The terminal crumb uses `{colors.ink}` to mark current position.

### Footer

**`footer`** — Dark footer in `{colors.primary}` background (#1c1c1c) with white text. Multi-column link layout with bold section headings (`{typography.title-sm}`) and regular body-sm links below. Links reduce to 75% opacity on hover rather than changing color. Section padding matches `{spacing.section}` top and bottom.

### Utility

**`quantity-selector`** — A compact ±1 stepper with a 40px-tall bordered container. Decrement and increment buttons are 40px wide with centered minus/plus glyphs. The number sits in `{typography.body-md}` between them. Border uses `{colors.hairline}`.

**`search-overlay`** — A full-viewport modal triggered from the nav search icon. A dark scrim (`{colors.overlay-scrim}`) covers the page while a white search panel slides down from the top with a 48px input field. Results appear below as product rows with thumbnail, title, and price.

**`badge-sale`** — A small red pill (`{colors.badge-sale}`) with white bold caption text, positioned absolute over product card images. Uses `{rounded.xs}` and tight 2px/8px padding to stay compact.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + cart icon; hero text drops to `{typography.display-md}`; Add to Cart button becomes sticky at bottom of viewport; image gallery switches to horizontal swipe carousel; footer stacks into single column accordion |
| Tablet | 744–1128px | 2-column product grid; nav links remain visible but compress spacing; hero uses `{typography.display-lg}`; product page splits image left (60%) and details right (40%); spec table remains full width below fold |
| Desktop | 1128–1440px | 4-column grid; full horizontal nav with centered links; product page image gallery and details side-by-side at 55/45 split; footer displays all columns inline |
| Wide | > 1440px | Content max-width caps at 1440px and centers; grid gaps widen to `{spacing.xl}`; hero section gains extra vertical padding (`{spacing.section-lg}`); product images can scale larger within their container |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile, even when visual size is smaller
- Quantity selector buttons expand to 48px on touch devices
- Variant swatches gain 4px additional margin on mobile to prevent mis-taps
- Nav hamburger icon touch area is 48×48px despite 24px visual icon size
- Footer accordion headers use full-width 48px-tall tap zones

### Collapsing Strategy

- Navigation links collapse into a slide-out drawer below 744px, with full-height overlay and close button
- Collection filters move from a persistent sidebar to a bottom-sheet modal on mobile
- Product spec tables remain full-width but switch from side-by-side label:value to stacked label-above-value on narrow screens
- Footer columns collapse into expandable accordions with chevron indicators on mobile
- Announcement bar text truncates with ellipsis on very narrow viewports; link remains tappable

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or brand color detected beyond near-black tones — the site may use a color accent (e.g. for sale badges or hover states) that loads dynamically via JavaScript or is only present on specific pages
- Only four hex values extracted (#1c1c1c, #dedede, #efefef, #121212), all achromatic — the badge-sale red (#cc0000) and star-rating gold (#ffc107) are reasonable assumptions for an e-commerce store but were not confirmed in extraction
- No meta theme-color set, so mobile browser chrome color is unknown
- Exact font weights used across the site could not be confirmed beyond family names (Lato, Nunito Sans) — weight assignments are based on typical usage patterns for these typefaces
- Button border-radius, box-shadow values, and transition timings were not available in the static extraction
- Icon system (line weight, size grid, source library) could not be determined
- Specific Shopify theme name and version unknown — component structure is inferred from common Shopify patterns rather than confirmed theme internals
