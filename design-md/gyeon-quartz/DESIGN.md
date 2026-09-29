---
version: alpha
name: "Gyeon Quartz"
source_url: "https://gyeonquartz.com"
captured_at: "2026-09-28T09:43:04.916121+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in CSS extracted from the GYEON global site
  (gyeon.co), which shares the brand system used across GYEON Quartz regional
  storefronts. The palette centers on a dark navy (#21314D) used for outlined
  buttons and hover fills, paired with white canvases and light neutral
  surfaces (#f3f3f3, #edf0f8) typical of a premium automotive-care catalog.
  A wide spread of secondary hex values — pinks/magentas (#de3f7d, #db458a,
  #e83e8c) and blues (#3692c0, #5d7cff, #78a6ea) — recur across the source
  but their exact UI role (category tagging, chart/badge accents, or CMS
  block colors) is not verifiable from static CSS; they are treated here as
  inferred accent options rather than confirmed primary brand colors.
  Typography is anchored by the observed heading stack "GT America
  Compressed" / "GT America Expanded" (bold, condensed, used for section
  titles and product names at 45px/41px line-height), which gives the brand
  its technical, motorsport-adjacent tone. No body-copy font-family was
  captured in the supplied evidence, so body text falls back to the
  generic sans-serif stack present in the CSS (Segoe UI, Roboto, Helvetica
  Neue, Arial) and is labeled inferred. Layout, spacing scale, and rounded
  corners are proposed conventions suited to a structured product/collection
  storefront, not measured observations.

colors:
  primary: "#21314d"
  ink: "#01051d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6a6a6a"
  hairline: "#dee2e6"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#de3f7d"
  accent-blue: "#3692c0"
  surface-tint: "#edf0f8"
  border-soft: "#ced4da"
  success: "#28a745"
  warning: "#ffc107"
  info: "#17a2b8"
typography:
  display-xl: {fontFamily: "'GT America Compressed', sans-serif", fontSize: 45px, fontWeight: 700, lineHeight: 0.91, letterSpacing: -0.25px}
  display-md: {fontFamily: "'GT America Expanded', 'GT America Compressed', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "'GT America Compressed', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focus:
      border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    hover:
      shadow: "0 4px 12px rgba(1,5,29,0.08)"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  collection-filter-tag:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
    active:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"

## Components

**button-primary** is a pill-shaped, filled call-to-action (e.g. "COATINGS COLLECTION" links) using the navy primary against white text; the full-rounded corner is proposed, matching the `.wp-block-button__link` `border-radius: 9999px` pattern observed elsewhere in the WordPress theme CSS.

**button-secondary** mirrors the outlined pattern directly observed in `#section-industry .section-button a` and `#section-packaging .section-button a`: transparent background, 1px navy border, navy text, filling to navy with white text on hover — this hover transition (`background-color 0.4s ease-in-out`) is an actual observed rule.

**text-input** is a proposed pattern for search/newsletter/contact forms; no input styling was present in the supplied evidence, so border, radius, and focus state are inferred conventions consistent with the neutral hairline palette.

**nav-bar** represents the top navigation housing "Products," "Experience Center," and regional-site menus described in the page text; exact height, sticky behavior, and mobile collapse were not present in the CSS evidence and are proposed.

**product-card** supports the "OUR RANGE" grid (ceramic coatings, maintenance products, towels, PPF, purify, interior care) and reuses the observed `.product-name` typography (GT America Compressed, 700, 20px) for titles; card border, radius, and hover elevation are proposed since no card-container CSS was captured.

**hero** models the full-bleed intro pattern seen in `.about-us-wrap .header-wrap` (`height: 100vh`, white background, white header text); the production homepage hero likely uses a dark or image overlay, so ink/primary are used here as an inferred substitute background suited to the "THE GYEON WAY" statement section.

**footer** is proposed as a dark closing band listing regional site links (visible in page text: Europe, Asia, North America groupings); no footer-specific CSS was supplied.

**badge** uses the accent-pink from the observed palette for small labels such as "NEW," "EVO," or category flags referenced in text (e.g. "EVO ALL SURFACE COATINGS"); this color-role mapping is inferred, not confirmed by any badge selector in evidence.

**search** and **collection-filter-tag** support the "PRODUCTS CATEGORIES" navigation (Exterior Coatings, Interior, PPF, Aero & Marine) referenced repeatedly in the page text; both are proposed components using the light surface-tint and primary-navy active state for consistency with the confirmed button color logic.

## Responsive Behavior

Recommended, not measured — no breakpoint or media-query evidence was supplied.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | 0–599px | Single-column product grid, nav collapses to hamburger/off-canvas menu |
| tablet | 600–959px | 2-column product grid, condensed hero heading using display-md |
| desktop | 960–1279px | 3–4 column product grid, full nav bar |
| wide | 1280px+ | Max-width content container, display-xl hero heading |

Touch targets should be a minimum 44×44px for nav items and buttons. Category/filter navigation should collapse into an accordion or dropdown below tablet width. These recommendations are conventions for a multi-category product catalog, not observed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from `gyeon.co` (the parent/global WordPress site), not directly from `gyeonquartz.com`; component and typography mappings are applied by brand-family inference and may not match the exact regional storefront markup.
- No body-copy `font-family` declaration was present in the supplied CSS; body/caption/button text families are inferred from the generic fallback stack rather than a confirmed brand typeface.
- The large secondary color set (pinks, blues, status colors like `#28a745`/`#ffc107`/`#17a2b8`) could not be tied to specific confirmed UI roles; accent, badge, and status-color assignments here are inferred, not verified.
- No layout, grid, spacing, or component CSS (cards, inputs, nav, footer) was included in the evidence beyond hero, button, and heading-typography rules; all spacing scale values and most component structures are proposed conventions.
- Mobile/responsive behavior, hover/focus states beyond the two documented button rules, and interaction patterns (menus, filters, carousels) were not observed and are proposed.
- Licensing and web-font availability for "GT America Compressed/Expanded" were not verified; these are proprietary commercial fonts and require confirmed license terms before production use.
