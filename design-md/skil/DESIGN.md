---
version: alpha
name: "Skil"
source_url: "https://skil.com"
captured_at: "2026-09-28T09:18:33.736673+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Skil's storefront CSS exposes a restrained neutral system (#ffffff canvas, #222222 ink,
  #444444 secondary text, #ededed hairlines) layered with a family of named "color-scheme"
  blocks used for section theming: warm terracotta (#e97750/#e17855) as the recurring
  highlight/accent, deep forest green (#0f3429) and sage (#5f9585/#24725b) for outdoor-
  equipment sections, rust brown (#5e2309) and cream (#f6f3ee/#fcfaf7/#ede1da) for
  lifestyle/material moments, and an acid lime (#f6ff94) used as an inverse/callout
  background. This interpretation treats #222222 as the operative brand primary (buttons,
  links, headings) and #e97750 as the singular accent for CTAs, badges, and battery-
  platform tags, since it recurs as --color-highlight across every observed scheme.
  Typography is inferred from the loaded font stack: Archivo (grotesque sans) is assigned
  to headings and UI chrome for an industrial, tool-catalog feel; Inter carries body copy
  and form text for readability; Bebas Neue is reserved for oversized hero/display
  moments consistent with power-tool marketing conventions. Arapey (serif) is present in
  the stack but its role could not be confirmed from the excerpt, so it is treated as
  unused/reserved rather than assigned. Rounded and spacing scales are proposed
  conventions, not measured values.

colors:
  primary: "#222222"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#555555"
  hairline: "#ededed"
  surface-soft: "#f3f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  highlight: "#e97750"
  accent-green: "#24725b"
  accent-forest: "#0f3429"
  accent-brown: "#5e2309"
  surface-cream: "#f6f3ee"
  accent-lime: "#f6ff94"
  danger: "#dc2626"
typography:
  display-xl: {fontFamily: "Bebas Neue, sans-serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.05, letterSpacing: 0.5px}
  display-md: {fontFamily: "Archivo, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Archivo, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.35, letterSpacing: 0.3px}
  button-md: {fontFamily: "Archivo, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.4px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottomColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  battery-system-tag:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the near-black ink as fill with white text, matching the observed `--color-btn-bg: #222222` / `--color-btn-text: #ffffff` pair repeated across every color-scheme block; hover states darkening to pure black are proposed based on `--color-btn-bg-hover: #000000`.

**button-secondary** mirrors the observed `--color-btn-secondary-bg/border: #ededed` tokens for a low-emphasis outlined action, useful for "View All" category links seen throughout the navigation data.

**text-input** is a proposed pattern for search and account forms, grounded in the light field background (`--color-field-bg`) and ink text color consistently defined per scheme.

**nav-bar** reflects the mega-menu structure evident in the excerpt (Products, Saws, Outdoor Power Equipment, Systems, Support, Register), rendered on the default white background-1 scheme with hairline dividers between mega-menu columns; collapse behavior on mobile is proposed, not observed.

**product-card** is inferred for catalog/category grid listings; surface-card white with a hairline border keeps tool photography as the visual focus, consistent with the light, neutral background-1/2 tokens.

**hero** maps to the promotional banners referenced in the text ("Get fall yardwork done fast," "Take on Anything") and is assigned the forest-green scheme-8 background as a bold seasonal treatment; other scheme backgrounds (brown, cream, sage) are proposed alternates for rotating campaigns.

**footer** is proposed using the ink/on-primary pairing for a dark, condensed utility footer typical of tool-brand sites, though no footer-specific CSS was supplied.

**badge** uses the recurring highlight terracotta for sale/new labels or stock indicators; not confirmed as an existing UI element, but consistent with `--color-highlight` being defined identically across every scheme, suggesting a persistent accent role.

**search** is a proposed pill-shaped input for the header search icon referenced in the page text, using surface-soft fill for a soft, low-contrast affordance.

**battery-system-tag** is a category-specific component addressing the PWRCORE 12/20/40/GO battery-platform labeling unique to power-tool merchandising; the acid-lime `--color-inverse` background (`#f6ff94`) is repurposed here as a distinctive tag color to visually separate battery-platform compatibility from generic badges.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| sm | 375px | Single-column product grid, stacked hero text, hamburger nav |
| md | 768px | 2-column product grid, mega-menu collapses to accordion |
| lg | 1024px | Full mega-menu nav bar, 3-column product grid |
| xl | 1280px+ | 4-column product grid, max-width container |

Touch targets should be a minimum 44px height for buttons and nav items on sm/md. Mega-menu columns (Power Tools, Saws, Outdoor Power Equipment, Systems) are recommended to collapse into an accordion or drawer below md. This table is a recommendation derived from typical e-commerce patterns, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This DESIGN.md was generated from static CSS custom-property extraction and page text only; no live rendering, computed styles, or DOM interaction was observed. Font sizes, weights, and letter-spacing in the typography tokens are proposed conventions, not measured from stylesheet rules (only font-family names were confirmed). The specific role of Arapey could not be determined and is treated as unused. Semantic assignment of Archivo to headings and Inter to body is inferred from typical pairing conventions, not confirmed usage in markup. Interaction states (hover/focus/active beyond the documented `--color-btn-bg-hover`), mobile menu behavior, and responsive breakpoints are not observed and are marked proposed. Licensing and self-hosting/CDN availability of Archivo, Bebas Neue, Arapey, and Inter were not verified.
