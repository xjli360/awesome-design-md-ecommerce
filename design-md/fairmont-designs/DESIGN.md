---
version: alpha
name: "Fairmont Designs"
source_url: "https://fairmontdesigns.com"
captured_at: "2026-09-29T04:21:38.801965+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fairmont Designs Hospitality presents itself through a restrained, editorial palette built on near-black ink (#1c1c1c), a warm off-white "tan" surface (#f1f0e9), and a crisp white canvas, all directly observed in the theme's root CSS variables (--dark, --tan, --line). Primary interactive elements — buttons and file-download links — use a dark charcoal-slate background (#32373c) with white text, evidenced by the wp-element-button and .wp-block-button__link rules; this is treated as the site's primary action color rather than an unverified accent hue, since the CSS-declared --primary green was not present in the confirmed observed palette. Body copy is set in "source-sans-pro" with a sans-serif fallback, while headings use the licensed display face "Wulkan Display" and its italic cut for emphasis, both confirmed in the theme's font-loading stylesheet. Hairlines and dividers reuse the observed #dddddd line color; secondary surfaces draw from #eeeeee and #f9fafb for card and panel backgrounds, and #313131 stands in for deep, dark utility-class sections (has-very-dark-gray-background-color). The rounded scale mirrors the observed fully-pill button radius (9999px) down to smaller proposed increments for cards and inputs. Because the source is a hospitality-contract furnishings site organized around projects, portfolio, and a product program rather than a retail catalog, component patterns favor a project/portfolio card alongside a generic product-card, with semantic color-to-role mapping explicitly labeled as inferred wherever the CSS only supplied a raw hex value without stated purpose.

colors:
  primary: "#32373c"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#414141"
  muted: "#555555"
  hairline: "#dddddd"
  surface-soft: "#f1f0e9"
  surface-card: "#f9fafb"
  surface-dark: "#313131"
  on-primary: "#ffffff"
  border-subtle: "#eeeeee"
typography:
  display-xl: {fontFamily: "'Wulkan Display', sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Wulkan Display', sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Wulkan Display', sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'source-sans-pro', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'source-sans-pro', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'source-sans-pro', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'source-sans-pro', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  portfolio-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** is modeled on the site's observed `.wp-element-button` / `.wp-block-button__link` rule set: a dark slate-charcoal fill (#32373c), white text, no border, and a fully-pill radius (9999px) that matches the CSS's `border-radius:9999px`. Padding follows the theme's `calc(.667em + 2px)` vertical / `calc(1.333em + 2px)` horizontal pattern, approximated here with the spacing scale.

**button-secondary** is a proposed outline variant, unobserved in the supplied CSS, intended for lower-emphasis actions such as "View All Projects." It reuses the hairline border color and ink text so it stays legible on both white and tan surfaces.

**text-input** and **search** are proposed patterns since no form-field CSS was supplied. Both use a light card surface, subtle border, and a small radius consistent with the site's generally soft, non-sharp corner treatment (contrasted with the fully-rounded buttons).

**nav-bar** is inferred from the site-map text listing (Portfolio, Projects, Products, Program, About, News, Contact) and assumes a white background with dark text, typical of the brand's clean editorial tone; no header CSS was directly observed.

**hero** reflects the homepage's large "Furnishing Imagination" statement copy. It is proposed as a dark, full-bleed panel using the observed `#313131` dark-gray background utility class, paired with the display-xl Wulkan Display treatment for the headline.

**footer** is modeled on the observed contact/site-map block layout (North America and International office listings), using the darkest ink tone as background with white text for strong contrast, though exact footer CSS was not supplied.

**product-card** is the category-appropriate component for a furniture/contract-furnishings brand: a light card surface with a title in Wulkan Display and supporting body copy, intended for use in a "Products/Program" catalog grid. No literal product-tile CSS was present in the evidence, so this pattern is proposed.

**portfolio-card** reflects the page's actual repeated content pattern — a scrolling list of named hospitality projects (e.g., "Sofitel Melbourne on Collins," "Kaohsiung Marriott Hotel") each paired with a location caption. It uses the tan surface color to differentiate project storytelling from commerce-style product tiles.

**badge** is a small proposed label (e.g., for "New," "Program," or region tags) using the tan surface and caption typography; it was not directly observed but follows the pill-radius convention seen on buttons.

## Responsive Behavior

Recommended, not measured breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column nav collapses to a toggle menu; hero headline drops to display-md size. |
| tablet | 600–1024px | Two-column project/product grids; nav-bar may remain inline or collapse depending on item count. |
| desktop | 1024–1440px | Full multi-column layout; observed `--padding:160px` and `--gutter:50px` variables suggest generous section spacing at this size. |
| wide | >1440px | Content likely remains max-width constrained with increased whitespace. |

Touch targets should be at least 44×44px for buttons and nav items. Navigation collapse behavior, hover/focus states, and animation timing (a `--easeOut` cubic-bezier was observed but its application was not) are proposed conventions, not confirmed interactions.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and text extraction only; no rendered layout, computed styles, or interaction states were observed. The mapping of #32373c to "primary" is inferred from its use on the sitewide button element, since the CSS-declared `--primary: #61A60E` green variable was not present in the confirmed observed color palette and could not be verified as a brand color. Spacing and rounded scales beyond the directly observed 9999px pill radius and #dddddd hairline are proposed, generic increments, not measured pixel values from the live site. Component states (hover, focus, active, disabled) were not present in the supplied CSS and are marked proposed throughout. Mobile/tablet navigation collapse behavior was not observed. "Wulkan Display" is a licensed/custom display font family referenced in the theme's font-loading stylesheet; its availability, licensing terms, and full weight range were not verified beyond the "regular" and "italic" declarations shown. Category classification was corrected from an initial "Bathroom Fixtures" mismatch to "Furniture" (contract hospitality furnishings) based on the site's own navigation and copy.
