---
version: alpha
name: "Little Snail"
source_url: "https://littlesnail.com.au"
captured_at: "2026-09-28T09:39:19.873547+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Little Snail is a WooCommerce-powered boutique selling European wooden, soft, and educational toys to Australian families. The observed CSS shows a white canvas (#ffffff) with dark neutral body text (#333333) and a small set of accent colors layered on top of a fairly standard WordPress/Storefront-derived stylesheet, including a broad Gutenberg default palette (reds, purples, yellows) that is likely used only occasionally in blog content rather than core UI chrome.
  The clearest brand signal is a warm orange (#e27e26) applied to feature links and call-to-action backgrounds, paired with a soft olive-green (#a2c164) used for the header shipping/promo strip and white text on both. A near-black slate (#32373c) is the default WordPress button color and is treated here as a secondary/neutral action color. Root variables define a consistent 16px corner radius for buttons and add-to-cart controls, which this spec treats as the brand's signature rounding rather than the sharper radii typical of stock themes.
  Typography is inferred as Source Sans Pro (a common Storefront/WooCommerce default and present in the observed font list) for body and UI text, with Schoolbell — a handwritten-style webfont observed only in a gift-wrap header rule — reserved as a playful accent for small decorative moments, not primary UI text. All sizes beyond the two explicitly observed (14px, 160%) are proposed.

colors:
  primary: "#e27e26"
  ink: "#141b38"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#a2c164"
  accent-dark: "#32373c"
  danger: "#bd1313"
typography:
  display-xl: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
  accent-script: {fontFamily: "'Schoolbell', cursive", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
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
    rounded: "{rounded.lg}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  shipping-banner:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** uses the observed orange (#e27e26) that appears as a background-color on feature links and CTA elements in the supplied CSS, paired with white text and the site's 16px root corner radius. This is proposed as the main "Add to cart" / "Shop now" action color.

**button-secondary** reuses the dark slate (#32373c) that WordPress's default `.wp-element-button` rule applies site-wide, giving a lower-emphasis action style (e.g. "View details") distinct from the orange primary.

**text-input** is a proposed pattern for search and account forms; no explicit input styling was present in the supplied CSS, so border color, radius, and padding are inferred from the general hairline/spacing scale rather than measured.

**nav-bar** represents the site header (`.site-header`), observed as white-background with the header widget region sitting above it in olive-green. Link typography and spacing are proposed defaults consistent with the small body-sm size confirmed in `.header-widget-region`.

**product-card** covers the toy listing tiles referenced by product-archive and product-detail background rules (`.archive-header`, `product-details-wrapper`, both white). Card radius uses the softer 8px scale rather than the 16px button radius, since no card-specific radius variable was supplied — this mapping is inferred.

**hero** is proposed for the homepage banner area (e.g. "Discover La Foret Mawa!!") using the soft off-white surface and large display typography; no hero-specific CSS was present in evidence, so backgrounds and spacing are proposed.

**footer** is inferred to use the dark slate button color as a broader footer background for contrast, since no dedicated footer selector was supplied; this should be verified against the live site.

**badge** proposes a small pill using the observed red (#bd1313) for sale/clearance flags, a plausible but unverified role given the "Clearance" and "Factory seconds" copy in the content.

**shipping-banner** is a category-specific component modeling the "$9.95 flat rate shipping or free over $150" strip, directly matching the observed `.header-widget-region` olive-green background and white text.

## Responsive Behavior
The following breakpoints are a recommendation only; no responsive CSS or viewport behavior was present in the supplied evidence.

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, shipping banner truncates to icon + short text |
| Tablet | 600–960px | 2–3 column product grid, nav-bar may condense category mega-menu into an accordion |
| Desktop | >960px | Full mega-menu navigation, 4+ column product grid, hero at full display-xl scale |

Touch targets for buttons and nav items should be at least 44px tall. Mobile category mega-menu (Baby / Children's toys / Gifting / Brands) should collapse into an accordion-style drawer given its depth in the observed content excerpt.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no rendered layout, hover/focus states, animations, or actual responsive breakpoints were observed. The exact primary body font behind `var(--wp--preset--font-family--primary)` is inferred as Source Sans Pro from the supplied font list and common Storefront-theme defaults — it has not been confirmed against a computed style. Schoolbell's actual usage scope beyond the single gift-wrap header rule is unknown. Several palette colors (Gutenberg preset reds, purples, yellows) appear to be default WordPress block-editor swatches rather than deliberate brand colors, and were excluded from primary role assignments accordingly. Component states (hover, active, disabled, error) are entirely proposed and not observed. Font licensing/availability for Schoolbell has not been verified. Card, hero, and footer background/spacing values are inferred defaults, not measured from rendered pages.
