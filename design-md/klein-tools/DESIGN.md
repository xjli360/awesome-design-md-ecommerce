---
version: alpha
name: "Klein Tools"
source_url: "https://kleintools.com"
captured_at: "2026-09-28T04:48:31.126775+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Klein Tools' public site evidence shows a utilitarian, high-contrast industrial system built around a single saturated safety-orange accent (#ee6809) against near-black and dark-grey chrome (#000000, #232323, #222222) with white canvas and mid-grey body copy (#333333). This pairing reads as job-site signage: high legibility, minimal decoration, and an accent reserved for calls-to-action, hover states, and the "back to top" control. Header and navigation surfaces use a dark #232323 band with white text, switching to orange on hover/focus, which we treat as the primary interactive-state pattern site-wide (inferred for buttons and links beyond the observed nav/back-to-top instances).

  Typography is exclusively Helvetica Now, a custom family expressed via multiple observed weight files (helveticanowdisplay-xbd, -bd, -md, helveticanowbold, helveticanowtext-regular), with Arial/Helvetica/sans-serif as CSS fallbacks. Headline treatments favor bold/extra-bold condensed display weights, uppercase, wide letter-spacing (observed .1em on the site-name), suited to a durable-goods, professional-trade brand rather than a lifestyle retailer.

  The interpretation below extends these observed fragments into a full system: dark utilitarian chrome, orange as the sole accent, generous hairlines and light-grey surfaces for card/table separation appropriate to a large SKU catalog, and compact, legible body type for dense product-spec content.

colors:
  primary: "#ee6809"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  header-bg: "#232323"
  header-bg-alt: "#222222"
  border-light: "#cccccc"
  danger: "#e62600"

typography:
  display-xl: {fontFamily: "helveticanowdisplay-xbd, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "helveticanowdisplay-bd, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "helveticanowdisplay-bd, Helvetica, Arial, sans-serif", fontSize: 24px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 2.4px}
  body-md: {fontFamily: "helveticanowtext-regular, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.125, letterSpacing: 0px}
  body-sm: {fontFamily: "helveticanowtext-regular, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "helveticanowtext-regular, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "helveticanowbold, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}

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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.on-primary}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.section}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.header-bg}"
    headerTextColor: "{colors.on-primary}"
    borderColor: "{colors.border-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** uses the observed orange accent (#ee6809) as its fill, matching the `#backtotop` control's background; on-primary text color is proposed as white for contrast, though the sole directly observed instance pairs orange with black text — treat text color as an inferred, not confirmed, general rule.

**button-secondary** is a proposed outline variant using the same orange as border and label color on a transparent/white field, intended for lower-emphasis actions (e.g., "View All") alongside primary CTAs like "Shop Now."

**text-input** is a proposed light-field input styled with the observed hairline grey border and body-grey text, sized for search and account forms; no live input styling was captured in the evidence.

**nav-bar** reflects the observed dark header/nav chrome (#232323) with white link text and orange hover state, directly grounded in `.top-header-row2 .nav-menu a` and its `:hover`/`:focus` rule.

**product-card** is a proposed catalog tile pattern (white surface, hairline border, title in the display weight) inferred from the large product/category listing structure implied by the navigation taxonomy, not from a captured card selector.

**hero** is a proposed full-bleed banner using the dark header background and large display type, matching the promotional copy pattern ("Built for today's pros," "Shop Now") seen in the page text excerpt, though no hero CSS was captured.

**footer** is proposed using black/ink as the base, consistent with the site's dark-chrome convention; no footer selectors were present in the evidence.

**badge** is a proposed pill/label component in orange, suited to flags like "New," "Made in USA," or "250th Edition" seen in product listings; not a directly observed style.

**search** is a proposed light-surface search field consistent with the site's "Search" nav item; exact field styling was not present in the CSS sample.

**spec-table** is a category-appropriate proposed component for hand-tool spec sheets (AWG ratings, sizes, materials), using dark header rows echoing nav chrome and light-grey body rows for scanability across Klein's dense SKU/spec content.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column; nav collapses behind `#navbar-toggle` (observed hidden-by-default hamburger button); touch targets ≥44px. |
| Tablet | 600–1023px | Two-column product grids; sub-menu becomes toggle-driven (`.subnav-toggle-button` observed). |
| Desktop | 1024–1439px | Full horizontal nav (`.top-header-row2 .nav-menu`) visible; multi-column category/product grids. |
| Wide | 1440px+ | Max-width content container; hero and grid spacing increase using `{spacing.section}`. |

This table is a recommendation based on the presence of toggle/hamburger selectors in the CSS, not measured viewport behavior. Interactive collapse thresholds, exact grid column counts, and touch-gesture behavior were not observed and should be validated against the live responsive site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, computed styles, or JavaScript-driven states were observed. Component definitions beyond `nav-bar` and the `#backtotop` button (hero, product-card, footer, search, spec-table, badge, text-input, button-secondary) are proposed inferences based on navigation taxonomy and page-text content, not captured selectors. The `.1em` letter-spacing on `.top-header-site-name` was converted to an approximate px value (2.4px) for schema compliance; treat as derived, not literal. Font weight mappings (e.g., 800 vs. 700) are approximations based on filename conventions (`-xbd`, `-bd`, `-md`) since no explicit `font-weight` numeric table was supplied for each face. Availability and licensing of the Helvetica Now custom font files were not verified. Color roles for `danger`, `header-bg-alt`, and `border-light` are inferred from limited single-use CSS rules and may not reflect systematic usage across the full site. Mobile menu interaction, hover/focus states beyond the two captured instances, and breakpoint pixel values are not observed and require live-site confirmation before implementation.
