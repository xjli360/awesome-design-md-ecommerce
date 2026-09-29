---
version: alpha
name: "Step2"
source_url: "https://www.step2.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A primary-yellow (#fac241) voltage runs through every CTA, badge, and interactive element on a warm off-white canvas (#e8e8e1), creating a playground of color that signals fun before a single word is read. The brand lives in the tension between bold primary accents and a surprisingly restrained neutral system — deep charcoal (#121212) for headlines, softer grays (#898989, #3d4246) for body copy, and a near-white surface (#fffefd) for product cards that let the toys themselves pop. Red (#ff0000) appears as an urgent accent on sale badges and clearance markers, while a forest green (#2b6450) surfaces in outdoor-product callouts and eco-friendly messaging. The typography system leans on a single sans-serif stack (Swiper Icons for iconography, with system fonts for body), keeping the interface clean and child-friendly without feeling cartoonish. Buttons are generously padded with {rounded.sm} corners, product cards use {rounded.md} to frame playhouses and wagons, and the navigation bar sits at a sturdy 72px height — substantial enough to feel anchored, light enough to stay out of the way. The overall effect is a digital toy box: organized, colorful, and built for exploration.

colors:
  primary: "#fac241"
  primary-active: "#e39e3d"
  primary-disabled: "#fdfd62"
  ink: "#121212"
  body: "#3d4246"
  muted: "#898989"
  muted-soft: "#c5c5c5"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#e8e8e1"
  surface-soft: "#f3f3f3"
  surface-card: "#fffefd"
  on-primary: "#121212"
  accent-red: "#ff0000"
  accent-green: "#2b6450"
  accent-blue: "#899df1"
  sale-badge: "#c92a39"
  clearance-badge: "#ff7f50"
  star-rating: "#fac241"

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
    letterSpacing: -0.3px
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
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
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
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
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
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 10px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 11px 15px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-red}"
    padding: 11px 15px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-rating-stars:
    color: "{colors.star-rating}"
    fontSize: "14px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: "400px"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: "56px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: "48px"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: "11px 19px"
    height: "48px"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: "40px"
    width: "40px"
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
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.md}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    minHeight: "120px"
  category-card-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    minHeight: "120px"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  clearance-badge:
    backgroundColor: "{colors.clearance-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: "36px"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: "36px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature yellow (#fac241) with dark text (#121212) for high contrast. Uses {typography.button-md} at 16px/600 weight with {rounded.sm} corners and generous 12px 24px padding. On hover/active, shifts to {colors.primary-active} (#e39e3d). Disabled state uses {colors.primary-disabled} (#fdfd62) with {colors.muted} text to visually de-emphasize without losing the yellow family.

**`button-secondary`** — An outlined variant for secondary actions, using the {colors.canvas} background with a 2px solid {colors.ink} border. Maintains the same 48px height and {rounded.sm} corners as the primary button. On hover, the background fills with {colors.ink} and text inverts to {colors.canvas}, creating a satisfying reversal.

**`button-accent-red`** and **`button-accent-green`** — Compact action buttons (36px height) used for clearance callouts and eco-friendly product badges respectively. These use {typography.button-sm} at 14px/600 weight and appear in product cards, category strips, and promotional banners.

### Cards
**`product-card`** — The core product display unit, using a clean white surface ({colors.surface-card}) with {rounded.md} corners and a subtle shadow (0 1px 3px rgba(0,0,0,0.08)). Each card contains a square-ratio image with {rounded.sm}, a product title in {typography.title-sm}, price in {typography.price}, and optional rating stars in {colors.star-rating}. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.12) for a gentle lift effect. Badges (sale, clearance, new) appear absolutely positioned at the top-left.

**`category-card`** — Navigation cards for product categories (Playhouses, Wagons, Slides, etc.). Default state is a white card with {rounded.md} and {typography.title-sm}. On hover, the entire card fills with {colors.primary} and text inverts to {colors.on-primary}, creating a bold color block that signals interactivity.

### Navigation
**`nav-bar`** — A 72px fixed-height bar on the {colors.canvas} background, containing the logo, category links, and utility icons (search, cart, account). Links use {typography.nav-link} at 16px/500 weight with {spacing.sm} {spacing.md} padding and {rounded.xs} hover states. Active links are underlined with a 2px {colors.primary} border. On scroll, the bar gains a subtle shadow (0 2px 4px rgba(0,0,0,0.08)) for visual anchoring.

### Forms
**`text-input`** — Standard input fields with {colors.surface-card} background, 1px {colors.hairline} border, and {rounded.sm} corners. On focus, the border thickens to 2px and switches to {colors.primary}. Error states use a 2px {colors.accent-red} border. All inputs maintain a consistent 48px height with 12px 16px padding.

### Search
**`search-bar`** — A pill-shaped input ({rounded.full}) with {colors.surface-card} background and 1px {colors.hairline} border. On focus, the border becomes 2px {colors.primary}. The search submit button is a 40px circle in {colors.primary} with a white icon, positioned at the right edge of the input.

### Footer
**`footer`** — A dark section ({colors.ink} background) with white text ({colors.canvas}) organized into columns. Links start in {colors.muted-soft} and brighten to {colors.canvas} on hover. Section headings use {typography.title-sm} for clear hierarchy. Padding is generous at {spacing.xxl} top/bottom and {spacing.lg} sides.

### Badges
**`sale-badge`** — A compact red badge (#c92a39) with white uppercase text in {typography.badge} (11px/700 weight). Used for percentage-off callouts and limited-time offers. **`clearance-badge`** — A coral badge (#ff7f50) for deeper discount items, following the same typography and sizing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack single-column; hero banner reduces to 300px min-height; search bar moves below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav shows 4-5 category links with overflow menu; product cards display in 2-column grid; hero banner at 350px min-height; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all category links; product cards in 3-4 column grid; hero banner at 400px min-height; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero banner expands to 450px min-height with wider padding |

### Touch Targets
- All interactive elements maintain minimum 44x44px touch targets
- Nav links have 48px minimum tap height
- Product card CTAs are 48px tall
- Search submit button is 40x40px (meets touch target with surrounding padding)
- Category cards are minimum 120px tall for easy tapping

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button that opens a slide-out panel on mobile
- Product description sections use accordion pattern on all breakpoints
- Footer link columns collapse to single-column accordion on mobile
- Mega-menu dropdowns collapse to simple link lists on tablet and below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family declarations were limited to "swiper-icons" in the extracted data; the system font stack used above is inferred from common Shopify patterns — actual brand fonts may differ
- Hover and active states for many components (accordion, breadcrumb, pagination) are inferred from common e-commerce patterns rather than extracted from the live site
- Error state styling for forms (validation messages, error icons) could not be extracted
- Dark mode or high-contrast mode configurations are not present in the extracted data
- Sub-brand or seasonal color palettes (holiday, back-to-school) could not be identified
- Animation durations, easing curves, and transition properties were not extractable
- The meta theme-color tag was absent, suggesting no browser chrome theming is implemented
- Icon set and icon sizing conventions (cart, search, account, social) could not be determined
- Loading states, skeleton screens, and empty states are not documented from extraction
- The extracted color list includes many generic web colors (#00ffff, #0000ff, #a52a2a) that are likely from third-party widgets or stock imagery rather than brand colors — these were excluded from the palette
