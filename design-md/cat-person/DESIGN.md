---
version: alpha
name: "Cat Person"
source_url: "https://catperson.com"
captured_at: "2026-09-28T04:46:19.019014+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cat Person's observed CSS shows a restrained, clinical-clean palette anchored by true black (#000000) and white (#ffffff), with a soft powder-blue family (#c7dbf0, #8fb7e1, #e3edf7) used specifically for call-to-action buttons and their hover states. Dark neutral text (#24292e) pairs with the light-blue buttons, while pure black/white pairs drive higher-contrast "dark" button variants. A wider gray scale (#333333 through #e6e6e6) supports body copy and hairlines, and a scattered set of saturated accents (#ff1138, #41bb80, #ffab00, #2563eb) appear in the extracted palette but are not tied to any component in the supplied evidence, so they are treated here as inferred utility/status colors rather than confirmed brand accents.
  Typography combines a licensed display family, Cooper (Light/Medium weights with italics), for headline-style moments with a Haas Grot pairing (Disp for buttons/labels, Text for body copy) for interface text, falling back to Helvetica Neue/Arial/sans-serif and Georgia/serif. This interpretation proposes a calm, product-forward layout: soft-blue primary actions, black secondary/dark actions, generous uppercase button labels, and light gray surfaces separating content sections. Sizing, spacing scale, and most component states beyond the observed button rules are proposed, not measured.

colors:
  primary: "#c7dbf0"
  ink: "#24292e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#e5e5e5"
  surface-soft: "#f1f1f3"
  surface-card: "#f5f5fa"
  on-primary: "#24292e"
  on-dark: "#ffffff"
  accent-hover: "#8fb7e1"
  secondary-dark: "#000000"
  highlight-soft: "#ffd8dc"
  success: "#41bb80"
  warning: "#ffab00"
  danger: "#b91c1c"
  link: "#2563eb"
  border-strong: "#333333"
typography:
  display-xl: {fontFamily: "CooperLtBTWXX-Light, Georgia, serif", fontSize: 48px, fontWeight: 300, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "CooperMdBTWXX-Medium, Georgia, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Haas Grot Disp Web, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Haas Grot Text Web, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Haas Grot Text Web, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Haas Grot Text Web, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Haas Grot Disp Web, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 2px}
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
    borderColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.accent-hover}"
      borderColor: "{colors.accent-hover}"
      textColor: "#000000"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "#e3edf7"
  button-dark:
    backgroundColor: "{colors.secondary-dark}"
    borderColor: "{colors.secondary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.canvas}"
      textColor: "#000000"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focus:
      borderColor: "{colors.link}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.highlight-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-plan-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.link}"
    selectedBackground: "#e3edf7"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-md}"
    detailTypography: "{typography.body-sm}"

## Components
**button-primary** reflects the observed `.button__cta` rule set: a soft powder-blue fill (#c7dbf0) with a matching border and dark ink text, shifting to the darker #8fb7e1 blue on hover/active exactly as coded. This is Cat Person's primary conversion action (e.g., "Start a Plan").

**button-secondary** mirrors `.button-secondary`: white background, dark 2px border, dark text, with a very light blue hover fill (#e3edf7) — proposed for lower-emphasis actions like "Learn More."

**button-dark** follows `.button-dark`: solid black fill with white text, inverting to white/black on hover. Likely used for high-contrast placements such as dark hero sections or sticky bars; hover inversion is observed in CSS, not confirmed live.

**text-input** is not present in the supplied CSS; its light border, white background, and blue focus ring are proposed conventions consistent with the observed hairline gray and link-blue values.

**nav-bar** is inferred from the page text listing "Log in / Wet Food / Dry Food / Treats / Toys / Shop All / Food Philosophy / Help & FAQ" — a simple white header with dark uppercase-style labels; exact spacing/height is proposed.

**product-card** is a proposed pattern for a food/treats storefront: white-to-off-white surface, rounded corners, product title in the Haas Grot Disp headline style, and price in dark ink — no card CSS was supplied.

**hero** is proposed based on the marketing copy ("Real, Healthy Cat Food Made Simple") pairing a large Cooper-family headline over a soft surface tone with a primary CTA button beneath it.

**footer** is proposed as a black band (matching `.button-dark`'s black/white pairing) with white text links, a common pattern for direct-to-consumer subscription brands; not confirmed from evidence.

**badge** and **search** are proposed utility components using the palette's soft pink (#ffd8dc) and rounded pill shapes for tags like "New" or "Grain-Free," and a pill-shaped search field consistent with the button radius conventions.

**subscription-plan-selector** is a category-appropriate proposed component for a cat-food subscription flow (the site markets a monthly delivery plan): selectable cards using the surface-card background, hairline borders, and a link-blue highlighted state for the chosen plan.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Range | Target | Notes |
|---|---|---|
| ≤479px | Small mobile | Single-column, stacked nav collapses to a menu icon |
| 480–767px | Mobile | Buttons full-width, product cards single column |
| 768–1023px | Tablet | 2-column product/plan grids |
| 1024–1439px | Desktop | 3–4 column grids, inline nav |
| ≥1440px | Large desktop | Max-width content container, extra whitespace |

Touch targets should be at least 44×44px; buttons already use generous padding (1.3rem 1.5rem per observed CSS) which supports this. Navigation is expected to collapse into a hamburger/drawer pattern below tablet width; this collapse behavior was not observed and is a standard proposal.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, DOM structure, or JavaScript-driven states were observed. Role assignments for many palette colors (e.g., #ff1138, #41bb80, #ffab00, #2563eb, #00b67a) are inferred utility/status guesses since no selectors tied them to specific UI elements. Font sizes, weights, and line-heights outside the explicitly captured button rule are proposed values, not measured. Layout structure (hero, product-card, nav-bar, footer, subscription-plan-selector) is inferred from page text and category convention, not from captured layout CSS. Mobile/responsive behavior and interaction states beyond the documented button hover/active rules are not observed. Availability, licensing, and web-font loading of Cooper and Haas Grot families were not verified and should be confirmed before implementation.
