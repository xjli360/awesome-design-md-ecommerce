---
version: alpha
name: "Rabbit"
source_url: "https://rabbit.tech"
captured_at: "2026-09-28T09:24:51.132281+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Rabbit's marketing site for OS3 runs on a near-black canvas (#000000) with warm off-white body copy (#e2dcd1) and a saturated orange accent (#ff4d06, with a close sibling #ff5c00) driving buttons, links and emphasis marks. The palette otherwise leans on a tight ramp of dark neutrals (#131516, #1c1c1c, #1a1a1a, #222222, #393939) for card and section separation, plus translucent whites/blacks (#ffffff33, #00000066) that read as hairlines and overlay scrims. Two custom local fonts are loaded via Next.js font optimization: a font whose generated family name contains "archivo" for body and interface text, and one containing "powerGrotesk" for larger display treatment — both ship with matching fallback family names and no verified generic mapping beyond the sans-serif stack applied here.
  This interpretation treats the site as a dark, technical, product-led surface: black canvas, warm-white body text, and a single hot-orange accent reserved for primary actions and highlighted words, consistent with the one confirmed button rule (`background-color:#ff4d06`, black text, 17px radius). Card surfaces, hairlines, muted grays, and the full type scale beyond the one measured body rule are inferred/proposed and not directly observed in layout. Sparse reds (#ba0000, #e40606) and amber (#ffb000) are treated as reserved status/alert accents given their low presence in the palette.

colors:
  primary: "#ff4d06"
  primary-alt: "#ff5c00"
  ink: "#ffffff"
  canvas: "#000000"
  body: "#e2dcd1"
  muted: "#8a8a8a"
  hairline: "#ffffff33"
  surface-soft: "#131516"
  surface-card: "#1c1c1c"
  surface-card-alt: "#1a1a1a"
  border-soft: "#393939"
  on-primary: "#000000"
  danger: "#ba0000"
  alert: "#e40606"
  warning: "#ffb000"
  overlay-scrim: "#000000b3"
typography:
  display-xl: {fontFamily: "__powerGroteskFont_859336, __powerGroteskFont_Fallback_859336, sans-serif", fontSize: 64px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -1px}
  display-md: {fontFamily: "__powerGroteskFont_859336, __powerGroteskFont_Fallback_859336, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  title-md: {fontFamily: "__archivoFont_931059, __archivoFont_Fallback_931059, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "__archivoFont_931059, __archivoFont_Fallback_931059, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.56, letterSpacing: 0px}
  body-sm: {fontFamily: "__archivoFont_931059, __archivoFont_Fallback_931059, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "__archivoFont_931059, __archivoFont_Fallback_931059, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "__archivoFont_931059, __archivoFont_Fallback_931059, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
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
    rounded: "{rounded.lg}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.border-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  model-picker:
    backgroundColor: "{colors.surface-card-alt}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary** is grounded directly in the one confirmed CSS rule (`.waitlist-klaviyo-form button`): black text on `#ff4d06`, previously observed with a 17px radius, here mapped to the nearest scale token (`{rounded.lg}`). Hover/disabled states are proposed, not observed.

**button-secondary** is an inferred outline treatment for lower-emphasis actions (e.g. "download", "explore"), using a soft dark border against the black canvas rather than a filled background.

**text-input** proposes a dark, slightly-lifted field (`{colors.surface-soft}`) for forms such as the Klaviyo waitlist signup, with a translucent hairline border since no literal input styling was captured in evidence.

**nav-bar** reflects the persistent top navigation implied by the page text ("OS3 r1 updates creations blog newsroom support"), rendered as a flat black bar with a bottom hairline; exact height, sticky behavior, and active-link styling are not observed.

**hero** models the top-of-page "start with the thought" section: full-width black background, large display type, generous section padding. Copy hierarchy and any background imagery/video are not confirmed by the evidence.

**product-card** is a proposed pattern for r1/OS3 feature tiles referenced in the body copy (e.g. "research you can actually use," "that folder you keep putting off"), using a card surface one step lighter than the page background to imply depth on a dark theme.

**footer** assumes a minimal dark footer consistent with the canvas color and muted gray text, separated by a hairline; link structure and legal content are not present in the supplied evidence.

**badge** is proposed for short status labels (e.g. "new" next to r1 updates), using the secondary orange as a compact pill, distinguishing it from the primary button color.

**search** is a proposed, unobserved component for locating support/FAQ content given the long question list in the excerpt ("what is OS3?", "do I need a perfect prompt?"), styled as a pill-shaped dark field.

**model-picker** is a proposed component specific to this product: a compact selector row/list styled to hold the long enumerated model names (claude-opus-5, gpt-6-astra, etc.) seen in the BYOK section, using card-level surface contrast rather than full-black.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:
| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <640px | Single-column stacking; nav collapses to a menu control; touch targets ≥44px. |
| tablet | 640–1024px | Two-column card grids where applicable; nav remains visible or condensed. |
| desktop | >1024px | Multi-column layout for feature sections and model lists; hover states enabled. |

Body-level CSS variables (`--mobile-margin:50px`, `--mobile-gutter:20px`, `--mobile-columns:4`) were observed and suggest a 4-column mobile grid with 50px outer margin and 20px gutters, but the corresponding tablet/desktop grid values were not present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, animation, or interaction states were observed. The dark-theme color-role mapping (canvas/ink/body/surface tiers) is inferred from a single body background rule and a single text-color utility class, not from a full style audit. Font-family values are reproduced exactly as emitted by Next.js local font optimization (hashed variable-style names); their true typeface identity, licensing, and availability as "Archivo" or "Power Grotesk" specifically have not been verified. All typography sizes except the one measured `.text-global-body` rule (16px/400/25px) are proposed, not observed. The border-radius scale and spacing scale follow the required fixed schema rather than being derived from evidence beyond the single 17px button radius. Component states (hover, focus, active, disabled), mobile navigation collapse behavior, and grid breakpoints above mobile are not observed and are marked proposed throughout.
