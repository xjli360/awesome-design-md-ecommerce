---
version: alpha
name: "Genki Buy"
source_url: "https://www.genkibuy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-performance PC and peripherals import shop that wears its Japanese-gaming enthusiasm on its sleeve through a deep indigo primary (#003388) — a color that reads as midnight-blue confidence rather than corporate navy, and appears across header bars, category badges, and primary CTAs. The palette leans cool and technical: a secondary blue (#0274be) for interactive hover states, a near-black ink (#222222) for body copy, and a sharp accent red (#fd1949) that snaps attention to sale tags, stock warnings, and limited-edition indicators. Surfaces stack from a clean white canvas (#fafafa) through soft grays (#efefef, #f1f1f1) to a darker surface (#e6e6e6) for footer and secondary panels, creating a layered hierarchy that feels like a well-organized electronics catalog. Typography runs Montserrat for display headings — a geometric sans-serif that echoes the angular lines of PC hardware — with Open Sans for body text, both set at moderate weights (400–600) to keep the interface readable during long browsing sessions. Product cards use `{rounded.sm}` corners and thin `{colors.hairline}` borders, while the search bar and primary CTA buttons adopt `{rounded.md}` for a slightly softer, approachable feel. The brand’s distinctive purple accent (#221155) appears sparingly — in the logo mark, selected navigation elements, and the "Genki" wordmark — adding a subtle otaku-culture nod without overwhelming the technical aesthetic. Checkout flows and cart summaries sit on `{colors.surface-card}` white with `{colors.hairline-soft}` dividers, keeping the transaction experience clean and trustworthy. The overall impression is of a store that knows its audience: enthusiasts who appreciate both raw specs and thoughtful design, where every pixel serves the goal of getting the right GPU or mechanical keyboard into the cart.

colors:
  primary: "#003388"
  primary-active: "#0274be"
  primary-disabled: "#808285"
  ink: "#222222"
  body: "#3a3a3a"
  muted: "#454f5e"
  muted-soft: "#808285"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#fafafa"
  surface-soft: "#efefef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#fd1949"
  accent-purple: "#221155"
  accent-cyan: "#05c2fc"
  deep-navy: "#003366"
  dark-bg: "#272138"
  dark-surface: "#0d0614"
  error: "#a90707"
  warning-bg: "#f2f0fe"
  warning-border: "#d8d8f5"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Montserrat', 'Red Hat Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.price-sm}"
    padding: "{spacing.xs} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-badge-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-accent:
    backgroundColor: "{colors.accent-purple}"
  stock-badge-instock:
    backgroundColor: "#e8f5e9"
    textColor: "#2e7d32"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  stock-badge-low:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.accent-purple}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  stock-badge-out:
    backgroundColor: "#ffebee"
    textColor: "{colors.error}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  cart-count-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Buy Now," and checkout progression. Rendered in deep indigo (`{colors.primary}`) with white uppercase Montserrat text at 14px/600. On hover, shifts to `{colors.primary-active}` (#0274be) — a lighter, more electric blue that signals interactivity. Disabled state drops to `{colors.primary-disabled}` (#808285), a muted gray that clearly indicates non-interactivity without ambiguity. The `{rounded.md}` (12px) corners give the button a modern, slightly softened edge that contrasts with the angular hardware imagery.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later." Uses a white fill with a 2px `{colors.primary}` border and matching indigo text. On hover, the background fills with `{colors.primary}` and text inverts to white. Maintains the same 44px height and `{rounded.md}` corners as the primary button for visual consistency in form layouts.

**`button-accent-red`** — A compact, high-urgency button reserved for limited-time offers, flash sales, and pre-order alerts. Uses `{colors.accent-red}` (#fd1949) as background with white text in `{typography.button-sm}` (12px uppercase). Smaller padding (8px 16px) and 36px height allow it to sit inline within product cards or alert banners without disrupting the layout.

### Navigation
**`nav-bar`** — A fixed-position top bar at 72px height with a white background and subtle bottom border (`{colors.hairline}`). On scroll, gains a light box-shadow for depth separation. Contains the logo (featuring `{colors.accent-purple}`), navigation links, search bar, and cart icon with count badge. The logo area uses a 40px height constraint to maintain alignment.

**`nav-link`** — Standard navigation items in Montserrat 14px/500 with 8px 12px padding. Active state receives a 2px bottom border in `{colors.primary}` and the text color shifts to match, creating a clear "you are here" indicator without a background pill.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a light gray background (`{colors.surface-soft}`) and subtle border. On focus, the background turns white and the border thickens to 2px in `{colors.primary}`, providing clear focus indication. The 44px height matches button heights for alignment in the nav bar.

### Product Cards
**`product-card`** — The core content unit for the product grid, rendered as a white card with `{rounded.sm}` (8px) corners and a 1px `{colors.hairline}` border. On hover, the card lifts with a subtle box-shadow and the border shifts to `{colors.primary}`, creating a selection effect without animation overhead. The image area occupies the top 200px with rounded top corners only, followed by title and price in the padding structure.

**`product-card-badge`** — A small red badge overlaid on the product image for "Sale," "New," or "Limited" indicators. Uses `{colors.accent-red}` background with white uppercase text at 11px/700. The `{rounded.xs}` (4px) corners keep it sharp and technical-looking.

**`category-badge`** — Pill-shaped category filters used in the sidebar or top strip. Active badges use `{colors.primary}` fill with white text; inactive badges use `{colors.surface-soft}` background with `{colors.muted}` text. Both share the same `{rounded.full}` shape and 4px 12px padding for consistent horizontal rhythm.

### Forms & Inputs
**`text-input`** — Standard text input fields for search, account forms, and checkout. White background with 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border expands to 2px `{colors.primary}`. Error state uses a 2px `{colors.error}` (#a90707) border. The 44px height matches button heights for aligned form layouts.

**`stock-badge-*`** — Three variants indicating product availability. Green-tinted for "In Stock," purple-tinted for "Low Stock" (matching `{colors.warning-bg}` and `{colors.accent-purple}`), and red-tinted for "Out of Stock." All use `{rounded.xs}` corners and `{typography.caption-bold}` for compact inline display.

### Footer
**`footer`** — A dark section anchored by `{colors.dark-bg}` (#272138) with white text. Links use `{colors.muted-soft}` (#808285) and lighten to white on hover. The footer contains three columns: customer service links, product categories, and newsletter signup. The newsletter input matches the `text-input` style but with a dark background variant.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), hamburger nav replaces full nav links, search bar collapses to icon-only, footer stacks vertically, hero section reduces padding to 32px |
| Tablet | 744–1128px | Two-column product grid, nav links show top 4 items with "More" dropdown, search bar remains full-width but shorter, footer splits into 2 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, search bar at 400px max-width, footer in 3 columns, hero section at full padding (64px) |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, search bar expands to 500px max-width, category strip shows all badges without overflow |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are at least 48px tall in their hit areas
- Nav links have 44px minimum touch height despite 14px font size
- Cart icon and search icon buttons are 44x44px with 20px icon size
- Category badges in mobile filter strip are 36px tall with 8px horizontal padding

### Collapsing Strategy
- Top nav links collapse to hamburger menu at < 744px, with the logo and cart icon remaining visible
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows
- Category filter strip collapses from horizontal scroll to a dropdown select at < 744px
- Footer columns collapse from 3 → 2 → 1 at tablet breakpoints
- Hero section reduces from 64px padding to 32px on mobile, and the secondary headline may be hidden
- Search bar collapses from full input to icon-only on mobile, expanding on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (especially secondary buttons, links, and form inputs) could not be fully extracted from the live site; the above hover states are inferred from common patterns
- Error state styling for form validation (error messages, iconography, border colors) is assumed based on the extracted error red (#a90707) but not confirmed
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or seasonal color palettes (e.g., holiday themes, collaboration collections) are not documented
- The exact font weights and sizes for display typography are inferred from the extracted font families and common e-commerce patterns; the live site may use different values
- Animation and transition durations/easings are not captured
- The checkout flow (multi-step vs. single-page, payment form styling) is not documented
- Mobile navigation drawer (hamburger menu) styling (background, animation, overlay) is not extracted
- The extracted color list contains many grays and blues that may include Shopify/checkout widget colors; the true brand palette may have fewer or different accent colors
- The "Astra" font family in the extracted list may be a theme default rather than an actively used brand font
