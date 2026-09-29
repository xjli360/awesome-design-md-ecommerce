---
version: alpha
name: "Sadowsky"
source_url: "https://www.sadowsky.com"
captured_at: "2026-09-28T09:33:02.642454+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sadowsky.com is a WordPress-built catalog site for Roger Sadowsky's NYC
  custom bass and guitar shop. The supplied palette is large but mostly
  generic: it includes stock WordPress/Gutenberg block-editor swatches,
  social-network brand colors, and page-builder plugin preset variables
  (postx_preset_*, preset-colorN) that are template defaults rather than
  confirmed Sadowsky brand marks. The most credible, site-specific signals
  come from the theme's own stylesheet: body copy set in Lato at #313131 on
  a near-white ground, and buttons styled with a dark slate fill (#32373c)
  and fully rounded (9999px) corners with white text. No distinct accent or
  logo color could be confirmed from evidence, so this interpretation treats
  the palette as restrained and neutral -- dark charcoal text, off-white
  surfaces, and light gray dividers -- consistent with a workshop/catalog
  site that lets instrument photography carry the visual weight. Heading
  font usage beyond Lato (e.g. Alfa Slab One, Philosopher, arsenalregular,
  cuprumregular) appears in the font-family evidence but its actual role in
  page headings is not confirmed and is treated as inferred/unverified.

colors:
  primary: "#32373c"
  ink: "#313131"
  canvas: "#ffffff"
  body: "#313131"
  muted: "#707070"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#fbfbfb"
  on-primary: "#ffffff"
  border-subtle: "#d4d4d4"
  neutral-mid: "#b2b2b2"
  neutral-dark: "#424242"
  overlay: "#0a0a0a"
typography:
  display-xl: {fontFamily: "'Lato', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Lato', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Lato', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Lato', sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 20px, letterSpacing: 0px}
  body-sm: {fontFamily: "'Lato', sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 18px, letterSpacing: 0px}
  caption: {fontFamily: "'Lato', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 16px, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Lato', sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
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
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.neutral-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    hairlineColor: "{colors.hairline}"
    headerTypography: "{typography.title-md}"
    cellTypography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** models the site's confirmed `.wp-block-button__link` / `.wp-element-button` styling: a dark slate (#32373c) fill, white text, and a fully rounded pill shape (9999px), matching the observed CSS exactly. Hover/focus states were not observed and are proposed as a slight darkening or opacity shift.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "View Details" links on instrument pages), reusing the primary ink color for border and text with a transparent fill; not directly observed.

**text-input** is inferred for order forms (the site references a "NYC Custom Bass and Guitar Order Form"). Styling follows the neutral palette and a modest 4px radius consistent with the site's generally low-radius, function-first aesthetic outside of buttons.

**nav-bar** reflects the large, deeply nested menu structure evident in the page text (Available Instruments, NYC Custom Basses, Archtops, Support, etc.), implying a multi-level dropdown navigation. Exact visual treatment (background, active-state indicator) is proposed, not measured.

**product-card** is a category-appropriate pattern for listing individual instruments (e.g. "NYC Custom Will Lee Signature 22 Fret Bass"). Card surface uses the near-white `surface-card` tone with a light border; layout (image, model name, price/spec line) is inferred from typical instrument-catalog conventions, not observed markup.

**hero** proposes a dark, editorial full-bleed treatment for the homepage headline ("Timeless & Cutting Edge") sitting over the dark ink tone, echoing the workshop/craftsman tone of Roger Sadowsky's quoted statement. No hero background image or exact composition was confirmed from evidence.

**footer** is inferred as a dark neutral band containing support links (Serial Numbers, Replacement Parts, Contact Us) seen in the sitemap text; typography and spacing follow the base scale.

**badge** is proposed for labeling instrument status (e.g. "Available," "Previously Sold," "Signature Model") given the site's explicit distinction between available and previously-sold instruments in its navigation.

**search** is inferred generically for a catalog site of this size; no search UI was directly observed in the evidence.

**spec-table** is a category-specific component for the site's "Instrument Specs," "Master Grade Wood Gallery," and "NYC Instrument Price Lists" content -- tabular technical data central to a custom lutherie business. Row/column styling is proposed using hairline dividers and compact body typography for scanability.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column stacking; nav collapses to a hamburger/off-canvas menu given the large multi-level menu tree observed in sitemap text. |
| tablet | 600-1024px | Two-column product/spec grids; nav may remain collapsed due to menu depth. |
| desktop | >1024px | Full multi-level dropdown nav; multi-column instrument grids and spec tables. |

Touch targets for buttons and nav items should be at least 44x44px. Given the deep menu hierarchy (Basses > NYC Custom > model variants, etc.), mobile navigation should collapse into an accordion or drill-down pattern rather than flyout submenus. This section is a UX recommendation only; no actual responsive CSS or breakpoints were present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from static CSS/text extraction only; no rendered layout, computed styles, hover/focus/active states, or real breakpoints were observed. The bulk of the supplied color palette (WordPress default block-editor swatches, social-brand hexes such as Facebook/Twitter/LinkedIn blues, and page-builder plugin preset variables like `postx_preset_*`) could not be confirmed as intentional Sadowsky brand colors and were largely excluded from the token set in favor of the few hexes tied to actual theme CSS rules (#313131 body text, #32373c buttons, #eeeeee/#ffffff neutrals). Font usage is only confirmed for Lato in body copy; other listed families (Alfa Slab One, Philosopher, arsenalregular, cuprumregular, Font Awesome sets) appear in the evidence but their applied role (headings, icons, or unused theme defaults) is unverified. All sizing, spacing, radius, and component-state values beyond the button radius/fill and body font metrics are proposed conventions, not measurements. Licensing/availability of any non-system font referenced has not been verified.
