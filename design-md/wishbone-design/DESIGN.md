---
version: alpha
name: "Wishbone Design"
source_url: "https://wishbonedesign.com"
captured_at: "2026-09-29T03:53:21.855977+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wishbone Design Studio's storefront CSS shows a warm, tactile palette built
  around a muted teal primary (#71a1a1) against a soft linen canvas (#f2ebe2),
  with near-black (#2f2f2f) used for both body text and a "dark" semantic
  token. Bootstrap-derived utility colors (success green #63c583, warning
  yellow #efd37b, danger red #dc3545, info cyan #17a2b8) are present in the
  compiled CSS variables and are treated here as inferred status/accent roles
  rather than confirmed UI usage. A separate navy (#204a80) appears explicitly
  on rich-text ".btn" elements, suggesting a secondary call-to-action accent
  distinct from the teal primary. Typography pairs a rounded proprietary
  sans, gt_walsheim_proregular, for body copy and buttons with
  itc-american-typewriter, a serif with typewriter character, bolded for all
  heading levels — an editorial, handcrafted contrast fitting a family-run
  NZ toy brand. This interpretation proposes a warm, low-saturation system:
  soft card surfaces, thin hairlines from the neutral gray-200/300 tokens,
  and generous spacing to suit a toy/product catalog with imagery-led
  browsing. Component patterns (product cards, nav, footer) are proposed
  conventions inferred from typical Shopify storefront structure, not
  confirmed layout observations.

colors:
  primary: "#71a1a1"
  ink: "#2f2f2f"
  canvas: "#f2ebe2"
  body: "#2f2f2f"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#204a80"
  accent-blue-hover: "#163257"
  success: "#63c583"
  warning: "#efd37b"
  danger: "#dc3545"
  info: "#17a2b8"
  dark: "#181818"
  tan: "#dcd1c2"
  teal-deep: "#3b5454"
  teal-pale: "#dce8e8"
  gray-light: "#e9ecef"
  disabled-bg: "#f6f6f6"
  disabled-text: "#b8b8b8"
typography:
  display-xl: {fontFamily: "itc-american-typewriter, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  display-md: {fontFamily: "itc-american-typewriter, serif", fontSize: 34px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "itc-american-typewriter, serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "gt_walsheim_proregular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "gt_walsheim_proregular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "gt_walsheim_proregular, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "gt_walsheim_proregular, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.42, letterSpacing: 0px}
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
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    hover: "{colors.accent-blue-hover}"
    active: "#0c1b2e"
    disabled:
      backgroundColor: "{colors.disabled-bg}"
      textColor: "{colors.disabled-text}"
  button-secondary:
    backgroundColor: "#dcdcdc"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    hover: "#c3c3c3"
    active: "#a9a9a9"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hoverTextColor: "#0d0d0d"
    activeBackground: "{colors.gray-light}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px #00000013"
  hero:
    backgroundColor: "{colors.tan}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.surface-soft}"
    linkTypography: "{typography.body-sm}"
    hairline: "{colors.teal-deep}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  age-range-badge:
    backgroundColor: "{colors.teal-pale}"
    textColor: "{colors.teal-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the navy (#204a80) observed on `.rte .btn` elements,
with documented hover (#163257) and active/focus (#0c1b2e) darkening steps
taken directly from the CSS cascade; the disabled state (gray background,
muted text) is also directly observed.

**button-secondary** mirrors the `.btn--secondary` rule set exactly as
supplied (`#dcdcdc` → `#c3c3c3` hover → `#a9a9a9` active), proposed here for
lower-emphasis actions like "add to wishlist" or filter toggles.

**text-input** is a proposed pattern; no explicit `input` styling was
supplied beyond font inheritance, so border, radius, and focus-ring color
are inferred from the broader neutral/teal palette.

**nav-bar** draws its hover and active states from `.mobile-nav__item a`
rules (`#333` idle, `#0d0d0d` hover, `#e9e9e9` active background), extended
here as a proposed pattern for a persistent top navigation, though only
mobile-nav selectors were directly observed.

**product-card** is an inferred composition for a toy catalog grid; no card
selector was present in the supplied CSS, so surface color, radius, and
shadow are proposed defaults consistent with the neutral/white tokens seen
elsewhere (e.g., table striping at `#0000000d`).

**hero** is proposed to introduce the brand's balance-bike/ride-on-toy
messaging using the warm tan (#dcd1c2) background and the serif display
type observed on headings; layout and imagery placement are not observed.

**footer** is proposed using the darkest observed neutral (#181818) for
contrast with the light body copy, appropriate for a closing
brand/newsletter/legal section referenced in the page text ("Email sign up",
"© Wishbone Design Studio").

**badge** and **age-range-badge** are proposed, category-appropriate
components for surfacing product status (e.g., "New", "Recycled Edition")
and toy age suitability (e.g., "1–5 yrs"), built from the warning-yellow and
pale-teal tokens present in the palette; neither was confirmed as an actual
UI element on the site.

**search** is a proposed pattern for the site's product search, styled
consistently with text-input using neutral borders and muted iconography;
no search-bar CSS was supplied.

## Responsive Behavior

Recommended, not measured, breakpoints aligned to the `--breakpoint-*`
custom properties found in the compiled CSS:

| Breakpoint | Width   | Notes (proposed) |
|-----------|---------|-------------------|
| xs        | 0px     | Single-column stacking, mobile nav drawer |
| sm        | 576px   | Two-column product grids begin |
| md        | 768px   | Nav collapses to `.mobile-nav__toggle` below this point |
| lg        | 992px   | Three/four-column product grids, full nav bar |
| xl        | 1200px  | Max-width content container |

Touch targets should be a minimum 44×44px for buttons and nav items,
consistent with the observed `.mobile-nav__item a` padding of 15px. The
`.mobile-nav__toggle` selector confirms a collapsing mobile menu exists;
its open/closed visual states were not captured in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text extraction of one
theme bundle; no rendered screenshots, DOM structure, or interaction states
(hover/focus/active beyond the explicit `:hover`/`:active`/`:focus` rules
quoted above) were observed. Product-card, hero, search, and nav-bar visual
compositions are inferred conventions for a Shopify-style toy storefront,
not confirmed layouts. The `gt_walsheim_proregular` and
`itc-american-typewriter` fonts are proprietary/licensed assets whose
availability and licensing terms were not verified — generic fallbacks
(`sans-serif`, `serif`) are included per requirement. Numeric type scale
values (font sizes for display/title/body variants) are proposed
estimates, not measured from rendered pixels. Several palette entries
(e.g., alpha-blended hexes like `#71a1a180`, `#00000013`) exist in the
source but were treated as effects/overlays rather than assigned semantic
roles. Breakpoint and spacing scales are conventional proposals layered
onto the observed `--breakpoint-*` variables, not confirmed responsive
behavior.
