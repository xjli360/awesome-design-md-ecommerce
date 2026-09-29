---
version: alpha
name: "Blueberry Pet"
source_url: "https://blueberrypet.com"
captured_at: "2026-09-28T10:12:26.931982+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Blueberry Pet's storefront CSS shows a working palette of a deep navy blue (#013a81) used for newsletter and form buttons, a soft sky-blue hover state (#a3dce6), and a large supporting set of neutrals (#ffffff, #191919, #333333, #777777, #e9e7e7, #f7f8fa) that carry text, backgrounds, and hairlines across the theme. Bootstrap-derived utility colors (#007bff, #28a745, #ffc107, #dc3545) and a review-widget accent (#393f79) also appear, suggesting the storefront layers a customized Shopify theme over stock component libraries and a third-party review app. Red tones (#ea0029, #f8353e, #c10b18) recur enough to be treated as an inferred sale/clearance accent, consistent with the "Sale / Markdown" navigation seen in the page text.

  Font evidence includes Oswald, Montserrat, Open Sans, and Source Sans Pro alongside Arial/sans-serif fallbacks; icon fonts (wokiee_icons, revicons, JudgemeStar) are excluded from typographic roles. This interpretation assigns Oswald/Montserrat to headings (a common condensed-plus-geometric pairing for pet/lifestyle retail) and Source Sans Pro/Open Sans to body copy — these role assignments are inferred, not confirmed by heading-specific selectors in the supplied evidence. The resulting system favors a clean, blue-and-white e-commerce shell with red used sparingly for urgency and promotions, matching the walking-gear/matching-set merchandising implied by the page content.

colors:
  primary: "#013a81"
  ink: "#191919"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#e9e7e7"
  surface-soft: "#f7f8fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-hover: "#a3dce6"
  secondary: "#393f79"
  sale: "#ea0029"
  info: "#007bff"
  success: "#28a745"
  warning: "#ffc107"
  danger: "#dc3545"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  variant-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"

## Components

**button-primary** uses the observed navy (#013a81) seen on the newsletter form button, with white text and a modest rounded corner; it is the proposed default for "Add to Cart" and checkout actions, though the live add-to-cart button color was not directly captured in the supplied CSS.

**button-secondary** is a proposed outline variant using the same primary navy on a white field, intended for secondary actions like "View Details" or "Compare" on collar/leash/harness listings.

**text-input** is inferred from generic form-reset rules (`button,input,optgroup,select,textarea`) and standard hairline/neutral colors; exact input styling (focus rings, validation colors) was not observed.

**nav-bar** reflects the deep mega-menu structure implied by the page text (Collars, Leashes, Harnesses, Matching Sets, etc.); background and hairline are proposed from the neutral palette since no header-specific selector was supplied.

**product-card** is proposed for grid listings of items like the "Silver-Powered Freshness" collar/harness set, pairing a soft hairline border with title and price typography drawn from the general type scale.

**variant-selector** is a category-appropriate proposed component for the size buttons observed in the text (Small/Medium/Large, 8"–16"), styled after the swatch/button-option patterns seen in the third-party `bcpo-front.css` (white/bordered, black-selected state), though that file is a generic product-options plugin, not brand-specific, so exact colors are approximated to the core palette instead of copied directly.

**hero** is a proposed full-width promotional banner treatment for seasonal campaigns ("Spring & Summer," "Walking Gears"), using the soft surface background and largest display typography; no hero-specific CSS was present in evidence.

**footer** is proposed as a dark, ink-colored band for legal/newsletter content, informed only by the presence of a dark ink neutral (#191919) elsewhere in the palette; footer-specific selectors were not supplied.

**badge** uses the sale-red (#ea0029) pulled from the observed reds, sized for "SOLD OUT," "Sale," or "New" labels referenced in the page text; pill shape is proposed.

**search** is a proposed rounded search field styled from generic neutral/hairline tokens; no search-bar CSS was included in the evidence.

## Responsive Behavior

| Breakpoint | Width      | Notes (proposed) |
|---|---|---|
| mobile | up to 767px | single-column product grid, collapsed hamburger nav, sticky mobile header implied by `.tt-mobile-header.stuck` selector |
| tablet | 768–1023px | 2–3 column product grid, condensed mega-menu |
| desktop | 1024px+ | full mega-menu with category flyouts, 4+ column product grid |

Touch targets should be a minimum 44×44px for variant buttons and cart actions. Navigation is expected to collapse into a mobile drawer below the tablet breakpoint, consistent with the `.tt-mobile-header` class present in evidence, though its exact collapse behavior, animation, and overlay opacity (`rgba(0,0,0,.55)` seen in one rule) were not verified through live interaction. This table is a recommendation based on common e-commerce patterns, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/text only; no rendered layout, computed styles, or DOM screenshots were available, so spacing, grid columns, and exact component sizing are proposed, not measured.
- Heading-to-font mapping (Oswald/Montserrat for display vs. Source Sans Pro/Open Sans for body) is inferred from common usage patterns and font-family presence, not from selector-level confirmation of which elements use which family.
- Icon fonts (wokiee_icons, revicons, JudgemeStar) were excluded from the typography scale as they are not prose/heading fonts; their glyph coverage and licensing were not verified.
- The `bcpo-front.css` rules originate from a third-party product-options add-on (hosted on a Heroku subdomain) and reflect a generic plugin skin rather than confirmed Blueberry Pet brand styling; they were used only loosely to justify the variant-selector pattern.
- Interaction states (hover, focus, active, disabled) beyond the two explicitly supplied hover rules (`.btn-primary:hover`, newsletter button hover) are proposed defaults, not observed.
- Mobile/responsive behavior, breakpoint pixel values, and touch-target sizing are recommendations only; no media-query breakpoints were present in the supplied evidence.
- Custom font availability, self-hosting, and licensing (e.g., Oswald, Montserrat, Source Sans Pro) were not verified against the live site's font-loading configuration.
