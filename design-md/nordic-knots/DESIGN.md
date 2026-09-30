---
version: alpha
name: "Nordic Knots"
source_url: "https://nordicknots.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Nordic Knots speaks in a quiet, deliberate visual language — one that trusts texture, material honesty, and the weight of negative space over loud typography or saturated color. The brand's canvas is a near-white `#fafafa` that leans warmer than hospital white, grounded by a deep ink `#212121` that appears in body copy, product titles, and the primary navigation bar. Accents arrive sparingly: a muted amber `#ff9800` for sale badges and limited-edition markers, a restrained blue `#2196f3` for informational links, and a soft green `#4caf50` for in-stock indicators. The palette's middle range — `#616161`, `#757575`, `#9e9e9e`, and `#bdbdbd` — does the heavy lifting for secondary text, placeholder copy, and hairline borders, creating a calm hierarchy that never competes with the product photography. Typography centers on NordicSans, a proprietary geometric sans-serif that carries the brand's Scandinavian ethos: clean, unornamented, and quietly confident. Display sizes run at moderate weights (500–600) rather than heavy 700+; the brand trusts generous whitespace and the tactile quality of wool, linen, and cotton swatches to carry emotional weight. Rounded corners are minimal — `{rounded.xs}` for buttons and `{rounded.sm}` for cards — preserving a crisp, architectural feel that mirrors the straight lines of a flat-weave rug. The overall effect is one of curated restraint: a digital space that feels like a Stockholm showroom, where every element earns its place and nothing shouts.

colors:
  primary: "#212121"
  primary-active: "#424242"
  primary-disabled: "#9e9e9e"
  ink: "#212121"
  body: "#424242"
  muted: "#616161"
  muted-soft: "#757575"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ff9800"
  accent-amber-active: "#f57c00"
  accent-blue: "#2196f3"
  accent-blue-active: "#1976d2"
  accent-green: "#4caf50"
  accent-green-active: "#388e3c"
  error: "#f44336"
  error-active: "#d32f2f"
  error-soft: "#e57373"
  star-rating: "#212121"
  sale-badge: "#de3535"
  sale-badge-text: "#ffffff"
  limited-edition: "#ffb74d"
  new-badge: "#ba68c8"
  new-badge-text: "#ffffff"
  swatch-wool: "#f2f2f2"
  swatch-linen: "#f6f6f6"
  swatch-cotton: "#ffffff"

typography:
  display-xl:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'NordicSans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
    textDecoration: line-through
    color: "{colors.muted}"

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.new-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-limited:
    backgroundColor: "{colors.limited-edition}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    color: "{colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  swatch-selector:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  swatch-selector-active:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 36px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep ink `#212121` with white text and a crisp `{rounded.xs}` corner. On hover, it shifts to `{colors.primary-active}` (`#424242`), and in its disabled state it fades to `{colors.primary-disabled}` (`#9e9e9e`). The uppercase label uses `{typography.button-md}` with 0.5px letter-spacing for a refined, architectural feel. **`button-secondary`** — An outlined variant on a white canvas with ink text, matching dimensions and typography, used for secondary actions like "View Details" or "Save for Later." **`button-tertiary-text`** — A text-only button with no background or border, used for subtle inline actions like "Clear filters" or "Cancel." **`button-pill`** — A fully rounded pill button used for compact actions like "Add to cart" on mobile or quick-filter tags, rendered at 36px height with `{typography.button-sm}`.

### Cards
**`product-card`** — The primary product display unit, a white card with `{rounded.sm}` corners containing an image, title, price, and optional badges. The image area shares the same corner radius for visual consistency. The title uses `{typography.title-sm}` in ink, while the price uses `{typography.price}`. Sale prices render the original in `{colors.muted}` with a line-through via `{typography.price-sale}`. **`product-card-badge`** — A small rectangular badge in `{colors.sale-badge}` (`#de3535`) with white text, positioned over the top-left of the product image. A "New" variant uses `{colors.new-badge}` (`#ba68c8`), and a "Limited Edition" variant uses `{colors.limited-edition}` (`#ffb74d`) with ink text.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on a white canvas, housing the logo, category links, search, and cart icon. Links use `{typography.nav-link}` — uppercase with 0.5px tracking — and the active state is indicated by a 2px bottom border in ink. Inactive links render in `{colors.muted}`. **`search-bar`** — A pill-shaped input on a soft gray `{colors.surface-soft}` background with a `{rounded.full}` radius, used for product and content search. On focus, the border shifts from `{colors.hairline}` to `{colors.ink}`.

### Forms
**`text-input`** — Standard single-line input with a white background, `{rounded.xs}` corners, and a `{colors.hairline}` border. On focus, the border becomes ink; on error, it switches to `{colors.error}` (`#f44336`). **`select-input`** — Matches the text input dimensions and styling, used for dropdowns like size or sort order. **`quantity-selector`** — A compact numeric input with increment/decrement buttons, used on product detail pages.

### Badges & Indicators
**`swatch-selector`** — A 32px circular swatch button for material or color selection, with a `{colors.hairline}` border. The active state uses a 2px ink border. **`rating-stars`** — Star icons rendered in `{colors.star-rating}` (`#212121`) at 14px, used on product cards and detail pages. **`filter-chip`** — A pill-shaped filter toggle with a `{colors.hairline}` border, used in category and search result filtering. The active state fills with ink and inverts the text.

### Footer
**`footer`** — A full-width footer in the brand's deep ink `{colors.primary}` with white text, containing link columns, newsletter signup, and social icons. Links use `{typography.link}` and shift to `{colors.hairline}` on hover. The footer is padded with `{spacing.xxl}` top and bottom.

### Accordion
**`accordion`** — A vertically stacked disclosure component used for FAQs, product details, and shipping information. Each item has a `{colors.hairline}` bottom border, a clickable header in `{typography.title-sm}`, and expandable content in `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner height reduces to 320px; filter chips stack vertically; accordion becomes primary layout for product details; search bar moves to full-width below nav. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero banner at 400px; filter chips wrap to two rows; product cards show 2-up layout. |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero banner at 480px; filter chips display in a horizontal strip; product cards show 3-up layout with hover states. |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner at 520px; additional whitespace around content; product cards show 4-up layout. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile.
- Icon buttons and swatch selectors are 40px and 32px respectively, with adequate padding to meet touch targets.
- Filter chips and pill buttons are 36px tall with generous horizontal padding.
- Accordion headers have 16px vertical padding to ensure easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The category strip collapses into a horizontal scrollable row on mobile and tablet.
- Product filters collapse into a modal or bottom sheet on mobile.
- The footer link columns stack vertically on mobile, with each column becoming an accordion.
- Hero banner text overlays collapse to a single column on mobile, with the CTA button full-width.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons and text inputs could not be reliably extracted.
- Error state styling for forms (error messages, iconography) is inferred from the error color palette but not confirmed from live site inspection.
- Dark mode or high-contrast mode tokens are not present in the extracted data.
- Sub-brand or collection-specific color palettes (e.g., "Wool Collection," "Linen Collection") may exist but were not detected.
- Animation and transition timing values (duration, easing) are not available.
- Shadow/elevation tokens for cards, modals, and dropdowns were not found in the extracted CSS.
- The exact font-weight range for NordicSans (e.g., available weights beyond 400 and 500) is unknown.
- Loading states, skeleton screen patterns, and empty state designs are not documented.
- The brand's icon system (SVG library, stroke widths, sizes) is not captured.
- Accessibility-specific tokens (focus rings, skip-to-content, screen-reader-only patterns) are absent from the extracted data.
- The newsletter signup form and its specific validation/error styling are not documented.
- Mobile-specific navigation patterns (hamburger menu animation, drawer width, overlay scrim) are inferred but not confirmed.
