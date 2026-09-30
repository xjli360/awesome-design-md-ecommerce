---
version: alpha
name: "Chicco"
source_url: "https://chiccousa.com"
captured_at: "2026-09-28T09:57:31.132552+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from Chicco USA's Bootstrap-derived design tokens and page CSS.
  The root stylesheet defines a neutral, utilitarian palette: dark ink (#2f333a) as primary text and
  brand-primary role, a warm red-orange (#db3b1f) as the declared --secondary/--danger accent, and
  layered light neutrals (#ffffff, #f7f7f8, #f2f2f2, #e9ecef, #dee2e6) for surfaces and hairlines.
  Slate-blue tones (#47596b, #69849b, #6286a3) appear in hero slide button states, suggesting a
  secondary cool accent family used sparingly in promotional contexts; this role is inferred, not
  confirmed sitewide. Typography is set via CSS custom properties: the root sans-serif family is
  declared as "Satoshi", product-tile links use "Open Sans", and CTA/subscribe buttons use
  "Montserrat"; "Playfair Display" is present in the font list but its applied selector was not
  captured, so it is treated here as a possible display/heading face, used cautiously and only where
  a distinct display voice is warranted. All fallbacks are generic (sans-serif/serif/monospace) per
  evidence. Rounded values are proposed conventions (pill buttons at 100px imply a "full" token).
  Spacing uses a standard 4/8-based scale as no explicit spacing tokens were resolved. Semantic
  color-to-role mapping (e.g., which neutral is "canvas" vs "surface-soft") is inferred from usage
  context, not directly labeled in source.

colors:
  primary: "#2f333a"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#2f333a"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f7f7f8"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent: "#db3b1f"
  accent-strong: "#ae2f19"
  accent-soft: "#f5c8c0"
  secondary-cool: "#47596b"
  secondary-cool-soft: "#69849b"
  success: "#008827"
  warning: "#ffc107"
  info: "#17a2b8"
  border-input: "#ced4da"
  tertiary: "#c7c7cb"
  general-text: "#54545c"
typography:
  display-xl: {fontFamily: "'Playfair Display', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Playfair Display', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Satoshi, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.general-text}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  car-seat-safety-callout:
    backgroundColor: "{colors.secondary-cool}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the declared --secondary/--danger accent (#db3b1f) as the strong call-to-action color, styled as a full pill per the 100px radius observed on the newsletter subscribe button. Hover/pressed states were not captured in evidence and are proposed only.

**button-secondary** proposes an outlined inverse treatment consistent with the hero slide buttons, which show white backgrounds transitioning to dark (#333333/#2f333a) fills on hover — a pattern directly observed in `.home-slides .home-slide .button:hover` rules.

**text-input** follows Bootstrap-derived conventions (border-color #ced4da is present in the palette as a Bootstrap default) since no bespoke input selector was supplied; padding and radius are proposed.

**nav-bar** is inferred from the page-text structure (search, account, cart, mega-menu labels like "Shop Our Products") rather than direct nav CSS; colors default to primary-on-white per body rules.

**product-card** reflects the `.js-einstein-carousel .product-tile` link styling (Open Sans, 600 weight, color #67696d) for product titles; card background and radius are proposed since no card container CSS was supplied.

**hero** is modeled on the homepage slide markup (`.home-slide.slide-one/.slide-two`) which pairs dark/blue-toned backgrounds with white button treatments; exact hero background color is not confirmed and primary ink is used as a placeholder.

**footer** draws on the light neutral tokens (#f7f7f8, #dee2e6) for a soft, low-contrast footer consistent with the extensive footer link list observed in page text (Customer Service, Shipping, Accessibility, etc.).

**badge** proposes use of the success green (#008827), defined in :root as --success, for stock/availability or certification labels (e.g., GREENGUARD Gold Certified mentioned in text); no badge component CSS was directly observed.

**search** is inferred from "Submit search keywords" / "Clear search keywords" text present multiple times, indicating a prominent search field; exact styling not observed.

**car-seat-safety-callout** is a category-specific proposed component for car-seat safety/certification messaging (e.g., "Choosing A Car Seat," "Installing a Car Seat"), using the cool slate-blue (#47596b) seen in slide-two button text as a trust-oriented accent distinct from the red CTA accent.

## Responsive Behavior

Breakpoints below mirror the Bootstrap-style custom properties found in global.css (`--breakpoint-*`); actual responsive layout was not observed and this table is a recommendation only.

| Token | Width | Notes (proposed) |
|---|---|---|
| xs | 0 | Single-column stack, full-width CTAs |
| sm | 34rem (~544px) | 2-column product grids begin |
| md | 48rem (~768px) | Nav collapses to horizontal bar |
| lg | 64rem (~1024px) | Full mega-menu, 3–4 column grids |
| xl | 80rem (~1280px) | Max content width, hero side-by-side |
| xxl | 90rem (~1440px) | Container max-width caps |

Touch targets are recommended at a minimum 44x44px for cart, search, and account icons. Mobile navigation should collapse into a hamburger/off-canvas menu below `md`; none of this interaction behavior was directly observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This is a static CSS/text extraction; no rendered layout, JavaScript-driven states, or actual mobile breakpoints were observed.
- Several CSS custom properties (e.g., `--up-sem-font-family-body`, `--up-sem-typography-global-h1-override-font-family`) reference unresolved design-token variables whose final computed values were not supplied, so body/heading font assignments are inferred from adjacent evidence (Open Sans on product links, root --font-family-sans-serif of "Satoshi").
- "Playfair Display" appears in the font-family list but no selector using it was included in evidence; its assignment to display-xl/display-md is a best-effort inference and may not reflect actual site usage.
- Hover, focus, active, and disabled states for buttons/inputs are proposed conventions except where explicitly shown (e.g., hero slide button hover colors).
- Rounded and spacing scales are conventional proposals, not measured from source, aside from the 100px pill radius observed on the subscribe button.
- Font licensing and availability (Satoshi, Montserrat, Open Sans, Playfair Display) were not verified; assume standard web-font loading via the site's own asset pipeline.
- Color-to-role mapping (e.g., "canvas" vs "surface-soft") is an interpretive grouping of the supplied hex values, not a direct semantic label from source CSS.
