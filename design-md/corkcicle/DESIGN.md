---
version: alpha
name: "Corkcicle"
source_url: "https://corkcicle.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the thermal physics of a triple-wall vacuum seal, Corkcicle lives in the tension between high-performance outdoor gear and the saturated, almost candy-colored palette of a 1990s surf shop. The extracted hex list is a riot of accents — #c93997 (a hot pink), #26c0c9 (a turquoise), #ffbb77 (marigold), #ff6c63 (coral), #78a354 (sage) — but the true structural foundation is a near-white #f3f3f3 canvas and an almost-black #080808 ink, with #f2f2f5 and #e1e1e1 providing soft surface layers. The brand voice is Cosmica, a chunky extra-bold sans-serif that appears in four weights (ExtraBold, Medium, Regular, SemiBold) and reads as confident, playful, and slightly retro — the kind of typeface that would look at home on a cooler lid or a skateboard deck. MaisonNeueMono appears for technical specs or small print, adding a utilitarian counterpoint. Buttons and badges use {rounded.full} pill shapes, while product cards land at {rounded.sm} — the brand avoids sharp corners for anything interactive, but keeps photography edges clean. The signature design move is color-blocking: a product shot on a #fdedde peach background, a CTA in #c93997 against #080808 text, a badge in #26c0c9. Corkcicle doesn't whisper — it uses high-chroma accents as functional wayfinding, not decoration.

colors:
  primary: "#c93997"
  primary-active: "#a82d7a"
  primary-disabled: "#e78caa"
  ink: "#080808"
  body: "#262626"
  muted: "#717171"
  muted-soft: "#88888d"
  hairline: "#d2d2d2"
  hairline-soft: "#e2e2e2"
  canvas: "#f3f3f3"
  surface-soft: "#f2f2f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-turquoise: "#26c0c9"
  accent-marigold: "#ffbb77"
  accent-coral: "#ff6c63"
  accent-sage: "#78a354"
  accent-hotpink: "#ff5988"
  accent-terracotta: "#ef7a5a"
  accent-burgundy: "#48151a"
  badge-green: "#20880c"
  badge-blue: "#007aff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'CosmicaExtraBoldRegular', 'CosmicaExtraboldRegular', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'CosmicaExtraBoldRegular', 'CosmicaExtraboldRegular', sans-serif"
    fontSize: 28px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'CosmicaSemiBoldRegular', 'CosmicaSemiboldRegular', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'CosmicaMediumRegular', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'CosmicaMediumRegular', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'CosmicaRegularRegular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'CosmicaRegularRegular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'CosmicaRegularRegular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  mono-sm:
    fontFamily: "'MaisonNeueMonoRegular', 'MaisonNeueMonoBold', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'CosmicaSemiBoldRegular', 'CosmicaSemiboldRegular', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'CosmicaSemiBoldRegular', 'CosmicaSemiboldRegular', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'CosmicaSemiBoldRegular', 'CosmicaSemiboldRegular', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'CosmicaRegularRegular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'CosmicaMediumRegular', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-accent-turquoise:
    backgroundColor: "{colors.accent-turquoise}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-pill-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-photo:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-badge:
    backgroundColor: "{colors.accent-turquoise}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.title-sm}"
    textColor: "{colors.accent-coral}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.hairline}"
  color-swatch-selected:
    border: "3px solid {colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-turquoise}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a pill-shaped button in #c93997 hot pink with white uppercase text set in Cosmica SemiBold at 15px. On hover, it shifts to #a82d7a; disabled state uses #e78caa. The {rounded.full} shape is non-negotiable — no square buttons exist in the system. **`button-secondary`** — An outlined variant with a 2px #080808 border on a white background, same pill shape and typography. Used for "Learn More" or secondary actions alongside primary buttons. **`button-accent-turquoise`**, **`button-accent-coral`**, and **`button-accent-marigold`** — Color-specific CTAs that appear in themed sections or seasonal promotions. Each uses the same pill shape and uppercase SemiBold type, but the text color flips to #080808 on lighter accents (turquoise, marigold) and white on darker ones (coral). **`button-pill-small`** — A compact 36px-tall variant for inline actions like "Add to Cart" on product cards or quick filters.

### Cards
**`product-card`** — A white card with {rounded.sm} corners and 16px padding, containing a 1:1 product photo (also {rounded.sm}), a title in {typography.title-sm}, and a price in {typography.title-sm}. Sale prices render in #ff6c63 coral. Badges (new, sale, bestseller) sit as {rounded.full} pills over the photo's top-left corner, using accent colors: #26c0c9 turquoise for standard badges, #ff6c63 coral for sale, #20880c green for new arrivals. **`color-swatch`** — A 32px circle with a 2px #d2d2d2 border; selected state swaps to a 3px #080808 border. Used in product detail views to show available colorways.

### Navigation
**`top-nav`** — A 72px white bar with a 1px #e2e2e2 bottom border. Nav links are uppercase Cosmica Medium at 14px with 0.3px letter-spacing. Active state underlines with a 2px #c93997 border and tints the text to the primary pink. The search bar is a {rounded.full} input with a 1px #d2d2d2 border that thickens to 2px #c93997 on focus.

### Forms
**`newsletter-input`** — A {rounded.full} text input with 12px/20px padding and a 1px #d2d2d2 border, paired with a **`newsletter-submit`** button in #26c0c9 turquoise. The submit button uses {typography.button-sm} uppercase text. **`quantity-selector`** — A compact row with two {rounded.full} icon buttons flanking a centered number in {typography.body-md}, set on a #f2f2f5 background with {rounded.sm} container.

### Footer
**`footer`** — A full-width #080808 section with white body text and #88888d link color. Links use {typography.link} (14px Cosmica Regular). The footer contains the newsletter form, navigation columns, and social icons in a stacked layout on mobile, grid on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; hero text reduces to {typography.display-lg}; footer stacks vertically; search bar becomes full-width; product cards use full-width with 8px padding |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4-5 links; hero uses {typography.display-xl} at 28px; footer uses 2-column layout; search bar is 320px max |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero uses {typography.display-xl} at 36px; footer uses 4-column grid; search bar is 400px max |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; hero content constrained to 1200px; all spacing scales up by 1.25x |

### Touch Targets
- All buttons and interactive elements minimum 44px height (exceeds Apple HIG)
- Color swatches at 32px with 8px touch padding
- Icon buttons at 40px diameter
- Quantity selector buttons at 32px within a 44px container
- Nav links have 8px vertical padding for tap area

### Collapsing Strategy
- Top-nav links collapse into a hamburger menu at < 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack from 4 to 1 on mobile
- Hero section reduces padding from 64px to 32px on mobile
- Search bar expands from fixed width to full-width on mobile
- Product card badges shift from top-left overlay to inline below photo on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (only primary button active/disabled were extractable; secondary button hover, nav-link hover, card hover were not visible in extracted data)
- Error state styling for form inputs (validation colors, error messages, border colors on error)
- Dark mode or high-contrast mode variants (no evidence of a dark theme in extracted CSS)
- Sub-brand or collection-specific palettes (Corkcicle may have seasonal colorways that override the system palette)
- Typography scale for mobile (all font sizes extracted from desktop; mobile scale may differ)
- Specific spacing values for product grid gaps (extracted as {spacing.base} but actual gap may be different)
- Animation and transition timing (no extracted values for hover transitions, page loads, or micro-interactions)
- Icon system details (social icons, cart icon, search icon — extracted only as "icons" font-family, no glyph map)
- Checkout flow styling (Shopify checkout may use a separate theme; extracted colors include #007aff which may be a checkout widget default)
- Accessibility contrast ratios (not verified against WCAG 2.1 AA/AAA for any color pair)
