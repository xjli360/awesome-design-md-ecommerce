---
version: alpha
name: "Electro-Harmonix"
source_url: "https://www.ehx.com"
captured_at: "2026-09-28T05:07:31.200858+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Electro-Harmonix's storefront markup exposes a functionally monochrome working
  palette: pure black (#000000) and white (#ffffff) anchor page-header and
  post-content backgrounds, while a dark charcoal-slate (#32373c) is the actual
  rendered background of the site's default button element, making it the most
  defensible candidate for a "primary" action color despite not being a
  saturated brand hue. Surrounding this are WordPress-default utility grays
  (#eeeeee, #f5f5f5, #f8f8f8, #313131, #dddddd, #777777, #222222) used for
  section backgrounds, borders, and secondary text. A large share of the
  supplied palette (vivid red #cf2e2e, oranges, blues, greens, purples) matches
  the stock Gutenberg block-editor preset swatches rather than confirmed
  brand-specific CSS rules; these are treated here only as an occasional
  "on sale" accent (inferred) and are not promoted to primary/interactive
  roles. Typography is limited to two observed families — Rubik and Open
  Sans — with sans-serif fallback; the pairing of Rubik for display/heading
  roles and Open Sans for body copy is an inferred convention, not a
  per-selector confirmation. The resulting interpretation favors a stark,
  utilitarian black/white/gray industrial-catalog aesthetic consistent with a
  decades-old effects-pedal manufacturer, with red reserved sparingly for
  promotional signaling.

colors:
  primary: "#32373c"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-alt: "#f8f8f8"
  panel-dark: "#313131"
  panel-light: "#eeeeee"
  accent-sale: "#cf2e2e"
  border-strong: "#e0e0e0"
typography:
  display-xl: {fontFamily: "Rubik, sans-serif", fontSize: 42px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Rubik, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Rubik, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Rubik, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairlineColor: "{colors.panel-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    saleTextColor: "{colors.accent-sale}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.panel-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairlineColor: "{colors.muted}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  media-demo-card:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"

## Components

**button-primary** renders on the dark slate (`#32373c`) rule confirmed on `.wp-element-button` — the only concretely observed interactive-element color in the evidence — with white text and modest padding derived from the site's `calc(em)` spacing pattern. **button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Add to Wishlist"), unobserved but consistent with a monochrome system. **text-input** assumes a light hairline border and white fill for search/newsletter fields; exact focus/error states are not observed. **nav-bar** is inferred as a black bar given the pervasive `#000` header/background usage in page-header and post-area rules; sticky/collapse behavior is not confirmed. **product-card** models the pedal-grid tiles (`li.product`) which explicit CSS confirms as white-background elements, extended with a proposed sale-price treatment using the red delete-price rule. **hero** is a proposed full-bleed black section for the homepage "EFFECTING MUSIC. SINCE 1968." banner; exact heights and imagery are not measured. **footer** uses the dark-gray utility class background (`#313131`) confirmed elsewhere in the stylesheet as a plausible footer tone. **badge** covers "Sale!"/"New" pill labels using the Gutenberg vivid-red preset as an inferred accent, since only the generic keyword `red` was confirmed for strikethrough pricing. **search** is a proposed light-panel treatment for the header search overlay referenced in page text ("Hit enter to search"). **media-demo-card** is a category-specific proposed component for the site's "Demo Videos"/"Effectology" content, styled as a neutral card to distinguish editorial/video content from commerce tiles.

## Responsive Behavior

Recommended, not measured breakpoints: `sm` ≤480px (single-column product grid, stacked nav collapsed to a hamburger/search icon), `md` 481–768px (2-column product grid), `lg` 769–1279px (3–4 column grid, inline nav), `xl` ≥1280px (content capped near the theme's `--wp--style--global--content-size: 1300px`). Touch targets for buttons and nav items should target a minimum 44×44px hit area; the primary nav's category flyout (Pedals, By Category, News & Videos) should collapse into an accordion on mobile. This section is a proposed convention derived from the theme's max-width token, not an observed responsive audit.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only; no rendered layout, real breakpoints, hover/focus states, or JavaScript-driven product-price behavior were observed. Much of the supplied color list (vivid orange, blue, purple, teal, pink swatches) matches default WordPress Gutenberg block-editor presets rather than confirmed brand-specific styling, so only black/white/gray tones plus a single red accent were promoted into functional roles; other palette entries were intentionally omitted rather than assigned unverified roles. The Rubik/Open Sans heading-vs-body pairing is inferred from a global font-family list, not from per-selector confirmation. Rounded-corner and spacing scales are proposed conventions, since no `border-radius` or spacing-scale rules were present in the evidence. Licensing/self-hosting status of Rubik and Open Sans was not verified. Mobile menu structure, cart/checkout flows, and product-page detail layout are not observed.
