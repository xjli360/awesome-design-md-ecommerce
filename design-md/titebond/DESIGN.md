---
version: alpha
name: "Titebond"
source_url: "https://titebond.com"
captured_at: "2026-09-29T04:06:18.750520+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Bootstrap 5.3.7 utility CSS and a supplied
  color palette rather than any bespoke stylesheet, so most tokens are proposed
  conventions rather than confirmed brand rules. The palette includes a bright
  yellow (#ffd51e) and a deeper gold (#dfba1a) alongside a full Bootstrap
  contextual set (blue, red, green, amber, cyan). Because Titebond's product
  line (wood glues, adhesives, caulks) is commonly associated with yellow
  packaging, #ffd51e is treated here as the inferred primary brand accent, used
  sparingly against neutral ink and white canvas rather than as a dominant
  field color. Body text follows Bootstrap's default #212529 on white, with
  #6c757d as muted secondary text and #dee2e6 as the standard hairline/border
  tone. Typography relies on two families present in the evidence: Oswald, a
  condensed sans well suited to an industrial/trade-tool heading voice, and
  Roboto for body copy, both inferred as role assignments since no explicit
  heading/body CSS rule was supplied. Layout, spacing scale, and corner radii
  are proposed defaults suitable for a technical, catalog-driven site, not
  measurements taken from the live page.

colors:
  primary: "#ffd51e"
  ink: "#141414"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#eeeeee"
  on-primary: "#141414"
  accent-gold: "#dfba1a"
  accent-orange: "#ff7f00"
  success: "#198754"
  warning: "#ffc107"
  danger: "#dc3545"
  info: "#0dcaf0"
  overlay-dark: "#242424"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Oswald, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Oswald, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  spec-sheet-link:
    backgroundColor: "transparent"
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    border: "none"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** is proposed as the main call-to-action treatment (e.g. "LEARN MORE," "FIND THE RIGHT PRODUCT"), using the yellow accent against dark text for high visibility; hover/active states are not observed and would need confirmation.

**button-secondary** offers an outlined alternative for lower-emphasis actions such as secondary navigation links; border and text colors reuse the neutral hairline and ink tokens rather than introducing new colors.

**text-input** covers form fields such as the site search or contact forms; padding and border follow Bootstrap's conventional control sizing, though exact site-specific control styling was not present in the supplied rules.

**nav-bar** represents the top navigation bar containing category links (Woodworking Glues, Construction Adhesives, Caulks & Sealants, Flooring Products) and utility links (Where To Buy, Get SDS); a light background with a bottom hairline is proposed, not confirmed from a captured header rule.

**product-card** is a proposed pattern for category/product listing tiles, giving each product family a bordered card with a title in the Oswald-based title style and supporting copy in body-sm; card elevation or shadow was not evidenced and is omitted.

**hero** models the homepage banner area referencing "TRUSTED TO FORM LIFELONG BONDS" and similar messaging; a dark overlay background with large display typography is proposed for legibility over imagery, though the actual hero background (image vs. solid color) is unconfirmed.

**footer** groups the observed footer links (Community, Media, Contact Us, Privacy Policy, Careers, copyright line) on a dark ink background with light text, a common industrial-site pattern; exact footer column layout is not observed.

**badge** is a small proposed component for labeling content such as "SDS" or category tags, using the gold accent in a pill shape; no such badge was directly observed in the extracted markup.

**search** models the "cancel / Search" control referenced in the page text, using a soft surface background to differentiate it from the page canvas.

**spec-sheet-link** is a category-appropriate component for a woodworking/adhesives brand, representing inline links to technical/SDS documents using the info-blue token for affordance; this pattern is proposed to match the site's emphasis on "Technical Resources" and "Get SDS" navigation items.

## Responsive Behavior

This is a recommendation based on Bootstrap's default breakpoint variables found in the CSS (`--bs-breakpoint-*`), not measured site behavior:

| Breakpoint | Width    | Layout guidance                          |
|-----------|----------|-------------------------------------------|
| xs        | 0px      | Single-column stack; nav collapses to menu icon |
| sm        | 576px    | Two-column product grids begin            |
| md        | 768px    | Nav bar expands inline; hero text width increases |
| lg        | 992px    | Three/four-column product grids           |
| xl        | 1200px   | Max content width constrained, added gutters |
| xxl       | 1400px   | Wide hero imagery, footer columns expand  |

Touch targets should be at least 44px in height for buttons and nav links on mobile. The primary navigation is expected to collapse into an off-canvas or dropdown menu below the `md` breakpoint; this behavior is inferred from standard Bootstrap navbar conventions, not confirmed via captured markup or JavaScript.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a limited static CSS/text extraction: the only rules supplied were generic Bootstrap 5.3.7 framework declarations, not page-specific or component-level styles, so most spacing, radius, and layout values are proposed conventions rather than measured facts. The role mapping of colors (e.g., treating #ffd51e as "primary") is inferred from category norms for this brand and the palette's composition, not from any CSS rule explicitly labeling a brand color variable. Font-family-to-role assignment (Oswald for headings, Roboto for body) is inferred from the supplied `font_families` list, since no heading- or body-specific font-family rule was included in the evidence. No interactive states (hover, focus, active), mobile menu behavior, or actual responsive breakpoints in use were observed. Custom font licensing and self-hosting/CDN availability for Oswald and Roboto were not verified in this evidence set.
