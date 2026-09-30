---
version: alpha
name: "SVS Sound"
source_url: "https://svsound.com"
captured_at: "2026-09-28T04:25:34.578180+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The SVS Sound stylesheet resolves to a high-contrast neutral system: near-black ink (#121212, #0f0f0f) on white (#ffffff) canvas, with a cool utility blue (#376cb1) driving interactive elements such as the Okendo review widget buttons and header sale-badge text (#549eff). Secondary neutrals span light grays (#f0f3f5, #f5f5f5, #dedede, #cccccc) for soft surfaces and hairlines, while darker slate tones (#1f2021, #242833, #29333d) suggest card or footer backgrounds inferred from a dark-mode section pattern. Accent hues (#ff4d95, #ffd200, #00caaa) appear sparsely and are treated here as promotional/badge accents rather than core brand color, since their component context is not confirmed. Typography is set in Assistant, a humanist sans-serif, with Arial as the observed system fallback; Baskerville also appears in the family stack but its applied role (heading vs. body) is not confirmed by the supplied rules, so it is treated as a possible display serif candidate only, not assigned to a token here. This interpretation proposes a clean e-commerce audio-brand system: confident black/white contrast, a single blue action color, and restrained accent usage reserved for sale/badge messaging. Layout, spacing, and interaction states below are proposed conventions for a product-catalog site, not measured observations.

colors:
  primary: "#376cb1"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#0f0f0f"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f0f3f5"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-blue: "#549eff"
  accent-pink: "#ff4d95"
  accent-yellow: "#ffd200"
  accent-teal: "#00caaa"
  dark-surface: "#1f2021"
  dark-surface-alt: "#242833"
  border-strong: "#0f0f0f"
  overlay: "#00000099"
typography:
  display-xl: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "15px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Assistant', Arial, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.3px"}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    typography: "{typography.title-md}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  spec-comparison-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md}"

## Components
**button-primary** uses the observed Okendo review-widget blue (#376cb1) as a stand-in for the site's primary action color, since the header's action buttons were not directly captured; hover/active states are proposed as identical fill per the widget's own hover-equals-active pattern.

**button-secondary** is a black-outline-on-white pattern inferred from the `:root` color-button variables (foreground 18,18,18 on white background), suited for "Add to Cart" alternates or filter toggles.

**text-input** proposes a light hairline border (#dedede) with square-to-slightly-rounded corners, consistent with the flat, no-radius button styling (`--oke-button-borderRadius:0`) observed in the review widget.

**nav-bar** is inferred as a white header bar with dark text and a thin hairline divider; the sale-callout span color (#549eff) suggests promotional text is distinguished from standard nav links via accent color rather than weight alone.

**product-card** proposes a soft off-white card surface (#f5f5f5) to separate speaker/subwoofer product tiles from the white page canvas, with title-md used for product names.

**hero** is a proposed dark full-bleed banner using one of the observed dark slate tones (#1f2021), since image-overlay text rules confirm white (#ffffff) text is placed over imagery in at least one section.

**footer** uses a deeper slate (#242833) as an inferred multi-column footer background, paired with white body text for contrast, consistent with the site's evident dark/light section alternation.

**badge** repurposes the observed yellow (#ffd200) for sale/promo pills, kept small and pill-shaped (full radius) to read as a secondary, non-primary accent distinct from the blue action color.

**search** is a proposed light-gray input treatment matching the `#f0f3f5` surface tone, giving it a visually recessed appearance relative to the pure-white page background.

**spec-comparison-table** is proposed for subwoofer/speaker technical specs, using the light surface tone and hairline dividers to keep dense numeric data legible without heavy borders.

## Responsive Behavior
This is a recommended pattern set, not measured site behavior:
| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid, nav collapses to hamburger, touch targets ≥44px |
| Tablet | 600–1024px | 2-column product grid, nav may remain inline or collapse depending on item count |
| Desktop | 1024–1440px | 3–4 column product grid, full horizontal nav |
| Wide | >1440px | Max-width content container, additional whitespace at page edges |

Buttons and nav links should maintain a minimum 44×44px touch target on mobile; the hamburger/mega-menu collapse point is a proposed convention, not confirmed by the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/custom-property extraction only; no rendered layout, breakpoint behavior, or JavaScript-driven interaction (menus, carousels, cart drawers) was directly observed. The primary action color is inferred from the Okendo review-widget's `--oke-button-*` variables (#376cb1), not from a confirmed site-wide "add to cart" or nav button. Accent colors (#ff4d95, #ffd200, #00caaa, #549eff) are present in the palette but their exact component usage (badges vs. sale banners vs. illustration) is not confirmed. Dark slate tones are assumed to represent footer/section backgrounds by convention, not by a captured dark-section rule. Baskerville appears in the font-family evidence but no selector ties it to a specific role, so it is not assigned to any typography token; Assistant is used throughout with Arial as the observed system fallback, and generic sans-serif is added defensively. All pixel sizes in typography, rounded, and spacing scales beyond the observed 15px body font-size are proposed conventions for a product-catalog site. Custom font hosting, licensing, and availability for Assistant/Baskerville were not verified.
