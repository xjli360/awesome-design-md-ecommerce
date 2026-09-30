---
version: alpha
name: "Rabbit"
source_url: "https://www.runinrabbit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A running brand that trusts a deep navy anchor (#283347) over the usual neon energy, letting a single electric accent (#00adef) act as the only jolt across a palette of charcoal grays (#515151, #363636, #4a5764) and warm off-whites (#e5e3df, #f5f5f5). The brand name itself — lowercase, set in a condensed sans that feels like a bib number — appears on nearly every product shot as a tonal watermark, a quiet signature that doesn't compete with the athlete. Buttons carry {rounded.full} pill shapes and that #00adef voltage, while product cards use {rounded.sm} corners and generous {spacing.base} padding to keep the shopping experience as uncluttered as a race course. The typography stack mixes Brandon-Regular (a geometric sans with humanist warmth) for display moments with Avenir Next for body copy, creating a system that reads fast at a glance — critical for a category where customers are often scrolling mid-run. The extracted color list is heavy on grays and social-icon blues (#1da1f1, #4266b2), but the true brand signature lives in that #283347/#00adef pairing: a midnight navy and a cyan that together suggest dawn on a long run, not a startup dashboard.

colors:
  primary: "#00adef"
  primary-active: "#0099d4"
  primary-disabled: "#b3e6ff"
  ink: "#283347"
  body: "#515151"
  muted: "#7a7a7a"
  muted-soft: "#b5b5b5"
  hairline: "#dbdbdb"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#283347"
  accent-charcoal: "#363636"
  accent-warm-gray: "#e5e3df"
  social-twitter: "#1da1f1"
  social-facebook: "#4266b2"
  social-pinterest: "#bd081d"
  sale-red: "#e50122"
  error: "#f14336"
  star-rating: "#ff5268"

typography:
  display-xl:
    fontFamily: "'Brandon-Regular', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brandon-Regular', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Brandon-Regular', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
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
    border: "2px solid {colors.ink}"
    padding: 10px 26px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "3:4"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.sale-red}"
  product-card-compare-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  social-icon-hover:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  size-selector-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
    height: 36px
  size-selector-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  size-selector-pill-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
  hero-section:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 28px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in the brand's electric cyan (#00adef). Used for "Add to Cart," "Shop Now," and primary checkout flows. On hover, shifts to a slightly deeper cyan (`{colors.primary-active}`) with no border change. Disabled state uses a pale cyan tint (`{colors.primary-disabled}`) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined pill button using the navy ink (`{colors.ink}`) as both text and border on a white background. Used for "View Details" and secondary actions where the primary button would overwhelm. Hover inverts to a solid navy fill with white text, providing a clear state change without relying on the brand's accent color.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel," "Clear Filters," and other low-emphasis actions. Relies on the body typography weight and the ink color, with no hover background change — only a color shift to `{colors.primary}` on hover.

**`button-sale`** — A red pill button (`{colors.sale-red}`) used exclusively for sale or clearance items. Matches the primary button's shape and padding but uses the sale red to create urgency without competing with the main brand accent.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). Navigation links are set in uppercase with 0.5px letter spacing, creating a clean, athletic feel. The active link is underlined with a 2px cyan bar (`{colors.primary}`), while inactive links sit in muted gray.

**`nav-link-active`** — The currently selected navigation item, distinguished by a 2px bottom border in the brand's cyan. No background change — the brand trusts the underline and uppercase weight to signal location.

**`nav-link-inactive`** — Default navigation links in muted gray (`{colors.muted}`), uppercase with tight tracking. Hover shifts to the ink color without underline, keeping the interface clean.

### Product Cards
**`product-card`** — The primary product display unit, a white card with `{rounded.sm}` corners and `{spacing.base}` padding. Product images use a 3:4 aspect ratio with `{rounded.xs}` corners, creating a subtle frame within the card. Price is set in `{typography.title-sm}` in the ink color, while sale prices shift to red with the original price shown as a line-through in muted gray.

**`product-card-badge`** — A small cyan pill badge (`{colors.primary}`) with uppercase white text, used for "New" or "Best Seller" tags. Positioned at the top-left of the product image.

**`product-card-sale-badge`** — Same shape as the standard badge but in sale red (`{colors.sale-red}`), used for "Sale" or "Clearance" tags.

### Forms & Inputs
**`text-input`** — Standard text input with a white background, `{rounded.sm}` corners, and a light gray border (`{colors.hairline}`). On focus, the border thickens to 2px and switches to the brand's cyan, providing a clear but understated focus indicator.

**`search-bar`** — A full pill-shaped search field (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`) and a subtle border. On focus, the border becomes a 2px cyan ring, maintaining the pill shape. Used in the header and on collection pages.

**`size-selector-pill`** — Individual size options rendered as small pill buttons with a white background and gray border. The active state fills with navy ink and white text, while disabled sizes show a line-through style on a soft gray background — a clear visual language for availability without relying on color alone.

**`quantity-selector`** — A compact input with `{rounded.sm}` corners and a gray border, used for adjusting item quantities in the cart. Maintains the same border and typography as text inputs for consistency.

### Footer
**`footer-section`** — A full-width footer with a navy background (`{colors.accent-navy}`) and white text, creating a strong visual anchor at the bottom of every page. Links are set in muted gray (`{colors.muted-soft}`) and shift to the brand's cyan on hover, echoing the primary accent against the dark background.

**`social-icon`** — Circular social media icons (36px) in muted gray against the navy footer. On hover, they shift to the brand's cyan, providing a subtle interactive cue without introducing the social platforms' native colors.

### Hero
**`hero-section`** — Full-width hero banners with a navy background and white text, used for collections and seasonal campaigns. The heading uses the largest display typography, while the CTA button follows the primary button pattern in cyan. The navy backdrop makes the cyan button pop without competing with product photography.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards stack in 2-column grid; hero heading drops to `{typography.display-md}`; size-selector pills wrap to 3 per row; footer links stack vertically |
| Tablet | 744–1128px | Nav-bar shows full links with reduced letter-spacing; product cards in 3-column grid; hero maintains `{typography.display-lg}`; search bar shrinks to 40px height |
| Desktop | 1128–1440px | Full nav-bar with uppercase links; product cards in 4-column grid; hero uses `{typography.display-xl}`; all components at default sizing |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid with increased padding; hero section uses wider margins |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px with 48px tap area via padding
- Size-selector pills are 36px tall with 44px tap area
- Search bar maintains 44px height on mobile
- Nav links have 48px tap area on mobile via expanded padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-in drawer for links
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer link columns collapse to accordion-style sections below 744px
- Size selector pills wrap to 2 columns on mobile to prevent horizontal scrolling
- Hero text stacks vertically below 744px, with the CTA button full-width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale) could not be reliably extracted — the current implementation uses a subtle shadow on hover, but exact values are unconfirmed
- Error states for form inputs (validation styling, error message typography) were not present in the extracted data
- Dark mode is not supported — all extracted colors assume a light theme
- Sub-brand or collection-specific palettes (e.g., trail running, marathon) could not be identified
- The extracted font list includes many fallbacks (Arial, Helvetica, Segoe UI, fantasy) that may not be actively used — Brandon-Regular and Avenir Next appear to be the primary choices, but exact font loading configuration is unknown
- Social icon colors (#1da1f1, #4266b2, #bd081d) are likely platform defaults rather than brand choices — the brand may use monochrome icons in practice
- The extracted color list is heavily weighted toward grays and blues, which may include Shopify admin elements or checkout widgets — the true brand palette may include additional accent colors not captured
- Star rating color (#ff5268) was extracted from a single instance and may not be the brand's standard rating color
- Animation durations and easing curves (transitions, hover effects) were not extractable from static CSS
- Mobile navigation drawer styling (background, overlay, close button) could not be determined
- Cart and checkout page styling was not included in the extraction scope
