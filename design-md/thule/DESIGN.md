---
version: alpha
name: "Thule"
source_url: "https://thule.com"
captured_at: "2026-09-28T09:57:29.549082+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from Bootstrap-derived utility CSS and a small
  set of Thule-specific neutral and muted-outdoor tones served from
  thule.com's production stylesheet. The observed palette mixes standard
  Bootstrap utility colors (#0d6efd primary, #198754 success, #dc3545/#af0a0a
  danger, #ffc107 warning) with a custom near-black text scale (#181818,
  #303030, #474747, #757575) and a set of muted stone/sage/dusty-blue tones
  (#cedddf, #aec5ca, #c1cebd, #cec3b6, #6694b5) that read as brand-adjacent
  outdoor accents rather than generic UI states; their exact semantic role is
  inferred, not confirmed by a labeled brand stylesheet.

  Typography evidence points to a Suisse-family typeface (suisse,
  SuisseWorks) as the intended brand voice, falling back through Frutiger,
  Helvetica Neue, Univers and Arial — a fallback stack consistent with a
  European outdoor-gear brand. Confirmed CSS shows headings (h1–h6) at
  font-weight 500 and line-height 1.2; all specific pixel sizes below are
  proposed, not measured.

  The resulting system favors a clean, functional, high-contrast interface —
  dark ink text on white/soft-neutral surfaces, a confident blue action
  color, and muted stone/sage tones reserved for category or lifestyle
  accents (e.g., strollers, camping, water sports) — appropriate for a
  technical outdoor-gear and child-transport retailer.

colors:
  primary: "#0d6efd"
  ink: "#181818"
  canvas: "#ffffff"
  body: "#474747"
  muted: "#757575"
  hairline: "#e0e0e0"
  surface-soft: "#f5f5f5"
  surface-card: "#f8f9fa"
  on-primary: "#ffffff"
  secondary-accent: "#6694b5"
  sage-accent: "#c1cebd"
  stone-accent: "#cec3b6"
  border-strong: "#a3a3a3"
  success: "#198754"
  danger: "#af0a0a"
  warning: "#ffc107"
typography:
  display-xl: {fontFamily: "suisse, 'Helvetica Neue', helvetica, arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "suisse, 'Helvetica Neue', helvetica, arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "suisse, frutiger, helvetica, arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "suisse, helvetica, arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "suisse, helvetica, arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "suisse, helvetica, arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "suisse, helvetica, arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairlineColor: "{colors.border-strong}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sage-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  stroller-finder:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.secondary-accent}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the confirmed `.btn-primary` Bootstrap-derived blue (`#0d6efd`) on white text, suited to primary calls to action like "Buy strollers" or "Add to cart." Hover/active state colors (`#0b5ed7`, `#0a58ca`) are present in the CSS but their applied visual timing is not observed.

**button-secondary** is a proposed outline treatment using the muted border-strong tone, intended for secondary actions such as "Learn more" or "Find your local dealer," which appear in the source copy but without dedicated button markup evidence.

**text-input** is inferred from generic Bootstrap form-control patterns (`.form-control`) with a light hairline border and soft rounding; no Thule-specific input styling was captured.

**nav-bar** is proposed as a clean white bar with dark ink text, reflecting the minimal, utility-first Bootstrap scaffolding observed; actual sticky/mega-menu behavior was not measured.

**product-card** proposes a soft off-white card surface (`#f8f9fa`) with a hairline border, appropriate for grid layouts implied by "Popular categories" (Hitch bike racks, Roof boxes, Rooftop tents, etc.); card geometry itself is not directly evidenced.

**hero** interprets the dark ink background seen in the near-black neutral scale (`#181818`) paired with white text, matching the marketing tone of "Bring your life®" banner copy; actual hero markup/background was not captured in the supplied CSS.

**footer** mirrors the hero's dark treatment for a grounded, technical brand close, holding link groups such as Order Support, Product Support, and Thule Group — all present in page text but without footer-specific selectors in evidence.

**badge** and **search** are proposed utility components: badge for category/feature tags (e.g., "Outdoor quality," safety-test callouts) using a sage accent; search as a pill-shaped input consistent with the rounded, full-radius token, though no search-bar CSS was directly observed.

**stroller-finder** is a category-appropriate proposed component — a filter/quiz-style panel using the dusty-blue secondary accent — reflecting the site's emphasis on the "Buy strollers" and "Active with kids" categories, though no such interactive tool markup was present in the supplied evidence.

## Responsive Behavior

Recommended breakpoints (not measured from thule.com, proposed for a Bootstrap-based system consistent with the observed `--bs-breakpoint-*` custom properties):

| Breakpoint | Width | Notes |
|---|---|---|
| xs | 0px | Single-column, stacked nav, full-width cards |
| sm | 576px | Confirmed Bootstrap variable; minor spacing increase |
| md | 768px | Confirmed Bootstrap variable; nav may collapse to hamburger |
| lg | 992px | Confirmed Bootstrap variable; multi-column product grids |
| xl | 1200px | Confirmed Bootstrap variable; max-width containers |
| xxl | 1400px | Confirmed Bootstrap variable; widest container |

Touch targets should be at minimum 44×44px for primary buttons and nav items. Navigation is expected to collapse to an off-canvas or hamburger menu below `md`. This table is a design recommendation based on standard Bootstrap breakpoint tokens found in the CSS, not a record of observed responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to a static Bootstrap-derived vendor stylesheet; no Thule-specific brand CSS file was supplied, so component-level styling (cards, nav, hero, footer) is largely inferred from generic utility classes and marketing copy.
- Many palette entries (e.g., `#0d6efd`, `#198754`, `#dc3545`, `#ffc107`) are standard Bootstrap defaults and may not reflect Thule's actual applied brand palette in production; muted stone/sage/blue tones are more likely brand-specific but their exact UI role is unconfirmed.
- Font family evidence (suisse, SuisseWorks, frutiger, univers) confirms intended typefaces but not licensing, availability, or exact size/weight pairings beyond the confirmed heading weight (500) and line-height (1.2).
- No interaction states (focus, hover timing, transitions), mobile layout, or grid structure were directly observed; all such behavior is proposed.
- Rounded and spacing scales follow a generic proposed system, not values extracted from the supplied CSS.
- Custom icon fonts (Font Awesome variants, frg-icons) are present but not used in this design system beyond acknowledging their existence.
