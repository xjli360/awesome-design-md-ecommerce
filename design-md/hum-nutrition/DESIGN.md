---
version: alpha
name: "Hum Nutrition"
source_url: "https://www.humnutrition.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A pink voltage — `#ee4b9b` — runs through every primary CTA, badge, and accent on an otherwise white `#fefefe` canvas, giving the brand the energy of a wellness startup that refuses to be beige. The palette pulls from the extracted site: a hot-magenta `#e10098` for hover states, a softer `#f8c1d9` for backgrounds, and a punchy lemon `#fecf0a` for limited-edition or sale moments. Typography relies on Montserrat at moderate weights — display sits at 24–32px in weight 500/600, never heavy, letting the pink do the shouting. Product cards use `{rounded.sm}` corners, while CTAs go full pill (`{rounded.full}`) at 48px height, creating a friendly, approachable rhythm. The nav bar stays minimal: white background, pink logo wordmark, and a cart icon that turns `#ee4b9b` on hover. The brand trusts clean product photography and generous whitespace over decorative flourishes — the pink is the ornament. A secondary palette of warm grays (`#545454`, `#757575`, `#9ca3af`) handles body text and muted labels, while `#010202` ink provides near-black contrast for headlines. The overall feel is confident, clinical but warm — like a dermatologist’s office that stocks neon lipstick.

colors:
  primary: "#ee4b9b"
  primary-active: "#e10098"
  primary-disabled: "#f8c1d9"
  ink: "#010202"
  body: "#545454"
  muted: "#757575"
  muted-soft: "#9ca3af"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#fefefe"
  surface-soft: "#f5f9fc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fecf0a"
  accent-hot-pink: "#ee0aa4"
  badge-pink-bg: "#ffe6f7"
  badge-pink-text: "#a01c3d"
  star-rating: "#fecf0a"
  scrim: "#060606"

typography:
  display-xl:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.3px
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  top-nav-logo:
    height: 28px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  top-nav-cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 24px
  top-nav-cart-icon-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-hot-pink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-pink-bg}"
    textColor: "{colors.badge-pink-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.star-rating}"
    marginTop: "{spacing.xs}"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    height: 36px
    marginTop: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 480px
    marginTop: "{spacing.md}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: 0.5px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    height: 44px
    border: "none"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    height: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.md}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.md}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered as a full-pill button in `#ee4b9b` with white uppercase Montserrat text. On hover, the background shifts to `#e10098`; on disabled, it fades to `#f8c1d9`. Used for "Add to Cart", "Subscribe", and "Shop Now" actions. Height is fixed at 48px with 14px/28px padding.

**`button-secondary`** — An outlined variant with a white background and `#ee4b9b` border and text. Active state uses `#e10098` border and a `#f5f9fc` background. Used for "Learn More" or secondary checkout options.

**`button-tertiary-text`** — A text-only button with no background or border, colored in `#ee4b9b`. Hover shifts to `#e10098`. Used for "Cancel" or "Skip" actions in flows.

**`button-yellow`** — A limited-edition accent button in `#fecf0a` with near-black text. Used for flash sales, bundles, or promotional CTAs. Same pill shape and 48px height as primary.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and `{spacing.base}` padding. Contains a square product image with `{rounded.xs}`, a title in `{typography.title-sm}`, price in `{typography.body-sm}`, optional star rating in `#fecf0a`, and a small pill badge for "NEW" or "BESTSELLER" in `#ffe6f7` with `#a01c3d` text. An "Add to Cart" mini-pill button sits at the bottom.

### Navigation
**`top-nav`** — A 72px white bar with `{spacing.xl}` horizontal padding. The logo sits left at 28px height. Nav links are uppercase Montserrat 13px/500 with `{spacing.sm}` vertical padding. Active/hover links turn `#ee4b9b`. The cart icon is a simple 24px SVG that tints pink on hover.

### Forms
**`text-input`** — A 44px input with `{rounded.sm}`, 1px `#e0e0e0` border, and `{spacing.sm}`/`{spacing.md}` padding. On focus, the border becomes 2px `#ee4b9b`. Error state uses 2px `#ee0aa4`. Used for email, name, and address fields.

**`search-bar`** — Similar to text-input but with a `#f5f9fc` background and `{rounded.sm}`. Focus shifts to white background with 2px pink border. Used for product search on the site.

**`newsletter-input`** — A full-pill input with white background, no border, 44px height, and `{spacing.sm}`/`{spacing.lg}` padding. Paired with a `newsletter-submit` pill button in `#ee4b9b`.

### Footer
**`footer`** — A near-black (`#010202`) section with white text. Links use `#9ca3af` and turn `#ee4b9b` on hover. Headings are uppercase captions with 0.5px letter spacing. Contains newsletter signup, navigation columns, and social icons.

### Accordion
**`accordion`** — A white section with a 1px `#e0e0e0` bottom border. The header uses `{typography.title-sm}` and the content uses `{typography.body-sm}` in `#545454`. Used for FAQ sections and product descriptions.

### Tabs
**`tab-active`** — An underlined tab with `#ee4b9b` bottom border and pink text. Inactive tabs use `#757575` text with no underline. Used for product category filtering ("Skin", "Body", "Mood").

### Progress & Toggle
**`progress-bar`** — A 4px pill-shaped bar in `#e0e0e0` with a `#ee4b9b` fill. Used for subscription progress or checkout steps.

**`toggle`** — A 44x24 pill switch with `#e0e0e0` background. Active state fills with `#ee4b9b`. The knob is a 20px white circle. Used for subscription auto-renewal toggles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; hero padding reduces to 32px; buttons go full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links; hero maintains 64px padding; search bar collapses to icon |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero at 64px padding; search bar visible |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 600px |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px preferred)
- Icon buttons minimum 40x40px
- Nav links minimum 44px tap area
- Accordion headers minimum 44px tap area
- Toggle minimum 44px width for tap

### Collapsing Strategy
- Top-nav links collapse to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Hero section reduces padding and stacks CTA below text on mobile
- Footer columns collapse to single column below 744px
- Search bar collapses to icon-only on mobile, expanding on tap
- Product card badges may hide on mobile to save space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components could not be fully extracted; primary-active and button-secondary-active are inferred from common patterns
- Error styling for forms (validation messages, error icons) not observed
- Dark mode not present on the live site
- Sub-brand or collection-specific palettes (e.g., "Good Night", "Daily Cleanse") not extracted
- Modal, tooltip, and dropdown component styling not observed
- Loading states (spinners, skeleton screens) not captured
- Focus-visible ring styles not extracted
- Typography line-height and letter-spacing values are estimated based on Montserrat best practices; exact values may vary
- The extracted font list includes monospace fallbacks (Consolas, Courier New, etc.) which may be used for code blocks or technical content, but primary brand font is Montserrat
- Some hex colors in the extracted list may be social icon colors (e.g., `#1f1f1f`, `#222222`) or checkout widget colors; the brand's true primary is `#ee4b9b` based on frequency and distinctiveness
