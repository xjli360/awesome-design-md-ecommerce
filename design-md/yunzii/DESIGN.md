---
version: alpha
name: "Yunzii"
source_url: "https://www.yunzii.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A keyboard brand that builds its visual identity on a deep, almost-black green (#2b2f2d) and a vivid teal accent (#108474), with a secondary jolt of orange (#ed9741) that appears in sale badges and promotional banners. The palette is unusually restrained for a mechanical-keyboard company — no neon RGB excess, no gamer-zone aggression. Instead, Yunzii presents itself as a serious toolmaker: the product pages use generous white canvas (#f9fafb) and soft gray surfaces (#f7f7f7, #eeeeee) to let the keyboards' own aluminum and PBT textures command attention. Typography runs Figtree at moderate weights — display headlines sit at 24–32px in weight 600, body copy at 14–16px in weight 400, and the brand avoids heavy 700+ weights except in price tags and CTA labels. Buttons use the teal primary (#108474) with white text (#ffffff) and {rounded.sm} corners — a friendly but not childish 8px radius. The navigation bar is a slim 64px strip of the dark green (#2b2f2d) with white nav links, and the footer repeats the same dark canvas with a secondary orange (#ed9741) used sparingly for newsletter signup prompts and social icons. Product cards are white (#ffffff) with {rounded.md} (12px) corners and a subtle drop shadow, each featuring a clean price block where the teal primary appears only on the "Add to Cart" button. The overall effect is a workshop aesthetic — precise, muted, confident — where the teal acts as a single voltage point rather than a flood.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a9d092"
  ink: "#2b2f2d"
  body: "#4a4a4a"
  muted: "#7b7b7b"
  muted-soft: "#9a9a9a"
  hairline: "#dadada"
  hairline-soft: "#e4e4e4"
  canvas: "#f9fafb"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ed9741"
  accent-red: "#de4c39"
  badge-green: "#ddf6cf"
  badge-green-text: "#2f3434"
  dark-canvas: "#2b2f2d"
  dark-canvas-alt: "#1f2323"
  star-rating: "#ed9741"
  price-text: "#de4c39"

typography:
  display-xl:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  price-sm:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px

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
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  button-accent-orange-active:
    backgroundColor: "#d97d2e"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-link:
    color: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-link-active:
    color: "{colors.primary}"
  nav-bar-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 4px 12px
  product-card-price:
    typography: "{typography.price-sm}"
    color: "{colors.price-text}"
    padding: 0 12px 8px 12px
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.badge-green-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
    padding: 0 12px 4px 12px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  footer-newsletter-input:
    backgroundColor: "{colors.dark-canvas-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  footer-newsletter-button:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and primary form submissions. Rendered in the brand teal (#108474) with white text and 8px rounded corners. On hover, shifts to a darker teal (#0d6b5d). Disabled state uses a muted green (#a9d092) to indicate inactivity without visual noise. Height is 44px with 12px vertical padding and 24px horizontal.

**`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Learn More". White background with dark ink text and a 1px hairline border. Active state darkens the border to ink color and adds a soft surface background. Same 44px height as primary for alignment in button groups.

**`button-accent-orange`** — Reserved for promotional contexts: newsletter signups, sale banners, and limited-time offers. Uses the orange accent (#ed9741) with white text and a slightly smaller 38px height to distinguish from primary CTAs. Hover darkens to #d97d2e.

### Cards
**`product-card`** — The core product display unit on collection pages and search results. A white card with 12px rounded corners, no border, and a subtle shadow (not specified in tokens but present in implementation). The image fills the top with rounded top corners only. Below the image, the title uses title-sm typography, price uses price-sm in red (#de4c39), and an optional star-rating row uses orange stars (#ed9741). A green badge (badge-green) may appear for "In Stock" or "New" labels.

**`product-card-badge`** — Small uppercase label pinned to the top-left of product images. Uses a light green background (#ddf6cf) with dark green text (#2f3434), 4px rounded corners, and 2px/8px padding. Font is 11px weight 600 with 0.3px letter spacing.

**`sale-badge`** — Red variant of the product badge for discount indicators. Uses accent-red (#de4c39) with white text. Same dimensions and typography as the green badge.

### Navigation
**`nav-bar`** — A fixed 64px top bar on the dark green canvas (#2b2f2d). Nav links are white, 15px weight 500 with 0.2px letter spacing, and 8px/16px padding. Active and hover states shift link color to the teal primary (#108474). The bar contains the brand logo on the left, category links in the center, and utility icons (search, cart, account) on the right.

**`search-bar`** — A pill-shaped search input (full rounded) with white background and 1px hairline border. On focus, the border thickens to 2px teal. Height is 40px with 8px/16px padding. Used in the nav bar on mobile and as a full-width element on the search page.

### Forms
**`text-input`** — Standard form input for checkout, account, and newsletter forms. White background with 1px hairline border and 8px rounded corners. Focus state swaps to a 2px teal border. Error state uses a 2px red border (#de4c39). Height is 44px with 10px/14px padding.

### Footer
**`footer`** — Full-width dark section using the same dark green (#2b2f2d) as the nav bar. Links are muted gray (#9a9a9a) and shift to teal on hover. The newsletter signup area uses a slightly darker input background (#1f2323) with an orange accent button (#ed9741). Section padding is 64px vertical and 32px horizontal.

### Hero
**`hero-banner`** — Full-width promotional banner on the homepage and campaign pages. Dark green background with white display text (32px weight 600). A single primary CTA button (teal, 48px height) sits below the headline. Padding is 48px vertical and 32px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column (2 columns max); hero banner text reduces to 24px; search bar moves to full-width below nav; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows abbreviated links (icons only for utility); product cards display in 2–3 columns; hero banner maintains 28px text; footer splits into 2-column layout |
| Desktop | 1128–1440px | Full nav bar with text links; product cards in 3–4 columns; hero banner at full 32px text; footer in 4-column grid |
| Wide | > 1440px | Content max-width capped at 1440px with centered container; product cards may show 4–5 columns; hero banner uses max-width 1200px centered |

### Touch Targets
- All buttons and interactive elements minimum 44px height (WCAG compliant)
- Nav bar links have 8px/16px padding for comfortable tap area
- Search bar at 40px height meets touch target minimum
- Product card CTAs maintain 44px height on all breakpoints
- Footer links have 12px minimum vertical padding on mobile

### Collapsing Strategy
- Nav bar links collapse to hamburger menu below 744px; utility icons (search, cart) remain visible
- Product grid reduces from 4 columns to 2 columns on tablet, to 1 column on mobile
- Footer grid reduces from 4 columns to 2 columns on tablet, to stacked single column on mobile
- Hero banner text reduces in size but remains full-width; CTA button shrinks to 40px height on mobile
- Search bar moves from nav bar to a full-width element below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary button hover states were reliably observed
- Error styling for form validation (beyond text-input error border) was not visible on the live site
- Dark mode is not implemented on the current site; all colors assume light mode
- Drop shadow values for product cards and modals could not be extracted; a subtle box-shadow is present but exact values are unknown
- Animation and transition durations (e.g., button hover, card hover lift) were not measurable
- The extracted font list included "JudgemeStar" (a review widget font) and "Muli" (likely legacy); Figtree appears to be the primary brand typeface based on usage frequency
- Sub-brand or campaign-specific palettes (e.g., holiday, collaboration) were not captured
- The extracted hex list contained many near-identical grays (#f7f7f7, #f9f9f9, #fafafa, #f0f0f0) — the palette above consolidates these into the most representative values
- Checkout flow styling (Shopify default vs. custom) could not be distinguished
