---
version: alpha
name: "Flicker Alley"
source_url: "https://www.flickeralley.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, archival canvas of #121212 — near-black, not pure black — that frames film history as a physical object to be held, studied, and admired. The brand’s primary voltage is #334fb4, a restrained indigo-blue that appears in navigation accents, product badges, and the occasional editorial underline; it never screams, it signals authority. Body text runs #dedede on the dark canvas, a warm silver rather than clinical white, while #f3f3f3 lifts headlines and price tags into legibility. The secondary surface #242833 sits between the deep background and the card foreground, creating a three-dimensional hierarchy without relying on hard shadows — think of a film archive’s storage boxes stacked in climate-controlled rows. Lato, set at moderate weights and generous line heights, carries the typographic load with a quiet professionalism that matches the brand’s mission: bringing film history to new audiences. Buttons are pill-shaped at {rounded.full}, but product cards and modals use {rounded.sm} — a deliberate restraint that keeps the interface from feeling toy-like. The search bar, a critical entry point for a catalog of obscure and restored titles, sits as a prominent {rounded.full} field on the dark canvas, inviting discovery. Every design decision — from the near-black backdrop to the indigo accent — treats the screen as a projection surface, not a storefront.

colors:
  primary: "#334fb4"
  primary-active: "#253a8a"
  primary-disabled: "#5a72c4"
  ink: "#f3f3f3"
  body: "#dedede"
  muted: "#a0a0a0"
  muted-soft: "#6a6a6a"
  hairline: "#3a3a3a"
  hairline-soft: "#2a2a2a"
  canvas: "#121212"
  surface-soft: "#242833"
  surface-card: "#1e1e1e"
  on-primary: "#ffffff"
  accent-gold: "#c9a84c"
  badge-new: "#334fb4"
  badge-restored: "#c9a84c"
  star-rating: "#c9a84c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: 1px solid "{colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: 1px solid "#e74c3c"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    border: 1px solid "{colors.primary}"
    rounded: "{rounded.full}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-details:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.accent-gold}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-restored:
    backgroundColor: "{colors.badge-restored}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: 1px solid "{colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  filter-dropdown:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: 1px solid "{colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderBottom: 1px solid "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-order", and "Subscribe". Rendered as a pill with {rounded.full} on the deep {colors.canvas} background, it uses {colors.primary} indigo fill with white text. On hover, it shifts to {colors.primary-active} for a darker, more grounded state. When disabled, it fades to {colors.primary-disabled} to signal unavailability without disappearing into the dark background.

**`button-secondary`** — Used for secondary actions like "View Details" or "Learn More". It sits on {colors.surface-soft} with {colors.ink} text, creating a subtle layered effect against the canvas. Active state uses {colors.hairline} as the background, deepening the layer without introducing a new color.

**`button-tertiary`** — A text-only button with {colors.primary} text on a transparent background, used for inline actions like "Clear Filters" or "Cancel". Maintains the same padding and height as other buttons for alignment in form layouts.

**`button-pill-gold`** — A special accent button reserved for premium content, limited editions, and "Restored" collections. Uses {colors.accent-gold} fill with {colors.canvas} text, creating a high-contrast signal that stands apart from the indigo system.

### Navigation
**`nav-bar`** — A fixed 64px bar at the top of every page, using {colors.canvas} background with a single {colors.hairline} bottom border. Navigation links use {typography.nav-link} with 0.5px letter spacing and uppercase transformation, giving the brand a archival, museum-like authority. The active link uses {colors.primary} while inactive links sit in {colors.muted}.

**`nav-link-active`** — The currently selected navigation item, distinguished by {colors.primary} text color. No underline or background change — the brand trusts color alone to indicate position.

**`nav-link-inactive`** — Default navigation links in {colors.muted}, creating a clear hierarchy between the current section and available destinations.

### Cards
**`product-card`** — The primary content container for film titles, using {colors.surface-card} (#1e1e1e) as a slightly lighter layer than the canvas. The card has {rounded.sm} corners — deliberately restrained to avoid competing with the film imagery. The image area uses rounded top corners only, creating a clean transition from visual to text.

**`product-card-title`** — Film titles rendered in {typography.title-sm} with {colors.ink} weight, keeping the focus on the artwork and metadata rather than typographic flourish.

**`product-card-price`** — Pricing displayed in {colors.accent-gold}, a warm metallic note that reads as premium against the dark card. This gold appears only in pricing and restoration badges, making it a rare, valuable signal.

### Forms
**`text-input`** — Standard text fields for checkout, account creation, and newsletter signup. Uses {colors.surface-soft} background with a {colors.hairline} border. On focus, the border switches to {colors.primary} indigo, providing clear keyboard focus indication without adding visual noise.

**`text-input-focus`** — Focus state uses the brand's primary indigo as a border color, creating a direct visual connection to the brand's accent system.

**`text-input-error`** — Error state uses a red border (#e74c3c) for accessibility, keeping the error signal distinct from the brand palette.

**`search-bar`** — The primary discovery tool, rendered as a full pill with {rounded.full} on {colors.surface-soft}. It sits prominently in the header and on the homepage, inviting users to explore the catalog. Focus state mirrors the text-input pattern with a {colors.primary} border.

**`filter-dropdown`** — Used in collection and search results pages for sorting by year, director, format, and genre. Matches the input styling with {colors.surface-soft} background and {colors.hairline} border, maintaining consistency across form elements.

### Badges
**`badge-new`** — A small indigo badge for newly added titles, using {colors.badge-new} with white text. The {rounded.xs} corners keep it compact and unobtrusive.

**`badge-restored`** — A gold badge for restored or remastered editions, using {colors.badge-restored} with dark text. This badge signals premium content and justifies higher price points.

### Hero
**`hero-section`** — The full-width hero area on the homepage and collection landing pages. Uses {colors.canvas} as background with {typography.display-xl} for headlines. The {colors.primary} CTA button sits as a pill, creating a clear action point against the dark field.

**`hero-cta`** — The hero's primary button, slightly larger than standard buttons at 48px height with 32px horizontal padding. Uses the same {rounded.full} pill shape and {colors.primary} fill.

### Footer
**`footer`** — A full-width footer on {colors.canvas} with a {colors.hairline} top border. Links use {colors.muted} with {typography.link} sizing, and hover to {colors.ink} for subtle interaction feedback.

**`footer-link`** — Standard footer links in {colors.muted}, maintaining the brand's quiet, archival tone even in secondary navigation.

**`footer-link-hover`** — Hover state lifts the link to {colors.ink}, providing clear feedback without introducing a new color.

### Cart
**`cart-item`** — Individual line items in the cart drawer or page, using {colors.surface-card} background with {colors.hairline} bottom borders for separation. The quantity selector and remove button sit inline, maintaining the compact, information-dense layout typical of film catalogs.

**`quantity-selector`** — A compact input for adjusting item quantities, using {colors.surface-soft} background with {rounded.sm} corners. Matches the filter dropdown styling for consistency.

### Ratings
**`star-rating`** — Star icons rendered in {colors.star-rating} gold, providing a warm accent within product cards and detail pages. The gold rating system echoes the pricing color, creating a cohesive premium signal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked hero layout, reduced padding |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, side-by-side hero content |
| Desktop | 1128–1440px | Three-column product grid, full navigation, multi-row hero with film stills |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, expanded whitespace |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Search bar expands to full width on mobile for easy thumb access
- Filter dropdowns use 40px height to accommodate touch targets
- Navigation links have 48px minimum tap area on mobile
- Product card images link to detail pages with 48px+ tap targets

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with full-height slide-out drawer
- Product grid reduces columns from 4 to 1 as viewport narrows
- Hero section stacks vertically on mobile, with CTA below headline
- Footer columns collapse to single column below 744px
- Filter sidebar becomes a top-mounted dropdown strip on mobile
- Cart drawer overlays full screen on mobile, slides in from right on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from common patterns; actual extracted hover colors are not available
- Error and validation styling (form errors, out-of-stock messaging) is assumed based on accessibility best practices
- Dark mode is not applicable — the brand already uses a near-black canvas as its default
- Sub-brand or collection-specific palettes (e.g., "Silent Film", "Noir", "Restored Classics") could not be extracted
- The extracted hex list (#121212, #dedede, #f3f3f3, #242833, #334fb4) appears to be the brand's core palette, but may be missing secondary accents used in editorial content or promotional banners
- Font weights beyond 400 and 700 are assumed; Lato may be used in 300 or 900 weights for specific editorial treatments
- Spacing values are estimated from common e-commerce patterns; actual site spacing may vary
- Animation durations and easing curves are not available from static extraction
- Shopify-specific components (cart drawer, checkout buttons, payment icons) follow platform defaults and may not reflect brand customization
- Social media icon colors and footer legal text styling are not captured
- The gold accent (#c9a84c) is inferred from the brand's use of gold in pricing and badges; actual extracted value may differ slightly
