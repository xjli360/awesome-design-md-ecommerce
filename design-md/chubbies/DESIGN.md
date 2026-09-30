---
version: alpha
name: "Chubbies"
source_url: "https://chubbiesshorts.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Five-inch inseam. That measurement — the number on the hang-tags, in the campaigns, practically in the brand name itself — is the whole thesis externalized as a UI system. Chubbies commits to color the same way it commits to short hemlines: fully and without hedging. The product palette reads directly into the design tokens — #f7a519 amber, #f24392 hot pink, #ff5a00 bonfire orange, #d1f270 lawn-party lime, and #02bce5 electric cyan all exist first as purchasable colorways and second as system accents. The navigational chrome wraps around a teal family (#0082a6, #006c8c, #036282) that gives the grid enough authority to route the eye without fighting the merchandise photography underneath it. Sofia Sans Condensed runs the display layer — headlines stack wide and tight, all-caps, at 800–900 weight, spaced so close the letterforms nearly merge into a single silk-screened mass. Montserrat handles everything transactional: price labels, navigation links, form inputs, and button text in bold uppercase with tracking opened to 1.5px for legibility at scroll speed. Corner radii stay blunt — {rounded.none} on product cards and primary CTAs, with the search bar as the lone exception at {rounded.full} — keeping the page reading like a printed catalog rather than a polished SaaS dashboard. Near-black #000a14 (not true black; slightly navy-shifted, warmer) grounds the ink layer in announcement bars, hero overlays, and footer fills, creating a consistent dark anchor across all three vertical ends of the scroll. Light scaffolding grays (#e0e0e0, #f0f0f0, #ededed) exist to amplify the accent colors by contrast rather than to carry any visual weight themselves. The urgency economy — countdown timers in #ff5a00, limited-colorway badges in #f24392, email-capture blocks saturated in #02bce5 — operates throughout the site with the same deadpan commitment the brand brings to its newsletter subject lines. Product badges are color-coded by urgency grade: orange for sale, pink for limited, lime for new. Nothing here asks the shopper to work very hard; the whole system is optimized to be operated at the lake with one hand.

colors:
  primary: "#0082a6"
  primary-active: "#036282"
  primary-disabled: "#4eb7ab"
  accent-amber: "#f7a519"
  accent-pink: "#f24392"
  accent-orange: "#ff5a00"
  accent-lime: "#d1f270"
  accent-cyan: "#02bce5"
  accent-teal-soft: "#daf2f0"
  accent-purple: "#29007c"
  accent-navy: "#172b85"
  ink: "#000a14"
  body: "#000a14"
  muted: "#717171"
  hairline: "#e0e0e0"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-amber: "#000a14"
  on-accent-lime: "#000a14"

typography:
  display-xl:
    fontFamily: "'Sofia Sans Condensed', Montserrat, sans-serif"
    fontSize: 72px
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Sofia Sans Condensed', Montserrat, sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Sofia Sans Condensed', Montserrat, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "'Sofia Sans Condensed', Montserrat, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  title-md:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  colorway-label:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    padding: 12px 30px
    height: 48px
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent-amber}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-ghost-light:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.canvas}"
    rounded: "{rounded.none}"
    padding: 12px 30px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    focusBorder: "2px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-announcement:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    height: 38px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  product-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  product-badge-new:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent-lime}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  product-badge-limited:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  colorway-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  colorway-label:
    textColor: "{colors.muted}"
    typography: "{typography.colorway-label}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-sale:
    textColor: "{colors.accent-orange}"
    typography: "{typography.price}"
  price-compare:
    textColor: "{colors.muted}"
    typography: "{typography.price}"
    textDecoration: line-through
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    selectedBackground: "{colors.ink}"
    selectedText: "{colors.canvas}"
    selectedBorder: "1px solid {colors.ink}"
    soldOutOpacity: 0.35
  hero-block:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent-amber}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 40px
    height: 52px
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
  email-capture-block:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 44px
    padding: "0 {spacing.base}"
  countdown-timer:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"

## Components

### Buttons

**`button-primary`** — Solid #0082a6 teal fill with all-caps Montserrat at 800 weight and 1.5px letter-spacing, square corners ({rounded.none}) on all four sides. Hover/active state darkens to #036282; disabled washes to the medium aqua {colors.primary-disabled}. The blunt square treatment is intentional — these buttons look cut from a printed catalog page, not rendered in a mobile UI kit.

**`button-accent-amber`** — The high-voltage CTA variant at #f7a519 with near-black {colors.on-accent-amber} text for maximum contrast. Deployed on hero modules, homepage feature blocks, and time-sensitive promotions where teal reads too measured; the warm amber signals summer and urgency simultaneously. Shares identical padding and height with button-primary — a drop-in swap at higher voltage.

**`button-secondary`** — White fill with a 2px solid {colors.ink} border and black text, for wishlist, "view all," or secondary inline actions. Maintains the same uppercase {typography.button-md} type treatment as the primary so the two can sit adjacent without visual hierarchy confusion.

**`button-ghost-light`** — Transparent fill with a 2px white border and white text, placed over dark-fill hero modules or photography backgrounds. Keeps the square-corner language consistent even when floating on full-bleed imagery.

### Nav Bar

**`nav-bar`** — 64px tall white bar with a bottom hairline in {colors.hairline}. Links use {typography.nav-link}: 13px Montserrat at 700 weight, all-caps, 0.8px tracking — compact and dense, fitting a broad category list without wrapping. An `nav-bar-announcement` strip sits above it at 38px in {colors.ink} fill with white caption text for free-shipping thresholds, flash-sale windows, or seasonal event callouts; this dark-to-light transition at the page top mirrors the dark footer below, bracketing the white canvas.

### Product Cards

**`product-card`** — Borderless, no-radius image tiles that sit flush in a grid with no gutter shadow or card container. Below the image: product name in {typography.title-sm}, colorway count in {typography.colorway-label} with {colors.muted} ink, and price in {typography.price}. Badges — `product-badge-sale` (#ff5a00), `product-badge-limited` (#f24392), `product-badge-new` (#d1f270) — sit as absolute-positioned overlays at the image top-left, each on its own line stacked vertically if multiple apply, communicating urgency grade by color before the shopper reads the label.

**`colorway-swatch`** — 24px circles at {rounded.full}, arranged in a tight horizontal row below the product name with {spacing.xs} gaps. Selected state adds a 2px {colors.ink} border ring directly on the circle. An overflow label using {typography.colorway-label} in {colors.muted} handles assortments of 8+ colorways without wrapping ("+ 12 more"). This row is the most color-dense element on the page and communicates breadth of assortment at a glance.

**`size-selector`** — Square tiles ({rounded.none}), 44px height, default in {colors.canvas} with a 1px {colors.hairline} border. Selected state inverts to full {colors.ink} fill with white text and a 1px {colors.ink} border. Sold-out sizes render at 35% opacity; a diagonal strikethrough CSS rule may overlay, consistent with Shopify PDP conventions.

### Hero

**`hero-block`** — Full-bleed dark ({colors.ink}) canvas at minimum 600px height with lifestyle photography or video underneath, overlaid by {typography.display-xl} headline text in white — typically one to two lines of all-caps, condensed type before text crops on mobile. The CTA uses `hero-cta` ({colors.accent-amber}) rather than the teal primary button; warm amber reads faster against the dark ground and reinforces the outdoor/summer orientation that photography alone cannot carry.

### Email Capture

**`email-capture-block`** — A full-width section block saturated in {colors.accent-cyan} (#02bce5). The heading runs in {typography.display-sm}, dark {colors.ink} text. The text input sits adjacent or stacked below, rendered in a white {colors.canvas} field ({rounded.none}) with a `button-primary` teal submit. The cyan fill is one of the most visually distinctive signatures in the Chubbies email-marketing system — it reads like a beach sign posted three days before a holiday and is immediately recognizable to returning customers.

### Urgency / Countdown

**`countdown-timer`** — An #ff5a00 orange block containing large digit display in {typography.display-sm} white text. Sits inside hero modules, above add-to-cart on limited colorways, or in the announcement bar when a flash sale is active. Square corners, no radius, matching the blunt grid language throughout. Digits refresh client-side; when the timer reaches zero, the block is replaced by a sold-out or expired-offer message in {colors.muted}.

### Search Bar

**`search-bar`** — The single pill-shaped element in the system ({rounded.full}), set in light gray {colors.surface-soft} (#f0f0f0). A deliberate formal contrast to the square-corner language everywhere else — the pill softens the utilitarian utility interaction without clashing with the brand register. Placeholder text uses {typography.body-md} in {colors.muted}; the bar expands on focus with no border change, relying on background contrast against the white canvas.

### Footer

**`footer`** — Full {colors.ink} (#000a14) background with white {typography.body-sm} copy. Column headings use {typography.title-sm} — uppercase, tracked — in white, with {spacing.base} margin below before the link list begins. The footer's dark ground directly echoes the announcement bar at the top of the scroll, creating a consistent dark frame around the white commerce canvas. Social links and legal copy occupy a bottom strip inside the same dark container.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to {typography.display-lg}; nav collapses to hamburger drawer; colorway swatches truncate to 4 visible + overflow label; size selector tiles go full-row |
| Tablet | 744–1128px | Two-column product grid; hero can hold a two-column text-plus-image split layout; full announcement bar remains; filter panel shifts to overlay |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; hero at full 600px min-height; sidebar filters active on collection pages |
| Wide | > 1440px | Grid max-width constrained to ~1440px and centered; hero photography scales but type container stays width-capped; no new layout changes above this breakpoint |

### Touch Targets
- All buttons and interactive swatch selectors minimum 44px in either dimension
- Size selector tiles 44px height on mobile, matching `text-input` height for tap consistency
- Colorway swatches rendered with 36px tap area on mobile via padding around the 24px visual circle
- Hamburger nav drawer renders links as full-row 56px tap targets for thumb accessibility
- Footer links minimum 44px vertical tap area, achieved via line-height and padding

### Collapsing Strategy
- Primary navigation collapses to hamburger icon at < 744px; categories become a vertically scrolled full-height drawer from the left edge
- Filters and sort controls on collection pages shift from a persistent left sidebar (desktop) to a bottom-sheet drawer triggered by a fixed filter button (mobile)
- Product image gallery collapses from hover-zoom static grid to swipeable touch carousel with dot pagination
- Email capture block stacks input above submit at mobile width; both go full-width with {spacing.sm} gap
- Countdown timer drops descriptive labels (days / hours / minutes) and renders digits only on mobile to fit within a single row

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed "Add to Cart" CTA color — button-primary teal (#0082a6) assigned from meta theme-color family; amber (#f7a519) may be the actual PDP CTA in live practice
- Muted text color (#717171) approximated — no mid-range gray for UI text present in the extracted hex set
- Body paragraph text color not directly confirmed; {colors.ink} (#000a14) applied throughout as a conservative default
- Font weights for Sofia Sans Condensed not confirmed via extraction — 800/900 weights assigned from visual brand norms
- The deep accent colors #29007c (purple) and #172b85 (navy) appear in extraction but their exact UI role — seasonal banner backgrounds, colorway swatches, promotional modules — could not be determined; surfaced as tokens but not wired to specific components
- Icon set and illustration style not captured; Chubbies is known for custom illustrated graphics in email and marketing collateral that may appear as UI elements on-site
- Exact hover and focus state styles for form inputs not extractable from static snapshot — focusBorder set to 2px solid {colors.ink} as a Shopify-conventional default
- Whether {colors.accent-navy} (#172b85) or {colors.accent-purple} (#29007c) appear in nav, hero, or promotional contexts versus only as colorway references is unverified
