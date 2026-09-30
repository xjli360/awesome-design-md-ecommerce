---
version: alpha
name: "CarPro"
source_url: "https://carpro.global/"
captured_at: "2026-09-29T03:58:57.551136+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  CarPro's public site presents a stark, high-contrast industrial identity built almost entirely on black, white, and a narrow set of saturated accents. Buttons use a faceted, clipped-corner shape (polygon clip-path) rather than rounded corners, rendered in pure black (#000000) and white (#ffffff) with a red (#ff2400) border variant used for secondary/PPF-related calls to action. A muted gray system (#a5a7ac, #383c42, #525252, #cfd1d5, #dcdde2) supports body copy, hairlines, and card surfaces against the white canvas, while isolated accent hues — cyan (#00bbff), green (#32c82e), and a warm gold (#b4904d) — appear in the palette and are treated here as inferred category or status accents (e.g. coating/ceramic callouts, availability states) rather than confirmed UI roles, since no selector evidence ties them to a specific component. Typography is set in the site's custom "Basier Square" webfont (delivered via Next.js font-loading classes) with a system fallback chain; only the button label styling (12px, weight 500, uppercase, 0.6px tracking, line-height 2) is directly observed in CSS, so all other type sizes below are proposed extrapolations sized for a technical, product-driven detailing brand. The resulting interpretation favors sharp geometric buttons, tight uppercase labels, and a monochrome-first surface system accented sparingly by the observed hues.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#383c42"
  muted: "#a5a7ac"
  hairline: "#cfd1d5"
  surface-soft: "#f2f2f2"
  surface-card: "#dcdde2"
  on-primary: "#ffffff"
  accent-alert: "#ff2400"
  accent-info: "#00bbff"
  accent-success: "#32c82e"
  accent-gold: "#b4904d"
  ink-secondary: "#25282c"
typography:
  display-xl: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.2px}
  title-md: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "__basierSquare_635c71, __basierSquare_Fallback_635c71, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 2, letterSpacing: 0.6px, textTransform: uppercase}
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
    padding: "{spacing.sm} {spacing.lg}"
    border: "2px solid {colors.ink}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "2px solid {colors.accent-alert}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    hairline: "{colors.ink-secondary}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.ink-secondary}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  product-category-tab:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.base}"

## Components
**button-primary** renders the site's faceted black button with clipped top-left and bottom-right corners (observed via `Button_Button__EzMQW` polygon clip-path), white uppercase label, and a black-to-transparent hover fill sweep — hover/focus fill motion is proposed based on the `.Button_Bg__VgNDc` transform rule but the exact timing curve beyond the observed 0.3s ease is not verified.

**button-secondary** reuses the same faceted shape but swaps the border to the observed red (#ff2400), matching `Button_ButtonSecondary__4a_h7`; this variant is inferred to signal PPF/protection-tier actions given its use alongside "Immortal" PPF content, though no explicit semantic label was present in the CSS.

**text-input** is a proposed field style (no input CSS was supplied) drawing on the muted hairline gray and canvas background to stay consistent with the site's flat, high-contrast surfaces; corner radius is a light proposed softness distinct from the sharp button facets.

**nav-bar** is inferred from the black `Button_ButtonMenu__P0bV2` menu-button styling and site navigation text (PRODUCTS/ABOUT/SUPPORT/CONTACT); actual header layout, scroll behavior, and sticky state were not observed and are proposed.

**product-card** is a proposed container for PPF/coating listings (e.g. "Immortal Gloss 2.0", "MadMatte") using the light gray card surface and hairline border for separation from the white canvas; no card CSS was directly supplied.

**hero** models the homepage's black-background statement area ("Future is looking bright", 15-year anniversary copy) using the darkest observed neutral and largest proposed display type; exact hero imagery, video, or overlay treatment is not confirmed from CSS alone.

**footer** is inferred from the closing navigation list (FIND A INSTALLER, PRODUCTS, ABOUT, SUPPORT, legal links) and uses the same black surface as the primary button for brand consistency; column layout and link styling are proposed.

**badge** proposes a small pill treatment for flags such as the "WARNING – Fake Products Spotted" notice or "NEW" labels, using the red accent for urgency; no badge selector was present in the supplied CSS, so shape and color pairing are inferred from context.

**search** and **product-category-tab** are proposed patterns supporting the PRODUCTS mega-navigation (PREPARE / PROTECT / MAINTAIN / ACCESSORIES) implied by the footer sitemap text; active-tab contrast follows the black/white button logic already observed, but the actual filtering UI was not present in the supplied markup.

## Responsive Behavior
Recommended, not measured: mobile up to 599px (single-column stacking, nav collapses to the `Button_ButtonMenu__P0bV2`-style trigger), tablet 600–959px (2-column product grids), desktop 960–1439px (3–4 column grids, full nav visible), wide 1440px+ (max-width container matching the observed `.Button_container__9dhh0` 12-column grid with 15px gutters). Touch targets should stay at or above 44px height; the observed `ButtonMenu` is 55px tall, which comfortably meets this. Collapse the PRODUCTS mega-menu into an accordion below 960px. All breakpoint values are proposed conventions, not extracted from media queries in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from a partial CSS extract (button components, color list, one font-loader reference, and page text) rather than a full stylesheet or rendered DOM audit. Only `button-md` typography values are directly observed; all other type scale sizes, weights, and line-heights are proposed and unverified. Semantic color roles (body text, hairlines, surface tiers) are inferred by matching neutral shades to plausible UI functions, not confirmed via labeled selectors. The accent hues (#00bbff, #32c82e, #b4904d) have no confirmed component association and are treated as inferred category/status accents only. No hover, focus, active, error, or loading states beyond the button hover rule were observed. Mobile/responsive layout, breakpoints, and grid collapse behavior are proposed conventions, not measured from live rendering. The "Basier Square" webfont is referenced only through Next.js–generated class identifiers (`__basierSquare_635c71` / `__basierSquare_Fallback_635c71`); its licensing, full weight range, and rendering fallback behavior were not verified. "Times" appears in the extracted font list but no CSS rule ties it to a specific element, so it was not used in the typography tokens above.
