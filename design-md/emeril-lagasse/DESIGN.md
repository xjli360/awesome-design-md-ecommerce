---
version: alpha
name: "Emeril Lagasse"
source_url: "https://www.emerileveryday.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  That unmistakable red — #c02826 — hits the page like a cast-iron sear mark, the same intensity Emeril brings to a stovetop. The Emeril Everyday digital storefront runs on a near-black scaffold (#171717 ink, #121212 for deep surfaces) that lets product photography of air fryers, pressure cookers, and blenders float against clean white canvas. Montserrat carries headlines at bold 700 weights with tight tracking, delivering punch without pretension — this is a kitchen brand that sells confidence, not aspiration. Inter handles body copy and UI labels at 400/500 weights, keeping readability high across spec-dense product comparison grids and recipe cards.

  Buttons land with full-bleed red backgrounds and white text, squared off at `{rounded.xs}` corners — just enough softening to feel approachable without drifting into lifestyle-brand pill shapes. Product cards use `{rounded.sm}` and a 1px `{colors.hairline}` border, stacking vertically on mobile with generous `{spacing.lg}` gutters. The navigation bar sits at 64px height on desktop with Montserrat 600-weight links against a `{colors.surface-dark}` background, creating a restaurant-menu authority that separates it from the typical Shopify lightweight header.

  A muted gray palette (#dedede for hairlines, a softer #f5f5f5 for alternating section bands) prevents the aggressive red-and-black pairing from feeling heavy. Sale badges and "Best Seller" flags use the primary red at `{typography.badge}` scale — 11px uppercase Montserrat 700 — punching out of card corners. The overall rhythm is dense and commercial: tight spacing between product grid items (`{spacing.md}`), compact filter bars, and information-rich hover states that reveal wattage specs and star ratings without requiring a click-through. This is a QVC-meets-modern-DTC sensibility — every pixel earns its place by moving product.

colors:
  primary: "#c02826"
  primary-active: "#a12120"
  primary-disabled: "#e8a3a2"
  ink: "#171717"
  ink-deep: "#121212"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#171717"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#c02826"
  star-rating: "#f5a623"
  success: "#2e7d32"
  border-strong: "#bcbcbc"

typography:
  display-xl:
    fontFamily: "'Montserrat', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  price:
    fontFamily: "'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  spec-label:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 54px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-error:
    border: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  nav-bar-mobile:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.base}"
    hoverShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  bestseller-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
    gap: 2px
  spec-row:
    typography: "{typography.spec-label}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    hoverColor: "{colors.on-dark}"
  collection-filter-bar:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline}
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid {colors.hairline}
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px

---

## Components

### Buttons

**`button-primary`** — Solid red (#c02826) background with white text in Montserrat 600 weight. Corners clip at 4px radius, giving a commercial directness that avoids playfulness. On hover, background deepens to #a12120; on press, a subtle 1px inset shadow appears. Disabled state washes to a muted rose (#e8a3a2) with reduced opacity.

**`button-secondary`** — White fill with a 2px solid ink-black border. Text matches the border in Montserrat 600. On hover the button inverts to full black fill with white text — a binary toggle that reinforces the brand's high-contrast palette. Used for "View Details" and secondary product actions.

**`button-add-to-cart`** — Full-width variant of the primary button at 54px height and 700 weight type. This is the loudest element on any product page, stretching edge-to-edge within its container to eliminate decision friction. Letter-spacing opens slightly to 0.3px for legibility at the larger size.

### Navigation

**`nav-bar`** — A 64px-tall dark bar (#171717) anchors the top of every page. Logo sits left, navigation links center in Montserrat 600 at 14px with 0.2px letter-spacing. Cart icon and hamburger menu (mobile) sit right. The bar does not use transparency or blur — it is an opaque slab that grounds the page.

**`announcement-bar`** — A 36px ribbon in primary red runs above the nav bar, typically carrying free-shipping thresholds or limited-time offers in centered caption-weight Inter. It scrolls away on mobile but remains sticky on desktop.

### Product Cards

**`product-card`** — White card with 8px radius and a 1px #dedede border. Product image fills the top in a 1:1 aspect ratio on a #f5f5f5 background. Title appears in Montserrat 600/16px, price in Montserrat 700/18px. Hover lifts the card with a soft 4px 12px shadow. Compare-at prices render in Inter 400 with a line-through decoration in muted gray.

**`sale-badge`** — Positioned absolute in the card's top-left corner, the badge uses primary red background with white uppercase Montserrat at 11px. Padding is tight (4px 8px) to keep it compact against the product image.

**`bestseller-badge`** — Same dimensions as sale-badge but uses ink-black background. Appears in top-right when a product carries the bestseller flag, never stacking with the sale badge on the same corner.

### Hero

**`hero-banner`** — Full-bleed section with a #121212 background and centered content. Minimum height 480px on desktop, collapsing to auto-height on mobile. Product photography typically fills one half while headline text (`display-xl`, 42px Montserrat 700) occupies the other. A primary CTA button sits below the subhead with 24px spacing.

### Product Page Details

**`spec-row`** — Horizontal key-value rows for wattage, capacity, dimensions. Inter 500/13px in body color, separated by 1px hairline-soft borders. These stack in a bordered container with no outer border — only internal dividers.

**`star-rating`** — Filled star icons in #f5a623 at 16px with 2px gaps. Partial fills use a clip-path approach. Rating count follows in caption typography.

**`quantity-selector`** — A compact inline control: minus button, numeric input (centered, body-md), plus button. 44px height, 1px hairline border, 4px corners. Buttons highlight to surface-soft on hover.

### Search & Filters

**`search-bar`** — An 8px-rounded input on surface-soft background. Placeholder text in muted gray, active text in ink. A magnifying glass icon sits 16px from the left edge. On focus, a 1px ink border replaces the default borderless state.

**`filter-chip`** — Small capsules (4px radius, not pills) in surface-soft gray. Active state inverts to ink-black fill with white text. Used in collection pages for appliance type, price range, and feature filters.

**`collection-filter-bar`** — A horizontal scrolling row of filter chips on mobile, a static flex row on desktop. Separated from the product grid by a single hairline border below.

### Footer

**`footer`** — Deep black (#121212) background with four-column link layout on desktop, accordion on mobile. Links render in Inter 14px at muted-soft gray (#999999), brightening to white on hover. Logo appears top-left in the footer with 48px bottom margin before link columns begin.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces text links, hero stacks vertically (image above text), announcement bar scrolls away, footer collapses to accordion |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed spacing, hero maintains side-by-side at reduced image scale |
| Desktop | 1128–1440px | Three- or four-column product grid, full nav with all links, hero at full 480px height with 50/50 split |
| Wide | > 1440px | Content max-width caps at 1440px and centers, side gutters grow, product grid holds four columns with increased card padding |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile
- Nav hamburger icon padded to 48×48px hit area
- Product card entire surface is tappable, not just the title link
- Quantity selector buttons expand to 44×44px on touch devices
- Filter chips maintain 12px horizontal gap to prevent mis-taps

### Collapsing Strategy

- Desktop mega-menu collapses to a full-screen slide-out drawer on mobile
- Product spec tables reflow from two-column key-value to stacked single-column below 744px
- Hero CTA button becomes full-width on mobile with increased height (54px)
- Footer four-column grid collapses to single-column accordions with tap-to-expand headers
- Announcement bar text truncates with ellipsis on narrow viewports rather than wrapping

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only four hex colors extracted (#171717, #dedede, #c02826, #121212); secondary accent colors (success green, warning states) are inferred rather than observed
- Star rating color (#f5a623) is a common convention assumption — actual implementation may differ
- No CSS custom properties or design-token JSON was accessible; Shopify theme likely loads variables via Liquid/JS
- Exact border-radius values could not be confirmed from extraction — 4px and 8px are based on visual approximation of the Shopify theme
- Font weight specifics (whether Inter uses variable font or static cuts) not confirmed
- Mobile nav drawer animation timing and easing not observable from static extraction
- Product image aspect ratios may vary by collection; 1:1 is the assumed default for appliance photography
