---
version: alpha
name: "Luli & Me"
source_url: "https://lulime.com"
captured_at: "2026-09-29T04:35:15.918263+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from the current lulime.com storefront, a WordPress/Elementor
  site presenting Luli & Me's heirloom-quality smocked children's dresses, with purchasing
  routed to Amazon. The observed CSS shows a deliberate brand palette of warm, heritage browns
  (#5C3A21 button fill, #2C1810 heading ink) paired with a clean white canvas, evoking the
  brand's "southern heirloom" positioning rather than the loud accent colors present in the
  broader supplied palette (which include many WordPress default block-editor swatches such as
  #cc3366, #fcb900, #0693e3 — these are treated as available-but-unused editor colors, not core
  brand identity, and are excluded from primary roles unless reused for accents).
  Typography pairs "Playfair Display" for display/heading roles (h1 observed at 40px/700/
  letter-spacing -0.3px) with "Source Sans 3" for buttons and UI text (16px/600, uppercase,
  0.5px tracking), and a system sans-serif stack for base body copy. Buttons use an 8px rounded
  corner and solid fill, consistent with a soft, boutique-catalog feel. Roles for muted text,
  hairlines, and soft surface tones are inferred from neutral grays present in the palette
  (#eeeeee, #cccccc, #666666) since no dedicated muted/border CSS was supplied. Card and section
  spacing follow the theme's declared 24px block-gap, extended here into a full spacing scale
  for consistency.

colors:
  primary: "#5C3A21"
  ink: "#2C1810"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#cccccc"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#cc3366"
  accent-terracotta: "#c77a2a"
  heading-alt: "#3d2b1f"
  footer-dark: "#32373c"
typography:
  display-xl: {fontFamily: "\"Playfair Display\", sans-serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.3px}
  display-md: {fontFamily: "\"Playfair Display\", sans-serif", fontSize: 30px, fontWeight: 700, lineHeight: 1.25, letterSpacing: -0.2px}
  title-md: {fontFamily: "\"Playfair Display\", sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "\"Source Sans 3\", sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"Source Sans 3\", sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.5px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
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
  buy-on-amazon-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
    borderColor: "{colors.primary}"

## Components

**button-primary**: The dominant CTA style observed in the Elementor kit CSS (`#5C3A21` fill, white text, 8px radius, uppercase Source Sans 3). Used for primary actions like collection links.

**button-secondary**: Proposed outline variant using the same brown as border/text on a transparent background, for lower-emphasis actions like "View Collection" links; not directly observed but consistent with the reset.css button pattern (`border:1px solid #c36`).

**text-input**: Proposed form field styling for the search field mentioned in nav text ("Search"). No dedicated input CSS was supplied, so padding and radius are inferred defaults consistent with the button radius scale.

**nav-bar**: Proposed minimal top navigation using canvas background and ink text, reflecting the simple "Dresses / Search" navigation implied by page text; no header CSS was supplied.

**product-card**: Proposed card pattern for the many individual dress listings (e.g., "Honeycomb Smocked Lavender Bishop Sleeve Dress") described in the page excerpt, using Playfair Display for the product title and body-sm for descriptive copy, matching the catalog-style repetition of "New Arrival" items.

**hero**: Proposed hero treatment for the homepage introduction ("Luli & Me: Timeless Heirloom Dresses…") using the display-xl heading style observed in the h1 CSS rule, on a soft neutral background to separate it from the white body canvas.

**footer**: Proposed dark footer using `#32373c`, the only dark neutral present in the supplied button/background CSS (`--wp--element-button` background), for contrast against the light body.

**badge**: Proposed "New Arrival" label component, styled with the rose accent color present in the palette, since the page text repeatedly flags items as "New Arrival" but no badge CSS was supplied.

**search**: Proposed pill-shaped search affordance referenced by the "Search" nav item; shape and color are inferred, not measured.

**buy-on-amazon-cta**: A category-specific component reflecting the site's actual commerce pattern — every product links out via a "Buy On Amazon" button rather than an on-site cart, styled identically to button-primary per the observed Elementor button CSS.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤600px (single-column product list, stacked hero, nav collapsed to a menu icon), tablet 601–1024px (2-column product grid, inline nav), desktop >1024px (3–4 column grid, content max-width per `--wp--style--global--content-size: 800px` / `--wp--style--global--wide-size: 1200px` tokens observed in the theme root). Touch targets for buttons and the Buy-on-Amazon CTA should maintain a minimum 44px height. This table is a recommendation derived from standard WordPress/Elementor conventions and the observed content-width tokens, not from captured live responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered layout, hover state, animation, or actual breakpoint behavior was observed. Header/navigation, form/input, and footer markup were not present in the supplied CSS, so those components are proposed patterns rather than confirmed styles. The large supplied color list includes many default WordPress block-editor palette swatches (e.g., `#fcb900`, `#0693e3`, `#9b51e0`) whose actual on-site usage is unconfirmed; only colors with clear CSS rule attribution (`#5C3A21`, `#2C1810`, `#32373c`, `#ffffff`, `#333333`) are treated as core brand colors, with others offered as possible accents. Font availability, licensing, and self-hosting status for "Playfair Display" and "Source Sans 3" were not verified beyond their appearance in `font-family` declarations. All pixel sizes outside the one observed h1 rule (40px/700/-0.3px) are proposed, not measured.
