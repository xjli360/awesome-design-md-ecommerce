---
version: alpha
name: "Armada Skis"
source_url: "https://www.armadaskis.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage alpine brand that uses #003399 as its primary signal — a deep, confident blue that reads as cold-mountain air rather than corporate navy — and #da532c as its accent voltage, an orange that lands like a beacon on a storm day. The brand's visual system is built on contrast: the blue carries primary CTAs, navigation bars, and the "THIS IS ARMADA." hero text, while the orange appears in sale badges, limited-edition callouts, and footer accents. The typography leans toward a clean sans-serif with moderate weight (500–600) for display sizes, avoiding the heavy 700+ that ski brands often use to signal aggression — Armada trusts its product photography and athlete imagery to carry the energy. Cards and buttons use {rounded.sm} (8px) corners, a subtle softening that prevents the interface from feeling too sharp, while the hero section uses {rounded.none} for a full-bleed, immersive feel. The canvas is pure white (#ffffff), with surface-soft (#f7f7f7) for alternating product rows and muted (#6a6a6a) for secondary text. The overall mood is clean, direct, and performance-oriented — no decorative flourishes, no ornamental typography, just the product and the mountain.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#b3c6e6"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#da532c"
  accent-orange-active: "#b8421f"
  accent-orange-disabled: "#f0b8a6"
  sale-badge: "#da532c"
  sale-badge-text: "#ffffff"
  star-rating: "#003399"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 14px 24px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.sale-badge-text}"
    rounded: "{rounded.sm}"
  button-accent-disabled:
    backgroundColor: "{colors.accent-orange-disabled}"
    textColor: "{colors.sale-badge-text}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-orange}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3:4"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.accent-orange}"
    marginTop: "{spacing.xs}"
  product-card-original-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    textDecoration: "line-through"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    height: "80vh"
    minHeight: "500px"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.full}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.full}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  size-selector-active:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  loading-spinner:
    color: "{colors.primary}"
    size: "32px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and "Explore" actions. Rendered in the brand's deep blue (#003399) with white text and 8px rounded corners. On hover, it shifts to `button-primary-active` (#002266) for a darker, more grounded state. When disabled, it uses `button-primary-disabled` (#b3c6e6) to signal inactivity while maintaining brand recognition.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white background with a 2px solid blue border and blue text. The active state inverts to a filled blue background with white text, providing clear hierarchy against the primary button.

**`button-accent`** — The orange (#da532c) variant reserved for urgency signals: sale items, limited-edition drops, and clearance events. It follows the same sizing and padding as `button-primary` but uses the accent orange to create visual contrast and urgency. The active state darkens to #b8421f, and the disabled state fades to #f0b8a6.

**`button-tertiary-text`** — A text-only button for less prominent actions like "Cancel" or "Skip". No background or border, just the blue text at 16px/600 weight. Used in forms and modals where visual weight should be minimal.

### Cards
**`product-card`** — The core product display unit, a white card with 8px rounded corners containing a 3:4 aspect ratio image, product title, and price. The title uses `title-sm` (16px/500 weight) with 8px top margin, and the price uses `body-md` (16px/600 weight) with 4px top margin. Sale items show the price in orange with a line-through original price in muted gray.

**`review-card`** — A customer review container with a subtle border (#ebebeb) and 8px rounded corners. Contains the review text in `body-sm`, a star rating rendered in the brand blue, and the reviewer name in `caption`. Padding is 16px on all sides.

### Navigation
**`nav-bar`** — The top-level site navigation, 72px tall with a white background and uppercase nav links at 14px/600 weight. On scroll, it gains a subtle box-shadow (0 2px 8px rgba(0,0,0,0.08)) for depth. Active nav links show a 2px blue bottom border.

**`category-strip`** — A horizontal scrollable strip of category filters (Men's, Women's, Skis, Apparel, etc.) on a light gray (#f7f7f7) background. Each tab is a pill-shaped button with 8px horizontal padding. The active tab fills with blue, while inactive tabs show muted gray text on transparent background.

### Forms
**`text-input`** — Standard form input with a white background, 1px gray border (#dddddd), 8px rounded corners, and 16px horizontal padding. On focus, the border thickens to 2px blue. Error states switch to a 2px orange border (#da532c).

**`size-selector`** — A clickable size chip (S, M, L, etc.) with a white background, 1px gray border, and 8px rounded corners. Active state shows a 2px blue border with a light gray background fill.

**`quantity-selector`** — A compact input for adjusting item quantities, with a white background, 1px gray border, and 8px rounded corners. Contains minus/plus buttons flanking the current quantity value.

### Search
**`search-bar`** — A full-width pill-shaped search input (9999px radius) with a white background, 1px gray border, and 24px horizontal padding. On focus, the border switches to 2px blue. The height is 56px, making it prominent but not overwhelming.

### Hero
**`hero-section`** — The full-width hero banner, 80vh tall with a minimum of 500px, using the brand blue as background and white text. The headline uses `display-xl` (48px/600 weight) with tight letter spacing (-1px). The CTA button inverts the scheme: white background with blue text.

### Footer
**`footer`** — A full-width footer in the brand blue with white text. Links are set at 14px/500 weight with 0.8 opacity, increasing to full opacity on hover. The footer uses 48px vertical padding and 24px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero section reduces to 60vh; product cards stack in single column; nav-bar collapses to hamburger menu; category-strip becomes horizontally scrollable with no overflow indicator; footer links stack vertically; search-bar reduces to icon-only |
| Tablet | 744–1128px | Hero section maintains 70vh; product cards display in 2-column grid; nav-bar shows 4-5 primary links with "More" dropdown; category-strip shows 6-8 visible tabs with scroll; footer links in 2-column layout |
| Desktop | 1128–1440px | Hero section at 80vh; product cards in 3-column grid; full nav-bar visible (8+ links); category-strip shows all tabs; footer links in 4-column layout |
| Wide | > 1440px | Hero section max-width 1440px centered; product cards in 4-column grid with max-width container; nav-bar and category-strip centered with max-width; footer content centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Product card tap targets are the entire card surface
- Category tabs are 48px tall minimum
- Size selector chips are 44x44px minimum
- Quantity selector buttons are 44x44px minimum

### Collapsing Strategy
- Nav-bar collapses to hamburger menu below 744px, with a slide-in drawer from the left
- Category-strip collapses to a "Filter" button with a modal overlay below 744px
- Product filters (size, color, price) collapse to a "Filters" button with a slide-in panel below 744px
- Footer link columns collapse to a single column with accordion-style expandable sections below 744px
- Product image galleries collapse to a single image with swipeable thumbnails below 744px
- Review sections collapse to show only 2 reviews with a "Show More" button below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; the typography block uses Inter as a reasonable sans-serif default for a performance-oriented brand, but the actual brand font may differ
- Hover and focus states for many components (text-input, size-selector, category-tab) are inferred from common patterns rather than extracted from the live site
- Error styling for forms (text-input-error border color, error message typography) is inferred
- Dark mode or high-contrast mode styling is not present in the extracted data
- Sub-brand or collection-specific color palettes (e.g., ARW, Armada x [collaborator]) are not captured
- Loading states (skeleton screens, shimmer animations) are not defined
- Modal and overlay styling (backdrop color, animation timing) is not captured
- The extracted hex list (#003399, #da532c) is minimal; the brand may use additional accent colors (e.g., a gray for technical specs, a green for sustainability messaging) that were not captured
- No Shopify platform detected; cart and checkout flows may use default Shopify styling rather than brand-specific design tokens
- The brand's athlete and team colorways (e.g., specific pro model graphics) are not represented in the design system
