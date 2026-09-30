---
version: alpha
name: "The Honest Kitchen"
source_url: "https://thehonestkitchen.com"
captured_at: "2026-09-28T09:02:55.235790+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Honest Kitchen's storefront theme (Shopify, evidenced by theme.BpMpUrW1.asset.min.css) pairs a warm,
  food-safe palette with a condensed display typeface. Observed CSS variables define --primary-font: Graphik
  Regular for body copy, --heading-font: Publish Gothic Condensed for headings, and --accent-font: Golden
  Plains, a script face reserved for occasional flourish copy (inferred use, not confirmed on-page).
  From the supplied palette, warm off-whites (#f9f8f4, #fbf7f1, #f2e7d4) are interpreted as canvas and
  card surfaces, appropriate to a "human grade, real food" positioning, while near-black (#1f1f1f) and
  dark gray (#303030) serve as ink and body text. A saturated berry-red (#bf0d3e, deepening to #950a30 on
  hover states) is treated as the primary brand accent, consistent with the emphasis on urgency (sale
  banners, CTAs) in the page text; a muted rose (#d96e8b) and warm gold (#e39d4d) are proposed as
  secondary accents for badges and diet-claim callouts (No Wheat/No Corn/No Soy/No GMO). Several palette
  entries (e.g. #0b57d0, #a8c7fa, #f0f4f9) resemble a third-party Google UI component rather than brand
  color and are excluded from role assignment. Rounding and button geometry follow the theme's own
  --rounding-buttons: 0.5rem token.

colors:
  primary: "#bf0d3e"
  primary-hover: "#950a30"
  ink: "#1f1f1f"
  canvas: "#f9f8f4"
  body: "#303030"
  muted: "#6b7280"
  hairline: "#dedede"
  surface-soft: "#f2e7d4"
  surface-card: "#fbf7f1"
  on-primary: "#ffffff"
  accent-gold: "#e39d4d"
  accent-rose: "#d96e8b"
  border: "#cccccc"
  disabled: "#9ca3af"
typography:
  display-xl: {fontFamily: "'Publish Gothic Condensed', sans-serif", fontSize: 64px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Publish Gothic Condensed', sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  display-accent: {fontFamily: "'Golden Plains', cursive", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Publish Gothic Condensed', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Graphik Regular', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Graphik Regular', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Graphik Regular', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Graphik Regular', sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.on-primary}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "5.75rem"
    hairline: "{colors.hairline}"
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
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.on-primary}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  diet-claim-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
- **button-primary**: The dominant call-to-action treatment (e.g. "Shop All," "Take Quiz"), using the berry-red accent from `.btn-primary` CSS with an inferred darker hover state (`primary-hover`) consistent with the `color-mix(...black 40%)` hover rule observed in the theme stylesheet.
- **button-secondary**: An outline variant proposed for lower-emphasis actions ("Learn More," "Find a Store"), sharing the primary's border color but with a transparent/canvas fill; hover and disabled states are proposed, not observed.
- **text-input**: Used for email capture ("Send us your email") and site search; light background with a hairline border, matching the button's 0.5rem corner radius token for visual consistency.
- **nav-bar**: A fixed-height header (5.75rem, per `--nav-height`) housing logo, primary shop links (Shop Dog/Cat/Treats), and utility icons; sits above an announcement carousel per the page text.
- **product-card**: Proposed grid tile for recipe/product listings (Clusters, Dry Food, Treats, Toppers), pairing a condensed title with body-weight pricing and a soft card background for separation from the cream page canvas.
- **hero**: Full-width promotional banner combining the display heading font with a warm surface tint, used for seasonal offers ("Fall Into Savings," "Up to 40% Off").
- **footer**: Dark, high-contrast footer block gathering Company/Support link columns and legal text, inverting the palette (dark background, light text) for visual closure at page end.
- **badge**: A rounded pill for promotional or nutrition callouts (e.g. "New!", sale percentages); gold fill chosen from palette to differentiate from red CTAs.
- **search**: A pill-shaped input proposed for header/product search, unobserved in provided markup but conventional for this theme family.
- **diet-claim-tag**: Category-specific component for the brand's recurring ingredient-exclusion messaging (No Wheat, No Soy, No GMO, No Corn); an outlined tag pattern keeps these claims legible without competing with primary CTAs.

## Responsive Behavior
| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| Mobile     | <640px      | Single-column stacking; nav collapses to hamburger; `--fs-xl` drops to the 2rem mobile value seen in CSS. |
| Tablet     | 640–1024px  | Two-column product grids; carousels retain swipe affordance. |
| Desktop    | >1024px     | Full nav bar (5.75rem height) with multi-column hero and shop-by-format grids. |

Touch targets should meet the theme's own `--touch-target-size` tokens (32px baseline, 44px on touch devices, per CSS). This table is a recommendation based on token evidence, not measured breakpoint behavior on the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Color-role assignments (primary accent, surface tiers) are inferred from a static palette dump; no rendered screenshots were available to confirm actual usage context.
- Several supplied hex values (e.g. `#0b57d0`, `#a8c7fa`, `#f0f4f9`, `#8e918f`) resemble a third-party Google UI/Material component rather than brand styling and were deliberately excluded from role mapping.
- Golden Plains and Publish Gothic Condensed are referenced by CSS variable name only; font licensing, weights, and full character support were not verified.
- Spacing and rounded scales beyond the observed `0.5rem` button/general radius are proposed conventions, not extracted values.
- No interaction states (focus rings, form validation, cart drawer, mobile nav animation) were observed; all such behavior is proposed and unverified.
- Mobile layout, carousel mechanics, and actual grid column counts were not confirmed via rendered DOM inspection.
