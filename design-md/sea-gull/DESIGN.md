---
version: alpha
name: "Sea Gull"
source_url: "https://seagulllighting.com"
captured_at: "2026-09-28T09:18:43.178583+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sea Gull Lighting's markup exposes a legacy catalog-site stack: a 1124px fixed
  `.full-body` wrapper, small utility type classes (bodytype9 through
  bodytype11_bold), and two competing font stacks — `proxima-nova-condensed`
  (with Cambria/Hoefler Text/serif fallbacks) on the document body, and
  `Lucida Sans Unicode, Arial` on form controls like `.registerButton`. The
  observed palette is dominated by neutral grays (#666, #757575, #cccccc,
  #ebebeb) against white, with a small set of teal-navy accents (#005072,
  #003b54, #87a3af, #a0c8ba, #ebf2f5) that plausibly carry the brand's
  coastal/"Sea Gull" identity, plus an isolated red (#ff0000) used for
  urgent/error text and a muted gold (#c69d4b) that could flag featured or
  premium collections. This interpretation treats the teal-navy family as
  primary brand color, gray text classes as body/muted roles, and the pale
  #ebf2f5/#f4f4f4 tones as soft surfaces for cards and panels — all inferred,
  since no rule states brand-color intent. Typography sizing is drawn from the
  literal 9–12px utility classes for body copy, while larger display sizes are
  proposed to give the interpretation a workable hierarchy for a modern
  product/category browsing experience (chandeliers, ceiling fans, LED,
  outdoor fixtures) without claiming any observed heading styles.

colors:
  primary: "#005072"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#373629"
  muted: "#757575"
  hairline: "#cccccc"
  surface-soft: "#ebf2f5"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent-teal: "#87a3af"
  accent-sage: "#a0c8ba"
  heading-navy: "#003b54"
  alert-red: "#ff0000"
  gold-accent: "#c69d4b"
  border-light: "#ebebeb"
typography:
  display-xl: {fontFamily: "proxima-nova-condensed, Cambria, 'Hoefler Text', serif", fontSize: 42px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  display-md: {fontFamily: "proxima-nova-condensed, Cambria, 'Hoefler Text', serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.2px}
  title-md: {fontFamily: "Lucida Sans Unicode, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "proxima-nova-condensed, Cambria, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "proxima-nova-condensed, Cambria, serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 9px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lucida Sans Unicode, Arial, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.heading-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px ridge {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    hairline: "1px solid {colors.border-light}"
  hero:
    backgroundColor: "{colors.heading-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.heading-navy}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
    border: "1px solid {colors.accent-teal}"

## Components
**button-primary** uses the teal-navy `{colors.primary}` as an inferred call-to-action fill, since no CSS explicitly labels a CTA button; the `.registerButton` rule (ridge border, `#EBF2F5` fill) is the closest observed analog and informs the **button-secondary** treatment instead, kept lighter and bordered to read as a subordinate action alongside primary.

**text-input** is proposed generically from form-field conventions; no input styling was present in the supplied CSS, so border, radius, and padding are placeholder values suited to a catalog search/login flow.

**nav-bar** draws its gray/uppercase tone from `.bottomNavigation` (#757575, bold, uppercase) and `.topAdminNav a` (#666, uppercase), suggesting the site's navigation rows favor muted, all-caps labels rather than bold color; padding and layout are proposed.

**product-card** is a category-appropriate addition for browsing chandeliers, fans, and fixtures. It borrows the pale `#f4f4f4` surface and light hairline (`#ebebeb`) observed elsewhere as panel/background tones, with title and body type drawn from the small utility classes.

**hero** is proposed and not observed; it uses `{colors.heading-navy}` (`#003B54`, seen only as small leftNavHeader text) scaled up to a full banner treatment as a plausible, brand-consistent extrapolation.

**footer** mirrors the literal `.homeCopyright` (#333) and general muted-gray footer text pattern, set on white with a hairline divider; copy size follows the smallest observed caption class.

**badge** is proposed for merchandising flags (e.g., "NEW IN 2026," ENERGY STAR); gold (`#c69d4b`) was chosen from the palette as a plausible accent distinct from the teal system, though no CSS rule confirms its brand usage.

**spec-badge** is a category-specific component for compliance/spec labels seen in the page text (ENERGY STAR, California Title 24, LED Lighting), using the soft blue surface and teal border to visually group technical callouts without asserting an observed style.

## Responsive Behavior
Recommended, not measured: stack the fixed 1124px `.full-body` layout into fluid containers below 1280px; collapse top navigation into a hamburger/drawer under 768px; single-column product-card grids under 600px; minimum 44px touch targets for buttons and nav items on touch devices.

| Breakpoint | Target |
|---|---|
| ≥1280px | Desktop, fixed-width container equivalent |
| 768–1279px | Tablet, fluid container |
| 480–767px | Mobile landscape, collapsed nav |
| <480px | Mobile portrait, single-column |

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This is a static-extraction interpretation: no JavaScript-driven states (hover, focus, active, mega-menu behavior) were observed, and no live layout, breakpoints, or mobile rendering were captured. Font availability and licensing for `proxima-nova-condensed` and the Avenir LT W01 variants listed in evidence were not verified and may require licensing to use as specified. Color-to-role mapping (primary, hero, badge, alert) is inferred from limited, small-scale utility classes and may not reflect actual brand guidelines. All typography sizes above the smallest observed (9–12px) utility classes are proposed placeholders for hierarchy, not measured values.
