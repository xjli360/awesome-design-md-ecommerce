---
version: alpha
name: "Mystery Ranch"
source_url: "https://mysteryranch.com"
captured_at: "2026-09-29T04:22:05.999610+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Mystery Ranch is a mission-driven outdoor and tactical backpack brand, and the observed CSS reflects a utilitarian, function-first storefront built on Bootstrap-derived components (table, btn, facets classes) rather than a bespoke design system. The evidence surfaces a neutral grayscale base (#ffffff, #f5f5f5, #333333, #6d6e71, #231f20) paired with a single warm accent, #ea7600, which is inferred as the primary brand/CTA color given its saturation contrast against the otherwise desaturated palette; #c6690a is treated as a hover/pressed variant of that accent. Supporting state colors (#dff0d8, #f2dede, #fcf8e3, #d9edf7) are standard Bootstrap alert/table tints, inferred as reused for inventory or form-validation feedback rather than brand expression. Typography centers on "Industry" for display/headline treatment (confirmed only on a jumbotron subheader selector) with "Open Sans"/Helvetica Neue/Arial as the body and fallback stack, consistent with a rugged, condensed-display + clean-sans-body pairing common to outdoor gear retailers. Layout, spacing, radii, and component states below are proposed conventions sized for a product-catalog experience (facets, filters, product cards, hero banners) and are not measured from live rendering; they extrapolate reasonable defaults from the class names and color tokens present in the evidence.

colors:
  primary: "#ea7600"
  primary-hover: "#c6690a"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6d6e71"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  border-default: "#cccccc"
  danger: "#c01a29"
  success-tint: "#dff0d8"
  danger-tint: "#f2dede"
  info-tint: "#d9edf7"
  warning-tint: "#fcf8e3"
typography:
  display-xl: {fontFamily: "'Industry', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Industry', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.border-default}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-default}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairline: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-default}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  filter-panel:
    backgroundColor: "{colors.surface-soft}"
    hairline: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    padding: "{spacing.base}"
    rounded: "{rounded.xs}"

## Components
**button-primary** is proposed as the orange (#ea7600) filled call-to-action used for "Shop Now," "Subscribe," and add-to-cart actions, with a darker (#c6690a) hover state inferred from the accent pair present in the palette; states beyond default/hover are proposed, not observed.

**button-secondary** is a white/bordered outline button using the observed `.btn-default` pattern (`color:#333;background:#fff;border-color:#ccc`), suited to secondary actions like "Learn More" alongside a primary CTA.

**text-input** covers search fields and form inputs (e.g., newsletter signup); border and sizing are proposed defaults since no explicit input CSS was supplied beyond generic `font:inherit` resets.

**nav-bar** represents the mega-menu structure implied by the extensive "Shop / Military / Fire / Hunting / Everyday Carry" navigation text; a white background with dark ink text is inferred from the base palette, as no nav-specific background color was captured.

**product-card** models catalog tiles (e.g., "Treehouse 38 $325.00") using a light card surface, hairline border, and title/price type pairing; card elevation/shadow is not observed and is omitted.

**hero** represents the homepage jumbotron ("WHITETAIL PACKS DESIGNED FOR PREPARATION") using a dark ink background with reversed white type, consistent with the `.jumbotron-subheader` selector using the Industry display font; exact hero imagery/overlay is not observed.

**footer** consolidates the extensive footer link groups (Contact, Legal, Social, Newsletter) into a dark ink band with light text, mirroring the hero's inverted treatment for visual bookending; this pairing is inferred, not confirmed via footer-specific CSS.

**badge** is a proposed small pill for "New" or sale flags (e.g., "New Assault," "New Hotshots/Handcrew" labels in nav), using the observed danger red (#c01a29) as a plausible flag color, though no badge-specific selector was supplied.

**filter-panel** is a category-appropriate component for the product-listing facet sidebar implied by `.facets-facet-list-filters-see-more-less` classes, styled with a soft gray surface and hairline dividers consistent with the observed Bootstrap table/panel tokens.

## Responsive Behavior
The following breakpoints are a **recommendation**, not measured site behavior, sized for a typical catalog/e-commerce layout:

| Breakpoint | Range | Layout guidance |
|---|---|---|
| Mobile | <576px | Single-column stack, nav collapses to hamburger, filter-panel becomes a drawer/modal |
| Tablet | 576–991px | 2-column product grid, condensed nav-bar |
| Desktop | 992–1279px | 3–4 column product grid, full mega-menu nav |
| Wide | ≥1280px | 4+ column grid, max-width container with generous section spacing |

Touch targets should be a minimum 44×44px for buttons and nav items; the mega-menu should collapse into an accordion on mobile with facet filters accessible via a slide-in panel. None of this responsive behavior was observed directly.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text evidence only; no rendered layout, computed styles, or DOM screenshots were available. Color **role assignments** (primary, ink, muted, hairline, etc.) are inferred from raw hex values and Bootstrap-class conventions, not confirmed brand guidelines — the true brand primary could differ from #ea7600. Typography sizes, weights, and letter-spacing beyond the single confirmed `.jumbotron-subheader` rule are proposed, not measured. "Industry" is a licensed commercial font; its availability, hosting method, and licensing on the live site were not verified. All component states (hover, focus, active, disabled) beyond the one captured `.btn-default:hover` rule are proposed patterns. Mobile navigation collapse, filter-drawer interaction, and actual cart/search UI behavior were not observed and are extrapolated from menu text content alone. Spacing and rounded-corner scales are conventional defaults, not extracted from the supplied CSS.
