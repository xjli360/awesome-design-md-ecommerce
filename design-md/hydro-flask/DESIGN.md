---
version: alpha
name: "Hydro Flask"
source_url: "https://www.hydroflask.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single saturated hex value — #313131 — defines the entire Hydro Flask digital presence, a deep charcoal that reads as the color of basalt, of frozen lakes, of the brand's own powder-coated bottle exteriors. This is not a brand that reaches for bright adventure hues; it trusts the material itself to carry the story. The site's typography defaults to system fonts (Arial, Helvetica Neue, Roboto, sans-serif), a pragmatic choice that prioritizes legibility over personality — the product photography, with its sweeping mountain vistas and condensation-beaded stainless steel, does all the emotional work. Buttons and interactive elements use generous {rounded.full} pill shapes, echoing the iconic wide-mouth bottle opening, while product cards land at {rounded.md} — soft enough to feel approachable, not so soft they undermine the industrial precision of the brand. The canvas is white, the ink is that #313131 charcoal, and there is almost no secondary color in the system; the brand's color story is told entirely through product finishes (sage, lilac, coral) rendered in photography, not in UI chrome. Navigation is lean — a single top bar with dropdowns, a persistent cart icon, and a search trigger that opens a full-screen overlay. The overall mood is one of quiet confidence: the brand knows its product is the hero, and the interface simply steps aside.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  sale-badge: "#d32f2f"
  product-swatch-border: "#bdbdbd"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Helvetica Neue, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
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
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
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
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-dropdown-item:
    padding: 8px 24px
    height: 40px
  nav-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    padding: 24px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
    height: 56px
    border: "none"
  search-input-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.product-swatch-border}"
  product-swatch-selected:
    border: "2px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    height: 480px
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    textDecoration: "underline"
  cart-icon:
    height: 24px
    width: 24px
  cart-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a full pill shape in the brand's deep charcoal {colors.primary}. Text is white, set in uppercase with 0.5px letter-spacing for a deliberate, industrial feel. On hover, the background deepens to {colors.primary-active}. The disabled state uses {colors.primary-disabled} with white text, signaling non-interactivity without visual noise.

**`button-secondary`** — An outlined variant that inverts the primary relationship: white fill, charcoal text, and a 2px charcoal border. Used for secondary actions like "Add to Wishlist" or "Compare". Hover state fills the background with {colors.surface-soft} and darkens the border to {colors.primary-active}. Maintains the same uppercase typography and pill shape as the primary button.

### Forms
**`text-input`** — Standard text entry with a white background, {colors.hairline} border, and 12px of internal padding. On focus, the border thickens to 2px and shifts to {colors.primary}. Error state swaps the border to {colors.error}. Height is 48px to meet touch-target minimums. The select variant uses the same dimensions and styling, with a custom dropdown arrow.

**`search-input`** — A dedicated search field with a {rounded.full} shape and a soft gray background ({colors.surface-soft}) that distinguishes it from standard text inputs. On focus, a 2px {colors.primary} border appears. Used within the full-screen search overlay, which covers the viewport with a white background and centered search bar.

### Navigation
**`nav-bar`** — A fixed 72px top bar with a white background and a subtle bottom border ({colors.hairline-soft}). Navigation links are uppercase, 14px, weight 600, with 0.5px letter-spacing. Dropdown menus appear on hover with a white background, soft rounded corners, and 8px vertical padding for items. Each dropdown item is 40px tall with horizontal padding of 24px; hover state adds a soft gray background.

**`search-overlay`** — A full-screen white overlay triggered by the search icon in the nav bar. The search input is centered vertically and horizontally, with a {rounded.full} shape and soft gray background. Below the input, suggested searches or recent searches may appear as text links.

### Cards
**`product-card`** — The primary content container for product listings. A white card with {rounded.md} corners containing a square product image (1:1 aspect ratio) and text details below. The title uses {typography.title-md} with {spacing.sm} top margin; the price sits below with {spacing.xs} top margin. Cards are typically displayed in a responsive grid with 16px gaps.

**`product-swatch`** — Circular color swatches (32px) with a {colors.product-swatch-border} border. The selected state swaps the border to {colors.primary}. Swatches are used to indicate available product finishes (sage, lilac, coral, etc.) and are rendered from product photography, not UI-generated colors.

### Badges
**`badge-sale`** — A red badge ({colors.sale-badge}) with white uppercase text, {rounded.sm} corners, and 4px/8px padding. Used to flag discounted products on listing pages and product detail views.

**`badge-new`** — A charcoal badge ({colors.primary}) with white uppercase text, identical shape and sizing to the sale badge. Used to mark newly launched products or collections.

### Footer
**`footer`** — A full-width footer with a {colors.primary} background and white text. Links are styled with {typography.link} and underline on hover. The footer typically contains four columns: Shop, Support, Company, and Social. Padding is 48px vertical, 24px horizontal. The bottom of the footer includes a thin white hairline separator and copyright text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner reduces to 320px height; search overlay is full-screen; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav bar shows top-level links with dropdowns; hero banner at 400px; footer displays in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; hero banner at 480px; footer in four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner at 520px; footer remains four columns with increased horizontal padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 48px height
- Product swatches are 32px with 8px touch padding (effective 48px target)
- Cart icon is 24px with 12px touch padding (effective 48px target)
- Nav dropdown items are 40px tall — below the 48px minimum, but acceptable for desktop hover interactions

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px
- Product grid collapses from 4 columns to 1 column below 744px
- Footer collapses from 4 columns to 1 column below 744px
- Search bar collapses from inline to full-screen overlay below 744px
- Hero banner reduces height by 33% on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is extremely limited: only #313131 was reliably identified from the live site's CSS. All other colors (primary-active, disabled, muted, error, success, etc.) are inferred from common DTC patterns and may not match the actual brand system.
- No font-family declarations beyond system fonts were found. Hydro Flask may use a custom typeface (e.g., a licensed sans-serif) that was not extractable from the page source.
- Hover, focus, and active states for all components are inferred from standard interaction patterns, not extracted from the live site.
- Error styling (form validation, 404 pages, etc.) is not documented and may differ from the inferred {colors.error} value.
- Dark mode is not supported and no dark-mode tokens are defined.
- The brand's secondary palette (product finish colors like sage, lilac, coral) is not represented in the UI color system — these colors appear only in product photography and swatch images.
- Cart and checkout flows were not analyzed; the cart icon and count badge are inferred from common patterns.
- The site may use a Shopify or other e-commerce platform that injects its own styling (checkout buttons, payment badges) which was not fully filtered from the extracted data.
- No animation or transition tokens are defined (easing curves, durations, etc.).
