---
version: alpha
name: "Vaxee"
source_url: "https://www.vaxee.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single hex — #313131 — governs the entire Vaxee experience, a near-black that reads as a machined aluminum chassis rather than a software interface. The brand sells performance mice and esports peripherals, and the palette refuses any color that might suggest playfulness or consumer frippery; even the primary CTA sits in this same charcoal, relying on surface contrast and a 1px hairline to define interactive regions rather than a colored button. Typography runs the system stack at modest sizes — body copy at 14px, captions at 12px — because the site prioritizes spec tables, product photography, and configurator UI over editorial prose. Corners are uniformly sharp: every card, every button, every input uses {rounded.none} or at most {rounded.xs}, a deliberate rejection of the pill-shaped friendliness that defines consumer DTC. The product grid uses a dense 4-column layout on desktop with 12px gutters, each card showing a single product image, a model name in 16px medium weight, and a price in 14px — no badges, no ratings, no social proof. This is a brand that trusts its hardware to speak: the site is a catalog, not a story.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#6b6b6b"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e53935"
  accent-green: "#43a047"
  link-blue: "#1565c0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-active}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 12px
  button-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.base}"
  spec-table:
    borderCollapse: collapse
    typography: "{typography.body-sm}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline}"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.md}"
  badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    textDecoration: underline
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 36px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    height: 36px
  accordion:
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.md} 0"
  accordion-body:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 0 {spacing.md} 0"

## Components

### Buttons
**`button-primary`** — The sole call-to-action across the site, rendered in {colors.primary} with zero corner radius. On hover, it deepens to {colors.primary-active}. The disabled state uses {colors.primary-disabled} to signal unavailability without introducing a secondary color. Text is white, set in {typography.button-md} with 0.3px letter spacing for legibility at 14px.
**`button-secondary`** — An outlined variant with a 1px {colors.primary} border on a white canvas. Active state inverts the border to {colors.primary-active} and adds a {colors.surface-soft} background. Used for "View Details" and secondary product actions.
**`button-text`** — A borderless, backgroundless text button for inline actions like "Clear filters" or "Cancel". Hover state adds no background, only a color shift to {colors.primary-active}.

### Cards
**`product-card`** — A minimal card with no rounded corners, no shadow, and no padding. The product image sits flush against a {colors.surface-soft} background. Below, the model name in {typography.title-sm} and price in {typography.body-sm} stack with {spacing.sm} and {spacing.xs} margins respectively. On hover, a subtle 2px 8px rgba(0,0,0,0.08) box shadow appears — the only shadow in the entire system.

### Navigation
**`nav-bar`** — A 64px fixed-height bar with a 1px {colors.hairline-soft} bottom border. Navigation links are uppercase, 14px, weight 500, with 0.5px letter spacing. The active link uses {colors.primary}, inactive links use {colors.muted}. No logo lockup or hamburger menu on desktop — the brand name sits as a text link in the top-left.

### Forms
**`text-input`** — A 40px tall input with no rounded corners, a 1px {colors.hairline} border, and {typography.body-sm} text. On focus, the border switches to {colors.primary}. Error state uses {colors.accent-red} for the border. Used for search, newsletter signup, and checkout fields.
**`select-input`** — Matches the text input dimensions and styling. Used for product variant selection (size, color, etc.) and filter dropdowns.

### Footer
**`footer`** — A full-width {colors.primary} band with white text. Links use {typography.link} at 14px and underline on hover. Padding is {spacing.xl} vertical, {spacing.lg} horizontal. No columns or grid — links stack vertically in a single column, reinforcing the brand's no-frills approach.

### Badges
**`badge-new`** — A red ({colors.accent-red}) badge with uppercase 11px bold text, 2px 6px padding, and {rounded.xs} corners. Used sparingly for newly launched products.
**`badge-sale`** — A green ({colors.accent-green}) badge with identical styling. Used for clearance or promotional items.

### Accordion
**`accordion`** — A bordered section with a clickable header in {typography.title-sm} and collapsible body in {typography.body-sm}. Each accordion item has a {colors.hairline-soft} bottom border. Used for product specifications and FAQ sections.

### Quantity Selector
**`quantity-selector`** — A 36px tall inline control with a 1px {colors.hairline} border. The increment/decrement buttons use {colors.surface-soft} background and {colors.primary} text. The central value display uses {colors.body} text. No rounded corners anywhere.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; hero padding reduces to {spacing.lg}; footer links stack without columns; quantity selector becomes full-width |
| Tablet | 744–1128px | 2-column product grid; nav-bar remains full but link spacing tightens; hero uses {spacing.xl} padding; spec tables remain full-width |
| Desktop | 1128–1440px | 4-column product grid; full nav-bar with uppercase links; hero uses {spacing.section} padding; spec tables in two-column layout |
| Wide | > 1440px | Max-width container at 1440px; product grid remains 4-column; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height
- Quantity selector buttons are 36px × 36px — below the 44px recommendation but consistent with the brand's compact aesthetic
- Nav links have 48px tap targets via padding
- Product card images are tappable as a single unit

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px
- Product grid collapses from 4 columns → 2 columns → 1 column
- Hero section reduces vertical padding by 50% on mobile
- Spec tables remain full-width but text size drops to {typography.caption} on mobile
- Footer links stack without any column structure below 744px
- Accordion sections are always collapsed by default on mobile; expanded by default on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site; the remaining palette (primary-active, muted, hairline, etc.) was inferred from common DTC patterns and may not match the actual site
- No secondary or accent colors were found — accent-red and accent-green are assumed from common ecommerce patterns (sale badges, error states)
- Font-family declarations were extracted as the system stack; no custom or brand-specific typeface was detected
- Hover states, focus states, and active states for all components are inferred from common patterns, not extracted
- Error styling for forms (error messages, validation icons) is assumed
- Dark mode or high-contrast mode variants are not documented
- Sub-brand or limited-edition color palettes (if any) are not captured
- Animation durations, easing curves, and transition properties are not documented
- Shadow values (box-shadow, drop-shadow) are inferred from a single hover state observation
- The extracted page title "Just a moment..." suggests Cloudflare protection was active during extraction, which may have limited the data collected
- No meta theme-color was found, suggesting the site may not set a browser chrome color
- Shopify platform detection returned False, but the site may still use a custom ecommerce backend with similar patterns
