---
version: alpha
name: "Evereden"
source_url: "https://evereden.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A calm, clinical warmth defines Evereden — a baby-care brand that trusts a near-all-white canvas (#ffffff) and a single, unexpected accent: a deep, almost-black ink (#1a1a1a) for headlines, with body text settling into a softer charcoal (#4a4a4a). There is no pastel pink or baby blue here; the palette reads more like a modern dermatologist’s office than a nursery. Primary CTAs and key interactive elements use a muted sage-green (#7a9e7e), a color that suggests botanical safety rather than urgency — it never screams. Buttons are softly pill-shaped ({rounded.full}) with generous internal padding, and product cards float on white backgrounds with barely-there hairlines (#e5e5e5) and {rounded.md} corners. Typography runs a clean, geometric sans-serif (closely resembling Neue Haas Grotesk or a similar neo-grotesk) at moderate weights: display heads at 500/600, body at 400, with tight line-heights and zero letter-spacing except for uppercase badges. The brand’s signature move is the “ingredient callout” — a small, uppercase badge (#7a9e7e background, white text) pinned to product imagery, signaling clean formulation without disrupting the visual. Navigation is a thin, transparent bar with a centered logo and minimal links, and the footer is a dense, organized grid of small text and social icons — more informational than aspirational. The overall effect is one of quiet authority: Evereden does not beg for attention; it assumes you’re already looking for the safest option.

colors:
  primary: "#7a9e7e"
  primary-active: "#5e8062"
  primary-disabled: "#c8d9ca"
  ink: "#1a1a1a"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-bg: "#7a9e7e"
  badge-text: "#ffffff"
  error: "#c13515"
  success: "#5e8062"
  link: "#7a9e7e"
  star-rating: "#1a1a1a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Neue Haas Grotesk Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Neue Haas Grotesk Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Neue Haas Grotesk Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-sage:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  product-card-photo:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  ingredient-callout:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-body:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0 {spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Subscribe," and key conversion points. Rendered as a pill-shaped button ({rounded.full}) with a sage-green background ({colors.primary}) and white text. On hover, the background deepens to {colors.primary-active}. The disabled state uses {colors.primary-disabled} with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details." Uses a white background with a 2px solid border in {colors.primary} and sage-green text. Hover state fills the background with {colors.primary} and inverts text to white. Disabled state uses {colors.primary-disabled} for both border and text.

**`button-tertiary-text`** — A text-only button for minimal interventions like "Cancel" or "Skip." No background or border, text in {colors.ink}. Hover adds a subtle underline. Used primarily in forms and modals.

**`button-pill-sage`** — A compact pill button for smaller UI contexts like filter strips or "Shop Now" badges on product cards. Uses {colors.primary} background, white text, and {typography.button-sm}. Height is 36px with 10px vertical padding.

### Navigation
**`top-nav`** — A transparent, fixed-position navigation bar at 72px height. The logo is centered, with minimal links (Shop, Learn, About) on either side. On scroll, the background transitions to {colors.canvas} with a subtle shadow. Active nav links have a 2px bottom border in {colors.primary}. Inactive links use {colors.muted}.

**`nav-link-active`** — The active state for top-level navigation items. Uses {colors.ink} text and a 2px solid bottom border in {colors.primary}. No background fill.

**`nav-link-inactive`** — The default state for navigation items. Uses {colors.muted} text. On hover, text transitions to {colors.ink} with a 1px bottom border in {colors.hairline}.

### Cards
**`product-card`** — The primary product display unit, used in grid layouts on collection pages and search results. A white card with a 1px {colors.hairline} border and {rounded.md} corners. The photo area occupies the top portion with a 1:1 aspect ratio and rounded top corners. Below the photo, a title, price, and optional ingredient badge are stacked with {spacing.sm} gaps. On hover, the card lifts with a subtle box-shadow and the border transitions to {colors.primary}.

**`product-card-photo`** — The image container within a product card. Uses {rounded.md} for top corners only, creating a seamless transition into the card body. Maintains a 1:1 aspect ratio. On hover, a subtle scale transform (1.02) is applied.

**`product-card-badge`** — A small rectangular badge pinned to the top-left corner of product imagery. Uses {colors.badge-bg} background, white text, and {typography.badge} with uppercase tracking. Content is typically "NEW" or "BESTSELLER."

### Forms & Inputs
**`text-input`** — Standard text input for forms (name, email, address). White background, 1px {colors.hairline} border, {rounded.sm} corners, and {typography.body-sm}. Focus state uses a 2px {colors.primary} border. Error state uses {colors.error} border with an error message below in {typography.caption}.

**`newsletter-input`** — A pill-shaped email input for the footer newsletter signup. White background, 1px {colors.hairline} border, {rounded.full} corners, and {typography.body-sm}. Paired with a {newsletter-submit} button that sits flush to the right.

**`newsletter-submit`** — The submit button for the newsletter form. Uses {colors.primary} background, white text, and {rounded.full} to match the input pill shape. Height matches the input at 48px.

### Footer
**`footer-section`** — The full-width footer area with a {colors.surface-soft} background. Contains a multi-column grid of links, a newsletter signup, and social icons. Links use {typography.caption} in {colors.muted}. The section has {spacing.section} vertical padding.

**`footer-link`** — Individual footer links in {colors.muted} with {typography.caption}. On hover, text transitions to {colors.ink}. No underline decoration.

### Accordion
**`accordion-header`** — Used on product detail pages for "Ingredients," "How to Use," and "Details" sections. A clickable header with {colors.ink} text, {typography.title-sm}, and a 1px {colors.hairline} bottom border. Includes a plus/minus icon that rotates on open. Padding is {spacing.lg} top and bottom.

**`accordion-body`** — The expandable content area below an accordion header. Uses {colors.body} text and {typography.body-sm}. Padding is {spacing.base} top and {spacing.lg} bottom. Content may include bullet lists, paragraphs, or ingredient callouts.

### Badges & Callouts
**`ingredient-callout`** — A small pill-shaped badge used on product detail pages to highlight key ingredients (e.g., "Shea Butter," "Vitamin E"). Uses {colors.badge-bg} background, white text, and {typography.badge} with uppercase tracking. Positioned inline near product descriptions or on imagery.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), hamburger menu replaces top nav, accordion-style footer, buttons go full-width, product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid (2 col), top nav collapses to logo + hamburger, footer becomes 2-column grid, buttons remain inline but smaller |
| Desktop | 1128–1440px | Three-column product grid (3 col), full top nav visible, footer 4-column grid, standard button sizes, product cards show hover states |
| Wide | > 1440px | Four-column product grid (4 col), max-width container at 1440px, top nav remains full, footer 4-column grid with increased padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons are 40px × 40px minimum.
- Accordion headers have 48px touch targets (including padding).
- Product card tap targets (title, price, badge) are at least 44px tall.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-out drawer. The drawer contains all nav links, search, and account links.
- The product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile).
- The footer collapses from 4 columns (desktop) → 2 columns (tablet) → stacked accordion (mobile).
- Accordion sections on product detail pages are collapsed by default on all breakpoints, with only the first section open on desktop.
- Image galleries on product pages collapse from a 2-column grid (desktop) to a single-column swipeable carousel (mobile/tablet).

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site; the palette above is inferred from the brand's general aesthetic and category conventions. The primary sage-green (#7a9e7e) is a best-guess based on the brand's botanical positioning — actual site colors may differ.
- No font-family declarations were found; the typeface stack uses "Neue Haas Grotesk" as a close approximation of the brand's likely neo-grotesk sans-serif. The actual font may be a custom or different typeface.
- Hover and focus states for all components are inferred from common DTC patterns rather than extracted from the live site.
- Error and success states for forms (input validation, submission feedback) are not confirmed from the live site.
- Dark mode is not supported and no dark-mode color tokens exist.
- Sub-brand or collection-specific palettes (e.g., "Evereden Baby," "Evereden Mama") are not documented.
- Animation durations, easing curves, and transition properties are not specified.
- The newsletter and accordion components are inferred from common e-commerce patterns; their exact implementation on the live site may vary.
- Social icon colors and specific footer link structures are not extracted.
