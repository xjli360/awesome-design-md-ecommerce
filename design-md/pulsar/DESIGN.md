---
version: alpha
name: "Pulsar"
source_url: "https://www.pulsar.gg"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A performance-first gaming gear brand that communicates through raw speed and precision, anchored on a near-black canvas of #111111 — the void from which every product emerges. The brand's primary voltage is #b12704, a burnt-orange-red that reads as heat, friction, and competitive intensity, deployed sparingly on CTAs, price highlights, and category badges. This is not a brand that softens its edges: buttons land at {rounded.sm} (8px), product cards at {rounded.md} (12px), and the overall geometry favors sharp, purposeful rectangles over pill-shaped friendliness. The typographic voice runs Open Sans at modest weights — body copy at 400, headings rarely exceeding 700 — letting the product photography and spec sheets carry the persuasive load. A secondary accent of #6371c7 (a muted periwinkle) appears on secondary actions and informational badges, creating a cool counterpoint to the aggressive primary. The palette is otherwise monochromatic: layers of gray from #989898 through #bebebe to #ebebeb build depth across surfaces, cards, and hairline borders, while #212b35 and #202223 provide dark-surface alternatives for dropdowns and footer regions. The brand's Shopify foundation surfaces through checkout-widget blues (#0080ff, #2f6ed6, #3d9ad1) and payment-method badges, but these are infrastructure, not identity. Pulsar speaks in grams, millimeters, and IPS ratings — the design system exists to make those numbers feel fast.

colors:
  primary: "#b12704"
  primary-active: "#8f1f03"
  primary-disabled: "#f0b8a6"
  ink: "#111111"
  body: "#353535"
  muted: "#989898"
  muted-soft: "#bebebe"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#212b35"
  surface-dark-soft: "#202223"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-secondary: "#6371c7"
  accent-blue: "#0080ff"
  accent-blue-active: "#2f6ed6"
  accent-blue-soft: "#3d9ad1"
  error: "#c00000"
  badge-new: "#b12704"
  badge-sale: "#c00000"
  star-rating: "#111111"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.3px
  spec-label:
    fontFamily: "'Open Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-blue-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-sm-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
    padding: 6px 14px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(17, 17, 17, 0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 16px rgba(17, 17, 17, 0.12)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-price-sale:
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  hero-cta-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.on-dark}"
    padding: "12px 30px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
    textColor: "{colors.primary}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    fontWeight: 700
    textTransform: uppercase
    padding: "{spacing.sm} {spacing.base}"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 14px
  star-rating-empty:
    textColor: "{colors.muted-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.body}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's burnt-orange-red (#b12704) on white. Used for "Add to Cart", "Buy Now", and primary checkout flows. On hover, darkens to `{colors.primary-active}` (#8f1f03). Disabled state fades to `{colors.primary-disabled}` (#f0b8a6) with reduced opacity. Height is 44px with 12px vertical padding and 24px horizontal, giving a compact but confident footprint.

**`button-secondary`** — Outlined variant with a white background, ink text, and a 2px hairline border. Used for "Learn More", "View Details", and secondary actions alongside primary buttons. Active state fills the background with `{colors.surface-soft}` and darkens the border to `{colors.muted}`.

**`button-ghost`** — Borderless text button with transparent background, used for tertiary actions like "Cancel", "Clear Filters", or dismiss actions. Hover state adds a soft background fill (`{colors.surface-soft}`) to indicate interactivity without competing with primary or secondary buttons.

**`button-accent-blue`** — Secondary accent button using `{colors.accent-blue}` (#0080ff), typically appearing in checkout flows (Shopify Pay integration) or informational CTAs. Active state shifts to `{colors.accent-blue-active}` (#2f6ed6).

**`button-sm`** — Compact 36px variant of the primary button, used in product cards, mini-carts, and inline actions. Maintains the same color logic but with tighter padding (8px vertical, 16px horizontal) and smaller typography.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft hairline border and 12px corner radius. Contains a square-ratio product image (top corners rounded), a title in `{typography.title-sm}`, and pricing in `{typography.body-md}` with weight 600. Sale prices render in `{colors.primary}`. On hover, the card elevates with a subtle box shadow and the border strengthens to `{colors.hairline}`. Badges (New, Sale, Out of Stock) overlay the top-left of the image area.

### Navigation
**`nav-bar`** — Fixed-height 64px white navigation bar with a soft bottom border. Logo left-aligned, nav links centered or right-aligned depending on viewport. Active nav links display the primary color with a 2px bottom border underline. On scroll, the bar gains a subtle box shadow for visual separation. Mobile navigation collapses into a hamburger menu with a full-screen overlay drawer.

**`category-strip`** — Horizontal scrollable strip of category tabs below the main nav, used for mouse series, accessories, and product type filtering. Active tabs show an underline in `{colors.primary}` with ink text; inactive tabs use `{colors.muted}`. The strip has a soft bottom border and 12px vertical padding.

### Forms
**`text-input`** — Standard text input with white background, 1px hairline border, 8px corner radius, and 48px height. On focus, the border becomes a 2px primary-colored stroke with no outline. Error state uses a 1px `{colors.error}` (#c00000) border. Placeholder text uses `{colors.muted}` (#989898).

**`select-dropdown`** — Matches the text-input dimensions and styling, used for product variant selection (size, switch type, color). The dropdown arrow is rendered in `{colors.muted}`.

**`quantity-selector`** — Compact 44px control with a central numeric display flanked by two 32px square buttons (minus/plus) on a soft background. Used on product detail pages and cart line items.

### Hero
**`hero-section`** — Full-width hero banner with a near-black (#111111) background and white text. Minimum height of 400px with generous section padding. Features a primary CTA (`{colors.primary}`) and an optional secondary outline CTA (white border on dark background). Product imagery or lifestyle photography sits within the hero, often bleeding to the edges.

### Badges
**`badge-new`** — Small uppercase label in `{colors.primary}` (#b12704) with white text, 4px corner radius, and tight 2px/6px padding. Used to flag newly released products on cards and listing pages.

**`badge-sale`** — Same shape and typography as `badge-new` but rendered in `{colors.error}` (#c00000) for discount or clearance indicators.

**`badge-out-of-stock`** — Neutral gray variant using `{colors.muted}` (#989898) for unavailable inventory states.

### Spec Table
**`spec-table`** — Structured data table used on product detail pages to display technical specifications (weight, dimensions, sensor type, battery life, etc.). Header row uses a soft background with uppercase, weight-700 labels. Alternating row backgrounds improve scanability. The table has a 1px soft border and 8px corner radius.

### Footer
**`footer-section`** — Full-width footer on a dark surface (`{colors.surface-dark}`, #212b35) with white text at 80% opacity for links. Link hover state increases opacity to 100% and shifts to `{colors.primary}`. Contains multi-column navigation, social links, and legal text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), hamburger nav, stacked hero layout, reduced section padding (32px), full-width cards, sticky bottom cart bar |
| Tablet | 744–1128px | Two-column product grid, expanded nav links (limited to 4-5), hero with side-by-side content, category strip horizontally scrollable |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, hero with large product imagery, spec tables side-by-side with description |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero content constrained to 1200px, additional whitespace around cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px touch target height
- Quantity selector buttons are 32px with adequate spacing to prevent mis-taps
- Category strip items have 48px minimum touch height for horizontal scrolling
- Mobile nav drawer links have 48px touch height with 8px vertical padding
- Product card CTAs are 44px minimum on mobile

### Collapsing Strategy
- Main navigation collapses to hamburger menu below 744px, with full-screen overlay drawer
- Product image gallery collapses from thumbnail strip to swipeable carousel on mobile
- Spec table collapses from side-by-side layout to stacked rows on tablet and below
- Footer columns collapse from 4-column grid to 2-column, then single column on mobile
- Category strip collapses from visible tabs to horizontally scrollable with fade indicators
- Hero section collapses from side-by-side (text + image) to stacked vertical layout on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by grays (#111111 through #ebebeb) and blues (#0080ff, #2f6ed6, #3d9ad1) that likely include Shopify checkout-widget colors, social-icon colors, and framework defaults. The most distinctive brand color is #b12704 (burnt orange-red), selected as primary, but its exact usage frequency on the live site could not be verified.
- Font-family declarations found only "Open Sans, sans-serif" — no weights, no fallback stack for display vs. body usage. The typography block uses reasonable Open Sans defaults; actual weight assignments may differ.
- No meta theme-color tag found — the brand may not use a browser chrome color, or it may be set dynamically.
- Hover, active, focus, and disabled states for all components are inferred from common patterns, not extracted from live CSS.
- Error state styling (form validation, error messages, inline errors) is not present in extracted data.
- Dark mode / high-contrast mode support is unknown.
- Sub-brand or product-series-specific color variants (e.g., X2, Xlite, Supergrip) may exist but are not captured.
- Animation durations, easing curves, and transition timing are not extracted.
- Icon system (SVG vs. icon font, stroke weights, sizes) is not documented.
- Shopify-specific components (cart drawer, checkout button, payment icons) use platform defaults that may override brand styling.
- Product swatch colors (mouse shell colors) are not extracted — these may vary by SKU and are likely managed as product metadata rather than design tokens.
