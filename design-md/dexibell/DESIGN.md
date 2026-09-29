---
version: alpha
name: "Dexibell"
source_url: "https://www.dexibell.com"
captured_at: "2026-09-28T09:34:11.726956+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dexibell's public site runs on WordPress with the Gutenberg block editor and the UIkit 3.1.5
  framework, and the observed evidence reflects that stack more than a bespoke brand system. The
  palette is dominated by neutral grays (#333333 headings, #666666/#999999 secondary text,
  #e5e5e5/#cccccc hairlines, #f8f8f8/#f4f4f4 light surfaces) with a near-black #32373c used as the
  actual button background/text-inverse pairing on `.wp-block-button__link`. Many other hexes in
  the supplied palette (e.g. #7a00df, #00d084, #0693e3, #34e2e4, #4721fb) match default WordPress
  block-editor color presets rather than confirmed brand choices, so they are treated here as
  unused/decorative rather than assigned roles. UIkit's own default theme colors (#1e87f0 primary,
  #32d296 success, #faa05a warning, #f0506e danger) are present in the CSS source and are mapped to
  functional accent/status roles as an inferred convention, since UIkit governs buttons, icon
  buttons and interactive states site-wide. Typography inherits the system font stack
  (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif) with UIkit's observed
  heading weight (400) and button treatment (14px, 38px line-height, uppercase). This interpretation
  proposes a restrained, catalog-driven UI suited to a technical instrument brand, leaning on
  neutral surfaces and a dark, high-contrast primary action color rather than invented brand hues.

colors:
  primary: "#32373c"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#e5e5e5"
  surface-soft: "#f8f8f8"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent: "#1e87f0"
  success: "#32d296"
  warning: "#faa05a"
  danger: "#f0506e"
  border: "#cccccc"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: "38px", letterSpacing: "0.5px", textTransform: "uppercase"}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.border}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  product-spec-table:
    backgroundColor: "{colors.canvas}"
    rowAltBackground: "{colors.surface-soft}"
    hairlineColor: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "#444444"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the dark near-black `#32373c` background with white text and a full pill
radius, matching the observed `.wp-block-button__link` rule directly (background, text color, and
`border-radius:9999px`). This is the strongest directly-evidenced interactive style on the site.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Learn more"
links on product tiles), reusing the same pill shape and button typography but with a transparent
fill and neutral border; its exact state styling is not observed.

**text-input** is proposed for newsletter/search/contact fields referenced in the page text
("Iscriviti alla newsletter", contact form). Border and radius values are inferred from the
neutral gray palette since no explicit input CSS was supplied.

**nav-bar** models the top navigation implied by the product/menu structure (Home, Products,
Accessories, Support, My Dexibell). Colors are inferred from the light canvas and heading-ink
palette; no header CSS block was supplied, so height, sticky behavior, and exact spacing are
proposed.

**product-card** supports the large VIVO/CLASSICO/COMBO instrument catalog. It uses the light
card surface (`#f4f4f4`) against the white canvas with a thin hairline border, sized for grid
listings; hover/focus elevation is not observed and is left undefined.

**product-spec-table** is a category-appropriate addition for digital piano technical
specifications (keybed type, polyphony, speaker wattage) commonly needed on instrument product
pages; alternating row shading uses the observed light surface tone for scannability.

**hero** is proposed for homepage banners like the "T2L Electric Piano" and "aquaviva 6.0 OS"
announcements referenced in the page text, using the largest display typography over the soft
light background; no hero CSS was directly supplied.

**footer** uses the dark primary tone for the site-wide footer, consistent with brand contact
info, legal text (Proel S.p.A.), and social links; text is white for contrast. Hairline dividers
between footer columns use a slightly lighter dark gray, proposed for legibility.

**badge** is proposed for "New" or "Novità" labels seen in the News & Social feed (e.g. dated
announcements), using the UIkit-sourced accent blue as a functional highlight color.

**search** models the store-locator / dealer-search flow mentioned in the copy ("Cerca il
rivenditore più vicino a te"), styled as a pill-shaped field on a soft neutral background.

## Responsive Behavior

This is a proposed recommendation, not measured site behavior. UIkit's own breakpoints were
present in the source CSS and are reused as a baseline:

| Breakpoint | Width | Layout guidance (proposed) |
|---|---|---|
| s | 640px | Single-column stacks, nav collapses to a toggle/hamburger menu |
| m | 960px | 2-column product grids, inline search |
| l | 1200px | 3–4 column product grids, full horizontal nav |
| xl | 1600px | Widened container, unchanged grid density |

Touch targets for buttons and icon controls should be at least 36–44px, aligning with the
observed `.uk-icon-button` 36×36px sizing. Navigation collapse, sticky-header behavior, and exact
grid column counts were not observed and should be validated against the live responsive site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, JavaScript
behavior, hover/focus states, or real breakpoint changes were observed. The primary brand color
(`#32373c`) is confirmed from one button rule, but no dedicated brand palette (e.g. a signature
accent hue) was present in the evidence — many supplied hex values match default WordPress
block-editor presets and UIkit framework defaults rather than confirmed Dexibell brand choices,
and are labeled/used accordingly as inferred or functional-only. Font stacks are system fonts only
(no proprietary/licensed webfont evidence was supplied), so no custom font availability or
licensing claims are made. Spacing scale, card elevation, hero and footer exact measurements,
mobile navigation pattern, and product-grid column counts are proposed conventions, not measured
values. Component states beyond the directly observed button rule (hover, active, disabled) are
proposed and unverified.
