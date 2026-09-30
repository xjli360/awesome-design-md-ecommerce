---
version: alpha
name: "Monday"
source_url: "https://drinkmonday.co/"
captured_at: "2026-09-29T04:11:55.800704+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Monday (drinkmonday.co) is a direct-to-consumer storefront for zero-alcohol
  spirits — Whiskey, Gin, and Mezcal — built on a warm, editorial palette
  rather than a typical bar-brand black-and-neon scheme. The supplied CSS
  shows two anchor brand colors used specifically on header/title elements:
  a warm bronze-tan (#8b713e) paired with breadcrumb and section-header
  text, and a soft cream (#e9e4d8) used for hero titles set against a dark
  background. Body copy blocks are governed by muted charcoal tones
  (#3d4246, #434343, #000000), suggesting a restrained, legible editorial
  voice rather than saturated marketing color. Warm off-whites (#f9f8f4,
  #f4f3ed, #f2ebdd) recur across surface roles, reinforcing a natural,
  botanical-adjacent tone consistent with an alcohol-alternative spirits
  brand. Bootstrap-derived utility colors (#0d6efd, #198754, #dc3545,
  #ffc107) are present from the underlying framework/theme and are treated
  here as inferred system-state colors (info/success/error/warning) rather
  than brand expression. Typography evidence points to Graphik family
  weights (Regular/Light/Semibold) as the working sans-serif for UI and
  body copy, and Antiga-Regular as a serif display face likely reserved for
  large hero headlines ("HAVE IT ALL WITHOUT ALCOHOL"). All sizes,
  weights, and component states below are proposed interpretations unless
  explicitly tied to a supplied selector.

colors:
  primary: "#8b713e"
  ink: "#000000"
  canvas: "#f9f8f4"
  body: "#3d4246"
  muted: "#6c757d"
  hairline: "#e9ecef"
  surface-soft: "#f2ebdd"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  cream-text: "#e9e4d8"
  hero-dark: "#0a2e1f"
  gold-accent: "#c9a84c"
  ink-soft: "#434343"
  border-strong: "#cccccc"
  success: "#198754"
  danger: "#dc3545"
  warning: "#ffc107"
typography:
  display-xl: {fontFamily: "Antiga-Regular, serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Antiga-Regular, serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Graphik-Semibold, Graphik, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Graphik-Regular, Graphik, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Graphik-Regular, Graphik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Graphik-Regular, Graphik, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Graphik-Semibold, Graphik, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.hero-dark}"
    textColor: "{colors.cream-text}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  bottle-quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  footer:
    backgroundColor: "{colors.hero-dark}"
    textColor: "{colors.cream-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is proposed for primary calls to action ("Add To Cart", "Shop Monday Gin"), using the observed bronze brand color as fill with a white on-primary label; hover/active/disabled states are not observed and are proposed as darkening/opacity adjustments only.

**button-secondary** covers outline-style actions (e.g. "Explore Our Range") using the same bronze as an outline/text color on a white surface, inferred to preserve brand-color consistency without introducing an unobserved second accent.

**text-input** supports newsletter signup ("JOIN NOW") and any account/search fields; border and radius values are proposed defaults since no input-specific CSS was supplied.

**nav-bar** represents the top navigation row (Whiskey / Mezcal / Gin / Bundles / Recipes / Stores) on the light canvas background; sticky/scroll behavior is not observed and is not assumed.

**hero** models the dark, full-bleed hero band carrying headline copy such as "HAVE IT ALL WITHOUT ALCOHOL," using the hero-dark background and cream-text color pairing drawn directly from the section-header CSS rule supplying `#e9e4d8` title color.

**product-card** is proposed for grid listings of the three spirit lines (Whiskey, Gin, Mezcal), using a plain white surface with a hairline border consistent with the neutral gray tokens present in the palette (Bootstrap-derived `#e9ecef`/`#cccccc`).

**bottle-quantity-selector** is a category-specific component modeling the observed bundle-pricing UI ("1 Bottle / 2 Bottles / 3 Bottles / 6 Bottles" with per-bottle price breaks); an active/selected tier is proposed to use the primary bronze fill, since the actual selected-state styling was not present in the supplied CSS.

**footer** reuses the hero's dark/cream pairing for the site footer (Fast Links, newsletter, legal), inferred as a shared "dark band" treatment rather than confirmed via footer-specific selectors.

**badge** is proposed for promotional flags like "Save $12 + Free Shipping," using the gold-accent color as a plausible, brand-adjacent alternative to the primary bronze for secondary emphasis.

**search** is a minimal proposed pattern for a site search affordance; no search-specific selectors were present in the supplied evidence, so styling follows the general text-input conventions.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | up to 575px | Single-column stacking; nav collapses to a menu toggle; hero headline drops to `{typography.display-md}` scale. |
| tablet    | 576–991px   | Two-column product grids; nav items may wrap or condense. |
| desktop   | 992–1439px  | Full nav row visible; three-column product/bundle grids. |
| wide      | 1440px+     | Max-width content container with increased side padding (`{spacing.xxl}`). |

Touch targets are recommended at a minimum 44×44px for buttons and quantity-selector options. Navigation collapse into a hamburger/menu pattern below the tablet breakpoint is a standard convention assumption, not a measured behavior of the live site. All breakpoint values are proposed defaults for a Shopify-style storefront and are not derived from a supplied media-query.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Colors were extracted from static CSS declarations tied to Shopify theme block IDs; several rules (e.g. `.body` color overrides) returned empty values in the supplied evidence and were excluded rather than guessed.
- The bronze (`#8b713e`) and cream (`#e9e4d8`) pairing is inferred as the primary brand accent because it is the only color pair explicitly tied to header/title selectors in the evidence; this is a reasonable but not certain semantic assignment.
- Several palette entries (`#0d6efd`, `#198754`, `#dc3545`, `#ffc107`, `#20b2aa`, `#44be70`, `#be2119`) closely match Bootstrap/framework or third-party review-widget (Stamped) defaults and are mapped here only as generic state colors, not confirmed brand choices.
- No verified interaction states (hover, focus, active, disabled) were present in the supplied CSS; all such states are proposed.
- Custom font availability, licensing, and exact weight files for Graphik and Antiga were not verified; generic serif/sans-serif fallbacks are included per requirement.
- No responsive/mobile layout screenshots or media queries were supplied; the breakpoint table above is a standard recommendation, not measured site behavior.
- Typographic sizes and line-heights are proposed based on typical editorial/DTC spirits-site conventions and are not confirmed pixel measurements from the live site.
