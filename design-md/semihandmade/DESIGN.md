---
version: alpha
name: "Semihandmade"
source_url: "https://semihandmade.com"
captured_at: "2026-09-29T04:02:52.191535+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Semihandmade's CSS evidence shows a Bootstrap-derived utility system layered with brand-specific type and a warm-coral accent. Headings use "Domaine Sans Text Regular" at font-weight 400, giving a quieter, editorial display voice rather than a bold slab; buttons use "GT America Bold Helvetica" at weight 700, creating clear contrast between calm headlines and assertive calls-to-action. The observed palette centers on a coral/red family (#f16154, #f16255, #d15449) used for accents and CTAs, paired with a deep navy (#001838) and a slate-blue (#43576b) that appears on the header and off-canvas navigation backgrounds. Bootstrap's neutral grays (#f8f9fa, #e9ecef, #ced4da, #6c757d, #212529) supply body text, borders, and light surfaces; a warm off-white (#f7f4f0) is treated here as a card surface to suit a home-goods/materials catalog. Role assignments beyond header background and button styling (e.g. body text color, hairlines, card surfaces) are inferred from Bootstrap defaults and general contrast logic, not confirmed page screenshots. No custom breakpoints, spacing scale, or corner-radius values were observed at scale; those below are proposed conventions sized for a product/e-commerce catalog with swatch and door-style browsing.

colors:
  primary: "#f16154"
  primary-strong: "#d15449"
  ink: "#001838"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#ced4da"
  surface-soft: "#f8f9fa"
  surface-card: "#f7f4f0"
  on-primary: "#ffffff"
  secondary-nav: "#43576b"
  footer-ink: "#151531"
  accent-warm: "#faba0a"
  success: "#198754"
  link: "#3182ce"
typography:
  display-xl: {fontFamily: "'Domaine Sans Text Regular', Helvetica, Arial, sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Domaine Sans Text Regular', Helvetica, Arial, sans-serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Domaine Sans Text Regular', Helvetica, Arial, sans-serif", fontSize: "22px", fontWeight: 400, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'GT America Bold Helvetica', Arial, sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1.5, letterSpacing: "0.2px"}
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
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.secondary-nav}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
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
  material-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xs}"

## Components

**button-primary** carries the coral CTA color observed across the palette (e.g. `#f16154`, `#d15449` variants) and the bold `GT America Bold Helvetica` button typography confirmed in the `.btn` CSS custom properties. Used for "Get Started," "Explore Options," and checkout actions.

**button-secondary** is a proposed outline variant sharing the same coral hue for text/border on a transparent field, intended for lower-emphasis actions like "Learn More" links seen throughout the copy.

**text-input** is a proposed neutral field using Bootstrap's light border tokens (`#ced4da`-class hairline) and body text color, sized for newsletter/search forms referenced in the footer sign-up block.

**nav-bar** reflects the observed `.section-header` and `#offCanvasMenu` background of `#43576b` with white text (`.section-header > *`), used for the sticky/off-canvas navigation containing the deep Getting Started/Cabinets/Collections menu tree.

**product-card** is a proposed catalog tile pattern for door-style and collection listings ("Shaker - Stone," "Slab - Tahoe"), using a warm off-white surface distinct from pure white canvas to suit material imagery.

**hero** is a proposed full-width banner pattern for the homepage lead ("Cabinet Doors for 50K+ IKEA Projects"), using display-xl heading typography and generous section padding.

**footer** uses the darker navy (`#151531`) present in the palette as a plausible footer background, with link-blue (`#3182ce`) for utility links (Privacy Policy, Terms), matching the extensive footer link list in the evidence.

**badge** is a proposed small pill using the observed yellow (`#faba0a`) for promotional flags such as "new!" or "Clearance," not confirmed against a specific rendered element.

**search** models the offcanvas/global search field referenced in the nav ("Open Search," "Offcanvas Search") with a soft neutral background.

**material-swatch-selector** is a category-specific proposed component for browsing finishes (DIY, Thermofoil, Painted, Walnut) with an active-state border in the primary coral to indicate selection.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior; only Bootstrap's default breakpoint variables (`--bs-breakpoint-*`: 576/768/992/1200/1400px) were present in evidence.

| Breakpoint | Width | Notes |
|---|---|---|
| xs | 0–575px | Single-column stacking; off-canvas nav becomes primary navigation pattern (menu structure observed in evidence). |
| sm | 576–767px | Two-column swatch/product grids proposed. |
| md | 768–991px | Header height (`--header-height: 76px` observed) likely fixed; announcement banner (`61px` observed) may collapse or persist. |
| lg | 992–1199px | Three-column product/material grids proposed. |
| xl+ | 1200px+ | Four-column grids proposed; max content width not observed. |

Touch targets should meet a 44px minimum tap area for swatch selectors and nav items (proposed, not measured). Off-canvas menu collapse/expand interaction is referenced in copy ("Offcanvas Search," "Back" labels in nav) but exact animation/timing was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered screenshots, computed layout, or live interaction states (hover, focus, active) beyond the `.btn` pseudo-class rules were verified. Color role assignments (e.g., body text, card surfaces, footer background) are inferred from Bootstrap conventions and general contrast logic rather than confirmed against on-page usage of each hex value. All spacing, rounded-corner, and typographic sizes not explicitly present in the supplied CSS (most font sizes, all spacing/radius values) are proposed defaults suited to an e-commerce/materials catalog, not measured site values. Breakpoint behavior, mobile menu mechanics, and grid column counts are recommendations only. Availability, licensing, and correct rendering of "Domaine Sans Text Regular" and "GT America Bold Helvetica" as web fonts were not verified; system fallbacks (Helvetica, Arial, sans-serif) should be assumed until confirmed.
