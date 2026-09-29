---
version: alpha
name: "Nanoleaf"
source_url: "https://nanoleaf.me"
captured_at: "2026-09-28T10:00:14.273511+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Nanoleaf's storefront CSS shows a Shopify-based smart-home retailer layered over a
  restrained neutral palette punctuated by a single signature green. The authoritative
  brand token is `--color-brand-green: #48A06A`, applied via CSS custom properties across
  navigation "segment" accents (AI & Robotics, Home & Lighting) and derived hover/dark
  variants through color-mix. A darker navy-black, `#1a1a2e`, recurs in a separate
  "bundle builder" component system (`--bb-dark`, `.bundler__product-toggle`) and is
  interpreted here as a secondary ink used for high-emphasis buttons and selected-state
  borders, distinct from the brand green. Surfaces are warm near-whites (`#f5f4f0`,
  `#f7f7f8`) against a pure white canvas, with light gray hairlines (`#e5e5e5`) for card
  and input borders. Sale/clearance messaging uses red (`#e63946`) and amber (`#f59e0b`)
  accents observed alongside percentage-off badges in the page text. Radii lean toward
  fully-rounded pill buttons (`--radius-button: 100px`) and a 12px card/image radius.
  Typography lists Gilroy and Inter among the loaded font families; Gilroy is inferred as
  a display/heading face (common for premium DTC hardware brands) and Inter as the body/UI
  workhorse, with system-ui and monospace stacks reserved for code/technical contexts. No
  live layout, hover, or breakpoint behavior was directly observed.

colors:
  primary: "#48A06A"
  primary-strong: "#308551"
  ink: "#1a1a2e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#71717a"
  hairline: "#e5e5e5"
  surface-soft: "#f5f4f0"
  surface-card: "#f7f7f8"
  on-primary: "#ffffff"
  accent-sale: "#e63946"
  accent-amber: "#f59e0b"
  success: "#51BD7A"
  wellness-tint: "#8fc8a5"
typography:
  display-xl: {fontFamily: "Gilroy, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gilroy, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gilroy, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 9px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  bundle-builder:
    backgroundColor: "{colors.canvas}"
    cardBorderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    toggleBackgroundColor: "{colors.ink}"
    toggleTextColor: "{colors.on-primary}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the brand green fill (`--color-brand-green`) directly observed in
`:root`, paired with a fully pill-shaped radius matching `--radius-button: 100px`. Hover/
active states are not observed in static CSS beyond the color-mix darkening formula and are
therefore proposed.

**button-secondary** is an inferred outline variant for lower-emphasis actions (e.g. "See
All"), reusing the hairline border color and ink text for contrast against the white canvas.

**text-input** proposes a light-bordered field consistent with the site's generally low-
contrast hairline system; no focus-ring color was directly observed, so focus treatment is
proposed rather than confirmed.

**nav-bar** reflects the text-based segment navigation ("AI & Robotics / Home & Lighting /
Wellness / Products / Technology / About / Sale") seen in page text; exact height and sticky
behavior are proposed, not measured.

**product-card** models the dense grid of product tiles (name, price, strike-through
compare-at price) implied by the page text excerpt, using the surface-card off-white and the
12px-equivalent large radius token to echo `--radius-card`.

**hero** is proposed as a dark, ink-background banner for the top-of-funnel promotional
messaging ("A Better Nanoleaf Experience Is Here!"); no hero-specific CSS was supplied, so
color and spacing choices here are interpretive.

**footer** is inferred as a dark ink-colored band for consistency with the bundle-builder's
dark UI language; actual footer markup/colors were not present in the supplied evidence.

**badge** directly reflects the sale/discount badges visible throughout the page text
("50% OFF", "NEW") and the `.bundler__product-badge` rule (uppercase, pill-radius, white
text on a solid fill); the accent-sale red is used here as one plausible fill, though amber
is equally evidenced for percentage badges.

**search** is a proposed pill-shaped input consistent with the rounded-full button language;
no search-bar CSS was directly supplied.

**bundle-builder** is the category-appropriate component, grounded directly in observed
`--bb-*` variables and `.bundler__product`, `.bundler__product-toggle`, and `.bb__qty`
rules: a card-based kit/bundle selector with an ink-colored selected-state border and a dark
pill toggle button, matching Nanoleaf's real merchandising pattern of starter kits and
bundles (e.g. "Nanoleaf Shapes Starter Kits", "Prismatic Fusion Bundle").

## Responsive Behavior

This table is a recommendation based on the two divergent `--section-spacing-*` value sets
observed in `:root` (one larger set — 24/48/64/80px — and one compressed set — 18/34/42/48px
— likely representing desktop vs. narrower-viewport scaling), not measured breakpoint
behavior.

| Breakpoint | Approx. width | Notes (proposed) |
|---|---|---|
| Compact | < 768px | Compressed section spacing (~18–48px); nav likely collapses to a menu icon; single-column product grid. |
| Medium | 768–1023px | Two-column product grid; standard section spacing begins scaling up. |
| Large | 1024–1439px | Full section spacing (24–80px scale); multi-column grids and visible top nav. |
| XL | ≥ 1440px | Max-width content container with generous section spacing at the upper end of the scale. |

Touch targets should be sized at a minimum of 44px in height for buttons and quantity
controls (the observed `.bb__qty button` is 36px/2.25rem, slightly below this recommended
minimum and flagged for proposed adjustment on touch devices). Navigation collapse and
mobile menu interaction were not observed and are proposed based on common e-commerce
patterns.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered layout,
  hover, focus, active, or animation states were directly observed.
- Font-family *roles* (Gilroy for display, Inter for body) are inferred from the loaded
  family list; no selector-to-role mapping was present in the supplied evidence, and
  Gilroy's licensing/availability for this project is not verified.
- The `body` color token (`#333333`) approximates a `rgba(26,26,46,0.72)` value found on
  `.ag__body`; the exact rendered gray depends on background compositing and is not a
  literal hex match.
- Two conflicting `--section-spacing-*` scales were present in the evidence with no
  associated media-query context supplied, so their breakpoint mapping is inferred.
- Card and button radius values (12px card, 100px/pill button) were rounded to the nearest
  token in the fixed `rounded` scale (`lg`, `full`); exact pixel fidelity is approximate.
- Mobile navigation structure, header height, and footer content/columns were not present
  in the supplied evidence and are entirely proposed.
- Accent colors for sale/clearance (`#e63946`, `#f59e0b`) were present in the palette but
  their exact applied context (badge vs. text vs. banner) was not confirmed by selector
  evidence.
