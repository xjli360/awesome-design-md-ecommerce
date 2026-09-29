---
version: alpha
name: "Hasami Porcelain"
source_url: "https://hasami-porcelain.com"
captured_at: "2026-09-29T04:00:14.650500+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The observed CSS shows a near-monochrome system built on pure black (#000000) text
  against a white (#FFFFFF) canvas, with two warm neutrals — taupe #998d71 and graphite
  #686763 — used as solid button backgrounds on `.btn_original` and `.btn_grey`
  respectively, directly mirroring the site's two product lines (ORIGINAL vs. THE GREY
  COLLECTION). A light grey #cccccc and mid greys #999999/#aaaaaa/#666666 appear as
  hairline borders (`.btn { border: 1px solid #999 }`), disabled/secondary text, and
  soft surface tints; these roles are inferred from typical usage since no dedicated
  surface class was captured. A pure red #ff0000 is present in the extracted palette
  but has no confirmed selector in the supplied evidence — it is treated as an
  unconfirmed/utility color, possibly a validation or legacy-markup artifact, and is
  not used for primary UI.

  Typography is condensed and geometric: `UniversLTStd-BoldCn` drives body copy, nav,
  and buttons at very tight, small sizes (12px body, 10–13px controls) with generous
  letter-spacing (0.03–0.06em) and a tall 1.8 line-height, giving the dense Japanese/
  English bilingual copy room to breathe. A Japanese fallback stack (太ゴB101, 游ゴシック
  体, Yu Gothic, メイリオ) ensures JP-locale rendering. The interpretation favors this
  restrained, catalog-like structure: flat pill buttons, thin hairline dividers, and
  large areas of white space framing product photography, consistent with a minimalist
  ceramics maker's visual identity.

colors:
  primary: "#998d71"
  accent-grey: "#686763"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#666666"
  muted-soft: "#aaaaaa"
  hairline: "#999999"
  surface-soft: "#cccccc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  alert: "#ff0000"
typography:
  display-xl: {fontFamily: "UniversLTStd-BoldCn, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.02em}
  display-md: {fontFamily: "UniversLTStd-BoldCn, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.02em}
  title-md: {fontFamily: "UniversLTStd-BoldCn, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.05em}
  body-md: {fontFamily: "UniversLTStd-Cn, UniversLTStd-BoldCn, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0.03em}
  body-sm: {fontFamily: "UniversLTStd-BoldCn, sans-serif", fontSize: 11px, fontWeight: 700, lineHeight: 1.36, letterSpacing: 0.05em}
  caption: {fontFamily: "UniversLTStd-BoldCn, sans-serif", fontSize: 10px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.06em}
  button-md: {fontFamily: "UniversLTStd-BoldCn, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.04em}
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
    padding: "{spacing.xs} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.accent-grey}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.caption}"
    padding: "{spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBorderColor: "{colors.ink}"
    inactiveBorderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"

## Components

**button-primary** maps to the observed `.btn_original` rule (`background-color:#998d71; border-radius:20px; padding:4px 20px`), representing the taupe-accented call-to-action for the ORIGINAL line; the near-full radius on a narrow fixed width reads as a pill, so it is mapped to `rounded.full` (proposed generalization of the literal 20px value).

**button-secondary** mirrors `.btn_grey` (`background-color:#686763`), used for THE GREY COLLECTION's parallel action, keeping identical shape/typography to `button-primary` so the two collections read as siblings distinguished only by color.

**text-input** is a proposed pattern; no form-field CSS was supplied, so border color, radius, and padding are inferred from the site's hairline (`#999`) and general spacing rhythm rather than observed.

**nav-bar** is grounded in `div#HEADER` (`fixed; height:40px; padding:25px 40px; background:#FFFFFF`) and `.sub` (11px, letter-spacing 0.05em), giving a slim, fixed, all-caps-feeling utility bar; exact link spacing/collapse behavior is not observed.

**product-card** is a proposed component for the ORIGINAL/GREY collection grids implied by the page text ("ORIGINAL", "GREY", product photography); background, border, and radius are inferred from the general white/hairline system, not a captured card selector.

**hero** corresponds to the large collection intro copy ("HASAMI PORCELAINのベーシックライン…") rendered on white; type size is proposed since no hero-specific font-size rule was supplied — only the body-level `font-family`/`color` stack was captured.

**footer** is inferred from the copyright line ("©HASAMI PORCELAIN All Rights Reserved.") and reuses the muted/hairline tokens for a quiet, low-emphasis close to the page; no dedicated footer selector was in evidence.

**badge** is a proposed small pill (e.g., "NEW" or collection tag) reusing the primary taupe fill and the observed 10px caption scale from `.btn_original`/`.btn_grey`; not an observed component.

**search** is proposed, styled consistent with the pill-button language (`rounded.full`, hairline border) though no search-input CSS was supplied.

**swatch-selector** is a category-specific proposed component for choosing between the Original semi-porcelain finish and the Grey glazed finish, using `surface-soft` (#cccccc) as an inactive fill and pure `ink` as the active-selection ring — an interpretation, not an observed control.

## Responsive Behavior

Recommended, not measured breakpoints: mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. The fixed `#HEADER` (40px height + 25px/40px padding) suggests the nav likely collapses to a compact bar or hamburger below tablet width, but no mobile-menu CSS was supplied to confirm this. Touch targets for pill buttons should be enlarged to at least 44px tall on touch devices even though the observed `.btn_original`/`.btn_grey` padding (4px 20px) yields a visually smaller hit area on desktop. Product grids should reflow from a multi-column desktop layout to a single or two-column mobile stack; this is a proposed convention for a catalog site, not an observed grid.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot and cannot confirm actual rendered layout, responsive breakpoints, hover/focus states beyond the single captured `.btn:hover`, or JavaScript-driven interactions (e.g., the `slider-pro.css` slider's real behavior). Several role assignments — `muted`, `muted-soft`, `surface-soft`, `surface-card`, and the unused `#ff0000` — are inferred from generic conventions rather than an explicit selector-to-role mapping in the evidence. Font sizes for `display-xl`, `display-md`, and `title-md` are proposed estimates since no heading-specific `font-size` rule was captured; only body (12px), `.sub` (11px), `.btn_original`/`.btn_grey` (10px), and `.btn` (13px) sizes are directly observed. Availability and licensing of `UniversLTStd-BoldCn`/`UniversLTStd-Cn` as web fonts were not verified; system/Japanese fallbacks should be assumed in absence of a confirmed `@font-face` block. Mobile navigation collapse, grid column counts, and card imagery treatment are proposed patterns only.
