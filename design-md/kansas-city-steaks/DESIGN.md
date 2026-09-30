---
version: alpha
name: "Kansas City Steaks"
source_url: "https://kansascitysteaks.com"
captured_at: "2026-09-29T03:56:34.881392+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Bootstrap-based CSS variables and a broad
  observed color palette on kansascitysteaks.com, an e-commerce storefront for
  steak, seafood, and gift-pack delivery. The confirmed typography stack sets
  body copy in "Roboto", with "Roboto Condensed" and "Roboto Slab" declared as
  alternate font variables (--font-alt1, --font-alt2), suggesting condensed
  type for navigation/labels and a slab serif for display headings—an
  inference from the CSS variable naming, not a captured heading render.
  Other font families present in the source (ArcherPro-Bold, EngraversMT,
  gotham-light/medium, tablet-gothic) appear in the evidence font list but are
  not tied to specific selectors here, so they are treated as unconfirmed and
  excluded from primary tokens.
  The palette is dominated by warm cream/tan surfaces (#fef9ed, #ede2c8,
  #bfa465) paired with a dark red (#ad0b21) that reads as the brand's call-to-
  action color, alongside near-black ink (#231f20) and Bootstrap's default
  grays for utility text and borders. This mapping proposes a butcher-shop-
  meets-catalog aesthetic: warm neutral canvas, deep red accents for urgency
  (sales, badges), and slab-serif display type for a premium, traditional
  steakhouse feel. All semantic role assignments below are inferred from
  observed values, not verified live renders.

colors:
  primary: "#ad0b21"
  primary-hover: "#9a001a"
  ink: "#231f20"
  canvas: "#faf9f7"
  body: "#212529"
  muted: "#605255"
  hairline: "#dddddd"
  surface-soft: "#fef9ed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#bfa465"
  accent-tan: "#ede2c8"
  success: "#00610b"
  error: "#dc3545"
  warning: "#f5a623"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "'Roboto Slab', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Roboto Slab', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0.25px}
  body-md: {fontFamily: "'Roboto', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Roboto', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "'Roboto', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.display-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  savings-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** is proposed for primary conversion actions ("Add To Cart", "Shop Now"), using the observed dark red as background with white text for contrast; hover/active states are not observed and would proportionally darken the fill.

**button-secondary** is an outlined variant for tertiary actions (e.g., "View More Details") sharing the primary red as text/border color on a white surface, proposed for lower-emphasis interactions alongside primary buttons.

**text-input** covers search and form fields, using a light hairline border and card-white background; focus-ring styling is not observed and is left as a proposed enhancement.

**nav-bar** represents the top utility/category navigation implied by the extensive "SHOP BY CUT" / "SEAFOOD" menu structure in the evidence; a white background with condensed bold labels is proposed for a dense multi-category menu, though exact height and collapse behavior are not observed.

**product-card** models the repeated product tiles seen in the evidence (e.g., "The Dinner Bell™", "Classic Cuts Trio Sampler"), pairing a slab-serif price treatment with condensed titles on a white card with light border, per catalog conventions.

**hero** is a proposed promotional banner component for top-of-page merchandising (e.g., "End of Summer Sale"), using the cream surface tone as a warm, appetite-appropriate background distinct from stark white.

**footer** proposes a dark ink background with white text for brand closure and trust content (phone number, policies), following the ink/on-primary contrast pair observed in the palette.

**badge** is a small pill-shaped label for merchandising flags (e.g., "Top Gift", "USDA Prime"), using the tan/gold accent to differentiate from the red urgency badge below.

**search** proposes a compact input embedded in the nav-bar, consistent with the "Search" control referenced in the page text.

**savings-badge** is a category-appropriate component for the frequent "Save $X" / percent-off callouts seen throughout the evidence (e.g., "Save $120.00"), using the primary red for urgency and immediate scannability against product pricing.

## Responsive Behavior

| Breakpoint | Width (proposed, from Bootstrap vars) | Layout Guidance |
|---|---|---|
| xs | 0px | Single-column stacked cards, collapsed nav behind a menu toggle |
| sm | 768px | Two-column product grid, inline search reveal |
| md | 992px | Three-column product grid, full horizontal nav |
| lg | 1200px | Four-column grid, expanded mega-menu categories |
| xl | 1400px+ | Max-width content container, generous section padding |

Touch targets should be at least 44px in the compact/xs range for cart and nav controls. Mega-menu category groups (Steaks, Seafood, Sides & Extras, Gifts) are recommended to collapse into an accordion below the `sm` breakpoint. This table is a recommendation derived from the `:root` breakpoint variables in the CSS, not measured or observed responsive behavior of the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS variable declarations and a flat color/font list, not a rendered or interactive capture of kansascitysteaks.com. Specific gaps: (1) exact heading font usage is inferred from `--font-slab`/`--font-alt1` variable names rather than a captured heading render; (2) fonts ArcherPro-Bold, EngraversMT, gotham-light/medium, and tablet-gothic appear in the evidence font list but have no associated selector, so their actual usage (e.g., in the logo or print materials) is unconfirmed and excluded from tokens; (3) all pixel sizes, spacing, and radius values are proposed defaults, not measured from layout; (4) hover, focus, active, and error interaction states are not observed and are labeled proposed; (5) mobile/tablet menu collapse behavior is inferred from Bootstrap breakpoint variables only, not observed rendering; (6) licensing and availability of any named custom fonts have not been verified.
