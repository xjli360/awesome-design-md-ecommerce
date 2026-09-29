---
version: alpha
name: "Balolo"
source_url: "https://www.balolo.de"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep teal #108474 anchors every primary action across Balolo's wood-and-workspace ecosystem — a color pulled from the heart of a forest rather than a tech dashboard, appearing on add-to-cart buttons, navigation highlights, and the brand's signature monitor-stand risers. The palette runs through a meticulous grayscale gradient (#1a1a1a for ink, #7b7b7b for body text, #b1b1b1 for muted, #dedede for hairline, #f9fafb for canvas) with a warm undertow in #f5f2ee and #cbc0ac that echoes natural wood tones without being literal. Plus Jakarta Sans carries the typography at moderate weights — display headlines sit at 500–600 rather than aggressive 700s, letting the product photography of walnut and oak grain do the heavy lifting. Cards use {rounded.sm} corners, buttons use {rounded.sm}, and the search bar uses {rounded.full}, creating a system that feels precise and workshop-crafted rather than playful. The brand's trust signal — a 4.8-star Judge.me badge — appears in {rounded.xs} pills with the extracted #108474 as its accent, and every product card floats on {surface-card} white with a {hairline} border that reads like a blueprint edge. This is a system built for clarity: the teal is the only color that ever feels like a decision, and everything else steps back to let the wood grain and the workspace function lead.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#b8d9d4"
  ink: "#1a1a1a"
  body: "#7b7b7b"
  muted: "#b1b1b1"
  muted-soft: "#c1c1c1"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#f9fafb"
  surface-soft: "#f5f2ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  wood-warm: "#cbc0ac"
  wood-warm-light: "#efece6"
  badge-green: "#108474"
  star-rating: "#1a1a1a"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Plus Jakarta Sans', 'Plus Jakarta Sans', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px

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
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  badge-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-pill-wood:
    backgroundColor: "{colors.wood-warm-light}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  star-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the brand's deep teal #108474. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to `{button-primary-active}` with #0d6b5d. Disabled state uses `{button-primary-disabled}` with #b8d9d4, maintaining the same 8px rounded corners and 44px height.

**`button-secondary`** — An outlined or ghost-style button on white canvas, used for "Learn More", "View Details", and secondary actions. Text is ink #1a1a1a with a 1px hairline border. On hover, the background fills with `{surface-soft}` #f5f2ee.

**`button-tertiary-text`** — A text-only button in primary teal, used for inline links like "Read Reviews" or "See All". No background, no border — just the teal text with underline on hover.

### Cards
**`product-card`** — The core product display unit, a white card with 8px rounded corners and a subtle 1px hairline border. Contains a product image with matching 8px rounded corners, a title in `{title-sm}`, and a price in `{body-sm}` at #7b7b7b. The card has no shadow — the brand relies on clean borders and whitespace rather than elevation.

**`badge-pill`** — A small, fully rounded pill in primary teal, used for "Best Seller", "New", or "4.8★" trust badges. Text is white, padding is 4px 12px. A secondary variant `{badge-pill-wood}` uses the warm #efece6 background with ink text for material-specific tags like "Walnut" or "Oak".

### Navigation
**`nav-bar`** — A 72px sticky header on white canvas, containing the logo, product category links in `{nav-link}`, a search bar pill, and a cart icon. On scroll, compresses to 60px. Active nav links are underlined in primary teal.

**`search-bar-pill`** — A fully rounded search input on #f5f2ee background, 44px tall, with placeholder text in #b1b1b1. On focus, the background shifts to white with a primary teal border.

### Forms
**`text-input`** — Standard text input fields on #f9fafb canvas, 44px tall with 8px rounded corners and 12px 16px padding. On focus, the border changes to primary teal. Used for email signup, contact forms, and checkout fields.

### Footer
**`footer-link`** — Standard link in #7b7b7b body text, no underline. On hover, turns primary teal. The footer is organized in columns with section headers in `{caption}` uppercase.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), nav collapses to hamburger menu, hero text reduces to `{display-md}`, search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid, nav shows top-level links only, search bar remains visible but compresses |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, search bar at full width |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, centered layout |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 40px tap area
- Search bar pill minimum 44px height
- Product card tap target is the entire card surface

### Collapsing Strategy
- Navigation collapses to hamburger menu at < 744px
- Product grid collapses from 4-column to 1-column at mobile
- Footer columns collapse to single column at < 744px
- Hero section reduces padding from 64px to 32px at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors are heavily weighted toward grayscale tones — the brand's true primary #108474 appears only once in the extracted list, suggesting it may be used sparingly or the extraction missed some pages. The remaining colors (#eeeeee, #f9fafb, #7b7b7b, etc.) form a clean grayscale system but lack the distinctive teal presence one would expect from a brand using it as primary.
- Font-family extraction returned "JudgemeStar" (a review-widget font) and "Plus Jakarta Sans" with some duplication. The actual brand font may include additional weights (e.g., 700 for display) not captured.
- Hover states for buttons, links, and cards are inferred from common patterns — actual transitions (ease, duration) not extracted.
- Error states for form inputs (red borders, error messages) not captured.
- Dark mode not present on the live site — no dark palette available.
- Sub-brand or collection-specific color variations (e.g., limited editions) not extracted.
- Spacing values are estimated from common patterns — actual padding/margin values may vary by component.
- No extracted data for modal, tooltip, or dropdown component styling.
