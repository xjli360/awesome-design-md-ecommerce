---
version: alpha
name: "Farrow & Ball"
source_url: "https://farrow-ball.com"
captured_at: "2026-09-28T09:05:30.055585+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built strictly from the supplied CSS evidence for
  farrow-ball.com, a Magento-based storefront selling handcrafted paint and
  wallpaper. The observed palette leans on muted, tonal neutrals (#f6f6f6,
  #eceae1, #cecece, #45484b) consistent with a paint-and-decorating retailer
  that lets product colour swatches carry visual weight rather than a loud
  brand palette. A desaturated teal-blue (#397082) and a deep sage (#467c5b)
  recur in the observed color list and are assigned here as primary and
  accent roles; this mapping is inferred, not confirmed as the brand's
  official accent color. #cecece appears repeatedly as a border-color across
  layout blocks and is mapped to hairline. #f6f6f6 appears as a repeated
  card background and is mapped to surface-soft; #eceae1 is a warmer
  observed neutral mapped to surface-card for contrast against pure white.
  Typography uses "Verlag" and "Open Sans" as observed in the font-family
  evidence, with sans-serif fallbacks; all sizes, weights and line-heights
  are proposed defaults, not measured. Components describe plausible
  e-commerce patterns (nav, product/colour cards, hero, footer, search)
  inferred from Magento/Page-Builder class conventions (data-pb-style
  blocks with border-radius and padding), not from any observed live
  rendering or interaction.

colors:
  primary: "#397082"
  ink: "#242627"
  canvas: "#ffffff"
  body: "#45484b"
  muted: "#757575"
  hairline: "#cecece"
  surface-soft: "#f6f6f6"
  surface-card: "#eceae1"
  on-primary: "#ffffff"
  accent-sage: "#467c5b"
  accent-red: "#a82635"
  accent-slate: "#3f4d57"
  accent-blue: "#135d95"
typography:
  display-xl: {fontFamily: "Verlag, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Verlag, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Verlag, sans-serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "'Open Sans', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.25px"}
  button-md: {fontFamily: "Verlag, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.accent-slate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
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
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg} {spacing.base}"
  colour-swatch-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary**: A solid-fill call-to-action ("Shop Dead Flat", "Get Mine") using the inferred primary teal-blue with white text. Hover/focus/disabled states are proposed, not observed.

**button-secondary**: An outlined variant for secondary actions ("Explore the collection"), sharing the primary color as border and text on a white ground. Interaction states are proposed.

**text-input**: A bordered field for search, email sign-up and account forms, using the observed hairline color (#cecece) as its border, consistent with border-color values repeated across multiple data-pb-style blocks in the evidence.

**nav-bar**: A white, top-anchored navigation bar hosting category flyouts (Paint, Wallpaper, Inspiration, Help & Advice) inferred from the page's mega-menu text content; visual structure (height, sticky behavior) is not observed and is proposed.

**hero**: A full-width promotional band (e.g. "Heritage, reimagined") using the darker slate accent as background with light body copy, echoing the dark background-color values (#4a5b6b-family tones approximated here by the observed #3f4d57) seen in page-builder hero-style blocks.

**footer**: A dark, ink-colored footer housing customer service links, B-Corp messaging and newsletter sign-up, inferred from the page text's footer-like content grouping; column layout is proposed.

**badge**: A small pill used for promotional flags such as "Free next day delivery" or sample-offer callouts, using the sage accent for a natural, paint-adjacent tone. Purely proposed; no badge markup was observed.

**search**: A soft-background search affordance styled with the repeated #f6f6f6 surface tone seen in multiple layout blocks, paired with a hairline border for definition.

**product-card / colour-swatch-card**: Two related card patterns — a general product-card (paint tins, wallpaper rolls) on the light gray surface (#f6f6f6), and a category-appropriate colour-swatch-card on the warmer surface (#eceae1) intended to represent individual paint shade tiles, since color/shade browsing is central to this brand's catalog. Rounded corners (8px) reflect the border-radius values repeatedly observed on data-pb-style card blocks.

## Responsive Behavior

Proposed breakpoint table (not measured from live responsive testing):

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | 0–599px    | Single-column stacking; nav collapses to a hamburger/off-canvas menu |
| tablet    | 600–1023px | Two-column card grids; condensed nav |
| desktop   | 1024–1439px| Multi-column grids (3–4 cards), full horizontal nav |
| wide      | 1440px+    | Max-width content container, generous side margins |

Touch targets are recommended at a minimum of 44×44px for buttons and nav items. Mega-menu flyouts should collapse into accordions on mobile. This table is a design recommendation only; no live responsive or interaction behavior was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extracted from page-builder class attributes (data-pb-style); no computed styles, live rendering, or DOM screenshots were available.
- Semantic role assignments (primary, accent-sage, accent-slate, accent-blue, accent-red) are inferred from a flat color list without confirmed usage context (text vs. background vs. decorative) for several values.
- Font sizes, weights, line-heights, and letter-spacing in the typography scale are proposed defaults; only the font-family names (Verlag, Open Sans) were observed in evidence.
- No hover, focus, active, error, or disabled states were observed; all interaction states in components are proposed.
- Mobile/tablet layout, menu collapse behavior, and breakpoint values were not observed and are recommendations only.
- Licensing and web-font availability for "Verlag" and "minion-pro" were not verified; generic sans-serif/serif fallbacks are assumed necessary.
