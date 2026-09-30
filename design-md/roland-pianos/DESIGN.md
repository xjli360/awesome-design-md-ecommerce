---
version: alpha
name: "Roland Pianos"
source_url: "https://www.roland.com"
captured_at: "2026-09-28T04:07:47.417138+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Roland's global stylesheet, which reveals a
  utilitarian, dark-and-light dual-mode UI built around a signature orange
  accent (#ff5a00) used consistently for hover and active states, alongside a
  secondary blue (#0064ff) reserved for a sub-brand context (BOSS). The base
  layout runs on white surfaces (#ffffff) and a light gray page background
  (#e5e5e5), bordered by a hairline gray (#e0e0e0). Text colors range from
  pure black body copy to a muted gray (#666666) used for header navigation
  links, with a lighter gray (#999999) for inactive icon states. No branded
  typeface was observed; only generic sans-serif, serif, and monospace
  fallbacks plus a private "glyphicon" icon font appear, so all type here uses
  system sans-serif stacks. Rounded pill shapes (circular play and scroll-up
  buttons) suggest a preference for fully rounded interactive controls over
  sharp corners, contrasted with square-cornered form inputs (explicit
  border-radius: 0). Semantic roles for card surfaces, badges, and dark
  sections are inferred from the broader neutral grayscale palette, not
  directly observed in context. The overall proposed direction favors a
  clean, image-forward instrument catalog with orange as the sole strong
  call-to-action color.

colors:
  primary: "#ff5a00"
  primary-alt: "#ff3c00"
  secondary: "#0064ff"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  subtle: "#999999"
  hairline: "#e0e0e0"
  divider: "#cccccc"
  canvas: "#ffffff"
  surface-soft: "#e5e5e5"
  surface-card: "#f2f2f2"
  surface-dark: "#141414"
  on-primary: "#ffffff"
  highlight: "#ffff00"
typography:
  display-xl: {fontFamily: "sans-serif", fontSize: "48px", fontWeight: 300, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "sans-serif", fontSize: "28px", fontWeight: 300, lineHeight: 1.1, letterSpacing: "0px"}
  title-md: {fontFamily: "sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.5px"}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    hoverColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    height: "50px"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    overlayText: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.subtle}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.divider}"
    rounded: "{rounded.full}"
    iconColor: "{colors.subtle}"
    focusBorderColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  sound-demo-player:
    backgroundColor: "{colors.ink}"
    playButtonBackground: "{colors.canvas}"
    playButtonIconColor: "{colors.primary}"
    rounded: "{rounded.full}"
    controlSize: "75px"
    padding: "{spacing.md}"

## Components

**button-primary** anchors calls-to-action such as "Explore" or "Buy," using the observed orange accent as background with white text, mirroring the hover-state color seen on `.button-up:hover:before`. **button-secondary** is a proposed outline variant for lower-priority actions on light surfaces, keeping the same orange for text/border to preserve brand recognition without competing visual weight.

**text-input** reflects the observed reset (`border-radius: 0`, `-webkit-appearance: none`) applied to form elements sitewide, rendered here as a square-cornered field with a light hairline border — a deliberate contrast to the fully rounded buttons elsewhere.

**nav-bar** is modeled on the `#productheader`/`#contentheader` rule: a fixed 50px white bar with a bottom hairline and muted gray link color (#666) that brightens to orange on hover, matching the observed `#ph-home:hover:before` behavior. Its full content arrangement (logo placement, dropdown behavior) is proposed, not measured.

**product-card** is an inferred pattern for piano model listings, using a soft off-white surface and hairline border to separate tiles against the page's gray background (#e5e5e5), since no card-specific selectors were present in the supplied CSS.

**hero** proposes a dark, full-bleed banner treatment consistent with `.billboard-headline` rules that set white text over imagery, using the display-md scale drawn from the observed 28px/300-weight headline rule.

**footer** is inferred as a dark closing band using the same neutral dark palette as other surface-dark elements, with muted text and orange link hover — no footer-specific CSS was supplied, so structure is proposed only.

**badge** is a small pill using the primary orange and full rounding, extrapolated from the site's evident preference for circular controls (button-play, button-up) rather than any observed badge selector.

**search** proposes a rounded input consistent with the pill-shaped button language, with orange focus state for consistency; no search-bar CSS was present in evidence.

**sound-demo-player** is a category-specific proposed component modeled directly on `.button-play`: a 75px circular white-bordered play control with an orange glyph, suited to audio/demo previews of digital piano tones — a natural extension of the observed play-button pattern for this product category.

## Responsive Behavior

Recommended breakpoints (not measured from live site):

| Breakpoint | Width      | Notes                                   |
|-----------|------------|------------------------------------------|
| mobile    | <600px     | single-column, collapsed nav             |
| tablet    | 600–1023px | two-column cards, condensed nav-bar      |
| desktop   | 1024–1599px| matches observed `min-width:1024px; max-width:1600px` on headers |
| wide      | ≥1600px    | content capped, centered                 |

Touch targets should be at least 44px; the observed 60–75px circular buttons already exceed this. Navigation should collapse into a hamburger/drawer pattern below tablet width. This table is a recommendation only — no responsive or mobile-specific CSS was present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from a static CSS snapshot (`base.css`) and a color/font extraction; no live rendering, JavaScript-driven states, or mobile viewport behavior were observed. Semantic role assignments (e.g., which grays serve as "body" vs. "muted" vs. "surface-card") are inferred from selector context, not confirmed via visual inspection. All typography sizes except the 28px/300-weight headline rule and icon-glyph sizes are proposed estimates, not extracted values. No proprietary or brand-licensed font was identified — only generic `sans-serif`, `serif`, `monospace`, and the icon font `glyphicon`; actual font licensing and availability are unverified. Component states such as focus, disabled, error, and active beyond the two documented hover rules (`.button-up:hover`, home-icon hover) are proposed and unobserved. Layout structure for cards, footer, hero, and search has no corresponding CSS evidence and is entirely inferred from general e-commerce conventions applied to the observed palette.
