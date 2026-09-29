---
version: alpha
name: "Bloom Baby"
source_url: "https://bloombaby.com"
captured_at: "2026-09-28T09:57:32.591370+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Bloom Baby's site evidence centers on a warm coral-orange accent (#f4633a) set
  against a strict black-and-white foundation (#000000 / #ffffff), consistent
  with the "design-forward parents" positioning stated in the page copy. The
  orange appears repeatedly in interactive states (button background, active
  border, hover shift to #d75733), so it is treated here as the primary
  action color, with white or black text chosen per context and labeled
  inferred where contrast was not directly measured. Supporting neutrals
  (#5c6077 slate, #e5e5eb hairline, #f9f5f2 and #fafafa soft off-whites) read
  as secondary text and card/section backgrounds; this role assignment is
  inferred from common usage patterns (e.g. #5c6077 appearing on a byline
  span) rather than confirmed page-wide. A muted navy (#1f2d5d) and a warm tan
  (#f1bd83) are carried forward as optional accent colors, since many other
  supplied hexes (wood tones, pink, teal, yellow) appear tied to individual
  product-color swatches (Fresco Noir, Coco Cappuccino, etc.) rather than
  core brand identity, and are excluded from primary tokens. Typography is
  built entirely from the observed Poppins family (regular/medium/semibold/
  bold classnames) with sans-serif fallback; no other brand font was found.
  All sizes, weights beyond family, and spacing/radius values are proposed
  unless a CSS rule explicitly stated them (e.g. 4px button radius, 14px
  base text).

colors:
  primary: "#f4633a"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#5c6077"
  hairline: "#e5e5eb"
  surface-soft: "#f9f5f2"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-navy: "#1f2d5d"
  accent-tan: "#f1bd83"
  success: "#009900"
  warning: "#ff9901"
  error: "#e43c0d"
typography:
  display-xl: {fontFamily: "poppins-bold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "poppins-semibold, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "poppins-semibold, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "poppins-regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "poppins-regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "poppins-medium, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "poppins-medium, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch:
    shape: "circle"
    size: "32px"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    gap: "{spacing.sm}"

## Components
**button-primary** carries the observed coral-orange active/background token and is used for primary conversion actions ("shop now", "checkout"); white text is proposed for contrast since the underlying widget default (black) is a third-party review-tool value, not a site-wide button rule.

**button-secondary** is a bordered, white-fill variant proposed for lower-emphasis actions ("learn more", filters); it reuses the hairline color for its border to stay visually quiet next to the primary orange.

**text-input** is proposed for search, email capture, and account/login fields, using the hairline border and muted placeholder color observed elsewhere in the site's neutral palette.

**nav-bar** reflects the dark-header/light-header text-color swap found in the CSS (`.dark-header a { color:#000 }` vs `.light-header a { color:#fff }`), implying the nav sits on variable hero backgrounds; exact height and collapse behavior are not observed.

**product-card** is proposed for highchair, crib, and bouncer listings (Fresco, Coco, Alma Mini, Retro Crib), using the soft off-white surface and a hairline border to separate cards on a light canvas, with price/title typography drawn from the type scale.

**hero** is proposed for the homepage banner ("begin life in style") using the soft cream surface and largest display type; no imagery or overlay treatment was present in the supplied CSS.

**footer** is proposed as a dark, ink-background block for the many listed footer links (Warranty, Returns, FAQs, Affiliate Program), inverting text to white/canvas for contrast.

**badge** covers small status labels such as "new!" or "Sale," using the primary orange fill and pill radius; exact usage/placement is inferred from copy mentions, not a rendered screenshot.

**search** is proposed for the header search affordance ("Search" in nav text), styled as a soft, bordered field consistent with the neutral surface palette.

**color-swatch** is a category-specific pattern proposed for the many product color/finish variants called out in the text (Fresco White/Noir/Silver/Rose Gold, Coco Natural Wood/Cappuccino, Beach House White); a circular swatch with a primary-colored selected ring is a common e-commerce pattern for this content, not a confirmed layout.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior (no responsive CSS was included in the supplied evidence):

| Breakpoint | Range | Nav | Product grid |
|---|---|---|---|
| Mobile | < 640px | Collapsed hamburger menu | 1 column |
| Tablet | 641–1024px | Condensed inline nav or hamburger | 2 columns |
| Desktop | > 1024px | Full horizontal nav | 3–4 columns |

Touch targets are recommended at a minimum 44×44px for buttons, color swatches, and nav links. The nav bar should collapse to a hamburger/off-canvas pattern below tablet width, and the color-swatch component should wrap to a horizontal scroll or multi-row layout on narrow viewports. None of this reflects observed DOM/media-query behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered screenshots, computed layout, or interaction states (hover/focus/active beyond the `:root` review-widget variables) were observed.
- Many supplied hex values (wood tones, pink #f8a8c9, yellow #f8ef22, teal #05aeb6) appear tied to individual product color-variant swatches rather than core brand tokens, and were deliberately excluded from the primary color set; this categorization is an inference.
- Role assignment for `body`, `muted`, `surface-soft`, and `surface-card` is inferred from limited context (a single byline-color rule and generic neutral hexes), not confirmed page-wide usage.
- All typographic sizes, weights (beyond the Poppins family name itself), letter-spacing, and line-heights are proposed; only the 14px `--oke-text-regular` value and 4px button-radius were directly observed in CSS.
- Spacing scale, component padding, breakpoints, and touch-target sizes are proposed conventions, not measured from the live site.
- Mobile/tablet navigation collapse, product-grid column counts, and hero layout are not observed and are marked as recommendations only.
- Poppins font availability, weight variants, and licensing for production use were not verified from the supplied evidence.
