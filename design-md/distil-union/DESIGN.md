---
version: alpha
name: "Distil Union"
source_url: "https://distilunion.com"
captured_at: "2026-09-28T09:49:42.319077+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Distil Union positions itself as a considered, systems-minded leather-goods maker
  (wallets, MagLock accessories, everyday-carry organization), and the extracted CSS
  supports a restrained, high-contrast retail aesthetic rather than a decorative one.
  The observed palette is dominated by near-black and near-white values (#000000,
  #121212, #ffffff, #fefefe) with a family of warm-to-cool grays (#333333, #595959,
  #777777, #9ca3a8, #cccccc, #dedede, #e6e6e6, #f0f0f0, #f1f1f1, #f3f3f3) used for
  text hierarchy, hairlines and soft surfaces. A blue pair (#1990c6, #136f99) appears
  specifically on Shopify's accelerated-checkout button and its hover state, so it is
  treated here as a payment-affordance accent, not a brand primary. A green (#33cc66)
  and a link-blue (#005fcc) are present in the raw palette and are mapped, as inferred
  roles, to success/confirmation and inline-link states respectively, since no other
  evidence disambiguates their use. Border-radius tokens on the one measurable
  interactive element (the checkout button) default to 0px, supporting a squared,
  architectural default rather than pill-shaped controls. Typography combines
  "Instrument Sans" (body/UI) with a licensed-looking "galanogrotesque" family
  (regular/medium/bold) for headings and a distinct "tttricksregular" face whose
  application is unconfirmed. Sizing below is grounded in the site's own --text-*
  custom properties where possible; larger display sizes are proposed extrapolations.

colors:
  primary: "#000000"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#e6e6e6"
  surface-soft: "#f3f3f3"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  border-strong: "#cccccc"
  accent-link: "#005fcc"
  success: "#33cc66"
  checkout: "#1990c6"
  checkout-hover: "#136f99"
  overlay: "#00000066"
typography:
  display-xl: {fontFamily: "galanogrotesquebold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "galanogrotesquemedium, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "galanogrotesqueregular, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Instrument Sans, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Instrument Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** — Solid black fill with white text and a 0px radius, matching the
squared `border-radius:0px` default seen on the Shopify accelerated-checkout button.
Used for primary CTAs like "Add to Cart" and checkout. Hover/active/disabled states
are proposed, not observed.

**button-secondary** — White/canvas background with a hairline border and dark text,
for tertiary actions ("Learn More," filter toggles). Border and hover treatment are
inferred from the general hairline-gray system rather than a captured secondary-button
rule.

**text-input** — Minimal bordered field (hairline border, small radius) for
newsletter/search/account forms. Focus-ring color and error-state styling are not
present in the extracted CSS and are marked proposed.

**nav-bar** — A white, sticky header (`--header-is-sticky: 1` observed) with a
three-column logo/nav grid (`--header-grid`) and a measured logo width shrinking from
100px to 70px on scroll or breakpoint. Padding uses the observed
`--header-padding-block` values (1rem / 1.6rem). Mobile hamburger behavior is not
observed and is proposed.

**product-card** — A bordered, un-rounded card for wallet/cardholder listings,
pairing a title in the galanogrotesque display face with a body-weight price line.
Hover elevation/zoom is not present in the extracted rules and is proposed.

**hero** — Full-bleed dark section using ink as background and white display type,
inferred from `--header-transparent-header-text-color: 255 255 255`, which implies a
dark or image hero the header can sit transparently over. Copy hierarchy and imagery
are proposed.

**footer** — Multi-column footer on a soft-gray surface, using
`--footer-content-justify-items: space-between` (observed) to justify link groups.
Column count and breakpoint collapse are proposed.

**badge** — Small pill label for sale/new/sold-out flags, drawing on the observed
`--on-sale-badge-*`, `--sold-out-badge-*`, and `--custom-badge-*` custom properties,
which confirm badges exist as a system even though their exact source colors (e.g.
`rgb(227 44 43)`) fall outside the supplied hex palette and are approximated here with
`{colors.primary}`/`{colors.on-primary}`.

**search** — Compact input+icon pattern on a soft surface, consistent with the site's
general light-gray secondary-surface treatment. Expand/overlay behavior on mobile is
not observed.

**color-swatch-selector** — Category-appropriate control for choosing wallet/leather
color or hardware finish: circular swatches with a hairline border that switches to a
primary-colored ring when selected. This entire pattern is proposed by category
convention, not directly observed in the extracted CSS.

## Responsive Behavior

| Breakpoint | Width   | Notes (proposed) |
|---|---|---|
| sm | ≤480px | Single-column product grid, stacked nav under a collapsed menu |
| md | 481–768px | 2-column product grid; container gutter narrows toward the observed 2rem token |
| lg | 769–1024px | 2–3 column grid; container gutter approaches the observed 3rem token |
| xl | ≥1025px | Full desktop grid; header logo at full 100px width per observed custom property |

Touch targets should be a minimum 44px hit area for nav, cart, and swatch controls.
Header logo width shifting from 100px to 70px and the sticky-header custom properties
are the only scroll/breakpoint-adjacent values directly observed; all column counts,
collapse points, and menu behavior above are a recommendation only, not measured site
behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/custom-property extraction plus page text; no rendered
  screenshots, computed layout, or DOM structure were available, so grid/column
  counts and actual card/hero composition are inferred from convention.
- The blue pair (#1990c6/#136f99) is confirmed only for Shopify's native accelerated
  checkout button; treating it as a general "checkout" accent elsewhere is an
  assumption.
- Sale/badge colors defined via `--on-sale-*`/`--custom-badge-*` use RGB triplets not
  present verbatim in the supplied hex palette; badge colors above are approximated
  with in-palette black/white rather than invented hexes.
- No hover, focus, active, or disabled interaction states were present in the
  extracted rules for most components; all such states are proposed.
- Mobile menu, filter-drawer, and swatch-selector interactions were not observed and
  are proposed by category convention (wallets/cardholders).
- Font availability, weights actually shipped, and licensing for "galanogrotesque"
  and "tttricksregular" were not verified; fallback stacks assume standard sans-serif
  substitution only.
- All display-tier font sizes (48px/32px/20px) are proposed; only the smaller
  `--text-xs` through `--text-xl` tokens (12–20px) were directly observed in `:root`.
