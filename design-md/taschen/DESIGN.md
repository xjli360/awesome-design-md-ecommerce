---
version: alpha
name: "Taschen"
source_url: "https://www.taschen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A riot of lime-green #79a70a against a near-white #fefefe canvas — Taschen’s digital storefront reads like a bookshop that swallowed a pop-art gallery. That electric green, pulled from the brand’s iconic logo, serves as the single voltage for primary CTAs, price tags, and category badges, while a secondary palette of deep navy #2e409e, warm ochre #f2be80, and brick #ac1212 surfaces in limited-edition banners and collection headers. The typography stack layers FoundersGroteskCondensed for bold, space-efficient display heads (tight letter-spacing, 700 weight) against Sabon Next LT Pro for body copy — a deliberate clash of condensed grotesque and humanist serif that echoes the publisher’s mix of avant-garde art books and classic monographs. Product covers are treated as full-bleed hero images, with no hard corner except the 8px `{rounded.sm}` on add-to-cart buttons and the 4px `{rounded.xs}` on badge labels. The checkout flow, powered by Shopify, introduces a secondary green #468847 for success states and a muted #dcdee0 for disabled controls. Navigation is a persistent top bar with a condensed logo lockup, dropdown menus for categories (Art, Architecture, Photography, etc.), and a search icon that expands into a full-width input on click. The overall feel is editorial and confident — generous whitespace around book spreads, 48px `{spacing.xxl}` section gaps, and a footer dense with newsletter signup, social links, and a “Books for Optimists Since 1980” tagline in FoundersGroteskCondensed at 14px.

colors:
  primary: "#79a70a"
  primary-active: "#468847"
  primary-disabled: "#dcdee0"
  ink: "#0e0d0e"
  body: "#484f51"
  muted: "#828282"
  muted-soft: "#a6a7a9"
  hairline: "#e5e5e5"
  hairline-soft: "#f1f3f7"
  canvas: "#fefefe"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#2e409e"
  accent-ochre: "#f2be80"
  accent-brick: "#ac1212"
  accent-purple: "#722b92"
  accent-gold: "#ebc621"
  success: "#468847"
  error: "#dd2b1c"
  info: "#5bbad5"
  badge-new: "#79a70a"
  badge-sale: "#dd2b1c"
  badge-limited: "#2e409e"
  star-rating: "#ebc621"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Sabon Next LT Pro', 'Georgia', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sabon Next LT Pro', 'Georgia', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Sabon Next LT Pro', 'Georgia', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sabon Next LT Pro', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Sabon Next LT Pro', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'FoundersGroteskCondensed', 'Inter', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.error}"

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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-icon-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  button-icon-circle-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.ink}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
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
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "none"
  search-input-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: 8px 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  nav-dropdown-item:
    padding: 8px 24px
    typography: "{typography.nav-link}"
  nav-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  logo:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    height: 32px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-banner-content:
    padding: "{spacing.xxl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
  category-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    width: 44px
    height: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"
  breadcrumb-current:
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    color: "{colors.ink}"
    fontWeight: 600
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-large:
    color: "{colors.primary}"
    size: 48px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand’s signature lime green `{colors.primary}`. Used for “Add to Cart”, “Checkout”, and “Subscribe” actions. On hover, shifts to a deeper green `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with muted text. Text is uppercase FoundersGroteskCondensed at 14px, 600 weight, with 8px `{rounded.sm}` corners.
**`button-secondary`** — An outlined variant with a white fill and `{colors.hairline}` border. Used for “View Details”, “Learn More”, and secondary checkout actions. Active state darkens the border to `{colors.ink}`. Same typography and height as primary.
**`button-tertiary-text`** — A text-only button with no background or border. Used for “Cancel”, “Remove”, and inline actions. Inherits `{typography.button-md}` and `{colors.ink}` text color.
**`button-icon-circle`** — A 40px circular icon button with a hairline border. Used for wishlist hearts, share icons, and cart adjustments. Active state fills the background with `{colors.surface-soft}` and darkens the border.
**`button-pill-primary`** — A smaller, fully rounded pill button for compact contexts like category filters or “Shop Now” badges. Uses `{typography.button-sm}` and `{rounded.full}`.

### Cards
**`product-card`** — A minimal card with no border or rounding, relying on the product image as the primary visual. The image container has a 3:4 aspect ratio and a soft `{colors.surface-soft}` fallback. Title uses `{typography.title-sm}` (Sabon Next LT Pro, 18px), price uses `{typography.price}` (FoundersGroteskCondensed, 16px). Badges (New, Sale, Limited Edition) overlay the top-left corner of the image with `{rounded.xs}` and uppercase condensed typography.
**`category-card`** — A square card (1:1 aspect ratio) for browsing by subject (Art, Architecture, Photography, etc.). The image fills the square, and the category name sits below in `{typography.title-md}`. No rounding — the hard edge reinforces the editorial grid.
**`hero-banner`** — A full-width, 480px-tall banner for featured collections or new releases. A dark scrim overlay (`{colors.scrim}` at 30% opacity) ensures text readability. Content is left-aligned with `{spacing.xxl}` padding. The CTA button uses `{colors.primary}`.

### Navigation
**`nav-bar`** — A fixed 72px top bar with a white background and a soft bottom border. The logo (FoundersGroteskCondensed, 28px) sits on the left, followed by category links in uppercase 14px. A search icon and cart icon sit on the right. On scroll, the bar gains a subtle box-shadow.
**`nav-dropdown`** — A flyout menu triggered by hovering over a category link. White background, 8px vertical padding, and a soft shadow. Items are 14px uppercase links with 24px horizontal padding. Hover state adds a light gray background.
**`breadcrumb`** — A secondary navigation path in 11px uppercase condensed type. Current page is `{colors.ink}`, ancestors are `{colors.muted}`. Separator is a forward slash.

### Forms
**`text-input`** — A standard input field with a 1px `{colors.hairline}` border and 8px rounding. Focus state swaps the border to `{colors.primary}`. Error state uses `{colors.error}`. Height is 48px for comfortable touch targets.
**`select-input`** — A dropdown selector matching the text-input styling. Used for sorting (Price, Title, Date) and filtering by format (Hardcover, Paperback, Special Edition).
**`search-input`** — A fully rounded search bar with a soft gray background (`{colors.surface-soft}`). On focus, the background turns white and a `{colors.primary}` border appears. Used in the nav bar and on the search results page.
**`newsletter-input`** — A text input paired with a `{colors.primary}` submit button for the footer signup form. The input has a 1px hairline border and 8px rounding.

### Footer
**`footer`** — A full-width footer with a `{colors.surface-soft}` background. Contains columns for Customer Service, About Taschen, and Social Links. Headings use 13px uppercase FoundersGroteskCondensed. Links are 14px Sabon Next LT Pro with underlines. The newsletter signup is prominently placed in the first column. The “Books for Optimists Since 1980” tagline sits at the bottom in 11px uppercase.

### Badges & Labels
**`badge`** — A small, uppercase label with `{rounded.xs}` corners. Three variants: green for “New”, red for “Sale”, and navy for “Limited Edition”. Used on product cards and collection banners. Text is white, 10px, 700 weight.
**`star-rating`** — A 5-star rating display using `{colors.star-rating}` (gold #ebc621). Stars are 14px. Used on product detail pages and review summaries.

### Modals & Overlays
**`modal`** — A centered dialog with 12px rounding, 32px padding, and a soft shadow. Used for quick-view product details, size guides, and shipping information. The close button is a 32px circular icon in the top-right corner.
**`modal-overlay`** — A 50% opacity black scrim behind the modal.
**`tooltip`** — A small, dark tooltip with 4px rounding and 4px/8px padding. Used for icon explanations and truncated text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger menu replaces top nav, hero banner height reduces to 320px, footer collapses to stacked layout, search becomes a full-screen overlay |
| Tablet | 744–1128px | Two-column product grid, top nav shows 4-5 category links with “More” dropdown, hero banner at 400px, footer uses 2-column grid |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all categories visible, hero banner at 480px, footer uses 4-column grid |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero banner at 520px with larger typography |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 44px for mobile touch targets.
- Icon buttons are 40px with 44px touch area via padding.
- Product card images are tappable with no minimum size, but the entire card area is clickable.
- Dropdown menus on mobile expand to full-width with 48px tap targets.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a full-screen overlay drawer.
- The category strip (featured subjects) collapses to a horizontal scrollable row on tablet and mobile.
- The footer collapses from 4 columns to 2 columns on tablet, then to a single stacked column on mobile.
- Product filters collapse into an accordion on mobile, with a “Filters” button that opens a slide-out panel.
- The hero banner text overlay reduces font size and padding on mobile to avoid overflow.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links were inferred from common patterns; exact extracted hover hex values are not available.
- Error styling (input borders, error messages, form validation) is based on standard Shopify patterns, not extracted from the live site.
- Dark mode is not supported by the extracted data; the site appears to be light-mode only.
- Sub-brand palettes (e.g., Taschen America, Taschen UK) may exist but were not extracted.
- The exact font weights for FoundersGroteskCondensed and Sabon Next LT Pro are inferred from common usage; the live site may use additional weights (e.g., 300, 800).
- The `textTransform: uppercase` on button and caption typography is inferred from the condensed, space-efficient aesthetic; the live site may use mixed case in some contexts.
- The `letterSpacing` values for condensed fonts are estimated based on typical grotesque typeface settings; the exact tracking may vary.
- The `aspectRatio` values for product and category cards are based on common book-publisher layouts; the live site may use different ratios for specific collections.
- The `boxShadow` values for dropdowns and modals are estimated; the live site may use different shadow intensities or directions.
- The `opacity` value for the hero banner overlay is an estimate; the live site may use a different opacity or a gradient overlay.
- The `height` values for the hero banner at different breakpoints are estimates; the live site may use viewport-relative units (e.g., 60vh).
- The `max-width` container value for wide screens is an estimate; the live site may use a different maximum width or no max-width at all.
- The exact font stack order (FoundersGroteskCondensed vs. Inter vs. Roboto) is based on the extracted declarations; the live site may use a different fallback order.
