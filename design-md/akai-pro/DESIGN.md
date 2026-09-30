---
version: alpha
name: "Akai Pro"
source_url: "https://www.akaipro.com"
captured_at: "2026-09-28T04:08:29.710730+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed evidence centers on a high-contrast, performance-gear palette: a
  saturated crimson (#c20439) as the sole brand accent, paired with near-black
  (#0d0d0d) and true black (#000000) for ink and utility marks, and white
  (#ffffff) as the dominant canvas. Mid-tone grays (#eeeeee, #eaeaea, #dddddd,
  #dbdbdb, #c2c2c2, #555555) appear as surfaces, dividers, and body-text
  candidates, though their exact roles are inferred rather than labeled in the
  source. A legacy Bootstrap-style blue (#337ab7) is present but not attached
  to any branded component in the supplied CSS; it is treated here as a
  possible embedded-widget or link color, not a core brand hue.
  Typography is condensed and industrial: alternate-gothic-compressed drives
  headings, alternate-gothic-atf drives uppercase button labels (confirmed at
  20px/600/100% line-height), and a cluster of univers-next-pro and
  georgiapro-condensed families are declared site-wide but not mapped to
  specific selectors in evidence, so their use is inferred. Inter/Arial/
  Helvetica serve as body-text fallbacks. The resulting interpretation favors
  sharp corners softened only slightly (4px, matching the observed .btn
  radius), flat color blocking, and a red-on-black-and-white system suited to
  music-hardware merchandising.

colors:
  primary: "#c20439"
  ink: "#0d0d0d"
  canvas: "#ffffff"
  body: "#555555"
  muted: "#c2c2c2"
  hairline: "#dddddd"
  divider-soft: "#dbdbdb"
  surface-soft: "#eeeeee"
  surface-card: "#eaeaea"
  on-primary: "#ffffff"
  overlay-black: "#000000"
  link: "#337ab7"
typography:
  display-xl: {fontFamily: "alternate-gothic-compressed, sans-serif", fontSize: 64px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "alternate-gothic-compressed, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "univers-next-pro-condensed, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "alternate-gothic-atf, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.divider-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.overlay-black}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.divider-soft}"
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
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  carousel:
    backgroundColor: "{colors.canvas}"
    dotInactiveColor: "{colors.overlay-black}"
    dotActiveColor: "{colors.overlay-black}"
    dotOpacityInactive: 0.25
    dotOpacityActive: 0.75
    padding: "{spacing.base}"

## Components

**button-primary** renders the confirmed `.btn.primary` pattern: solid crimson fill, white label, uppercase condensed type, and a 4px radius taken directly from the observed `.btn` rule. It is the highest-emphasis call-to-action, e.g. "Shop Now" or "Add to Cart."

**button-secondary** mirrors the observed `.btn.secondary` treatment — white background with dark-ink text — intended for use on dark hero or footer sections where a lighter action is needed without competing with the primary red. Outline and hover-fade states are proposed extensions of the observed `.btn.primary.outline` and rgba-hover pattern.

**text-input** is a proposed pattern for search boxes, newsletter fields, and account forms; no input styling was present in the supplied CSS, so border, padding, and radius follow the site's general flat/4px-corner language rather than direct observation.

**nav-bar** is inferred as a white, ink-text horizontal bar with a light hairline divider, consistent with the canvas/ink/hairline palette; no header markup was supplied, so structure, height, and sticky behavior are proposed.

**product-card** proposes a light-gray (#eaeaea) card surface with a soft divider border, suited to displaying DJ controllers and MPCs with condensed titles and small body copy — a reasonable pattern for a hardware catalog, though no card markup was observed.

**hero** interprets the large `.h1`/`alternate-gothic-compressed` heading rule as sitting inside a dark, full-bleed section, following the brand's evident preference for high-contrast black grounds with white display type; exact hero composition is not confirmed by the evidence.

**footer** is proposed as a dark-ink block with white text and soft-gray dividers, extending the `.btn.tertiary` dark-surface logic already present in the button rules.

**badge** proposes a small crimson pill for labels like "New" or "Best Seller," reusing the primary color and caption typography; no badge component was present in the supplied CSS.

**search** proposes a light-surface input using `#eeeeee` as background, distinct from the plain white canvas, to visually separate search from page content; unconfirmed by direct evidence.

**carousel** is grounded in the observed `.slick-dots` rules: black dot glyphs at 25% opacity inactive and 75% opacity active, which this spec treats as the standard indicator pattern for homepage product/feature sliders.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| Mobile     | up to 599px | Single-column stacks; nav collapses to a menu icon |
| Tablet     | 600–1023px  | Two-column product grids; carousel dots remain visible |
| Desktop    | 1024px+     | Full multi-column layout; hover states on buttons active |

Touch targets should be at least 44×44px, exceeding the raw 20px button font-size, via the padding values defined in `spacing.md`/`spacing.lg`. Navigation collapse, carousel swipe behavior, and card-grid column counts are proposed conventions and were not observed in the supplied static CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from a static CSS/color/font extraction and a single homepage title; no live rendering, computed layout, or DOM structure was inspected. Semantic role assignments for grays (#eeeeee, #eaeaea, #dddddd, #dbdbdb, #c2c2c2, #555555) are inferred from typical surface/hairline/body-text usage, not confirmed selectors. The blue (#337ab7) is preserved as a `link` token but its actual usage context (possibly a third-party widget or legacy component) is unverified. Typography sizes outside the confirmed `.btn` and `.h1` rules (display-md, title-md, body-md/sm, caption) are proposed estimates, not measured values. Several declared font families (univers-next-pro-*, georgiapro-condensed, kallisto, alternate-gothic-atf-thin) appear in the font-family list without an attached selector in evidence, so their applied role is inferred. No interaction states (hover/focus/active) beyond the explicitly supplied `.btn` rules were observed, and no mobile or tablet layout was captured. Licensing and availability of all non-system font families (alternate-gothic-*, univers-next-pro-*, georgiapro-condensed, kallisto) are proprietary and unverified for reuse.
