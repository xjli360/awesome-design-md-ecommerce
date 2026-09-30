---
version: alpha
name: "NS Design"
source_url: "https://www.thinkns.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, resonant #2d2d2d ink on a warm #fcfbf7 canvas, where the brand's true voltage is carried not by a single accent but by the interplay of three: a cool, precise #0073e5 that reads as engineered clarity, a burnished #d7b87e that recalls aged brass and wood grain, and a restrained #9b1b30 that appears only in select moments of emphasis. The typographic voice is a deliberate mix — Montserrat for clean, modern display weight, Source Sans Pro for readable body copy, and Open Sans Condensed for tight navigation — suggesting a brand that bridges luthier craftsmanship with digital precision. Product imagery dominates over decorative UI; the interface steps back to let the instruments' curves and finishes speak. Corners are mostly sharp ({rounded.none} to {rounded.sm}), with the only softening appearing on media cards and button edges ({rounded.md}), reinforcing a sense of machined exactness. The overall mood is gallery-meets-workshop: generous whitespace, muted secondary surfaces (#f7eddc), and a hierarchy that trusts the photography to do the emotional work while the type system handles information architecture.

colors:
  primary: "#0073e5"
  primary-active: "#006ba1"
  primary-disabled: "#8ed1fc"
  ink: "#2d2d2d"
  body: "#444444"
  muted: "#505050"
  muted-soft: "#949494"
  hairline: "#8c8c8c"
  hairline-soft: "#eeeeee"
  canvas: "#fcfbf7"
  surface-soft: "#f7eddc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-brass: "#d7b87e"
  accent-brass-dark: "#796545"
  accent-brass-deep: "#625137"
  accent-red: "#9b1b30"
  accent-red-active: "#c02b0a"
  accent-purple: "#7a00df"
  ink-deep: "#111111"
  ink-light: "#003399"
  ink-mid: "#003388"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans Condensed', 'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
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
    border: "2px solid {colors.ink}"
    padding: 10px 26px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-brass:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-brass}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 4px 12px rgba(45,45,45,0.1)"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-brass}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's cool blue {colors.primary} and white text. Used for key actions like "Shop Now", "Learn More", and "Configure". On hover, shifts to {colors.primary-active} for a darker, more grounded state. Disabled state uses {colors.primary-disabled} to signal inactivity without visual noise. The {rounded.sm} corners keep the button feeling precise and engineered, not playful.

**`button-secondary`** — An outlined alternative that sits on the {colors.canvas} background with a 2px {colors.ink} border. Used for secondary actions like "View Details" or "Compare Models". Active state fills the background with {colors.surface-soft} for a subtle pressed effect. The border weight ensures the button remains legible against the warm canvas.

**`button-tertiary-text`** — A text-only button in {colors.primary} with no background or border. Used for inline actions, "Read More" links in product descriptions, and dismissible UI elements. Relies on the {typography.button-md} weight for sufficient presence without a container.

**`button-accent-brass`** — A warm, earthy alternative to the primary blue, using {colors.accent-brass} on a {colors.ink-deep} text. Deployed on product detail pages for "Add to Cart" when the product photography features warm wood tones, or as a secondary CTA in hero sections. The brass hue echoes the physical materials of the instruments.

**`button-accent-red`** — A high-emphasis button reserved for clearance, limited editions, or "Last Chance" urgency. Uses {colors.accent-red} with white text. Appears sparingly — typically only one per page — to preserve its signal value.

### Cards
**`product-card`** — A white card ({colors.surface-card}) with {rounded.md} corners and a 1px {colors.hairline} border. The product image occupies the top with {rounded.md} top corners, while the title, series name, and price sit below in {typography.title-sm} and {typography.body-sm}. On hover, a subtle box-shadow lifts the card 4px off the canvas, suggesting selectability without animation.

**`product-badge-new`** — A small red badge ({colors.accent-red}) with white uppercase text in {typography.badge}. Positioned at the top-left of the product image. The {rounded.sm} corners and tight padding keep it from competing with the product photography.

**`product-badge-sale`** — A brass badge ({colors.accent-brass}) with dark text ({colors.ink-deep}), used for promotional pricing. Same shape and size as the new badge, but the warm metallic tone signals value rather than novelty.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on {colors.canvas}. Navigation links use {typography.nav-link} (Open Sans Condensed, uppercase, 15px, bold, tracked 0.5px) for a condensed, architectural feel. Active page links shift to {colors.primary}, while hover reveals a {colors.accent-brass} color shift — a subtle nod to the brand's material palette. The bar has a 1px {colors.hairline-soft} bottom border.

**`nav-link-active`** — The current page or section indicator. Uses {colors.primary} with no underline or background change — the color alone signals location.

**`nav-link-hover`** — On hover, links transition to {colors.accent-brass} over 200ms. This brass glow is the brand's signature micro-interaction, echoing the warm metallic hardware on the instruments.

### Forms
**`text-input`** — A standard input field with {colors.canvas} background, 1px {colors.hairline} border, and {rounded.sm} corners. On focus, the border thickens to 2px and shifts to {colors.primary}. Error state uses a 2px {colors.accent-red} border. Height is 44px for comfortable touch targeting. Placeholder text uses {colors.muted}.

### Hero
**`hero-section`** — A full-width dark section using {colors.ink-deep} as background with {colors.canvas} text. Used for flagship product launches and brand storytelling. The {typography.display-xl} headline sits at 42px with generous padding ({spacing.section} top/bottom). A lighter variant (`hero-section-light`) uses {colors.surface-soft} with {colors.ink} text for secondary hero areas.

### Footer
**`footer-section`** — A dark footer on {colors.ink-deep} with {colors.muted-soft} text. Links use {typography.link} and shift to {colors.accent-brass} on hover. The footer is divided into columns with {colors.hairline} dividers between sections. Social icons appear as {icon-button} elements with {rounded.full} shape.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-md}; buttons go full-width; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses {typography.display-lg}; side-by-side content sections |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at full {typography.display-xl}; multi-column footer |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns; hero has larger padding; content sections have wider gutters |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Icon buttons are 40px × 40px minimum
- Product cards have full-surface tap targets (no small hit areas)
- Nav links have minimum 48px tap height on mobile

### Collapsing Strategy
- Mobile nav collapses to hamburger icon with slide-in drawer
- Product filters collapse to a "Filter" button that opens a modal overlay
- Footer columns stack vertically on mobile
- Hero content stacks (headline above description above CTA) on mobile
- Multi-column product descriptions collapse to single column below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for many components are inferred from common patterns; the live site may use different transitions or color shifts
- Error state styling for forms (validation messages, error icons) was not extractable from the static HTML
- Dropdown menus and mega-nav behavior could not be observed
- Dark mode or high-contrast mode specifications are absent from the extracted data
- The extracted color list contains many framework defaults (WordPress palette colors like #f78da7, #cf2e2e, #ff6900, #fcb900, #7bdcb5, #00d084, #0693e3) that are unlikely to be brand colors — these have been excluded from the palette
- Font weights beyond 400 and 700 were not extractable; intermediate weights (500, 600) are inferred
- Line heights and letter-spacing values are estimated based on common typographic practice, not extracted from CSS
- The brand's true primary accent may be #d7b87e (brass) rather than #0073e5 (blue) — the blue appears more frequently in UI chrome while the brass appears in brand-voice moments; further design review is recommended
- Animation durations, easing curves, and transition properties were not extractable
- Shadow values (box-shadow, drop-shadow) are estimated
- Z-index layering and stacking contexts are unknown
- Print stylesheet behavior is not documented
