---
version: alpha
name: "Sharp"
source_url: "https://www.sharpusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The #ee1e3a red that fires across Sharp's primary CTAs reads less like warmth and more like a control-panel indicator — a precision signal cut from the same vocabulary as power buttons and status LEDs. Sharp Electronics USA runs its pages from a clean white canvas with measured technical spacing, leveraging the authority of Japanese engineering heritage through systematic hierarchy rather than expressive flourish. Product pages organize as feature grids and specification tables that reward the deliberate buyer comparing magnetron wattages and convection modes side by side. The typography stack — system sans-serif in the absence of extracted brand fonts — holds a clean, almost industrial rhythm: heavy weights for display headlines, regular-weight copy for specification content, a register that says "engineered to last" rather than "designed to desire." Navigation runs horizontally across a white bar, product categories listed with clinical directness. There is no gradient softness anywhere. The red (#ee1e3a) operates at single points of commitment — add-to-cart actions, promotional callouts, the sharp edge of a discount badge — while the surrounding white-and-gray scaffold holds space for product photography. Rounded corners stay restrained at {rounded.xs} and {rounded.sm}, reinforcing machine-made precision across every interactive surface. A surface-card at #ffffff floats against a #f5f5f5 surface-soft, creating the minimal separation that product listings need to read as discrete objects without decorative shadow depth. Model numbers rendered in monospace beneath product titles are a quiet signal: this brand's customers open spec sheets before they open their wallets.

colors:
  primary: "#ee1e3a"
  primary-active: "#c91530"
  primary-disabled: "#f7a0aa"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-mid: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-promo: "#ee1e3a"
  badge-new: "#1a1a1a"
  spec-stripe: "#f9f9f9"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-upper:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  model-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 8px 16px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-top:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4:3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-model:
    typography: "{typography.model-number}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 440px
    padding: "{spacing.section} {spacing.xxl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 28px
  badge-promo:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 44px
    width: 48px
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
  category-nav-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripeColor: "{colors.spec-stripe}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  feature-tile:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  feature-tile-icon:
    color: "{colors.primary}"
    size: 40px
  feature-tile-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  footer-logo:
    filter: "brightness(0) invert(1)"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 600

## Components

### Buttons
**`button-primary`** — The main call-to-action renders in Sharp's #ee1e3a against white type at {rounded.xs} 4px radius, preserving the technical, machine-made character of the brand. Hover darkens to `primary-active` (#c91530); disabled bleeds to `primary-disabled` (#f7a0aa) with corner geometry unchanged. At 44px tall and 12px/24px padding, it meets both click and touch targets without oversizing.

**`button-secondary`** — An outlined variant with {colors.ink} border and type on white, matching the primary's 44px height and {rounded.xs} radius. Used for secondary product actions — "Compare," "Download Manual," "Find a Dealer" — that matter to a specification-aware buyer but must not compete visually with the red Add to Cart.

**`button-ghost`** — A {colors.primary} outline-and-text variant at `button-sm` scale, used for filter toggles, pagination controls, and secondary listing-page navigation. Shares {rounded.xs} with the full button family for visual coherence across scale.

### Text Input / Search
**`text-input`** — Standard field with a 1px {colors.hairline} border at rest, snapping to 1px {colors.primary} red on focus. The {rounded.xs} radius and 44px height hold consistent across search, email subscription, and dealer-locator form contexts.

**`search-bar`** — A compound control pairing the text input with `search-button`: the input's right edge carries {rounded.none} to sit flush against the solid {colors.primary} submit container housing a white magnifier glyph. Together they read as a single inline instrument rather than two adjacent elements.

### Navigation
**`nav-bar`** — White canvas bar with a 1px bottom {colors.hairline} hairline separating branded header from page content. The Sharp wordmark anchors left; product category links sit center-right in {typography.nav-link}. A `nav-bar-top` utility strip above it in {colors.ink} carries promotional messaging or dealer-locator prompts at {typography.caption} scale — the only place {colors.ink} is used as a full-bleed background in the header zone.

**`category-nav`** — A secondary horizontal tab strip on {colors.surface-soft} used within product listing pages to filter by subcategory. The active tab underlines in 2px {colors.primary} with type color switching to match. This keeps the accent confined strictly to interaction indicators, never bleeding into passive chrome.

### Product Card
**`product-card`** — White {colors.surface-card} with a 1px {colors.hairline} border and {rounded.sm} corners, containing a 4:3 product photograph, title in {typography.title-sm}, model number in monospace {typography.model-number} beneath it, price in {typography.price-display}, and a compact {colors.primary} CTA button. No box-shadow — the brand uses border over elevation. Promotional and new-model badges overlay the image corner when applicable.

### Hero
**`hero`** — Full-width {colors.ink} dark canvas with white headline and subhead copy. Minimum height 440px. A single {colors.primary} CTA button anchors the text block. Product photographs are typically PNG cutouts rendered without background against the dark field, letting appliance geometry read against the black without competing graphic texture. No gradient overlay.

### Badges
**`badge-promo`** — The #ee1e3a rectangle in uppercase 11px carries "SALE," "LIMITED TIME," or wattage callouts overlaid on product card imagery. **`badge-new`** — The same geometry in {colors.ink} black announces new model arrivals. Both use {rounded.xs} and identical padding; the only distinction is background color.

### Spec Table
**`spec-table`** — Sharp's most brand-specific component. Alternating {colors.spec-stripe} and {colors.canvas} rows separate spec labels from values in a two-column layout: labels in {typography.spec-label} semi-bold, values in {typography.spec-value} regular. The outer container carries a 1px {colors.hairline} border at {rounded.sm}. This table appears on every product detail page and is the primary surface for comparison-shopping; it should never be hidden behind a "Show More" collapse on desktop.

### Feature Tile
**`feature-tile`** — A {colors.surface-soft} tile at {rounded.sm} illustrating product features: Inverter Technology, Auto-Cook Programs, Keep Warm Mode. A {colors.primary} icon at 40px sits above a {typography.title-md} heading and {typography.body-sm} description. Tiles grid 3-up on desktop, collapse to single column on mobile.

### Footer
**`footer`** — Full-width {colors.ink} dark footer with link columns for Products, Support, About Sharp, and Legal. Column headings use {typography.title-sm} white; links use {typography.caption} at {colors.muted-soft}. The Sharp logo renders with `filter: brightness(0) invert(1)` to display white on dark. A copyright bar at base in {typography.caption-sm} is separated from link columns by a 1px {colors.muted} hairline.

### Breadcrumb
**`breadcrumb`** — Lightweight path indicator in {typography.caption} at {colors.muted}, with the current page node switching to {colors.ink} semi-bold. Slash separator. Used on all product detail and category pages; absent from the homepage.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal links; hero drops to 280px min-height; spec-table scrolls horizontally; feature-tile grid collapses to 1-column; nav-bar-top strip hidden |
| Tablet | 744–1128px | 2-column product grid; horizontal nav retained with category overflow into dropdown; hero scales to 360px; feature-tile grid 2-column |
| Desktop | 1128–1440px | 3–4 column product grid; full nav-bar with all category links visible; hero at 440px; spec-table full-width; feature-tile 3-column |
| Wide | > 1440px | Content max-width 1400px centered; hero background extends full-bleed; product grid auto-fits to 4–5 columns |

### Touch Targets
- All buttons, inputs, and nav links maintain a minimum 44px height across breakpoints
- Product card CTAs expand to full-width button on mobile to ease tapping
- Category-nav tab items gain 12px additional horizontal padding on touch viewports
- Search compound control stacks vertically on mobile: full-width input above a full-width submit button

### Collapsing Strategy
- `nav-bar-top` utility strip hides entirely below 744px
- Primary nav compresses to logo + hamburger at < 744px; drawer slides from right on {colors.canvas}
- Category nav tabs scroll horizontally with momentum scrolling on mobile rather than wrapping to a second row
- Footer link columns collapse from 4-column to 2-column at tablet, then single-column at mobile
- Spec table becomes a horizontally scrollable container at < 744px; row labels pin-stick left via sticky positioning

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No font families extracted** — the site likely delivers font assets via JS or CDN without detectable `font-family` declarations at extraction time. Typography tokens use Arial / Helvetica Neue as system-safe fallbacks; actual brand fonts (potentially a licensed grotesque or Sharp-proprietary face) must be confirmed by inspecting loaded font files in browser DevTools.
- **Only one hex color extracted (#ee1e3a)** — the full palette including nav background, footer dark, surface tones, and hairline values has been derived from standard electronics-brand conventions and Sharp's known visual identity. All gray and dark tokens should be validated against the live site before production use.
- **No meta theme-color defined** — browser chrome color on mobile is unspecified; recommend setting `<meta name="theme-color" content="#ee1e3a">` or `"#1a1a1a"` depending on header treatment preference.
- **Promotional color variants unconfirmed** — sale pricing colors, clearance badge hues, and bundle-deal highlight treatments were not captured; `badge-promo` may differ from the extracted primary.
- **Icon system not identified** — Sharp likely uses a custom or licensed icon set for navigation glyphs and feature-tile icons; glyph style (outline vs. filled, stroke weight) should be confirmed before implementation.
- **Animation and transition values not extracted** — hover transition duration and easing on buttons, card interactions, and nav dropdowns are unspecified; 150ms ease-in-out assumed as default.
