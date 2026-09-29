---
version: alpha
name: "Campania International"
source_url: "https://www.campaniainternational.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep hunter green (#015845) anchors every interaction on a site that sells cast-stone vessels weighing upward of 200 pounds — the color reads as aged patina, wet moss, the underside of a terracotta saucer left in shade all summer. Against a near-white canvas (#fbfbfb) the green carries primary CTAs, navigation highlights, and collection-header bands without competing with the heavily textured product photography that does the real selling. Typography inherits the system stack — no branded webfont load detected — which keeps page weight low for a catalog that leans on large hero imagery of urns photographed in situ among boxwood hedges and limestone walls. The type strategy favors medium-weight sans-serif at generous sizes for product names (`{typography.display-md}`) and lighter body copy (`{typography.body-md}`) that stays out of the way. Corner radii are conservative: product cards use a subtle `{rounded.xs}` or `{rounded.sm}`, buttons sit at `{rounded.xs}`, and nothing approaches pill territory — the geometry mirrors the squared, architectural silhouettes of the planters themselves. Spacing is generous vertically (`{spacing.section}` between collection rows) but tighter horizontally within grids, letting each planter card breathe against the pale background. A secondary warm stone tone (#d4c5a9) surfaces in badges and accent borders, nodding to the natural limestone and terra-cotta finishes the brand is known for. The overall impression is a catalog for landscape architects and serious gardeners: restrained, material-forward, and trusting the product to hold attention without typographic or chromatic noise.

colors:
  primary: "#015845"
  primary-active: "#014a3a"
  primary-disabled: "#9abfb5"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6e6e6e"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#fbfbfb"
  surface-soft: "#f4f4f2"
  surface-card: "#ffffff"
  surface-warm: "#f7f5f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-stone: "#d4c5a9"
  accent-stone-soft: "#ebe4d6"
  accent-terracotta: "#b86f4a"
  footer-bg: "#1a1a1a"
  footer-text: "#d9d9d9"
  success: "#2e7d32"
  error: "#c62828"
  sale: "#b52a1c"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px
  nav-link-upper:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-compare:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
    transition: background-color 0.2s ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-logo:
    maxHeight: 44px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    boxShadow: 0 4px 20px rgba(0,0,0,0.08)
    border: 1px solid {colors.hairline-soft}
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    backgroundSize: cover
    backgroundPosition: center
  hero-banner-overlay:
    background: linear-gradient(to right, rgba(1,88,69,0.85), rgba(1,88,69,0.4))
  collection-header:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 0
    border: 1px solid {colors.hairline-soft}
    transition: box-shadow 0.2s ease
    hoverShadow: 0 2px 12px rgba(0,0,0,0.06)
  product-card-image:
    aspectRatio: 1 / 1
    objectFit: cover
    rounded: "{rounded.xs} {rounded.xs} 0 0"
    backgroundColor: "{colors.surface-soft}"
  product-card-body:
    padding: "{spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    color: "{colors.muted}"
  finish-swatch:
    width: 28px
    height: 28px
    rounded: "{rounded.full}"
    border: 2px solid {colors.hairline}
    cursor: pointer
  finish-swatch-active:
    border: 2px solid {colors.primary}
    boxShadow: 0 0 0 2px {colors.canvas}, 0 0 0 4px {colors.primary}
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-bestseller:
    backgroundColor: "{colors.accent-stone}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  breadcrumb:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    separator: "/"
    activeColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: none
    focusBorder: 1px solid {colors.primary}
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 14px
    border: 1px solid {colors.hairline}
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: 1px solid {colors.primary}
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.nav-link-upper}"
    color: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.body-sm}"
    color: "{colors.footer-text}"
    hoverColor: "{colors.on-dark}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
    padding: "{spacing.sm} {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid {colors.hairline}
    buttonWidth: 44px
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    activeColor: "{colors.primary}"
    padding: 8px 12px
    gap: "{spacing.xs}"

---

## Components

### Buttons

**`button-primary`** — Solid deep-green button used for Add to Cart, checkout steps, and primary form submissions. Background is `{colors.primary}` (#015845) with white text at weight 600. On hover, darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with `not-allowed` cursor. Corners use `{rounded.xs}` (4px) — deliberately squared-off to echo the architectural geometry of cast-stone planters.

**`button-secondary`** — White-fill button with a 2px green border and green text. Used for secondary actions: "View Details," "Continue Shopping," wishlist additions. On hover the background shifts to `{colors.surface-soft}` and border darkens. Same 4px radius as primary.

**`button-add-to-cart`** — Full-width variant of the primary button used on product detail pages. Slightly taller (52px) and wider padding to anchor the purchase action below finish/size selectors.

### Navigation

**`nav-bar`** — 72px-tall sticky header on white canvas with a thin bottom hairline. Logo sits left; main category links (Planters, Fountains, Statuary, Garden Décor) in `{typography.nav-link}` centered or left-aligned. Right side holds search icon, account, and cart with item count badge. On scroll, a subtle shadow replaces the border.

**`nav-dropdown`** — Mega-menu panel that opens on hover for categories with subcollections (e.g., Planters → by Shape, by Size, by Material). White card with `{rounded.sm}` corners and a soft box shadow. Organized in multi-column grid with optional category thumbnails.

**`announcement-bar`** — Full-width green strip above the nav bar for shipping thresholds, seasonal promotions, or sale callouts. White text in `{typography.caption}` centered. Auto-rotates messages if multiple are configured.

### Product Cards

**`product-card`** — Square-ratio product image atop a white card body. Border is `{colors.hairline-soft}` at rest; on hover a subtle elevation shadow appears. Card body shows product name in `{typography.title-sm}`, price in `{typography.price}`, and optionally a row of `finish-swatch` circles for color/material variants. Badges (Sale, New, Bestseller) position absolute top-left over the image.

**`finish-swatch`** — 28px circles showing available finishes (Verde, Aged Limestone, Copper Bronze, etc.). Active swatch gets a double-ring treatment via box-shadow. Hovering a swatch can optionally swap the card image to that finish.

### Product Detail

**`quantity-selector`** — Minus/plus buttons flanking a numeric input, all within a bordered container at 44px height. Buttons are 44px wide tap targets.

**`breadcrumb`** — Muted-color path navigation (Home / Planters / Large Urns / Product Name) in `{typography.body-sm}`. Current page is `{colors.ink}`, ancestors are `{colors.muted}` and linked.

### Filtering & Search

**`search-bar`** — Soft-gray background input with no visible border at rest; on focus a 1px green border appears. Rounded at `{rounded.sm}` for slight softness without pill shape. Magnifying-glass icon inside left.

**`filter-chip`** — Small bordered pills for active filters (material: Cast Stone, size: Large). Active state inverts to green fill with white text. Clicking the × removes the filter.

### Collection Pages

**`collection-header`** — Warm off-white banner (`{colors.surface-warm}`) spanning full width with collection name in `{typography.display-md}` centered. Optional short description below in `{typography.body-md}`. Provides visual separation between nav and the product grid.

### Hero

**`hero-banner`** — Full-bleed lifestyle image (garden scene with planters in context) with a gradient overlay shifting from opaque green on the text side to transparent. Display-xl white headline, body-lg subtitle, and a secondary button (white outline on dark) for the CTA. Minimum 480px height desktop.

### Badges

**`badge-sale`** — Red (`{colors.sale}`) with white text, used on product cards and detail pages when compare-at price is set. **`badge-new`** — Green primary background, signals recent additions to the catalog. **`badge-bestseller`** — Warm stone tone (`{colors.accent-stone}`) with dark text, a softer callout for perennial top sellers.

### Footer

**`footer`** — Dark background (`{colors.footer-bg}`) with four-column layout: Shop (categories), About (story, sustainability, press), Support (shipping, returns, FAQ), and Newsletter signup. Column headings use `{typography.nav-link-upper}` (uppercase, tracked). Links in muted light gray that brighten on hover. Bottom bar holds copyright, payment icons, and legal links.

### Pagination

**`pagination`** — Numeric page links in `{typography.body-sm}`. Active page uses `{colors.primary}` text color. Arrows for prev/next. Generous tap padding for mobile.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up tight). Nav collapses to hamburger + slide-out drawer. Hero reduces to 320px height with stacked text. Footer stacks into accordion sections. Announcement bar text truncates or scrolls. |
| Tablet | 744–1128px | Two- or three-column product grid. Nav shows top-level links but dropdowns become tap-to-toggle. Hero maintains overlay layout but at reduced padding. Filters move to a slide-out sheet triggered by a "Filter" button. |
| Desktop | 1128–1440px | Three- or four-column product grid. Full mega-menu hover navigation. Sidebar filters on collection pages. Hero at full 480px+ height. |
| Wide | > 1440px | Content max-width caps at 1440px, centered. Product grid stays four columns. Increased horizontal padding (`{spacing.xxl}`). Hero image scales but text container remains capped width. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile and tablet.
- Finish swatches increase to 36px on touch devices with 8px gap.
- Quantity selector buttons fill 48px on mobile for easier tapping.
- Nav drawer links get 48px row height with full-width tap area.

### Collapsing Strategy

- Navigation: desktop mega-menu → mobile hamburger with accordion sub-menus.
- Collection filters: desktop sidebar → mobile bottom-sheet or slide-out with "Apply" button.
- Product grid: 4-col → 3-col → 2-col; card image aspect ratio stays 1:1 throughout.
- Footer: 4-column horizontal → stacked accordion with toggle arrows.
- Hero text: maintains hierarchy but font sizes step down one scale level per breakpoint.

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex colors (#015845, #fbfbfb) were extractable from the live site; the accent-stone, terracotta, footer, and status colors are inferred from the brand's product line and common Shopify patterns — they should be validated against the live stylesheet or theme settings.
- Font stack returned as `inherit` — no custom webfont was detected. The site may load fonts via JavaScript, a Shopify theme app, or the fonts may genuinely be system defaults. Verify in browser DevTools whether a branded serif or display face appears on headings.
- No meta theme-color was set, so mobile browser chrome color is unknown.
- Specific box-shadow values, transition durations, and animation easing curves could not be extracted and are estimated from common Shopify Dawn/Prestige theme defaults.
- Mega-menu structure and hierarchy depth are assumed from typical planter/garden category taxonomy — actual nav architecture may differ.
- No dark-mode tokens observed or inferred.
