---
version: alpha
name: "Akaso"
source_url: "https://akasotech.com"
captured_at: "2026-09-28T04:25:46.408222+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The supplied evidence is dominated by a Vue.js Element-UI component library
  (date-picker, pagination, dialog, table-filter selectors), so most palette
  hexes—#409eff, #67c23a, #e6a23c, #f56c6c, #909399, #dcdfe6—are that
  framework's stock interaction-state colors (hover blue, success, warning,
  danger, disabled/muted) rather than confirmed Akaso brand marks. A smaller
  set of hexes falls outside Element-UI's default set: #294033 (dark forest
  green), #0f8cff and #0066cc (saturated blues), and #fff7e5 (warm cream).
  These are treated here, with lower confidence, as the site's actual brand
  colors—fitting an outdoor action-camera identity—and are promoted to
  primary/accent roles; this mapping is inferred, not measured from rendered
  pages. Grays (#303133, #606266, #909399) are reused for ink/body/muted
  text, and #dcdfe6/#e4e7ed for hairlines, consistent with typical component
  library conventions. Typography evidence shows Gabarito in Black through
  Regular weights (a display/heading family) paired with Open Sans in
  Regular/SemiBold/Bold (a body/UI family); Arial, Helvetica, Georgia, and
  monospace stacks are treated as fallback-only. The interpretation below
  favors a bold, high-contrast display scale for hero/product moments and a
  calmer utility scale for specs, forms, and commerce chrome.

colors:
  primary: "#294033"
  accent: "#0f8cff"
  link: "#0066cc"
  ink: "#303133"
  canvas: "#ffffff"
  body: "#606266"
  muted: "#909399"
  hairline: "#dcdfe6"
  surface-soft: "#f5f7fa"
  surface-card: "#f7f7f7"
  warm-surface: "#fff7e5"
  on-primary: "#ffffff"
  success: "#67c23a"
  warning: "#e6a23c"
  danger: "#f56c6c"
  info: "#909399"
typography:
  display-xl: {fontFamily: "Gabarito ExtraBold, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gabarito Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gabarito SemiBold, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Open Sans SemiBold, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 22px, letterSpacing: 0.2px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    focusBorder: "{colors.accent}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeColor: "{colors.primary}"
    hoverColor: "{colors.accent}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    height: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    mutedTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaBackground: "{colors.accent}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.warm-surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    focusBorder: "{colors.accent}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    rowHairline: "{colors.hairline}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
`button-primary` uses the dark-green brand tone with white text for primary calls to action (Add to Cart, Shop Now); a proposed hover/active state would darken or shift toward the accent blue, but no such interaction was observed. `button-secondary` is an outline treatment against canvas, intended for tertiary actions like "Learn More," with hairline borders drawn from the component library's border grays. `text-input` mirrors Element-UI's form conventions—hairline border, muted placeholder—with a proposed accent-blue focus ring since no focus-state color was directly captured. `nav-bar` is a proposed light header with primary-colored active link state, sized to a generic touch-friendly height; actual scroll/sticky behavior is unobserved. `product-card` groups camera product tiles with card-surface background, title in the Gabarito display scale, and specs/price in body/caption weights. `hero` is a proposed full-bleed banner in the primary dark-green with white display type, suited to outdoor/action-camera imagery; the accent blue marks the CTA button. `footer` reuses the primary color as a dark band, a common pattern for brand sites, with link color pulled from the distinct #0066cc hex. `badge` (e.g., "New," "Waterproof," "4K60") uses the warm-cream surface with primary-colored text, borrowing the one non-framework warm hex in the palette. `search` is a pill-shaped field for site/product search, styled consistent with the soft-surface gray family. `spec-table` is a category-specific component for camera technical specifications, using a light header band and hairline row dividers to keep dense spec data legible, echoing the muted/ink text pairing seen in dialog and table CSS.

## Responsive Behavior
The following breakpoints are a proposed recommendation, not measured from the live site:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <480px | Single-column stacking; nav collapses to a hamburger/drawer; hero title drops to `display-md`. |
| tablet | 480–959px | Two-column product grids; search and nav condense; touch targets ≥44px. |
| desktop | 960–1279px | Multi-column grids (3–4 up); full nav bar visible. |
| wide | ≥1280px | Max-width content container with generous `spacing.section` gutters. |

All interactive targets (buttons, nav links, badges) should maintain a minimum 44×44px touch area on mobile/tablet. Navigation is assumed to collapse below `tablet`; no actual mobile menu markup or breakpoint was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS extraction dominated by a third-party Vue/Element-UI component library, not from rendered marketing pages; most palette hexes are that library's default interaction-state colors (info/success/warning/danger, hover blues, disabled grays) and may not represent Akaso's true brand palette. The promotion of #294033, #0f8cff, #0066cc, and #fff7e5 to primary/accent/link roles is an inference based on their absence from Element-UI defaults, not a confirmed brand-guideline match. Typography weights (Gabarito, Open Sans variants) are observed as font-family declarations, but exact size/line-height pairings for a full type scale, actual heading hierarchy, and font licensing/availability were not verified. No live layout, responsive breakpoints, hover/focus/active interaction states, or mobile navigation behavior were observed—all such details above are explicitly proposed. Component padding, radii, and spacing values are drawn from the fixed scale provided and are not measured from rendered elements.
