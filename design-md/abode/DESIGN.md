---
version: alpha
name: "Abode"
source_url: "https://goabode.com"
captured_at: "2026-09-28T09:38:13.306745+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Abode's observed CSS shows a clean, technical DIY-security aesthetic: white canvas (#ffffff),
  a near-black slate ink (#2d3037) for headings and body copy, and a cyan-teal primary
  (#44bed8) used consistently for buttons and text links, with a darker teal hover state
  (#3dabc2) confirmed in :hover rules. A secondary "dark-blue" button variant (#3652e7,
  hover #0041c4) appears alongside the primary teal, suggesting a two-accent system for
  primary vs. alternate CTAs. Typography pairs Rubik for large headings (48px/500 weight,
  observed on h1) with Inter for body copy and buttons (16px body, 14px/600 buttons),
  both falling back to system sans-serif stacks.
  This interpretation extends that evidence into a full system: muted grays (#a1a4b2,
  #62697a) are inferred for secondary text and metadata; a light divider tone (#dfe4eb)
  is proposed for hairlines and card borders since no explicit border color was captured;
  and status colors (success #39bd76, warning #ebb238, danger #fb5858) are inferred from
  the broader palette to support security-specific states like armed/disarmed and sensor
  alerts, which are common to this product category but not directly observed in the
  supplied CSS. Fully-rounded (pill) buttons are directly observed via border-radius:360px.

colors:
  primary: "#44bed8"
  primary-hover: "#3dabc2"
  secondary: "#3652e7"
  secondary-hover: "#0041c4"
  ink: "#2d3037"
  body: "#62697a"
  muted: "#a1a4b2"
  hairline: "#dfe4eb"
  canvas: "#ffffff"
  surface-soft: "#f7f9fa"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  disabled: "#8fd8e8"
  success: "#39bd76"
  warning: "#ebb238"
  danger: "#fb5858"
  info: "#1e73be"
  dark: "#1a1a2e"
typography:
  display-xl: {fontFamily: "Rubik, sans-serif", fontSize: "48px", fontWeight: 500, lineHeight: 1.15, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Rubik, sans-serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Rubik, sans-serif", fontSize: "24px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.5, letterSpacing: "0px"}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.base} {spacing.xl}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    position: "sticky-top"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    overlayButton: "button-white-blur"
    typography: "{typography.display-xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  faq-accordion:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.body-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  device-status-indicator:
    armedColor: "{colors.success}"
    disarmedColor: "{colors.muted}"
    alertColor: "{colors.danger}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** reflects the directly observed `.button` rule: cyan-teal fill (#44bed8), white text, pill-shaped radius (360px, mapped to `rounded.full`), and a confirmed hover to a deeper teal (#3dabc2). Padding is approximated to the closest scale steps from the observed 16px/42px values.

**button-secondary** models the observed `.button.outline` pattern: transparent background, teal text and border, filling solid teal on hover. This is used for lower-emphasis actions like "Compare Systems" or "Shop Cameras."

**nav-bar** is inferred from the observed sticky `#header` rule (white background, position:sticky, subtle shadow) combined with the text-based mega-menu categories present in the page text (Security Systems, Cameras, Add-ons, Integrations, Compare, Blog). Exact menu layout and dropdown behavior are proposed, not measured.

**hero** is a proposed full-bleed section pattern inferred from page copy ("Build a System / Shop Abode") and the observed `.button.white` variant with `backdrop-filter: blur(10px)`, suggesting a translucent white CTA over a photographic/dark background — a common security-brand hero treatment, not directly confirmed in layout terms.

**product-card** is proposed for the kit/device grids (Iota, Smart Security Kit, Abode Cam 2, sensors) implied by repeated product names and discount callouts in the page text. Card surface, radius, and spacing are inferred defaults using the neutral surface and hairline tokens.

**badge** supports the frequent percentage-off labels seen in the content ("50% OFF," "42% OFF," "45% OFF"). Color is inferred as danger/red for urgency-style discount tags, since no explicit badge CSS was supplied.

**faq-accordion** is proposed to match the structured Q&A content on the page (HomeKit compatibility, subscription requirements, DIY install, monitoring). Typography reuses body tokens; interactive expand/collapse states are not observed.

**device-status-indicator** is a category-specific, fully inferred component for representing armed/disarmed/alert states common to security systems, using the success, muted, and danger tokens from the broader observed palette since no live app or dashboard UI was captured.

**footer** and **search** are both proposed patterns using dark and soft-surface tokens respectively; neither footer background nor search-field styling was present in the supplied CSS, so these are structural placeholders consistent with the rest of the system.

## Responsive Behavior

This is a recommended pattern set, not measured site behavior:

| Breakpoint | Width      | Layout guidance                                  |
|-----------|------------|---------------------------------------------------|
| mobile    | 0–599px    | Single-column stacks; nav collapses to hamburger  |
| tablet    | 600–1023px | 2-column product grids; nav shows condensed items |
| desktop   | 1024–1439px| 3–4 column product grids; full mega-menu          |
| wide      | 1440px+    | Max-width container (~1280px), centered content   |

Touch targets should be a minimum of 44×44px, particularly for pill-shaped buttons and badge/status chips. Primary navigation is expected to collapse into a slide-in or drawer menu below tablet width; this collapse behavior is proposed and was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered layout, breakpoints, or interaction states (hover, focus, active, disabled beyond the one `.button.disabled` rule) were directly observed except where explicitly noted.
- Several roles (body secondary text, hairline/divider color, surface-soft/surface-card) are inferred from the general observed palette rather than tied to a specific selector.
- Padding values on `button-primary`/`button-secondary` are approximated to the nearest spacing-scale steps; the observed values (16px/42px) do not map exactly to the defined scale.
- Footer, search, hero, product-card, faq-accordion, and device-status-indicator are proposed structural components based on page content and category norms, not confirmed by supplied selectors.
- Font availability, licensing, and exact weight range for Rubik and Inter were not verified beyond the values present in the supplied `@font-face`/body rules.
- Mobile and tablet navigation collapse patterns are recommendations only; no responsive CSS or media queries were included in the supplied evidence.
