---
version: alpha
name: "Veritas"
source_url: "https://www.leevalley.com/en-us/tools/brand/veritas/sharpening-tools"
captured_at: "2026-09-29T04:15:55.964770+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Veritas is the in-house tool brand of Lee Valley Tools, presented here within Lee Valley's parent e-commerce site rather than as an independent storefront. The observed palette is dominated by neutral grays and off-whites (#eeeeef page background, #4a4a4a body copy, #767676 muted text) paired with a small set of deep institutional blues (#013056, #00467e, #003c71) used for buttons and links, consistent with a trade-tool retailer's restrained, functional aesthetic. No Veritas-specific accent color was distinguishable from Lee Valley's general site chrome, so the primary action color is inferred from the observed button background (#013056) rather than confirmed brand guidelines.
  Typography is dual-stack: computed styles on this page resolve to "Open Sans"/"Open Sans Fallback," while the stylesheet also defines a separate `body.veritas-font` rule (verdana, arial, helvetica) presumably reserved for Veritas-branded product or legacy content blocks. This document treats Open Sans as the primary observed UI font and notes the verdana/arial stack as an available but unconfirmed secondary treatment.
  The interpretation favors a clean, catalog-style grid suited to precision hand-tool merchandising: flat surfaces, thin hairlines, small-radius buttons, and generous whitespace, avoiding decorative flourishes not evidenced in the CSS.

colors:
  primary: "#013056"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#003c71"
  accent-blue: "#00467e"
  page-bg: "#eeeeef"
  border-subtle: "#e3e2e2"
  neutral-100: "#f4f4f4"
  neutral-300: "#cccccc"
  text-strong: "#333333"
  alert: "#c6093b"
  highlight: "#ffdd00"
typography:
  display-xl: {fontFamily: "Open Sans, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Open Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.accent-blue}"
    borderColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-strong}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.page-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.neutral-100}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  info-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.link}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.lg}"

## Components

**button-primary** is proposed for primary cart/checkout actions ("Add To Cart"), using the observed dark blue button background (#013056) confirmed from a computed-style snapshot on this page, paired with white text and a small corner radius consistent with a utilitarian catalog UI. Hover/active states are not observed and are proposed only.

**button-secondary** covers outline-style actions such as "More Options" or "Learn More," using the alternate observed blue (#00467e) as border/text color on a white background — this pairing is inferred from two distinct blue button/text values found in the CSS rather than a directly observed secondary-button rule.

**text-input** and **search** share a plain bordered field pattern using the neutral hairline gray (#dddddd) for borders, since no distinct input styling was present in the supplied evidence; padding and radius are proposed defaults appropriate to a dense product-catalog layout.

**nav-bar** models the top category navigation (Tools/Hardware/Home/Kitchen/Garden/Gifts/Clearance/Discover) implied by the page text, using white background and the strong neutral text color (#333333); no measured height, sticky behavior, or hover state was present in evidence.

**product-card** represents each sharpening-tool listing (name, price, Add To Cart), using a white surface with a subtle border (#e3e2e2) and small radius; layout as a responsive grid is inferred from the flat list of repeated product/price/button text in the page excerpt, not from measured grid CSS.

**hero** models the "PM-V11 Story" promotional block, using the light page background (#eeeeef) and the observed caption paragraph styling (max-width 720px, centered, #4a4a4a body text) taken directly from the `#header-title-section-with-caption-rte p` rule.

**footer** reflects the multi-column footer link list (About Us, Careers, Contact Us, Your Account, Shop, etc.) using a light neutral background and muted gray text; column layout and breakpoints are proposed, not measured.

**badge** is a proposed component for promotional flags such as "Fall Clearance Event," using the observed red (#c6093b) found in the palette as an inferred alert/clearance color, since no explicit badge rule was present in evidence.

**info-banner** covers the PM-V11 steel-alloy educational banner and similar editorial callouts, reusing the soft surface and link-blue (#003c71) confirmed from the anchor-color rule within the caption block.

## Responsive Behavior

This is a proposed, unmeasured breakpoint recommendation, not observed site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <600px | Single-column product list; nav collapses to a menu toggle; hero text reduces to `{typography.title-md}`. |
| tablet | 600–1024px | 2-column product grid; nav shows condensed top-level items. |
| desktop | >1024px | 3–4 column product grid; full horizontal nav bar. |

Touch targets are recommended at a minimum 44×44px for buttons and nav items, per general accessibility practice, not a value extracted from the CSS. Collapse of secondary filters/facets into an off-canvas panel on mobile is a proposed pattern for a tool-catalog page of this density and is not confirmed from the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, interaction states (hover/focus/active beyond the few hover rules supplied), or mobile viewport behavior were observed. Semantic color roles (primary, alert, highlight) are inferred from limited computed-style samples and general palette presence, not from a documented brand style guide. Font usage is split between an observed "Open Sans" computed-style result and a separately defined but unconfirmed `veritas-font` (verdana/arial/helvetica) stack; which governs the actual rendered Veritas sections is uncertain. All spacing and rounded-corner scale values are proposed defaults, not measured from the page. Custom font licensing/availability was not verified — Open Sans and the system fallbacks are assumed web-safe/Google Fonts-hosted. Product-grid column counts, card dimensions, and breakpoint pixel values are estimates for a catalog page of this type, not extracted measurements.
