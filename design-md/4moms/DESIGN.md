---
version: alpha
name: "4moms"
source_url: "https://4moms.com"
captured_at: "2026-09-28T10:16:52.996997+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  4moms is a Shopify-hosted storefront for high-tech baby gear (swings, bassinets,
  playards, high chairs). The observed CSS exposes a Bootstrap-derived variable set
  (--primary, --gray-lighter, --gray-dark, etc.) layered under a custom brand font,
  bc-novatica-cyr, with system-font fallbacks. Body copy renders in a warm dark gray
  (#494949) on white, with letter-spacing of .01em, suggesting a clean, legible,
  slightly technical tone appropriate to a product-engineering brand. The palette is
  large and utility-driven: a Bootstrap-style semantic set (success green, danger red,
  info cyan, warning yellow) coexists with softer brand-adjacent tones (blue, pink,
  tan, khaki) whose actual UI usage is not confirmed by the supplied evidence. This
  interpretation treats #4e85e6 (the declared --primary) as the brand accent, #212529
  and #494949 as ink/body text, and the --gray-lighter/--gray-light pair as soft
  surface and hairline colors, since these map directly to Bootstrap card/table
  patterns observed (card-header, table-striped, table-hover). Rounded and spacing
  scales are proposed conventions, not measured, chosen to fit a modern e-commerce
  layout. All semantic role assignments beyond the literal CSS variable names are
  inferred and flagged accordingly.

colors:
  primary: "#4e85e6"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#494949"
  muted: "#666666"
  hairline: "#e9ecef"
  surface-soft: "#f8f9fa"
  surface-card: "#f0f0f7"
  on-primary: "#ffffff"
  secondary: "#cccccc"
  success: "#00a465"
  danger: "#dc3545"
  info: "#17a2b8"
  warning: "#eee57a"
  indigo: "#6610f2"
  purple: "#ce00d9"
  pink: "#d885c1"
  orange: "#f48d52"
  teal: "#20c997"
  khaki: "#c0b095"
  brown: "#816960"
  tan: "#d3b69f"
  border-light: "#dcdce0"
  border-lighter: "#e9e9e9"
  border-mid: "#e2e2e2"
  gray-mid: "#737373"
  gray-dim: "#636363"
typography:
  display-xl: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "20px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0.01em"}
  body-md: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.01em"}
  body-sm: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.01em"}
  caption: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "bc-novatica-cyr, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1.5, letterSpacing: "0.01em"}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-light}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripeColor: "{colors.surface-soft}"
    hoverColor: "{colors.border-mid}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
- **button-primary** — proposed as the primary call-to-action treatment (Shop, Add to Cart), using the declared `--primary` blue with white text; hover/active states are not observed and would need runtime verification.
- **button-secondary** — an outline variant proposed for lower-emphasis actions (e.g., "Get Support"), reusing primary blue as text/border on a white fill.
- **text-input** — a light-bordered field styled from the `--gray-light` hairline token; focus-ring color is not confirmed in the supplied CSS and is left unspecified here.
- **nav-bar** — inferred from body/header structure (white background, dark ink text) since no explicit header selector was supplied; search icon and cart count are present in page text but not styled here.
- **product-card** — proposed pattern for gear listings (swings, bassinets, playards), using the `--gr1` (#f0f0f7) soft surface as a card background with a light border, appropriate for a product grid.
- **hero** — a large banner treatment using the soft gray surface and the display-xl type scale; suited to the "New Chapter" UPPAbaby-family announcement banner referenced in page text, though its actual visual form is not observed.
- **footer** — proposed as a dark/ink-toned band per common e-commerce convention; the supplied CSS does not confirm footer background color, so this is a stylistic proposal, not an observation.
- **badge** — a small pill using the success green, proposed for stock/shipping messaging (e.g., "Free shipping over $70"); color choice is inferred from the semantic `--success` variable.
- **search** — a soft-surface input field for the site search referenced in page text ("Search Search Search").
- **spec-table** — directly grounded in observed `.table-striped` and `.table-hover` rules (stripe via `rgba(0,0,0,.05)`, hover via `rgba(0,0,0,.075)`), proposed for product spec/comparison tables common to a gear-and-playmats catalog.

## Responsive Behavior
The following breakpoints are a recommendation based on the Bootstrap-style variables observed (`--breakpoint-sm:576px; --breakpoint-md:768px; --breakpoint-lg:992px; --breakpoint-xl:1200px; --breakpoint-xxl:1480px`), not measured live layout behavior:

| Breakpoint | Width | Nav behavior (proposed) | Grid (proposed) |
|---|---|---|---|
| xs | <576px | Hamburger/collapsed nav | 1-column product grid |
| sm | ≥576px | Collapsed nav, larger touch targets | 1–2 column grid |
| md | ≥768px | Nav may expand partially | 2-column grid |
| lg | ≥992px | Full horizontal nav | 3-column grid |
| xl/xxl | ≥1200–1480px | Full nav, wider content max-width | 3–4 column grid |

Touch targets should target a minimum 44px hit area for buttons and nav icons (per the observed `.znt-pause-gif_button` 44px sizing). Mobile nav collapse and menu interaction states are not observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- All colors listed are pulled directly from supplied CSS variables/palette, but their assignment to specific UI roles (nav, footer, badges) is inferred, not confirmed by rendered screenshots.
- Font sizes, weights (beyond the observed `1rem`/`400` body and the presence of a Bold cut of `bc-novatica-cyr`), and letter-spacing at display/title scales are proposed, not measured.
- No hover, focus, active, or disabled states were present in the supplied CSS; all interaction states are proposed conventions.
- Mobile/responsive layout, nav collapse behavior, and grid column counts are not observed; the breakpoint table uses only the declared `--breakpoint-*` variable values.
- Licensing and web-font delivery details for `bc-novatica-cyr` (a proprietary/custom font referenced by name only) are not verified; system fallbacks are included per the observed `font-family` stack.
- Rounded and spacing scales are conventional proposals, not derived from measured border-radius or margin/padding values in the supplied CSS.
