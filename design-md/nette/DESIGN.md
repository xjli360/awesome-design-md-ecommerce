---
version: alpha
name: "Nette"
source_url: "https://nettenyc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, sustainable fragrance house that lives in the electric tension between high-voltage chartreuse and deep, serious indigo. The brand’s signature move is a neon-lime green (#e5ff01) that feels like a lightning strike against a midnight-blue (#001da3) background — a pairing that reads as both eco-conscious and quietly luxurious. The palette is built on a warm off-white canvas (#fcfbf9) with soft surfaces (#f7f9fa) and a secondary blue (#0022bc) that adds depth to buttons and accents. The typography is a study in contrast: the geometric precision of Instrument Sans for body text, paired with the quirky, mono-spaced character of Lars Mono for display and labels — a nod to both Scandinavian minimalism and the brand’s technical, ingredient-forward ethos. Rounded corners are generous but not pillowy: cards and inputs use {rounded.sm} (8px) while buttons and badges lean into {rounded.md} (12px). The overall effect is a space that feels lab-clean but warmly human, where a lime-green CTA pulses against a navy field like a botanical extract under a microscope. The brand trusts color as its primary emotional signal — there is no heavy photography or illustration — relying instead on flat, saturated swatches and clean typographic hierarchy to convey its clean-beauty mission.

colors:
  primary: "#e5ff01"
  primary-active: "#cfe700"
  primary-disabled: "#f5ff9a"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#505050"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e7edf0"
  canvas: "#fcfbf9"
  surface-soft: "#f7f9fa"
  surface-card: "#ffffff"
  on-primary: "#001da3"
  accent-blue: "#001da3"
  accent-blue-active: "#0022bc"
  accent-blue-soft: "#e7ebff"
  accent-yellow: "#fed602"
  swatch-lime: "#e5ff01"
  swatch-navy: "#001a94"
  swatch-light-navy: "#061c81"
  swatch-mid-blue: "#99a5da"
  swatch-light-blue: "#b3bbe3"
  swatch-charcoal: "#1d1d1d"
  swatch-stone: "#c6c6c6"
  swatch-warm-white: "#f2f2f2"
  badge-new: "#e5ff01"
  badge-sale: "#fed602"
  star-rating: "#001da3"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Lars Mono', 'Source Code Pro', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
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
    rounded: "{rounded.md}"
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.md}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 28px
    height: 48px
    border: "2px solid {colors.accent-blue}"
  button-pill-lime:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.accent-blue}"
    borderBottom: "2px solid {colors.accent-blue}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-active:
    border: "1px solid {colors.accent-blue}"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  swatch-selector:
    rounded: "{rounded.full}"
    size: "32px"
    border: "2px solid transparent"
  swatch-selector-active:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: "40px"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"

## Components

### Buttons
**`button-primary`** — The brand’s main call-to-action, a high-voltage lime (#e5ff01) rectangle with navy (#001da3) text. On hover, it shifts to a slightly deeper lime (#cfe700); when disabled, it fades to a pale pastel lime (#f5ff9a). The 12px rounded corners and 48px height give it a solid, tactile feel without being aggressive. **`button-secondary`** — A deep navy (#001da3) button with white text, used for secondary actions like “Add to Cart” or “Learn More.” Active state darkens to #0022bc. **`button-tertiary`** — An outlined version with a transparent background and a 2px navy border, for less prominent actions. **`button-pill-lime`** — A fully pill-shaped variant of the primary button, used for badges, tags, or compact CTAs in tight spaces.

### Cards
**`product-card`** — A clean white card with 8px rounded corners and 16px padding, used to display fragrance products. The image area is a perfect square (1:1 aspect ratio) with matching 8px rounding. A small badge (lime for “New,” yellow for “Sale”) sits in the top-left corner. The card relies on the product’s own color swatch and typography for hierarchy — no drop shadows or heavy borders. **`accordion`** — A bordered card with 8px rounding, used for product descriptions and ingredient lists. Active state gets a navy border. The header uses the title-sm typography and toggles open to reveal body-sm content.

### Navigation
**`nav-bar`** — A 72px-tall white bar with uppercase mono-spaced links (Lars Mono, 14px, 0.5px letter-spacing). The active link is underlined with a 2px navy border. The bar is fixed at the top and collapses to a hamburger menu on mobile. **`search-bar`** — A pill-shaped input on a soft gray background (#f7f9fa), used for product search. It expands to full width on mobile.

### Forms
**`text-input`** — A standard input with a 1px light gray border (#d9d9d9) and 8px rounding. On focus, the border thickens to 2px and turns navy (#001da3). Error state uses a 2px lime border (#e5ff01) — a deliberate choice that signals attention without alarm. **`select-input`** — Matches the text-input styling for visual consistency. **`quantity-selector`** — A compact 40px-tall control with soft gray background, used in cart and product pages.

### Footer
**`footer`** — A dark charcoal (#212121) footer with white text and light gray (#999999) links. The section uses 64px vertical padding and 32px horizontal padding. Links are underlined on hover. The footer contains columns for customer service, about, and social links.

### Badges & Swatches
**`badge-new`** — A lime (#e5ff01) badge with navy text, used to flag new arrivals. **`badge-sale`** — A yellow (#fed602) badge with dark text, used for sale items. Both use 4px rounding and uppercase mono-spaced type at 10px. **`swatch-selector`** — A 32px circular color swatch for product variants (e.g., candle scents). Active state shows a 2px dark border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger; product cards stack vertically; hero section reduces padding to 32px; search-bar becomes full-width; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows all links but with reduced horizontal padding; hero uses 48px padding; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; standard padding and spacing; hero uses 64px padding |
| Wide | > 1440px | Max-width container at 1440px; content is centered; product grid can expand to four columns; hero uses 80px padding |

### Touch Targets
- All buttons and interactive elements are at least 48px tall (exceeding the 44px WCAG minimum).
- Icon buttons are 40x40px with 8px rounding.
- Swatch selectors are 32px circles, with at least 8px gap between them.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- The top nav collapses to a hamburger menu below 744px.
- The product grid collapses from 3 columns to 2 at tablet, and 1 at mobile.
- The footer collapses from 4 columns to 2 at tablet, and 1 at mobile.
- The hero section reduces its vertical padding by half on mobile.
- The search bar becomes a full-width input below 744px, replacing the inline pill.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) could not be reliably extracted from the static HTML/CSS analysis. The active states provided are best guesses based on color shifts.
- Error styling for form inputs (beyond the lime border) is inferred; actual error messages, icons, and validation patterns are unknown.
- Dark mode is not present on the live site; no dark-mode tokens are defined.
- Sub-brand or seasonal palettes (e.g., holiday, limited edition) are not captured.
- The exact font weights for Lars Mono and Instrument Sans are inferred from common web usage; the live site may use additional weights (e.g., 300, 700) that were not found.
- Animation and transition durations (e.g., button hover, accordion open/close) are not specified.
- The product card’s hover state (e.g., lift, shadow, border change) is unknown.
- The cart and checkout flow styling is partially inferred from the product page; full checkout design tokens are missing.
- The exact spacing between grid items and the grid gutter width are not explicitly defined in the extracted data.
