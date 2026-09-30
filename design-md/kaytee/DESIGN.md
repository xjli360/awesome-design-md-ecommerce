---
version: alpha
name: "Kaytee"
source_url: "https://kaytee.com"
captured_at: "2026-09-28T09:17:55.210397+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kaytee's supplied CSS evidence combines a legacy Sitecore/jQuery-UI base theme
  with brand-level component overrides, yielding a broad but only partially
  brand-specific palette. Directly observed rules confirm white (#ffffff) page
  backgrounds, near-black body copy (#000/#333333), and an accordion
  variant using a deep maroon-red header (#9f1c33) on white text — the clearest
  brand-specific color signal in the evidence. The wider palette contains warm
  oranges (#f47523), teals (#15909c, #89c6cc), navy (#263971), greens (#006e43),
  golds (#f0b323, #ecb324), and multiple reds (#ae1831, #de232f, #c01f3a),
  consistent with a multi-species (small animal / pet bird / wild bird) brand
  system using color-coded sections; this segmentation is inferred, not proven
  by the supplied rules. Typography is only directly confirmed as
  Arial/Helvetica for body text and Trebuchet MS/Tahoma for legacy UI widgets;
  Gotham, Bernhardt CG, Montserrat, Open Sans, and Roboto appear in the font
  list but their specific applied roles are not confirmed by the supplied
  declarations, so heading fonts here are proposed/inferred. This interpretation
  favors a clean, editorial pet-care layout: warm neutral surfaces, a maroon/red
  accent inherited from the observed accordion pattern, and generous section
  spacing to support the site's multi-species content hubs.

colors:
  primary: "#9f1c33"
  accent-orange: "#f47523"
  accent-teal: "#15909c"
  accent-navy: "#263971"
  success: "#006e43"
  gold: "#f0b323"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#75767a"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#fdf9f4"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Gotham', 'Montserrat', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Gotham', 'Montserrat', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  species-tile:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-teal}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.base}"
    typography: "{typography.body-sm}"

## Components

**button-primary** uses the maroon-red (#9f1c33) that is the one clearly brand-specific accent color confirmed in the supplied CSS (the accordion variant-2 header background). Applying it to primary CTAs is a proposed extension of an observed pattern, not a directly confirmed button style.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "See Why We're Vet Recommended"), reusing the primary hue as text/border on a transparent fill; no secondary-button CSS was present in evidence.

**text-input** follows generic form conventions inferred from the reset stylesheet's neutral, undecorated base styles; no dedicated input skin was observed beyond the legacy jQuery UI widget styles, which are treated as non-brand chrome.

**nav-bar** is proposed as a light, white-background bar given the reset's white canvas and dark body text, appropriate for the catalog/species navigation described in the page content (Small Animal, Pet Bird, Wild Bird, Learn & Care).

**product-card** supports the "Our Family of Products" grid (Forti-Diet, Clean & Cozy, Timothy Complete, etc.) using the warm off-white surface-card tone (#fdf9f4) observed in the palette, paired with a hairline border for separation; card elevation/shadow was not observed and is omitted.

**hero** is proposed for the homepage's "The Little Things Make a Big Difference" banner, using a soft neutral surface and the largest display type scale; no hero-specific background color or image treatment was confirmed in evidence.

**footer** proposes a dark ink-colored footer for the About/Find Products/Learn and Care link columns and social/newsletter sign-up; the reset CSS did not include footer-specific declarations, so this is an inferred convention.

**badge** is proposed for content like "150 Years" or "Vet Recommended" callouts, using the observed gold tone (#f0b323) as an accent chip; no badge markup or styling was present in the supplied rules.

**search** is proposed for the site's visible "Search" affordance, styled as a pill-shaped field on the soft-gray surface tone; no search-bar CSS was captured in evidence.

**species-tile** is a category-specific component proposed for the "Find Care for Your Small Animals & Birds" grid (Rabbit, Guinea Pig, Conure, Canary, etc.), using a teal accent to distinguish species/category links; this pattern is inferred from the page's textual content structure, not from captured tile CSS.

## Responsive Behavior

Recommended breakpoints (not measured from live site):
| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacks; nav collapses to menu toggle |
| tablet | 600–959px | 2-column product/species grids |
| desktop | 960–1279px | 3–4 column grids; full nav bar |
| wide | 1280px+ | Max-width content container, unchanged column count |

Touch targets should be at least 44×44px for nav, search, and CTA buttons. Navigation is expected to collapse into a hamburger/menu pattern below tablet width, and the species-finder grid should reflow from multi-column to single-column stacking on mobile. These are proposed conventions only; no responsive CSS or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus/active states, or JavaScript-driven interactions were observed. Most color-to-role mappings (primary, hero, footer, badge, species-tile accents) are inferred from a broad supplied palette and a single confirmed component rule (accordion variant-2), not from direct evidence of those specific components. Heading font usage (Gotham, Montserrat, Bernhardt CG) is listed in the font-family evidence but not tied to specific selectors in the supplied CSS, so display typography is proposed; availability and licensing of Gotham and Bernhardt CG for production use were not verified. Font sizes beyond the confirmed 12px body-text value are proposed, not measured. Spacing and rounded-corner scales are proposed design-system defaults, not extracted from layout CSS. Mobile/responsive behavior, breakpoints, and any grid/flex structure were not present in the supplied evidence and are marked as recommendations only.
