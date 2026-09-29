---
version: alpha
name: "Unit Editions"
source_url: "https://www.uniteditions.com"
captured_at: "2026-09-28T04:09:58.569162+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from CSS evidence drawn almost entirely from third-party Shopify commerce widgets (BOGOS bundle/volume-discount modules and a free-gifts app) rather than from Unit Editions' core storefront templates. That distinction is treated as a constraint: colors such as the purple accent-alt and the blue accent are inferred to be functional/system colors introduced by app UI, not confirmed brand identity, and are reused here as secondary accents rather than primary brand signals.

  The dependable signal across the evidence is a high-contrast, editorial black-and-white foundation (#000000 on #ffffff) with a family of neutral grays (#303030, #616161, #f3f3f3, #e0e0e0) used for text hierarchy, muted copy, panel backgrounds, and hairline borders — a palette consistent with a design-focused art-book and zine publisher that favors print-like restraint over decorative color. Typography evidence includes "Berthold Akzidenz Grotesk," a grotesque family historically associated with design publishing, alongside Helvetica/Arial fallbacks; this is treated as the observed brand voice, layered onto a generic sans-serif stack for reliability.

  The resulting system favors sharp geometry, minimal rounding, generous whitespace, and a strictly neutral surface palette, with the small set of saturated colors (purple, blue, red, amber, green) reserved for functional states — cart actions, success confirmations, warnings, and alerts — inferred from their narrow, transactional CSS contexts.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#616161"
  hairline: "#e0e0e0"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#2332d5"
  accent-alt: "#7367f0"
  success: "#29845a"
  warning: "#ffaa00"
  danger: "#f72119"
typography:
  display-xl: {fontFamily: "Berthold Akzidenz Grotesk, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Berthold Akzidenz Grotesk, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Berthold Akzidenz Grotesk, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Berthold Akzidenz Grotesk Medium, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
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
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    padding: "{spacing.lg}"

## Components

**button-primary** anchors primary actions (add to cart, checkout) using the stark black-on-white contrast observed in the base palette; the app-widget evidence showed dark neutral buttons (#303030) rather than pure black, so this component treats near-black as the working primary and reserves true black for text/ink.

**button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g., "view details"), using the hairline gray border rather than a filled background, consistent with the restrained neutral system.

**text-input** follows standard form conventions inferred for a commerce site; no direct input styling was present in evidence, so border and padding values are proposed defaults aligned to the hairline and spacing tokens.

**nav-bar** is proposed as a flat, high-contrast header bar; site navigation markup was not present in the supplied CSS, so structure and behavior (sticky, transparent-on-scroll) are unobserved and not claimed.

**product-card** represents a publication/zine listing tile. Title and price color values (#303030) are drawn from bundle-widget product typography, extended here to general catalog cards as an inferred pattern.

**hero** is a proposed full-bleed editorial banner using the display-xl scale; no hero markup was present in evidence, so copy treatment, imagery, and exact scale are proposed rather than observed.

**footer** is proposed as an inverted (black background, white text) block, consistent with an editorial, print-inspired identity; no footer CSS was present in evidence.

**badge** covers small status labels (e.g., "sold out," "limited edition"), using the light surface-soft background seen in the volume-discount widget header, repurposed as a general tag pattern.

**search** is a proposed lightweight search field styled with the light gray surface tone observed elsewhere in the widget backgrounds.

**cart-drawer** is the one component most directly grounded in evidence, since BOGOS bundle and free-gift widgets describe cart-adjacent UI: dark add-to-cart buttons (#303030/#7367f0), white card surfaces, gray borders (#e0e0e0), and muted subtitle text (#616161). Layout proportions and open/close interaction are proposed, not observed.

## Responsive Behavior

The following breakpoint table is a recommendation based on common editorial/e-commerce patterns; no media queries or responsive layout were present in the supplied evidence.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column cards, stacked nav, full-width cart drawer |
| Tablet | 600–959px | Two-column product grid, condensed nav |
| Desktop | 960–1439px | Three to four-column grid, persistent nav bar |
| Wide | 1440px+ | Max-width content container, increased whitespace |

Touch targets should maintain a minimum 44×44px hit area for buttons and nav items. Navigation is expected to collapse into a drawer or menu button below the tablet breakpoint. All of this is proposed guidance, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

The supplied CSS is dominated by third-party Shopify app widgets (BOGOS bundles/volume discounts, a free-gifts module) rather than Unit Editions' core theme, storefront, or product-detail templates; core brand layout, hero treatment, navigation, and typographic hierarchy were not directly observed. Semantic role assignments for accent, accent-alt, success, warning, and danger are inferred from narrow transactional contexts and may not reflect actual brand usage elsewhere on the site. Font availability and licensing for "Berthold Akzidenz Grotesk" were not verified; it is used here only because it appears in supplied font-family declarations, with Helvetica/Arial as safe fallbacks. All typography sizes beyond generic defaults, spacing scale, rounding scale, breakpoints, and interaction states (hover, focus, active, disabled) are proposed and not measured from live CSS. Mobile layout behavior, animation, and true navigation structure were not observed in the provided evidence.
