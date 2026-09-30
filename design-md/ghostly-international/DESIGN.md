---
version: alpha
name: "Ghostly International"
source_url: "https://www.ghostly.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record label and shop where a ghostly lavender #ccccff sits as the quiet, spectral backdrop across product pages and collection grids, while a neon violet #912eff and cyan #51feff serve as the brand's primary voltage — the violet driving add-to-cart buttons and the cyan illuminating sale badges and limited-run alerts. Type is set in Lars FS GI Light, a geometric sans-serif with unusually light optical weight that feels airy and slightly detached, as if the letters are floating above the page rather than pressing into it. The shop runs on Shopify, and the checkout experience defaults to a clean white canvas #ffffff with #f7f7f7 surface cards and #e4e4e4 hairline borders — but the brand's true personality lives in the accent palette: a lime green #00ff00 for sold-out indicators, a highlighter yellow #ffff00 for pre-order badges, and a deep purple #912eff that appears nowhere in nature but everywhere in Ghostly's visual identity. The result is a digital storefront that feels more like an experimental gallery than a merch shop — generous whitespace, thin type, and neon accents that pulse against the lavender haze.

colors:
  primary: "#912eff"
  primary-active: "#7a1fcc"
  primary-disabled: "#c9a3ff"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e4e4e4"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-lavender: "#ccccff"
  on-primary: "#ffffff"
  accent-cyan: "#51feff"
  accent-lime: "#00ff00"
  accent-yellow: "#ffff00"
  accent-violet: "#912eff"
  accent-blue: "#5497ff"
  accent-gray: "#aaaaaa"
  accent-gray-light: "#cfcfcf"

typography:
  display-xl:
    fontFamily: "'Lars FS GI Light Extended', 'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lars FS GI Light Extended', 'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Lars FS GI Mono', monospace, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Lars FS GI Mono', monospace, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lars FS GI Light', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase

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
    padding: 12px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
  button-accent-cyan-active:
    backgroundColor: "#3dd4d4"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
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
    border: "1px solid {colors.accent-lime}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-lavender}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  badge-sold-out:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-pre-order:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-limited:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 32px
    marginTop: "{spacing.lg}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, rendered in the brand's signature violet #912eff with white uppercase type. Hover shifts to a deeper purple #7a1fcc. Disabled state uses a washed-out lavender #c9a3ff. All buttons use zero border-radius — the brand rejects pill shapes and rounded corners in favor of sharp, deliberate rectangles that match the geometric precision of the Lars typeface.

**`button-secondary`** — An outlined variant with a white background, black text, and a single hairline border. On hover, the border thickens to black and the background shifts to the soft surface tone #f7f7f7. Used for "View Collection" links and secondary checkout actions.

**`button-ghost`** — A text-only button with no background or border. Hover reveals a soft gray background #f7f7f7. Used for "Cancel" actions, filter resets, and dismissible banners.

**`button-accent-cyan`** — A high-voltage cyan #51feff button reserved for limited-time offers, flash sales, and exclusive drops. The cyan sits on the same zero-radius rectangle as the primary button but communicates urgency through its electric, almost-neon quality. Hover darkens to #3dd4d4.

### Badges
**`badge-sold-out`** — A lime green #00ff00 badge that appears in the top-left corner of product card images. The green is intentionally jarring against the lavender and white backgrounds — it's meant to signal finality and scarcity simultaneously. Uses the monospaced variant of Lars for a technical, inventory-system feel.

**`badge-pre-order`** — Highlighter yellow #ffff00 badge for upcoming releases. The yellow is the brightest element on any page and draws the eye before any other content. Positioned identically to the sold-out badge for visual consistency.

**`badge-limited`** — Cyan #51feff badge for limited edition pressings, signed copies, or artist-exclusive merchandise. The cyan sits between the violet primary and the lime sold-out in the brand's accent hierarchy — urgent but not final.

**`badge-new`** — Violet #912eff badge on white text for newly added items. Uses the primary brand color to signal official newness rather than scarcity.

### Cards
**`product-card`** — A minimal, borderless card with a full-bleed product image and text below. No rounded corners anywhere — the card is a strict rectangle. On hover, the entire card background shifts to the lavender #ccccff, creating a ghostly glow effect that gives the brand its name. The image remains unchanged while the text area subtly illuminates.

**`product-card-title`** — The album or merchandise title set in Lars FS GI Light at 16px with normal weight. No truncation — titles wrap naturally. Margin-top of 8px from the image.

**`product-card-price`** — The price in muted gray #666666 at 14px light weight. Sits 2px below the title. No currency symbol prefix on the Ghostly store — just the number.

### Navigation
**`nav-bar`** — A fixed 64px header with white background and uppercase navigation links in Lars FS GI Light at 14px. The nav includes "Music," "Merch," "Artists," "News," and a search icon. On scroll, a subtle bottom border appears at #f0f0f0. The Ghostly logo sits left-aligned in the brand's signature lavender when active.

**`nav-bar-sticky`** — The scrolled state adds a 1px hairline-soft border at the bottom to create visual separation from page content. The background remains white — no blur or transparency effects.

### Forms
**`text-input`** — A rectangular input field with a 1px hairline border #e4e4e4 and 16px padding. Focus state swaps the border to violet #912eff. Error state uses lime green #00ff00 border — an unusual choice that pairs the error signal with the brand's sold-out color rather than traditional red.

**`search-bar`** — A soft gray #f7f7f7 input field with no border in its default state. On focus, the background turns white and a 1px violet border appears. The search icon sits left-aligned within the field.

### Footer
**`footer`** — A full-width section with soft gray background #f7f7f7 and muted text #666666. Links are set in the same Lars FS GI Light at 14px and turn violet on hover. The footer includes newsletter signup, social links, and legal text — all in the brand's restrained, airy typography.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger menu, hero section reduces to 32px padding, badges stack vertically on cards, footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav links remain visible but "Artists" and "News" collapse into a "More" dropdown, hero uses 48px padding, search bar moves to a toggle icon |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full nav visible, hero at 64px section padding, search bar fully expanded in nav |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px centered, hero content max-width at 1200px, product cards maintain 1:1 aspect ratio on images |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product cards have full-surface tap targets (no separate "Add to Cart" button — tapping the card navigates to the product page)
- Nav links have 48px minimum tap area on mobile
- Quantity selectors in cart use 44px × 44px plus/minus buttons
- Badges are minimum 20px height with 8px internal padding

### Collapsing Strategy
- On mobile, the full navigation collapses to a hamburger menu with a slide-in drawer from the left
- The search bar collapses to a magnifying glass icon; tapping expands a full-width search overlay
- Product filters collapse to a "Filter" button that opens a bottom sheet
- The footer newsletter signup collapses to a single-line input with inline submit button
- Collection headers reduce from display-md (28px) to display-sm (24px) on mobile
- Product card images switch from landscape to square aspect ratio on mobile to maintain visual consistency in single-column view

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex color list includes #b3d4fc (likely a Shopify or browser default focus ring) and #aaaaaa (a generic gray) — these have been excluded from the brand palette as they are not distinctive to Ghostly International
- Hover states for product card images (zoom, overlay, or color shift) could not be reliably extracted from the static HTML/CSS analysis
- The exact font weights for Lars FS GI Light and Lars FS GI Light Extended are inferred from typical usage (300 for body, 400 for titles) — the actual weight values on the live site may vary slightly
- Error message styling for form validation (color, position, animation) was not visible in the extracted data
- Dark mode is not present on the live site and has not been designed
- The checkout flow uses Shopify's default styling with the brand's primary color applied to the payment button — exact checkout component tokens (shipping form, payment selection, order summary) are Shopify defaults
- Mobile navigation drawer animation timing and easing curves could not be extracted
- The brand's email signup modal or popup behavior (if any) was not captured in the extraction
- Sub-brand or collection-specific color variations (e.g., artist-specific landing pages) may exist but are not represented in the global palette
- The "Lars FS GI Mono" font is referenced in badge typography but its exact weight (likely 400) and letter-spacing values are inferred from monospace conventions rather than extracted CSS
