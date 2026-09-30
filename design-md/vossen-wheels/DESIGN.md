---
version: alpha
name: "Vossen Wheels"
source_url: "https://vossenwheels.com"
captured_at: "2026-09-28T09:42:03.148393+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Vossen Wheels' public site evidence shows a WordPress/Gutenberg-based build using default block-editor color slugs (very-light-gray #eee, very-dark-gray #313131) alongside a bold saturated red (#d21c24) and a darker red (#9c1116) that appear distinct from the WordPress admin/editor defaults (#007cba family) and from generic Gutenberg swatches (#0693e3, #ff6900, #00d084, etc.), which are treated as unused CMS palette noise rather than brand color. The red is inferred as the brand primary/accent given its saturation and separation from neutral tones, consistent with automotive performance branding; this mapping is inferred, not confirmed by a style guide.

  Typography is set in Arial/Helvetica/Open Sans with sans-serif fallback and no custom display face was observed; the "slick" family reference is a carousel icon font, not body type. A 16px "normal" and 42px "huge" preset size pair anchors the proposed type scale. Buttons observed with fully rounded pill radius (9999px) and a dark slate fill (#32373c) inform the button-primary/secondary treatment. The overall interpretation favors a dark, industrial, high-contrast layout (near-black ink on white canvas, light gray surfaces for cards) suited to a forged-wheel manufacturer, with red reserved for calls-to-action and emphasis. All spacing, radii beyond the observed pill, and layout structure are proposed conventions, not measured.

colors:
  primary: "#d21c24"
  primary-dark: "#9c1116"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#eeeeee"
  surface-dark: "#313131"
  button-dark: "#32373c"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.button-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  fitment-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed pill radius (9999px) seen on `.wp-block-button__link` and the inferred brand red as fill, intended for primary CTAs like "Explore all wheels" or "Request a Quote." Hover/active states are proposed only, not observed.

**button-secondary** reuses the dark slate `#32373c` fill directly evidenced on block buttons, paired with the same pill radius, for secondary actions (e.g., "Find a Dealer") that should not compete visually with the primary red CTA.

**text-input** is a proposed pattern for contact/quote forms and dealer search, using canvas background, hairline border, and small radius; no input styling was present in the supplied CSS, so all visual details here are inferred conventions.

**nav-bar** is proposed as a dark, near-black bar carrying the site's persistent header links (Store, Wheels, Gallery, Find a Dealer) and phone number, consistent with the industrial, high-contrast tone suggested by the dark-gray/black palette entries; exact height and behavior were not observed.

**product-card** represents a wheel/finish listing tile (e.g., GNX-05, HFX-5) using the light gray card surface (#eeeeee) against white canvas, with a title/spec typography pairing; card shadow, hover elevation, and grid spacing are proposed, not measured.

**hero** models the homepage lead area ("Meet the worlds best" / forged pricing callouts) on the dark surface color with large display type and a primary CTA button; exact hero height, imagery treatment, and text alignment are inferred.

**footer** is proposed on the same dark-gray surface used elsewhere in the evidence, carrying navigation groupings (Wheels, Galleries, Manufacturing, Blog) and the copyright line; link color and column layout are proposed.

**badge** is a small pill label using the primary red, suited to flags like "New Release," "TÜV Verified," or lug-pattern tags (5-Lug/6-Lug/8-Lug) seen in the gallery text; this is a proposed component, not a directly observed UI element.

**search** is a proposed rounded search/filter field for the dealer locator or wheel gallery, styled with the light soft-gray surface and hairline border; no search markup was present in the supplied CSS.

**fitment-selector** is a category-appropriate proposed component for vehicle/wheel fitment filtering (make, model, lug pattern, bolt pattern) referenced implicitly by the Vehicle Gallery and lug-count labels (5/6/8-Lug) in the page text; styling is inferred from the general card/surface palette since no fitment-tool CSS was supplied.

## Responsive Behavior

Proposed breakpoints (not measured from live site): mobile ≤480px, tablet 481–1024px, desktop 1025px+. Below tablet, nav-bar collapses to a hamburger/off-canvas menu; product-card grids reduce from 4/3 columns to 1–2 columns; hero display type scales down toward `{typography.display-md}` sizing. Touch targets on button-primary/secondary and search should maintain a minimum 44px height using `{spacing.md}`–`{spacing.lg}` vertical padding. This section is a recommendation only; no responsive CSS or media queries were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only; no live rendering, computed styles, or DOM screenshots were available. Semantic color roles (primary red, dark surfaces, button-dark) are inferred from Gutenberg utility classes and observed inline button styles, not from a documented brand style guide, so exact brand-color intent is unconfirmed. Most typography sizes beyond the two WordPress presets (16px/42px) are proposed scale values, not extracted CSS. No custom/proprietary display font was found — Open Sans/Arial/Helvetica with sans-serif fallback is the only evidenced stack, and its licensing/availability was not verified here. Interaction states (hover, focus, active, disabled), mobile menu behavior, and actual card/grid layout were not observed and are marked proposed throughout. Several WordPress default swatches (Gutenberg presets like #0693e3, #ff6900, #cf2e2e, etc.) appear in the palette but are treated as unused editor defaults rather than brand colors, given the site's actual visible red/gray/black usage pattern.
