---
version: alpha
name: "Owlet"
source_url: "https://owletcare.com"
captured_at: "2026-09-28T04:24:24.670966+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Owlet's storefront pairs a warm, nursery-adjacent palette with a clinical
  teal anchor, reflecting its positioning as an FDA-cleared health-tech
  product sold to parents. The dominant background is a soft warm off-white
  (#f7f1ed) rather than clinical white, paired with a deep teal
  (#1d464b) used consistently for headline copy, body text, and button
  labels — this teal is treated here as the primary brand ink. A muted sage
  (#c2d4c8) appears as a CTA background in promotional blocks and is
  proposed as the primary interactive accent. Warm neutrals (#faefe5,
  #eedad3, #fff6ee) suggest a supporting "soft surface" family for
  cards and section backgrounds, while pure white (#ffffff) serves as
  card/surface base and on-dark text.
  A secondary blue pair (#1990c6 / #136f99) appears only in Shopify's
  accelerated-checkout component and is inferred here as the system's link/
  interactive-blue role rather than a core brand color. Success, warning, and
  error roles (#4caf82, #fba11a, #ce2c2c) are inferred from generic UI
  greens/oranges/reds in the palette, not from confirmed alert components.
  Typography is serif display (Source Serif Pro/4) over sans body (Source
  Sans Pro/3), observed directly in hero heading and description rules.

colors:
  primary: "#1d464b"
  ink: "#1d464b"
  canvas: "#f7f1ed"
  body: "#1d464b"
  muted: "#744343"
  hairline: "#dedede"
  surface-soft: "#faefe5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#c2d4c8"
  accent-blush: "#eedad3"
  interactive-blue: "#1990c6"
  interactive-blue-hover: "#136f99"
  border-light: "#e5e5e5"
  skeleton: "#dedede"
  success: "#3f8843"
  warning: "#fba11a"
  error: "#ce2c2c"
typography:
  display-xl: {fontFamily: "'Source Serif Pro', 'Source Serif 4', Georgia, serif", fontSize: "42px", fontWeight: 400, lineHeight: 1.0, letterSpacing: "-0.02em"}
  display-md: {fontFamily: "'Source Serif Pro', 'Source Serif 4', Georgia, serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.01em"}
  title-md: {fontFamily: "'Source Sans Pro', 'Source Sans 3', sans-serif", fontSize: "24px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0"}
  body-md: {fontFamily: "'Source Sans Pro', 'Source Sans 3', sans-serif", fontSize: "22px", fontWeight: 400, lineHeight: 1.37, letterSpacing: "0"}
  body-sm: {fontFamily: "'Source Sans Pro', 'Source Sans 3', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0"}
  caption: {fontFamily: "'Source Sans Pro', 'Source Sans 3', sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.02em"}
  button-md: {fontFamily: "'Source Sans Pro', 'Source Sans 3', sans-serif", fontSize: "16px", fontWeight: 500, lineHeight: 1.0, letterSpacing: "0"}
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
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    descriptionTypography: "{typography.body-md}"
    textColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vitals-status-card:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    valueTypography: "{typography.display-md}"
    labelTypography: "{typography.caption}"
    accentColor: "{colors.success}"

## Components

**button-primary** uses the sage accent (#c2d4c8) confirmed in a hero CTA rule as a background with dark teal label text — a soft, non-alarming call-to-action consistent with a nursery/health product. **button-secondary** is a proposed outline treatment using the same teal on white, for lower-emphasis actions; its hover/active states are not observed and are proposed only. **text-input** and **search** share a white surface with a light hairline border (#dedede, inferred from the checkout skeleton and border-variable values) since no dedicated form-field CSS was captured. **nav-bar** assumes the warm canvas background seen applied to the header wrapper in a promo-section override, with teal text; sticky/scroll behavior is not observed. **product-card** proposes a white surface with a light border and rounded corners for listing Owlet's monitor/camera products; no literal card CSS was supplied. **hero** reflects the one concretely observed pattern: centered serif headline (42px, -0.02em tracking) over a sans description (22px) on the warm canvas background. **footer** is proposed as a dark-teal, white-text band for contrast and closure, mirroring the brand's primary/on-primary pairing; no footer CSS was captured. **badge** is a small pill using the blush accent for status labels (e.g., "FDA-cleared"), proposed. The category-specific **vitals-status-card** is a proposed pattern for displaying live monitor readings (heart rate, oxygen) using the soft peach surface with a success-green accent, intended for an app-preview or dashboard-style section; it is entirely inferred from category context, not from captured component markup.

## Responsive Behavior
This is a recommended breakpoint strategy, not measured site behavior — no responsive/media-query evidence was captured beyond a `--font-body-mobile-size` variable indicating at least one mobile-specific override.

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacks; hero heading may reduce toward `display-md`. |
| tablet | 600–1023px | Two-column product/vitals grids; nav may collapse to a hamburger. |
| desktop | 1024–1399px | Full nav, multi-column layouts. |
| wide | ≥1400px | Content capped near the observed `--page-width: 1400px` container. |

Touch targets should be at least 44px tall (aligned with the observed Shopify accelerated-checkout button's 44px default block size). Primary navigation is expected to collapse below tablet width; this is a proposed convention, not confirmed markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Color variables were captured as RGB triples partially truncated in the CSS excerpt (e.g., `--color-accent-2`, `--color-border`); exact hex equivalents were approximated from the nearest values in the observed hex palette (e.g., hairline mapped to `#dedede`) and should be re-verified against live computed styles.
- `--color-support-error` was empty in the source and no confirmed error/success/warning UI was observed; those roles are fully inferred from generic palette hues.
- Body base font-size uses a `1.5rem` mobile variable of uncertain root scaling; body-md/body-sm pixel values here are best-effort reconciliations with the one concrete 22px description rule, not confirmed global defaults.
- No hover, focus, active, or disabled states were observed for any interactive component; all such states are proposed.
- No mobile-collapsed navigation, menu, or cart-drawer markup was captured; responsive behavior above is a design recommendation only.
- Rounded-corner scale is proposed; the only observed radius value (checkout button, `0px` default) suggests sharper corners may be more accurate than the `md`/`lg` values listed.
- Custom font availability/licensing for Source Serif Pro/4 and Source Sans Pro/3 was not verified; fallback stacks (Georgia, sans-serif) should be used defensively.
- Spacing scale is a proposed system; only `--page-gap: 20px` and grid gaps (`30px`) were directly observed and do not map cleanly onto the scale above.
