---
version: alpha
name: "Extreme Terrain"
source_url: "https://extremeterrain.com"
captured_at: "2026-09-28T04:30:38.547514+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  ExtremeTerrain's observed CSS points to a utilitarian, catalog-driven storefront built around a single olive-green brand accent (#738537, with a deeper variant #4c5f1b used on light buttons) set against neutral grays and near-black text (#212121). Promotional buttons introduce a secondary orange (#e83d00) and a caution yellow (#ffce3e), both tied to hover/pressed states on marketing CTAs, suggesting a layered accent system: green for primary brand actions, orange/yellow for urgency and secondary promos. Typography mixes "Inter" for pricing figures, "Roboto Flex" for buttons and marketing headers, and an Arial/Helvetica Neue/Lucida Grande stack presumably for default body copy where no webfont is declared. Card-level UI (fitment text, review counts, badges) relies on small 12px gray labels (#797979) against white/off-white card surfaces (#ffffff, #edeeee), implying a dense, information-forward product grid typical of parts catalogs. Rounded pill badges (border-radius:100px) and 4px button corners are the only radius values directly observed. This interpretation proposes a cohesive scale around these fragments; exact layout, spacing rhythm, and most typographic sizes beyond the ones cited are inferred, not measured.

colors:
  primary: "#738537"
  brand-deep: "#4c5f1b"
  accent-caution: "#ffce3e"
  accent-alert: "#e83d00"
  ink: "#212121"
  body: "#58595b"
  muted: "#797979"
  hairline: "#e2e5e7"
  surface-soft: "#f4f4f4"
  surface-card: "#edeeee"
  canvas: "#ffffff"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: '"Roboto Flex", sans-serif', fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: '"Roboto Flex", sans-serif', fontSize: 28px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: '"Roboto Flex", sans-serif', fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: 'Arial, "Helvetica Neue", Helvetica, sans-serif', fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: 'Arial, "Helvetica Neue", Helvetica, sans-serif', fontSize: 12px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  caption: {fontFamily: 'Arial, "Helvetica Neue", Helvetica, sans-serif', fontSize: 12px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.2px}
  button-md: {fontFamily: '"Roboto Flex", sans-serif', fontSize: 16px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0px}
  price-lg: {fontFamily: '"Inter", sans-serif', fontSize: 18px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
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
    textColor: "{colors.brand-deep}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-lg}"
    mutedTypography: "{typography.caption}"
    mutedColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    ctaBackground: "{colors.primary}"
    titleTypography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** reflects the marketing CTA pattern (`.main_btn`) with an olive-green fill, white text, and Roboto Flex bold labels; padding and no-shadow styling are directly observed, while corner radius is proposed since no explicit `border-radius` was captured on this exact rule.

**button-secondary** is inferred from `.top_finds_buttons a`, which sits on a white background with brand-deep green text and a 4px radius — treated here as the outline/secondary counterpart to the solid primary button.

**text-input** has no direct CSS evidence; it is a proposed pattern using the site's neutral hairline and body typography so forms (email signup, search) stay visually consistent with card and button styling.

**nav-bar** is proposed. No header/navigation selectors were present in the supplied CSS; the pattern assumes a white bar with dark ink text and a light hairline division, consistent with the rest of the light-canvas UI.

**product-card** is grounded in `.product_container` rules: a muted 12px fitment/count label in gray, a bold 18px Inter price, and a strikethrough original-price treatment. Card background and radius are proposed since container-level box styling wasn't shown.

**hero** draws on `.marketing_initiative_v2 .hero_container`, which hosts a ghost/ solid button pair and Roboto Flex heading text; background darkness and exact padding are proposed extrapolations from a promo-banner pattern, not measured.

**footer** is fully proposed — no footer selectors were in evidence — modeled on the dark/ink surface used elsewhere for contrast blocks, with small body-sm text for legal/link columns.

**badge** generalizes the `.wheel_tire_kit_badge` pill (gray fill, white text, fully rounded, small bold caption) into a reusable status/label chip for stock, kit, or clearance flags.

**search** is proposed, using the soft-gray surface token to differentiate an input affordance from card and page backgrounds without introducing an unobserved color.

**fitment-selector** is a category-specific, proposed component: off-road parts sites typically require a Year/Make/Model vehicle picker above the fold. It borrows the soft surface, primary accent, and small body typography already established, but its existence/layout on ExtremeTerrain was not confirmed in the supplied evidence.

## Responsive Behavior

This is a recommended pattern, not measured site behavior — no media queries or breakpoint values were present in the supplied CSS.

| Breakpoint | Width      | Layout guidance |
|---|---|---|
| mobile | up to 599px | Single-column product grid; fitment-selector collapses into a full-width modal/drawer; nav collapses to a hamburger + search icon. |
| tablet | 600–1023px | Two-column product grid; hero CTA stacks text over button row. |
| desktop | 1024–1439px | Multi-column (3–4) product grid; persistent top nav with inline search. |
| wide | 1440px+ | Same as desktop with additional max-width container and increased gutter (`{spacing.xl}`). |

Touch targets should be at least 40px in height, matching the observed `.top_finds_buttons a` button height. Badges and caption text remain small (12px) and are not intended as tap targets themselves — wrap them in adequately sized touch areas on mobile.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static bundled CSS only; no rendered page, DOM structure, or breakpoint/media-query data was available, so all responsive behavior above is a proposal.
- Several color-to-role mappings (hairline, surface-soft, surface-card, body) are inferred from generic gray/near-white values in the palette without a corresponding named selector confirming that exact role.
- Font sizes for display-xl, display-md, title-md, body-md, and caption are proposed; only the 12px/16px/18px sizes tied to price, button, and header rules were directly observed.
- No navigation, footer, form input, or search-bar selectors were present in the supplied CSS; those components are structurally proposed based on category conventions, not verified against the live site.
- The fitment-selector component assumes a Year/Make/Model vehicle picker common to off-road parts retailers; its presence and styling on ExtremeTerrain were not confirmed in the evidence.
- "Roboto Flex" and "Inter" font availability, self-hosting/licensing, and fallback rendering were not verified beyond their appearance in CSS `font-family` declarations.
- Interaction states (hover/focus/active) beyond the few `:hover`/`:focus` rules supplied (e.g., catalog_request buttons) are otherwise unconfirmed and marked proposed where used.
