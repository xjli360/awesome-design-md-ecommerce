---
version: alpha
name: "Bilstein"
source_url: "https://bilstein.com"
captured_at: "2026-09-28T04:58:25.126077+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  BILSTEIN's public site combines a technical, functional palette with a single vivid brand accent. The dominant surface is white (#ffffff) with dark ink (#182128) body text, supported by soft gray panels (#f4f5f7) and hairline dividers (#dae2e6) that separate content on an otherwise minimal ground. A saturated yellow (#ffdc00) is treated here as the primary accent, echoing BILSTEIN's historical yellow shock-absorber livery present in the supplied palette; this pairing is an inferred brand role, not a confirmed component capture. A secondary engineering blue (#0094d8, #014f89) is proposed for links and informational emphasis. Buttons are observed using solid black (#000000) and dark slate (#32373c) fills with white text, plus white-on-transparent outlined variants, all rendered with generous pill or rounded-rectangle radii per the .wp-block-button__link and .button-v2 rules. Headings use interstate-condensed at font-weight 800, a condensed, high-contrast display face well suited to automotive/technical branding; body copy is assumed to fall back to noto-sans, Helvetica, or Arial per the supplied font stack, since no explicit body-text selector was captured in the evidence. The resulting interpretation favors a dense, engineering-catalog aesthetic: flat surfaces, hard-edged imagery, condensed headlines, and restrained, high-contrast accent use against a largely monochrome UI shell.

colors:
  primary: "#ffdc00"
  ink: "#182128"
  canvas: "#ffffff"
  body: "#182128"
  muted: "#6a737d"
  hairline: "#dae2e6"
  surface-soft: "#f4f5f7"
  surface-card: "#ffffff"
  on-primary: "#182128"
  accent-blue: "#0094d8"
  accent-blue-dark: "#014f89"
  surface-dark: "#23282d"
  on-dark: "#ffffff"
  button-dark: "#32373c"
  button-black: "#000000"
typography:
  display-xl: {fontFamily: "interstate-condensed, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "interstate-condensed, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "interstate-condensed, Helvetica, Arial, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "noto-sans, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "noto-sans, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "noto-sans, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "interstate-condensed, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderWidth: "2px"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  dealer-locator-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    accentColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the brand yellow fill with dark ink text, used for the highest-priority calls to action such as "View product catalog." Pill radius is drawn from the observed `.wp-block-button__link` `border-radius:9999px` rule; hover/active states are proposed and not confirmed in the evidence.

**button-secondary** is an outlined variant matching the `.button-v2.-outlined` and `.-black.-outlined` patterns observed in CSS, using a 2px border and transparent background, intended for secondary actions like "Find a BILSTEIN dealer near you."

**text-input** is a proposed form field style for contact/dealer-search forms, using the light gray surface and hairline border tokens for a quiet, utilitarian look consistent with the site's flat panel system; no live input styling was captured.

**nav-bar** represents the top-level menu implied by the page text (Performance, OE Replacement, Motorsport, Off-Road, Career, Product Catalog, language switcher). Layout, sticky behavior, and exact height are inferred, not measured.

**product-card** is proposed for the "Product Catalog" grid, pairing a condensed title with a shorter descriptive line, appropriate for shock-absorber/suspension product lines such as Performance, Off-Road, and Camper.

**hero** models the homepage's large introductory section ("Way more than a shock absorber") against a dark surface, using the display-xl heading style derived from the observed 800-weight condensed heading rule; exact hero imagery and layout are not observed.

**footer** groups legal/utility links (Imprint, Legal Notice, Privacy Policy, Terms & Conditions) mentioned in the page text, styled on the dark surface tone with blue link accents for contrast; structure is inferred from typical footer patterns, not captured markup.

**badge** is a small proposed label component (e.g., "New," "OE") using the primary yellow, useful for flagging catalog or packaging updates such as the mentioned QR-code/authenticity packaging refresh.

**search/dealer-locator-card** pairing addresses the "Find BILSTEIN dealers and experts near you" feature: a search input feeding into result cards with blue accent highlights for selected/nearby dealers; interaction behavior is proposed only.

## Responsive Behavior

This is a recommended breakpoint scheme, not a measured observation of the live site:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column stacking; nav collapses to a toggled menu; product/dealer cards stack full-width. |
| tablet | 600–1023px | Two-column card grids; nav may remain collapsed or show condensed horizontal links. |
| desktop | ≥1024px | Multi-column catalog/dealer grids; full horizontal nav with language switcher visible. |

Touch targets should be at least 44×44px for buttons and nav items given the automotive/dealer-locator use case where users may search on mobile in a workshop or field context. Primary/secondary buttons should retain full pill shape at all sizes; outlined buttons should increase border contrast on small screens if the surrounding surface is dark.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, breakpoints, hover/focus states, or JavaScript-driven interactions (e.g., dealer search, catalog filtering, language switcher behavior) were observed. The mapping of `#ffdc00` to "primary" and `#0094d8` to "accent-blue" is an inferred brand-role assignment based on known BILSTEIN product color and palette presence, not a captured component. Body text font family is assumed from the supplied font stack (`noto-sans`) since only heading typography (`interstate-condensed`) was explicitly ruled in the CSS. All typography sizes other than font-weight/family for headings are proposed defaults. `interstate` and `interstate-condensed` availability, licensing, and self-hosting status were not verified. Spacing and rounded-corner scales beyond the observed `9999px` pill and button padding values are proposed conventions for consistency, not measured site tokens.
