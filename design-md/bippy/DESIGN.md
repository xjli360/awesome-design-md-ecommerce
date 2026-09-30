---
version: alpha
name: "Bippy"
source_url: "https://heybippy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bippy is a body-care brand that wraps itself in a warm, approachable palette anchored by a signature coral-salmon (#e5877c) that reads as both playful and nurturing — the kind of color that feels like a soft towel fresh from the dryer. This primary voltage carries through CTAs, badges, and accent elements, while a complementary deep navy (#404365) grounds the system with stability and a touch of sophistication. The brand avoids harshness entirely: text lives in a soft charcoal (#333333) rather than pure black, and the canvas is a clean white (#ffffff) that lets product photography and the coral pop. Secondary accents of muted blue-gray (#4a5764) and a friendly sky blue (#00b3ff) appear in navigation and links, while a family of warm grays (#d3d3d3, #eeeeee, #cccccc) handles borders, dividers, and surface treatments. Typography leans on a sans-serif stack of Avenir Next, Helvetica Neue, and Open Sans — clean, rounded, and highly legible at every size. Buttons are softly pill-shaped (`{rounded.sm}`), cards have gentle rounding (`{rounded.md}`), and the overall feel is one of calm confidence: this is a brand that wants you to feel good in your skin, not overwhelmed by flash. The Shopify platform underpins a straightforward ecommerce flow with a sticky nav bar, prominent search, and product cards that foreground the hero image and price.

colors:
  primary: "#e5877c"
  primary-active: "#e77769"
  primary-disabled: "#fb8077"
  ink: "#333333"
  body: "#4e4e4e"
  muted: "#777777"
  muted-soft: "#888888"
  hairline: "#d3d3d3"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#efefef"
  on-primary: "#ffffff"
  accent-navy: "#404365"
  accent-blue: "#00b3ff"
  accent-blue-active: "#007ace"
  accent-red: "#e50122"
  accent-red-soft: "#f14336"
  star-rating: "#222222"
  badge-new: "#ff5268"
  badge-sale: "#e50122"
  scrim: "#1e1e1e"

typography:
  display-xl:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px

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
    rounded: "{rounded.sm}"
    padding: 12px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
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
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-sale-price:
    color: "{colors.accent-red}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  badge-new:
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
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand coral (#e5877c) and white text. On hover, it shifts to a slightly deeper coral (#e77769). The disabled state uses a lighter, desaturated coral (#fb8077). All primary buttons use 8px rounded corners and 48px height for a consistent, touch-friendly target.

**`button-secondary`** — An outlined button with a white fill, dark text, and a 2px hairline border. On active state, the border darkens to the ink color and the background takes a soft gray (#f6f6f6). Used for "Add to Cart" alternatives and secondary actions.

**`button-tertiary-text`** — A text-only button with no background or border, using the primary coral for text. Ideal for inline actions like "View Details" or "Learn More" where visual weight should be minimal.

**`button-pill-primary`** — A fully pill-shaped variant of the primary button, used for promotional badges, filter tags, and compact CTAs. Same coral fill and white text, but with full rounding and tighter padding.

**`button-pill-outline`** — A pill-shaped outlined button with a 1px hairline border. Used for category filters and secondary tag-style actions.

### Cards
**`product-card`** — The core product display unit, a white card with 12px rounded corners and no padding at the card level (padding is handled by child elements). The image area has top-only rounding to match the card shape. The title uses 16px medium weight, and the price sits below in 16px regular weight. Sale prices render in the accent red (#e50122). A badge overlay (new or sale) sits in the top-left corner of the image area.

**`hero-banner`** — A full-width promotional section with a soft gray background (#f6f6f6) and large display typography. Includes a primary CTA button. Used for seasonal promotions, new product launches, or brand storytelling.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar, 72px tall, white background, with a subtle bottom border (#dedede). Navigation links use 15px medium weight and shift to coral on hover and active states. The active link also gets a 2px coral bottom border.

**`search-bar`** — A pill-shaped search input with a soft gray background (#f6f6f6) and a 1px hairline border. On focus, the border becomes 2px coral. Placeholder text uses the muted gray (#777777).

### Forms
**`text-input`** — Standard text input with a white background, 1px hairline border, and 8px rounded corners. On focus, the border becomes 2px coral. Error state uses a 2px red border (#e50122). Height is 48px for touch accessibility.

**`quantity-selector`** — A compact input for selecting product quantities, with a white background, 1px hairline border, and 8px rounded corners. Height is 40px.

### Footer
**`footer`** — A full-width footer with a deep navy background (#404365) and white text. Links are white and turn coral on hover. Padding is generous (48px vertical) to create a grounded, substantial feel.

### Badges
**`badge-new`** — A small, uppercase badge with a pink-red background (#ff5268) and white text. Used to flag new products or collections. 4px rounded corners and tight padding.

**`badge-sale`** — A small, uppercase badge with a red background (#e50122) and white text. Used to flag sale or discounted items. Same shape as the new badge.

### Miscellaneous
**`divider`** — A 1px horizontal line using the hairline gray (#d3d3d3). Used to separate sections within a page or card.

**`accordion`** — A collapsible section with a title row (18px, semibold) and a bottom border. The content area uses 14px regular weight body text in the muted gray (#4e4e4e). Used for product descriptions, ingredients, and shipping details.

**`star-rating`** — A set of filled or empty stars rendered in dark gray (#222222). The star size is 16px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero banner reduces to 24px display text; search bar moves to a dedicated icon; footer links stack in a single column; padding reduces to 16px on all sides |
| Tablet | 744–1128px | Two-column product grid; nav bar shows condensed links (icons + short labels); hero banner uses 28px display text; search bar is full width in the nav; footer uses a 2-column link layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with text links; hero banner uses 32px display text; search bar is a pill in the nav; footer uses a 3-column link layout; standard padding of 24px on content areas |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner centered with max-width; all other layouts scale proportionally; extra whitespace on the sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Nav bar links and icons have a minimum tap area of 44x44px.
- Product card CTAs ("Add to Cart", "Quick View") are at least 48px tall.
- Quantity selector buttons are 40x40px minimum.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The search bar collapses into a search icon that opens a full-screen overlay on mobile.
- Product filters collapse into a "Filter" button that opens a modal or bottom sheet on mobile.
- The footer link columns collapse into a single vertical stack on mobile.
- The hero banner image and text stack vertically on mobile (image on top, text below).
- Product image galleries collapse from thumbnails to a single swipeable carousel on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary button and nav links have reliable hover data; others are inferred).
- Focus ring styles and keyboard navigation patterns (no extracted data).
- Error state styling for forms beyond the text-input border (no error message typography or iconography).
- Dark mode or high-contrast mode color overrides.
- Sub-brand or seasonal palette variations (e.g., holiday, limited edition).
- Animation and transition timing functions (ease-in, ease-out, duration).
- Shadow and elevation tokens (no box-shadow values extracted).
- Icon set and icon sizing guidelines (no SVG or icon font data).
- Typography scale for mobile (all sizes are desktop; responsive reductions are estimated).
- Specific font weights beyond 400, 500, 600, 700 (no extracted data for 300 or 800).
- Line-height and letter-spacing for all typography tokens (values are estimated based on common practice).
- Component spacing within cards (e.g., padding between title and price is estimated).
- Product card hover states (e.g., image zoom, shadow lift).
- Search result dropdown styling.
- Cart and checkout flow component styling.
- Loading states and skeleton screens.
- Accessibility contrast ratios (no color contrast data extracted).
