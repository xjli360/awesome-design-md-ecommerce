---
version: alpha
name: "Motul"
source_url: "https://motul.com"
captured_at: "2026-09-28T04:29:30.813344+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Motul's evidence points to a utilitarian, high-contrast industrial palette built around near-black ink (#202020), white canvas (#ffffff), and a saturated red (#ed1c24) used as the active/accent color in navigation state (ProductCategoryRail_railItemActive). Supporting neutrals include light grays (#f8f8f8, #f3f3f3, #e7e7e7, #dadada) for surfaces, hairlines, and hover states, plus darker grays (#3b3e3f, #727272) for secondary text. Typography is system-first: the CSS custom properties resolve --font-family-title and --font-family-body to Graphik with Helvetica, Roboto, Arial, sans-serif fallbacks in the default (non-localized) root scope; localized variants swap in Be Vietnam Pro, Graphik LCG, or GE SS Two, none of which are treated as brand-default here since the base :root applies to the primary domain. This interpretation proposes a compact, functional automotive-retail system: sticky white header with a thin gray hairline, red used sparingly for primary actions and active states, and dark near-black for solid CTA buttons (as seen in MobileMenuSubDialog_blackButton). Rounded corners are small and utilitarian (2–4px) per observed .25rem/.125rem radii. All roles beyond directly observed selectors (body text color, muted text, card surfaces) are inferred from adjacent neutral tokens in the palette, not measured directly.

colors:
  primary: "#ed1c24"
  primary-strong: "#db3832"
  ink: "#202020"
  canvas: "#ffffff"
  body: "#3b3e3f"
  muted: "#727272"
  hairline: "#e7e7e7"
  hairline-soft: "#dadada"
  surface-soft: "#f8f8f8"
  surface-card: "#f3f3f3"
  surface-alt: "#f7f7f7"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  border-mid: "#cccccc"
  border-dark: "#333333"
typography:
  display-xl: {fontFamily: "Graphik, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Graphik, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Graphik, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica, Arial, Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica, Arial, Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica, Arial, Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.1px}
  button-md: {fontFamily: "Graphik, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.xl}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-mid}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottomColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    position: "sticky"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    linkTypography: "{typography.body-sm}"
    dividerColor: "{colors.border-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  category-rail-item:
    backgroundColor: "transparent"
    hoverBackgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.lg}"

## Components
**button-primary** renders the observed red accent as a solid call-to-action, appropriate for "shop" or "find product" actions; hover/focus states are proposed, not measured. **button-secondary** mirrors the observed `.MobileMenuSubDialog_blackButton` pattern: near-black background, white uppercase text, generous horizontal padding — directly evidenced in CSS. **button-outline** is a proposed lower-emphasis variant using the mid-gray border token for secondary actions like "learn more." **text-input** proposes a bordered, softly-rounded field consistent with the site's small-radius language (.125rem–.25rem observed on menu and rail components); no live form field was captured in evidence. **nav-bar** reflects the observed `.Header_header` sticky white bar with a light gray bottom hairline and z-index layering — this structure is directly evidenced. **product-card** is inferred for a lubricant-catalog context; padding and radius extrapolate from the observed `.ProductCategoryMenuContent` panel styling (white background, .25rem radius, padding). **hero** is a proposed dark full-bleed banner using ink as background, suited to automotive/motorsport imagery, not observed in the supplied CSS. **footer** is inferred as a dark section for consistency with the button-secondary ink tone; link and divider treatment are proposed. **badge** proposes a small red pill for labels like "new" or category tags, reusing the primary accent. **search** is a proposed light-gray input consistent with `.ProductCategoryRail` hover background (#f3f3f3). **category-rail-item** is directly evidenced from `.ProductCategoryRail_railItem` and its active/hover states, including the red active background and gray hover background.

## Responsive Behavior
This is a recommended structure, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <640px | Single column; nav collapses to hamburger/mobile menu dialog (evidenced class name `MobileMenuSubDialog` suggests such a pattern exists) |
| Tablet | 640–1024px | Two-column product grids; sticky header retained |
| Desktop | 1024–1440px | Full desktop nav with product-category flyout panel (`ProductsMenuContent`), multi-column footer |
| Wide | >1440px | Max-width content container, additional whitespace |

Touch targets should be at least 44×44px for nav and buttons; the mobile menu should collapse category rails into an accordion or full-screen dialog, consistent with the evidenced `MobileMenuSubDialog` naming, though its exact interaction was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, interaction, or mobile viewport was observed. Color role assignments (body, muted, surface-card, etc.) are inferred from neutral-scale proximity in the supplied palette, not confirmed against live element usage beyond the selectors explicitly listed. Typography sizes, weights, and letter-spacing for display/title/body/caption scales are proposed conventions, not measured from live rendered CSS (only font-family and a few weight/size pairs for specific components were evidenced). Localized font families (Be Vietnam Pro, Graphik LCG, GE SS Two) are documented in evidence but excluded from default typography tokens since they apply only under non-default `:lang()` scopes; their licensing and availability for the primary English/default locale are unverified. Hover, focus, active, and disabled states beyond the one evidenced active/hover pair (`ProductCategoryRail_railItemActive`) are proposed design conventions only. No breakpoint values were present in the supplied CSS; the responsive table above is a generic recommendation.
