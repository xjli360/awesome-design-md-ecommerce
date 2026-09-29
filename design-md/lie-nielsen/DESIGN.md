---
version: alpha
name: "Lie-Nielsen"
source_url: "https://www.lie-nielsen.com"
captured_at: "2026-09-29T04:18:21.430198+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lie-Nielsen Toolworks is a Maine-based maker of premium hand tools —
  planes, saws, chisels, and sharpening equipment — sold through a
  Bootstrap-based storefront (Fulfil.io commerce, cloud-hosted assets).
  The observed CSS surfaces a neutral gray/white UI shell typical of
  Bootstrap defaults (#ffffff, #f5f5f5, #dddddd, #333333, #777777) plus
  a warm accent pair used consistently on interactive chat/CTA controls:
  a burnt-orange (#e15c20) and a brass-gold (#e7b41d), with a darker
  orange (#9d4015) for hover/focus states. Because the supplied evidence
  is dominated by the third-party Olark chat widget's theme and Bootstrap
  utility classes, semantic roles for primary text, card surfaces, and
  hairlines below are inferred from conventional dark-gray-on-white
  patterns (#333333 ink, #555555 body, #777777 muted, #dddddd/#cccccc
  hairlines) rather than confirmed page-chrome selectors.
  Typography draws on the loaded font stack: Lora (serif) is proposed
  for display/heading roles to reflect a craftsman, catalog-print
  sensibility appropriate to fine hand tools, while Open Sans/Helvetica/
  Arial sans-serif carries body and UI text, matching the Bootstrap
  system-font fallback chain actually present in the CSS. No live
  layout, breakpoints, or interaction states were observed; all sizing
  and spacing values are proposed conventions layered onto the
  confirmed color and font evidence.

colors:
  primary: "#e15c20"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#555555"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#edeeef"
  on-primary: "#ffffff"
  accent-gold: "#e7b41d"
  accent-dark: "#9d4015"
  border-strong: "#cccccc"
  heading: "#2d2d2d"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lora, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Open Sans', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  category-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.heading}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.heading}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** uses the confirmed burnt-orange (#e15c20) with white text, matching the Olark widget's action buttons; this is the strongest direct color-to-role evidence in the source data.

**button-secondary** is a proposed outline variant reusing the primary orange for border/text on a transparent field, giving a lighter-weight action for secondary flows like "Add to Wishlist" — not observed directly.

**text-input** is inferred from Bootstrap's default form reset (`font:inherit;color:inherit`) and standard hairline borders; padding and radius are proposed conventions, not measured.

**nav-bar** represents the top-level bar implied by the deep textual navigation (Hand Tools, Sharpening, Education, Events, Information); no header CSS was supplied, so background/spacing are inferred defaults.

**category-mega-menu** is a category-appropriate component reflecting the site's multi-level tool taxonomy (Handplanes → Bench Planes → Standard/Low Angle/High Angle Frogs, etc.); presented as a proposed flyout/panel pattern since no menu-specific selectors were in evidence.

**product-card** is proposed to house individual tool listings (e.g., a Bevel Edge Chisel or Dovetail Saw), using the near-white surface-card tone and hairline border for subtle separation on a white canvas.

**hero** proposes a light, soft-gray banner area for homepage or category introductions, using the serif display type to signal the brand's craftsman positioning; no hero markup was in the supplied CSS.

**footer** is inferred as a dark band (reusing the near-black heading color) carrying copyright, social links (Instagram/YouTube), and "Powered by Fulfil.io" text seen in the page excerpt.

**badge** reuses the brass-gold accent for small status labels (e.g., "New" or "Made in USA"), pairing with dark ink text for contrast; this pairing is proposed, not confirmed by a badge selector.

**search** is inferred from the visible "Search / Search" prompt in page text; styled as a bordered field consistent with the neutral input treatment used elsewhere.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Layout guidance                                  |
|-----------|------------|---------------------------------------------------|
| xs        | <576px     | Single-column stack; nav collapses to hamburger    |
| sm        | 576–767px  | 2-column product grids; mega-menu becomes accordion|
| md        | 768–991px  | 3-column product grids; inline top nav             |
| lg        | 992–1199px | Full mega-menu on hover; 4-column grids            |
| xl        | ≥1200px    | Max-width container; generous section spacing      |

Touch targets should be at least 44×44px for cart, search, and nav-menu triggers. The category mega-menu is proposed to collapse into a tap-to-expand accordion below `md`. None of this reflow behavior was observed in the supplied static CSS/HTML; it is a conventional proposal for an e-commerce catalog of this depth.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

The supplied evidence is dominated by the third-party Olark chat widget theme and generic Bootstrap resets, not first-party page-chrome selectors (header, footer, product grid, cards). Consequently, role assignments for ink, body, muted, hairline, and surface tones are inferred from conventional dark-gray-on-white UI patterns rather than confirmed selectors. Font-role mapping (Lora for display, Open Sans for body) is inferred from the loaded font list only; no heading/body selector paired a font-family with an element. All font sizes, line-heights, letter-spacing, spacing scale, and radius values are proposed design conventions, not measured from the live site. No interaction states (hover, focus, active) besides the Olark widget's orange hover/focus were observed. No mobile/responsive layout, grid structure, or breakpoint behavior was present in the supplied CSS. Licensing and self-hosting terms for Lora and Open Sans were not verified from this evidence and should be confirmed independently before implementation.
