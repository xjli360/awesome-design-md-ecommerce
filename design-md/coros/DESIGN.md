---
version: alpha
name: "Coros"
source_url: "https://coros.com"
captured_at: "2026-09-28T04:56:48.355587+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Coros (高驰) presents its GPS-watch and endurance-training catalog on a stark
  white canvas (#ffffff) with near-black ink (#000000, #0d0d0d) for headlines
  and product names, reflecting a technical, performance-sports register aimed
  at runners, cyclists, climbers and mountaineers. Deep navy-black surfaces
  (#020015, #0b0b21, #0f1528) appear in the supplied evidence as dark-mode or
  hero-band backgrounds, inferred here as a "night" surface family used behind
  full-bleed product imagery. A saturated red family (#e52431, #e70453,
  #e62e3b, #e0161d) recurs across the palette and is interpreted as the
  primary accent for calls-to-action, badges and highlighted specs, consistent
  with Coros's competitive/athletic positioning; role assignment is inferred,
  since the evidence does not label button states. Grays (#767676, #626262,
  #9ca3af, #ebebeb, #f5f5f5, #f0f0f0) support secondary text, hairlines and
  card surfaces. Typography mixes a Latin display face (DINCOROS-Bold/Black,
  PFDINTextPro) for numerals and hero titles with CJK faces (SourceHanSansCN,
  NotoSansJP, PingFang SC, Microsoft YaHei) for Chinese body copy, plus Inter
  as a system fallback — all observed in the shipped CSS. Layout structure
  (grid, spacing, breakpoints) is not measurable from static evidence and is
  proposed rather than observed.

colors:
  primary: "#e52431"
  ink: "#0d0d0d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#d6d6d6"
  surface-soft: "#f5f5f5"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  night: "#020015"
  night-alt: "#0b0b21"
  accent-magenta: "#e70453"
  accent-red-alt: "#e62e3b"
  muted-2: "#626262"
  border-subtle: "#ebebeb"
  text-tertiary: "#9ca3af"
  overlay-dark: "#000000cc"
  overlay-light: "#ffffff4d"
typography:
  display-xl: {fontFamily: "DINCOROS-Black, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "DINCOROS-Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "SourceHanSansCN-Regular, \"PingFang SC\", \"Microsoft YaHei\", sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "SourceHanSansCN-Regular, \"PingFang SC\", \"Microsoft YaHei\", sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "SourceHanSansCN-Regular, \"PingFang SC\", sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "SourceHanSansCN-Regular, \"PingFang SC\", sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "SourceHanSansCN-Regular, \"PingFang SC\", \"Microsoft YaHei\", sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "56px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.night}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.text-tertiary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    highlightColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.border-subtle}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary** — the main CTA style (e.g. "了解更多" / "立即购买"), using the observed red accent as background with white text; hover/active states are proposed, not observed. **button-secondary** — outline variant for lower-priority actions on light backgrounds, sharing button typography but with a hairline border instead of a fill. **text-input** — generic form field (search, contact) styled with the soft-gray surface and hairline border seen across the neutral palette; focus ring is proposed. **nav-bar** — top navigation strip; white background with black text is consistent with the `body { background-color: #ffffff }` rule, though the exact nav markup/height is inferred. **product-card** — used for watch/product tiles (PACE 4 Pro, APEX 4, NOMAD, etc.); card surface and rounded corners are proposed conventions since no explicit card CSS was supplied, but the light-gray tones (#f0f0f0/#f5f5f5) support a card-on-white pattern. **hero** — full-bleed banner using a dark navy surface (#020015/#0b0b21) behind large display type, matching Coros's product-launch imagery style; exact hero markup not observed. **footer** — dark, dense link footer (site-map, support, legal) inferred from footer copy in the page-text excerpt, styled with muted gray text on near-black. **badge** — small red label for "新品上市" (new arrivals) or sale flags, reusing the primary accent. **search** — pill-shaped input for site search, proposed styling only. **spec-comparison-row** — a category-appropriate component for the "表款对比" (watch comparison) table, using the primary red to highlight the selected/featured column against neutral hairlines.

## Responsive Behavior
| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <768px | Single-column product grid, nav collapses to hamburger/drawer |
| tablet | 768–1199px | 2-column product grid, condensed hero copy |
| desktop | ≥1200px | 3–4 column product grid, full nav bar visible |

Touch targets should be at least 44×44px for buttons and nav icons. Navigation collapse, drawer behavior, and grid column counts above are proposed conventions for a wearables e-commerce site and are not measured from live rendering.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, breakpoints, hover/focus states, or JavaScript-driven interactions were observed. Color-to-role mapping (e.g., which red variant is the "true" CTA color, dark navy as hero vs. dark-mode background) is inferred from frequency and typical e-commerce convention, not confirmed via screenshots. Font-family assignments use only the family names present in the supplied CSS (DINCOROS, PFDINTextPro, SourceHanSansCN, NotoSansJP, PingFang SC, Microsoft YaHei, Inter) with generic fallbacks; actual font licensing, availability, and rendering weight are not verified. All spacing, radius, and breakpoint values are proposed design-system defaults, not measured from the live site. Component states (hover, focus, disabled, loading) are proposed only.
