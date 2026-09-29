---
version: alpha
name: "Nantucket Sinks"
source_url: "https://nantucketsinksusa.com"
captured_at: "2026-09-28T04:51:24.176125+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Nantucket Sinks USA is a B2B kitchen and bathroom fixture supplier with a
  nautical-adjacent, utilitarian brand voice ("Fireclay," "Granite Composite,"
  "Stainless Steel" collections named for New England coastal towns). The
  observed palette centers on a deep slate-blue (#376082) paired with a
  brighter working blue (#3d9be9) and a pale sky tint (#c1def7); these read
  coherently as a coastal/marine accent family and are proposed here as
  primary, link, and soft-surface roles respectively. Neutrals are drawn from
  a warm gray scale (#151414 through #f1f0ef) rather than pure black/white,
  suiting dense catalog and spec-sheet content. Several additional ramps
  (reds, greens, oranges, purples) were observed but appear to be a generic
  Wix status/utility palette rather than brand-specific; they are mapped
  sparingly to badge/alert roles only. Body copy is set in the explicitly
  observed `Arial, Helvetica, sans-serif` stack. Poppins and Raleway appear
  among loaded font families without a confirmed selector binding; they are
  used here, as inferred, for headline roles typical of the surrounding Wix
  template. Layout, radii, and spacing are proposed conventions for a
  catalog-heavy B2B fixtures site, not measured from live DOM geometry.

colors:
  primary: "#376082"
  ink: "#151414"
  canvas: "#ffffff"
  body: "#383838"
  muted: "#767574"
  hairline: "#e0dfdf"
  surface-soft: "#f1f0ef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#3d9be9"
  sky-tint: "#c1def7"
  link: "#116dff"
  deep-navy: "#2b5672"
  border-strong: "#8f8f8f"
  border-light: "#e2e2e2"
  neutral-mid: "#a8a6a5"
  neutral-quiet: "#cccccc"
  success: "#4b916d"
  warning: "#f9ad4d"
  danger: "#df3131"
  danger-deep: "#9c2426"
  accent-purple: "#5000aa"
  brass-accent: "#c38f42"
typography:
  display-xl: {fontFamily: "Poppins, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Raleway, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.sky-tint}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sky-tint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.deep-navy}"
    borderColor: "{colors.hairline}"
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
  material-filter-chip:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    selectedBackgroundColor: "{colors.accent-blue}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** uses the deep slate-blue as a solid call-to-action fill (e.g., "Become a Dealer," "View Now") against white text, matching the site's B2B, catalog-driven tone. Hover/pressed states are proposed, not observed.

**button-secondary** is an outlined variant for lower-priority actions (secondary catalog links, "View All >" affordances), sharing the primary color as both border and text to keep the palette restrained.

**text-input** covers newsletter and contact-form fields ("Role / Profession," dealer contact form referenced in page text). A light hairline border on white keeps forms legible against the dense navigation content; focus states are proposed.

**nav-bar** models the multi-level mega-menu implied by the extensive Kitchen/Bathroom/Accessories/Support hierarchy in the page text. A white background with dark ink text and a light hairline bottom border is proposed to separate it from hero content without adding another brand color.

**product-card** supports the collection and accessory listings (e.g., Cape Fireclay, Rockport Granite Composite, Sconset Stainless Steel). A soft rounded corner and hairline border distinguish cards on a white canvas; title uses the heading typography scale, description uses body-sm.

**hero** is proposed for homepage/collection landing banners, using the deeper navy as background with the pale sky tint reserved for subtle overlay or divider use, echoing the coastal/nautical naming convention (Nantucket, Cape, Vineyard, Orleans).

**footer** groups the large Support/Documents/Showroom link inventory visible in the page text (Brochures, Catalogs, DXF files, Warranty Info, FAQs). Dark navy background with sky-tint links keeps link density readable while reusing existing palette colors.

**badge** is proposed for award/recognition callouts referenced in the copy ("Recognized by KBB," "As Seen & Recognized"), using a soft neutral fill with navy text rather than introducing a new accent color.

**search / material-filter-chip**: search models a proposed catalog search affordance; material-filter-chip supports filtering by material (Fireclay, Granite Composite, Stainless Steel, Brass, Copper) and category (Farmhouse, Prep Station, Bar Sinks), a pattern implied directly by the taxonomy in the page text, with the working blue signaling an active/selected filter state.

## Responsive Behavior

Proposed breakpoints (not measured from live site behavior):

| Breakpoint | Width       | Nav behavior                | Grid                          |
|-----------|-------------|------------------------------|--------------------------------|
| mobile    | <480px      | collapsed hamburger menu    | 1-column product cards         |
| tablet    | 480–1024px  | condensed top nav, sub-menus as accordions | 2-column product grid |
| desktop   | 1024–1440px | full mega-menu with hover flyouts | 3–4 column product grid |
| wide      | >1440px     | mega-menu, max-width container | 4+ column product grid |

Touch targets on filter chips, nav items, and buttons should be at least 44×44px. Mega-menu categories (Kitchen, Bathroom, Utility, Accessories, Support) should collapse into stacked, tap-expandable accordions below tablet width. This table is a recommendation for implementation, not a measurement of the current site's responsive markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, active, mobile menu behavior) were observed. Semantic role assignment for colors (primary, link, badge, danger, success, etc.) is inferred from likely usage patterns and Wix-template conventions, not confirmed by selector-to-role mapping in the supplied CSS. Typography sizes, weights, and line-heights are proposed design values; only the body font stack (`Arial, Helvetica, sans-serif`) is directly confirmed by an observed selector rule, while Poppins/Raleway usage for headings is inferred from the presence of those families in loaded font lists without a confirmed binding. Spacing scale, border radii, breakpoints, and component states are proposed conventions suitable for a B2B fixtures catalog, not measurements from the live DOM. Custom/webfont licensing and availability (Poppins, Raleway, Futura, Avenir variants observed in the font list) were not verified for production use.
