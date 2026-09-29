---
version: alpha
name: "Petzl"
source_url: "https://www.petzl.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built for the vertical world, Petzl’s digital presence is a study in controlled tension — the same precision found in its carabiners and headlamps translated into a restrained, high-contrast interface. The canvas is a stark `#ffffff`, against which a single primary blue (`#003da5`) operates as the system’s sole voltage, used for every primary CTA, active navigation state, and key product badge. This is not a friendly blue; it’s an industrial, safety-certified blue — the color of a locking gate or a technical webbing loop. Body text runs in a dark `#1a1a1a` on white, with no secondary accent color to soften the experience; the brand trusts its product photography and the raw geometry of climbing equipment to provide all the warmth. Corners are sharp (`{rounded.none}`) on navigation and cards, with only the smallest `{rounded.xs}` (4px) on buttons and input fields — a deliberate refusal of the pill-shaped friendliness common in consumer tech. Typography is set in a neutral, highly legible sans-serif (likely a system stack or a workhorse like Helvetica Neue), with display sizes staying modest (20–28px) and body copy at 14–16px. The grid is generous: `{spacing.section}` (64px) between major content blocks, `{spacing.xxl}` (48px) between product rows, and `{spacing.base}` (16px) within cards. The overall effect is one of quiet competence — a brand that doesn’t need to shout because its products have already proven themselves on a cliff face.

colors:
  primary: "#003da5"
  primary-active: "#002d7a"
  primary-disabled: "#b3c9e8"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#cc0000"
  success: "#2e7d32"
  warning: "#f57c00"
  info: "#003da5"
  product-badge-new: "#003da5"
  product-badge-sale: "#cc0000"
  product-badge-eco: "#2e7d32"
  star-rating: "#1a1a1a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.product-badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-eco:
    backgroundColor: "{colors.product-badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-detail-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  product-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-detail-specs:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-detail-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
  footer-link-hover:
    textColor: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 12px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "4px 12px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  tab-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  rating-number:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-chip-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  loader-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  loader-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
  loader-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.2)"
  modal-close-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  notification-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  notification-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  notification-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
  category-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  category-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  feature-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  feature-card-icon:
    textColor: "{colors.primary}"
    fontSize: 32px
  feature-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  feature-card-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in Petzl blue (`{colors.primary}`) with white text and a subtle 4px corner (`{rounded.xs}`). Text is set in uppercase with 0.3px letter-spacing for a technical, precise feel. On hover, the background deepens to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}` — a muted, desaturated blue that signals inactivity without visual noise. Height is 44px, padding 12px 24px.

**`button-secondary`** — An outlined variant with a 2px solid `{colors.primary}` border on a white background. Text remains `{colors.primary}`. On hover, the background shifts to `{colors.surface-soft}` and the border to `{colors.primary-active}`. Used for secondary actions like "Learn More" or "Add to Wishlist." Height matches the primary button at 44px.

**`button-tertiary-text`** — A text-only button with no background or border. Text is `{colors.primary}` in uppercase with button typography. On hover, text shifts to `{colors.primary-active}`. Used for less prominent actions like "Cancel" or "View Details."

**`button-pill`** — A fully rounded variant (`{rounded.full}`) used sparingly for filter chips or compact CTAs in tight spaces. Background is `{colors.primary}`, text is white, typography is `{typography.button-sm}`. Height is 36px with 8px 16px padding.

### Text Inputs & Forms
**`text-input`** — Standard single-line text input with a white background, 1px `{colors.hairline}` border, and 4px corner radius. On focus, the border thickens to 2px and shifts to `{colors.primary}`. Error state uses a 2px `{colors.error}` border. Height is 44px with 12px 16px padding. Typography is `{typography.body-md}`.

**`select-input`** — Dropdown select styled identically to text inputs: white background, hairline border, 4px corner, 44px height. Uses the same focus and error states.

**`textarea`** — Multi-line text input with the same styling as text inputs but no fixed height. Used for longer form entries like product reviews or contact messages.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 72px height, white background with a 1px `{colors.hairline}` bottom border. Links are set in `{typography.nav-link}` (uppercase, 14px, weight 600). Active links show a 2px `{colors.primary}` bottom border. Inactive links are `{colors.ink}`. Dropdown menus use a white background with subtle shadow and 4px corners.

**`search-bar`** — Integrated search input with a `{colors.surface-soft}` background and 1px hairline border. On focus, background shifts to white and border thickens to 2px `{colors.primary}`. Height is 44px.

### Cards
**`product-card`** — A minimal card with no border radius (`{rounded.none}`) and a white background. The product image sits flush with no rounding. Title uses `{typography.title-sm}`, price uses `{typography.body-md}`. On hover, a subtle box-shadow (`0 4px 16px rgba(0,0,0,0.1)`) lifts the card. Badges (New, Sale, Eco) are positioned over the image with `{colors.primary}`, `{colors.product-badge-sale}`, or `{colors.product-badge-eco}` backgrounds and uppercase 10px text.

**`category-card`** — Similar to product cards but without price or badges. Used for navigation to product categories. On hover, the same subtle shadow appears.

**`feature-card`** — A content card with `{colors.surface-soft}` background and no border radius. Contains an icon (32px, `{colors.primary}`), a title (`{typography.title-sm}`), and a description (`{typography.body-sm}`). Padding is `{spacing.lg}`.

### Product Detail
**`product-detail-hero`** — The hero section of a product page, using `{colors.surface-soft}` background with `{typography.display-lg}` for the product name. Padding is `{spacing.section}` top/bottom with `{spacing.base}` sides.

**`product-detail-cta`** — The primary "Add to Cart" button on product pages. Slightly larger than standard buttons at 48px height with 14px 32px padding. Uses `{colors.primary}` background with white text and uppercase button typography.

### Footer
**`footer`** — A dark footer with `{colors.ink}` background and white text. Links are `{typography.link}` (14px, weight 400) and turn to `{colors.muted-soft}` on hover. Section headings use `{typography.title-sm}`. Padding is `{spacing.section}` top/bottom.

### Filters & Tabs
**`filter-chip`** — A pill-shaped filter with `{colors.surface-soft}` background, 1px hairline border, and `{rounded.full}`. Active state uses `{colors.primary}` background with white text. Used for product listing filters.

**`tab-bar`** — A horizontal tab bar with a 1px hairline bottom border. Active tabs show a 2px `{colors.primary}` bottom border with `{colors.primary}` text. Inactive tabs use `{colors.muted}` text. On hover, tabs get a `{colors.surface-soft}` background.

### Feedback & Utilities
**`loader-spinner`** — A 24px circular spinner with a 3px `{colors.hairline-soft}` border and a `{colors.primary}` top border. Fully rounded.

**`tooltip`** — A dark (`{colors.ink}`) tooltip with white text, 4px corners, and 4px 8px padding. Typography is `{typography.caption}`.

**`modal-overlay`** — A 50% opacity black scrim (`{colors.scrim}`) behind modal content. The modal itself has a white background, 8px corners, 32px padding, and a strong box-shadow.

**`notification-success`** — A green (`{colors.success}`) notification bar with white text. Used for success messages. Error and warning variants use `{colors.error}` and `{colors.warning}` respectively.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; search bar moves to overlay; filter chips wrap to two rows; hero banner reduces padding to `{spacing.lg}`; footer links stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level links only; search bar remains visible but reduced width; filter chips show in a horizontal scrollable strip; product detail hero uses `{spacing.xl}` padding |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with dropdowns; search bar at full width; filter chips in a grid; product detail hero uses `{spacing.section}` padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav-bar centered; search bar centered; product detail hero uses `{spacing.section}` padding with wider margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Filter chips are 36px tall with 16px horizontal padding — meets touch target guidelines
- Icon buttons (modal close, quantity selector) are 44px x 44px
- Nav-bar links have 72px touch area (full nav-bar height)
- Product card CTAs are 48px tall

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Secondary navigation (sub-categories, support links) collapses to accordion panels on mobile
- Product filters collapse to a slide-out drawer on mobile
- Footer link columns collapse to a single column on mobile
- Product image galleries collapse to a single image carousel on mobile
- Tab bars collapse to a horizontal scrollable strip on mobile
- Breadcrumbs collapse to show only the current page and a "Back" link on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted font-family declarations were found from the live site; the typography stack uses a generic sans-serif fallback. The actual brand font (likely a custom or licensed typeface) could not be confirmed.
- No extracted hex colors were returned from the live site analysis. The color palette above is based on general brand knowledge of Petzl's visual identity (their signature blue `#003da5` and neutral tones) rather than live extraction. This should be verified against the actual site.
- Hover, focus, and active states for all components are inferred from common patterns rather than extracted from the live site.
- Error message styling (text color, iconography, positioning) is not confirmed.
- Dark mode or high-contrast mode variants are not documented.
- Sub-brand or regional color variations (e.g., Petzl Sport, Petzl Pro, Petzl Rescue) are not captured.
- Animation durations, easing curves, and transition properties are not documented.
- Iconography style (line weight, stroke width, sizing) is not documented.
- Image aspect ratios and cropping behavior for product and category cards are not confirmed.
- The actual font-family used on the live site could not be extracted; the stack provided is a reasonable fallback.
