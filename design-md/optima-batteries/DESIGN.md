---
version: alpha
name: "Optima Batteries"
source_url: "https://optimabatteries.com"
captured_at: "2026-09-29T03:59:32.944901+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Optima Batteries presents a dark, high-contrast storefront running on a Salesforce
  Commerce/Experience Cloud stack (visible via slds-, dxp-, and lwc- prefixed
  selectors). The confirmed page shell sets `body` to white text on a black
  background (--opt-color-white / --opt-color-black), giving the site a
  performance/automotive tone consistent with racing sponsorships and product
  lines named RedTop, YellowTop, BlueTop, and OrangeTop. The observed palette
  is broad and includes many Salesforce Lightning Design System utility tones
  (blues like #0176d3/#1b96ff, greens, semantic reds) that are platform
  defaults rather than confirmed brand marks; a smaller set of reds, oranges,
  yellows and blues plausibly echoes the product-line naming and is used here
  as inferred accent colors. The exact hex behind the CSS variable
  `--primary-color` was not resolved in the supplied evidence, so the primary
  action color below is an inferred selection from the observed red swatches.
  Typography combines a Barlow/Barlow Condensed workhorse stack with several
  Knockout condensed display weights, which strongly suggests a bold
  motorsport-style headline face paired with a clean grotesque for body and UI
  text; this mapping is inferred, since the heading font-family CSS variable
  was not resolved to a literal name. Layout evidence includes an 8px-radius
  combobox/button pattern from the "battery finder" tool, used below as a
  concrete component reference.

colors:
  primary: "#ea001e"
  ink: "#ffffff"
  canvas: "#000000"
  body: "#ffffff"
  muted: "#939393"
  hairline: "#2e2e2e"
  surface-soft: "#181818"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffdd00"
  accent-blue: "#1b96ff"
  accent-orange: "#ff5d2d"
  border-strong: "#444444"
typography:
  display-xl: {fontFamily: "KnockoutNo.67FullBantamweight, Barlow Condensed, sans-serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.05, letterSpacing: 0.5px}
  display-md: {fontFamily: "KnockoutNo.68FullFeatherweight, Barlow Condensed, sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.5px}
  title-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.25px}
  body-md: {fontFamily: "Barlow, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Barlow, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 1px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  battery-finder-panel:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.primary}"
    headerBorderColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** targets the site's calls to action (SHOP NOW, LEARN MORE, SIGN UP). It uses the inferred brand red against white text, with the compact `sm` radius consistent with the flat, angular automotive tone of the visual references; hover/active states are proposed, not observed.

**button-secondary** is a proposed outline/ghost treatment for secondary actions in dark hero sections, using an underline-reveal affordance loosely suggested by the `.slds-button__neutral` `::before` underline animation seen in the CSS, adapted here as a generic pattern rather than a literal reproduction.

**text-input** reflects the confirmed `.optima-combobox-input__button` rule set: black background, no border, `8px` radius, and roughly `17px/16px` padding, generalized here for form fields such as the "Find Your Battery" year/make/model selectors.

**nav-bar** is inferred from the presence of `.optima-header`, mobile nav toggle lines, and cart/account link styling. It assumes a black bar with white text and a condensed button-style label typography; exact height, sticky behavior, and hover treatment are not confirmed by the evidence.

**product-card** is proposed for the "Shop by Application" and "Shop by Product Line" tiles (Car & Truck, RedTop, YellowTop, etc.). Given the site's photography-driven tiles typically sit on light backgrounds for contrast against the black page, a white card surface is used; this is an inferred, not measured, choice.

**hero** models the large rotating banner ("WHATEVER MOVES YOU…", "ORANGETOP QH6…") using the confirmed black canvas, white heading color, and the largest display type scale, with generous vertical section spacing typical of full-bleed carousel hero patterns.

**footer** is inferred from the link groups (SHOP, SUPPORT, CONNECT, ABOUT, FIND OPTIMA) and the Clarios copyright line. A slightly lighter near-black surface separates it from the primary black canvas, with muted grey body text and hairline dividers between columns.

**badge** is a small proposed label element for flagging product-line names or promotional tags (e.g., "NEW", "ORANGETOP"), using the yellow accent for visibility against the dark canvas; not confirmed against any specific observed badge markup.

**search** generalizes the header "Search" affordance and the battery-lookup inputs into a shared dark, rounded field pattern consistent with the one concrete combobox rule available in the evidence.

**battery-finder-panel** is the category-appropriate component: it reproduces the confirmed structure of `.optima-static-battery-finder__header` (primary-color background, white 12px right border) paired with the black-background, rounded combobox inputs used for Vehicle Type/Year/Make/Model/Engine selection — a distinguishing, evidence-backed pattern for an automotive battery retailer.

## Responsive Behavior

Recommended (not measured) breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | single-column stacked nav, hamburger toggle (`.nav-button__line` suggests a 3-line icon), battery finder fields stack vertically |
| tablet | 600–1023px | 2-column product/application grids, condensed nav remains collapsed |
| desktop | 1024–1439px | full horizontal nav, multi-column carousels and product-line grids |
| wide | 1440px+ | max-width content container, larger hero display type |

Touch targets should be at least 44×44px for finder dropdowns and nav buttons. The mobile nav close button and hamburger lines observed in CSS imply a slide-in or overlay pattern on small screens; exact animation, breakpoint values, and collapse thresholds are proposed defaults, not measured from live responsive testing.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.


- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states were observed. The palette includes numerous Salesforce Lightning Design System (SLDS) utility and semantic tokens (e.g., blues, greens, standard reds) inherent to the underlying commerce platform, which may not correspond to Optima's intentional brand colors — the `primary` value here is an inferred selection from the available reds since `--primary-color`'s literal hex was not resolved in evidence. Heading font-family was referenced via `var(--dxp-g-heading-font-family)` without a resolved literal name; Knockout condensed weights are present in the font list and are used here as the most plausible inferred display face, but this mapping is unconfirmed. Card, footer, and nav surface colors are proposed for contrast and usability, not observed computed styles. No hover, focus, error, or loading states were observed for any component. Mobile menu behavior, carousel interaction, and cart/account flows are inferred from class names only. Availability and licensing of the Knockout and Barlow font families for production use have not been verified.
