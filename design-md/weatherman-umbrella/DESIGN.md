---
version: alpha
name: "Weatherman Umbrella"
source_url: "https://weathermanumbrella.com"
captured_at: "2026-09-28T09:13:28.672999+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Weatherman Umbrella is a Shopify-built DTC storefront for storm-tested umbrellas,
  ponchos, sun shirts and rain accessories, fronted by Chief Meteorologist Rick
  Reichmuth. The observed CSS exposes a small functional palette rather than a
  broad brand system: a saturated orange (#ef4e23) drives primary button and
  outline states across templates, while a teal (#00a9b1) governs the active
  text-field background and text color, suggesting it is reserved for search or
  form focus states rather than primary CTAs. Neutrals run from near-black
  (#121212, #000000) through mid grays (#6e6968, #8e8e8e) to off-white surfaces
  (#f9fafb, #fafafa, #f1efed), consistent with a light canvas storefront using
  gray-scale cards and hairlines for separation. Two additional blues
  (#1990c6, #136f99) appear without a clear role and are treated here as
  secondary/link accents (inferred). Font stacks list Barlow, Lexend, Noto Sans,
  Roboto and "untitled sans" alongside system fallbacks; since no selector-level
  mapping was supplied, this spec infers "untitled sans" for display/heading use
  and Barlow for body/UI text, both flagged as unverified pairings. The resulting
  interpretation favors a clean, weather-utility aesthetic: bold orange calls to
  action, muted gray body copy, and generous whitespace implied by the observed
  section-spacing custom properties.

colors:
  primary: "#ef4e23"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#1f2937"
  muted: "#6e6968"
  hairline: "#eaeaea"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-teal: "#00a9b1"
  accent-blue: "#136f99"
  accent-blue-alt: "#1990c6"
  sale-soft: "#fbd3d1"
  border-strong: "#d1d5db"
  sold-out-bg: "#eeeeee"
typography:
  display-xl: {fontFamily: "'untitled sans', sans-serif", fontSize: 60px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'untitled sans', sans-serif", fontSize: 44px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "'untitled sans', sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.accent-teal}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "linear-gradient(180deg, rgba(0,0,0,0) 33%, rgba(0,0,0,0.4) 100%)"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    saleBackground: "{colors.primary}"
    saleText: "{colors.on-primary}"
    soldOutBackground: "{colors.sold-out-bg}"
    soldOutText: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.accent-teal}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  weather-spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.accent-blue}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** is inferred from the `--button-background: 239 78 35` / `--button-text-color: 255 255 255` custom properties observed on collection and hero sections; it is proposed as the storefront's default add-to-cart and "Shop Gear" call-to-action.

**button-secondary** is a proposed outline treatment for secondary actions (e.g. "Choose options" alternates); no outline CSS was directly captured, so its border/ink pairing is inferred from the neutral palette.

**text-input** reuses the only observed form-state variables (`--text-field-background`, `--text-field-text-color: #00a9b1`), which strongly suggest a teal-tinted input/search field; exact border and focus-ring behavior are proposed.

**nav-bar** reflects the observed sticky header (`--header-is-sticky: 1`, `--header-padding-block`, `--header-logo-width`) and mega-menu structure (Shop, Explore, Support, Bundles); color values are proposed since no header background hex was directly listed beyond white canvas defaults.

**product-card** is a proposed pattern for the "Just in & Trending" grid (Stride Poncho, Puddle Jumper listings); card surface, hairline and radius are inferred from the neutral off-white palette, not measured directly.

**hero** models the homepage banner ("Rain? Keep Moving.") using the captured `content-over-media-gradient-overlay` gradient, applied over an inferred dark ink background since no hero background color was explicitly listed.

**footer** and its muted-gray-on-soft-surface treatment are proposed; the palette supplies plausible neutral candidates but no footer-specific selector was captured.

**badge** consolidates observed sale/sold-out state variables (`--sold-out-badge-background: 239 239 239`, on-sale styling) mapped to the closest supplied hex equivalents, since exact on-sale hex (227 44 43) fell outside the provided palette array.

**search** and **weather-spec-badge** are proposed, category-appropriate components: search reuses the teal text-field tokens; weather-spec-badge is designed for the site's "Wind-Proof Tested to 55 mph / UV Protective / 100% Recycled Canopy" feature callouts, using pill shape and a secondary blue accent inferred from the unused `#1990c6`/`#136f99` swatches.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column hero, stacked nav, collapsed mega-menu into drawer |
| Tablet | 640–1024px | 2-column product grid, condensed header padding |
| Desktop | >1024px | Full mega-menu grid (`logo primary-nav secondary-nav`), 3–4 column product grid |

Touch targets should target a minimum 44×44px hit area for nav, cart, and account icons. Mega-menu items should collapse to an accordion drawer below tablet width. This table is a recommendation derived from the observed CSS grid/container variables (`--header-grid`, `--container-gutter`), not measured live responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS custom properties and page text only; no rendered layout, hover/focus states, or breakpoint behavior were directly observed.
- Font-to-role mapping (headings vs. body) is inferred; "untitled sans" and Barlow roles are unverified guesses based on stack ordering, and licensing/availability of "untitled sans" was not confirmed.
- Several palette entries (accent-blue, accent-blue-alt, sale-soft) have no confirmed selector role and are assigned speculatively to secondary/accent components.
- Exact on-sale badge color (`227 44 43`) was referenced in CSS but not present in the supplied hex array, so primary orange was substituted as the nearest available token.
- Spacing and radius scales follow the requested standard template values rather than site-measured pixel values, since no border-radius properties were present in the supplied evidence.
- Mobile menu, cart drawer, and account page visuals were not captured and are entirely proposed.
