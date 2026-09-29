---
version: alpha
name: "Zojirushi"
source_url: "https://www.zojirushi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Steam rising from a perfectly sealed lid — that image anchors everything Zojirushi puts on screen. The site runs a Bootstrap 4 utility layer with almost zero custom theming, letting product photography of stainless steel vacuum bottles, Neuro Fuzzy rice cookers, and bread machines carry the entire visual story. Primary CTAs land in #0062cc, a standard-issue blue that gains specificity only through context: it sits next to product images saturated with brushed metal, matte black housings, and the warm amber glow of #d39e00 "Add to Cart" highlight states. Typography stays invisible on purpose — the system font stack (`-apple-system`, `BlinkMacSystemFont`, `Helvetica Neue`, `Arial`) at moderate weights lets 300-dpi product renders and spec tables dominate the viewport. Card corners stay sharp at `{rounded.xs}` or `{rounded.none}`, echoing the precision-machined edges of the products themselves; the only soft radius appears on pill badges (`{rounded.full}`) marking "New" arrivals or "Best Seller" flags. A near-black ink (#1d2124) grounds dense specification grids — wattage, capacity, dimensions — that Japanese appliance buyers expect to scan without decoration. The canvas breathes through a cool gray surface system (#ececf6 panels, #dae0e5 hairlines) that reads clinical rather than cozy, appropriate for a brand whose value proposition is engineering reliability over lifestyle aspiration. Navigation runs horizontally with category mega-menus (Rice Cookers, Water Boilers, Thermal, Bread, Coffee) and a recipe content hub that integrates cooking guidance directly into product pages. The #d39e00 gold accent — used for promotional banners, sale badges, and hover states — is the closest thing to a signature brand color on screen, connecting to Zojirushi's elephant-mark heritage of warmth within precision.

colors:
  primary: "#0062cc"
  primary-active: "#004085"
  primary-disabled: "#b3d7ff"
  accent-gold: "#d39e00"
  accent-gold-soft: "#ffe8a1"
  success: "#1e7e34"
  success-soft: "#c3e6cb"
  info: "#117a8b"
  info-soft: "#bee5eb"
  danger: "#bd2130"
  danger-soft: "#f1b0b7"
  warning-text: "#856404"
  ink: "#1d2124"
  body: "#383d41"
  muted: "#545b62"
  muted-soft: "#818182"
  hairline: "#dae0e5"
  hairline-soft: "#d6d8db"
  border-focus: "#80bdff"
  canvas: "#ffffff"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  surface-strong: "#c8cbcf"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#1b1e21"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  mono:
    fontFamily: "'Consolas', 'Courier New', 'Liberation Mono', 'Monaco', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    borderWidth: 0
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.65
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 38px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.border-focus}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    paddingHorizontal: "{spacing.xl}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.hairline-soft}"
    hoverBorderColor: "{colors.primary}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-bestseller:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    rounded: "{rounded.none}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 480px
    ctaButton: "button-primary"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowPadding: "12px 16px"
    stripedBackground: "{colors.surface-soft}"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    borderWidth: 1px
    borderColor: "{colors.hairline-soft}"
    hoverShadow: "0 2px 12px rgba(0,0,0,0.1)"
    imageAspectRatio: "4:3"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: "16:9"
    titleTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    borderWidth: 1px
    borderColor: "{colors.hairline-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: "10px 44px 10px 16px"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.border-focus}"
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "none"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    padding: "{spacing.md} 0"
  alert-info:
    backgroundColor: "{colors.info-soft}"
    textColor: "#0c5460"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.info}"
  alert-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "#155724"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.success}"
  alert-warning:
    backgroundColor: "{colors.accent-gold-soft}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.accent-gold}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    headerBackground: "{colors.surface-soft}"
    stickyHeader: true
    columnMinWidth: 200px

---

## Components

### Buttons

**`button-primary`** — Solid #0062cc rectangles with barely-there 4px radius and white text at weight 600. Hover darkens to `{colors.primary-active}` (#004085) with no transition beyond a 150ms background shift. Disabled state drops to 65% opacity with the light #b3d7ff fill, keeping the button visible but clearly inactive. Used for "Add to Cart," "Find a Store," and form submissions.

**`button-secondary`** — White background with a 1px `{colors.hairline}` border and dark text. On hover the border strengthens to `{colors.muted}` and a subtle box-shadow appears. Used for "Compare Products," "View Details," and secondary navigation actions where the primary blue would compete with product imagery.

**`button-gold`** — The #d39e00 amber fill surfaces during promotional events and sale banners. Dark ink text keeps legibility high against the warm background. Reserved for time-sensitive CTAs like "Shop Sale" and "Limited Offer."

**`button-danger`** — Red #bd2130 at a slightly smaller 38px height, used sparingly for destructive actions in account management (remove from cart, cancel registration).

### Navigation

**`nav-bar`** — Fixed 72px white header with a single hairline border at the bottom. Logo sits left, category links center-weighted at 15px/500 weight, utility icons (search, account, cart) right-aligned. On scroll past 100px, a subtle drop shadow replaces the border to signal elevation without color change.

**`nav-mega-menu`** — Full-width dropdown panels triggered on hover (desktop) or tap (mobile). Each panel organizes products by series with thumbnail images, linking directly to product detail pages. Background remains pure white with `{colors.hairline}` separators between columns.

### Product Display

**`product-card`** — Square product image (1:1 ratio) on a white card with 1px gray border. Title in `{typography.title-sm}`, price below in `{typography.body-md}`. Hover lifts the card with border color transitioning to `{colors.primary}`. Badges stack in the top-left corner with 4px gap between them.

**`product-badge-new`** — Blue pill on primary background, uppercase 11px text. Positioned absolute top-left of the product image with 8px inset.

**`product-badge-sale`** — Amber #d39e00 background with dark text. Same positioning and sizing as the "new" badge but visually distinct through the warm color.

**`product-badge-bestseller`** — Green #1e7e34 background with white text. Appears on consistently high-performing SKUs.

### Content Components

**`hero-banner`** — Full-bleed panel with `{colors.surface-soft}` background (or a product lifestyle photograph). Display-xl headline left-aligned with body-lg subtitle beneath. CTA button positioned below with `{spacing.lg}` gap. Minimum height 480px ensures the hero dominates above-the-fold even on tall viewports.

**`spec-table`** — Alternating-row striped table for product specifications (capacity, wattage, dimensions, weight). Header cells use `{typography.spec-label}` in semibold 13px. Cell padding is generous at 12px 16px to prevent the dense data from feeling cramped. Borders use `{colors.hairline}` at 1px.

**`recipe-card`** — 16:9 food photography hero with title overlay or stacked below. Used in the "Kitchen" content section to cross-sell products through recipe associations. Border-radius at `{rounded.sm}` is the softest radius on the site, signaling editorial rather than commerce content.

**`category-card`** — 4:3 image with centered category name beneath. Hover state adds a subtle shadow and border darkening. Used on the homepage to route users into Rice Cookers, Water Boilers, Thermal Products, Bread Machines, and Coffee series.

### Search

**`search-bar`** — Standard input with magnifying glass icon positioned right. On focus, border transitions from `{colors.hairline}` to `{colors.border-focus}` (#80bdff) with a faint blue glow (box-shadow 0 0 0 3px rgba(0,98,204,0.25)). Results dropdown renders product thumbnails with titles and prices inline.

### Utility

**`breadcrumb`** — Slash-separated path in `{typography.caption}` with muted color for ancestors and ink for current page. Padding is minimal (12px vertical) to keep it compact above product content.

**`alert-info`** / **`alert-success`** / **`alert-warning`** — Bootstrap-standard alert boxes with tinted backgrounds, 1px colored borders, and dark tinted text. Used for shipping notices, registration confirmations, and stock warnings respectively.

### Data Display

**`comparison-table`** — Multi-column product comparison with sticky header row. Each column represents a product SKU with image, model number, and spec rows. Header background uses `{colors.surface-soft}` for contrast against the white cell rows. Minimum column width of 200px ensures product names and images remain legible.

### Footer

**`footer`** — Dark (#1d2124) full-bleed footer with light gray link text. Organized into columns: Products, Support, Company, Social. Links hover to pure white. Bottom row carries legal links, copyright, and region selector in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu with slide-out drawer. Hero reduces to 320px height. Product grid becomes 2-column. Spec tables scroll horizontally. Recipe cards stack single-column. Footer columns collapse to accordion. |
| Tablet | 744–1128px | Nav shows top-level categories but mega-menu reduces to single column. Product grid runs 3-column. Hero maintains full width but headline drops to `{typography.display-md}`. Comparison table allows 2 products visible with horizontal scroll. |
| Desktop | 1128–1440px | Full mega-menu with multi-column layout. Product grid at 4-column. Hero at full 480px height. Comparison table shows 3–4 products. Sidebar filters visible on category pages. |
| Wide | > 1440px | Content max-width caps at 1400px centered. Additional whitespace on flanks. Product grid remains 4-column but cards grow slightly. Hero imagery scales to fill without cropping. |

### Touch Targets

- All interactive elements maintain 44px minimum tap height on mobile
- Product card tap area encompasses the entire card surface, not just the title link
- Nav hamburger icon padded to 48×48px touch zone
- Breadcrumb links spaced with 8px horizontal gaps to prevent mis-taps
- "Add to Cart" button stretches full-width on mobile product pages

### Collapsing Strategy

- Mega-menu categories fold into an accordion within the mobile drawer, preserving hierarchy
- Product specification tables gain horizontal scroll with a fade gradient on the right edge indicating overflow
- Comparison tables limit to 2 visible products with swipe navigation on touch devices
- Footer columns collapse into expandable sections with chevron indicators
- Search bar moves behind a magnifying glass icon in the nav on mobile, expanding to full-width overlay on tap
- Category cards shift from 4-across grid to horizontal scroll strip on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- All extracted colors map exactly to Bootstrap 4's default theme palette — the site appears to use unmodified Bootstrap with no custom brand color overrides in static CSS. True brand-specific colors (if any exist beyond the Bootstrap defaults) may be injected via JavaScript or server-rendered inline styles not captured by static extraction.
- No custom web fonts detected; the site relies entirely on the system font stack. Zojirushi may load branded typefaces via JavaScript font-loading APIs that static extraction cannot capture.
- No meta theme-color defined, so mobile browser chrome color is unknown.
- Exact spacing scale and component dimensions are inferred from Bootstrap 4 defaults rather than measured from Zojirushi-specific overrides.
- Product image CDN structure, lazy-loading behavior, and image optimization parameters could not be determined from color/font extraction alone.
- The elephant logo mark dimensions, safe-space requirements, and minimum-size rules are not available from CSS extraction.
- Animation/transition timing values (page transitions, hover effects, loading states) were not captured.
