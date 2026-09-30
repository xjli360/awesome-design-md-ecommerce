---
version: alpha
name: "Strasser Wood"
source_url: "https://strasserwood.com"
captured_at: "2026-09-29T04:15:25.233741+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Strasser Wood's public site pairs a serif display face (Libre Baskerville, falling
  back to Georgia) with a light-weight sans body face (Lato, falling back to
  Helvetica Neue/Helvetica/Arial), an observed pairing that signals custom
  woodworking heritage (serif headlines) against a clean, showroom-catalog
  utility (sans body/UI). The observed palette is warm and low-saturation:
  a near-black charcoal family (#1b1c18, #2a2b27, #3a3b35) for text and dark
  surfaces, a warm-white/beige family (#faf8f5, #f0ebe5, #e3d9d2, #d0c8c0) for
  page background, cards, and primary CTAs, and two muted accent tones
  (#768a8f, a dusty blue-grey; #68605a, a warm taupe) whose exact usage in the
  live site is not confirmed from static CSS alone and is therefore treated as
  inferred secondary/tertiary accent. A single warm red (#b94040) appears in
  the palette but its functional role (alert, sale badge, or decorative) is
  unverified and is mapped here only as an optional alert/accent color.
  Buttons are observed as square-cornered, uppercase, letter-spaced
  (0.22em), which this spec generalizes into a squared-off, minimal-radius
  design language across components, while still offering a conservative
  rounded scale for any softer UI needs. Body copy is set light (weight 300)
  at 1.5 line-height, consistent with an editorial, spacious cabinetry
  catalog rather than a dense e-commerce grid.

colors:
  primary: "#e3d9d2"
  ink: "#1b1c18"
  canvas: "#faf8f5"
  body: "#1b1c18"
  muted: "#888885"
  hairline: "#d0c8c0"
  surface-soft: "#f0ebe5"
  surface-card: "#ffffff"
  on-primary: "#1b1c18"
  ink-2: "#2a2b27"
  ink-3: "#3a3b35"
  body-secondary: "#4a4a46"
  accent-cool: "#768a8f"
  accent-warm: "#68605a"
  alert: "#b94040"
typography:
  display-xl: {fontFamily: "'Libre Baskerville', Georgia, serif", fontSize: 64px, fontWeight: 400, lineHeight: 1.08, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Libre Baskerville', Georgia, serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.08em}
  button-md: {fontFamily: "'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.22em}
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
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.primary}"
    hover:
      backgroundColor: "transparent"
      textColor: "{colors.primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid rgba(255,255,255,0.45)"
    hover:
      backgroundColor: "rgba(255,255,255,0.1)"
      border: "1px solid {colors.canvas}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    overlay: "rgba(0,0,0,0.25)"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink-2}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"

## Components

**button-primary** is drawn directly from the observed `.btn-primary` rule: a beige-filled, square-cornered, uppercase, letter-spaced call-to-action ("Open the Configurator") that inverts to an outline on hover. **button-secondary** mirrors the observed `.btn-ghost` treatment used over the dark hero image: a transparent, white-bordered ghost button. **text-input** is proposed, generalizing the site's HubSpot form fields (`.showroom-form-wrap .hs-form`) into a plain, square-cornered field with a hairline border; exact padding/border styling on inputs themselves was not directly supplied and is inferred. **nav-bar** is proposed from the page's evident top-level navigation structure (Collections, Products, About, Resources, phone number) but no header CSS was supplied, so background/spacing are inferred defaults on the canvas color. **hero** reflects the observed `.hero h1` styling (serif display type, white text, dark overlay implied by text-shadow) atop what is presumably a photographic background image; the overlay color is proposed. **product-card** is proposed for the seven-collection grid (Alki, Belltown, SoDo, etc.) and the vanity-top/mirror/hardware category tiles; card chrome (border, radius) is inferred from the site's generally flat, hairline-bordered aesthetic rather than directly observed card CSS. **footer** is proposed using the dark charcoal-2 tone as a plausible footer surface, consistent with the dark hero and button treatments seen elsewhere; no footer-specific CSS was supplied. **badge** is proposed for small status labels like "Made to Order · Shipped in 2–3 Weeks" or "100% Made in USA," using the caption typography and a soft beige fill. **search** generalizes the "Item Look-Up" tool into a simple bordered search field, styling inferred from text-input conventions since no dedicated search CSS was supplied. **configurator-panel** is the category-appropriate component for this bathroom-fixtures brand's core "Vanity Configurator" workflow: a soft-surfaced panel intended to house collection/size/finish/hardware selectors, styled proposed and consistent with the observed beige-light surface tones, since no configurator-specific CSS was included in evidence.

## Responsive Behavior

Recommended breakpoints (not measured from the live site): mobile ≤480px, small tablet 481–768px, tablet 769–1024px, desktop 1025–1440px, wide ≥1441px. The observed hero headline uses a `clamp(40px, 5.5vw, 76px)` fluid scale, suggesting the live site already employs fluid typography at least for the hero; other breakpoint behavior is not observed. Navigation should collapse to a hamburger/off-canvas menu at ≤768px given the number of top-level sections (Vanities & Cabinets, Products, About, Inspiration, Resources). Touch targets for buttons and nav items should be at least 44×44px. Product/collection card grids should reflow from multi-column (desktop) to single or two-column (mobile). This section is a design recommendation only; no actual responsive CSS or breakpoints were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, computed box model, or interaction states (focus, active, error, loading) were observed, so all such states are proposed. Semantic color-role mapping (e.g., treating `--beige` as "primary") is inferred from a single observed CTA button and may not reflect the brand's full intended color system. The accent tones `#768a8f`, `#68605a`, and especially `#b94040` have unverified functional roles and are included conservatively. Typography sizes beyond the observed hero H1 (`clamp(40px,5.5vw,76px)`) and button label (11px/700/0.22em) are proposed approximations, not measured. Mobile/tablet layout, navigation collapse behavior, and card grid behavior were not observed and are recommendations only. Font availability, licensing, and self-hosting terms for Lato and Libre Baskerville were not verified from the supplied evidence and should be confirmed against actual font-loading/licensing before implementation.
