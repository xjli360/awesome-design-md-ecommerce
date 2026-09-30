---
version: alpha
name: "Bravado Spice"
source_url: "https://bravadospice.com"
captured_at: "2026-09-28T10:21:21.495811+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bravado Spice's public CSS shows a Shopify storefront built on a light, food-forward palette anchored by a warm terracotta (#d9725b), a fresh herb green (#abd38a, customized into the Judge.me review-widget variables), and near-black ink (#000000) on a soft cream canvas (#fefaf9). A darker charcoal (#2f3132) appears as the page-builder's primary button color, while light peach (#fae8e3) and pale sage (#f5f7f2) function as soft surface tints suited to product cards and callouts. Typography is confirmed as Poppins across body copy, labels, and buttons (body: 400/16px/1.4em; buttons: 400/16px/1.2em), with heading weight set to 500 for h2-h6. The Shopify page-builder module additionally defines large-scale heading tokens (h1: 72px/90px/600/-0.02em; h2: 60px/72px/600/-0.02em) which this spec treats as observed display sizing. A custom asset named "AbolitionTest-RoundOblique" is present in the font stack and is inferred here as a possible bold display face for hero headlines, though its actual application in layout was not observed. Buttons show a 3px border-radius and 2px border stroke. Color-role assignments (primary, muted, hairline, surface tiers) are semantic inferences drawn from where each hex is most plausibly used, not confirmed computed styles.

colors:
  primary: "#d9725b"
  secondary: "#abd38a"
  surface-dark: "#2f3132"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f7f2"
  surface-card: "#fae8e3"
  canvas: "#fefaf9"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "AbolitionTest-RoundOblique, Poppins, sans-serif", fontSize: 72px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.02em}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 60px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.02em}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 28px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "proposed soft drop shadow, not observed"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  heat-level-indicator:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the terracotta brand accent as its fill, a color chosen for its association with warmth/spice in the observed palette, paired with white text and the 3px-adjacent `sm` radius drawn from the theme's own `border-radius: 3px` button rule. **button-secondary** is a proposed outline variant reusing the same primary hue for border and label text, for lower-emphasis actions like "Learn more."

**text-input** is inferred from generic form styling conventions (no direct input CSS was supplied); it pairs the cream canvas with the light-gray hairline border observed elsewhere in the palette.

**nav-bar** is proposed as a light cream bar with dark ink labels and a hairline bottom border, consistent with the light body background and dark body text confirmed in the base `body` rule.

**product-card** leans on the light peach surface tint (`#fae8e3`) as a warm, food-appropriate card background, with title and price typography matching the theme's confirmed heading and body rules; the drop shadow is a proposed, unobserved refinement.

**hero** repurposes the dark charcoal `--ecom-global-colors-primary` value as a full-bleed section background, sized using the observed 72px/90px h1 tokens from the page-builder's global typography variables, giving large campaign headlines strong contrast against white text.

**footer** mirrors the hero's dark surface treatment for visual bookending, using smaller body-sm typography for link lists; exact footer layout was not present in the supplied evidence and is inferred from common Shopify footer conventions.

**badge** adopts the fresh green (`#abd38a`) used to theme the Judge.me review widget, extended here as a small pill for flags like "New" or "Bestseller," with a fully rounded corner.

**search** is a proposed pill-shaped input using the pale sage surface-soft tint, intended to sit in the nav-bar or a dedicated search overlay; no search-specific CSS was supplied.

**heat-level-indicator** is a category-appropriate proposed component for a hot-sauce/condiment brand: a small chip using the peach surface and terracotta accent to represent spice-level ratings on product listings, not confirmed against any supplied selector but consistent with the site's food-product content.

## Responsive Behavior

| Breakpoint | Target | Notes (proposed) |
|---|---|---|
| < 480px | Mobile | Single-column stacks; nav collapses to a hamburger/drawer; hero title drops toward `{typography.display-md}` scale. |
| 480–768px | Large mobile / small tablet | Two-column product grids; sticky add-to-cart bar suggested for PDP. |
| 768–1024px | Tablet | Nav switches to inline links; product-card grid moves to 3 columns. |
| ≥ 1024px | Desktop | Full nav bar; container width capped near the observed `--ecom-global-container-width: 1200px`; product grid 4 columns. |

Touch targets should be at least 44px in height for buttons and nav items on mobile. Mobile nav collapse, sticky elements, and grid column counts above are **recommended patterns**, not measured from live site behavior, since no responsive/media-query evidence or runtime screenshots were supplied.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All extraction is static: no rendered layout, breakpoints, hover/focus states, or JS-driven interactions (cart drawer, currency selector, sliders) were actually observed.
- Color **roles** (primary, muted, hairline, surface tiers) are inferred from where each hex most plausibly applies; the base theme button rule (`background:#fefaf9; color:#fefaf9; border:#fefaf9`) suggests real button coloring is set via per-instance overrides not present in this evidence, so `button-primary`'s terracotta fill is a design proposal, not a confirmed computed style.
- Numerous supplied hexes (e.g., payment-brand blues/reds, Facebook blue `#3b5998`) are third-party icon/payment colors and were deliberately excluded from brand role assignment.
- `display-xl`'s use of `AbolitionTest-RoundOblique` is inferred purely from the font-face name present in the asset list; no selector tying it to headings was supplied, and its licensing/availability as a web font was not verified.
- Heading sizes for `title-md`, `body-sm`, and `caption` are proposed values, not present verbatim in the supplied CSS (the h3–h6 rule was truncated before its font-size declaration).
- `rounded` and `spacing` scales follow a standard proposed system; only the button's 3px radius and the slick-dot's 10px/20px values were directly observed.
