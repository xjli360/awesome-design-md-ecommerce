---
version: alpha
name: "Ultrahuman"
source_url: "https://ultrahuman.com"
captured_at: "2026-09-28T10:00:08.651455+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Ultrahuman's evidence shows a black-and-white foundation with a saturated
  blue (#112baf) reserved for primary calls to action, layered over a system
  of black- and white-alpha overlays (#0000001a, #00000099, #ffffff1a, etc.)
  used for hairlines, disabled states, and translucent panels. Soft
  near-white surfaces (#f5f5f5, #fafafa, #f0f0f0, #ededed, #eeeeee) suggest
  card and section backgrounds distinct from the pure white canvas. A small
  set of saturated accents (#7bd8db cyan, #0eff6e green, #0882ff/#3b82f6
  blues) appear in the palette and are inferred here as data-visualization
  or status-indicator colors befitting a biometrics product, though their
  exact usage was not confirmed in the supplied rules.

  Typography draws on the observed font stack: Graphik as the primary
  humanist sans for UI and body copy, Geist as a secondary interface
  typeface, spaceGrotesk for numeric emphasis, and dharma-gothic-e — a
  condensed display face — inferred as the headline/stat typeface fitting
  the large tracked-metric callouts ("128,205,702 nights tracked"). JetBrains
  Mono/SF Mono are treated as the monospace choice for technical readouts.
  Rounded and spacing scales are proposed conventions, not measured, sized
  to match the pill-shaped buttons (border-radius 50px/100px) seen in the
  CSS evidence.

colors:
  primary: "#112baf"
  accent-blue: "#1539f5"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000b3"
  muted: "#6b6b6b"
  hairline: "#0000001a"
  hairline-strong: "#00000033"
  surface-soft: "#f5f5f5"
  surface-card: "#f0f0f0"
  surface-alt: "#ededed"
  on-primary: "#ffffff"
  overlay-dark: "#00000080"
  overlay-light: "#ffffff80"
  data-cyan: "#7bd8db"
  data-green: "#0eff6e"
  data-blue-bright: "#0882ff"
  near-black: "#030509"
typography:
  display-xl: {fontFamily: "dharma-gothic-e, Arial Narrow, sans-serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -1px}
  display-md: {fontFamily: "graphikExtended, Graphik, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  title-md: {fontFamily: "graphik, Graphik, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.3px}
  body-md: {fontFamily: "graphik, Graphik, sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "graphik, Graphik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "geist, Geist, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "graphik, Graphik, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: -0.42px}
  stat-mono: {fontFamily: "JetBrains Mono, SF Mono, Consolas, monospace", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.overlay-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  metric-readout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.stat-mono}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed `.ctaButton.primary` pattern: solid `#112baf` fill, white text, fully rounded corners, and a backdrop blur noted in the source CSS (blur is proposed as a decorative treatment, not guaranteed cross-browser). Hover/active states are proposed since no hover CSS was supplied for this exact class.

**button-secondary** mirrors the observed `.secondaryButton` — transparent background, translucent white border (`#ffffff33`-class hairline), pill radius, intended for use on dark hero backgrounds. Hover border-brightening (`#ffffff8c`) was observed and is preserved as the proposed hover state.

**text-input** is a proposed component; no form-field CSS was present in evidence. It borrows the soft off-white surface and thin hairline border pattern seen elsewhere in the palette for consistency.

**nav-bar** is inferred from the presence of a "Logo" element and top-level menu labels (Ring, Advanced Markers, Performance Lab, Shop) in the page text; exact nav styling (sticky behavior, scroll transitions) was not observed in the CSS rules.

**product-card** is proposed for the Shop/Ring PRO listing grid implied by page text ("Shop all", "Ring PRO", "Ring AIR"); card surface and radius are inferred conventions, not measured from supplied selectors.

**hero** reflects the large marketing banners implied by copy ("Power Moves," "Category-Defining Battery Life"); dark background with oversized display type is a proposed interpretation consistent with the condensed display font family present in evidence.

**footer** is inferred from country/store listings in page text (London, Abu Dhabi, Gurgaon, etc.); near-black background and muted white text follow the observed alpha-white text tokens (`#ffffffbd`, `#ffffff66`).

**badge** covers small pill labels such as "New" or "M2 Live" implied in copy; styling borrows the observed `.disclaimerButton` pattern (black fill, white text, full radius).

**search** is a proposed component with no direct evidence; included for category completeness (e-commerce shop browsing) using the shared soft-surface and full-radius conventions.

**metric-readout** is a category-appropriate proposed component for displaying biometric stats (sleep score, glucose reading, battery days) referenced heavily in page text; it uses a monospace/stat typeface to visually differentiate numeric health data from prose, though no dedicated CSS selector for this pattern was supplied.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|------------|-------------|-------------------|
| xs         | <480px      | Single-column stack; nav collapses to hamburger/drawer |
| sm         | 480–767px   | Product cards stack 1-up; hero type scales to ~60% of display-xl |
| md         | 768–1023px  | 2-up product/metric grids; nav shows condensed inline links |
| lg         | 1024–1439px | Full desktop nav; 3–4 column shop grids |
| xl         | ≥1440px     | Max-width content container; generous section padding (`{spacing.section}`) |

Touch targets are recommended at a minimum 44×44px for buttons and nav items, consistent with the pill-button padding observed (`12px 24px`). Collapse of multi-item navigation into a drawer/menu below `md` is a proposed pattern; no mobile menu markup or media queries were present in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence consists of static CSS rules and page text only; no rendered screenshots, computed layout, or DOM structure were available, so all spacing/grid measurements beyond the literal CSS values are proposed.
- Semantic role mapping (which alpha-black/white tokens serve as "muted" vs "hairline" vs "disabled") is inferred from typical usage patterns, not confirmed by class names in all cases.
- Font availability, licensing, and exact weights for Graphik, Geist, dharma-gothic-e, and spaceGrotesk were not verified; these are treated as observed family names only, with generic fallbacks appended.
- No hover, focus, active, or error states were directly observed for most components (text-input, search, nav-bar); these are labeled proposed.
- Mobile/responsive DOM behavior, breakpoint values, and menu collapse logic were not observed in the supplied evidence and are offered only as design recommendations.
- Data-visualization accent colors (#7bd8db, #0eff6e, #0882ff family) appear in the raw palette but their functional assignment (status/positive/negative/chart series) could not be confirmed from the supplied selectors.
