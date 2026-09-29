---
version: alpha
name: "Kaba Baby"
source_url: "https://kabababy.com"
captured_at: "2026-09-28T10:16:01.805528+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Kaba Baby's evidence set centers on a burnt-orange primary (#f3761f) set against
  a deep navy ink (#1a2238) and a white canvas, a pairing confirmed directly in the
  theme's heading rule (h1-h5 render in #f3761f) and in body/button copy (#1a2238 on
  #fff). A cream surface (#f9f1e1) is used as the literal background for the promo
  bar and popup button text, giving a soft, nursery-adjacent counterpoint to the
  citrus primary; a related blush tone (#fdf1e8) is treated here as an inferred
  card surface for product tiles. Headings use Libre Baskerville, a serif observed
  directly on h1-h5 selectors; body copy, inputs, and buttons use the system UI
  stack (system_ui, -apple-system, Segoe UI, Roboto, etc.) at a compact 13px base
  with 1.6 line-height, and buttons render uppercase at roughly 11px/600 weight per
  the .button.solid/.outline rules. Several additional font names appear in the
  raw evidence (Jost, Averia Serif Libre, Baskerville, La Belle Aurore,
  BlackSingature) but no selector in the supplied CSS assigns them a role, so they
  are excluded from typography tokens and flagged in Known Gaps. Neutral grays
  (#5e6473, #d1d2d7) are inferred as muted-text and hairline roles from their tonal
  position in the swatch list, not from confirmed selectors. Rounded and spacing
  scales are proposed conventions, anchored only loosely to the 16px chat-widget
  radius present in :root variables.

colors:
  primary: "#f3761f"
  ink: "#1a2238"
  canvas: "#ffffff"
  body: "#1a2238"
  muted: "#5e6473"
  hairline: "#d1d2d7"
  surface-soft: "#f9f1e1"
  surface-card: "#fdf1e8"
  on-primary: "#ffffff"
  accent-gold: "#f1b324"
  surface-warm: "#fce3d2"
  highlight: "#f4db7d"
typography:
  display-xl: {fontFamily: "'Libre Baskerville', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  display-md: {fontFamily: "'Libre Baskerville', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  title-md: {fontFamily: "'Libre Baskerville', serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif", fontSize: 11px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    padding: "{spacing.xs} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    headingColor: "{colors.primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  print-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.md}"

## Components
**button-primary** reflects the directly observed `.button.solid` rule: a solid `#f3761f` fill with white uppercase text and no visible border-radius specified, here mapped to a small `rounded.sm` for consistency with the outline variant.

**button-secondary** mirrors the observed `.button.outline` pattern — a 2px ink-colored border with matching text, transitioning to primary-colored border/text on hover, a state confirmed in the theme CSS.

**text-input** has no directly observed styling in the supplied evidence; its canvas background, hairline border, and body typography are proposed defaults consistent with the surrounding system-font UI.

**nav-bar** is inferred from header/promo-bar context; the promo bar itself is directly observed to pair a cream background (`#f9f1e1`) with primary-colored text and links, a distinct sub-pattern worth preserving in any header implementation.

**product-card** is proposed for the "BEST SELLERS" grid referenced in page text (e.g., "Zip-Up Sleep & Play One-Piece — $19.99"); surface-card and muted price coloring are inferred, not measured from card-specific selectors.

**hero** uses the confirmed heading color/typeface pairing (Libre Baskerville, `#f3761f`) over a white canvas; padding and layout proportions are proposed since no hero-specific box model was in the extracted CSS.

**footer** is proposed from the sitemap text (About, Customer care, social links) with muted body copy and primary-colored links for consistency with global link treatment; no footer-specific selectors were supplied.

**badge** models the "GOTS Certified" / "20% OFF" promotional language using the confirmed cream-on-orange color relationship from the promo bar, applied at small pill scale — a proposed reuse of an observed color pairing.

**search** is a proposed minimal input treatment; the evidence only confirms a "Search" menu entry exists, not its visual styling.

**print-tag** is a category-appropriate proposed component for surfacing named prints ("Magnetic Tennis Queen," "Choo Choo Train," "GIFY," "Green Is For Go") mentioned under "Shop by Print," using a warm blush surface to differentiate print collections from standard product tags.

## Responsive Behavior
This is a recommended structure, not measured site behavior — no breakpoint or device-specific CSS was present in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| sm | 0–599px | Single-column product grid, collapsed hamburger nav |
| md | 600–899px | 2-column product grid, promo bar remains full-width |
| lg | 900–1199px | 3-column product grid, inline nav links |
| xl | 1200px+ | 4-column product grid, max-width container |

Touch targets should be at least 44×44px for nav, cart, and button elements regardless of the compact 11–13px type scale observed in desktop CSS. Primary navigation is assumed to collapse into a disclosure/hamburger pattern below `md`, consistent with the `.disclosure__toggle` selector present in the theme but whose open/closed visual states were not included in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
The supplied evidence is a static, partial extraction of selectors and computed values, not a rendered-page audit — no layout grid, spacing rhythm, or component geometry beyond the listed rules was observed. Several font names (Jost, Averia Serif Libre, Baskerville, La Belle Aurore, BlackSingature) appear in the raw font list but are not tied to any supplied selector, so they are omitted from typography tokens; their licensing and actual usage on the live site are unverified. Neutral roles (`muted`, `hairline`, `surface-card`, `surface-warm`, `highlight`) are inferred from swatch tone/position rather than confirmed selector context, since the palette array does not label roles. All font sizes beyond the directly observed `13px` body and `.6875em` button rules are proposed estimates for hierarchy purposes. The `rounded` scale is proposed; the only radius value in evidence (`16px`, from the Shopify chat widget `:root` variable) is not confirmed to apply to buttons, cards, or inputs. No hover/focus/active states were observed beyond the documented `:focus` outline (`#f3761f`, 5px) and the `.button.outline`/`.button.simple` hover color swap. Mobile menu behavior, cart drawer interaction, and any JavaScript-driven states were not present in the supplied static evidence and are not claimed here.
