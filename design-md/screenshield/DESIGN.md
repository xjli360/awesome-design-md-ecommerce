---
version: alpha
name: "ScreenShield"
source_url: "https://www.screenshield.us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A protective-tech brand that wraps its products in a stark red-and-charcoal language — #ff0000 is the single voltage that marks every "Add to Cart" button, sale badge, and category highlight, set against a field of near-blacks (#1a1a1a, #222222, #252525, #2e2e2e, #303030) and cool grays (#e1e3e4, #d4d6d8, #8a8a8a, #677279). The palette reads like a tool kit: the red is urgent and precise, not warm; the grays are industrial, not soft. Montserrat runs at medium weights across headings and body, with Open Sans as a secondary for dense product specs and legal copy — both sans-serifs that lean technical rather than friendly. Cards and buttons use tight radii (`{rounded.sm}` at 8px, `{rounded.md}` at 12px) that feel machined, not pillowy — there is no `{rounded.full}` anywhere in the primary UI. The checkout flow introduces a secondary green (#11ae66, #00aa00, #008a00) for success states and "In Stock" badges, and a lighter red (#ee0000) for hover states on the primary action. Shopify's platform DNA shows in the `{rounded.sm}` text inputs and the `{spacing.base}`–`{spacing.lg}` grid gutters, but the brand overrides the default blue with its own red, green, and a slate-blue (#3d8cf4) that appears only in footer links and legal text. The overall impression is of a precision-instrument storefront — every edge accounted for, every color carrying a job.

colors:
  primary: "#ff0000"
  primary-active: "#ee0000"
  primary-disabled: "#f4534d"
  ink: "#1a1a1a"
  body: "#303030"
  muted: "#677279"
  muted-soft: "#8a8a8a"
  hairline: "#d4d6d8"
  hairline-soft: "#e1e3e4"
  canvas: "#ffffff"
  surface-soft: "#f3f5f6"
  surface-card: "#ffffff"
  surface-dark: "#222222"
  surface-darker: "#252525"
  surface-darkest: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#11ae66"
  success-active: "#008a00"
  success-bg: "#e1ffd0"
  error: "#f4534d"
  error-active: "#ee0000"
  link: "#3d8cf4"
  link-visited: "#00798e"
  badge-sale: "#ff0000"
  badge-new: "#00badb"
  star-rating: "#ff0000"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px
  link:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
    color: "{colors.primary}"
  spec:
    fontFamily: "'Open Sans', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
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
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-success-active:
    backgroundColor: "{colors.success-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid transparent"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    objectFit: cover
  product-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.primary}"
  product-compare-at-price:
    typography: "{typography.price}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 32px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
  breadcrumb-separator:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption-sm}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  pagination-disabled:
    backgroundColor: transparent
    textColor: "{colors.hairline}"
    typography: "{typography.button-sm}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-small:
    color: "{colors.primary}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (#ff0000) with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#ee0000) for a subtle darkening. Disabled state uses `{colors.primary-disabled}` (#f4534d) at 50% opacity. Used for "Add to Cart," "Buy Now," and primary checkout actions. Height is fixed at 48px with 12px/24px padding.

**`button-secondary`** — An outlined variant with white background, `{colors.ink}` text, and a 2px `{colors.hairline}` border. Active state thickens the border to `{colors.muted}`. Used for "Learn More," "View Details," and secondary form actions. Same 48px height as primary.

**`button-tertiary`** — A text-only button with no background or border, using `{colors.ink}` and `{typography.button-md}`. Used for "Cancel," "Clear," and inline actions where visual weight should be minimal.

**`button-success`** — Green variant using `{colors.success}` (#11ae66) for positive actions like "Confirm Order" or "Apply Coupon." Active state shifts to `{colors.success-active}` (#008a00). Same dimensions as primary.

**`button-pill`** — A compact, fully rounded variant (`{rounded.full}`) at 36px height, used for filter tags, category pills, and mobile navigation toggles. Uses `{typography.button-sm}` for tighter spacing.

### Cards
**`product-card`** — White card with `{rounded.sm}`, a 1px `{colors.hairline-soft}` border, and `{typography.body-sm}` for description text. On hover, the border strengthens to `{colors.hairline}` and a subtle shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card. The product image area uses `{rounded.sm}` on top corners only, with `object-fit: cover` for consistent aspect ratios.

**`product-title`** — Uses `{typography.title-sm}` (16px, weight 600) in `{colors.ink}`. Truncates to two lines on product-grid cards.

**`product-price`** — Uses `{typography.price}` (18px, weight 700) in `{colors.ink}`. Sale prices render in `{colors.primary}` via `product-price-sale`, with the original price shown as `product-compare-at-price` in `{colors.muted-soft}` with `text-decoration: line-through`.

### Navigation
**`nav-bar`** — Fixed-height 64px bar with white background, `{colors.ink}` nav links, and a 1px `{colors.hairline-soft}` bottom border. On scroll, a sticky variant adds a subtle shadow. Nav links use `{typography.nav-link}` (14px, weight 600, uppercase with 0.5px letter-spacing). Active links switch to `{colors.primary}`.

**`search-bar`** — Compact 40px input with `{colors.surface-soft}` background and `{rounded.sm}`. On focus, the background shifts to white and a 2px `{colors.primary}` border appears. Uses `{typography.body-md}` for placeholder and entered text.

**`breadcrumb`** — Inline navigation using `{typography.caption-sm}` in `{colors.muted}`, with `{colors.muted-soft}` separators. The active (current) breadcrumb uses `{colors.ink}`.

### Badges & Labels
**`badge-sale`** — Red badge on `{colors.badge-sale}` (#ff0000) background with white text, `{rounded.xs}`, and `{typography.badge}` (11px, weight 700, uppercase with 0.5px letter-spacing). Used for discount indicators and sale flags.

**`badge-new`** — Cyan badge on `{colors.badge-new}` (#00badb) background. Used for new product introductions.

**`badge-success`** — Green badge on `{colors.success-bg}` (#e1ffd0) background with `{colors.success}` text. Used for "In Stock" and "Available" labels.

**`badge-out-of-stock`** — Gray badge on `{colors.surface-soft}` background with `{colors.muted}` text. Used for unavailable items.

### Forms
**`text-input`** — Standard 48px input with white background, `{rounded.sm}`, and a 1px `{colors.hairline}` border. Active state uses a 2px `{colors.primary}` border. Error state uses a 2px `{colors.error}` (#f4534d) border. Uses `{typography.body-md}` for input text.

**`select-input`** — Same dimensions and styling as text-input, with a custom dropdown arrow in `{colors.muted}`.

**`textarea`** — Same styling as text-input but without a fixed height, allowing vertical resize.

**`quantity-selector`** — A 40px horizontal control with `{rounded.sm}` and a 1px `{colors.hairline}` border. Contains two `quantity-button` elements (32px, `{rounded.xs}`, `{colors.surface-soft}` background) flanking the numeric value.

### Footer
**`footer`** — Full-width section on `{colors.surface-darkest}` (#1a1a1a) background with white text. Uses `{typography.body-sm}` for body copy and `{typography.title-sm}` for column headings. Footer links use `{typography.link}` in `{colors.muted-soft}`, shifting to white on hover. Padding is `{spacing.section}` (64px) top and bottom.

### Hero
**`hero-section`** — Full-bleed section on `{colors.surface-dark}` (#222222) background with white text. Uses `{typography.display-xl}` (32px, weight 700) for the headline. The primary CTA (`hero-cta`) is 52px tall with `{typography.button-lg}` (18px, weight 600) and `{rounded.sm}`.

### Accordion
**`accordion`** — Collapsible sections with `{rounded.sm}`, a 1px `{colors.hairline-soft}` border, and `{typography.body-md}` for content. Headers use `{colors.surface-soft}` background with `{typography.title-sm}`. Content area uses white background with `{typography.body-sm}`.

### Loading & Dividers
**`loading-spinner`** — 24px animated spinner in `{colors.primary}`. A smaller 16px variant (`loading-spinner-small`) is used for inline loading states.

**`divider`** — 1px horizontal rule in `{colors.hairline-soft}`. A stronger variant (`divider-strong`) uses `{colors.hairline}` for more visual separation.

**`tooltip`** — Dark tooltip on `{colors.ink}` background with white text, `{rounded.xs}`, and `{typography.caption-sm}`. Padding is 4px horizontal and 8px vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-lg}`; buttons become full-width; footer stacks vertically; search bar moves to overlay |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links; hero maintains `{typography.display-xl}`; footer shows 2-column layout; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at full width; footer shows 4-column layout; search bar in nav |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero content max-width 1200px; footer max-width 1440px |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44px height for touch accessibility
- Product cards have 48px minimum tap area for "Add to Cart" and "Quick View" overlays
- Quantity selector buttons are 32px × 32px with 4px internal padding
- Mobile nav hamburger icon is 44px × 44px
- Filter and sort dropdowns on mobile use full-width 48px touch targets
- Pagination arrows are 40px × 40px

### Collapsing Strategy
- Primary nav collapses to a hamburger menu below 744px, with a full-screen overlay drawer
- Product filters collapse to a slide-out panel on mobile, triggered by a "Filter" button
- Product description, reviews, and specs collapse into accordion sections on mobile and tablet
- Footer columns collapse to a single column on mobile, with accordion-style section headers
- Hero section reduces padding from `{spacing.section}` to `{spacing.xl}` on mobile
- Product image galleries switch from thumbnail grid to swipeable carousel on mobile
- Search bar transforms from inline input to full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from the extracted color palette and common patterns; actual hover transitions (duration, easing) were not extractable
- Error and validation styling (error messages, success messages, inline validation) is based on the extracted error/success colors but exact implementations (iconography, positioning) are unknown
- Dark mode is not present on the live site; all dark surfaces are part of the light theme (footer, hero)
- Typography scale (font sizes, line heights, letter-spacing) is reconstructed from common Shopify patterns using Montserrat and Open Sans; exact values may vary from production
- Animation and transition specifications (durations, easing curves, micro-interactions) were not extractable
- Icon set and illustration style are not documented; the brand likely uses a custom icon set for product features and shipping icons
- Sub-brand or collection-specific color variations (e.g., for ScreenShield Pro, ScreenShield Glass+) were not extractable
- The extracted color list includes several greens (#11ae66, #00aa00, #008a00, #4ac30a, #00aa00) and a cyan (#00badb) that appear in checkout widgets and badges; exact usage rules for each green variant are inferred
- The blue (#3d8cf4) appears only in footer links and legal text; its hover state (#00798e) is inferred from the extracted dark teal
- Shopify's default checkout styling may override some form and button styles; the documented components represent the storefront experience only
- Font stack order (Montserrat vs Open Sans priority) is inferred from declaration frequency; exact fallback chain may differ
- Rounded corner values are reconstructed from common patterns; the extracted site uses `{rounded.sm}` (8px) for most elements but exact radii for cards, inputs, and buttons may vary by 2-4px
- Spacing scale is reconstructed from Shopify's default grid (16px base) and common e-commerce patterns; exact section padding and gutter values may differ
