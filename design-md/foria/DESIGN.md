---
version: alpha
name: "Foria"
source_url: "https://foriawellness.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, intimate palette rooted in #222633 — a near-black ink that feels like the inside of a velvet box — sets Foria apart from the pastel-and-white conventions of sexual wellness. Against this darkness, #f388a1 (a warm, desaturated rose) and #9d4c1d (a burnt terracotta) emerge as the brand's emotional voltage: the rose for pleasure, the terracotta for grounding. The canvas is #fefefe, not pure white, giving body to a system where every surface card sits on {colors.surface-soft} (#dedede) and every hairline is {colors.hairline} (#aaaaaa). Typography runs on three weights of Basis Grotesque — bold for headlines, medium for navigation, regular for body — set at generous leading that mirrors the brand's unhurried, permission-giving voice. Buttons are pill-shaped ({rounded.full}), CTAs carry the rose voltage, and the entire experience feels like a private consultation rendered in type and space. The brand trusts negative space as much as it trusts its accent colors; product pages breathe with {spacing.section}-scale padding, and the checkout flow strips away every decorative element until only the essential remains: the product, the price, the path to purchase.

colors:
  primary: "#f388a1"
  primary-active: "#d96a85"
  primary-disabled: "#f3c4d0"
  ink: "#222633"
  body: "#1e2020"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#aaaaaa"
  hairline-soft: "#dedede"
  canvas: "#fefefe"
  surface-soft: "#dedede"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  accent-terracotta: "#9d4c1d"
  accent-purple: "#a45cec"
  accent-red: "#c70039"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'basis_grotesquebold', 'Basis Grotesque', -apple-system, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'basis_grotesquebold', 'Basis Grotesque', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'basis_grotesquebold', 'Basis Grotesque', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'basis_grotesqueregular', 'Basis Grotesque', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'basis_grotesqueregular', 'Basis Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'basis_grotesqueregular', 'Basis Grotesque', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'basis_grotesqueregular', 'Basis Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'basis_grotesquemedium', 'Basis Grotesque', sans-serif"
    fontSize: 11px
    fontWeight: 500
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
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
    padding: 14px 32px
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
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  button-pill-accent:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-price:
    typography: "{typography.button-md}"
    textColor: "{colors.ink}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-bestseller:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  rating-stars:
    color: "{colors.accent-terracotta}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand rose {colors.primary} with white text and a pill shape ({rounded.full}). On hover, it deepens to {colors.primary-active}. When disabled, it fades to {colors.primary-disabled} with the same pill silhouette, signaling unavailability without visual noise.

**`button-secondary`** — An outlined variant on a white canvas with {colors.ink} text and a 1px {colors.hairline} border. The active state swaps the border to {colors.ink} and fills the background with {colors.surface-soft}. Used for secondary actions like "Learn More" or "Add to Wishlist."

**`button-tertiary-text`** — A text-only button with no background or border. The default uses {colors.ink}; on hover it shifts to {colors.primary}. Reserved for low-emphasis actions such as "Cancel" or "Skip."

**`button-pill-accent`** — A smaller pill button using {colors.accent-terracotta} for high-emphasis promotional actions like "Shop the Sale" or "Get 20% Off." Typography is {typography.button-sm} with tighter padding.

### Cards
**`product-card`** — A white card ({colors.surface-card}) with {rounded.md} corners and {spacing.base} padding. The product image sits at the top with {rounded.sm}, followed by the title in {typography.title-md}, the price in {typography.button-md}, and optional badges. The card has no border; it relies on the contrast between {colors.canvas} and the page background.

**`product-card-image`** — The image container within a product card, using {rounded.sm} to soften the transition between visual and textual content. Aspect ratio is typically 1:1 or 4:5 depending on product photography.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a 1px {colors.hairline-soft} bottom border. Navigation links use {typography.nav-link} — uppercase, medium weight, 0.5px letter-spacing. The active link switches to {colors.primary}. The bar contains the brand logo on the left, primary links in the center, and utility icons (search, account, cart) on the right.

**`nav-link-active`** — The active state for navigation links, using {colors.primary} to indicate the current page or section.

### Forms
**`text-input`** — A standard input field with a white background, {colors.hairline} border, and {rounded.sm}. On focus, the border switches to {colors.ink}. On error, it switches to {colors.accent-red}. Height is 48px with 12px/16px padding for comfortable typing.

**`search-bar`** — A pill-shaped search input on a {colors.surface-soft} background with {colors.muted} placeholder text. On focus, it expands to a white background with an {colors.ink} border. Used in the nav and on search result pages.

### Badges
**`badge-new`** — A small pill badge in {colors.primary} with white text, used to flag newly launched products. Padding is 4px 10px with {typography.badge}.

**`badge-sale`** — A terracotta pill badge ({colors.accent-terracotta}) for sale or discount items. Same shape and typography as `badge-new`.

**`badge-bestseller`** — A purple pill badge ({colors.accent-purple}) for top-selling products. Same shape and typography as `badge-new`.

### Footer
**`footer-section`** — A dark footer with {colors.ink} background and white text. Links use {colors.muted-soft} and shift to {colors.primary} on hover. The section uses {spacing.section} for vertical padding and {spacing.lg} for horizontal.

**`footer-link`** — Footer links in {colors.muted-soft} with {typography.link}. On hover, they transition to {colors.primary}.

### Hero
**`hero-section`** — A full-width hero with a {colors.ink} background and white text. The headline uses {typography.display-xl} with generous padding. The CTA is a large pill button ({colors.primary}) with {typography.button-lg}.

**`hero-cta`** — The primary call-to-action within the hero, using {typography.button-lg} for larger tap targets. Padding is 16px 40px with {rounded.full}.

### Accordion
**`accordion-trigger`** — A full-width clickable row with {colors.ink} text in {typography.title-md} and a 1px {colors.hairline-soft} bottom border. Padding is {spacing.base} on top and bottom.

**`accordion-content`** — The expandable panel below the trigger, using {colors.body} text in {typography.body-md} with {spacing.base} padding.

### Quantity Selector
**`quantity-selector`** — A compact control with a white background, 1px {colors.hairline} border, and {rounded.sm}. Used on product detail pages for adjusting item count. Height is 40px with 8px/12px padding.

### Rating Stars
**`rating-stars`** — Star icons rendered in {colors.accent-terracotta} at 16px. Used on product cards and detail pages to display customer ratings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-lg}; buttons become full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses {typography.display-xl} at 32px; side-by-side accordion sections |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full typography scale; multi-column footer |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero background extends full-width while content stays constrained |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Product card tap targets are the full card area, not just the title or price.
- Accordion triggers are full-width with 48px minimum height.
- Quantity selector buttons are 40px × 40px minimum.

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px.
- Product grid collapses from 3 columns to 2 at 1128px, then to 1 at 744px.
- Footer links collapse from multi-column to single-column stack below 744px.
- Hero content stacks vertically (image above text) below 744px.
- Accordion sections remain single-column on mobile; on tablet and above, they can display side-by-side in a two-column layout.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; exact transition durations and easing curves were not extracted.
- Error styling (input validation, form submission errors) beyond the `text-input-error` border color was not observed.
- Dark mode is not present on the live site; all colors assume a light theme.
- Sub-brand or collection-specific color palettes (e.g., limited edition drops) were not extracted.
- The exact font sizes and line heights for Basis Grotesque are estimated based on common usage; the live site may use slightly different values.
- Spacing tokens are inferred from common grid patterns; the exact spacing scale used in the Shopify theme may vary.
- The `accent-purple` (#a45cec) and `accent-red` (#c70039) appear in the extracted colors but their specific usage (badges, links, icons) is inferred.
- Checkout-specific components (Shopify Pay button, Klarna, Afterpay) were not analyzed; their colors are excluded from the palette.
- The `scrim` color (#121212) is assumed for overlay backgrounds; its opacity was not extracted.
