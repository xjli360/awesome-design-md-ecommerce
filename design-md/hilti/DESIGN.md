---
version: alpha
name: "Hilti"
source_url: "https://hilti.com"
captured_at: "2026-09-28T09:55:14.999425+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hilti's public storefront draws on a restrained industrial palette anchored by
  a saturated safety red (#d2051e), paired with two darker red states (#ab0115,
  #920314) that the observed CSS applies explicitly to hover and active button
  states. Neutral text and chrome are built from warm grays (#524f53, #7d7565,
  #bab9ba) rather than pure black, giving the UI a slightly softened,
  construction-tool feel against off-white and white surfaces (#ffffff,
  #f2f1ef, #f8f8f7, #fbfaf8). A small set of status accents (#19af37 green,
  #ffaf00 amber, #4292ed blue) appear in the palette and are inferred here as
  success/warning/info roles, since no selectors confirming their semantic use
  were supplied. Typography is set in a proprietary "Hilti" family (Roman and
  Bold cuts) with Arial/Helvetica/sans-serif fallbacks, consistent with a B2B
  industrial brand that controls its own type but must degrade gracefully.
  This interpretation proposes a componentized system (buttons, cards, nav,
  hero, selector tool) suited to a technical product catalog and engineering
  services site, using only the observed hex values and font names. Sizes,
  spacing, and rounding are proposed conventions, not measured page metrics.

colors:
  primary: "#d2051e"
  primary-hover: "#ab0115"
  primary-active: "#920314"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#524f53"
  muted: "#7d7565"
  hairline: "#cbc8c1"
  surface-soft: "#f2f1ef"
  surface-card: "#fbfaf8"
  on-primary: "#ffffff"
  disabled: "#bab9ba"
  border-subtle: "#ededed"
  success: "#19af37"
  warning: "#ffaf00"
  info: "#4292ed"
  overlay-heavy: "#00000080"
  overlay-light: "#00000026"
typography:
  display-xl: {fontFamily: "Hilti Bold, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Hilti Bold, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Hilti Bold, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Hilti Roman, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Hilti Roman, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Hilti Roman, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Hilti Bold, Arial, Helvetica, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
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
    hover: {backgroundColor: "{colors.primary-hover}"}
    active: {backgroundColor: "{colors.primary-active}"}
    disabled: {backgroundColor: "{colors.disabled}"}
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hover: {borderColor: "{colors.primary-hover}", textColor: "{colors.primary-hover}"}
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focus: {borderColor: "{colors.primary}"}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  selector-tool-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.info}"

## Components

**button-primary** uses the observed solid red fill (#d2051e) with white text, matching the `.btn-tertiary-major` selectors in the evidence, which explicitly define background/border color plus distinct hover (#ab0115) and active (#920314) reds. This is the highest-confidence component mapping in the document.

**button-secondary** is a proposed outline variant using the same primary red for border and text on a transparent background, inferred from the `.btn-tertiary-minor` border-color rules in the CSS, though the full secondary-button treatment (fill, padding) was not directly observed.

**text-input** is proposed; no form-field CSS was supplied. Border and focus colors are inferred from the neutral hairline (#cbc8c1) and brand red respectively, following common pattern conventions rather than observed rules.

**nav-bar** is proposed as a white bar with muted-gray body text (#524f53), consistent with the icon-color variables (`--svg-icon-color: #524f53`) seen for default (non-hover) navigation icon states in the evidence.

**product-card** is proposed for the catalog-driven nature of the site (power tools, fasteners, accessories) using the softer off-white card surface (#fbfaf8) and a subtle border (#ededed), both present in the palette but not tied to a confirmed card selector.

**hero** reflects the homepage's promotional banner content (sale/offer messaging) described in the page text, using the light warm-gray section background (#f2f1ef) as an inferred canvas for large promotional typography.

**footer** is proposed as a dark, high-contrast band using pure black (#000000) with white text, since the observed palette includes true black and the evidence lists an extensive footer link structure (Products, Solutions, Company, Services) typical of a dense industrial-B2B footer.

**badge** is proposed for promotional/status labels (e.g., "Sale Happening Now," "Limited-time offer") referenced in the page text, styled in primary red as a pill using the `full` radius token; no badge-specific CSS was supplied.

**search** reflects the "Search / Search suggestions" UI referenced in the page text; styling is proposed using the soft surface and hairline border tokens, as no search-input selectors were included in the evidence.

**selector-tool-card** is a category-appropriate proposed component for Hilti's "selector charts" and "Pick the right product for the job" feature described in the page text, using the observed blue (#4292ed) as an inferred informational accent for tool/spec-comparison affordances.

## Responsive Behavior

This is a proposed responsive scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| xs | <480px | Single-column stacks; nav collapses to hamburger + icon-only cart/search |
| sm | 480–767px | Two-column product grids; hero CTA stacks below heading |
| md | 768–1023px | Three-column product grids; nav shows primary items inline |
| lg | 1024–1439px | Full desktop nav; four-column product grids |
| xl | ≥1440px | Max-width content container with increased section padding |

Touch targets are recommended at a minimum 44×44px for buttons and icon controls, particularly for the cart, search, and account icons referenced in the page text. Primary navigation is assumed to collapse into a drawer or accordion below the `md` breakpoint given the depth of the "Products / Solutions / Engineering Center / News / Info and Resources" menu structure, but this collapse behavior was not observed directly.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, computed styles, or DOM structure was observed, so grid systems, spacing rhythm, and component composition are proposed, not measured.
- Font sizes, line-heights, letter-spacing, and weights in the typography scale are proposed conventions; only the font-family names ("Hilti," "Hilti Bold," "Hilti Roman," Arial, Helvetica, sans-serif) were confirmed in evidence.
- Semantic color roles (ink, body, muted, surface-soft/card) are inferred from usage context in fragmentary selectors (icon colors, button states) and may not match the actual design system's naming or full usage.
- Status colors (#19af37, #ffaf00, #4292ed) exist in the palette but no selectors confirming their success/warning/info roles were supplied; these mappings are inferred by convention only.
- No hover/focus/active states were observed for inputs, search, cards, or footer links; only button-major hover/active/disabled states were directly evidenced.
- No mobile menu, breakpoint, or interaction behavior was observed; the responsive table above is a recommendation only.
- Availability, licensing, and web-embedding rights for the "Hilti" proprietary font family were not verified; fallback stack is required for any implementation.
