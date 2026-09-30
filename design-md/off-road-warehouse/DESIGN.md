---
version: alpha
name: "Off Road Warehouse"
source_url: "https://offroadwarehouse.com"
captured_at: "2026-09-28T10:19:38.129615+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Off Road Warehouse's storefront runs on a Magento-based theme with Tailwind
  utility classes layered on top. The only strongly attested brand color is
  the CSS custom property `--primary: #ed1c24`, a saturated red used for
  primary buttons and add-to-cart actions, paired with `--secondary: #e7e7e7`
  and `--tertiary: #000`. Surrounding UI chrome (grays, borders, muted text)
  comes from a Tailwind gray scale (#111827, #6b7280, #e5e7eb, #f3f4f6) that
  is typical of utility-first builds rather than confirmed brand identity —
  these are treated as inferred structural neutrals. Barlow is the only
  proprietary-feeling font actually observed in CSS, applied to h1 headings
  at 700 weight; body copy falls back to system sans-serif stacks (Roboto,
  Helvetica Neue, Arial), so body typography is inferred from stack order,
  not a confirmed brand font choice.

  The interpretation leans into a rugged, utilitarian parts-catalog feel:
  bold red CTAs on neutral gray/white surfaces, uppercase button labeling
  (observed via `text-transform: uppercase` on `.btn` and pagebuilder
  buttons), and a dense e-commerce layout suited to fitment-driven shopping
  (year/make/model selection, category grids, product cards with hover
  states). All measurements not explicitly present in supplied CSS are
  marked proposed.

colors:
  primary: "#ed1c24"
  ink: "#111827"
  canvas: "#ffffff"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#e7e7e7"
  tertiary: "#000000"
  link: "#2563eb"
  accent-yellow: "#fae703"
  border-strong: "#000000"
typography:
  display-xl: {fontFamily: "Barlow, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.0, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.title-md}"
  hero:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.border-strong}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the site's actual `--primary` red (`#ed1c24`) with white text, matching the observed `.btn.btn-tocart` and `pagebuilder-button-primary` rules; uppercase text-transform and bold weight are observed CSS behaviors carried into `typography.button-md`.

**button-secondary** is an outlined variant using the same red for border and text on a transparent fill, inferred from the `.action.secondary` pattern where `--btn-color` and `--btn-border` both resolve to `var(--primary)`; hover-to-filled states referenced in CSS (`--btn-hover-bg: var(--primary)`) are proposed for interactive states not directly observed.

**text-input** is a proposed pattern for search and account forms, using neutral hairline borders and canvas background consistent with the surrounding gray/white palette; no explicit input CSS was supplied, so sizing and radius are inferred defaults.

**nav-bar** represents the top utility/account bar and category menu implied by page text ("Shop By Category," "My Account," "Sign In"); white background with dark text is inferred from the absence of a dark header rule in supplied CSS.

**product-card** models the catalog grid tiles referenced by `.product-item` and `.group-hover:scale-125` hover-zoom behavior on product images; the `.product-item:hover .btn-tocart` rule confirms a color-invert hover treatment (black background, white text) worth noting as an observed interaction, though its full visual context is not verified.

**hero** is a proposed full-bleed promotional band using the black (`--tertiary`) backgrounds seen in multiple `[data-pb-style]` page-builder blocks (`background-color:#000`), consistent with dark hero/banner sections typical of the "Let Us Build the Package" promotional copy.

**footer** reuses the black/white contrast pattern from page-builder blocks, housing the observed link groups (Company, Support, Sales Contact) in the page text; link coloring uses the light `--secondary` gray for reduced-emphasis navigation.

**badge** is a proposed sale/promo tag using the bright yellow (`#fae703`) found in the palette, appropriate for price-match or clearance callouts referenced in page text ("Price Match. Contact Us!"); this color's actual UI role was not confirmed in supplied CSS.

**search** models the header search field implied by page text ("Search"), styled with a soft gray background for visual separation from the white nav bar.

**vehicle-fitment-selector** is a category-appropriate component for the Year/Make/Model widget explicit in the page text and evidence (extensive year dropdown list, "Select Vehicle," "Vehicle Make," "Vehicle Model"); it uses the primary red as an accent for the active/selected state, proposed since no dedicated selector CSS was supplied.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Layout notes (proposed) |
|-----------|-------------|--------------------------|
| mobile    | <640px      | Single-column product grid, collapsed hamburger nav, sticky vehicle-selector bar |
| tablet    | 640–1024px  | 2–3 column product grid, condensed nav with icon-only account/cart |
| desktop   | 1024–1440px | Full nav bar, 4-column product grid, persistent vehicle selector in header |
| wide      | >1440px     | Max-width content container, unchanged grid density with increased gutters |

Touch targets for buttons and nav items should target a minimum 44px height, consistent with `.btn` padding scale (`{spacing.md} {spacing.lg}`). Mobile category and account menus are assumed to collapse into a slide-out or accordion pattern; this is a UX recommendation only, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/HTML text; no rendered screenshots, computed styles, or live interaction states were captured.
- Semantic color roles (ink, body, muted, hairline, surface-soft) are inferred from generic Tailwind-style gray hex values and are not explicitly labeled as brand colors in source CSS.
- Hero, footer, and badge visual treatments are proposed compositions built from fragments of `[data-pb-style]` block rules and general palette availability, not confirmed full-page layouts.
- Typography sizes for `display-xl`, `display-md`, `body-sm`, and `caption` are proposed scale extrapolations; only the `h1`/`.h1` rule (Barlow, 700, 28px) was directly observed.
- Hover, focus, active, and disabled states beyond the documented `.btn-tocart` hover and pagebuilder disabled shadow reset were not observed and are marked proposed where used.
- Mobile/tablet navigation collapse behavior, menu interactions, and vehicle-selector widget behavior were not observed in supplied evidence; breakpoints are standard recommendations only.
- Font licensing and self-hosting/availability of Barlow were not verified; fallback to system sans-serif stacks should be assumed until confirmed.
