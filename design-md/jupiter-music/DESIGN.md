---
version: alpha
name: "Jupiter Music"
source_url: "https://www.jupitermusic.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep teal #007581 — the color of a brass bell's patina after years of play — anchors Jupiter Music's digital presence, appearing in primary CTAs, navigation highlights, and product-badge accents against a neutral canvas of #ffffff and soft gray surfaces at #f7f7f7. The brand's typographic voice is absent from extracted data, but the visual system relies on generous whitespace and a restrained palette of three core grays (#555555, #35373c, #f0f0f0) to let instrument photography and product details command attention. Buttons carry a subtle {rounded.sm} radius — friendly enough for a music educator browsing, precise enough for a professional musician. The top navigation sits at 80px height with a clean white background, using the teal only for active states and the primary "Shop" call-to-action. Product cards use {rounded.md} corners and a soft drop shadow, presenting saxophones, flutes, and trumpets as aspirational objects rather than commodity goods. The brand's secondary accent — a warm brass-gold #c8a84e — appears sparingly on sale badges and limited-edition callouts, echoing the physical instruments' hardware. This is a system built for clarity: high-contrast body text at #35373c on white, muted secondary text at #555555, and hairline borders at #e0e0e0 that separate sections without visual noise. The absence of a declared typeface suggests either a system font stack or a brand font that couldn't be extracted — a known gap that would define the brand's personality once resolved.

colors:
  primary: "#007581"
  primary-active: "#005a63"
  primary-disabled: "#b3d9dc"
  ink: "#35373c"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#c8a84e"
  accent-gold-light: "#f0e6c8"
  sale-badge: "#c8a84e"
  error: "#d32f2f"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 24px
    height: 48px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-light}"
    textColor: "{colors.ink}"
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
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: 720px
  hero-subheading:
    typography: "{typography.body-lg}"
    color: "{colors.body}"
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  divider:
    height: 1px
    backgroundColor: "{colors.hairline}"
    margin: "{spacing.lg} 0"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  filter-chip-hover:
    backgroundColor: "{colors.hairline-soft}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  category-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Shop Now", "Add to Cart", and "Learn More" actions. Filled with the brand teal #007581, white text, and a subtle 8px radius that feels approachable without being casual. On hover, darkens to #005a63; disabled state uses a pale teal #b3d9dc to signal inactivity without disappearing. The 48px height meets WCAG touch-target minimums.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Compare Models". White background with a 2px teal border, maintaining the same 48px height and 8px radius as the primary. On hover, the background shifts to the soft gray surface #f7f7f7 and the border darkens to the active teal.

**`button-tertiary`** — A text-only button for inline actions within product cards or filter bars. No background or border — just teal text at 16px/600 weight. Used for "Quick View", "Add to Wishlist", and similar low-emphasis actions.

**`button-gold`** — Reserved for premium or limited-edition callouts, using the brass-gold #c8a84e as background with dark ink text. Appears on "Limited Edition" product pages and special collection banners. The gold-light variant (#f0e6c8) serves as the hover state.

### Cards
**`product-card`** — The core product display unit, used in grid layouts for saxophones, flutes, trumpets, and clarinets. White background with a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)) and 12px rounded corners. Contains a 4:3 aspect-ratio product image, title in 18px/600 weight, and price in 16px/400 weight. On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.12) for a subtle lift effect.

**`category-card`** — Used on the homepage and navigation to showcase instrument families (Brass, Woodwinds, Marching, etc.). Larger than product cards with 24px padding and a lighter shadow (0 1px 4px rgba(0,0,0,0.06)). On hover, gains a 1px teal border and a more pronounced shadow to indicate selection.

### Navigation
**`nav-bar`** — A fixed 80px header with white background and a 1px soft hairline bottom border (#f0f0f0). Contains the Jupiter Music logo on the left, primary navigation links (Instruments, Accessories, Education, Support) in the center, and utility icons (Search, Account, Cart) on the right. Active nav links show a 2px teal underline; hover states shift text to teal.

**`filter-chip`** — Pill-shaped filter buttons used in product listing pages for sorting by category, price range, or instrument type. 36px height with soft gray background (#f7f7f7) and 14px/600 weight text. Active state fills with teal and white text; hover state darkens the background to #f0f0f0.

### Forms
**`text-input`** — Standard form input for search, account forms, and checkout. 48px height with 16px horizontal padding, 8px radius, and a 1px hairline border. On focus, gains a 2px teal border. Error state uses a 2px red border (#d32f2f). The clean, minimal styling keeps the focus on the content rather than the container.

**`search-bar`** — A full-radius pill input used in the hero section and mobile navigation. Same 48px height as standard inputs but with 20px horizontal padding and fully rounded ends. On focus, the border thickens to 2px teal, creating a clear visual anchor for the search action.

### Badges
**`sale-badge`** — A small uppercase label in brass-gold #c8a84e with dark ink text, used to highlight discounts, clearance items, or limited-time offers. 4px radius with 4px/8px padding, positioned at the top-left corner of product card images.

**`new-badge`** — A teal-filled badge (#007581) with white text for new arrivals or recently added products. Same dimensions and positioning as the sale badge, but using the brand primary color to signal freshness rather than urgency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to 28px; filter chips stack vertically; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce font size to 14px; hero maintains two-column layout; filter chips wrap in a horizontal scroll |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero uses two-column layout with image and text side by side; filter chips in a single horizontal row |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for WCAG compliance
- Filter chips at 36px height are below the 44px recommendation but are used in non-critical contexts; primary actions use 48px height
- Product card tap targets (title, price, image) are each minimum 48px tall in mobile layouts
- Nav bar hamburger icon and utility icons are 44x44px minimum tap area

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 4 columns to 1 column on mobile, with 16px gutters
- Hero section stacks vertically on mobile — text above image — with 24px spacing between elements
- Filter chips collapse from a horizontal row to a vertical list with a "Filters" toggle button
- Footer links collapse from 4 columns to 2 columns on tablet, single column on mobile
- Search bar moves from inline in the nav to a full-width expandable section below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Typography**: No font-family declarations were extracted from the live site. The system font stack (Inter, system-ui) is assumed as a placeholder. The actual brand typeface — whether a custom font, a Google Font, or a system stack — remains unknown and would significantly impact the brand's visual identity.
- **Hover states**: While some hover behaviors are inferred from common patterns (darkening primary, shadow lift on cards), the actual extracted hover values (color transitions, timing, easing curves) are not available.
- **Focus states**: Keyboard focus indicators, outline styles, and focus-visible behaviors are not extracted. Assumed to use a 2px teal outline for accessibility.
- **Error states**: Form validation styling (error messages, success states, helper text) is not extracted. Error color #d32f2f is a common default, not confirmed from the live site.
- **Dark mode**: No dark mode implementation was detected. The brand may not support it, or it may be behind a user preference that wasn't captured.
- **Sub-brand palettes**: Jupiter Music may have distinct color treatments for sub-brands (e.g., Jupiter Marching, Jupiter Education) that were not extracted.
- **Animation tokens**: Transition durations, easing curves, and micro-interaction timings are not available. Assumed 200-300ms ease-in-out for hover states.
- **Iconography**: The extracted data does not include icon styles, stroke weights, or icon set used. The brand may use custom instrument illustrations or a standard icon library.
- **Photography treatment**: While product photography is central to the brand, the specific image treatment (color grading, overlay gradients, aspect ratios beyond 4:3) is not extracted.
- **Checkout flow**: Shopify Pay, Klarna, or Afterpay widget colors may appear in the extracted palette but are not part of the brand's core design system. These are noted as potential noise in the extracted colors.
