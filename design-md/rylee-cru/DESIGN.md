---
version: alpha
name: "Rylee + Cru"
source_url: "https://ryleeandcru.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every collection at Rylee + Cru opens with an illustration — a heron, a sprig of botanicals, a cluster of small folk-art animals rendered in a loose hand that looks borrowed from a well-loved picture book — and the storefront is built to honor that handmade origin rather than suppress it under a generic e-commerce shell. The wordmark is set in a bracketed serif at modest scale, and the ampersand joining the two names carries more brand weight than any other glyph on the page: it names a specific creative partnership at a moment when most children's apparel has consolidated under anonymous corporate abbreviations. Type runs deep charcoal (#313131, the sole confirmed extracted token) against canvas surfaces that lean warm cream rather than clinical white, giving even tight product grids the feeling of a boutique shelf photographed in window light. CTAs are filled with the same dark charcoal, communicating quiet authority rather than urgency; no high-chroma accent color competes for attention anywhere in the layout. Rounded corners are kept moderate throughout — {rounded.sm} on inputs and product cards, {rounded.full} on filter chips and small badges — friendly without tipping into the exaggerated pill shapes common in fast-fashion DTC. Navigation is spare by the standards of a multi-SKU apparel site: gender tabs, age-range selectors, collection names, and a discreet Sale entry do the structural work without a mega-menu. Product cards trust lifestyle photography to carry persuasion, placing price in caption-weight type directly below the image rather than in a colored sticker, keeping browsing unhurried. The brand's illustration motifs — the same birds and botanicals from the prints — recur in editorial section headers and the footer, turning the garment graphic into a recurring identity device. Extraction was blocked by anti-bot gating and returned only one confirmed hex value; all palette tokens and font stacks below are inferred from documented brand assets and representative visual analysis.

colors:
  primary: "#313131"
  primary-active: "#1c1c1c"
  primary-disabled: "#c2b9b3"
  ink: "#313131"
  body: "#4c4440"
  muted: "#8c827c"
  hairline: "#e4dcd6"
  canvas: "#fdf9f4"
  surface-soft: "#f7f1e9"
  surface-card: "#ffffff"
  on-primary: "#fdf9f4"
  blush: "#d4a99a"
  sage: "#8fa88c"
  sand: "#c9b89a"
  sale-red: "#b85c4a"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  label-xs:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    linkTypography: "{typography.title-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    drawerBackgroundColor: "{colors.canvas}"
    drawerWidth: 320px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    rounded: "{rounded.none}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: 0px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: button-primary
    layout: two-column-text-image
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    minHeight: 200px
    padding: "{spacing.xxl} {spacing.xl}"
    illustrationPlacement: right
    illustrationMaxWidth: 360px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    padding: 6px 14px
    height: 32px
  badge-new:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: 3px 10px
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "#ffffff"
    typography: "{typography.label-xs}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  size-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    unavailableTextColor: "{colors.primary-disabled}"
    unavailableTextDecoration: line-through
    width: 48px
    height: 40px
  illustration-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    layout: two-column-text-image
    illustrationMaxWidth: 480px
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: 10px 16px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    padding: "{spacing.lg}"
    ctaComponent: button-primary
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    columnHeaderTypography: "{typography.label-xs}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
    columns: 4

## Components

### Buttons

**`button-primary`** — Solid charcoal (#313131) fill with warm-cream on-primary lettering, uppercase spaced at 0.1em tracking, 48px tall with {rounded.sm}. On hover the fill deepens to `primary-active` (#1c1c1c) with no outline ring; disabled state washes to the dusty `primary-disabled` tone and drops pointer events. On mobile this button runs full-width to fill the single-column layout; on desktop it scales to auto-width following its content.

**`button-secondary`** — Same height and letter-spacing as primary, reversed: warm-cream background with a 1px solid ink border and ink lettering. Used for secondary actions such as "Continue Shopping," filter resets, and size-guide links — always appears below or alongside a primary to maintain clear hierarchy.

**`button-ghost`** — Transparent, no border, inline underline in ink at {typography.button-sm}. Reserved for "See All" expansions within editorial blocks and tertiary navigation links where a bordered button would feel too heavy for the surrounding whitespace.

### Inputs

**`text-input`** — 48px tall, {rounded.sm}, 1px hairline border at rest. Focus upgrades to a 1px solid ink border with no glow or drop-shadow — consistent with the brand's restraint on visual noise. Placeholder in {colors.muted}. Shared across email capture, checkout fields, and the search module.

**`search-bar`** — Slightly shorter variant (44px) used inline in the nav region. Same border and focus behavior as text-input. Icon-only magnifier at the right edge; no explicit submit button — Enter key triggers.

### Navigation

**`nav-bar`** — 64px tall desktop bar with warm-cream background and a 1px hairline bottom border. Navigation links render in {typography.title-sm} (uppercase, 0.1em spacing) and read as low-key editorial labels rather than prominent buttons. Wordmark in {typography.display-sm} (Georgia serif) sits left-aligned; wishlist, search, and cart icons sit right-aligned as icon-only controls. No dropdown mega-menus — collections are flat entries. Mobile collapses to 56px with a hamburger that expands a 320px drawer from the left; drawer links are full-width with {spacing.lg} vertical padding to hit 44px touch targets.

### Product Card

**`product-card`** — Square or portrait image tile with no border-radius on the image itself, maintaining the grid's editorial rigidity. Product name in {typography.body-sm} at normal weight below the image; price on the next line in the same size but rendered in {colors.muted} to create a subtle hierarchy. No add-to-cart affordance at card level — clicking navigates to the PDP. `badge-new` and `badge-sale` overlay the top-left corner of the image as pill chips.

### Hero Banner

**`hero-banner`** — Warm surface-soft field with the collection headline in {typography.display-xl} (Georgia serif, weight 400) and a single body line in {typography.body-md}. CTA is button-primary at auto-width, left-aligned on desktop. Lifestyle photography or brand illustration bleeds in from the right half of the container on desktop; stacks as a full-width image below the text block on mobile. No video autoplay, no countdown overlays.

### Collection Header

**`collection-header`** — Narrower editorial band (min-height 200px) that labels the active collection in {typography.display-md} with a short descriptor in {typography.body-md} below. A brand illustration — typically a motif lifted directly from the season's print — floats to the right. On mobile the illustration is hidden and the text centers to avoid a cramped two-column layout at narrow viewports.

### Filter Chip

**`filter-chip`** — Full pill ({rounded.full}), 32px tall, {typography.label-xs} uppercase. Inactive: canvas background, 1px hairline border, ink text. Active: ink fill, on-primary text — the same binary inversion used on the primary button, scaled down. Chips scroll horizontally as a single row on mobile; on desktop they stack as a left-panel column with {spacing.sm} vertical gap between each.

### Badges

**`badge-new`** — Outlined pill with 1px ink border, ink text at {typography.label-xs}. Appears in the top-left corner of product-card image tiles; never appears alongside a sale badge on the same card.

**`badge-sale`** — Solid-fill pill in {colors.sale-red} with white text at {typography.label-xs}. Appears only on actively discounted products; replaces `badge-new` if both conditions apply.

### Size Chip

**`size-chip`** — 48×40px near-square chip with {rounded.xs} corners. Hairline border at rest, 1px solid ink border when selected. Out-of-stock sizes retain their position in the grid but render in `primary-disabled` text with a line-through rather than being hidden — communicating stock reality rather than masking it.

### Illustration Editorial Block

**`illustration-editorial`** — Full-width surface-soft section, no card chrome or shadow. Two columns: headline in {typography.display-md} and body in {typography.body-md} on the left; a brand illustration — herons, botanicals, folk-animal motifs extracted from the season's print work — on the right at up to 480px wide. Used for brand story sections and mid-page collection introductions. On mobile the illustration column hides and text runs single-column at centered alignment.

### Cart Drawer

**`cart-drawer`** — 400px slide-in panel from the right, canvas background, 1px hairline left border. Section headline in {typography.title-md}. Line items show product thumbnail, name in {typography.body-sm}, and quantity stepper. Subtotal and a full-width button-primary ("Checkout") pin to the bottom of the drawer with {spacing.lg} padding.

### Footer

**`footer`** — Surface-soft background, 1px hairline top border, four desktop columns (Shop, About, Help, Newsletter). Column headers in {typography.label-xs} uppercase; links in {typography.body-sm} at {colors.ink}. Newsletter column contains a stacked label, text-input, and button-secondary. Social icons are minimal line SVGs at 20×20px. On mobile, columns collapse to accordion panels with the column header as the 48px-tall toggle trigger.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to 56px bar with hamburger drawer; hero stacks text above full-width image; filter chips scroll horizontally; button-primary goes full-width; illustration-editorial hides illustration column; footer collapses to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; partial nav links visible before hamburger threshold; hero switches to side-by-side at reduced padding; footer two-column; filter chips remain horizontal scroll row |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with all links and icons exposed; hero full two-column with section-scale padding; filter chips become left-panel column sidebar; footer four-column |
| Wide | > 1440px | Content max-width container (~1360px) centered in viewport; grid stays four columns; section padding scales up proportionally; no structural changes beyond centering |

### Touch Targets

- All interactive chips, icon buttons, and nav links maintain a minimum 44×44px tap area on mobile regardless of visual size
- Size chips are 48×40px with at least {spacing.xs} gap between adjacent chips to prevent mis-taps
- Nav hamburger icon area is padded to 44×44px even when the visible glyph is smaller
- Footer accordion section header rows are padded to 48px touch height
- Filter chip minimum height is 32px but tap area is extended to 44px via padding or pseudo-element

### Collapsing Strategy

- No mega-menu present — collection taxonomy is shallow enough for a flat hamburger drawer list
- Desktop filter sidebar becomes a bottom-sheet modal on mobile, triggered by a "Filter & Sort" button above the product grid
- Product card names truncate to two lines with ellipsis rather than reflowing fully, preserving grid rhythm
- Illustration column in editorial blocks drops out below tablet breakpoint; text reflows to single-column centered
- Cart drawer becomes a full-screen overlay on mobile rather than a 400px panel
- Footer columns collapse to labeled accordion panels; only one panel open at a time

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full palette unconfirmed**: anti-bot gating ("Just a moment...") blocked live extraction; only `#313131` was captured. All colors except `ink` and `primary` are inferred from brand photography and visual references — treat as design approximations requiring live verification.
- **Custom font stack unknown**: extraction returned only OS system-font stacks. Rylee + Cru uses what appears to be a custom or licensed serif for display headings; the Georgia fallback here is a conservative placeholder. Font names and weights must be confirmed against live CSS.
- **Primary CTA color unconfirmed**: it is unclear whether the button fill is the dark charcoal (#313131) or a distinct brand accent. Dark charcoal is used here based on the brand's observed restraint and the absence of any extracted bright accent value.
- **Illustration asset format unknown**: whether brand motifs are inline SVGs, rasterized PNGs, or embedded within product photography could not be determined from extraction.
- **Animation and transition values**: hover durations, page-transition behavior, and scroll-triggered reveals are not extractable from a blocked page.
- **Exact breakpoints unconfirmed**: pixel thresholds above match common headless/Squarespace defaults and are consistent with observed mobile/desktop layout differences, but should be verified in DevTools.
- **Sale badge color** (`sale-red` #b85c4a) is inferred; no promotional color was extracted from the live site.
- **Blush, sage, and sand accent tokens** are inferred from the brand's documented seasonal palette and apparel colorways, not from UI extraction — they may not appear as named CSS custom properties.
