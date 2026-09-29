---
version: alpha
name: "Malco"
source_url: "https://malcoproducts.com"
captured_at: "2026-09-29T04:19:04.035129+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Malco Tools is a manufacturer-direct site for HVACR and building-construction hand tools, and the supplied CSS points to a utilitarian, catalog-driven interface rather than a lifestyle brand. The body font stack is futura-pt for running text and futura-pt-bold for all headings, falling back to system sans-serif stacks (-apple-system, Segoe UI, Roboto, etc.), giving the brand a geometric, industrial voice consistent with a tools manufacturer. The measured background is a near-white #fefefe with primary copy at #222 and a secondary dark tone of #333 appearing in form and hover states.
  The palette contains a cluster of saturated reds (#aa112c, #8b0019, #920f26, #7d131e, #880e23, #630012) that recur across many shades, which is treated here as the inferred brand-primary family, with #aa112c selected as the representative primary since it is the most saturated and central value in that cluster. A default WordPress button style uses a near-black slate (#32373c) with white text and a fully-rounded (9999px) pill shape; this is documented as an observed component pattern but labeled as a generic theme default rather than a confirmed brand-primary button, since no button rule ties it to the red cluster. Grays (#eee, #f1f1f1, #ddd, #8a8a8a, #313131) supply muted text, hairlines, and soft surfaces. No custom heading sizes beyond a 42px "huge" preset and 16px "normal" preset were observed, so most type sizes below are proposed, not measured.

colors:
  primary: "#aa112c"
  ink: "#222222"
  canvas: "#fefefe"
  body: "#333333"
  muted: "#8a8a8a"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  primary-dark: "#630012"
  primary-deep: "#46000d"
  ink-soft: "#313131"
  border-dark: "#32373c"
  surface-alt: "#f1f1f1"
  accent-warn: "#ffae00"
typography:
  display-xl: {fontFamily: "futura-pt-bold, sans-serif", fontSize: "42px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "futura-pt-bold, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "futura-pt-bold, sans-serif", fontSize: "22px", fontWeight: 700, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "futura-pt, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "futura-pt, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "futura-pt, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.25px"}
  button-md: {fontFamily: "futura-pt-bold, sans-serif", fontSize: "18px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-download-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components
**button-primary** is the proposed call-to-action style (e.g. "Where to Buy," "Add to Toolbox"), using the inferred brand red as background with white text and a fully rounded pill shape, matching the observed `border-radius: 9999px` on `.wp-block-button__link`. **button-secondary** is a proposed outline variant for lower-emphasis actions such as "View Catalog," reusing the primary red as border and text color on a transparent field.

**text-input** covers search and contact-form fields (the site includes a Gravity Forms contact form referenced in the CSS); it is proposed with a light hairline border and white card background, since no explicit input styling was supplied beyond a hover-state rule (`#gform_submit_button_20:hover`) showing a `#333` border and white background — that hover treatment is carried into the secondary-button proposal.

**nav-bar** represents the top utility/mega-menu structure implied by the large "Markets / Products / Support / Company" navigation tree in the page text; layout and collapse behavior are not measured, only the color/typography tokens are grounded in the observed body and hairline values.

**product-card** is proposed for the extensive product-category grid (Snips, Shears, Pliers, Hex Drivers, etc.); it reuses the observed "Add to Toolbox" hover-overlay pattern (`.img-container:after`) as a documented interaction — a white-bordered, uppercase, `futura-pt-bold` label that fades in on hover (`opacity: 0` transitioning via CSS transitions), confirmed directly in the supplied CSS for `.page-id-46553`.

**hero** is a proposed full-width band using the darker ink-soft tone (`#313131`, the theme's "very-dark-gray" utility color) as background with white text, sized at the display-xl scale; no hero-specific CSS was supplied, so exact treatment is inferred from generic dark/light block-color utilities present in the theme (`.has-very-dark-gray-background-color`).

**footer** reuses the same dark surface and white text for consistency with the one confirmed dark/light color pairing in the CSS, sized down to body-sm for link density, appropriate for the long footer navigation implied by the repeated category listing in the page text.

**badge** is a proposed small pill label (e.g. "New," "GOBLUE!" product line marker) using primary red and full rounding, extrapolated from the pill-shaped button radius token since no distinct badge CSS was observed.

**search** is proposed as a rounded, light-gray field for the "Search Field" element referenced in the page text navigation, using the theme's light-gray utility background (`#f1f1f1`/`#eee` family) rather than pure white, to visually differentiate it from card surfaces.

**spec-download-card** is a category-specific component proposed for the Catalogs/Videos/Tool-registration document links called out repeatedly in the nav (PDF spec sheets, catalogs); it uses the soft off-white surface and primary-red icon accent to signal downloadable technical content typical of a hand-tools manufacturer site.

## Responsive Behavior
Breakpoints are not measured from live layout; the following table is a proposed convention derived only from the numeric font-size scale variable naming pattern found in the raw data (`small=0em&medium=40em&large=64em&xlarge=75em&xxlarge=90em`), reinterpreted as pixel-equivalent breakpoints:

| Breakpoint | Width     | Notes (proposed) |
|-----------|-----------|-------------------|
| small     | 0px+      | Single-column stacked nav, mega-menu collapses to accordion |
| medium    | 640px+    | Two-column product grid begins |
| large     | 1024px+   | Full mega-menu nav bar, three-column product grid |
| xlarge    | 1200px+   | Four-column product grid, hero at full display-xl scale |
| xxlarge   | 1440px+   | Max-width content container, generous side margins |

Touch targets are recommended at a minimum 44×44px for buttons and nav items, with the observed pill radius (`9999px`) retained at all sizes. Given the deep multi-level category taxonomy in the page text (Markets > sub-markets > products > sub-categories), mobile nav should collapse into a drill-down accordion rather than a flat hamburger list. None of this responsive behavior was directly observed in the supplied CSS; it is a recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no live rendering, computed layout, or DOM interaction was captured. The brand-primary red is inferred from a cluster of similar dark-red hex values with no single rule explicitly labeling one as "primary" or "brand" — actual brand-book usage may differ. The `#32373c` dark-slate button color is a WordPress theme default (`.wp-element-button`) and may not reflect the true production button style if overridden elsewhere on the live site. Heading and body sizes beyond the confirmed 16px/42px presets are proposed, not measured. The `futura-pt` and `futura-pt-bold` fonts are referenced by name in the CSS but their licensing, hosting method (e.g., Typekit/Adobe Fonts), and actual on-page rendering were not verified. No hover/focus/active states were observed except the single Gravity Forms submit-button hover rule and the product-card "Add to Toolbox" overlay; all other interaction states listed above are proposed conventions. Mobile menu behavior, breakpoint pixel values, and grid column counts are not observed and are presented only as reasonable defaults for a tools-catalog site.
