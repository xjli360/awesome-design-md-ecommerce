---
version: alpha
name: "Light in the Attic"
source_url: "https://www.lightintheattic.net"
captured_at: "2026-09-28T09:15:42.531924+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Light in the Attic's storefront runs on a Shopify theme with a neutral, editorial base: body text and headings resolve to a near-black ink (#231f20) on an off-white canvas (#fafafa), with white (#ffffff) reserved for cards and elevated surfaces. A saturated yellow (#ffd50d, with a near-duplicate #fbd10d) appears repeatedly in the palette and is treated here as the brand accent — inferred as the primary interactive/highlight color given its distinctiveness against an otherwise grayscale system of #eeeeee, #dddddd, #e5e5e5, and #999999 tones used for muted text, hairlines, and soft surfaces.

  Typography pairs a serif display face, century-old-style-std (falling back to Arial/serif), used only for h1/h2 at large, uppercase-capable sizes, with Jost (falling back to Arial/sans-serif) for h3–h6, body copy, and all form/button elements. This split is observed directly in the theme CSS. Button variants (.btn-black, .btn-white, .btn-plain) show a consistent transparent-background, bordered pattern rather than filled buttons, which this spec generalizes into primary/secondary button tokens. Numeric sizes for body text, spacing, and radii beyond what CSS exposed are proposed for a cohesive system, not measured.

colors:
  primary: "#ffd50d"
  ink: "#231f20"
  canvas: "#fafafa"
  body: "#231f20"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#231f20"
  accent-alt: "#fbd10d"
  tint-warm: "#fffceb"
  border-soft: "#e5e5e5"
  overlay-dark: "#000000bf"
  overlay-ink: "#231f20d4"
  disabled: "#aaaaaa"
typography:
  display-xl: {fontFamily: "century-old-style-std, Arial, serif", fontSize: "60px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0px"}
  display-md: {fontFamily: "century-old-style-std, Arial, serif", fontSize: "55px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "0px", textTransform: "uppercase"}
  title-md: {fontFamily: "Jost, Arial, sans-serif", fontSize: "24px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Jost, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Jost, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "Jost, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Jost, Arial, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "0.5px"}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-soft}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    overlayColor: "{colors.overlay-ink}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "{colors.overlay-dark}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "transparent"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    borderBottom: "1px solid {colors.surface-card}"
    padding: "{spacing.xs}"
  release-variant-tag:
    backgroundColor: "{colors.tint-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** is proposed as a solid yellow (#ffd50d) call-to-action for high-priority actions like "Add to Cart" or "Preorder," using dark ink text for contrast since no filled-button example was present in the extracted CSS — the observed .btn-black/.btn-white classes are transparent-with-border instead.

**button-secondary** generalizes the observed .btn-black/.btn-white pattern: transparent background with a 1px solid border, suited to secondary actions such as "View Product" or filter toggles. Hover/active states were not observed and are proposed only.

**text-input** is modeled loosely on the observed `form.search-form input[type=search]` (bottom-border only, transparent background, white text on dark contexts). The light-surface variant defined here is inferred for use in account/newsletter forms elsewhere on the site.

**nav-bar** reflects the site's evident navigation vocabulary (Just added, Preorders, Now shipping, Features, Merch, Sale, LITA Artists, Labels, Browse) sitting above a light canvas; exact height, sticky behavior, and mobile menu treatment are not observed.

**product-card** is inferred from the repeated "View Product" grid pattern in the page text (artist name, title, thumbnail). Card surface, border, and radius are proposed defaults consistent with the theme's otherwise minimal, edge-lit aesthetic.

**hero** represents the rotating feature banners referenced in the copy (e.g., "Grand Theft Auto VI," "A La Altura," "Faye Wong"). Layout, imagery, and overlay opacity are proposed; only the dark overlay tint (#231f20d4) is grounded in the observed palette.

**footer** uses the ink color as background with light text, inferred from the semi-transparent dark tokens (#000000bf, #231f206b) present in the palette, which suggest dark overlays/footers elsewhere in the theme. Link list mirrors the observed footer copy (Customer Service, Company, Follow Us).

**badge** and **release-variant-tag** address the record-label/shop-specific need to flag "LITA Exclusive," "Repress Alert," "Back in stock," and vinyl-color callouts (e.g., "Transparent Orange," "splatter vinyl") seen throughout the text. The warm tint (#fffceb) and primary yellow are used to differentiate promotional vs. informational tags; this pairing is a proposed convention.

**search** reflects the literal observed search-form styling (transparent field, white underline, white icon button) intended for use on dark headers; a light-mode counterpart is proposed but unobserved.

## Responsive Behavior

| Breakpoint | Width      | Notes (proposed) |
|---|---|---|
| mobile | 0–599px | Single-column product grid; nav collapses to a hamburger/off-canvas menu; touch targets ≥44px. |
| tablet | 600–1023px | 2-column product grid; search and filters may move into a drawer. |
| desktop | 1024–1439px | 3–4 column product grid; full horizontal nav visible. |
| wide | 1440px+ | Max-width content container with increased gutter (`{spacing.xxl}`). |

This table is a recommendation for implementation, not a measurement of the live site's actual breakpoints, grid counts, or collapse thresholds, none of which were present in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was limited to a static CSS/text snapshot; no rendered layout, hover/focus/active states, animations, or JavaScript-driven interactions (cart drawer, filter panel, search-as-you-type) were observed.
- Color-to-role mapping is inferred: the yellow (#ffd50d/#fbd10d) is assumed to be the brand accent based on its distinctiveness in an otherwise grayscale palette, but no button, link, or CTA rule in the supplied CSS explicitly assigns it that role.
- Body copy and UI font sizes (16px, 14px, 12px caption) are proposed defaults; only h1–h6 sizes and the 12px search-input font-size were directly observed.
- Spacing and radius scales are conventional proposals, not derived from measured margins/padding in the source CSS.
- Availability, licensing, and web-font loading status of `century-old-style-std` were not verified; it is used here strictly as an observed `font-family` declaration with system fallbacks.
- Mobile navigation structure, product-card imagery treatment, and footer column layout are inferred from page text/content order, not from actual DOM or viewport screenshots.
