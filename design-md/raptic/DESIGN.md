---
version: alpha
name: "Raptic"
source_url: "https://www.rapticstrong.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark canvas of #111111 sets the stage for a brand that sells armor for phones — not through grit, but through a clean, almost surgical precision. The primary voltage is #108474, a deep teal that reads as industrial and reliable, not playful; it appears on primary CTAs, selected states, and the brand's signature badge system. A secondary accent of #ffac00 (amber) and its near-twin #fbcd0a (golden yellow) provide the only warmth, used sparingly on sale flags, rating stars, and promotional ribbons. The typography stack pairs Archivo (a geometric sans with sharp, squared terminals) for display and button text with Nunito Sans (a softer, rounded sans) for body copy — a deliberate tension between the brand's protective, angular hardware and the approachable interface that sells it. Every corner is softly rounded ({rounded.sm} on buttons, {rounded.md} on product cards), but never pill-shaped: the brand avoids the friendly extremes of consumer tech, preferring a 12px radius that feels engineered rather than cuddly. The checkout flow, powered by Shopify, introduces a secondary palette of social-login blues (#3b5998, #1da1f2, #dd4b39) and payment-widget colors, but the core experience stays anchored in the dark teal and near-black (#121212) of the navigation and footer. Product cards float on a #f9fafb canvas with #eeeeee dividers, and the star-rating system uses #ffac00 against #555555 text — a consistent signal that the brand's confidence comes from protection, not personality.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#8ccfc2"
  ink: "#111111"
  body: "#444444"
  muted: "#555555"
  muted-soft: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ffac00"
  accent-gold: "#fbcd0a"
  star-rating: "#ffac00"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-google: "#dd4b39"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"
  footer-bg: "#121212"
  footer-text: "#aaaaaa"
  badge-teal: "#108474"
  badge-amber: "#ffac00"
  badge-lavender: "#a89cc8"
  badge-mint: "#c1e6e6"

typography:
  display-xl:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "'Archivo', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-compare:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-amber-active:
    backgroundColor: "#e69900"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid #c13515"
    textColor: "#c13515"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.15)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-amber}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-amber}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-amber}"
  product-card-price-compare:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted-soft}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-lavender:
    backgroundColor: "{colors.badge-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-mint:
    backgroundColor: "{colors.badge-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  social-icon:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    height: 44px
    padding: "0 12px"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature teal (#108474) with white uppercase text. Uses Archivo at 14px with 0.5px letter-spacing for a confident, engineered feel. On hover, shifts to `primary-active` (#0d6b5c); disabled state uses `primary-disabled` (#8ccfc2). The 8px radius (`{rounded.sm}`) keeps the button feeling precise rather than pill-soft.

**`button-secondary`** — A white button with a thin hairline border (#dedede) and dark ink text. Used for "Add to Cart" when the primary is reserved for "Buy Now" or checkout. Active state fills the background with `surface-soft` (#f2f2f2) and darkens the border to `muted` (#555555).

**`button-amber`** — The promotional accent button, using `accent-amber` (#ffac00) with dark ink text. Reserved for sale banners, limited-time offers, and "Shop Sale" CTAs. Active state darkens to #e69900.

**`button-ghost`** — A text-only button with teal text on transparent background. Used for "Learn More" links within product cards and secondary navigation. Active state adds a subtle `surface-soft` background.

### Text Inputs & Forms
**`text-input`** — Standard text input with white background, 1px hairline border, and 8px radius. Focus state swaps to a 2px teal border with no outline. Error state uses a red border (#c13515) and red text for the error message. Height is 44px with 12px/16px padding for comfortable touch targets.

**`select-input`** — Matches the text input structure but includes a custom dropdown arrow. Same height, radius, and border treatment.

**`quantity-selector`** — A horizontal stepper with a central input field flanked by minus/plus buttons. The buttons use `surface-soft` background and sit flush against the input border. Used on product detail pages for cart quantity adjustment.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height on a near-black background (#111111). Navigation links are set in Archivo uppercase at 13px with 0.5px letter-spacing — the brand's most formal typographic treatment. Active and hover states shift link color to `accent-amber`. On scroll, a subtle box-shadow appears. The Shopify cart icon and search icon sit on the right, rendered in white.

**`nav-link`** — Individual navigation items with 8px/16px padding. The uppercase, tightly-spaced Archivo treatment gives the nav a technical, protective feel — like specs on a military-grade case.

### Product Cards
**`product-card`** — A white card with 12px radius (`{rounded.md}`) and a subtle 1px/3px box-shadow. On hover, the shadow deepens to 4px/12px. The card image uses the same radius on top corners only, creating a clean break between photo and content. Title uses `title-sm` (16px Archivo semibold), price uses `price` (18px Archivo bold). Sale items show the sale price in `accent-amber` with the compare-at price in `muted-soft` with a line-through.

**`badge`** — Small uppercase labels (10px Archivo bold, 0.5px letter-spacing) with 4px radius. Available in four color variants: teal (primary), amber (sale), lavender (new arrival), and mint (eco-friendly). Padding is tight at 2px/8px to sit neatly on product images or card corners.

**`star-rating`** — Rendered in `accent-amber` (#ffac00) at 14px. Used on product cards and review sections. Empty stars use `muted-soft` (#7b7b7b).

### Footer
**`footer`** — A dark section on `footer-bg` (#121212) with 64px vertical padding. Text is set in Nunito Sans at 14px in `footer-text` (#aaaaaa). Column headings use `title-sm` in white. Links hover to white. Social media icons (24px circles) use their respective brand colors.

### Accordion
**`accordion`** — Collapsible sections with white background, 1px hairline border, and 8px radius. Headers use `title-sm` with 16px/24px padding. Content area has 24px left/right padding and 16px bottom padding. Used on product detail pages for specs, shipping info, and warranty details.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), hamburger nav replaces top nav links, footer collapses to stacked columns, product images full-width, buttons full-width, accordion always expanded |
| Tablet | 744–1128px | Two-column product grid, top nav shows 4-5 links with "More" dropdown, footer in 2 columns, product detail page uses 50/50 image/text split |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, footer in 4 columns, product detail page has sticky add-to-cart sidebar |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid can show 4 columns on collection pages |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Product card tap targets extend to the full card area on mobile.
- Quantity selector buttons are 44px × 44px minimum.
- Nav links have 8px/16px padding, ensuring adequate tap area even on dense layouts.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px. The hamburger icon is a 24px icon in white.
- Footer columns collapse from 4 to 2 at tablet, then to a single stacked column on mobile.
- Product filters (on collection pages) collapse into a slide-out drawer on mobile.
- Accordion sections on product detail pages collapse/expand independently on all breakpoints.
- Search bar collapses to an icon on mobile, expanding to full-width on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom, alternate image reveal) could not be reliably extracted from the static HTML.
- Active/visited states for footer links are assumed based on common patterns but not confirmed from the live site.
- Error styling for form validation (beyond the text-input error state) — such as inline error messages, success states, and disabled input styling — was not observed.
- Dark mode is not present on the site; no dark mode tokens are defined.
- The `#a89cc8` (lavender) and `#c1e6e6` (mint) colors appear in the extracted palette but their specific usage context is unclear — they may be used for limited-edition product badges or seasonal promotions. Their application as badge variants is an informed guess.
- Social icon colors (#3b5998, #1da1f2, etc.) are standard brand colors for Facebook, Twitter, Google, Pinterest, and LinkedIn — their exact size and placement in the footer is inferred from common Shopify patterns.
- The `#ffff00` (pure yellow) in the extracted palette is likely a temporary sale or promotional accent, not a core brand color. It is not included in the primary palette.
- Font weights for Archivo and Nunito Sans beyond the extracted declarations (e.g., 300, 400, 600, 700) are assumed based on common web usage — the exact weight availability on the live site was not verified.
- The `Baskerville` font-family declaration in the extracted list is likely used for a specific decorative element (e.g., a logo or quote) and is not part of the core system. It is omitted from the typography tokens.
- `JudgemeIcons` and `JudgemeStar` font families are from the Judge.me review app and are not part of the brand's design system. They are used for star ratings and review icons.
- `monospace` and `sans-serif` are generic fallbacks, not brand fonts.
- The `#3b5998` (Facebook blue), `#1da1f2` (Twitter blue), `#dd4b39` (Google red), `#e60023` (Pinterest red), and `#0073b1` (LinkedIn blue) are standard social media brand colors and are included as social-icon tokens, not as core brand colors.
- The `#111111` and `#121212` near-black colors are used for the nav bar and footer respectively — their exact relationship (one is slightly warmer than the other) is noted but the difference is minimal.
- The `#f9fafb` canvas color is a very light gray, nearly white — it may be the same as the page background in some sections, with `#ffffff` reserved for card surfaces.
