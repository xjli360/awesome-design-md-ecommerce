---
version: alpha
name: "Backdrop"
source_url: "https://backdrophome.com"
captured_at: "2026-09-28T04:50:13.898798+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Backdrop's supplied CSS evidence is dominated by third-party component
  libraries (Uppy file uploader, Swiper carousel) rather than bespoke
  storefront styling, so this interpretation infers a restrained, editorial
  palette consistent with a premium DTC paint and wallcoverings brand. The
  named font family akzidenz-grotesk — a well-known grotesque sans
  historically favored by design-forward brands — is the one specific
  typeface signal in the evidence; it is paired here with system-ui
  fallbacks (-apple-system, Segoe UI, Roboto, Helvetica, Arial) for body
  copy, an inferred split between display and body roles. Core neutrals
  (#ffffff, #1f1f1f, #333333, #757575, #dfdfdf, #fafafa) form the working
  UI palette, standing in for canvas, ink, body text, muted copy, hairlines,
  and soft surfaces. A blue (#1269cf) present in the palette is proposed as
  the primary interactive color for buttons and links, though its exact
  application (uploader chrome vs. brand UI) could not be confirmed from
  the sample. Warm, paint-adjacent neutrals (#dad3c9, #fdeff1) and a
  certified-green (#1bb240) are reserved for soft surfaces and
  eco/certification badging, referencing the site's Green Wise and Climate
  Label messaging. All layout, spacing, and component states below are
  proposed conventions for a paint-sample-driven e-commerce experience, not
  measured observations.

colors:
  primary: "#1269cf"
  ink: "#1f1f1f"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#dfdfdf"
  surface-soft: "#fafafa"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-green: "#1bb240"
  accent-red: "#e32437"
  accent-gold: "#f6a623"
  warm-neutral: "#dad3c9"
  blush: "#fdeff1"
typography:
  display-xl: {fontFamily: "akzidenz-grotesk, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "akzidenz-grotesk, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "akzidenz-grotesk, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "akzidenz-grotesk, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-sample-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.sm}"

## Components
**button-primary** is the principal call-to-action treatment (e.g. "Shop Paint," "Add to Cart"), using the inferred primary blue against a white label; hover/active states are proposed, not observed.

**button-secondary** provides an outlined variant for lower-emphasis actions ("See the Collection," "Explore All Inspiration"), sharing the primary's border color on a white fill; this contrast pattern is proposed.

**text-input** covers search and form fields (e.g. newsletter signup, "Contact Us"), using a hairline border and muted-neutral canvas; focus-ring styling is not confirmed in the evidence and is proposed.

**nav-bar** represents the top navigation housing Paint, Wallcoverings, Rugs, Resources, Inspo, Reviews, and Cart; a bottom hairline separates it from content. Sticky/scroll behavior is not observed and is proposed.

**product-card** applies to paint-color tiles and wallcoverings listings, using a soft card surface, subtle border, and a two-tier type hierarchy (title/body) for color name and description.

**hero** models the homepage banner pattern seen in the text excerpt ("PREMIUM PAINT & WALLCOVERINGS," Porsche x Backdrop), pairing a large display headline over a soft-surface background with generous section padding.

**footer** is proposed as a dark, ink-toned band (inverting body text to on-primary white) carrying Shop/Company/Trade/Community links and certification mentions (Climate Label Certified); this inversion is a convention, not a captured screenshot.

**badge** supports the certification and collection callouts referenced in copy (Green Wise certified, Climate Label Certified, limited-edition collection tags) as a small pill using the accent-green fill; other accent colors may substitute for promotional badges.

**search** is a lightweight input treatment for the paint/wallcovering catalog search, using muted placeholder text and a soft background to differentiate from primary form fields.

**swatch-sample-card**, a category-specific component, models the 12x12" adhesive paint-swatch product referenced in the source copy — a compact card with a color-fill area, hairline border, and small caption label for the color name/code; interaction states (select, add-to-cart) are proposed.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column stacks, nav collapses to a hamburger/drawer, swatch cards go full-bleed at 2-up grid |
| Tablet | 600–1023px | 2–3 column product/swatch grids, nav may remain collapsed |
| Desktop | 1024–1439px | Full horizontal nav, 3–4 column grids, hero at full padding |
| Wide | 1440px+ | Max-width content container, additional gutter, grids may expand to 4–5 columns |

Touch targets should be a minimum 44×44px for buttons and swatch-card tap areas, consistent with the `--swiper-navigation-size:44px` value present in the evidence (used there for carousel arrows). Navigation collapse, drawer/menu patterns, and carousel swipe gestures are proposed conventions inferred from the presence of Swiper in the codebase, not confirmed interaction observations.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- The supplied CSS is largely third-party UI-library styling (Uppy uploader, Swiper carousel), not bespoke storefront CSS, so brand-specific component styling (real button/nav/card rules) is not directly observed.
- Color role assignments (primary, ink, muted, hairline, etc.) are inferred from a flat palette list without confirmed selector-to-role mapping for most brand surfaces.
- akzidenz-grotesk is confirmed present as a font-family value, but actual weight availability, licensing, and webfont-loading behavior were not verified.
- All typography sizes, spacing scale, and rounded-corner values are proposed conventions, not measured from rendered layout.
- No responsive/mobile layout, hover, focus, or animation states were directly observed; all such behavior above is labeled proposed.
- Component existence (hero, product-card, swatch-sample-card, etc.) is inferred from page text/structure references, not from captured DOM or visual screenshots.
