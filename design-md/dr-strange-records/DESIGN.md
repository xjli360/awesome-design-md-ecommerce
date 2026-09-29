---
version: alpha
name: "Dr. Strange Records"
source_url: "https://www.drstrange.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-blue #3984c6 storefront that reads more like a rare-vinyl archive than a retail site — the single accent color, a saturated cobalt, appears on every add-to-cart button, category badge, and navigation highlight, giving the interface the focused energy of a collector's flashlight beam. The brand trusts its inventory photography over decorative imagery; product grids sit on a white canvas with minimal chrome, letting album art and sleeve condition speak. Type leans toward a clean, slightly condensed sans-serif at modest weights — body copy at 15px with generous line-height (1.6) keeps reading comfortable across long discography scrolls, while section headers at 24px weight 600 create clear hierarchy without shouting. Search is the primary navigation gesture, surfaced as a persistent pill-shaped input (`{rounded.full}`) in the top bar, reflecting a catalog-driven experience where customers arrive knowing what they want. Category strips use soft-pill badges (`{rounded.lg}`) in the primary blue against white, with secondary tags in muted gray for format (LP, 7", CD) and condition. The footer is unusually dense — a single-column stack of links, store policies, and social icons that reads like the back of a record sleeve. There is no hero carousel, no lifestyle photography, no promotional noise; the design assumes the visitor is already a convert, here to browse the stacks.

colors:
  primary: "#3984c6"
  primary-active: "#2a6da8"
  primary-disabled: "#a3c8e8"
  ink: "#1a1a1a"
  body: "#2d2d2d"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#e63946"
  badge-sale: "#2a9d8f"
  star-rating: "#f4a261"
  format-lp: "#3984c6"
  format-cd: "#6b6b6b"
  format-7inch: "#e63946"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 5px 15px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 9px 13px
  text-input-error:
    border: "1px solid {colors.badge-new}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 18px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    padding: 9px 17px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.lg}"
    padding: 4px 12px
  category-badge-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.lg}"
    padding: 4px 12px
  format-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  format-badge-lp:
    backgroundColor: "{colors.format-lp}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  format-badge-cd:
    backgroundColor: "{colors.format-cd}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  format-badge-7inch:
    backgroundColor: "{colors.format-7inch}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.xxs} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.sm} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.sm}"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base} 0"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} 0"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    padding: "{spacing.base} 0 {spacing.sm} 0"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-hover:
    textColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.base} 0"
  breadcrumb-active:
    textColor: "{colors.ink}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    height: 24px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Submit" actions. Rendered in the brand cobalt `{colors.primary}` with white text and a subtle 6px radius (`{rounded.sm}`). On hover, shifts to `{colors.primary-active}` (#2a6da8) for a darker, more grounded state. Disabled state uses `{colors.primary-disabled}` (#a3c8e8) with full opacity — no transparency.

**`button-secondary`** — An outlined alternative for secondary actions like "Save for Later" or "View Details". White background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Active state fills with `{colors.surface-soft}` and darkens the border to `{colors.muted}`.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Clear Filters" and "Cancel". No background, `{colors.primary}` text, and no border. Hover adds underline.

**`button-pill-primary`** — Full-pill variant used for category tags and filter chips. Smaller padding (6px 16px) with `{typography.button-sm}`. Active state uses `{colors.primary}`; inactive uses `{colors.canvas}` with a `{colors.hairline}` border.

### Navigation
**`nav-bar`** — A fixed 64px header with white background and a subtle bottom border (`{colors.hairline-soft}`). Contains the store logo (left), primary nav links (center), and cart icon with badge (right). The logo is a text-based wordmark in `{colors.ink}` at `{typography.display-md}` weight.

**`nav-link`** — Inline navigation items with 8px 12px padding and `{rounded.sm}`. Default state is transparent with `{colors.ink}` text. Active state uses `{colors.surface-soft}` background and `{colors.primary}` text to indicate the current section.

**`breadcrumb`** — Secondary navigation for product category pages. `{typography.caption}` in `{colors.muted}`, with the current page rendered in `{colors.ink}`. Separators are "›" in `{colors.muted-soft}`.

### Cards
**`product-card`** — The core inventory display unit. A white card with `{rounded.md}` (8px) corners and no shadow — the brand relies on grid spacing (`{spacing.base}` gap) and album art contrast for visual separation. The image occupies the top with a 1:1 aspect ratio and `object-fit: cover`. Below: title (`{typography.title-sm}`), artist (`{typography.body-sm}` in `{colors.muted}`), and price (`{typography.price}` in `{colors.ink}`). A `{rounded.lg}` badge (new, sale, or format) can overlay the top-left of the image.

### Forms
**`text-input`** — Standard input field for search, checkout forms, and account pages. White background, `{colors.ink}` text, 42px height, and a `{colors.hairline}` border. Focus state thickens the border to 2px `{colors.primary}`. Error state uses `{colors.badge-new}` (#e63946) border.

**`search-bar-pill`** — The primary search interface, a persistent pill-shaped input in the top nav. `{colors.surface-soft}` background with a `{colors.hairline}` border. On focus, background shifts to white and border becomes 2px `{colors.primary}`. Placeholder text in `{colors.muted-soft}`.

### Badges
**`category-badge`** — Pill-shaped tags for record categories (Rock, Jazz, Soul, etc.). `{colors.primary}` background with white uppercase text at 11px. Inactive state uses `{colors.surface-soft}` background with `{colors.muted}` text.

**`format-badge`** — Smaller rectangular badges for media format (LP, CD, 7"). Each format has a distinct color: LP in `{colors.format-lp}` (#3984c6), CD in `{colors.format-cd}` (#6b6b6b), 7" in `{colors.format-7inch}` (#e63946). Default (unselected) uses `{colors.surface-soft}` with `{colors.muted}` text.

### Footer
**`footer`** — A dense, dark footer on `{colors.ink}` background. Links in `{colors.muted-soft}` with `{typography.link}` sizing. Section headings in white `{typography.title-sm}`. Social icons are circular (`{rounded.full}`) at 32px, defaulting to `{colors.muted-soft}` and transitioning to white on hover. The footer stacks vertically on mobile with `{spacing.lg}` between sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger, footer stacks vertically, search bar moves below logo, category badges wrap to 2 rows |
| Tablet | 744–1128px | Two-column product grid, nav links visible (limited to 4), search bar inline with logo, footer in 2 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, persistent search bar, footer in 3 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, footer in 4 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height on mobile
- Cart icon badge is 18px minimum with 4px touch padding
- Category badges are 28px minimum height
- Filter dropdowns are 36px minimum height
- Pagination buttons are 36px minimum height

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Category filter strip collapses to a single "Filter" dropdown button below 744px
- Product grid columns reduce from 4 → 3 → 2 → 1 as viewport narrows
- Footer columns reduce from 4 → 3 → 2 → 1
- Search bar collapses from inline to full-width below the logo on mobile
- Breadcrumb truncates with "..." on mobile, showing only current page and parent

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#3984c6) was extracted from the live site; the full palette above is inferred from common e-commerce patterns and record-store conventions. The actual secondary colors, error states, and surface tones may differ.
- No font-family declarations were reliably extracted; Inter is assumed as a common modern sans-serif. The actual typeface may be different (e.g., system fonts, a custom face).
- Hover and focus states for all components are inferred from standard web patterns, not extracted from the live site.
- No dark mode or high-contrast mode tokens were found.
- The checkout flow (cart page, payment forms, order confirmation) was not analyzed and may use different styling.
- No animation or transition timing values were extracted.
- The actual spacing scale, rounded corner values, and component dimensions are estimated based on common DTC patterns and may not match the live site exactly.
- No data on error messaging, empty states, or loading skeletons was available.
- The brand's logo (text vs. image) and its exact styling could not be determined.
