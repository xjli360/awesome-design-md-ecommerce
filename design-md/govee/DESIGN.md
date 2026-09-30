---
version: alpha
name: "Govee"
source_url: "https://govee.com"
captured_at: "2026-09-28T09:41:43.049798+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Govee's storefront evidence points to a Shopify Oxygen build layered with Tailwind and a daisyUI-derived
  token system (--rounded-btn, --rounded-box, oklch color channels), styled with the Gotham typeface over
  a system-font stack. The observed palette centers on a saturated cyan-blue family (#00a0df, #18a2e3,
  #20dbef) that reads as the brand's signature RGBIC lighting identity, paired with deep near-black
  neutrals (#161617, #252525, #29323c) for text and dark surfaces, and neutral grays (#cecece, #86868c,
  #f5f5f5) for muted copy, hairlines, and soft backgrounds. A secondary accent cluster of amber (#fd9d02),
  magenta (#b931c9), and green (#22cc95) is inferred to support promotional badges, color-mode indicators,
  and status messaging, echoing the multicolor product category itself. White (#ffffff) is treated as the
  primary canvas and on-primary text color. Button styling (height 3rem, .875rem/600-weight label, .5rem
  radius, hover-darkened fill) is directly grounded in observed .btn rules. All heading weights, section
  spacing, and card layouts beyond these primitives are proposed interpretations suited to a smart-home
  product catalog, not confirmed live-page measurements.

colors:
  primary: "#00a0df"
  ink: "#161617"
  canvas: "#ffffff"
  body: "#252525"
  muted: "#86868c"
  hairline: "#cecece"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#20dbef"
  accent-amber: "#fd9d02"
  accent-magenta: "#b931c9"
  success: "#22cc95"
  error: "#fc3a57"
  dark-surface: "#29323c"
  border-dark: "#373737"
  overlay-scrim: "#0000001a"
typography:
  display-xl: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Gotham, system-ui, -apple-system, Segoe UI, Roboto, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.dark-surface}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    saleBadgeColor: "{colors.accent-amber}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.border-dark}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  color-scene-selector:
    backgroundColor: "{colors.surface-card}"
    swatchColors: ["{colors.primary}", "{colors.accent-magenta}", "{colors.accent-cyan}", "{colors.accent-amber}", "{colors.success}"]
    activeRingColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs}"

## Components
**button-primary** is grounded in the observed `.btn` rule: 3rem height, .5rem radius, 600-weight .875rem label, with a darkened hover fill inferred from the `.btn:hover` background/border color-mix rule. It is proposed as the primary CTA (e.g., "Shop Now", "Subscribe Now").

**button-secondary** is a proposed outline variant using the dark border tone (#29323c) seen as the default `.btn` border-color, intended for lower-emphasis actions like "See All Blogs."

**text-input** is proposed for search and account fields; no live input styling was captured, so background, border, and radius are inferred from the surrounding soft-gray and hairline palette.

**nav-bar** reflects the page's stated top navigation items (outdoor lights, indoor lights, shop by room, deals, explore, support, community); colors are inferred from the white canvas and dark body text, not measured header CSS.

**product-card** is proposed to match the "What's Popular Now" grid (product name, price, optional sale badge) using the 1rem card radius (`--rounded-box`) observed in the token block.

**hero** is proposed for the homepage banner ("Slay with Govee Halloween Lights"), using a dark surface background with the primary cyan as an accent, since actual hero background/image treatment was not captured in the CSS evidence.

**footer** is proposed using the darkest ink tone with muted gray text for policy/link copy, consistent with dark-neutral values present in the palette but not confirmed as the live footer.

**badge** covers sale/discount and "new" labels (e.g., "$23 Off", "new") using the amber accent and full-pill radius (`--rounded-badge` ≈1.9rem, approximated to `rounded.full`).

**search** is proposed for the header search affordance; no dedicated search-input CSS was present in evidence.

**color-scene-selector** is a category-specific proposed component for RGBIC/scene color pickers referenced in "LuminBlend+" and "DaySync" marketing copy, using the multicolor accent set (cyan, magenta, amber, green) drawn directly from the observed palette to represent selectable light colors/scenes.

## Responsive Behavior
Recommended, not measured:

| Breakpoint | Width | Layout notes |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet | 640–1024px | 2-column product grid, condensed nav labels |
| desktop | 1024–1440px | 3–4 column product grid, full nav bar |
| wide | >1440px | Max-width content container, larger hero imagery |

Touch targets should be at least 44×44px, matching the observed `.btn` 3rem (48px) height. Navigation is assumed to collapse into a drawer/menu below tablet width; this collapse behavior was not observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived solely from static CSS/text extraction and does not reflect a rendered or interactive audit of govee.com. Specific gaps:
- No layout, grid, or breakpoint values were present in evidence; all responsive guidance above is proposed.
- Color-role assignment (primary vs. accent vs. status colors) is inferred from frequency and naming conventions (e.g., oklch `--p`, `--er`, `--su` tokens), not confirmed against rendered UI.
- Typography sizes beyond the `.prose h1` (2.25em/800) and `.btn` (.875rem/600) rules are proposed estimates, not measured.
- Gotham is declared in the `body` font-family rule but its actual availability, licensing, and rendering (vs. system fallback) were not verified.
- No hover/focus/active/disabled states were observed beyond the single `.btn:hover` rule; all other interaction states are proposed.
- Mobile navigation, cart, and account-flow UI were not present in the supplied evidence.
