---
version: alpha
name: "Lanikai"
source_url: "https://www.lanikaiukuleles.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built around the warm resonance of wood and nylon, Lanikai uses a deep navy anchor (#003a70) as its primary voltage — a color that reads as both nautical and musical, evoking the midnight-blue fretboard of a concert ukulele. The site's canvas is a soft off-white (#fcfbfe) that avoids the sterile glare of pure white, while body text runs in #212121 for comfortable readability at 16px. What distinguishes Lanikai's palette from a generic instrument retailer is the presence of a muted lavender (#e9e6ed) used in secondary backgrounds and a cool gray (#cfc8d8) for subtle dividers — these lilac-tinged neutrals suggest the softness of a padded gig bag interior. The brand's secondary accent, a restrained navy (#293c5b), appears on hover states and footer backgrounds, creating a layered depth that mirrors the instrument's own construction. Typography relies on Montserrat for display headings — a geometric sans-serif with a musical rhythm in its letterforms — and Open Sans for body copy, both set at moderate weights (400–600) that let product photography carry the emotional weight. Buttons use a gentle 8px radius (`{rounded.sm}`) rather than sharp corners, and product cards employ a 12px radius (`{rounded.md}`) that echoes the curve of a ukulele body. The overall feel is unhurried and acoustic — a digital space that breathes like a slow strum.

colors:
  primary: "#003a70"
  primary-active: "#293c5b"
  primary-disabled: "#abcae9"
  ink: "#212121"
  body: "#121212"
  muted: "#515151"
  muted-soft: "#767676"
  hairline: "#c1c6c8"
  hairline-soft: "#d0d5d2"
  canvas: "#fcfbfe"
  surface-soft: "#e9e6ed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#293c5b"
  accent-lavender: "#cfc8d8"
  accent-blue: "#1863dc"
  accent-green: "#2f6627"
  accent-gold: "#ffba00"
  accent-red: "#aa0000"
  star-rating: "#ffba00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  button-icon-circle-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea-input:
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
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
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
    textColor: "{colors.ink}"
    padding: "12px 16px 4px 16px"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 16px 8px 16px"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "0 16px 12px 16px"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "80px 24px"
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  hero-cta:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "48px 24px 24px 24px"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    opacity: 0.3
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "24px"
  category-tile-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "24px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "16px 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 16px 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep navy (#003a70) with white text and an 8px radius (`{rounded.sm}`). Uses Montserrat 14px semibold uppercase with 0.5px letter-spacing for a confident, musical precision. On hover, shifts to `{colors.primary-active}` (#293c5b); disabled state fades to `{colors.primary-disabled}` (#abcae9). Height is 44px with 12px/24px padding.
**`button-secondary`** — An outlined variant with a white fill, navy text, and a 2px solid navy border. Active state darkens the border to `{colors.primary-active}`. Used for secondary actions like "View Details" or "Compare".
**`button-tertiary-text`** — A text-only button with no background or border, using navy text and the same uppercase Montserrat treatment. Used for "Learn More" links and filter resets.
**`button-icon-circle`** — A 40px circular button with navy fill and white icon, used for cart, wishlist, and search toggles. Outline variant swaps fill for a 2px navy border on white.

### Cards
**`product-card`** — A white card with a 12px radius (`{rounded.md}`) and no shadow — the brand relies on the product image to create depth. The image area uses `{rounded.md}` on top corners only, creating a subtle visual separation. Title uses 16px Montserrat semibold, price in 16px Open Sans regular, and rating in 13px caption gray. A gold badge (`{colors.accent-gold}`) can overlay the image for "Limited Edition" flags.
**`category-tile`** — A soft lavender (`{colors.surface-soft}`) tile with 12px radius used to display ukulele categories (Soprano, Concert, Tenor, etc.). Active state fills with navy and inverts text to white. Padding is 24px on all sides.

### Navigation
**`nav-bar`** — A 72px white bar with a subtle bottom border (`{colors.hairline-soft}`). Navigation links use Montserrat 14px medium uppercase in muted gray, switching to navy on active/hover. Sticky variant uses a stronger border (`{colors.hairline}`) for visual anchoring.
**`breadcrumb`** — Small 13px Open Sans links in muted gray, with the active page rendered in `{colors.ink}`. No separators — uses spacing alone.

### Forms
**`text-input`** — White input with a 1px hairline border and 8px radius. On focus, the border thickens to 2px and shifts to navy. Height is 48px with 12px/16px padding. Select and textarea variants follow the same pattern.
**`search-bar`** — A pill-shaped (`{rounded.full}`) white input with a 1px hairline border, 48px height, and 12px/20px padding. Focus state uses a 2px navy border.

### Footer
**`footer`** — A deep navy (`{colors.accent-navy}`) section with white text, 48px top padding and 24px bottom padding. Links are 14px Open Sans regular in white. Dividers between sections use `{colors.hairline-soft}` at 30% opacity for a subtle separation that doesn't compete with the dark background.

### Badges
**`badge-new`** — Green (#2f6627) background with white text, 4px radius, 11px Montserrat bold uppercase. Used for new arrivals.
**`badge-sale`** — Red (#aa0000) background with white text. Used for clearance items.
**`badge-limited`** — Gold (#ffba00) background with dark text. Used for limited edition instruments.

### Pagination
**`pagination-button`** — White button with a 1px hairline border, 8px radius, 36px height. Active state fills navy, disabled state uses soft lavender background with muted text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 48px 16px; search bar moves to sticky top; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 64px padding; search bar in header; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero at 80px padding; search bar in nav; footer uses four-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero centered with max-width 1200px; category tiles in 6-column grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40px with 44px touch area via padding
- Product card tap targets (title, price, image) are full-width with minimum 48px height
- Category tiles are minimum 120px tall for easy tapping
- Pagination buttons are 36px with 8px gap — consider 44px minimum on mobile

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button that opens a slide-out panel on mobile
- Footer columns collapse to single-column stacked layout below 744px
- Category tiles collapse from 6-column grid to 2-column grid on mobile
- Hero text reduces from 36px to 24px on mobile; CTA button remains full-width
- Search bar moves from inline in nav to a sticky top bar on mobile
- Product images switch from landscape to square crop on mobile to maintain visual consistency

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components could not be fully extracted from static CSS — primary-active (#293c5b) and primary-disabled (#abcae9) are inferred from common patterns
- Error styling for form inputs (border color, error text color) not present in extracted data — recommend #aa0000 for error borders with #121212 for error text
- Dark mode not present on the live site — no extracted colors or patterns to reference
- Sub-brand or collection-specific palettes (e.g., "Koa Series" vs "Mahogany Series") not captured — may use wood-tone accents not in extracted hex list
- Font weights beyond 400 and 600 not confirmed — extracted CSS shows Montserrat and Open Sans but weight values are inferred from common web usage
- Spacing values are inferred from typical e-commerce patterns — exact padding/margin values from the live site could not be reliably extracted
- Animation and transition durations not present in extracted data — recommend 200ms ease for hover states, 300ms ease for modals and slide-outs
- Modal and dialog styling (overlay opacity, close button placement) not captured — recommend 80% white overlay with 24px close button in top-right
- Checkout flow styling not present — the site does not appear to use Shopify, so checkout may be custom or use a third-party provider with its own styling
- Social media icon colors (Facebook blue #1863dc, Instagram purple #720eec, YouTube red #aa0000) appear in extracted hex list but are not part of the brand's core palette — these should be used only for their respective icons
- The extracted hex list contains many colors that appear to be from third-party widgets (Klarna pink, Afterpay blue, etc.) — these should not be used in brand components
- Star rating color (#ffba00 gold) is inferred from common e-commerce patterns — exact color not confirmed from extracted data
- Product swatch colors (wood finishes, ukulele body colors) not captured — these would be product-specific and not part of the design system
