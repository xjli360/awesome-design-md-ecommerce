---
version: alpha
name: "Wunderlang"
source_url: "https://wunderlang.com"
captured_at: "2026-09-29T04:00:26.642209+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wunderlang presents itself as a Squarespace-built storefront for a kids' denim,
  knitwear and jersey line, organized around a spaced-letter wordmark treatment
  ("D E N I M", "K N I T W E A R") and editorial lookbook sections. The observed
  palette is dominated by near-black and grey UI tones (#111111, #222222,
  #999999, #dddddd, #f6f6f6) typical of Squarespace's default chrome, alongside
  a small set of warmer, brand-distinct hues — a coral-red accent (#f0523d)
  drawn from an interactive hover state, a dusty clay tone (#cda99d), an olive
  green (#365313), a deep brown (#382110) and a warm off-white (#f5efec). These
  warmer tones are interpreted here as the brand's product/accent palette,
  suited to a natural-fiber, sustainability-forward kids clothing line, while
  the greys and near-blacks are treated as inferred UI/text infrastructure.
  Typography draws on the observed families: Clarkson for display headings
  (matching the letter-spaced, uppercase editorial style seen in copy), EB
  Garamond as a softer serif accent for titles, Karla for body copy, and
  Helvetica Neue for small interface text such as buttons and cookie notices,
  where exact sizes (12px, 15px) were directly observed. Layout patterns below
  are proposed conventions for a boutique kids apparel site, not measured
  observations.

colors:
  primary: "#f0523d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#f5efec"
  on-primary: "#ffffff"
  accent-clay: "#cda99d"
  accent-olive: "#365313"
  accent-brown: "#382110"
  accent-warm: "#eb4924"
typography:
  display-xl: {fontFamily: "Clarkson, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: 2px}
  display-md: {fontFamily: "Clarkson, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 1.5px}
  title-md: {fontFamily: "EB Garamond, serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "Karla, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Karla, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0.05em}
  button-md: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: normal, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    shadow: "none (flat editorial style, proposed)"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayColor: "{colors.accent-brown}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"
    hairline: "{colors.accent-brown}"
  badge:
    backgroundColor: "{colors.accent-clay}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fabric-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-olive}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** uses the coral-red accent (#f0523d) as a call-to-action fill, styled after the observed "SHOP NOW" and newsletter sign-up patterns; the uppercase, letter-spaced button typography is drawn directly from the newsletter-form-button CSS (15px, uppercase, centered). **button-secondary** is a proposed outlined/light variant for secondary actions such as "View fullsize" links in the lookbook grid, using surface-soft with a hairline border rather than a measured style. **text-input** is inferred for newsletter and account forms, using a plain bordered field consistent with the minimal, editorial aesthetic implied by the site copy; no live form styling was captured. **nav-bar** proposes a flat white header with uppercase nav labels ("SHOP", "WUNDERLANG", "JOURNAL"), matching the plain-text navigation structure visible in the page text, though exact spacing/height are not measured. **product-card** is a category-appropriate pattern for a denim/knitwear/jersey shop grid, pairing a warm card surface (#f5efec) with title and price typography; card imagery, hover states and grid spacing are proposed, not observed. **hero** models the "DENIM OF DREAMS" landing banner with large spaced display type over a full-bleed image area; overlay/scrim color is inferred from the darkest brand-adjacent tone (#382110) for text legibility, not confirmed from CSS. **footer** reflects the observed footer content structure (Info, Sustainability, Care Instructions, Social, copyright line) on a dark ink background with light text, a common Squarespace footer treatment though the specific background choice here is inferred. **badge** is proposed for callouts such as "New" or size labels, using the dusty clay accent for a soft, kidswear-appropriate tone. **search** is a minimal inferred pattern consistent with Squarespace's default search affordance; no distinct search UI was present in the supplied evidence. **fabric-tag** is a category-specific proposed component for surfacing material/care information (e.g. "Organic Denim", "Silk Blend"), directly motivated by the site's Sustainability, "Benefits of Silk," and Care Instructions footer links, using the olive accent to suggest a natural-materials focus.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Nav | Product Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger menu | 1 column |
| Tablet | 600–900px | Condensed horizontal nav | 2 columns |
| Desktop | 900–1280px | Full horizontal nav | 3 columns |
| Wide | >1280px | Full nav, wider gutters | 4 columns |

Touch targets for buttons and nav items should be at minimum 44×44px per common accessibility guidance. Below the tablet breakpoint, primary navigation is expected to collapse into a slide-out or overlay menu, and the footer link groups (Info, Social) should stack vertically. None of this responsive behavior was directly observed in the supplied CSS; it is proposed based on category norms for editorial e-commerce sites.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS declarations, page text, and a partial color/font inventory, not a rendered or interactive audit of wunderlang.com. Several limitations apply: (1) many supplied hex values belong to third-party social-icon brand colors (Facebook, Instagram, Pinterest, etc.) and were excluded from the brand palette, but the remaining "brand" hues (#f0523d, #cda99d, #365313, #382110, #eb4924, #f5efec) are inferred as product/accent colors rather than confirmed from a brand style guide. (2) Font role assignments (Clarkson for display, EB Garamond for titles, Karla for body) are inferred from typical usage patterns of these families in Squarespace templates, not confirmed from selector-level CSS mapping specific headings. (3) No hover, focus, active, or error states were observed beyond the cookie-banner reject/hover rules; all other interaction states are proposed. (4) No mobile or responsive layout was directly observed; the breakpoint table is a category-standard recommendation. (5) Component sizes, spacing values, and border-radii not explicitly present in the supplied CSS (e.g. product-card padding, hero padding) are proposed defaults for visual consistency, not measurements. (6) Availability and licensing of Clarkson and EB Garamond for reuse outside this site were not verified.
