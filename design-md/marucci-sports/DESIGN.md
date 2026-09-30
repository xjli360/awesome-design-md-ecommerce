---
version: alpha
name: "Marucci Sports"
source_url: "https://maruccisports.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built for the batter's box, where #010101 near-black meets #db1e36 — a red that carries the crack of the bat. The palette is deliberately restrained: deep ink (#231f20) for body text, a range of warm grays (#f4f4f4, #f0f0f0, #e5e5e5) for surfaces and hairlines, and a single accent red (#da020f) that signals urgency on sale badges and clearance markers. The typography leans on Anton and Oswald — both condensed, all-caps display faces that read like jersey lettering — paired with Gotham for body and navigation. There is no softness here: corners are either sharp ({rounded.none}) or minimally rounded ({rounded.xs}), and buttons sit at a compact 40px height. The brand trusts its red to do the work — it appears only on primary CTAs, price badges, and the Marucci "M" mark. Everything else recedes into the grayscale, letting product photography and the red itself carry the emotional weight.

colors:
  primary: "#db1e36"
  primary-active: "#c40014"
  primary-disabled: "#f0b0b8"
  ink: "#010101"
  body: "#231f20"
  muted: "#494949"
  muted-soft: "#888888"
  hairline: "#c4c4c4"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-strong: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-sale: "#da020f"
  accent-blue: "#216ba5"
  badge-gold: "#ffb13b"
  badge-green: "#bfcd14"
  star-rating: "#ffb13b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Anton', 'Oswald', 'Goldman', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Anton', 'Oswald', 'Goldman', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Anton', 'Oswald', 'Goldman', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.25px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Anton', 'Oswald', 'Goldman', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.15px
    textTransform: uppercase
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 23px
    height: 40px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 23px
    height: 40px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    height: "500px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, always filled with Marucci red (#db1e36) and white uppercase type. On hover, the red deepens to #c40014. The disabled state drops to a pale pink (#f0b0b8) with white text. Compact at 40px height with minimal 4px rounding, the button reads as athletic and direct — no wasted space.

**`button-secondary`** — A white button with black text, used for secondary actions like "View Details" or "Add to Cart" alongside a primary button. The outline variant adds a 2px solid black border for visual weight. Hover state fills the background with #f4f4f4.

**`button-tertiary-text`** — A text-only button in Marucci red, used for links like "Shop All" or "Learn More" within content sections. No background, no border — just the red text with a hover underline.

**`button-pill-red`** — A fully rounded pill variant of the primary button, used for promotional banners or sticky CTAs. Same red fill, but shorter at 36px with 8px vertical padding and 20px horizontal.

### Navigation
**`top-nav`** — A white 72px bar with uppercase nav links in Gotham 600. The active link gets a 2px red bottom border and red text. Inactive links are black. The nav collapses to a hamburger menu on mobile, with the Marucci logo centered.

**`nav-link-active`** — Active state with red text and a 2px red underline. Used for the current page or section.

**`nav-link-inactive`** — Default state with black text. Hover transitions to red text with no underline.

### Cards
**`product-card`** — A clean white card with no rounding, relying on product photography for visual interest. The card contains the product image, name, price, and a color swatch strip. On hover, a subtle box shadow lifts the card. The price is always displayed in the primary red badge.

**`product-card-hover`** — Hover state with a soft box shadow (0 4px 12px rgba(0,0,0,0.08)). No border or rounding change — the shadow alone signals interactivity.

### Badges
**`price-badge`** — A small red badge with white uppercase text, used to display the current price on product cards. Minimal 4px rounding and 2px vertical padding keep it compact.

**`sale-badge`** — A bright red (#da020f) badge for sale or clearance items. Same shape as the price badge, but a more urgent red.

**`new-badge`** — A green (#bfcd14) badge for new arrivals. Uses the same compact shape and uppercase typography.

### Hero
**`hero-section`** — A full-width section with a black (#010101) background and white text. The display typography uses Anton at 48px with 1px letter spacing, all caps. The hero typically features a single product image or athlete photo overlaid with the headline and a primary CTA button.

### Footer
**`footer`** — A black (#010101) footer with white body text and gray links (#888888). Links are Gotham 14px regular weight. The footer contains columns for product categories, customer service, and social links.

**`footer-link`** — Footer links in muted gray (#888888) with no underline. Hover transitions to white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger; hero height reduces to 300px; product cards stack in single column; footer columns stack vertically |
| Tablet | 744–1128px | Nav remains horizontal but reduces font size to 12px; hero height at 400px; product cards in 2-column grid; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with 14px type; hero at 500px; product cards in 3-4 column grid; footer in 4 columns |
| Wide | > 1440px | Max-width container at 1440px; hero height scales to 600px; product cards in 4-5 column grid |

### Touch Targets
- All buttons and links maintain a minimum 44px touch target height on mobile
- Nav hamburger icon is 48px × 48px
- Product card tap area covers the full card
- Search bar tap area is 40px height minimum

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button that opens a drawer on mobile
- Footer columns stack to single column below 744px
- Hero text overlay reduces font size from 48px to 28px on mobile
- Product image galleries collapse to single-image view with dots on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; only primary button hover was confirmed
- Error states for form inputs (text fields, search) were not observed
- Dark mode is not present on the live site; no dark mode tokens are defined
- Sub-brand palettes (Marucci Pro, Marucci Youth, etc.) may exist but were not extracted
- The exact font weights for Gotham (400, 600, 700) are inferred from common usage; the live site may use additional weights
- The `textTransform: uppercase` on display and button typography is inferred from the all-caps nature of Anton/Oswald and common sports-brand patterns; not all instances may be uppercase
- Spacing values for component padding (e.g., button padding) are estimated from common patterns; exact values may vary
- The `boxShadow` on product-card-hover is an estimate; the live site may use a different shadow value
- The `border` property on button-secondary-outline is inferred; the live site may use a different border width or color
- The `height` values for hero and nav are estimated from common sports-brand patterns; exact values may vary
