---
version: alpha
name: "iBUYPOWER"
source_url: "https://www.ibuypower.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-performance PC builder where the brand voltage comes from a bright, competitive accent — #ee730a, a vivid safety-orange that appears on configurator CTAs, spec badges, and sale flags, cutting through a palette dominated by #404040 ink, #ebebeb hairline, and #ffffff canvas. The site reads like a spec sheet come to life: dense product cards with stacked pricing, wattage ratings, and RGB-switch icons, all held in place by a strict 12-column grid and sharp {rounded.sm} corners on every module. Navigation is a two-tier bar — a thin utility strip of account, support, and financing links in {colors.muted} #737373, then a fat primary bar with dropdown mega-menus for Desktop, Laptop, Parts, and Deals, each category badge carrying the orange #ee730a or a gaming-green #9bca3e. The hero section on the homepage is a full-bleed dark canvas (#272727) with a single hero PC rendered in high-contrast, the CTA button glowing in #ee730a on #ffffff text — no gradient, no shadow, just flat, confident color. Product cards use a three-column layout on desktop, each card a white {surface-card} with a 4:3 product image, a title in {typography.title-md} at 16px/600 weight, a row of spec pills (CPU, GPU, RAM) in {typography.caption} with {rounded.full} backgrounds in #ebebeb, and a price block that stacks MSRP and sale price in #bd2426 red. The checkout flow shifts to a cooler register: #0051c3 blue for primary actions, #163959 for the progress bar, and #f68b1f for financing CTAs — a deliberate palette switch from the gaming-orange of the storefront to a trustworthy, financial-services blue. The typography stack is system-native: -apple-system, Segoe UI, Roboto, Helvetica Neue — no custom font, which keeps page loads fast and the spec-sheet density readable at any zoom level. Every interactive element — buttons, dropdowns, filter chips — uses a 2px focus ring in #62a1d8, a light blue that appears nowhere else in the palette, reserved entirely for accessibility.

colors:
  primary: "#ee730a"
  primary-active: "#c16508"
  primary-disabled: "#f9b169"
  ink: "#404040"
  body: "#595959"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#ebebeb"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gaming-green: "#9bca3e"
  gaming-green-dark: "#516b1d"
  sale-red: "#bd2426"
  sale-red-light: "#de5052"
  accent-blue: "#0051c3"
  accent-blue-dark: "#163959"
  focus-ring: "#62a1d8"
  financing-accent: "#f68b1f"
  hero-canvas: "#272727"
  hero-canvas-alt: "#521010"
  badge-orange: "#ee730a"
  badge-green: "#9bca3e"
  badge-red: "#bd2426"
  star-rating: "#f68b1f"
  scrim: "#000000"

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
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
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
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  nav-link-small:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.25px
  price-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  price-strikethrough:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  button-checkout:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-financing:
    backgroundColor: "{colors.financing-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "2px solid {colors.focus-ring}"
    outline: "none"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 32px 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-nav-utility:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link-small}"
    height: 36px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-primary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 16px 24px
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  nav-category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.md}"
  product-card-spec-pill:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-sale-price:
    typography: "{typography.price-md}"
    textColor: "{colors.sale-red}"
  product-card-strikethrough:
    typography: "{typography.price-strikethrough}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-green:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-red:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.hero-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "480px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 40px"
    height: 56px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "2px solid {colors.focus-ring}"
    outline: "none"
  footer:
    backgroundColor: "{colors.hero-canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.accent-blue-dark}"
    height: 4px
    rounded: "{rounded.full}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  configurator-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    width: "320px"
  configurator-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
  configurator-option-selected:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "2px solid {colors.primary}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the storefront, configurator, and cart. Uses #ee730a orange fill with white text, 4px rounded corners, and 16px/600 weight system font. On hover, shifts to #c16508. Disabled state uses #f9b169. Height is 44px with 12px/24px padding. **`button-secondary`** — Outlined variant for secondary actions like "Compare" or "Save for Later." White background with 2px #ebebeb border, ink text. Active state swaps border to #404040. **`button-hero`** — Larger version (56px tall, 18px font) used on the homepage hero and landing pages. Same orange fill, more generous 16px/32px padding. **`button-checkout`** — The checkout flow primary button, deliberately switching to #0051c3 blue to signal a shift from gaming to financial trust. 48px tall, 14px/28px padding. **`button-financing`** — Small financing CTA in #f68b1f with ink text, 36px tall, used on product cards and the configurator sidebar.

### Cards
**`product-card`** — The core content module for the product grid. White surface with 1px #ebebeb border, 4px rounded corners, 16px padding. Contains a 4:3 product image, title in 16px/600 weight, a row of spec pills (CPU, GPU, RAM) in 12px/500 weight with full-rounded #ebebeb backgrounds, and a price block. Sale prices render in #bd2426 red with a strikethrough MSRP in #737373. An orange badge (#ee730a) sits absolutely positioned at top-left for "Sale" or "New" flags; green badges (#9bca3e) indicate "In Stock" or "Free Shipping"; red badges (#bd2426) mark "Low Stock" or "Clearance." **`configurator-option`** — Selectable component in the build-your-own-PC sidebar. White card with 1px hairline border, 4px rounded, 12px padding. Selected state swaps to a 2px #ee730a border and light gray fill. **`spec-table-row`** — Alternating white rows with 1px #dedede bottom border, 14px body text, 8px/16px padding. Header rows use #f7f7f7 background with 14px/600 weight.

### Navigation
**`top-nav-utility`** — Thin 36px strip at the very top of every page. White background, #737373 text in 13px/500 weight. Contains account, order status, support, and financing links. Separated from the primary nav by a 1px #ebebeb border. **`top-nav-primary`** — The main 64px navigation bar with dropdown mega-menus. White background, 15px/600 weight ink text. Category labels like "Desktop," "Laptop," "Parts," and "Deals" sit as text links; "Deals" often carries an orange badge (#ee730a) with uppercase 11px/700 weight text. **`nav-dropdown`** — Mega-menu panel that appears on hover. White background, 8px rounded, 16px/24px padding, with a 0 8px 24px rgba(0,0,0,0.12) shadow. Contains category columns, featured product thumbnails, and promotional banners.

### Forms
**`text-input`** — Standard 44px input with 1px #ebebeb border, 4px rounded, 14px horizontal padding. Focus state uses a 2px #62a1d8 border — the only place this light blue appears in the entire palette, reserved exclusively for accessibility. **`select-dropdown`** — Same dimensions as text input but with a 32px right padding for the dropdown arrow. **`filter-chip`** — Pill-shaped toggle for product filtering (e.g., "Intel," "NVIDIA," "Under $1000"). White background with 1px hairline border, 36px tall, 8px/16px padding. Active state inverts to #404040 fill with white text.

### Search
**`search-bar`** — Full-rounded pill input at 44px height, white background, 1px #ebebeb border, 20px horizontal padding. Focus state uses the same #62a1d8 2px ring as all inputs. Sits in the primary nav bar, often with a magnifying glass icon in #737373.

### Footer
**`footer`** — Full-width dark section on #272727 background. Text in #bfbfbf at 14px/400 weight. Links render in the same muted tone and shift to white on hover. Organized in columns with category headings in 14px/600 weight white. Includes legal text, social icons, and a "Back to Top" link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; filter chips stack vertically; hero section reduces to 320px min-height; spec pills wrap to two rows; price blocks stack MSRP above sale price; configurator sidebar becomes a bottom sheet; search bar moves to a full-screen overlay. |
| Tablet | 744–1128px | Two-column product grid; top-nav utility strip hides account/financing links behind a "More" dropdown; filter chips show as horizontal scroll; hero section maintains 400px min-height; configurator sidebar collapses to a sticky bottom bar. |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; filter chips in a horizontal strip above the grid; hero section at 480px min-height; configurator sidebar fixed at 320px width; spec tables render as full-width. |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; hero section expands to 560px min-height with larger typography; configurator sidebar remains 320px; additional whitespace around product cards. |

### Touch Targets
- All interactive elements (buttons, links, inputs, chips) maintain a minimum 44x44px touch target.
- Filter chips are 36px tall but use 8px padding to ensure 44px tap area.
- Product card CTAs ("Customize," "Buy Now") are 44px minimum height.
- Nav dropdowns require a 200ms hover delay to prevent accidental opens on touch devices.
- Search bar tap target is 44px tall with full-width expansion on mobile.

### Collapsing Strategy
- Top-nav utility strip collapses to a single "More" icon on tablet and below.
- Primary nav collapses to a hamburger menu on mobile, with a slide-out drawer from the left.
- Product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile).
- Filter chips collapse from horizontal strip to a "Filters" button that opens a modal on mobile.
- Configurator sidebar collapses to a sticky bottom bar on tablet and below, expanding to a full-screen overlay on tap.
- Spec tables collapse to a stacked "key-value" list on mobile, with a "Show Full Specs" toggle.
- Hero section collapses from full-bleed to a contained card on mobile, with smaller typography and reduced padding.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is dominated by grays (#404040, #ebebeb, #dedede, #595959, #737373, #272727) and blues (#62a1d8, #2f7bbf, #163959, #0051c3), with #ee730a as the most distinctive accent. The palette may include additional gaming-themed colors (neon green, cyberpunk pink, etc.) that weren't captured due to framework filtering or low frequency in the extracted HTML/CSS.
- No custom font-family was detected; the site uses a system font stack. The brand may use a proprietary or licensed font on marketing pages that wasn't present in the extracted CSS.
- Hover states for buttons, links, and cards are inferred from common patterns; exact colors may differ on the live site.
- Error states for forms (validation messages, error borders) were not extracted. The focus ring color (#62a1d8) is the only accessibility token identified.
- Dark mode is not present in the extracted data; the site appears to be light-mode only.
- The checkout flow palette (#0051c3, #163959, #f68b1f) is inferred from extracted blues and the financing accent; exact checkout component tokens may vary.
- Star rating color (#f68b1f) is assumed from the financing accent; actual rating stars may use a different yellow/gold.
- The hero canvas color (#272727) and its alt (#521010) are extracted but may represent specific promotional sections rather than a global dark theme.
- No animation or transition tokens (durations, easings) were extracted.
- The brand may use gradient overlays on hero images or product cards that weren't captured in the flat color extraction.
- Sub-brand or promotional palettes (e.g., "RDY" pre-built series, "Slate" custom builds) may introduce additional accent colors not present in the main palette.
