---
version: alpha
name: "Reaper Miniatures"
source_url: "https://www.reapermini.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A tabletop RPG miniature manufacturer that operates with the blunt, no-nonsense authority of a warehouse built for hobbyists who know exactly what they want. The palette is dominated by a battleship gray canvas (#f5f5f5) and near-black ink (#0a0a0a), with a single, unmistakable brand voltage in #cc0000 — a deep, dried-blood red that appears on primary CTAs, sale badges, and the site's critical action points. This is not a friendly e-commerce pastel; it's the color of a warning label or a critical hit. Supporting accents like #3273dc (a flat, utilitarian blue) and #00d1b2 (a teal-green) come from the Bulma CSS framework, but the brand has adopted them as its own for secondary actions and success states. The typography stack is a defensive, system-first cascade — `-apple-system, BlinkMacSystemFont, Helvetica Neue, Arial, sans-serif` — that prioritizes legibility over personality, a deliberate choice for a catalog-heavy site where product images must do the talking. Cards and buttons use modest `{rounded.sm}` corners, never the pill shapes of consumer brands; the search bar is a simple `{rounded.sm}` rectangle. The overall impression is that of a tool, not a destination — a dense, information-rich interface where the #cc0000 red acts as a beacon for "buy now" and "sale," and everything else recedes into the gray.

colors:
  primary: "#cc0000"
  primary-active: "#990000"
  primary-disabled: "#e6b3b3"
  ink: "#0a0a0a"
  body: "#363636"
  muted: "#4a4a4a"
  muted-soft: "#7a7a7a"
  hairline: "#dbdbdb"
  hairline-soft: "#e8e8e8"
  canvas: "#f5f5f5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#23d160"
  info: "#3273dc"
  warning: "#ffdd57"
  danger: "#ff3860"
  link: "#209cee"
  sale-badge: "#cc0000"
  new-badge: "#00d1b2"
  out-of-stock: "#959595"
  price: "#363636"
  sale-price: "#cc0000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 10px 20px
    height: 40px
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
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.info}"
    boxShadow: "0 0 0 2px rgba(50, 115, 220, 0.25)"
  text-input-error:
    border: "1px solid {colors.danger}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 32px 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    border: "1px solid {colors.hairline}"
  checkbox:
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    backgroundColor: "{colors.canvas}"
  checkbox-checked:
    backgroundColor: "{colors.info}"
    border: "1px solid {colors.info}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-bar-link-active:
    textColor: "{colors.canvas}"
  nav-bar-link-hover:
    textColor: "{colors.canvas}"
  nav-bar-dropdown:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.price}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.sale-price}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
  product-card-badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
  product-card-badge-out-of-stock:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.info}"
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 16px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 24px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-disabled:
    textColor: "{colors.muted-soft}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  breadcrumb-link:
    textColor: "{colors.link}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
  badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
  badge-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
  badge-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
  badge-out-of-stock:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.on-primary}"
  table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textTransform: uppercase
  table-row-hover:
    backgroundColor: "{colors.hairline-soft}"
  table-row-stripe:
    backgroundColor: "{colors.surface-soft}"
  table-border:
    border: "1px solid {colors.hairline}"
  alert:
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-success:
    backgroundColor: "#e6ffe6"
    textColor: "{colors.success}"
    border: "1px solid {colors.success}"
  alert-info:
    backgroundColor: "#e6f2ff"
    textColor: "{colors.info}"
    border: "1px solid {colors.info}"
  alert-warning:
    backgroundColor: "#fff9e6"
    textColor: "#8a6d00"
    border: "1px solid {colors.warning}"
  alert-danger:
    backgroundColor: "#ffe6e6"
    textColor: "{colors.danger}"
    border: "1px solid {colors.danger}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "rgba(10, 10, 10, 0.86)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  modal-close:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  progress-bar-fill-success:
    backgroundColor: "{colors.success}"
  spinner:
    border: "2px solid {colors.hairline}"
    borderTop: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature #cc0000 red on a white background. Used for "Add to Cart," "Buy Now," and primary checkout flows. On hover, it darkens to #990000 (`{colors.primary-active}`). The disabled state uses a pale pink `{colors.primary-disabled}` to signal inactivity without visual noise. Text is set in `{typography.button-md}` (14px, weight 600) with 0.5px letter spacing for a slightly tighter, more authoritative feel. The button has `{rounded.sm}` corners and a compact 40px height.

**`button-secondary`** — A ghost button with a transparent background and a 2px `{colors.hairline}` border. Used for "View Details," "Cancel," and secondary actions that should not compete with the primary. On hover, the background fills with `{colors.hairline}`. The height and typography match `button-primary` for consistent alignment in forms and toolbars.

**`button-link`** — A text-only button styled as a link, using `{colors.link}` (#209cee) and `{typography.link}`. Used for "Learn More" and inline actions within product descriptions or cards. No background, no border.

**`button-success`, `button-danger`, `button-warning`, `button-info`** — Semantic action buttons using the Bulma framework's accent colors. `button-success` (#23d160) is used for "Confirm" or "Save" actions. `button-danger` (#ff3860) is used for destructive actions like "Delete" or "Remove from Cart." `button-warning` (#ffdd57) is used for "Add to Wishlist" or "Notify Me." `button-info` (#3273dc) is used for "More Info" or "Learn More" on product pages. All share the same `{rounded.sm}` shape and 40px height.

**`button-small`** — A compact 28px version of the primary button, used in table rows, inline forms, and quantity selectors. Uses `{typography.button-sm}` (12px, weight 600) and `{rounded.xs}`.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. Contains a product image with `{rounded.sm}` on a `{colors.surface-soft}` background, a title in `{typography.title-sm}`, and a price in `{typography.body-md}`. Sale prices are rendered in `{colors.sale-price}` (#cc0000). On hover, the card gains a subtle box shadow. Badges (sale, new, out-of-stock) are positioned at the top-left of the image, using `{typography.badge}` (11px, weight 700, uppercase) with `{rounded.xs}`.

**`product-card-badge-sale`** — A red badge (`{colors.sale-badge}`) with white text, used to indicate discounted items. The badge is compact (2px/6px padding) and positioned absolutely on the card image.

**`product-card-badge-new`** — A teal badge (`{colors.new-badge}`) with white text, used for newly released miniatures. The teal (#00d1b2) provides a clear visual distinction from the sale red.

**`product-card-badge-out-of-stock`** — A gray badge (`{colors.out-of-stock}`) with white text, used for unavailable items. The muted gray signals unavailability without the urgency of red.

### Navigation
**`nav-bar`** — A dark, full-width navigation bar with a `{colors.ink}` (#0a0a0a) background and white text. Links are set in `{typography.nav-link}` (14px, weight 600, uppercase) with 0.5px letter spacing, giving the navigation a utilitarian, warehouse-directory feel. The active link is white, inactive links are `{colors.muted-soft}` (#7a7a7a). The bar is 56px tall, compact enough to leave maximum vertical space for product imagery.

**`nav-bar-dropdown`** — A dropdown menu that appears on hover over nav links. Uses the same `{colors.ink}` background as the nav bar, with `{rounded.sm}` corners and `{typography.body-sm}` for dropdown items.

### Forms
**`text-input`** — A standard text input with a white background, `{colors.body}` text, and a 1px `{colors.hairline}` border. On focus, the border changes to `{colors.info}` (#3273dc) with a 2px blue box-shadow ring. Error states use a `{colors.danger}` (#ff3860) border. The input is 40px tall with 8px/12px padding.

**`select-input`** — A dropdown select styled to match the text input, with an additional 32px of right padding to accommodate a custom dropdown arrow. Same 40px height and border styling.

**`textarea`** — A multi-line text input with the same styling as `text-input`, but without a fixed height.

**`checkbox`** — A square checkbox with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. When checked, the background fills with `{colors.info}` (#3273dc).

### Search
**`search-bar`** — A simple rectangular search input with `{rounded.sm}` corners, matching the text input styling. On focus, the border shifts to `{colors.info}`. The search button is a `{colors.primary}` red rectangle with white text, positioned to the right of the input.

### Footer
**`footer`** — A dark footer matching the nav bar's `{colors.ink}` background, with `{colors.muted-soft}` link text. Links lighten to white on hover. The footer uses `{typography.body-sm}` for text and `{typography.link}` for links.

### Tables
**`table`** — A standard data table with `{colors.canvas}` background and `{colors.body}` text. Headers use `{colors.surface-soft}` background with `{typography.caption}` (uppercase, weight 400). Rows have alternating `{colors.surface-soft}` stripes, and hover states use `{colors.hairline-soft}`. Borders are 1px `{colors.hairline}`.

### Alerts & Feedback
**`alert-success`, `alert-info`, `alert-warning`, `alert-danger`** — Contextual alert banners with light background tints and colored borders. Success uses a green tint with `{colors.success}` border, info uses blue with `{colors.info}`, warning uses yellow with `{colors.warning}`, and danger uses red with `{colors.danger}`. All have `{rounded.sm}` corners and `{typography.body-sm}`.

**`tooltip`** — A dark tooltip with `{colors.ink}` background and white text, using `{typography.caption}` and `{rounded.xs}`. Positioned above or below the target element.

**`modal-overlay`** — A semi-transparent black overlay (86% opacity) that covers the screen behind a modal. The modal content is a white card with `{rounded.md}` corners and `{spacing.lg}` padding. The close button is a circular 32px icon with `{colors.hairline}` background.

**`progress-bar`** — A thin 8px progress bar with `{rounded.full}` corners. The fill uses `{colors.primary}` by default, with a `progress-bar-fill-success` variant using `{colors.success}` for completed states.

**`spinner`** — A 24px circular spinner with a `{colors.hairline}` border and a `{colors.primary}` top border, indicating loading states.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Single-column product grid (1 column). Nav bar collapses to hamburger menu. Search bar moves below nav. Footer stacks vertically. Product cards stack full-width. Hero banner reduces padding. |
| Tablet | 768–1024px | Two-column product grid. Nav bar remains horizontal but with reduced link spacing. Search bar is full-width below nav. Footer columns collapse to 2. Product cards show in 2-column grid. |
| Desktop | 1024–1440px | Three-column product grid. Full nav bar with all links visible. Search bar is inline in nav. Footer shows 4-column layout. Product cards show in 3-column grid with hover effects. |
| Wide | > 1440px | Four-column product grid. Maximum content width of 1440px centered. Nav bar has additional spacing. Product cards show in 4-column grid with full hover states. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 40px to meet touch target guidelines.
- Nav bar links have a minimum tap area of 44x44px.
- Checkbox and radio inputs have a minimum 24x24px tap area.
- Close buttons on modals are 32x32px minimum.
- Pagination buttons are 32x32px minimum.

### Collapsing Strategy
- On mobile (< 768px), the top nav bar collapses into a hamburger menu with a slide-out drawer.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile.
- The footer collapses from 4 columns on desktop to a single column on mobile.
- The hero banner collapses from a full-width layout to a stacked layout on mobile.
- Search functionality collapses from an inline search bar on desktop to a full-width bar below the nav on mobile.
- Table views on mobile may collapse to card-style layouts for better readability.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While hover states for buttons and cards are defined, hover states for nav bar dropdowns, footer links, and table rows are inferred from common patterns and may differ from the live site.
- **Error states**: Form validation error states (text-input-error) are defined, but the exact error message styling, iconography, and placement are not confirmed from the extracted data.
- **Dark mode**: No dark mode variant is defined. The site appears to use a light-only color scheme.
- **Sub-brand palettes**: Reaper Miniatures may have sub-brands or product lines (e.g., Bones, Dark Heaven, Pathfinder) with their own color treatments. These are not captured.
- **Typography weights and sizes**: The exact font sizes and weights for display and body text are estimated based on common e-commerce patterns and the extracted font stack. The live site may use different values.
- **Iconography**: No icon set is defined. The site likely uses Font Awesome or a custom icon set for cart, search, and social icons, but specific icon styles and sizes are unknown.
- **Animation and transitions**: Transition durations, easing functions, and animation styles are not extracted. The site likely uses simple CSS transitions for hover states.
- **Checkout flow**: The checkout process may use a different color scheme or component set (e.g., Shopify's default checkout). The extracted colors include some that may belong to third-party payment widgets.
- **Accessibility**: Focus ring styles, skip-to-content links, and ARIA labels are not defined. The site's accessibility implementation is unknown.
- **Print styles**: No print-specific styles are defined. Product pages may have print-friendly layouts for reference sheets.
- **Custom fonts**: The extracted font stack is entirely system fonts. The site may use a custom web font (e.g., a display font for headings) that was not detected in the extraction.
