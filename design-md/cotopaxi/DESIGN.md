---
version: alpha
name: "Cotopaxi"
source_url: "https://www.cotopaxi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the conviction that outdoor gear can be both vividly colorful and deeply purposeful, Cotopaxi wraps its mission in a palette that feels like a well-loved thrift-store haul: the deep indigo of a high-altitude sky (#2c2a41) anchors the experience, while a warm terra-cotta (#e18133) and a dusty sage (#9ebadc) appear as accent colors that refuse to be quiet. The signature blue (#007aaf) — pulled from the brand's logo and the meta theme-color — acts as a reliable north star across navigation bars, primary buttons, and footer backgrounds, while the lighter airy blue (#b7d9f0) softens the edges of cards and banners. The canvas is a warm off-white (#f1f0eb) rather than a sterile pure white, giving the entire site the feel of a well-worn trail map spread across a wooden table. Type is set in a clean, approachable sans-serif (likely a system stack given the `inherit` extraction) that never competes with the product photography — the gear is the hero, and the typography steps back to let the vibrant yellows, oranges, and blues of the products do the talking. Buttons are softly rounded (`{rounded.sm}`), product cards carry a gentle shadow and `{rounded.md}` corners, and the overall rhythm is generous without being wasteful: `{spacing.section}` of 64px separates major content blocks, while `{spacing.base}` of 16px keeps the reading experience intimate. The brand's "Gear For Good" ethos is woven into every interaction — a subtle badge on product cards, a persistent banner in the footer, and a warm tone in the microcopy that treats the customer like a fellow adventurer rather than a transaction.

colors:
  primary: "#007aaf"
  primary-active: "#006494"
  primary-disabled: "#b7d9f0"
  ink: "#2c2a41"
  body: "#3c3c3c"
  muted: "#777575"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f1f0eb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#e18133"
  accent-sage: "#9ebadc"
  accent-yellow: "#ec8816"
  accent-purple: "#7069bc"
  accent-red: "#d10000"
  accent-green: "#199800"
  badge-do-good: "#134791"
  badge-new: "#e18133"
  badge-sale: "#d10000"
  star-rating: "#ec8816"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
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
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-terracotta:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(44, 42, 65, 0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(0, 122, 175, 0.15)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(44, 42, 65, 0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(44, 42, 65, 0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-do-good:
    backgroundColor: "{colors.badge-do-good}"
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
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  section-header:
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} 0 {spacing.base}"
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
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.primary}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    padding: "{spacing.base} 0"
    typography: "{typography.body-md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and "Donate" actions. Rendered in the brand's signature blue (`{colors.primary}`) with white text and a soft 8px radius. On hover, it deepens to `{colors.primary-active}` (#006494). The disabled state uses the lighter blue (`{colors.primary-disabled}`) to signal inactivity without losing brand identity.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Learn More." Uses a 2px solid stroke in `{colors.ink}` on the warm off-white canvas. On hover, the background fills with `{colors.surface-soft}` to provide a subtle lift.

**`button-tertiary-text`** — A text-only button reserved for inline actions like "Clear Filters" or "Cancel." Uses `{colors.primary}` text on a transparent background with no border, keeping the interface clean and reducing visual noise.

**`button-accent-terracotta`** — A specialty button for promotional banners and limited-edition drops. Uses the warm terra-cotta (`{colors.accent-terracotta}`) to draw attention without competing with the primary blue. Typically paired with `{typography.button-sm}` for compact layouts.

**`button-pill-primary`** and **`button-pill-outline`** — Pill-shaped variants used in the filter strip, category navigation, and search suggestions. The filled version uses `{colors.primary}`, while the outline version uses a 1px stroke on a transparent background. Both use `{rounded.full}` for a friendly, approachable feel.

### Cards
**`product-card`** — The core product display unit, a white card with a 1:1 aspect-ratio image area and a 12px corner radius. The image sits flush to the top corners, while the title and price stack below with `{spacing.sm}` and `{spacing.base}` padding. On hover, the card lifts with a deeper shadow (`0 4px 12px rgba(44, 42, 65, 0.12)`), signaling interactivity. Badges for "Do Good," "New," and "Sale" overlay the top-left corner of the image.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, using the warm off-white canvas background. Links are set in uppercase with `{typography.nav-link}` (14px, weight 600, 0.25px letter-spacing). The active state is indicated by a 2px bottom border in `{colors.primary}`. On scroll, a subtle shadow (`0 2px 8px rgba(44, 42, 65, 0.08)`) appears beneath the bar.

**`nav-link`** — Individual navigation items with 8px vertical and 12px horizontal padding. The active state uses `{colors.primary}` text with the bottom border, while inactive links remain in `{colors.ink}`.

### Forms
**`text-input`** — Standard text input fields for search, email signup, and checkout forms. Uses the warm off-white canvas background, 48px height, and a 1px hairline border. On focus, the border shifts to `{colors.primary}` with a 3px blue glow (`rgba(0, 122, 175, 0.15)`). Error states use `{colors.accent-red}` for the border.

**`select-input`** — Dropdown selectors styled identically to text inputs, used for size, color, and quantity selection on product pages.

**`quantity-selector`** — A compact 40px-high input for adjusting item quantities, with a 1px hairline border and 8px padding. Used in cart and product detail pages.

### Badges
**`badge-do-good`** — A dark blue (`{colors.badge-do-good}`) badge indicating products that support Cotopaxi's social mission. Uses uppercase 11px bold type with 0.5px letter-spacing and a 4px radius. Positioned at the top-left of product card images.

**`badge-new`** — A terra-cotta (`{colors.badge-new}`) badge for newly launched products, using the same typography and positioning as the do-good badge.

**`badge-sale`** — A red (`{colors.badge-sale}`) badge for discounted items, using the same styling to maintain visual consistency across badge types.

### Hero & Sections
**`hero-banner`** — Full-width hero sections on the homepage and collection pages. Uses `{colors.primary}` as the background with white text in `{typography.display-xl}`. A dark overlay (`{colors.scrim}` at 30% opacity) sits over background images to ensure text readability. Minimum height of 400px with `{spacing.section}` vertical padding.

**`section-header`** — Section titles across the site, using `{typography.display-lg}` (28px, weight 700) with `{spacing.xl}` top padding and `{spacing.base}` bottom padding. Used for "Shop by Category," "New Arrivals," and "Our Mission" sections.

### Filters
**`filter-chip`** — Pill-shaped filter options in collection pages, using `{colors.surface-soft}` background with a 1px hairline border. Active filters switch to `{colors.primary}` background with white text, providing clear visual feedback.

### Footer
**`footer`** — The site footer uses the deep indigo (`{colors.ink}`) as its background, creating a strong visual anchor at the bottom of every page. Links are set in `{colors.muted-soft}` and shift to white on hover. The footer contains navigation columns, a newsletter signup, and the "Gear For Good" mission statement.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), nav collapses to hamburger menu, hero banner reduces to 300px min-height, filter chips stack vertically, footer links collapse into accordion sections |
| Tablet | 744–1128px | Two-column product grid (2 items per row), nav links remain visible but condensed, hero banner at 350px min-height, filter chips wrap to two rows, footer displays in two columns |
| Desktop | 1128–1440px | Three-column product grid (3 items per row), full nav bar visible, hero banner at 400px min-height, filter chips in a single horizontal row, footer in four columns |
| Wide | > 1440px | Four-column product grid (4 items per row), max-width container at 1440px, hero banner expands to 500px min-height, additional whitespace around content blocks |

### Touch Targets
- All interactive elements (buttons, links, filter chips) maintain a minimum touch target of 44x44px on mobile and tablet.
- Product card tap areas extend to the full card boundary, not just the title or price text.
- Filter chips use 36px minimum height with 16px horizontal padding to ensure comfortable tapping.
- Quantity selector buttons (plus/minus) are 40x40px with no overlap.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer. The search bar moves into the drawer as a full-width input.
- Product filters collapse into a "Filter" button that opens a modal overlay, rather than showing inline chips.
- Footer link groups collapse into accordion sections with expandable headers, saving vertical space.
- The hero banner reduces its headline to `{typography.display-md}` (24px) and stacks the CTA button below the text rather than beside it.
- Product detail pages collapse the image gallery into a single-column swipeable carousel, with thumbnails hidden.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family**: The extraction returned `inherit` for font-family declarations. The system stack used in the typography block is an educated assumption based on common Shopify practices. The actual brand font (if any custom typeface is used) could not be determined.
- **Hover states**: While hover states for buttons and cards are defined, hover states for navigation links, filter chips, and footer links are inferred from common patterns rather than extracted from the live site.
- **Error and validation styling**: Error states for forms (beyond the red border) and validation messages could not be extracted. The `text-input-error` token is a best-guess implementation.
- **Dark mode**: No dark mode variant was detected. The brand's use of a warm off-white canvas suggests light mode is the primary experience.
- **Sub-brand palettes**: Cotopaxi may use distinct color palettes for specific product lines (e.g., "Do Good" collection, limited editions). These could not be extracted.
- **Animation and transition values**: Timing functions, durations, and easing curves for hover states, page transitions, and loading states are not captured.
- **Iconography**: The extracted colors include several that may belong to social media icons or payment method badges (e.g., `#d10000` for a red social icon, `#199800` for a green payment badge). These have been assigned as accent colors but may not be part of the brand's core palette.
- **Checkout-specific styling**: Shopify's checkout page uses its own theme and may not follow the same design tokens as the main site. Checkout-specific colors (e.g., Klarna pink, PayPal blue) have been filtered out where possible.
- **The extracted color list is unusually large (30+ colors) and includes many grays and near-grays** (`#dedede`, `#b9b9b9`, `#cdcdcd`, `#e5e5e5`, `#979797`, `#aaaaaa`, `#f1f1f1`, `#eeeeee`, `#e2e2e2`, `#dbdbdb`). These likely represent border colors, background variations, and stock-image dominant tones rather than intentional brand palette choices. The core palette has been distilled to the most distinctive and frequently used colors.
