---
version: alpha
name: "Satisfy"
source_url: "https://satisfyrunning.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A monochrome running brand that finds its voltage in the gap between raw concrete and warm stone — the palette runs from #121212 ink through #5c5951 stone to #baafa4 sand, all held by a #f8f9f9 canvas that reads as slightly warm off-white rather than clinical white. The brand’s signature move is the use of ABC Simon Mono as its primary display face — a monospaced grotesk that gives product names, size labels, and navigation the authority of a factory spec sheet or a military-issue tag. This is not the breathless aspirational language of performance sportswear; it is the deadpan precision of a garment that knows exactly what it is. Body copy runs in ABC Walter Neue, a clean geometric sans with slightly compressed proportions, while Assistant appears as a utilitarian fallback for checkout and utility text. The site uses hard corners everywhere — {rounded.none} on cards, buttons, inputs — and the only curve in the system is the {rounded.full} pill used on size-selector chips and the cart quantity badge, a deliberate tension between the brutalist grid and the softness of a single worn-in cotton tee. Product photography is high-contrast, often underexposed, with models shot against raw studio backdrops or outdoor grit; the brand trusts texture and shadow over color. The checkout flow introduces a secondary accent in #fefff2, a pale bone-white that sits between canvas and sand, used for order-summary backgrounds and confirmation panels. There is no hero carousel, no lifestyle video — the homepage leads with a static grid of product thumbnails and a single line of monospaced type, as if the store were a rack in a concrete room.

colors:
  primary: "#121212"
  primary-active: "#2a2a2a"
  primary-disabled: "#b6b6b6"
  ink: "#121212"
  body: "#5c5951"
  muted: "#b6b6b6"
  muted-soft: "#d3d3d3"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f8f9f9"
  surface-soft: "#f3f4f4"
  surface-card: "#ffffff"
  on-primary: "#f8f9f9"
  sand: "#baafa4"
  bone: "#fefff2"
  stone: "#5c5951"
  light-stone: "#dbdfe0"
  warm-gray: "#e5e0db"
  badge-bg: "#121212"
  badge-text: "#f8f9f9"

typography:
  display-xl:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'ABC Walter Neue', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'ABC Walter Neue', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01px
  body-md:
    fontFamily: "'ABC Walter Neue', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABC Walter Neue', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'ABC Walter Neue', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
  price:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  size-label:
    fontFamily: "'ABC Simon Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "24px 16px"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-sold-out:
    textColor: "{colors.muted}"
    opacity: 0.5
  size-selector-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.size-label}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  size-selector-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  size-selector-chip-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    cursor: not-allowed
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid transparent"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  notification-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: "0 12px"
    height: 40px
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Solid black (#121212) rectangle with zero border-radius, set in ABC Simon Mono uppercase 13px. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to #2a2a2a to signal interactivity without breaking the monochrome grid. Disabled state uses #b6b6b6 text on #b6b6b6 background — the button becomes a ghost of itself, barely legible, which is intentional: if you can't buy, the system doesn't pretend you can.

**`button-secondary`** — Outlined variant for secondary actions like "View Size Guide" or "Continue Shopping". White background with a 1px solid black border, same monospaced uppercase treatment. On hover, fills with #f3f4f4 surface-soft. The outline weight stays consistent — no thickening on interaction.

**`button-text`** — Ghost button used for tertiary actions like "Clear Filters" or "Cancel". No background, no border, just black monospaced text. Underlined on hover via text-decoration rather than border-bottom, to keep the baseline grid clean.

**`button-pill`** — The only curved button in the system, used exclusively for size-selector chips and filter tags. Full border-radius, 36px height, black fill. The pill shape signals "this is a toggle, not an action" — it's the brand's single concession to softness, and it's reserved for selection mechanics.

### Navigation
**`nav-bar`** — Fixed top bar at 72px height, white background with a 1px #e5e5e5 bottom border. Logo sits left-aligned in ABC Simon Mono, navigation links in 12px uppercase monospaced. The bar is deliberately sparse — no search icon, no cart icon visible until scroll or hover triggers a secondary bar. The brand name IS the navigation.

**`nav-link`** — Uppercase monospaced 12px links with 24px vertical padding. Active state gets a 2px solid black bottom border that sits inside the nav-bar's bottom border, creating a subtle nested-line effect. No hover color change — only the underline appears.

### Cards
**`product-card`** — Zero-radius card with white background and no shadow. The product image fills the top, with title and price set below in ABC Walter Neue (title) and ABC Simon Mono (price). Sold-out items render at 50% opacity with muted text — the card doesn't hide, it fades. No quick-add button, no color swatches, no hover overlay. The product speaks for itself.

**`product-card-title`** — 14px/600 weight in ABC Walter Neue, set in black. No truncation — if the product name is long, it wraps to two lines max.

**`product-card-price`** — 14px monospaced in #5c5951 stone. No currency symbol on the PDP grid; the dollar sign appears only on the product page itself.

### Forms
**`text-input`** — Rectangular input with 1px #dedede border, 48px height, 12px/16px padding. On focus, border switches to solid black with no outline ring — the brand avoids the blue glow that most systems use. Error state uses the same black border but with black text, since the only error worth signaling is "this field is required" and the brand trusts the user to see the missing data.

**`select-input`** — Same dimensions and border as text-input, with a custom chevron in black. No background color change on hover — the select is a utility, not an experience.

**`size-selector-chip`** — Pill-shaped toggle at 36px height with 1px #dedede border and 8px/16px padding. Active state fills black with white text. Disabled state uses #f3f4f4 background with #b6b6b6 text and a not-allowed cursor — sizes that are out of stock are visually removed from consideration.

### Badges & Indicators
**`cart-badge`** — 20px circle (full border-radius) in solid black, containing white monospaced 10px text. Sits at the top-right of the cart icon. The number is the only dynamic element in the nav — it appears and disappears without animation.

**`notification-bar`** — 36px black bar at the top of the page for announcements ("Free shipping on orders over $200"). Set in 11px uppercase monospaced caption. Dismissible via an X button in the same typeface. The bar sits above the nav, separated by a 1px hairline.

### Dividers & Structure
**`divider`** — 1px solid #dedede line used between sections. `divider-soft` uses #e5e5e5 for less visual weight inside cards or accordion panels. No spacing is built into the divider component — it's a pure line that relies on parent padding.

### Footer
**`footer`** — Full-width black (#121212) section with white text. Links are set in ABC Walter Neue 13px with no underline by default; underline appears on hover. The footer uses the same monospaced uppercase for section headers ("Support", "About", "Legal") and body weight for link content. No social icons — the brand doesn't link out.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes 2 columns; hero text reduces to 24px; footer stacks vertically; size-selector chips become full-width |
| Tablet | 744–1024px | Nav shows 4-5 links; product grid at 3 columns; hero at 28px; footer splits into 2 columns |
| Desktop | 1024–1440px | Full nav with all links; product grid at 4 columns; hero at 36px; footer at 4 columns |
| Wide | > 1440px | Max-width container at 1440px; product grid stays at 4 columns with increased whitespace; hero text at 40px |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain minimum 44px tap target height
- Size-selector chips are 36px height but padded to 44px tap area via invisible extension
- Nav hamburger icon is 48x48px tap target
- Cart badge is 20px but sits inside a 44x44px icon container
- Accordion headers are 48px minimum height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button that opens a drawer on mobile
- Footer columns collapse to single-column accordion on mobile
- Size selector chips wrap to two rows on mobile instead of scrolling horizontally
- Hero section reduces padding from 64px to 32px on mobile
- Product images switch from 4:5 to 1:1 aspect ratio on mobile for better thumb visibility

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns; the live site may use different transitions or color shifts
- Error styling for form validation (error messages, border colors on invalid inputs) could not be extracted
- Focus ring styles (outline color, width, offset) are not present in the extracted data — assumed to use the primary black with 2px offset
- Dark mode is not implemented on the live site; no dark palette exists
- Sub-brand or collection-specific color variations (e.g., limited edition drops) may exist but were not captured
- Animation durations and easing curves are not specified — the site appears to use minimal transitions (0.2s ease for color changes, 0.3s ease for drawer opens)
- The exact weight of ABC Simon Mono used for display text could not be confirmed; 400 (Regular) is assumed based on typical monospaced usage
- ABC Walter Neue weights are inferred; the site may use 400/500/600 variants that were not all present in extracted CSS
- Checkout flow colors (Shopify Pay buttons, Klarna badges) were filtered from the extraction and may introduce blue/green accents that are not part of the brand system
- The bone-white #fefff2 appears only in checkout context and may be a Shopify default rather than a brand color
- Social media icon colors and hover states are not captured — the footer currently has no social links
- Loading states (skeleton screens, spinners) are not defined in the extracted data
- The site may use a sticky "Add to Cart" bar on mobile PDP that was not captured in the component set
