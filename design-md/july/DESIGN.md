---
version: alpha
name: "July"
source_url: "https://july.com"
captured_at: "2026-09-28T09:12:13.132238+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  July's storefront evidence points to a high-contrast, editorial travel-goods aesthetic built on a black/white core with warm neutral supports. The root body sets a black background with white foreground variables, and utility classes force pure black text/borders on interactive elements, indicating a stark monochrome UI skeleton. Warm off-whites (#f7f6f4, #fbf7f0, #f4f4f4) recur as likely card/section surfaces against true white and true black, while a muted gray (#666666) and a light hairline gray (#d3d3d3, used on the observed circular close-button border) suggest secondary text and dividers. A small cluster of desaturated accent hues — olive (#a5a987), terracotta (#ca7a4f), deep forest (#203c2b), burgundy (#6f2b31), and indigo (#3e4288) — appears in the palette and is interpreted here as seasonal/collection accent color, not core UI color; this mapping is inferred, not confirmed by layout evidence.
  Typography draws on an extensive custom "July" font family set (July Sans Serif, July Bold, July Autograph, etc.) alongside editorial serif candidates (PPEditorialNew, Georgia) and a monospace stack for code-like UI. Display type is assigned to an editorial serif per brand-marketing convention common to DTC luggage sites; this pairing is proposed, not observed in layout. Body and UI text use July Sans Serif, matching the one concretely observed UI rule (.select-button: 14px/500). The toggle/select-button pattern (unselected white-on-black outline vs. selected black fill with asymmetric bottom radius) is treated as the basis for the category-specific size/variant selector.

colors:
  primary: "#000000"
  ink: "#171513"
  canvas: "#ffffff"
  body: "#1c1c1c"
  muted: "#666666"
  hairline: "#d3d3d3"
  surface-soft: "#f7f6f4"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  surface-warm: "#fbf7f0"
  border-subtle: "#cccccc"
  accent-olive: "#a5a987"
  accent-terracotta: "#ca7a4f"
  accent-forest: "#203c2b"
  accent-indigo: "#3e4288"
  accent-burgundy: "#6f2b31"
typography:
  display-xl: {fontFamily: "PPEditorialNew, Georgia, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "PPEditorialNew, Georgia, serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "July Bold, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "July Sans Serif, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "July Sans Serif, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "July Sans Serif, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "July Sans Serif, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
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
    border: "1px solid {colors.hairline}"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border-bottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    placeholderColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackgroundColor: "{colors.primary}"
    textColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    selectedRounded: "0 0 {rounded.lg} {rounded.lg}"
    padding: "{spacing.sm} {spacing.none}"

## Components

**button-primary** is the core call-to-action treatment (e.g. "Quick add", "Shop All"), rendered black-on-white per the `--tw-bg-opacity` black body rule and forced-black button/border utility classes observed in the CSS bundle.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Discover our collections"), using the canvas surface with a hairline border, inferred from the general monochrome system rather than a directly observed secondary-button rule.

**text-input** covers newsletter signup and search fields; styling is proposed from generic input resets (`font: inherit`, no native chrome) combined with the hairline border used elsewhere.

**nav-bar** represents the persistent header (Luggage / Bags / Accessories / Set & Save / Personalization / Shop All / Help). Background and text colors are inferred as canvas/ink for a light header, since the only directly observed nav-adjacent color (`#1f3e3c`) was excluded for not appearing in the supplied palette array.

**product-card** models the best-seller/new-arrival grid items with price, swatch count ("+9", "+7"), and quick-add affordance seen in the page text; padding and radius are proposed, not measured.

**hero** models the top marketing banner ("Elevate your travel experience") as a full-bleed dark section with large display type; imagery and exact copy placement are not observed and are proposed.

**footer** reflects the three-column link structure (PRODUCTS / ABOUT / SUPPORT) plus legal/copyright text, using the confirmed body-level black background as its base color.

**badge** covers "Best Seller" and "New Arrival" labels visible in the product grid text; color choice (terracotta) is an inferred accent assignment, not a confirmed badge color.

**search** models the overlay search panel ("Search luggage, bags & more") paired with the observed circular `.close-button` treatment (1px `#d3d3d3` border, 50% radius, 10px padding) for its dismiss control.

**size-selector** is the category-specific component for choosing luggage size/variant (Carry On, Checked, Checked Plus). It is directly grounded in the observed `.select-button` / `.select-button.selected` rules: unselected state is white fill with black text and a black border; selected state inverts to black fill with white text and adds an asymmetric bottom border-radius (20px), reproduced here via `{rounded.lg}` on the bottom corners only.

## Responsive Behavior

This is a recommended pattern, not measured site behavior; no breakpoints, container queries, or mobile layouts were present in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| xs | 0–479px | Single-column product grid, collapsed nav into a menu drawer |
| sm | 480–767px | 2-column product grid, search overlay full-screen |
| md | 768–1023px | 2–3 column grid, inline nav with condensed spacing |
| lg | 1024–1439px | Full horizontal nav, 3–4 column product grid |
| xl | 1440px+ | Max-width content container, 4-column grid, larger hero type |

Touch targets should be a minimum 44×44px for quick-add and size-selector controls. Nav categories should collapse into a hamburger/menu pattern below `md`. The size-selector's toggle group should stack to full-width buttons on `xs`/`sm`. None of this is confirmed by DOM or viewport evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, spacing, or breakpoint behavior was observed.
- Color-to-role mapping (e.g. which accent applies to badges vs. seasonal collections) is inferred from palette presence, not confirmed component usage.
- Display/heading font pairing (PPEditorialNew/Georgia) is a plausible editorial-brand convention, not verified against an actual heading element in the supplied CSS.
- Font availability, licensing, and web-font loading for all "July"-prefixed proprietary families are unverified.
- Interaction states beyond `.select-button`/`.select-button.selected` and `.close-button` (hover, focus, disabled, error) were not present in evidence and are proposed defaults.
- Mobile menu, search overlay, and quick-add drawer behavior are not observed; only their presence in page text/CSS class names is confirmed.
- Numeric sizes in the typography and spacing scales beyond the one confirmed rule (`.select-button`: 14px/500) are proposed, not measured.
