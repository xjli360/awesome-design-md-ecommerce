---
version: alpha
name: "Educational Insights"
source_url: "https://www.educationalinsights.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A playful, curiosity-driven learning brand that uses a clean white canvas and a single vibrant accent — a warm, confident coral (#ff6b35) — to signal fun without sacrificing clarity. The coral appears on every primary CTA, the add-to-cart button, and the playful "Shop by Age" category badges, acting as a visual exclamation point against an otherwise restrained palette of deep navy ink (#1a1a2e), soft gray body text (#4a4a4a), and a warm off-white surface (#faf8f5) that softens the digital experience. Rounded corners are everywhere: product cards use a generous 12px radius (`{rounded.md}`), buttons are pill-shaped (`{rounded.full}`), and the search bar sits in a softly rounded container (`{rounded.lg}`), creating a tactile, approachable feel that mirrors the physical toys and games the brand sells. Typography runs a clean, geometric sans-serif — likely a variant of Montserrat or similar — with display headlines at 28px in weight 700, body copy at 16px in weight 400, and button labels at 14px in weight 600. The brand trusts large, friendly product photography and generous whitespace over dense copy, with a four-column grid on desktop that collapses to two on tablet and a single column on mobile. Navigation is straightforward: a sticky top bar with the logo, search, account, and cart icons, plus a secondary nav for categories (Science, Math, Reading, etc.). The overall mood is one of joyful discovery — the digital equivalent of a well-lit, organized classroom where every shelf invites exploration.

colors:
  primary: "#ff6b35"
  primary-active: "#e55a2b"
  primary-disabled: "#ffd4b3"
  ink: "#1a1a2e"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#faf8f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#4caf50"
  accent-blue: "#2196f3"
  accent-yellow: "#ffc107"
  badge-age-3-5: "#ff6b35"
  badge-age-6-8: "#4caf50"
  badge-age-9-12: "#2196f3"
  star-rating: "#ffc107"
  sale-badge: "#e53935"
  scrim: "rgba(0, 0, 0, 0.5)"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 15px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.sale-badge}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  secondary-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0, 0, 0, 0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-rating:
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    textAlign: "center"
  category-card-hover:
    backgroundColor: "{colors.hairline-soft}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 32px"
  age-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  age-badge-3-5:
    backgroundColor: "{colors.badge-age-3-5}"
  age-badge-6-8:
    backgroundColor: "{colors.badge-age-6-8}"
  age-badge-9-12:
    backgroundColor: "{colors.badge-age-9-12}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 44px
    border: "none"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    padding: "8px"
    border: "1px solid {colors.hairline}"
  wishlist-button-active:
    color: "{colors.sale-badge}"
  cart-icon:
    color: "{colors.ink}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "2px 6px"
    position: "absolute"
    top: "-4px"
    right: "-4px"
  account-icon:
    color: "{colors.ink}"
    height: 24px
  logo:
    height: 32px
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's coral (#ff6b35) with white text and a full pill shape. On hover, it shifts to a slightly darker coral (#e55a2b). The disabled state uses a pale coral (#ffd4b3) with white text. **`button-secondary`** — An outlined variant with a white fill, ink-colored text, and a 2px solid ink border. On hover, the background fills with the soft surface color (#faf8f5). **`button-tertiary-text`** — A text-only button in coral, used for secondary actions like "Learn More" or "View Details". **`button-pill-primary`** — A smaller pill button used for age badges and category filters, with the same coral fill and white text. **`button-pill-outline`** — A small pill button with a transparent fill, ink text, and a light gray border, used for less prominent filters.

### Cards
**`product-card`** — The primary product display unit, a white card with a 12px rounded corner and a subtle drop shadow. On hover, the shadow deepens. The card contains an image (1:1 aspect ratio, top-rounded corners), a title in 16px weight 600, a price in 16px weight 400, and a star rating. A badge can be overlaid on the image, positioned top-left, for promotions or age ranges. **`category-card`** — A soft, clickable card used for category navigation (e.g., "Science", "Math"). It has a soft off-white background, centered text, and a 12px rounded corner. On hover, the background darkens slightly.

### Navigation
**`nav-bar`** — The primary sticky navigation bar, 64px tall, with a white background and a thin bottom border. It contains the logo, search bar, account icon, and cart icon with a coral badge. **`secondary-nav`** — A 48px tall bar below the primary nav, with a soft off-white background, used for category links. Active links are underlined in coral. **`breadcrumb`** — A simple breadcrumb trail in muted gray, with the active page in ink. Separators are a lighter gray.

### Forms
**`text-input`** — A standard text input with a white fill, ink text, a 1px light gray border, and 8px rounded corners. On focus, the border becomes a 2px coral line. On error, the border becomes a 2px red line. **`select-dropdown`** — A styled select element matching the text input's dimensions and border. **`textarea`** — A multi-line text input with the same styling as the text input. **`newsletter-input`** — A pill-shaped input in the footer, with a white fill and no border, paired with a coral pill button.

### Footer
**`footer`** — A dark footer with a deep navy ink background and white text. Links are in a lighter gray and turn white on hover. The newsletter signup is a prominent feature, with a white pill input and a coral pill button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for products; nav collapses to hamburger menu; secondary nav becomes a scrollable horizontal strip; hero banner reduces padding; footer stacks vertically. |
| Tablet | 744–1128px | Two-column grid for products; nav remains expanded but secondary nav may collapse to a dropdown; hero banner uses moderate padding. |
| Desktop | 1128–1440px | Four-column grid for products; full nav with secondary nav visible; hero banner uses full section padding. |
| Wide | > 1440px | Max-width container (1440px) centered; four-column grid maintained; hero banner may use a wider layout. |

### Touch Targets
- All buttons and interactive elements are at least 44px tall (button-primary, button-secondary, text-input, etc.).
- Icon buttons (wishlist, cart, account) are at least 44x44px tap targets, even if the icon itself is smaller.
- Search bar is 40px tall, but the surrounding container provides a larger tap area.
- Category cards are at least 120px tall on mobile to ensure easy tapping.

### Collapsing Strategy
- Primary nav collapses to a hamburger menu on mobile (< 744px). The menu slides in from the left or right.
- Secondary nav collapses to a scrollable horizontal strip on mobile, or a dropdown select.
- Product grid collapses from 4 columns (desktop) to 2 (tablet) to 1 (mobile).
- Footer sections stack vertically on mobile.
- Hero banner text and CTA stack on mobile, with the CTA full-width.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations could not be extracted from the live site; the typography block uses educated guesses based on common educational brand choices (Montserrat for headings, Open Sans for body). Actual fonts may differ.
- No meta theme-color was found; the brand may not use one, or it may be set dynamically.
- No extracted hex colors were available from the live site; the color palette is an educated reconstruction based on common educational brand patterns and the brand's playful, coral-accented identity. Actual brand colors may differ.
- Hover, focus, and active states for many components (e.g., text-input-focus, product-card-hover) are inferred from common patterns and may not match the live site exactly.
- Error styling for forms (text-input-error) is inferred; the brand may use a different error color or pattern.
- The brand's use of dark mode, if any, is unknown.
- Sub-brand or seasonal color palettes (e.g., for specific product lines) are not captured.
- The exact spacing and padding values for many components are estimated; actual values may vary.
- The brand's use of animations, transitions, or micro-interactions is not documented.
