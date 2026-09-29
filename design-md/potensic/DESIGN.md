---
version: alpha
name: "Potensic"
source_url: "https://potensic.com"
captured_at: "2026-09-28T04:25:50.506824+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The evidence reflects a Bootstrap-derived utility framework layered under a
  consumer-drone storefront, so the palette is broader than a single brand
  system: true UI colors sit alongside contextual accents (badge greens,
  warning ambers, danger reds) inherited from a shared component library.
  Within that set, #007bff reads as the most likely interactive/primary
  accent given its repeated use across .btn-primary, .btn-outline-primary,
  and link-adjacent states, while #212529 and #333333 anchor body text and
  #ffffff anchors the canvas. #f8f9fa, #f5f5f5, and #ededed are treated as
  layered neutral surfaces for cards and soft sections, and #dee2e6/#e1e1e1
  serve as hairline dividers. This interpretation proposes a clean,
  utility-grid commerce layout: bold hero imagery for drone products, card
  grids for model comparisons, and confidence-building CTAs in the primary
  blue. Typography relies solely on the observed system-font stack
  (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans,
  sans-serif) — no proprietary display face is confirmed. All sizing,
  spacing, and radius values beyond the literal Bootstrap tokens (0.25rem
  radius, 0.375rem/0.75rem button padding) are proposed, not measured.

colors:
  primary: "#007bff"
  primary-hover: "#0062cc"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dee2e6"
  divider-soft: "#e1e1e1"
  surface-soft: "#f8f9fa"
  surface-card: "#f5f5f5"
  surface-alt: "#ededed"
  on-primary: "#ffffff"
  success: "#28a745"
  warning: "#ffc107"
  danger: "#dc3545"
  info: "#17a2b8"
  secondary: "#6c757d"
  dark: "#343a40"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.divider-soft}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
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
  spec-table:
    backgroundColor: "{colors.canvas}"
    hairlineColor: "{colors.hairline}"
    headerBackgroundColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** — The main call-to-action style (e.g. "Buy Now," "Add to Cart"), using the observed `#007bff` fill with white text. Hover/active/disabled state colors are proposed, not confirmed in the supplied CSS.

**button-secondary** — An outline variant echoing `.btn-outline-primary`, used for secondary actions like "Learn More" or "Compare." Its transparent fill and blue border are directly observed; hover-fill behavior is proposed.

**text-input** — A generic form field (search, contact, newsletter signup) styled with a light hairline border and white background, inferred from Bootstrap form conventions rather than directly observed input CSS.

**nav-bar** — A top navigation bar on a white canvas with muted body-colored links, proposed as sticky or static; no scroll-state or mobile-menu behavior was present in the evidence.

**product-card** — A drone-model card using the soft `#f5f5f5` surface with a light `#e1e1e1` border, intended for grid listings on category or home pages. Image treatment and hover elevation are proposed.

**hero** — A full-width introductory banner on white canvas, pairing a large display headline with a primary button; imagery, video, or carousel behavior is not confirmed by the evidence and is proposed.

**footer** — A dark closing section (`#343a40`) with muted links, consistent with the dark/secondary tones in the observed button classes; multi-column layout is proposed, not measured.

**badge** — A small pill label (e.g. "New," "Best Seller") using the observed success green, sized for compact placement on product cards; color-coding by status (info/warning/danger) is proposed using other observed utility colors.

**search** — A lightweight search field using the soft neutral surface color, intended for header or support-page search; no evidence of a dedicated search-input class was found.

**spec-table** — A comparison table for drone specifications (weight, flight time, camera), using hairline row dividers and a light header background; row-striping and responsive collapse are proposed.

## Responsive Behavior
This is a proposed breakpoint recommendation, not a measured observation of the live site's responsive CSS.

| Breakpoint | Width | Layout guidance |
|---|---|---|
| xs | <576px | Single-column stacks; nav collapses to a hamburger/drawer (proposed) |
| sm | ≥576px | 2-column product grids; larger touch targets (44px min) |
| md | ≥768px | 2–3 column grids; inline nav begins to expand |
| lg | ≥992px | Full horizontal nav; 3–4 column product/spec grids |
| xl | ≥1200px | Max-width container (~1140–1320px), generous section padding |

Touch targets should be at least 44×44px for buttons and nav items on small screens. Collapse the navigation into a drawer or accordion below `md`, and stack spec-table columns into label/value pairs below `sm`. None of this reflects confirmed media queries from the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
The supplied evidence is a static CSS/color extraction from a Bootstrap-based utility layer, not a rendered capture of Potensic's actual marketing pages — no hero, product-grid, or footer markup was directly observed. Semantic role assignments (primary accent, surface layering, hairline vs. divider) are inferred from class-name conventions (`.btn-primary`, `.btn-light`, etc.) rather than confirmed brand usage. All typography sizes, weights, letter-spacing, and line-heights beyond the base `body` rule (`font-size:1rem; line-height:1.5; color:#212529`) are proposed defaults. No custom or licensed display font was found in the evidence; only the system-font stack is confirmed, and its licensing is inherently system-level (no verification needed). Responsive breakpoints, mobile navigation behavior, hover/focus/active states, and any interaction patterns are proposed and not measured from live site behavior.
