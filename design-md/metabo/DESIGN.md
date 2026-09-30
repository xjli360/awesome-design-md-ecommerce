---
version: alpha
name: "Metabo"
source_url: "https://metabo.com"
captured_at: "2026-09-28T10:34:11.806412+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Metabo's public site evidence shows a professional industrial-tools palette
  built on a dark forest green (#224b44, with tonal variants #15433d, #09726a,
  #314e49, #36706b) paired with neutral black/white and a family of saturated
  reds (#ed1a3b, #e2032e, #f21024, #a50a20) that likely signal alerts, safety
  callouts, or accent CTAs rather than primary navigation chrome. Body copy and
  structural elements use plain black (#000000) and near-black (#222222) text
  on white, with mid-grey neutrals (#626262, #777777, #cccccc, #f0f0f0)
  supplying muted text, hairlines, and soft surface fills — all inferred roles
  since the CSS does not label semantic intent directly.

  Typography is anchored in Arial/sans-serif for nearly all defined utility
  classes (headers, footers, product titles), with a proprietary "Metabo W01
  Regular" webfont and "MetaboSans"/"MetaboSlab" families referenced in the
  font stack, suggesting a branded display face reserved for hero or logotype
  contexts. This interpretation treats MetaboSans as the display typeface and
  Arial as the dependable body/UI workhorse, reflecting the CSS's own
  fallback pattern. Uppercase, bold, tightly-tracked headers dominate the
  observed rules, reinforcing an industrial, engineering-catalogue tone
  suited to a professional power-tools audience.

colors:
  primary: "#224b44"
  primary-dark: "#15433d"
  primary-tonal: "#09726a"
  accent: "#ed1a3b"
  accent-dark: "#a50a20"
  ink: "#000000"
  body: "#222222"
  canvas: "#ffffff"
  muted: "#626262"
  hairline: "#cccccc"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  surface-alt: "#f3f3f3"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  border-strong: "#aaaaaa"
typography:
  display-xl: {fontFamily: "'MetaboSans', Arial, sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Arial, sans-serif", fontSize: 26px, fontWeight: 700, lineHeight: 2.5em, letterSpacing: 0.5px}
  title-md: {fontFamily: "Arial, sans-serif", fontSize: 26px, fontWeight: 700, lineHeight: 1.875em, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.5em, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.25em, letterSpacing: 0.5px}
  button-md: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.125em, letterSpacing: 0.5px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  battery-compat-tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    border: "1px solid {colors.primary-tonal}"

## Components
**button-primary** proposes the deep brand green as a solid fill for the main calls to action (e.g. "Add to comparison," "Find a dealer"), matching the green used across observed header and label classes. **button-secondary** is an outlined inversion for lower-priority actions, keeping the same green ink on white so it reads as a family with the primary button. **text-input** is a proposed, unobserved pattern using the soft grey surface fill (#f0f0f0) seen elsewhere in the palette, giving search and form fields a recessed, catalogue-like feel. **nav-bar** is inferred from the max-width, centered `body` container and the `.languageHeader`/`.footerHeaderStyle` classes, suggesting a white top bar with bold uppercase green or black labels for the large mega-menu of tool categories. **product-card** draws on `.productTitleStyle` (bold black title on white) to lay out tool thumbnails, names, and specs with a thin hairline border, appropriate for the dense product-category listings evidenced in the page text. **hero** is a proposed banner treatment using the green background with white bold text, echoing `.productTitleBiggerStyle`'s white-on-dark pairing, suited to campaign banners like "New W15 Series Angle Grinders." **footer** is inferred from `.footerHeaderStyle`/`.footerSubMenuHeaderStyle`, using a darker green tone with small uppercase white labels for the many regional/site links and service info. **badge** is a proposed component using the recurring red accent family to flag safety notices, new-product callouts, or recall/warning messaging, consistent with the "Important Safety/Recall Notices" content on the page. **search** is proposed as a light grey field styled like text-input, positioned for the "Search Suggestions" functionality referenced in the extracted text. **battery-compat-tag** is a category-appropriate, proposed component for labeling 12V/18V battery-pack system compatibility on product listings, using the tonal green accents observed in the palette to visually group Metabo's cordless ecosystem.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column nav collapses to hamburger; category mega-menu becomes accordion |
| Tablet | 600–1024px | 2-column product grid; sticky search bar |
| Desktop | 1024–1280px | Matches observed `body{max-width:1280px}` container; multi-column mega-menu |
| Wide | >1280px | Content remains capped at 1280px, centered per observed `margin:0 auto` |

Touch targets should be a minimum 44×44px for button and nav components; the extensive nested category menu implied by the page text suggests collapsing sub-lists behind expandable disclosure controls on narrow viewports. None of this responsive behavior was directly observed; it is inferred from the single fixed-width container rule captured in evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, hover/focus states, animations, or actual mobile breakpoints were observed. Color-to-role mapping (e.g. which red is used for alerts vs. accents, which green variant serves as primary vs. hover) is inferred from repeated usage patterns in class names like `boxHeaderGreenStyle`, not confirmed visually. Typography sizes for `display-xl` and `body-md` are proposed extrapolations, not directly present in the supplied CSS. The proprietary "Metabo W01 Regular," "MetaboSans," and "MetaboSlab" fonts are referenced in the stylesheet but their licensing, availability, and exact letterforms were not verified. Component states (hover, active, disabled, error) are entirely proposed and unobserved. The `battery-compat-tag` and other category-specific components are speculative design proposals based on the product taxonomy described in the page text, not on captured UI markup.
