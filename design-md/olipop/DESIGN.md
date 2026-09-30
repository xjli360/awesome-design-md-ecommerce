---
version: alpha
name: "Olipop"
source_url: "https://drinkolipop.com/"
captured_at: "2026-09-29T04:15:58.508339+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from drinkolipop.com's verified storefront CSS and
  visible palette. The site pairs a deep botanical green (#034638, #14433d) with
  warm cream surfaces (#fff6ea, #fffbf5) and a bright citron accent (#ffff7d,
  hover #e2eb28) used on the observed ".button-citron" pill control. A secondary
  teal (#008168) appears on the video-hero play button, and a soft blue
  (#2491c4) and reserved red (#d20000) appear in the palette but their exact
  product use is not confirmed from static evidence, so they are treated as
  inferred secondary/status accents. Typography is anchored on two confirmed
  font tokens: "Ano" (used explicitly in the button-citron rule, weight 700,
  18px/28px) for interactive and title text, and "WindsorEF"/"Windsor Bold" —
  present in the font list and consistent with Olipop's known display-headline
  use — proposed here for display headings; a "Brown" family is present in the
  font list and is proposed for running body copy, with Inter/system sans-serif
  as safe fallbacks. Rounded values follow the observed 50px pill radius on
  buttons, generalized to a full-round token; card and surface radii are
  proposed since no explicit card CSS was supplied. Spacing is a standard
  proposed scale, not measured from layout. Overall the interpretation aims for
  a friendly, grocery-shelf-adjacent CPG feel: cream backgrounds, deep green
  trust color, and a punchy citron call-to-action.

colors:
  primary: "#034638"
  ink: "#14433d"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#737373"
  hairline: "#e6e6e6"
  surface-soft: "#fff6ea"
  surface-card: "#fffbf5"
  on-primary: "#ffffff"
  accent-citron: "#ffff7d"
  accent-citron-hover: "#e2eb28"
  accent-teal: "#008168"
  accent-blue: "#2491c4"
  status-alert: "#d20000"
  status-success: "#44be70"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "WindsorEF, Windsor Bold, serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "WindsorEF, Windsor Bold, serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Ano, Ano Bold, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Brown, Inter, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Brown, Inter, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Brown, Inter, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Ano, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 28px, letterSpacing: 0px}
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
    backgroundColor: "{colors.accent-citron}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-citron-hover}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    activeBorder: "2px solid {colors.accent-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** reflects the confirmed `.button-citron` rule: a fully-rounded pill with a citron fill, bold Ano typography, and a documented hover shift to `#e2eb28`. It is proposed as the primary "Add to Cart" / "Shop" action.

**button-secondary** is a proposed outline variant using the primary green for contexts (e.g., "Find a Store") where a lower-emphasis action sits beside a citron CTA. Hover/focus states are not observed and are proposed as a fill-on-hover pattern.

**text-input** is a proposed field style for the "Subscribe" email capture form referenced in the footer copy; border and radius values are inferred defaults, not measured from the klaviyo form markup.

**nav-bar** represents the top utility/nav row ("Shop / Learn / Subscribe / Find a store / Log in") implied by the page text. Background and hairline are proposed since no nav-specific selector was supplied.

**product-card** is proposed for the flavor grid ("Caramel Apple," "Cherry Cola," etc.) with "Add 12 Pack" actions. Card background uses the warm off-white surface tone; exact card padding/shadow was not present in supplied CSS.

**hero** models the "Drippin' in delicious" flavor-launch banner, using the display headline typography and cream surface tone consistent with the palette's warm neutrals.

**footer** uses the dark green primary as background per common Olipop footer treatment; text/link colors default to on-primary white. Actual footer background hex was not directly confirmed in supplied selectors and is treated as inferred.

**badge** is proposed for labels like "New" and "9g Fiber" / "6g Fiber" line tags seen in the page text, using the citron-hover tone for visibility against cream or white surfaces.

**search / flavor-selector** are proposed, category-appropriate patterns: a pill search field and a flavor/fiber-line filter control (9g vs 6g), styled consistently with the button and badge radii but not tied to a specific observed selector.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <480px | Single-column flavor grid, stacked nav collapsed to menu icon |
| tablet | 480–1024px | 2–3 column product grid, inline nav links |
| desktop | >1024px | Full multi-column flavor grid, persistent top nav |

Touch targets should be at least 44px tall, matching the Shopify accelerated-checkout button min-height token (`44px`) observed in supplied CSS. Nav and filter controls are proposed to collapse into a hamburger/drawer pattern below tablet width; this is a recommendation, not an observed mobile behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no rendered layout, real interaction states, or JavaScript-driven behavior (carousels, add-to-cart flows, flavor selectors) were observed. Color role assignments (e.g., which green is "primary" vs. "ink", which yellow is default vs. hover) are inferred from partial selector context and may not match final brand usage. "WindsorEF"/"Windsor Bold" and "Brown" appear only as font-family names in the supplied evidence with no confirming selector shown; their actual application to headings/body text is inferred, not verified, and custom font licensing/availability was not checked. All spacing, radius, and breakpoint values beyond the single confirmed 50px pill radius and 18px/28px button type are proposed defaults for a beverage e-commerce interface, not measurements from the live site.
