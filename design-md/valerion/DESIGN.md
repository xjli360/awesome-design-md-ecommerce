---
version: alpha
name: "Valerion"
source_url: "https://valerion.com"
captured_at: "2026-09-29T03:59:47.821046+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Valerion (AWOL's premium home-cinema line) presents as a near-black, cinema-styled
  storefront: page background and body render as solid black (#000000) with white
  (#ffffff) body copy, confirmed directly from computed body styles (16px, weight 500,
  line-height 1.33em, letter-spacing -0.03em). A saturated cyan-teal (#00e5e3) appears
  in the observed palette and is interpreted here as the primary accent for CTAs and
  highlight moments, consistent with a projector/cinema brand needing a glow-like
  signature color against black. A blue (#007aff) surfaces as the Swiper carousel
  theme color and is treated as a secondary interactive accent for slider controls and
  links, inferred rather than confirmed as a core brand color. Neutral tones (#b3b3b3
  muted gray, #f2f2f2 soft white, #121212 near-black) and several alpha-black values
  (#00000026, #00000040, #00000080, transparent) are assumed to serve overlays, hairline
  dividers, and layered surfaces on the dark canvas — these role assignments are
  inferred, not measured. Typography uses the custom "awolPPNeueMontreal" family
  (confirmed on body and h1 elements) with generic sans-serif fallback; "awolDm" is
  present in the font stack but its specific usage was not captured in the computed
  samples, so it is treated speculatively as a numeral/price-display face.

colors:
  primary: "#00e5e3"
  ink: "#ffffff"
  canvas: "#000000"
  body: "#f2f2f2"
  muted: "#b3b3b3"
  hairline: "#00000026"
  surface-soft: "#00000040"
  surface-card: "#121212"
  on-primary: "#000000"
  accent-secondary: "#007aff"
  scrim: "#00000080"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 64px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -1px}
  display-md: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  title-md: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.02em}
  body-md: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.33em, letterSpacing: -0.03em}
  body-sm: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.4, letterSpacing: -0.02em}
  caption: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: -0.01em}
  button-md: {fontFamily: "awolPPNeueMontreal, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.02em}
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
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    overlayColor: "{colors.scrim}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-comparison-table:
    backgroundColor: "{colors.surface-card}"
    headerColor: "{colors.primary}"
    textColor: "{colors.ink}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** — The core purchase CTA ("Shop Now", "Buy Now", "Discover"). Uses the teal accent (#00e5e3) as a bright, glowing action color against the black canvas, with black text for contrast. Hover/pressed states are proposed, not observed.

**button-secondary** — An outline/ghost variant matching computed samples where button background resolves to transparent (`rgba(0,0,0,0)`) with white text and an implied white border, used for secondary actions like "Discover" links inside dark hero panels.

**text-input** — Proposed for cart/search/newsletter fields; no dedicated input styling was captured in the extracted CSS, so background, border, and padding are inferred from the surface-card and hairline tokens.

**nav-bar** — Represents the top utility bar (Projectors, Shop by Scenario, My Cart). Assumed transparent-to-black on scroll, consistent with the black body background; exact scroll-state behavior was not observed.

**product-card** — Used for bundle listings such as "AWOL Valerion Pro + FREE Accessory Bundle." Card surface uses the near-black #121212 to separate from the pure-black page background, a distinction inferred from the palette rather than measured spacing/shadow data.

**hero** — Full-bleed promotional banner (e.g., "Elevated Fall Viewing") over black canvas with an alpha-black scrim (#00000080) for text legibility over imagery; scrim opacity is inferred, not confirmed via a captured overlay rule.

**footer** — Site-wide footer carrying warranty/shipping trust badges ("24-Month Warranty," "30-Day Money Back Guarantee") in muted gray text on black, with hairline dividers between sections.

**badge** — Small pill labels for trust markers and promo tags (e.g., "No.1 UST laser projector brand"); rendered in the teal primary for visibility, rounded fully.

**search** — Proposed header search affordance; no direct search UI was present in the extracted markup, so this pattern is speculative, built from soft-surface and muted-placeholder tokens.

**spec-comparison-table** — Category-appropriate component for comparing projector models (Valerion Max vs. Pro2/Pro vs. Long-Throw) side by side, using card surface with a teal header row to align with the "Choose Your AWOL Valerion" model-selection pattern implied by the page text.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <640px | single-column hero/product stacking, nav collapses to menu icon |
| tablet | 640–1024px | 2-column product/bundle grids |
| desktop | 1024–1440px | 3–4 column grids, full nav-bar visible |
| wide | >1440px | max-width container, additional whitespace |

Touch targets should be at least 44×44px for buttons and badges. Nav items are assumed to collapse into a hamburger/drawer under 1024px. None of this was confirmed via responsive CSS or live rendering — it is a conventional recommendation only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static: no live layout, computed hover/focus/active states, or JavaScript-driven interactions (e.g., cart drawer, carousel behavior) were observed.
- Role assignments for the alpha-black values (#00000026, #00000040, #00000080) as hairline/scrim/surface-soft are inferred from plausible dark-UI conventions, not from matched selectors.
- "awolDm" font's actual application (if any, e.g., numerals or price displays) is unconfirmed; only "awolPPNeueMontreal" was seen in captured computed styles.
- All typography sizes beyond the one directly observed body rule (16px/500/1.33/-0.03em) are proposed, not measured.
- Rounded-corner and spacing scales are template defaults, not derived from captured border-radius or margin/padding values.
- Custom font licensing/availability for "awolPPNeueMontreal" and "awolDm" was not verified; fallback to generic sans-serif is assumed.
- Mobile/tablet layout, breakpoints, and touch-target sizing are proposed conventions, not observed from responsive CSS.
