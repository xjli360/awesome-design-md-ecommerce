---
version: alpha
name: "Alvarez Guitars"
source_url: "https://www.alvarezguitars.com"
captured_at: "2026-09-29T04:11:02.775003+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Alvarez Guitars' WordPress-based storefront, whose exposed CSS shows a neutral, utility-driven palette dominated by grayscale values (#1f1f1f, #333333, #666666, #dddddd, #f7f7f7) alongside a Bootstrap-derived accent set (#0275d8 blue, #5cb85c green, #f0ad4e amber, #d9534f red, #5bc0de cyan). No brand-specific hex beyond this system was present in the evidence, so the interpretation treats the dark grays as primary ink and the blue as the sole strong accent for interactive elements, both labeled inferred roles rather than confirmed brand colors. A warm tan (#c8bfb2) appears in the palette and is proposed here as an optional wood-toned accent for badges or dividers, evoking the instrument material without asserting it as a verified brand color. Typography draws only from families actually present in the CSS/font list: acumin-pro and freight-sans-pro (likely body/heading webfonts), Open Sans and Raleway (utility/plugin fonts), and system-ui/Helvetica/Arial fallbacks. Layout patterns (hero, product grid, series cards, comparator UI) are inferred from page-text structure (Latest Products, Featured Guitars, Explore by Series) and plugin selectors (guitar-comparator), not from measured rendering. All sizing, spacing, and radius values are proposed defaults suited to a photography-forward instrument catalog, not extracted measurements.

colors:
  primary: "#0275d8"
  ink: "#1f1f1f"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-wood: "#c8bfb2"
  success: "#5cb85c"
  warning: "#f0ad4e"
  danger: "#d9534f"
  info: "#5bc0de"
  dark: "#292b2c"
typography:
  display-xl: {fontFamily: "acumin-pro, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "acumin-pro, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "freight-sans-pro, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Raleway, Helvetica, Arial, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.info}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-wood}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  series-selector-card:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    descriptionTypography: "{typography.body-sm}"
    descriptionColor: "{colors.muted}"
    padding: "{spacing.lg}"
  comparator-panel:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    buttonBorder: "1px solid {colors.ink}"
    buttonHoverBackground: "{colors.ink}"
    buttonHoverTextColor: "{colors.on-primary}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    padding: "{spacing.lg}"

## Components
**button-primary** is proposed for primary calls to action ("Explore Laureate Series," newsletter signup) using the observed blue accent (#0275d8) against white text; hover/active states are not observed and would need confirmation. **button-secondary** covers outline-style actions, modeled on the comparator plugin's bordered black buttons that visibly invert to a filled black background on hover in the supplied CSS (`.compare-add-guitar-button:hover`). **text-input** proposes a light-bordered field for search or newsletter forms; no live input styling was captured. **nav-bar** is inferred from the text-only menu structure (Guitars, Ukuleles, Where to Buy, Compare, Store) and assumes a light canvas bar with a hairline divider, not confirmed sticky/scroll behavior. **product-card** models the "Featured Guitars" grid items (e.g., DYM66HD, FYM70), pairing a bold title with a lighter series label, using card border and radius as proposed defaults. **hero** represents the top "Laureate Series, Beyond Dedication" banner as a dark, full-bleed panel with large display type; actual background imagery/color was not measured, so the dark neutral (#292b2c) is used as a placeholder. **footer** reflects the observed link list (Privacy, Terms, Warranty, Contact us) on a dark background with informational-blue links, consistent with the palette's #5bc0de. **badge** is a proposed small pill for series/category tags (e.g., "Yairi," "Masterworks") using the inferred wood-tone accent. **search** is a lightweight proposed treatment for the site's search feature referenced in the nav. **series-selector-card** models the "Explore by Series" carousel (Artist Elite, Regent, Yairi, Masterworks, Laureate) as bordered content tiles. **comparator-panel** directly reflects the supplied `guitar-comparator` plugin CSS, including its black-bordered, hover-inverting buttons and muted gray labels (#666, #d3d3d3), making it the most evidence-grounded component in this set.

## Responsive Behavior
Recommended, not measured: mobile <768px collapses the nav into a toggled menu with 44px-minimum touch targets; product/series grids drop from 3–4 columns to 1–2 columns; the comparator panel stacks vertically below 768px. Breakpoint table (proposed): mobile 0–599px (1-col), tablet 600–959px (2-col), desktop 960–1279px (3-col), wide ≥1280px (4-col). Buttons and comparator controls should maintain a minimum 44×44px tappable area on touch devices; none of this was verified via live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/text extraction; no live rendering, hover states, animations, or actual breakpoints were observed. Color roles (primary, muted, accent-wood, etc.) are inferred assignments from a generic Bootstrap-influenced palette, not confirmed brand guidelines — the true Alvarez brand palette may differ from what this shared plugin/theme CSS exposes. Typography sizes and weights beyond the two `--wp--preset--font-size` values (16px, 42px) are proposed, not measured. Font family availability, licensing, and actual application (which text uses acumin-pro vs. freight-sans-pro vs. Open Sans) were not verified. Mobile menu behavior, carousel mechanics ("Explore by Series," "Latest Models"), and comparator interaction states are inferred from selector names only. No imagery, iconography, or grid measurements were confirmed from rendered pages.
