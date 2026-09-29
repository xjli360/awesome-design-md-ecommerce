---
version: alpha
name: "Bella & Duke"
source_url: "https://bellaandduke.com"
captured_at: "2026-09-28T09:52:59.082708+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Bella & Duke's public CSS evidence centers on a deep teal (#003a3a, also seen as
  #003b3b) used for the WordPress admin/sidebar chrome, paired with a bright yellow
  (#fff964) as a hover/icon accent within that same internal tooling context. Because
  no storefront-scoped color variables resolved in the extracted CSS (button colors
  reference unresolved Elementor global-color custom properties), the teal and yellow
  pairing is treated here as an inferred brand identity signal rather than a confirmed
  UI token, reused across primary and accent roles. Supporting neutrals (#ffffff,
  #fffdf5, #f0ece4, #333333, #666666, #e0e0e0) are drawn from the broader observed
  palette and assigned to canvas, surface, body-text, and hairline roles by inferred
  convention for a warm, natural-food editorial feel. #00b67a is retained specifically
  for Trustpilot-style review badges, matching its real-world brand association visible
  in the page copy. Typography is grounded in the one confirmed UI font stack, "DM
  Sans", used verbatim in button CSS (font-size 18px, line-height 36px, weight normal),
  extended here to body and UI text. "Youth" appears in the observed font list and is
  tentatively assigned to display headings, though its actual usage location, weights,
  and licensing are unverified. The 8px button border-radius is directly observed and
  used as the base rounded-md token throughout.

colors:
  primary: "#003a3a"
  secondary-teal: "#446161"
  accent-yellow: "#fff964"
  accent-orange: "#ff6900"
  success-green: "#00b67a"
  warm-peach: "#fdd187"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  surface-soft: "#f0ece4"
  surface-card: "#fffdf5"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "Youth, DM Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Youth, DM Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "DM Sans, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "DM Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "DM Mono, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "DM Sans, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 36px, letterSpacing: 0px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    hoverTextColor: "{colors.accent-yellow}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nutrition-calculator:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.warm-peach}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.body-sm}"
    resultTypography: "{typography.display-md}"

## Components

**button-primary** models the observed `.bd-cta-spirulina` pattern: a solid teal fill with white text and an 8px radius directly copied from the CSS `border-radius: 8px` rule. This is used for the site's "Try Now" and "Get Their Perfect Meals" calls to action.

**button-secondary** mirrors `.bd-cta-spirulina-outline`, an inverted treatment with a transparent/canvas fill and a 2px teal border, intended for lower-emphasis actions alongside a primary CTA. Hover-state color shift to `#446161` is proposed based on the sibling hover rule.

**text-input** is a proposed pattern for the pet-details calculator form ("How old is your pet?", weight entry) since no dedicated input CSS was present in evidence; sizing and border follow the neutral hairline token.

**nav-bar** infers a teal header bar consistent with the site's admin-bar/sidebar teal, with yellow hover text matching the one confirmed `--wpext-sidebar__text-hover` variable. Actual public-facing nav styling was not present in evidence.

**hero** proposes a soft warm background for the top banner introducing the "40% off" offer and subscription pitch, using large display typography; exact hero markup/CSS was not captured.

**product-card** is proposed for the recipe/range tiles described in the page copy (e.g., "Adult Dog + Premium Complete," "Cat + Kitten + Premium Complete"), using the card surface tone and hairline border for separation.

**footer** assumes the teal brand color continues into the footer band for visual bookending, consistent with the one confirmed dark teal token; footer layout itself is unobserved.

**badge** is proposed for the Trustpilot rating indicator referenced in the page text, using the Trustpilot-associated green already present in the observed palette.

**nutrition-calculator** is a category-appropriate component modeling the "Get Your Personalised Price" daily-amount/daily-cost calculator described in the page text, combining a card surface with a warm accent and large numeric result typography; no calculator-specific CSS was captured.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column stacking; nav collapses to a hamburger/off-canvas panel; calculator fields stack vertically. |
| Tablet | 600–1023px | Two-column product grids (consistent with observed `grid-col-tablet-2` utility class); condensed nav. |
| Desktop | 1024px+ | Multi-column layout up to the observed `--wp--style--global--wide-size: 1200px` content ceiling. |

Touch targets should be a minimum of 44px, satisfied by the observed 50px button height. Nav collapse thresholds, grid column counts, and exact stacking behavior are recommendations only, not measured from a live render.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- CSS was extracted statically; no JavaScript-driven states (hover, focus, open menu, calculator interactions) were observed or verified.
- Primary/accent button colors reference unresolved Elementor CSS custom properties (`--e-global-color-*`); their actual hex values were not present in evidence, so semantic color-to-role mapping (primary, on-primary) is inferred rather than confirmed.
- "Youth" appears only in the raw font-family list; its assigned use for display headings, its available weights, and its licensing/availability are unverified.
- Mobile and tablet layouts are proposed conventions based on generic responsive patterns and one grid-column utility class name, not confirmed breakpoints or measured viewport behavior.
- Spacing scale, border-radius scale (beyond the one observed 8px value), and component padding are proposed defaults for design consistency, not extracted measurements.
- No product photography, imagery treatment, or iconography details were present in evidence.
