---
version: alpha
name: "Evodesk"
source_url: "https://www.evodesk.com"
captured_at: "2026-09-28T04:44:36.509647+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evodesk's storefront markup exposes a compact, functional palette anchored by
  a warm coral primary (#ec785c) used for calls-to-action, a deep slate-navy
  (#20304a) reserved for headings, and pure black body copy on a white canvas.
  Supporting neutrals (#cacaca, #767676, #f4f4f4, #fafafa) appear across
  small-text, secondary buttons, and light section fills, suggesting a
  restrained, engineering-forward brand voice consistent with a "Made in
  USA," patent-driven adjustable-desk manufacturer. Montserrat is the only
  font-family explicitly bound to body and heading selectors; other listed
  families (Georgia, Consolas, monospace) are not tied to any shown rule and
  are treated as unused/system fallbacks here. Buttons are explicitly
  border-radius:0, so the interpretation below treats squared, industrial
  corners as the default brand shape language rather than the softer rounded
  tokens, which are offered only as a proposed alternate scale. Because the
  supplied evidence is standing/adjustable-height desks rather than
  gaming-specific hardware, this spec avoids inventing gaming-only visual
  motifs (RGB, angular gamer branding) and instead reflects the observed,
  premium-industrial, made-to-order tone. Layout, breakpoints, and hover/focus
  states beyond the two documented button states are inferred conventions,
  not measured behavior.

colors:
  primary: "#ec785c"
  primary-hover: "#e75430"
  primary-strong: "#cc4b37"
  ink: "#20304a"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#767676"
  muted-hover: "#5e5e5e"
  hairline: "#cacaca"
  surface-soft: "#f4f4f4"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  success: "#3adb76"
  success-hover: "#22bb5b"
  warning: "#ffae00"
  navy-deep: "#171f32"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14.4px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  configurator-swatch:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"

## Components

**button-primary** carries the only two hover/focus states directly observed in the CSS (`#ec785c` → `#e75430`, or `#cc4b37` on `.primary`), so it is treated as verified for base and hover; all other component states below are proposed extensions of that pattern.

**button-secondary** mirrors the observed `.button.secondary` rule (`#767676` → `#5e5e5e` on hover), used for lower-emphasis actions such as "Compare" or "Learn more" links seen in the page copy.

**text-input** is inferred; no form-field CSS was supplied, so border, radius, and padding follow the same squared, hairline-bordered convention as buttons for visual consistency, labeled proposed.

**nav-bar** is inferred from the presence of a persistent header implied by repeated nav-like text ("Products Compare Reviews About Support"); background/ink colors reuse the documented heading and canvas tokens, but exact height, sticky behavior, and dropdown treatment are not observed.

**product-card** supports the desk-model grid (Pro, Studio L, Aviator L, Limited) referenced in the text; card fill and border reuse observed neutrals, radius is a modest proposed `sm` softening applied only to cards, not buttons.

**hero** models the "Supercharged Standing Desks" / "Watch the Film" banner pattern described in the excerpt; large display type in `ink` on a soft neutral field, with a primary-button CTA. Imagery, video-embed behavior, and exact copy placement are not observed.

**footer** is proposed using the darkest palette color (`#171f32`) as an inferred footer/utility-band role, since no footer selectors were supplied; text and link colors invert to white/hairline for contrast.

**badge** covers recurring flags such as "NEW," "Q3 Build Slots Sold Out," and "Made in USA," using the warning-yellow token as an attention color since no dedicated badge selector was present in evidence.

**search** and **configurator-swatch** are both proposed, category-appropriate patterns: search supports the site's product/model lookup, while configurator-swatch reflects the described "3D Online Configurator" with "over 100 colors and options," using a selectable-swatch grid bordered in hairline gray with a primary-color selected state.

## Responsive Behavior
Recommended, not measured, breakpoint scale:

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| small     | 0–47.9em   | Single-column stacks, nav collapses to menu icon |
| medium    | 48–64em    | 2-column product grids, condensed nav |
| large     | 64.1–90em  | Full nav bar, 3-column product/desk grids |
| xlarge+   | 90em+      | Max-width container, wider hero imagery |

Touch targets should be a minimum of 44px height for buttons and swatch controls; the `configurator-swatch` component should enlarge tap area beyond its visual chip on touch devices. Nav collapse to a hamburger/off-canvas pattern below `medium` is a convention recommendation only, as no header markup or media queries were included in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered screenshots, computed layout, or DOM structure were available. Semantic role mapping (e.g., which neutral is "surface-card" vs. "surface-soft," footer color choice) is inferred from color frequency and likely usage, not confirmed via selector context. All font sizes except the `.button` `0.9rem` value are proposed, not observed. No breakpoint media-query values were supplied beyond a Foundation-style size-name string, so the responsive table above is a best-practice recommendation, not evidence of Evodesk's actual behavior. Hover/focus/active states beyond the two documented button rules, mobile nav behavior, and product-card real content are unobserved. Montserrat's licensing/self-hosting status was not verified; generic `sans-serif` fallback is assumed safe. The brand category supplied ("Gaming Desks") does not match the observed evidence, which describes adjustable-height/electric standing desks; this spec reflects the latter and avoids inventing gaming-specific visual claims.
