---
version: alpha
name: "Teenage Engineering"
source_url: "https://teenage.engineering"
captured_at: "2026-09-28T04:28:06.736596+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Teenage Engineering's public site pairs a near-black ink (#0f0e12) against
  pure white (#ffffff) and a soft off-white (#f5f5f5) surface, producing the
  brand's signature lab-clean, instrument-panel feel. Root CSS exposes a
  disciplined grey ramp (#e5e5e5 through #272727) for hairlines, placeholders
  and disabled states, plus a small set of saturated signal colors (#0071bb
  blue, #006837 green, #f05a24 orange, #b81d13 red, #fab413 yellow, #c0262c
  error) that read as product/category or status accents rather than primary
  UI color — an inferred mapping since no live component context was
  captured. Typography runs on two custom fluid families, te-20 and te-40
  (with "Unicode" and sans-serif fallbacks), set only at font-weight 100/300
  — no bold weight is exposed — reinforcing a thin, technical typographic
  voice. Font sizes and line-heights are defined as viewport-relative calc()
  expressions rather than fixed px, so all pixel values below are derived
  approximations at a 980px reference width, not measured renders. Corner
  radii swing between a fully square tile mode and a fluid, near-full pill
  mode (--round:9999px), suggesting sharp rectangles for structural elements
  and pill shapes for buttons/badges. This spec proposes a restrained,
  monochrome-first system with the color ramp reserved for accents.

colors:
  primary: "#0f0e12"
  ink: "#0f0e12"
  canvas: "#ffffff"
  body: "#0f0e12"
  muted: "#767676"
  hairline: "#e5e5e5"
  surface-soft: "#f5f5f5"
  surface-card: "#f1f2f2"
  on-primary: "#e5e5e5"
  accent-blue: "#0071bb"
  accent-green: "#006837"
  accent-orange: "#f05a24"
  accent-red: "#b81d13"
  accent-yellow: "#fab413"
  accent-purple: "#9a01a6"
  error: "#c0262c"
  grey-200: "#cccccc"
  grey-300: "#b2b2b2"
  grey-900: "#4d4d4d"
  grey-1000: "#272727"
typography:
  display-xl: {fontFamily: "\"te-40\", \"Unicode\", sans-serif", fontSize: 72px, fontWeight: 100, lineHeight: 1.11, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"te-40\", \"Unicode\", sans-serif", fontSize: 54px, fontWeight: 100, lineHeight: 1.11, letterSpacing: -0.25px}
  title-md: {fontFamily: "\"te-20\", \"Unicode\", sans-serif", fontSize: 36px, fontWeight: 300, lineHeight: 1.11, letterSpacing: 0px}
  body-md: {fontFamily: "\"te-20\", \"Unicode\", sans-serif", fontSize: 26px, fontWeight: 300, lineHeight: 1.15, letterSpacing: 0px}
  body-sm: {fontFamily: "\"te-20\", \"Unicode\", sans-serif", fontSize: 18px, fontWeight: 300, lineHeight: 1.11, letterSpacing: 0px}
  caption: {fontFamily: "\"te-20\", \"Unicode\", sans-serif", fontSize: 13px, fontWeight: 300, lineHeight: 1.2, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"te-20\", \"Unicode\", sans-serif", fontSize: 18px, fontWeight: 300, lineHeight: 1.2, letterSpacing: 0.3px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.surface-card}"
    activeBorderColor: "{colors.ink}"
    swatchColors: ["{colors.accent-blue}", "{colors.accent-green}", "{colors.accent-orange}", "{colors.accent-red}", "{colors.accent-yellow}", "{colors.accent-purple}"]
    rounded: "{rounded.full}"
    padding: "{spacing.xs}"

## Components

**button-primary** uses the dark ink background with light on-primary text, matching the observed dark mobile-cart theming pair (#0f0e12 background, #e5e5e5 text). Fully rounded (pill) per the site's `--round:9999px` token; hover/active states are proposed, not observed.

**button-secondary** is an outline variant on transparent background with a hairline grey border, intended for lower-emphasis actions such as "learn more" links. State transitions (hover fill, focus ring) are proposed.

**text-input** derives directly from the observed `form.css` field tokens: off-white background, grey-700 placeholder, thin grey-100 border, and a rounded corner scaled from viewport width — here fixed to `rounded.md` as a static approximation. Disabled state uses grey-300 text on grey-100 background, per observed `--field-color-disabled` and `--field-background-disabled`.

**nav-bar** is inferred from root theme variables (`--theme-mc`, `--theme-mobile-cart`) which default to the near-black ink with light grey text, suggesting a persistent dark header/utility bar; actual nav layout and scroll behavior were not observed.

**product-card** proposes a soft light-grey card (from the palette's #f1f2f2) with generous padding and large rounded corners, echoing the site's tile-radius concept (`--tile-border-radius`) though the exact pixel value is fluid and viewport-dependent rather than fixed.

**hero** is a full-bleed white section carrying the largest display type (te-40 at thin weight), consistent with a synth/hardware brand that foregrounds product imagery over dense copy; actual hero copy, imagery, and layout are not observed.

**footer** mirrors the nav-bar's dark theming and uses the smallest caption typography, sized proportionally via the observed `--footer-height` and `--footer-column` calc tokens; column structure is inferred, not measured.

**badge** is a proposed small pill label for product status or category tagging (e.g. "new", "field"), using one accent from the signal-color set; color choice per badge type is not observed and would need product-page confirmation.

**search** is proposed as a pill-shaped field consistent with the dark `--theme-mobile-search` token, using the same off-white/placeholder pairing as text-input.

**swatch-selector** is a category-appropriate component for a specialty-gadget brand known for multi-color hardware variants (e.g. OP-1, TX-6). It cycles through the observed signal-color ramp as swatch fills with a dark active-ring indicator; this pattern is proposed, not confirmed from captured markup.

## Responsive Behavior

| Breakpoint | Approx. width | Notes |
|---|---|---|
| compact | <600px | Single-column stacks; nav collapses to icon-only bar; touch targets ≥48px per observed `--btn-min-click-area` |
| regular | 600–1024px | Two-column product grids; footer columns reduce from the observed multi-column layout |
| wide | >1024px | Full multi-column grid; largest type scale (`display-xl`) applies |

This table is a recommendation derived from the presence of fluid, viewport-relative CSS custom properties (`--client-width`-based calc chains) and is **not** a measured breakpoint set — no explicit `@media` rules were included in the supplied evidence. All interactive elements should maintain the observed 48px minimum click area regardless of breakpoint.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically; no rendered layout, hover/focus states, animations, or JavaScript-driven behavior were observed.
- Color **roles** (primary vs. accent vs. status) are inferred from variable naming and pairing; the six signal colors (blue/green/orange/red/yellow/purple) could equally represent product-line branding rather than UI accents.
- Typography **pixel sizes** are derived approximations from `calc()` expressions at an assumed 980px reference width; actual rendered sizes scale fluidly with `--client-width` and were not measured in a browser.
- `rounded` and `spacing` scales are proposed conventional values, not extracted directly — the site's real radius/spacing tokens are fluid (`vw`-based) and vary by breakpoint in ways not fully captured here.
- Custom font families (`te-20`, `te-40`, `TechnoType`, `franxurter`, `riddim`, etc.) are referenced by name only; their availability, licensing, and exact glyph rendering were not verified.
- Mobile navigation, cart, and search interaction patterns are inferred solely from CSS variable names (`--theme-mobile-cart`, `--theme-mobile-search`) and were not visually confirmed.
