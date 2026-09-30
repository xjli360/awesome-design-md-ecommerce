---
version: alpha
name: "Burt's Bees for Pets"
source_url: "https://burtsbeesforpets.com"
captured_at: "2026-09-28T10:13:14.192955+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from a small set of global CSS rules and a
  supplied color/font inventory for burtsbeesforpets.com, a Wix-built
  storefront for the Burt's Bees for Pets grooming line. The base stylesheet
  sets body typography to Arial/Helvetica with a sans-serif fallback, while
  the broader font inventory includes Poppins (regular, semibold,
  extralight) and Madefor Display/Text weights, indicating a Wix site-builder
  environment where multiple font families are loaded but only a subset are
  likely used for on-page headings versus body copy. No component-level
  typography or spacing was directly observed beyond a reset-button utility
  and a generated Stylable button class, so this document proposes a
  restrained, brand-plausible system rather than claiming measured styles.
  The palette is taken directly from supplied hex values: a warm red
  (#db1734) is assigned as primary/accent, near-black and white anchor
  ink/canvas, and a warm brown (#5e514d) is proposed as body-text tint to
  echo the brand's "naturally derived" positioning. Additional supplied hues
  (yellow, pink, blues, rust) are retained as secondary accent options.
  Layout, spacing, and interaction patterns below are inferred conventions
  for a grooming/pet-care e-commerce site, not confirmed observations.

colors:
  primary: "#db1734"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#5e514d"
  muted: "#757575"
  hairline: "#5f6360"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffd203"
  accent-pink: "#ed1566"
  accent-blue: "#116dff"
  accent-blue-soft: "#5e97ff"
  accent-rust: "#9e3b1b"
  overlay: "#00000099"
  transparent: "#00000000"
  deep: "#080808"
typography:
  display-xl: {fontFamily: "poppins-semibold, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "poppins-semibold, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "poppins, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "poppins-semibold, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xl}"
    hairline: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.base}"
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    accentColor: "{colors.accent-yellow}"

## Components

**button-primary** is proposed as the main call-to-action treatment (e.g. "Shop Now"), using the observed red (#db1734) as background with white text; hover/active states were not observed and are proposed as slightly darkened variants.

**button-secondary** offers an outlined alternative for lower-emphasis actions such as "Learn More," reusing the primary red as border/text color on a white canvas — a proposed pattern, not confirmed from CSS.

**text-input** covers search and form fields (e.g. wholesale contact forms), styled with a light hairline border and minimal rounding consistent with a clean, utilitarian Wix-site aesthetic; no focus-state styling was observed.

**nav-bar** represents the top navigation seen in page text ("COLLECTIONS SHOP CONTACT US WHOLESALE"), rendered on a white background with dark text and a bottom hairline; sticky/scroll behavior is inferred, not measured.

**product-card** is proposed for grooming-product listings in the Collections/Shop views, pairing a title in the mid-weight Poppins style with body-weight pricing text inside a lightly bordered, rounded container.

**hero** models the homepage/collections intro area referencing "by nature. for nature. for all.", using large display typography over a soft surface background; exact hero imagery and layout were not observed.

**footer** reflects the visible footer links (FAQs, Terms & Conditions, Privacy Policy, Contact Us, Wholesale) on a near-black background (#080808) with light text, a common dark-footer pattern inferred for contrast, not confirmed via footer-specific CSS.

**badge** is a proposed small label (e.g. "Cruelty-Free" or "Natural") using the observed yellow accent as a pill-shaped highlight, since no dedicated badge markup was present in the supplied evidence.

**search** proposes a pill-shaped search field for the Shop section, consistent with the rounded, friendly tone suggested by the brand copy; not directly observed in the CSS excerpt.

**ingredient-callout** is a category-appropriate component surfacing claims from the page text (no phthalates, parabens, sulfates, dyes), using a soft surface with a yellow accent to echo the brand's naturally-derived messaging; purely a proposed content pattern.

## Responsive Behavior

The following breakpoints are a **recommendation only**, not measured from the live site:

| Breakpoint | Width      | Notes                                   |
|-----------|------------|------------------------------------------|
| Mobile    | 0–479px    | Single-column stack, nav collapses to menu icon |
| Tablet    | 480–1023px | Two-column product grids, nav may remain inline or collapse |
| Desktop   | 1024px+    | Multi-column grids, full inline nav      |

Touch targets should target a minimum of 44×44px for buttons and nav items. Navigation collapse into a hamburger/drawer pattern below tablet width is a common Wix-site convention and is proposed here, not confirmed via the supplied CSS (only a generic `:root` viewport-unit setup and a reset-button utility were present, with no explicit media queries supplied).

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence consisted of a small CSS rule sample (body, `:root`, `.reset-button`, and one generated Stylable button class) plus a raw color and font-family list; no full stylesheet, computed layout, or DOM structure was available.
- Semantic color roles (primary, ink, canvas, muted, hairline, surface-soft/card) are inferred assignments from the supplied hex list; the source CSS did not label these roles explicitly.
- Typography sizes, weights, letter-spacing, and line-heights in the `typography` block are proposed values for a plausible grooming e-commerce hierarchy; only the font-family tokens themselves (Arial, Helvetica, Poppins variants, Madefor variants) are observed, and only Arial/Helvetica/Poppins variants were used here to satisfy exact-match requirements.
- Component definitions (button-secondary, text-input, nav-bar, product-card, hero, footer, badge, search, ingredient-callout) are proposed UI patterns appropriate to a pet-grooming storefront; none reflect confirmed selectors or verified interaction states (hover, focus, active, disabled) beyond the generic Stylable button variable hooks noted in evidence.
- Responsive breakpoints and mobile/collapse behavior were not observed and are stated as recommendations.
- Availability and licensing of the Madefor and Poppins font families for production use were not verified from the supplied evidence.
