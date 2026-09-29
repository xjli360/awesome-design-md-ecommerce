---
version: alpha
name: "Article"
source_url: "https://www.article.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Coral (#ff6458) burns like a lit match against a field of architectural neutrals — that single warm accent does all the heavy lifting on a site otherwise governed by restraint. Article's digital presence mirrors the showroom philosophy of its furniture: generous negative space, photography scaled to breathe, and typography that steps back so oak grain and linen weave sell themselves. The type system pairs a proprietary "article-font" display face with Proxima Nova for body and UI text, running lighter weights than most e-commerce competitors; headings rarely exceed semi-bold, trusting hierarchy to come from scale and spacing rather than stroke width. Cards and containers sit at `{rounded.sm}` or `{rounded.xs}` — just enough softness to avoid clinical rigidity without veering into playful territory. The background alternates between pure white `{colors.canvas}` and a barely-warm gray `{colors.surface-soft}` (#f2f2f2) that groups product grids into visual rooms. Navigation is flat and unadorned: no underlines, no colored backgrounds, just `{colors.ink}` (#141414) text at `{typography.nav-link}` weight with a coral underline on active state. Product cards rely on oversized imagery (aspect-ratio locked at 4:5), a single `{typography.title-md}` product name, and price in `{typography.body-md}` — dimensions and material tags appear only on hover or in a secondary line at `{typography.caption}` weight. The sale system layers a gold badge (#e6b94f) and a green in-stock dot (#3cb064) as the only departures from the coral-and-gray world; these semantic colors are used sparingly and never decoratively. Buttons are rectangular with `{rounded.xs}` corners and generous vertical padding, giving CTAs a slab-like solidity that echoes the straight lines of mid-century furniture legs. The overall rhythm is slow and spacious — `{spacing.section}` between content blocks, `{spacing.lg}` gutters in product grids — letting each piece of furniture command attention the way it would on a concrete gallery floor.

colors:
  primary: "#ff6458"
  primary-active: "#cc5046"
  primary-disabled: "#ffe0de"
  primary-hover: "#ffa29b"
  ink: "#141414"
  ink-secondary: "#2e2e2e"
  body: "#626262"
  muted: "#828282"
  muted-soft: "#a7a7a7"
  hairline: "#cacaca"
  hairline-soft: "#ececec"
  border-light: "#c2c2c2"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-subtle: "#f8f8f8"
  surface-muted: "#f3f3f3"
  surface-divider: "#eeeeee"
  surface-hover: "#efefef"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#3cb064"
  sale: "#e6b94f"
  scrim: "rgba(0, 0, 0, 0.5)"

typography:
  display-xl:
    fontFamily: "'article-font', 'Proxima Nova', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'article-font', 'Proxima Nova', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'article-font', 'Proxima Nova', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'article-font', 'Proxima Nova', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-category:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Proxima Nova', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 15px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 48px
    height: 56px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.surface-divider}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-category-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-category}"
    padding: "{spacing.xl} {spacing.xxl}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4:5"
    padding: 0
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.primary}"
  product-card-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  product-card-swatch-active:
    border: "2px solid {colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
    contentMaxWidth: 1400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "3:4"
    overlay: "linear-gradient(transparent 50%, rgba(0,0,0,0.35))"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-bestseller:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  stock-indicator:
    color: "{colors.success}"
    typography: "{typography.caption}"
    dotSize: 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    iconColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink-secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
  image-gallery:
    rounded: "{rounded.none}"
    thumbnailSize: 72px
    thumbnailGap: "{spacing.sm}"
    thumbnailBorderActive: "2px solid {colors.ink}"
    thumbnailBorderDefault: "1px solid {colors.hairline-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
    buttonColor: "{colors.ink}"
  toast-notification:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"

---

## Components

### Buttons

**`button-primary`** — A solid coral (#ff6458) rectangle with 4px radius and bold white text, used for all high-intent actions: "Add to Cart," "Shop Now," "Continue." On hover the fill darkens to #cc5046 with a subtle 150ms ease transition. Disabled state bleaches to #ffe0de with white text remaining but pointer-events removed. The slab proportions (48px height, 32px horizontal padding) give the button visual weight without relying on rounded softness.

**`button-secondary`** — A 1px solid ink (#141414) outline on white with bold dark text, used for lower-priority actions like "View Details" or "Save." On hover the background tints to #f2f2f2 while the border remains solid. Maintains the same 48px height and 4px radius as primary, creating visual alignment when buttons sit side-by-side on product pages.

**`button-tertiary`** — Text-only with underline decoration in ink color; no background, no border. Used inline for "Learn More" links and expandable content triggers. Hover state removes underline and shifts color to body gray.

**`button-add-to-cart`** — Full-width variant of the primary button with extra vertical breathing room (56px height) and increased horizontal padding. Sits alone in the product detail sticky bar on mobile and below the price block on desktop.

### Navigation

**`nav-bar`** — A minimal 64px-tall white bar with a thin divider at the bottom. The Article logotype sits left in the proprietary display font; category links ("Living," "Bedroom," "Dining," "Outdoor," "Office") run center-aligned in semi-bold 14px Proxima Nova. Cart icon and account icon anchor right. On scroll, the bottom border swaps for a subtle box-shadow.

**`nav-category-dropdown`** — Full-width mega-menu panel that slides down on category hover. White background, organized in a multi-column grid with collection thumbnails at 120px square. Subcategory headings use `title-md`, individual links use `body-sm`. Panel exits with a 200ms opacity fade.

### Product Cards

**`product-card`** — Zero-radius container with no visible border; the image itself defines the card boundary. Product image at 4:5 aspect ratio fills the top region with object-fit cover. Below the image: product name in `title-md`, material/color descriptor in `body-sm` muted, then price in `price` weight. Color swatches display as 20px circles with a 2px border, active swatch gaining an ink-colored ring. On hover, the image crossfades to an alternate lifestyle angle.

**`product-card-sale-price`** — When a sale is active, the original price renders in `body-sm` with strikethrough and muted color, while the new price renders in `price-sale` typography colored coral (#ff6458). A `badge-sale` floats at the top-left corner of the product image.

### Hero

**`hero-banner`** — Full-bleed container with a large lifestyle photograph and text overlay. Minimum height 560px, content limited to 1400px max-width with section-level padding. Headline uses `display-xl` in dark ink over a light image or white text over a dark image. A single coral CTA button sits below the headline with `spacing.lg` gap. The image zooms subtly (scale 1.02) over 8 seconds for ambient motion.

### Badges

**`badge-sale`** — Uppercase 11px bold text in white on a coral background with 4px radius. Positioned absolute at top-left of product card images with 12px inset.

**`badge-new`** — Same structure as sale badge but ink-colored background (#141414) with white text.

**`badge-bestseller`** — Gold (#e6b94f) background with dark text, signaling popularity without the urgency of the sale badge.

### Search

**`search-bar`** — A rounded-sm (#f2f2f2) input field with a search icon left-aligned in muted gray. Expands to full viewport width on mobile with a modal overlay; on desktop it sits in the nav bar and expands inline to ~400px on focus. Placeholder text in `body-md` muted. Results appear in a dropdown panel below, matching `nav-category-dropdown` shadow treatment.

### Filters

**`filter-chip`** — Small rectangular pills with 1px hairline border and body-md text, used for size/color/material filters in collection pages. Active state inverts to ink background with white text. Chips wrap in a horizontal scroll container on mobile.

### Image Gallery

**`image-gallery`** — Product detail image viewer with a main image (no border radius) and a vertical strip of 72px square thumbnails to the left on desktop, horizontal strip below on mobile. Active thumbnail gets a 2px ink border; others have a soft 1px hairline. Main image supports pinch-zoom on touch devices and a loupe on desktop hover.

### Footer

**`footer`** — Dark (#2e2e2e) full-width section with white text organized in 4-5 columns: product categories, company info, customer service, and social links. Column headings in `title-sm` bold white, links in `body-sm` at reduced opacity (0.7) that brightens to 1.0 on hover. Newsletter signup input at bottom with a coral submit button.

### Toast & Notifications

**`toast-notification`** — A dark ink-colored chip with white text and sm radius that slides up from the bottom-right (desktop) or bottom-center (mobile). Used for "Added to cart" confirmations and stock alerts. Auto-dismisses after 4 seconds with a fade-out.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-out drawer; hero text drops to `display-md`; add-to-cart becomes sticky bottom bar; filters collapse into a bottom sheet; image gallery switches to horizontal swipe carousel |
| Tablet | 744–1128px | Two-column product grid; nav remains full but category dropdown triggers on tap; hero maintains full-bleed with `display-lg` headline; filter chips scroll horizontally |
| Desktop | 1128–1440px | Three-to-four column product grid with `spacing.lg` gutters; full mega-menu navigation; product detail uses 60/40 image-to-info split; image gallery with vertical thumbnail strip |
| Wide | > 1440px | Content max-width caps at 1400px, centered; product grid holds four columns; additional whitespace absorbed by canvas margins; hero images scale without cropping |

### Touch Targets

- All interactive elements maintain minimum 44px touch target on mobile, even when visually smaller
- Product card swatches expand their tap region to 44px with transparent padding despite 20px visual size
- Navigation hamburger icon uses 48px hit area
- Quantity selector +/- buttons padded to 44px square

### Collapsing Strategy

- Navigation categories collapse into a full-height slide-out drawer from left, with accordion sub-menus
- Product filters collapse into a bottom sheet triggered by a sticky "Filter" button
- Footer columns stack vertically as accordions on mobile, each heading toggling its link list
- Breadcrumbs truncate with ellipsis on mobile, showing only immediate parent and current page
- Image gallery loses thumbnail strip; main image becomes a horizontal swipe carousel with dot indicators

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The proprietary "article-font" display typeface could not be fully characterized (metrics, variable-font axes, fallback alignment); the font-family stack is inferred from CSS class names
- Exact transition/animation durations and easing curves are not extractable from static analysis
- Icon system details (stroke width, size grid, specific glyph set) are not available from color/font extraction
- Hover-state image swap behavior on product cards may vary by collection and could not be confirmed for all templates
- Mobile sticky-bar z-index layering and specific scroll-trigger thresholds are implementation-dependent
- Dark-mode or reduced-motion preferences were not detectable in the extraction
