---
version: alpha
name: "Dieux"
source_url: "https://www.dieuxskin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dieux is a skincare brand that feels like a quiet, clinical rebellion against the industry's noise. The canvas is a warm, off-white `#fbf8f0` that reads as paper or unglazed ceramic, not sterile lab white — a deliberate choice that signals transparency and honesty. The brand's primary voltage is a muted, dusty coral `#e0634e`, used sparingly on CTAs and accents, never screaming for attention. Text lives in a restrained palette of near-blacks (`#222222`, `#2e2e2e`) and soft grays (`#7f7f7f`, `#666666`), set in a mix of GT America for clean, modern body copy and the stately serif Perpetua for editorial moments. A secondary palette of muted blues (`#83adc5`, `#b9d9eb`) and a deep teal (`#3d7562`) appears in product photography and ingredient callouts, adding a layer of clinical calm. The system avoids hard corners — `{rounded.sm}` (8px) on buttons and `{rounded.md}` (12px) on cards keeps the interface approachable without being childish. There is no hero gradient, no heavy shadow; the design trusts typographic hierarchy, generous `{spacing.section}` (64px) breathing room, and the raw texture of ingredients photography. The overall mood is that of a well-edited lab notebook: precise, unadorned, and quietly confident.

colors:
  primary: "#e0634e"
  primary-active: "#d02030"
  primary-disabled: "#f0c0b8"
  ink: "#222222"
  body: "#2e2e2e"
  muted: "#7f7f7f"
  muted-soft: "#b1b1b1"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#fbf8f0"
  surface-soft: "#fbf8f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#83adc5"
  accent-blue-soft: "#b9d9eb"
  accent-teal: "#3d7562"
  error: "#dc3545"
  error-strong: "#8b0000"
  success: "#00a12a"
  star-rating: "#222222"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Perpetua Titling', 'Perpetua', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Perpetua Titling', 'Perpetua', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT America Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'GT America Mono', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
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
    textColor: "{colors.on-primary}"
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
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
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
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sold-out:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-ingredient:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    padding: "{spacing.base} {spacing.md}"
  ingredient-list:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    lineHeight: 1.6
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and key checkout flows. Rendered in the brand's muted coral `#e0634e` with white text, 8px rounded corners, and uppercase GT America at 14px/600 weight. On hover, it shifts to `#d02030` for a subtle but clear active state. The disabled state uses a lighter, desaturated coral `#f0c0b8` to signal non-interactivity without visual noise.

**`button-secondary`** — A outlined variant for secondary actions like "Learn More" or "View Ingredients". Uses the warm canvas `#fbf8f0` background with a 1px hairline `#e5e5e5` border and near-black `#222222` text. Maintains the same 44px height and uppercase typography as the primary button for visual consistency in forms and product grids.

**`button-tertiary-text`** — A text-only button for inline actions like "Cancel" or "Clear filters". No background or border, relying on the `#222222` ink color and uppercase GT America to remain legible against any surface. Used sparingly to avoid clutter.

**`button-pill-primary`** — A fully pill-shaped variant (`{rounded.full}`) reserved for subscription toggles and "Notify Me" signups. Uses the same coral `#e0634e` but at a smaller 12px uppercase size, making it feel more intimate and less transactional than the standard primary button.

### Cards
**`product-card`** — The core product display unit, a white `#ffffff` card with 12px rounded corners (`{rounded.md}`). Contains a product image (also 12px rounded), the product name in 16px/600 GT America, and the price in 14px/400 at `#7f7f7f`. No shadow or border — the card relies on the contrast between the white surface and the warm `#fbf8f0` canvas for separation. Used in grid layouts on collection pages and the homepage.

**`hero-section`** — A full-width banner section on the homepage and landing pages. Uses the warm canvas `#fbf8f0` as background, with a 48px Perpetua Titling heading and 16px GT America body for the subheading. The section padding is 64px (`{spacing.section}`) top and bottom, creating a generous, editorial feel. No background image overlay — the typography and whitespace do the work.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, using the canvas `#fbf8f0` background. Links are set in 14px/500 uppercase GT America with 0.3px letter spacing. Active links use `#222222`, inactive links use `#7f7f7f`. The bar includes a centered logo (typically the Dieux wordmark in Perpetua or a custom logotype) and a right-aligned cart icon. On mobile, the nav collapses into a hamburger menu.

### Forms
**`text-input`** — Standard text input for email signups, search, and checkout forms. Uses the canvas `#fbf8f0` background with a 1px `#e5e5e5` border and 8px rounded corners. On focus, the border switches to `#222222` for clear visual feedback. Error states use `#dc3545` border. Height is 48px with 12px/16px padding for comfortable touch targets.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used in the mobile nav and collection page headers. Uses a slightly lighter surface `#fbf8f1` background with 14px GT America text. Height is 40px, making it compact enough for header placement without sacrificing usability.

### Badges
**`badge-new`** — A small, monospaced label for "NEW" products, using the muted blue `#83adc5` background with white text. Set in 10px uppercase GT America Mono with 4px rounded corners (`{rounded.xs}`). Placed in the top-left corner of product card images.

**`badge-sold-out`** — Uses the error red `#dc3545` for "SOLD OUT" indicators. Same typography and sizing as the new badge, but with stronger visual weight to clearly communicate unavailability.

**`badge-ingredient`** — A teal `#3d7562` badge for highlighting key ingredients (e.g., "Retinol", "Vitamin C") on product cards or ingredient pages. Uses the same monospaced typography as other badges for consistency.

### Footer
**`footer`** — A dark footer section with `#222222` background and white `#fbf8f0` text. Links are set in 14px GT America at `#b1b1b1` for legibility against the dark background. The footer includes columns for "Shop", "Learn", "About", and "Support", plus a newsletter signup form. Padding is 64px (`{spacing.section}`) top and bottom.

### Accordion
**`accordion`** — Used on product detail pages for ingredient lists, usage instructions, and FAQs. No rounded corners, with a 1px `#e5e5e5` border separating each item. Headers are 16px/600 GT America with 16px/12px padding. Content sections use 16px/400 GT America body text. The accordion relies on a simple plus/minus icon for expand/collapse affordance.

**`ingredient-list`** — A specialized typography token for ingredient lists, using 12px uppercase GT America Mono at `#7f7f7f` with 1.6 line height. This creates a clinical, lab-notebook feel that aligns with the brand's transparency ethos.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grids, collapsed nav (hamburger), full-width hero, 16px horizontal padding |
| Tablet | 744–1128px | Two-column product grids, expanded nav with dropdowns, 24px horizontal padding, hero text scales down |
| Desktop | 1128–1440px | Three-column product grids, full nav, 32px horizontal padding, hero uses display-xl |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero uses display-xl with larger spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility.
- Icon buttons are 40x40px with `{rounded.full}` for easy tapping.
- Product card tap targets are the entire card surface, not just the title or price.
- Nav links have 32px minimum touch height on mobile.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu with a slide-out drawer.
- Product grids collapse from 3 columns to 2 columns on tablet, and 1 column on mobile.
- The hero section reduces heading size from 48px to 32px on mobile, and stacks the subheading below.
- Footer columns collapse from 4 columns to 2 columns on tablet, and 1 column on mobile.
- Accordion content is always collapsed by default on all breakpoints.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be reliably extracted from the live site.
- Error styling for form validation (inline messages, iconography) is inferred from the error color token but not confirmed.
- Dark mode tokens are not present; the brand appears to use only the warm canvas `#fbf8f0` as its primary background.
- Sub-brand or collection-specific palettes (e.g., limited edition drops) may exist but were not observed.
- The exact font weights for GT America (e.g., 400, 500, 600) are inferred from common usage; the site may use additional weights.
- The `Kapakana` font family was found in declarations but its usage context (headings, decorative elements) could not be determined.
- Animation and transition tokens (duration, easing) were not extracted.
- The `Perpetua!important` declaration suggests a possible override pattern, but the specific context is unknown.
- Spacing for specific components (e.g., product card padding) is estimated based on common patterns and may differ from the live implementation.
