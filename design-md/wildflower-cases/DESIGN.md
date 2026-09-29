---
version: alpha
name: "Wildflower Cases"
source_url: "https://www.wildflowercases.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A candy-pink voltage of #e50669 runs through every primary CTA, add-to-bag button, and navigation accent, set against a near-white canvas of #f7f7f8 that keeps the focus on the cases themselves — each one a limited-edition fashion accessory rather than a phone protector. The brand leans on GTAmerica for its clean, slightly condensed body and Recife-Light for display moments, creating a contrast between utilitarian sans and a delicate, editorial serif that whispers "fashion" without shouting. Product thumbnails sit in tight grids with generous whitespace, each card a simple image-plus-price unit that lets pattern and color do the selling — no dense copy, no feature bullets. The secondary palette pulls from the cases themselves: a blush #fd83c2, a seafoam #b2f9e9, a marigold #ffcf2a, and a deep navy #272d45 that anchors the footer and utility text. Badges and sale tags use {rounded.full} pills in that signature pink, while the overall layout stays airy and editorial — a fashion magazine translated into a product grid, not a utility app. The brand's voice is confident but not loud, letting the product photography (always the hero) and the occasional all-caps headline carry the energy.

colors:
  primary: "#e50669"
  primary-active: "#c40057"
  primary-disabled: "#fca3c9"
  ink: "#231f20"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#fd83c2"
  accent-seafoam: "#b2f9e9"
  accent-marigold: "#ffcf2a"
  accent-navy: "#272d45"
  accent-teal: "#0e7a82"
  sale-badge: "#e50669"
  new-badge: "#00eab6"
  star-rating: "#ffcf2a"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Recife-Light', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Recife-Light', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'GTAmerica-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GTAmerica-Medium', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'GTAmerica-Medium', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'GTAmerica', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'GTAmerica-Medium', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'GTAmerica-Medium', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.body-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  social-icon:
    color: "{colors.muted-soft}"
    size: 24px
  star-rating:
    color: "{colors.star-rating}"
    size: 14px
  color-swatch:
    rounded: "{rounded.full}"
    size: 24px
    border: "1px solid {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The signature CTA across the site, used for "Add to Bag", "Checkout", and primary form submissions. Filled with the brand's hot pink `{colors.primary}` and white text on a `{rounded.sm}` rectangle. On hover, shifts to `{colors.primary-active}` with no scale or shadow change — the color shift alone signals interactivity. Disabled state uses `{colors.primary-disabled}` with full opacity, no text change.

**`button-secondary`** — Outlined alternative for secondary actions like "View Details" or "Continue Shopping". White fill with `{colors.ink}` text and a `{colors.hairline}` border. Active state fills `{colors.surface-soft}` and darkens the border to `{colors.muted}`.

**`button-pill-primary`** — Small pill-shaped badge-buttons used for filter tags, collection links, and promotional chips. Uses `{rounded.full}` and compact padding. The same hot pink fill and white text as the primary button, but at `{typography.button-sm}` size.

**`button-pill-outline`** — The unfilled counterpart to the pill button, used for "clear filters" or "view all" links within filter strips. Transparent background with a `{colors.hairline}` border.

### Cards
**`product-card`** — The core product display unit, a simple image-plus-text stack with no border or background fill (the canvas itself provides separation). The product image fills a 1:1 aspect ratio square with no rounding — hard corners keep the photography editorial and unadorned. Below the image, the product title sits in `{typography.body-sm}` and the price in `{typography.price}`. On hover, a subtle `{colors.surface-soft}` background may appear behind the text block, but the image remains unchanged. Badges (`{badge-new}`, `{badge-sale}`, `{badge-sold-out}`) overlay the top-left corner of the image as small pills.

**`hero-banner`** — Full-width promotional banner used for collection launches and seasonal campaigns. Uses `{colors.surface-soft}` as a neutral backdrop with `{typography.display-xl}` in Recife-Light for the headline. The banner may feature a full-bleed product image on desktop, with the headline overlaid at left or center. Padding is generous at `{spacing.section}` top and bottom.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, white background with uppercase `{typography.nav-link}` links in `{colors.muted}`. The logo (typically "WILDFLOWER" in a custom wordmark or Recife-Light) sits left-aligned. A search icon and bag icon sit right-aligned. On mobile, the nav collapses to a hamburger menu with a slide-out drawer.

**`nav-link`** — Uppercase, letter-spaced navigation items in `{colors.muted}` with 16px horizontal padding. Active or hover state shifts to `{colors.ink}` with no underline — the color change alone indicates selection.

### Forms
**`text-input`** — Standard input field for email signup, search, and address forms. White fill with a `{colors.hairline}` border and `{rounded.sm}` corners. Focus state swaps the border to `{colors.primary}`. Error state uses the same pink border with no additional icon — the color change is the signal.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used in the mobile nav and footer. White fill with `{colors.hairline}` border and placeholder text in `{colors.muted}`. On focus, the border shifts to `{colors.primary}`.

**`quantity-selector`** — A compact input for cart quantity adjustments. `{rounded.sm}` with a `{colors.hairline}` border, containing a minus button, the quantity number, and a plus button. The number sits in `{typography.body-md}`.

### Badges
**`badge-new`** — A small pill badge in `{colors.new-badge}` (seafoam green) with dark text, used to flag newly added products. Uppercase `{typography.badge}` with tight tracking.

**`badge-sale`** — A hot pink pill badge matching `{colors.sale-badge}`, used for markdowns and promotional pricing. White text, same uppercase badge typography.

**`badge-sold-out`** — A neutral gray pill in `{colors.muted-soft}` for out-of-stock items. White text, same badge styling.

### Color Swatches
**`color-swatch`** — A 24px circle (`{rounded.full}`) used in product detail pages to show available case colors. Each swatch is a solid fill of the case color with a `{colors.hairline}` border. Selected state swaps the border to `{colors.ink}` with 2px thickness.

### Footer
**`footer-section`** — A deep navy (`{colors.accent-navy}`) footer with white and `{colors.muted-soft}` text. Links are in `{typography.link}` with `{colors.muted-soft}` color. Social icons are 24px and match the link color. The footer typically includes columns for "Shop", "Help", "About", and "Connect", plus a newsletter signup form.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), hamburger nav replaces full nav, hero banner stacks image below text, search bar moves to sticky top, footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid, full nav with condensed link spacing, hero banner side-by-side layout, footer in 2-3 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav with standard spacing, hero banner full-width with overlay text, footer in 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) for content, hero banner may use wider padding |

### Touch Targets
- All buttons and links: minimum 44px height for touch targets on mobile
- Color swatches: 24px diameter, but tap area extends to 44px via invisible padding
- Nav icons (search, bag): 44px tap area
- Quantity selector buttons: 44px minimum tap area

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px
- Product grid reduces columns: 4 → 3 → 2 → 2 on mobile (never single column for product thumbnails)
- Footer columns collapse: 4 → 2 → 1
- Hero banner switches from overlay to stacked layout at < 744px
- Search bar moves from nav to sticky top bar on mobile
- Filter sidebar (if present) becomes a bottom sheet or dropdown on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (whether image zoom, color overlay, or text underline) could not be reliably extracted from static analysis
- Error styling for form validation (error messages, input error icons) was not observed in the extracted data
- Dark mode is not supported — all extracted colors assume light theme
- Sub-brand or collection-specific palettes (e.g., limited-edition collaborations) may introduce additional accent colors not captured here
- The exact font weights for GTAmerica variants (Regular, Medium, Bold) were inferred from common usage; the site may use additional weights like Light or Black
- Recife-Light appears to be the only Recife weight used; heavier weights (Regular, Medium) may exist but were not detected
- The `oke-widget-icons` font family suggests Okendo reviews integration; review-specific typography and star sizing may differ from the `star-rating` token defined here
- Shopify checkout and payment widget colors (Afterpay, Klarna, Shopify Pay) were filtered from the extracted palette but may introduce additional brand-adjacent colors in the purchase flow
- Animation and transition timings (hover fades, menu slide durations, image lazy-load effects) were not extractable
- The extracted color list included several grays and near-whites that may represent specific surface or border tokens not fully mapped; the `hairline-soft` and `surface-soft` tokens are best approximations
