---
version: alpha
name: "Meross"
source_url: "https://meross.com"
captured_at: "2026-09-28T04:56:53.505960+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Meross's site evidence shows a clean, light-mode Vue/Element-UI-based storefront with a
  saturated cyan-blue accent (#0097e0, with a slightly deeper #0d8ed6 used on hover states)
  set against white surfaces and near-black/dark-gray text (#000000, #333333). Navigation
  chrome uses a muted gray (#8f8e93) for inactive menu items and a soft neutral shadow
  (#a29e9e) for the fixed header's drop shadow. Typography relies on a proprietary
  "CentraNo2" family in four weights (Light, Regular, Bold, Black) with Arial/Helvetica/
  sans-serif and CJK fallbacks (PingFang SC, Microsoft YaHei), consistent with a
  bilingual/global product site. The submenu and cookie-banner CSS reveal fully rounded
  pill buttons (2rem radius) and rounded submenu panels, suggesting a soft, approachable
  UI language appropriate to a consumer IoT brand. Several colors in the supplied palette
  (success green, warning orange, danger red, info gray, and numerous light-blue/gray
  tints) match Element UI's default component palette rather than confirmed brand marks;
  these are treated here as inferred system/status colors for form and alert states,
  not primary brand identity. Layout structure (grid widths, container sizes) is not
  measurable from the supplied CSS and is proposed rather than observed.

colors:
  primary: "#0097e0"
  primary-hover: "#0d8ed6"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#8f8e93"
  hairline: "#dcdfe6"
  surface-soft: "#f8fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  shadow-neutral: "#a29e9e"
  footer-ink: "#1a2139"
  text-secondary: "#3c4043"
  success: "#67c23a"
  warning: "#e6a23c"
  danger: "#f56c6c"
  info: "#909399"
  border-light: "#c8c9cc"
  surface-alt: "#f2f3f5"
typography:
  display-xl: {fontFamily: "CentraNo2-Black, Arial, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "CentraNo2-Bold, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "CentraNo2-Bold, Arial, sans-serif", fontSize: 25.6px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "CentraNo2-Regular, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "CentraNo2-Light, Helvetica, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "CentraNo2-Light, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "CentraNo2-Regular, Arial, sans-serif", fontSize: 17.6px, fontWeight: 400, lineHeight: 1, letterSpacing: 0px}
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
    backgroundColor: "{colors.canvas}"
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
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary-hover}"
    typography: "{typography.body-sm}"
    shadow: "0 0.13rem 0.6rem {colors.shadow-neutral}"
    height: "57px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.text-secondary}"
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
  device-status-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-light}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    onlineColor: "{colors.success}"
    offlineColor: "{colors.muted}"
    alertColor: "{colors.danger}"
    typography: "{typography.body-sm}"

## Components
**button-primary** is the pill-shaped call-to-action seen in the cookie-consent banner (`border-radius:2rem`, white text on a solid fill); the fill color itself was not directly captured on the button but is proposed as the brand primary blue, consistent with hover-state link colors elsewhere in the header. **button-secondary** is a proposed outline variant for lower-emphasis actions such as "Learn more," inferring the same pill shape for visual consistency. **text-input** is a proposed form field style since no explicit input CSS was supplied; border and radius are inferred from the site's generally soft, rounded chrome. **nav-bar** reflects the observed fixed header (`position:fixed`, `height:3.571rem`, white background, drop shadow using the supplied `#a29e9e`), with muted gray inactive items and a blue hover/active state drawn directly from the CSS. **product-card** is a proposed pattern for listing smart-home devices (plugs, sensors, switches); no card CSS was supplied, so border, radius, and padding are inferred defaults matching the site's soft-rounded submenu panels. **hero** is inferred from the homepage copy pattern (large heading + "Learn more" links for featured products like the Bluetooth Sensor Kit); no hero-specific CSS was captured. **footer** uses the dark navy `#1a2139` as an inferred background (present in the palette but not confirmed to a footer selector) since the visible footer text (copyright, links) suggests a darker closing band typical of the category; this mapping is speculative. **badge** is proposed for labeling product states (e.g., "New") using a light neutral surface, inferring restraint consistent with the observed light UI. **search** is a proposed pattern, unobserved directly, styled to match the soft surface tone (`#f8fafb`) seen in the palette. **device-status-card**, the category-appropriate component, proposes a compact card for showing a smart device's connectivity state, using the Element-UI-style semantic colors (success/warning/danger/info) present in the supplied palette for status indication — a reasonable inferred fit for a home-automation dashboard context, though no such UI was directly observed in the evidence.

## Responsive Behavior
Recommendation only — no responsive/mobile layout was observed in the supplied evidence.
| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <480px | Single-column stacking; nav collapses to hamburger/off-canvas menu |
| Tablet | 480–960px | Two-column product grids; submenu panels may become accordions |
| Desktop | 960–1440px | Fixed header as observed (~57px height); multi-column mega-menu submenus |
| Wide | >1440px | Max-width content container centered; hero imagery scales up |

Touch targets should be at least 44×44px; the pill button radius (`{rounded.full}`) and generous horizontal padding in the observed cookie button support this at desktop scale. The multi-column "submenu-full-screen" pattern observed in CSS should collapse to a vertical accordion below tablet width — this collapse behavior is proposed, not measured.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover/focus/active, form validation, mobile menu behavior) were directly observed. Several palette entries (e.g., success/warning/danger/info blues, greens, oranges, and grays) match default Element UI component-library colors rather than confirmed brand-specific choices, and are labeled as inferred semantic/status colors rather than verified brand identity. Button fill colors, hero section styling, footer background, product-card, and search-input styling were not present in the supplied CSS and are proposed patterns only. Font sizes not directly present in the supplied rules (display-xl, display-md, body-md, body-sm, caption) are proposed scale values, not measured. Availability, licensing, and web-font-loading behavior of the proprietary "CentraNo2" family were not verified. No breakpoint values or media queries were present in the supplied CSS; the responsive table above is a design recommendation only.
