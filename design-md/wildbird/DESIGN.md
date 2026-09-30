---
version: alpha
name: "Wildbird"
source_url: "https://wildbird.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baby carrier brand built on a palette of muted earth and stone — #676986 (a quiet slate), #d6aa62 (a warm, desaturated gold), and #272d45 (a deep ink) — that feels more like a ceramic studio than a baby-gear store. The brand’s signature move is the absence of primary-color baby tropes: no bright blues, pinks, or yellows dominate. Instead, a soft canvas of #f4f4f6 and #f7f7f8 carries product photography, while #d6aa62 acts as the single accent voltage — used sparingly on buttons, badges, and the occasional underline. Typography runs on Quarto A/B for display (a refined serif that suggests heirloom quality) and Inter for body (clean, legible, modern). Carriers are photographed on real parents in real homes, not studio sets, and the UI mirrors that: generous whitespace, soft rounded corners at {rounded.lg} on product cards, and a persistent top nav with a thin hairline of #dbdde4. The checkout flow introduces a secondary accent of #00caaa (a minty teal) that feels like a surprise — it appears on the cart icon and progress indicators, hinting at a sustainability or organic-cotton subtext. The overall effect is restrained, warm, and materially honest: a brand that trusts its product photography and its customers’ desire for simplicity over decoration.

colors:
  primary: "#d6aa62"
  primary-active: "#a86629"
  primary-disabled: "#e5e5eb"
  ink: "#272d45"
  body: "#454142"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#00caaa"
  accent-red: "#ff5742"
  accent-sage: "#718472"
  accent-teal-dark: "#0e7a82"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Quarto A', 'Quarto B', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Quarto A', 'Quarto B', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Quarto A', 'Quarto B', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-teal-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
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
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    padding: "{spacing.sm} 0 {spacing.base}"
    typography: "{typography.body-md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  cart-icon:
    color: "{colors.accent-teal}"
    height: 24px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.accent-teal}"
    height: 4px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s warm gold {colors.primary} with white text and uppercase Inter at 14px. Used for “Add to Cart,” “Checkout,” and primary form submissions. On hover, shifts to the deeper {colors.primary-active} (#a86629). Disabled state uses {colors.primary-disabled} with muted text.

**`button-secondary`** — A ghost-style button on the {colors.canvas} background with a thin {colors.hairline} border. Used for “Learn More” and secondary navigation actions. Hover state darkens the border to {colors.ink}. Text remains uppercase Inter.

**`button-tertiary-text`** — A text-only button with no background or border, used for “Cancel,” “View All,” or inline links that need button semantics. Inherits {colors.ink} and underlines on hover.

**`button-teal-accent`** — A secondary accent button using the minty {colors.accent-teal} (#00caaa). Appears in cart-related flows (e.g., “Continue Shopping” or promotional banners) and on sustainability badges. Text is dark {colors.ink} for contrast.

### Cards
**`product-card`** — A white card with soft {rounded.lg} corners and no border, relying on shadow (not yet extracted) for elevation. The image fills the top with matching corner radius, followed by the title in {typography.title-sm} and price in {typography.body-sm} in {colors.muted}. Used on collection pages and the home page.

**`badge-new`** — A pill-shaped badge in {colors.accent-teal} with uppercase 11px Inter. Signals new arrivals or limited drops. Positioned at the top-left of product-card images.

**`badge-sale`** — Same shape as badge-new but in {colors.accent-red} (#ff5742) with white text. Used for markdowns or clearance items.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 72px height on {colors.canvas} with a soft bottom border of {colors.hairline-soft}. Logo sits left, nav links center or right, cart icon (in {colors.accent-teal}) rightmost. Active page is indicated by a 2px underline in {colors.primary}.

**`nav-link-active`** — The active nav state: no background, but a 2px bottom border in {colors.primary} directly under the text. Inactive links use {colors.muted} text color.

### Forms
**`text-input`** — Standard input field on {colors.canvas} with a 1px {colors.hairline} border and {rounded.sm}. On focus, the border thickens to 2px and turns {colors.primary}. Height is 48px with 12px/16px padding. Used for email, search, and address fields.

**`quantity-selector`** — A compact inline control with minus/plus buttons flanking a numeric display. Bordered in {colors.hairline}, {rounded.sm}, 44px height. Used on product detail pages.

### Footer
**`footer-section`** — A dark footer on {colors.ink} (#272d45) with white text. Links are in {colors.muted-soft} (#9a9db1) and use {typography.link}. Padding is {spacing.xxl} horizontally and vertically. Contains columns for “Shop,” “Learn,” “Support,” and social links.

### Accordion
**`accordion-trigger`** — A full-width clickable row with {typography.title-sm} and a thin bottom border. Used on product detail pages for “Details,” “Care Instructions,” and “Shipping & Returns.” The content area uses {typography.body-md} with 8px top / 16px bottom padding.

### Cart
**`cart-icon`** — A shopping bag icon rendered in {colors.accent-teal} at 24px height. Sits in the top nav. A small badge (not yet extracted) may show item count.

**`progress-bar`** — A thin 4px bar used in the cart to show free-shipping thresholds. The track is {colors.hairline-soft}, the fill is {colors.accent-teal}, with {rounded.full} ends.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to {typography.display-lg}; footer stacks vertically; accordions always open? |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses {typography.display-xl}; footer in two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero full-width with image; footer in four columns |
| Wide | > 1440px | Max-width container (likely 1440px) centered; product grid may expand to four columns; hero may have parallax or full-bleed image |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons, inputs, quantity selector)
- Nav links at 72px tap area (full nav-bar height)
- Accordion triggers full-width with 44px+ tap height
- Cart icon minimum 44x44px tap area (icon is 24px, padded within nav-bar)

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at tablet, 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, 1 at mobile
- Hero section reduces font size and may stack image below text on mobile
- Accordion content may default to closed on mobile to save vertical space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, text inputs, and nav links are inferred but not extracted from live CSS
- Error states (red border, error message styling) not observed — likely use {colors.accent-red} but unconfirmed
- Focus ring styles (outline, box-shadow) not extracted
- Shadow/elevation tokens (box-shadow values for cards, modals, dropdowns) not present in extracted data
- Dark mode or high-contrast mode not implemented on live site
- Sub-brand or collection-specific palettes (e.g., “Aerial” vs “Ring Sling” lines) may exist but not extracted
- Typography weights beyond 400/500/600 not confirmed (Quarto may have italic or bold variants not seen)
- Spacing for specific components (e.g., product-card padding, footer link spacing) inferred from common patterns
- Checkout flow colors (#00caaa, #ff5742) appear but their exact usage context (progress bar, promo badges) is best-guess
- Social icon colors (Instagram, Facebook, etc.) not extracted
- Mobile nav hamburger icon and overlay styling not observed
- Loading states (spinner, skeleton) not present in extracted data
