---
version: alpha
name: "The Ordinary"
source_url: "https://theordinary.com"
captured_at: "2026-09-28T04:09:54.212001+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  A clinical skincare brand that uses a stark white canvas and a single red accent — #e83f42 — as its only emotional release, applied to the cart icon, sale badges, and the "Add to Cart" button that sits like a stop sign against a field of gray. The palette is almost entirely achromatic: #757575 for body text, #e1ded9 for hairline borders, #f7f7f7 and #f9f9f9 for soft surfaces, and #222222 for ink. This is a brand that refuses to seduce — no gradients, no photography, no lifestyle imagery. Product pages are clinical grids of ingredient names in Jost, a geometric sans-serif that reads like a lab report. The typographic system is built on Jost for headings and Geologica for body, with Geologica declared `!important` in the CSS, suggesting a deliberate override of a framework default. Buttons are hard-cornered rectangles (`{rounded.none}`) with #e83f42 fill and white text, or outlined in #757575 for secondary actions. The search bar is a simple rectangle with #e1ded9 borders and #f7f7f7 background. There is no hero image, no carousel, no decorative illustration — the brand communicates entirely through typographic hierarchy, whitespace, and the occasional red intervention. The product grid uses 4-column layouts on desktop with tight spacing (`{spacing.base}` between cards), each card showing a product name in Jost, a price in Geologica, and a "Size" dropdown. The footer is a dense gray block with #404040 background and white links. The brand's integrity is in its refusal to perform — it looks like a scientific journal that happens to sell things.

colors:
  primary: "#e83f42"
  primary-active: "#cc0000"
  primary-disabled: "#ed6d6f"
  ink: "#222222"
  body: "#757575"
  muted: "#7e7b79"
  muted-soft: "#818182"
  hairline: "#e1ded9"
  hairline-soft: "#d8d8d8"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-strong: "#f9f9f9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  footer-bg: "#404040"
  error: "#b3261e"
  success: "#0f461b"
  warning: "#856404"
  info: "#0c5460"
  sale-badge: "#e83f42"
  sold-out: "#d8d8d8"

typography:
  display-xl:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Geologica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Geologica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Geologica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Geologica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Geologica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  product-name:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  product-price:
    fontFamily: "'Geologica', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.body}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-name:
    typography: "{typography.product-name}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    textColor: "{colors.body}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.sm}"
  sold-out-badge:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 40px
    border: "1px solid {colors.hairline}"
  size-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 40px
    border: "1px solid {colors.hairline}"
    padding: "0 {spacing.md}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a hard-cornered rectangle filled with `#e83f42` and white uppercase text in Jost 14px/600. On hover, it shifts to `#cc0000` for a deeper red state. The disabled state uses `#ed6d6f`, a faded pinkish-red that signals unavailability without ambiguity. Padding is 14px top/bottom and 32px left/right, creating a substantial 48px-tall button that reads as authoritative against the white canvas.

**`button-secondary`** — An outlined alternative with white background, `#757575` text, and a `1px solid #e1ded9` border. On hover, the border darkens to `#757575` and the background shifts to `#f7f7f7`. Used for "View Product" links and secondary checkout actions. Same 48px height and uppercase Jost typography as the primary.

**`button-tertiary-text`** — A text-only button with no background or border, using `#757575` body color. On hover, it switches to `#222222` ink. Used for "Learn More" links and cancel actions within forms. No padding — the text itself is the hit target.

### Navigation
**`top-nav`** — A 60px-tall white bar with a `1px solid #e1ded9` bottom border. Contains the brand logo on the left and nav links on the right. Links use Jost 14px/500 in `#222222` with `{spacing.base}` horizontal padding. The active link switches to `#e83f42`. No dropdowns, no mega-menus — the nav is a single row of text.

**`nav-link`** — Simple text links in Jost 14px/500, `#222222` by default, `#e83f42` when active. No underline decoration. Hover state is `#e83f42` as well, creating a consistent red indicator for the current section.

### Cards
**`product-card`** — A white card with no border, no shadow, and no rounded corners. Contains a square image area (1:1 aspect ratio) on a `#f7f7f7` background, followed by the product name in Jost 15px/500 and the price in Geologica 14px/400 in `#757575`. A "Size" dropdown sits below the price. Cards are spaced `{spacing.base}` apart in a responsive grid. No hover elevation — the card is flat.

**`sale-badge`** — A small red rectangle (`#e83f42`) with white uppercase text in Jost 11px/600. Padding is 2px top/bottom and 8px left/right. Positioned at the top-left corner of the product image. No rounded corners.

**`sold-out-badge`** — A gray rectangle (`#d8d8d8`) with `#222222` text. Same dimensions and typography as the sale badge. Used to overlay on product images for out-of-stock items.

### Forms
**`search-bar`** — A 40px-tall rectangle with `#f7f7f7` background, `#e1ded9` border, and `#757575` placeholder text in Geologica 14px. On focus, the background becomes white and the border switches to `#757575`. No rounded corners, no icon — just a bare input field.

**`quantity-selector`** — A 40px-tall rectangle with white background and `#e1ded9` border. Contains a minus button, a number display, and a plus button. Uses Geologica 14px for the number. No rounded corners.

**`size-dropdown`** — A 40px-tall select element with white background, `#e1ded9` border, and `#757575` text. Uses Geologica 14px. Padding is 0 12px. No custom arrow styling — the browser default dropdown arrow is used.

### Footer
**`footer`** — A dense gray block with `#404040` background and white text. Contains 4-5 columns of links, each with a Jost 16px/500 heading and Geologica 14px/400 link items. Links are underlined on hover. Padding is 48px top/bottom and 64px left/right. No borders, no dividers — just text on gray.

### Accordion
**`accordion`** — A white panel with a `1px solid #e1ded9` bottom border. The header uses Jost 18px/500 in `#222222` with `{spacing.base}` vertical padding. The content area uses Geologica 14px/400 in `#757575` with `{spacing.base}` bottom padding. Used on product pages for ingredient lists and usage instructions. No icons — the header text itself is the click target.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger menu, footer stacks vertically, buttons become full-width |
| Tablet | 744–1128px | 2-column product grid, nav links remain visible but reduced font size to 13px, footer splits into 2 rows |
| Desktop | 1128–1440px | 4-column product grid, full nav, footer in 4 columns |
| Wide | > 1440px | 4-column product grid with max-width container (1440px), centered content |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have `{spacing.base}` horizontal padding, creating comfortable tap targets
- Quantity selector buttons are 40px × 40px minimum
- Dropdown selectors are 40px tall

### Collapsing Strategy
- The top nav collapses to a hamburger menu at < 744px, with the menu drawer sliding in from the left
- The product grid collapses from 4 columns → 2 columns → 1 column as viewport shrinks
- The footer collapses from 4 columns → 2 rows of 2 → single column at mobile
- Accordion content is collapsed by default on mobile product pages, with only the first panel open

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover and focus states for most components could not be reliably extracted from the CSS — the extracted colors include many framework defaults (Bootstrap alert colors, social media icons) that may not be part of the brand's design system
- Error and validation styling for form inputs is not confirmed — the `#b3261e` error color is inferred from common patterns
- The exact font weights for Geologica are uncertain — the CSS shows `!important` declarations suggesting framework overrides, but the weight values are assumed
- Dark mode is not supported — the brand uses a white canvas exclusively
- Sub-brand or collection-specific palettes (e.g., "The Ordinary" vs. "NIOD") are not captured
- The extracted hex list includes many colors that appear to be Bootstrap utility classes (alert-success, alert-danger, etc.) — the true brand palette is likely smaller and more focused on the achromatic scale with the single red accent
- Animation and transition durations are unknown — the brand appears to use no micro-interactions
- The `#1877f2` and `#dc049b` colors are likely social media brand colors (Facebook, Instagram) rather than design system tokens
