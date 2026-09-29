---
version: alpha
name: "State Bags"
source_url: "https://statebags.com"
captured_at: "2026-09-28T09:48:36.989860+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  STATE Bags' storefront evidence surfaces a broad Shopify color palette used
  across product-swatch and promotional CSS rather than a documented brand
  system, so this interpretation treats a subset as the working UI palette
  and labels the rest as decorative/product-swatch only. Deep forest green
  (#197f66) is read as the primary brand accent given its repeated presence
  outside swatch rules; near-black (#000000) and near-white (#fffefa/#ffffff)
  anchor ink and canvas, consistent with the hero button's black border on a
  warm off-white fill. A warm cream (#f9f7ec) and light gray (#eeeeee) are
  proposed as soft surface tones for cards and section backgrounds, both
  drawn from the observed set. Hairlines use a light gray (#dedede) already
  present in the palette.

  Typography evidence is limited: the only font-family captured in the CSS
  is "JudgemeStar," which by name and context is almost certainly an icon
  glyph font shipped by the Judge.me reviews widget, not a brand text
  typeface. No heading, body, or button font was observed. To comply with
  "observed families only," JudgateStar is referenced in the stack for
  traceability, but paired with system sans-serif fallbacks for actual
  rendering guidance, and this limitation is called out explicitly below.
  All font sizes, weights, and spacing/rounding scales are proposed
  conventions for a bag/backpack e-commerce UI, not measured values.

colors:
  primary: "#197f66"
  ink: "#000000"
  canvas: "#fffefa"
  body: "#121212"
  muted: "#737373"
  hairline: "#dedede"
  surface-soft: "#f9f7ec"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-gold: "#e3c10d"
  accent-purple: "#403f6f"
  accent-blue: "#4e9fe3"
  accent-pink: "#f8bed6"
  success: "#00ad00"
  focus-ring: "#1f75fe"
  border-strong: "#c0c0c0"
typography:
  display-xl: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "JudgemeStar, system-ui, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.02em}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** uses the observed forest-green (#197f66) as a fill with white text, proposed as the primary add-to-cart/CTA treatment; sharp-to-slightly-rounded corners (4px) align with the hero button's minimal, squared border style seen in CSS (`border-color:#000000`). **button-secondary** mirrors the hero carousel's captured `.btn` rule directly: off-white fill (#fffefa), black border, black text — this is the one button style with direct CSS evidence. **text-input** is a proposed neutral field using canvas background and a light hairline border for forms like newsletter signup or search. **nav-bar** is inferred from `.header-outer` variables (logo width, uppercase link transform, letter-spacing tokens) indicating a horizontal top navigation with uppercase links; exact colors were not captured, so canvas/ink are proposed. **product-card** is sized for the bundle/product grid described in page text (e.g., "Kane Bundle," "Sleepover Bundle") with a light gray surface and soft rounding, proposed since no card CSS was supplied. **hero** reflects the observed hero carousel section with a warm cream background and bold display type for campaign messaging like "Live Life With Open Hands." **footer** is proposed as a dark, high-contrast band using body/ink as background, common for utility links and donation-program messaging referenced in the text ("we donate a percentage of the proceeds"). **badge** uses the observed gold swatch color (#e3c10d) as a small pill for labels such as "Bundle and Save 15%" or "New Arrivals," proposed placement and shape. **search** is a proposed pill-shaped input matching the site's "Search / Submit" utility affordance mentioned in navigation text. **color-swatch-selector** is a category-specific component modeled directly on the many `.product-swatch label.color-*` rules observed (e.g., color-olive, color-burgundy, color-sand), rendered as small circular selectors using product-surface and border-strong tones since individual swatch hex values in the evidence were flattened to a single gold placeholder.

## Responsive Behavior
Recommended, not measured: mobile <640px collapses nav-bar into a hamburger/off-canvas menu, single-column product-card grid, and stacked hero text over image. Tablet 640–1024px moves to a 2-column product grid with nav links visible but condensed. Desktop >1024px uses the full multi-column grid and horizontal nav implied by `--header-logo-width` and `--header-links-margin-horizontal` tokens. Touch targets for button-primary/secondary and color-swatch-selector should maintain a minimum 44px hit area regardless of visual padding. All breakpoint values are proposed conventions, not extracted from responsive CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed. The single captured font-family, "JudgemeStar," is almost certainly a Judge.me review-widget icon font rather than a brand text typeface, so all typography entries fall back to system sans-serif for practical rendering while retaining the observed name for traceability — real brand fonts (headings, body) were not present in the supplied evidence and must be verified against the live site or theme files. Font licensing/availability for any eventual real typeface is unverified. Numeric type scale, spacing scale, and rounding tokens are proposed design conventions, not measured values. Color-role assignments (primary, muted, hairline, surfaces) are inferred from a large undifferentiated palette dominated by per-SKU swatch colors; several palette entries (e.g., #833ab4, #fd1d1d, #fcb045 — an Instagram-gradient-like set) were excluded as likely third-party social icon colors rather than brand colors. Component definitions (nav-bar, product-card, footer, search, hero) beyond the one directly observed `.btn` rule are proposed patterns suited to a bags/backpack storefront and should be validated against actual rendered pages before implementation.
