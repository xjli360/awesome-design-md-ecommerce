---
version: alpha
name: "Modiphius"
source_url: "https://www.modiphius.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A tabletop RPG publisher that uses a deep teal (#108474) as its primary brand voltage — a color that reads as both dungeon-crypt and premium board-game felt, appearing on every primary CTA, navigation bar, and product-badge background. The palette is unusually broad for a games publisher: alongside the teal sits a warm marigold (#b2920d), a cool navy (#2f3590), a bright signal blue (#3968d9), and a coral-pink (#fb8077) that could be a critical-hit indicator or a limited-edition accent. The canvas is a near-white (#f9fafb) with a secondary surface (#f3f3f3) that keeps the reading experience airy despite the dense product catalog. Typography runs Nunito Sans at modest weights — display headlines sit at 500–600 weight rather than the heavy 700+ of action-RPG sites — letting the product photography and miniatures do the heavy lifting. Buttons use a soft 8px radius (`{rounded.sm}`) that feels approachable rather than sharp, while product cards take a slightly larger 12px radius (`{rounded.md}`) to distinguish them from interactive elements. The nav bar carries the teal as a full-width band, a confident move that signals "this is a brand, not a forum." The extracted color list is noisy with Shopify-widget blues (#007aff), review-platform purples (#a89cc8), and stock-image tones, but the teal-marigold-navy triad is the brand's true signal.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d4c9"
  ink: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#b2920d"
  accent-navy: "#2f3590"
  accent-blue: "#3968d9"
  accent-coral: "#fb8077"
  accent-yellow: "#fbcd0a"
  accent-red: "#eb2020"
  accent-orange: "#ff9b56"
  star-rating: "#fbcd0a"
  badge-new: "#108474"
  badge-sale: "#eb2020"
  badge-preorder: "#b2920d"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.1px
  link:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Fira Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.1px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  top-nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    margin-top: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    margin-top: "{spacing.xs}"
  product-card-compare-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    textDecoration: line-through
  product-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
    height: 20px
  product-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
  product-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
  product-badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
  product-badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.lg}"
    height: 44px
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px {spacing.md}"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "4px {spacing.md}"
    height: 32px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.body}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    padding: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand teal (#108474) as a full background with white text. On hover, it shifts to a darker active state (#0d6b5d). The disabled state uses a muted teal (#a3d4c9) to indicate non-interactivity. The 8px radius (`{rounded.sm}`) keeps the button feeling approachable rather than aggressive.

**`button-secondary`** — A white button with a subtle hairline border, used for secondary actions like "View Details" or "Cancel." On hover, the border darkens to the ink color and the background takes a soft surface tone. Text remains ink (#121212) for readability.

**`button-tertiary-text`** — A text-only button in the primary teal, used for inline actions like "Clear filters" or "See more." No background or border — just a clickable label that respects the brand color.

**`button-accent-marigold`** and **`button-accent-navy`** — Accent buttons for promotional or category-specific CTAs. The marigold (#b2920d) is used for pre-order or special-edition calls, while the navy (#2f3590) appears on collection pages or brand-specific landing sections.

**`button-pill-cart`** — A fully rounded pill button used for the "Add to Cart" action on product cards and quick-buy surfaces. Smaller than the primary button at 36px height, using `{typography.button-sm}` to fit compact layouts.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px radius (`{rounded.md}`) and 16px padding. The product image sits inside with a smaller 8px radius (`{rounded.sm}`), creating a nested-corner hierarchy. The title uses `{typography.title-sm}` (16px, 600 weight), and the price sits below in `{typography.body-md}`. A compare-at price, when present, uses `{typography.body-sm}` with a line-through and muted color.

**`product-badge`** — Small uppercase badges that sit on the top-left corner of product images. Four variants exist: "NEW" (teal background), "SALE" (red, #eb2020), "PRE-ORDER" (marigold, #b2920d), and "SOLD OUT" (ink, #121212). All use 11px bold uppercase text with 4px radius corners.

### Navigation
**`top-nav`** — A full-width teal band (#108474) at 56px height, carrying uppercase nav links in white. This is the brand's most visible signature — the teal header is the first thing a visitor sees. Dropdown menus drop onto a white canvas with soft rounded corners.

**`search-bar`** — A white search input with a hairline border and 8px radius. On focus, the border switches to the primary teal. The 40px height keeps it compact enough to sit in the nav without dominating.

### Forms
**`newsletter-input`** and **`newsletter-submit`** — A paired input-and-button for email capture. The input is a standard white field with hairline border; the submit button uses the primary teal. Both share the same 44px height and 8px radius for visual alignment.

**`quantity-selector`** — A compact input for cart quantity adjustment, using a white background, hairline border, and centered text. The 40px height matches the search bar and filter dropdowns for consistency.

### Filters
**`filter-dropdown`** — A standard select-style dropdown for sorting and filtering product lists. White background, hairline border, 8px radius, 40px height.

**`filter-chip`** — A pill-shaped chip for active filter tags, using a soft surface background (#f3f3f3) and body text. When active, the chip fills with the primary teal and white text.

### Footer
**`footer`** — A dark footer section using the ink color (#121212) as background, with white text and muted-gray links. The newsletter signup sits here as a primary conversion point.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack in single column; filter chips wrap to two rows; hero banner reduces to 48px padding; search bar moves to expandable overlay |
| Tablet | 744–1128px | Top nav shows limited links with "More" dropdown; product cards in 2-column grid; filter sidebar collapses to top bar with dropdowns; hero banner uses 32px padding |
| Desktop | 1128–1440px | Full top nav visible; product cards in 3-column grid; filter sidebar visible on left; hero banner at full padding (64px) |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero banner centered with max-width content area |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px minimum, with 36px circle variants for secondary actions
- Filter chips are 32px tall — the smallest touch target — acceptable for non-primary interactions
- Product card CTAs (Add to Cart) use the 36px pill button to fit card constraints while remaining tappable

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-out drawer for full navigation
- Filter sidebar collapses to a horizontal bar with dropdown selectors below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Hero banner reduces vertical padding and may hide secondary text on mobile
- Footer columns stack vertically below 744px, with newsletter signup remaining prominent

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most components (button-secondary, filter chips, pagination) were inferred from common patterns — exact extracted hover colors were not available from the static CSS analysis
- **Error states** for form inputs (validation borders, error messages, success states) were not extracted — standard red (#eb2020) is assumed for error borders based on its presence in the palette
- **Focus states** (keyboard focus rings, active tab indicators) were not reliably extracted — a 2px primary-teal outline is assumed
- **Dark mode** — no dark mode tokens were found; the brand appears to use a light-only scheme
- **Sub-brand palettes** — Modiphius publishes multiple game lines (Fallout, Dune, Star Trek, etc.) that may have their own accent colors not captured in the global palette
- **Typography scale** — exact font sizes and weights were inferred from common web patterns and the extracted font-family declarations; the brand may use a more nuanced scale with additional sizes
- **Spacing scale** — the extracted spacing tokens are a best-guess based on common e-commerce patterns; the brand may use a custom scale with additional values
- **Animation tokens** — no transition durations, easing curves, or animation properties were extracted
- **Icon system** — the brand uses custom icons (likely SVG or icon font) but no icon library or sizing tokens were extracted
- **Review widget** — Judgeme icons were detected in the CSS but no styling tokens for the review display were extracted
- **Checkout colors** — Shopify checkout colors (#007aff, #c4cdd5) appear in the extracted palette but are platform defaults, not brand choices
