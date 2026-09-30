---
version: alpha
name: "Alo Yoga"
source_url: "https://www.aloyoga.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage wellness brand that uses a neon-lime green (#dbf482) as its primary signal — a color so electric it feels like a match struck against the muted charcoal (#232933) and deep ink (#121212) of its canvas. This is not the soft, muted palette of traditional yoga brands; it's a studio-to-street system built on contrast: the lime appears on CTAs, sale badges, and product highlights, while the body grid stays clean on white (#ffffff) with soft pink (#f9cae6) and sage (#758e6d) accents for seasonal collections. Typography runs a two-family system — arquitecta for display headers (bold, condensed, architectural) and proxima-nova for body (clean, neutral, highly readable at small sizes). The brand uses generous whitespace and full-bleed hero imagery, with product cards that float on white with subtle shadows. Every button is a pill (`{rounded.full}`), every input has a soft corner (`{rounded.md}`), and the checkout flow uses teal (#00aba9) as a secondary accent for trust signals. The overall effect is athletic but luxurious — a gym that looks like a gallery, with the lime acting as the single voltage that says "click here."

colors:
  primary: "#dbf482"
  primary-active: "#c2e06a"
  primary-disabled: "#eaf5c4"
  ink: "#121212"
  body: "#232933"
  muted: "#758e6d"
  muted-soft: "#9baa94"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  accent-pink: "#f9cae6"
  accent-teal: "#00aba9"
  accent-sage: "#758e6d"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'arquitecta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'arquitecta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'arquitecta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'arquitecta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-lime:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px {spacing.base}"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid #e74c3c"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "3:4"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0 0 0"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} 0 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px {spacing.sm}"
    position: "top-left"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 500px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
    letterSpacing: 1px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    height: 44px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    height: 44px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  checkout-button:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, always filled with the neon-lime (#dbf482) and set in uppercase proxima-nova at 14px/600. The pill shape (`{rounded.full}`) gives it a sporty, approachable feel. On hover, the lime shifts to a slightly deeper green (`{colors.primary-active}`). Disabled state uses a washed-out lime (`{colors.primary-disabled}`) with muted text — never fully invisible, but clearly inactive.

**`button-secondary`** — An outlined variant for secondary actions, using a white fill with a thin hairline border. Hover darkens the border to ink and optionally fills with a soft gray surface. Used for "Add to Bag" on product pages and "View All" links in collection grids.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel," "Clear Filters," or "Learn More" links. Relies on the uppercase button typography and hover underline for affordance.

**`button-pill-lime`** — A compact pill used for sale badges, promo tags, and quick-add actions on product cards. Same lime fill but smaller padding and font size — designed to sit inside tight grid cells.

**`button-pill-outline`** — A compact outlined pill for "New," "Best Seller," or "Limited Edition" badges. Transparent background with a hairline border, used to denote status without competing with the product image.

### Navigation
**`top-nav`** — A fixed 72px white bar with a thin bottom border. Contains the logo (left), nav links (center), and utility icons (search, account, cart — right). Nav links are uppercase proxima-nova at 13px/600 with 1px letter-spacing, giving the brand a clean, editorial feel. Active state has a 2px ink underline.

**`nav-link`** — Individual navigation items with generous horizontal padding. Hover adds a subtle underline or opacity shift. The active page gets an ink underline to anchor the user.

**`search-bar`** — A pill-shaped input with a soft gray fill and hairline border, placed in the top nav or as a full-width hero element. On focus, the fill turns white and the border switches to ink. Placeholder text is body color.

### Cards
**`product-card`** — A minimal, borderless card with a 3:4 aspect ratio image and text below. No rounded corners — the brand trusts the image to do the work. The title sits in title-sm (16px/600), price in body-sm (14px/400). A lime badge (`{product-card-badge}`) can overlay the top-left corner for sale items.

**`product-card-badge`** — A small lime pill pinned to the top-left of the product image. Uses badge typography (11px/700, uppercase) with tight padding. Only appears on sale or "New" items.

### Forms
**`text-input`** — A standard input with 12px rounded corners, white fill, and a hairline border. Focus shifts the border to ink. Error state uses a red border (#e74c3c) — the only place red appears in the system.

**`size-selector`** — A pill-shaped button group for size selection (XS–XL). Inactive items have a white fill with hairline border. Active items invert to ink fill with white text. Hover adds a subtle shadow or border darkening.

**`quantity-selector`** — A compact horizontal control with minus, number, and plus buttons. Uses a hairline border and body typography. Used in cart and product detail pages.

### Footer
**`footer`** — A full-width dark section with ink background and white text. Links are muted-soft (#9baa94) on hover turning white. Headings are uppercase with 1px letter-spacing. The footer uses a multi-column layout with accordions on mobile.

### Accordion
**`accordion`** — A border-bottom-only container for FAQ and product details. The header is title-sm with no background, and clicking toggles the content panel. Content uses body-sm with reduced opacity for readability. No icons — the brand uses plus/minus or chevron rotation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, hamburger nav, accordion footer, product cards stack 2-per-row, hero reduces to 300px min-height |
| Tablet | 744–1128px | Two-column product grid, expanded nav links (no hamburger), footer splits into 2-column layout, hero at 400px |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, footer in 4-column layout, hero at 500px |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid can go 4-column, hero at 600px with full-bleed imagery |

### Touch Targets
- All buttons and interactive elements: minimum 44px height, 48px preferred
- Icon buttons: 40px x 40px minimum
- Nav links: 44px tap area (padding ensures this even if text is smaller)
- Size selectors: 44px height minimum
- Quantity selector buttons: 44px x 44px tap targets

### Collapsing Strategy
- Top nav: nav links collapse into hamburger menu below 744px; search icon remains visible, cart icon remains visible
- Product grid: 4-column on wide → 3-column on desktop → 2-column on tablet → 2-column on mobile (with smaller cards)
- Footer: 4-column on desktop → 2-column on tablet → accordion on mobile
- Hero: full-bleed on all sizes, but text overlay stacks vertically on mobile (image behind, text below on narrow screens)
- Product filters: sidebar on desktop → horizontal strip on tablet → bottom sheet or modal on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary and secondary button hover colors were extracted. Hover for links, icons, and product cards is inferred from common patterns — actual values may differ.
- **Error styling**: The error border color (#e74c3c) is a standard web default, not confirmed from the live site. Error text color and iconography are unknown.
- **Dark mode**: No evidence of a dark mode implementation. The brand uses a white canvas with ink text — dark mode would require full inversion.
- **Sub-brand palettes**: Alo Yoga has sub-lines (Alo Moves, Alo Accessories, etc.) that may use different accent colors. Only the main brand palette is captured here.
- **Animation tokens**: No timing, easing, or transition values were extracted. The brand likely uses subtle fades and slides, but exact values are unknown.
- **Font weights**: arquitecta weights are assumed 600/700 based on display usage; proxima-nova weights are standard 400/600. Actual weight availability may vary.
- **Checkout colors**: The teal (#00aba9) appears in checkout flows but may be a Shopify default rather than a brand choice. It's included as an accent but should be verified.
- **Spacing scale**: The spacing tokens are based on common 8px/4px systems. Actual padding/margin values on the live site may use a different scale (e.g., 10px, 20px, 40px).
- **Rounded corners**: Product cards appear to use `{rounded.none}` based on extracted CSS, but some may use subtle rounding on hover or in specific contexts.
- **Iconography**: No icon set or stroke weights were extracted. The brand likely uses custom line icons, but exact specifications are unavailable.
