---
version: alpha
name: "SJC Drums"
source_url: "https://www.sjcdrums.com"
captured_at: "2026-09-28T04:07:35.383860+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  SJC Drums presents a stripped-down, high-contrast identity built on pure
  black text (#000000) over white canvas (#ffffff), with a single saturated
  magenta-red accent (#d92351) drawn directly from the site's --color-accent
  custom property. A cool neutral gray (#919da9) recurs across multiple
  button variants in the extracted CSS, functioning as a secondary/muted
  action color. Heading typography is explicitly set to Barlow at weight 800,
  with confirmed sizes of 32px, 24px, 20px, and 18px across heading levels;
  body copy falls back to a system-ui stack rather than a proprietary
  typeface. Several decorative display fonts (Anton, Permanent Marker,
  Shrikhand, Archivo, Quicksand) appear in the font-family evidence but their
  applied context is not confirmed, so they are treated as inferred
  decorative accents rather than core system fonts. A dark slate tone
  (#242d35) and light neutral surfaces (#f3f3f3, #fdfdfd) are inferred as
  section and card backgrounds to support a bold, editorial, product-forward
  layout typical of a drum-hardware brand. Rounded pill buttons (40px radius
  observed) inform a full-radius button convention. All roles beyond direct
  CSS variable matches are explicitly labeled inferred below.

colors:
  primary: "#d92351"
  on-primary: "#ffffff"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#919da9"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#fdfdfd"
  dark: "#242d35"
  alert: "#db302a"
  text-secondary: "#666666"
typography:
  display-xl: {fontFamily: "Barlow, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "system-ui, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "system-ui, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "system-ui, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "system-ui, Arial, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    textColor: "{colors.muted}"
    border: "1px solid {colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  custom-builder-card:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.lg}"
    titleTypography: "{typography.title-md}"
    ctaColor: "{colors.primary}"
    padding: "{spacing.xl}"

## Components

**button-primary** uses the accent magenta-red directly from the observed `--color-accent` variable, with a full pill radius echoing the 40px `border-radius` seen on several `.pf-button` variants. This is the confirmed CTA style for purchase and lead actions.

**button-secondary** mirrors the neutral gray (`#919da9`) outline pattern that appears repeatedly across `.pf-button-3` through `.pf-button-7` selectors, forming a consistent low-emphasis action style for filters or secondary links.

**text-input** is a proposed pattern; no form-field CSS was supplied, so border, radius, and padding are inferred from the site's general hairline and spacing conventions rather than observed styles.

**nav-bar** is inferred as a light, white-background bar with black text and a thin divider, consistent with the site's high-contrast black-on-white foundation; exact height and sticky behavior were not observed.

**product-card** is proposed for drum kit/hardware listings, using the near-white card surface and heading-scale typography (title-md at 24px, matching the confirmed `.pf-heading-3` size) to present product name and price.

**hero** applies the dark slate tone as a full-bleed section background with large Barlow display type, an inferred pattern intended to showcase artist/drum kit imagery; no hero-specific CSS was captured in evidence.

**footer** reuses the dark surface color for a grounded, brand-heavy closing section; content structure (columns, social icons) is proposed, not observed.

**badge** repurposes the observed red (`#db302a`) for sale, "new," or limited-edition tags — a plausible but inferred use, since no badge-specific class was present in evidence.

**search** and **custom-builder-card** are both proposed, category-appropriate additions: search reuses the soft surface and pill radius for consistency, while custom-builder-card responds to the brand's "Custom Drums" positioning (from the page title) with a callout module directing users toward a build/configure flow — this component is a design proposal, not a captured UI pattern.

## Responsive Behavior

This is a recommended breakpoint strategy, not measured site behavior:

| Breakpoint | Width       | Behavior (proposed) |
|-----------|-------------|----------------------|
| Mobile    | < 640px     | Single-column stacking, nav collapses to a toggled menu, hero type steps down to `display-md` |
| Tablet    | 640–1023px  | Two-column product grids, nav remains condensed |
| Desktop   | ≥ 1024px    | Multi-column grids, full nav bar, `display-xl` hero type |

Touch targets should maintain a minimum 44×44px hit area for buttons and nav items, using `{spacing.md}`–`{spacing.lg}` padding. Navigation collapse and menu-toggle interaction were not observed and are recommended defaults only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction and a single evidence payload; no live rendering, computed layout, or DOM interaction was observed. Component states (hover, focus, active, disabled) are proposed, not verified. Several decorative font families (Anton, Permanent Marker, Shrikhand, Baskerville, Quicksand, Archivo, Abel) appear in the raw font-family list but their applied usage, licensing, and availability were not confirmed and are excluded from core typography tokens. Spacing and rounded scales beyond the explicit 32/24/20/18px heading sizes and the 40px pill-button radius are proposed conventions, not measured values. Mobile navigation collapse, search interaction, and the custom-builder flow are inferred from brand context (site title "SJC Custom Drums") rather than observed UI. Color roles for `surface-soft`, `surface-card`, `dark`, and `alert` are inferred semantic assignments from a larger observed palette and should be validated against live pages before implementation.
