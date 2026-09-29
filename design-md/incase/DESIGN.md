---
version: alpha
name: "Incase"
source_url: "https://www.incase.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fourteen product colorways — lime (#9fcc4b), chartreuse (#ceea37), hot pink (#e71f7b), coral (#fda262), sky blue (#bfecf5), and nine more — stacked on a near-black (#1c1c1c) and pale ash (#eaebef) structural grid is Incase's sharpest design statement: the protective gear IS the color story. The brand sells precision-fit laptop bags and cases, and its UI treats those colorways as first-class content — large circular swatches, high-saturation product photography on bare white tiles, and a deliberately quiet typographic voice in plain Arial so nothing competes with the objects themselves. The primary CTA voltage is a bold orange-red (#ff5a2b), used sparingly on add-to-cart buttons and promotional highlights; its warmth signals action without clashing against any of the product hues in the catalog. The structural palette is tripartite: near-black (#1c1c1c) for headings and navigation, steel blue-gray (#7e838c) for secondary text and metadata, and ash (#eaebef) as the ambient page fill. Navy (#233246) and medium steel (#40799d) surface in collection banners and layered UI panels, providing depth without resorting to pure black wallpaper. Cards are sharp — {rounded.none} to {rounded.xs} — consistent with a brand that values engineered precision over softened consumer appeal. Navigation is wide and flat, exposing the full product taxonomy through a mega-menu that opens with category headings in tight uppercase Arial. Spacing is deliberate: product grids breathe at {spacing.xxl} column gaps, hero modules occupy full-viewport frames, and section separators fall at {spacing.section}. The overall effect is a storefront that presents like a clean-room specification sheet — exact, stripped, entirely confident that the products require no ornamental framing to earn attention.

colors:
  primary: "#ff5a2b"
  primary-active: "#e03e12"
  primary-disabled: "#f9bfac"
  ink: "#1c1c1c"
  dark-ink: "#0a0a0a"
  body: "#415064"
  muted: "#7e838c"
  muted-soft: "#a3a4a8"
  hairline: "#eaebef"
  hairline-mid: "#c1cac5"
  canvas: "#ffffff"
  surface-soft: "#eaebef"
  surface-card: "#ffffff"
  surface-warm: "#f7e4df"
  on-primary: "#ffffff"
  navy: "#233246"
  steel: "#40799d"
  charcoal: "#34282c"
  ash: "#dfd6d3"
  product-lime: "#9fcc4b"
  product-chartreuse: "#ceea37"
  product-pink: "#e71f7b"
  product-blush: "#fabee8"
  product-coral: "#fda262"
  product-sage: "#99c8b4"
  product-sky: "#bfecf5"
  product-crimson: "#97293c"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  nav-category:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  badge-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    categoryLabelTypography: "{typography.nav-category}"
    linkTypography: "{typography.nav-label}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 0
    gap: "{spacing.sm}"
  product-card-hover:
    border: "1px solid {colors.hairline-mid}"
    shadow: "0 4px 16px rgba(0,0,0,0.08)"
  color-swatch:
    width: 20px
    height: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  hero-module:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 580px
    padding: "{spacing.section} {spacing.xxl}"
  hero-split:
    leftBackground: "{colors.surface-soft}"
    rightBackground: "{colors.canvas}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-md}"
    padding: "{spacing.xxl}"
  collection-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-colorway:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-drawer:
    backgroundColor: "{colors.canvas}"
    inputComponent: "text-input"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    borderLeft: "1px solid {colors.hairline}"
    ctaComponent: "button-primary"
  product-image-rail:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "1px solid transparent"
    thumbnailActiveBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption-bold}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}) rectangle in #ff5a2b with white uppercase Arial at 14px/700 and 0.5px tracking. The zero-radius treatment keeps the orange-red CTA visually flush with the grid and product photography edges. Active state drops to #e03e12; disabled fades to a desaturated coral (#f9bfac) while preserving the uppercase label and correct height.

**`button-secondary`** — Transparent fill with a 2px #1c1c1c outline, same sharp corner, same uppercase label treatment. Appears alongside the primary on PDPs for secondary actions ("Add to Wishlist," "Find in Store"). On dark backgrounds it inverts: white outline, white label.

**`button-ghost`** — Text-only label in #7e838c, no border, no background. Handles low-hierarchy actions — filter resets, "View All" links, pagination controls — without adding visual weight to the page.

### Text Input

**`text-input`** — Thin 1px #eaebef border at rest, transitions to 1px #1c1c1c on focus. No border-radius; fully rectangular. Placeholder in #7e838c at 14px/400. Used in search, newsletter subscribe forms, and all checkout fields.

### Navigation

**`nav-bar`** — 60px white bar with a 1px #eaebef bottom border. Logo sits left; top-level category links in 13px/500 Arial span the center; search, account, and cart icons cluster right. On scroll the bar gains a soft box-shadow rather than changing color, preserving the white canvas identity.

**`nav-mega-menu`** — Full-width dropdown panel below the nav bar, white background, with department headings in 11px tracked uppercase (#1c1c1c or #233246) and product-type links beneath in standard 13px. Columns are separated by whitespace only — no vertical rules. An editorial product image or campaign banner may occupy a right-side panel for featured collections.

### Product Card

**`product-card`** — Square image tile on a #eaebef background, zero radius, with the product name in 14px/700, a color swatch row below, and price in 16px/700. On hover a 1px #c1cac5 border traces the card edge and a subtle 4px shadow lifts it. Color swatches ({color-swatch}) render as 20px circles — up to six visible, overflow collapsed to a "+N" caption in 12px muted gray.

### Hero

**`hero-module`** — Full-bleed #0a0a0a section with a white 40px/700 headline, 16px/400 body copy, and an #ff5a2b primary CTA. On desktop, lifestyle photography bleeds to the right half while text anchors the left 50%. Minimum height is 580px; vertical padding enforces {spacing.section} so the headline never crowds the nav bar or CTA.

**`hero-split`** — Two-column split: a left #eaebef ash panel with a 28px/700 headline and short descriptor, and a right white panel showing an isolated product. Used on category intros and campaign landing pages. Both panels carry {spacing.xxl} internal padding; no dividing border.

### Collection Banner

**`collection-banner`** — Full-width #233246 navy strip with white 28px/700 heading, used as the page header for collection and category listing pages. Image-free — relies on the navy-white contrast for visual authority. Swaps to #ff5a2b background for sale or limited-run events.

### Badges

**`badge-new`** — 4px-radius #ff5a2b chip with 10px uppercase white label at 0.8px tracking, 3×8px padding. Placed top-left corner of product card imagery. Used for new arrivals and recent additions.

**`badge-sale`** — Near-black (#0a0a0a) variant of the same chip geometry, deployed when a product has a markdown price. Label reads "SALE" or the discount percentage.

**`badge-colorway`** — Ash (#eaebef) chip with #7e838c label, used to indicate color counts or limited availability — e.g., "3 Colors" — beneath the product title on cards with no visible swatch strip.

### Color Swatches

**`color-swatch`** — 20px circular chips with a 2px transparent border on rest; the active swatch gains a 2px #1c1c1c ring with an inset gap so the actual color reads clearly. The product palette spans fourteen hues from lime (#9fcc4b) to crimson (#97293c) to sky (#bfecf5), making these chips the primary color-communication layer before photography loads. On mobile, the row is horizontally scrollable if more than four swatches are present.

### Search

**`search-drawer`** — A drop-down bar that replaces the top portion of the page below the nav bar, autofocusing a text-input. Suggestions populate as a flat list — product names, categories, and popular searches — below the input field. No modal overlay; the page dims behind a translucent scrim layer.

### Cart Drawer

**`cart-drawer`** — Right-side slide-in panel with a 1px #eaebef left border. Header "Your Cart" in 16px/700; line items show product thumbnail, name in 14px/400, selected color in 12px muted caption, and price in 16px/700. Subtotal row and primary CTA ("Checkout") pin to the drawer bottom with a 1px #eaebef top border separating them from the items list.

### Product Image Rail

**`product-image-rail`** — Vertical strip of small thumbnails on the left side of the PDP image viewer on desktop. Each thumbnail sits on an #eaebef background; the active thumbnail is outlined in a 1px #1c1c1c border. No border-radius on any tile. Thumbnails are spaced at {spacing.sm} intervals.

### Footer

**`footer`** — Near-black (#0a0a0a) full-width block with four link columns. Column headings in 12px/700 uppercase tracked; links in 14px/400 at #a3a4a8 brightening to white on hover. A thinner sub-footer strip below carries social icons, copyright, and legal links in 12px caption gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger plus icon tray; hero-module stacks text above image full-width; hero-split becomes single column with image on top; color-swatch row truncates at 4 chips with "+N" overflow |
| Tablet | 744–1128px | Two-column product grid; nav-mega-menu becomes full-screen overlay accordion; hero-module maintains side-by-side at reduced headline (display-md 28px); cart-drawer slides up full-width from the bottom |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar and mega-menu panel; hero-module at 580px minimum height; cart-drawer as a 400px fixed right panel |
| Wide | > 1440px | Content capped at 1440px with auto horizontal margins; product grid may expand to five columns; hero photography extends edge-to-edge behind a max-width text container |

### Touch Targets

- Nav icons (search, account, cart) and hamburger: minimum 44×44px tap zone regardless of visual size
- Color swatches: 20px visual chip wrapped in a 36px minimum touch area
- Product card: full card surface including image tile is the tap region
- All primary and secondary CTAs: fixed 48px height

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; mega-menu categories become stacked accordion sections inside a full-height slide-in drawer
- Footer columns collapse to a single accordion list on mobile; column headings become toggle triggers
- Product image rail switches from a vertical left column to a horizontal scrolling thumbnail strip beneath the main image on mobile and tablet
- Search triggers a full-width takeover bar that slides down over the nav content on mobile, rather than dropping below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected; Arial/Helvetica stacks are system defaults — Incase may load a proprietary or licensed typeface via Shopify theme JS that was not captured during extraction
- Meta theme-color is absent; the true mobile browser chrome color cannot be confirmed from extraction
- Button and card border-radius values are inferred from brand aesthetic ({rounded.none}) rather than measured from rendered CSS
- Hover/focus transition durations and easing curves are not available from extraction
- The fourteen product colorways are present in the hex palette but their exact names and SKU-to-hex mappings (e.g., which hex is "Desert Camo" vs. "Cobalt") are unknown
- Dark-mode or alternate seasonal theme presence could not be verified
- The icon system (SVG sprite, icon font, or custom glyph set) used throughout nav, cart, and PDP is unidentified
- Exact mega-menu column counts and featured-panel image dimensions are unconfirmed
