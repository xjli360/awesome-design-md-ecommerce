---
version: alpha
name: "Benjamin Moore"
source_url: "https://benjaminmoore.com"
captured_at: "2026-09-28T09:56:26.825613+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Benjamin Moore's homepage evidence points to a neutral, paper-and-charcoal foundation punctuated by rotating paint-swatch color. The body background (#EFEFEF) and a near-black ink (#1A1A1A) form the primary reading surface, observed directly on `body` and the `.toggleBtn` component, which also shows an inferred border/rule role for the same dark tone. A saturated blue (#367fda) appears distinct from the earthy, muted swatch palette and is treated here as the interactive/link accent, though its exact UI role (link vs. CTA) is inferred rather than confirmed. The remaining palette is dominated by warm, desaturated clay, sand, forest, and navy tones (e.g. #b36957, #9c6040, #306e6d, #2b3762, #af8840) consistent with a paint retailer showcasing color chips; these are mapped as accent/swatch tokens rather than core UI chrome, since the CSS evidence shows them appearing as content, not structural color.

  Typography combines Macklin (likely the licensed display face for headings) with Moderat for body/interface text, falling back to Helvetica/sans-serif per the observed `font-family:inherit` pattern. Sizes and weights beyond the observed 1rem/20px body line-height are proposed to establish a coherent, editorial-but-functional hierarchy suited to a premium paint brand: generous whitespace, soft 4-8px radii, and rectangular, low-ornamentation buttons echoing the flat, borderless `.toggleBtn` control observed in the CSS.

colors:
  primary: "#367fda"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#777777"
  hairline: "#d6d6d6"
  surface-soft: "#efefef"
  surface-card: "#eeece1"
  on-primary: "#ffffff"
  accent-terracotta: "#b36957"
  accent-clay: "#9c6040"
  accent-forest: "#306e6d"
  accent-navy: "#2b3762"
  accent-gold: "#af8840"
  accent-sand: "#daca9c"
typography:
  display-xl: {fontFamily: "Macklin, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Macklin, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Moderat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Moderat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-sm: {fontFamily: "Moderat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "Moderat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Moderat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-tile:
    backgroundColor: "{colors.accent-terracotta}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.canvas}"
    padding: "{spacing.sm}"

## Components
**button-primary** uses the blue accent as a call-to-action fill, inferred from its distinctiveness against the earthy swatch palette; exact CTA usage on the live site is not confirmed from static CSS alone.

**button-secondary** is a proposed outline variant using the observed ink color as both text and border, mirroring the flat, borderless aesthetic seen in `.toggleBtn` but adapted for a bordered secondary action.

**text-input** is a proposed pattern for search/newsletter fields, pairing the canvas background with a hairline border consistent with the muted gray (#d6d6d6) present in the palette.

**nav-bar** reuses the observed body background (#EFEFEF) so the header reads as an extension of the page surface, with a hairline rule beneath it; sticky/scroll behavior is proposed, not observed.

**product-card** (e.g., paint can or sample listings) uses a slightly warmer off-white (#eeece1) surface to differentiate cards from the cooler page background, with a thin hairline border; this differentiation is inferred, not measured.

**hero** models the homepage's large introductory banner ("Explore 3,500 colors...") using the surface-soft background and display-xl type; actual hero markup/CSS was not present in evidence.

**footer** is proposed as a dark, ink-colored band for sitemap/legal links (Privacy, Terms, Accessibility) noted in page text, inverting to on-primary text for contrast; no footer CSS was supplied.

**badge** represents small labels such as "Color of the Year" callouts, using the gold accent tone from the swatch palette; purely a proposed pattern for merchandising emphasis.

**search** supports the "Find a Store" / color search utility referenced in page text; styling is proposed using the same input conventions as text-input.

**color-swatch-tile** is a category-appropriate component representing individual paint color chips (e.g., "Silhouette AF-655," "Raindance 1572") seen throughout the page text, using accent palette colors as fills with a caption-styled name/number label overlay.

## Responsive Behavior
Recommended, not measured, breakpoints: mobile ≤480px, tablet 481–1024px, desktop ≥1025px. Navigation is proposed to collapse into a toggle/hamburger pattern below tablet width, consistent with the `.toggleBtn` disclosure control observed in CSS. Touch targets should be at least 44×44px for buttons and swatch tiles. Product/color-swatch grids are proposed to reflow from multi-column (desktop) to 2-column (tablet) to single-column (mobile), but no grid or media-query evidence was supplied to confirm actual behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from a limited static CSS/text snapshot and does not reflect verified live rendering, responsive breakpoints, or interaction states (hover, focus, active, disabled). The role of #367fda as a primary/CTA color is inferred from its visual distinctiveness, not confirmed usage. Component definitions beyond `.toggleBtn` and `body` are proposed patterns, not extracted selectors. Macklin and Moderat are treated as the brand's custom typefaces based on font-family evidence, but licensing, weight availability, and fallback behavior were not verified. Spacing and rounded-corner scales beyond the observed 16px/24px padding are proposed defaults for consistency, not measured values. Mobile layout, grid structure, and footer/nav markup were not present in the supplied evidence.
