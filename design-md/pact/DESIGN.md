---
version: alpha
name: "Pact"
source_url: "https://wearpact.com"
captured_at: "2026-09-28T04:15:46.880128+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pact's stylesheet confirms a body typeface stack of Averta, Helvetica Neue,
  and Arial set at 14px (.875rem) with 1.5 line-height over a warm dark-gray
  ink (#4d4a43) on a white canvas (#ffffff). Headings inherit this same family
  at weight 500 and a tight 1.1 line-height, so the interpretation treats
  Averta as the single confirmed brand typeface across display and body
  roles rather than introducing an unverified serif. The supplied palette
  mixes true brand-adjacent tones — a mid-green (#38761d) with a darker
  hover variant (#254d13), a terracotta accent (#c8422d) with its hover
  (#9e3424), warm off-whites (#f7f7f5, #f0f0ed, #ebeae8), and an earthy tan
  (#a98d6d) — with generic third-party utility colors from Bootstrap-style
  alert classes and the jQuery UI Smoothness theme (e.g. #dff0d8, #fcf8e3,
  #cccccc). This document assigns the green and terracotta family to
  brand-facing primary/accent roles as an inferred choice consistent with
  an eco-apparel positioning, and reserves the neutral off-whites and
  warm grays for surfaces and hairlines. No live layout, spacing, or
  interaction states were observed; sizes, radii, and component patterns
  below are proposed conventions grounded only in the confirmed color and
  type values.

colors:
  primary: "#38761d"
  primary-dark: "#254d13"
  ink: "#4d4a43"
  canvas: "#ffffff"
  body: "#4d4a43"
  muted: "#94928e"
  hairline: "#ebeae8"
  surface-soft: "#f7f7f5"
  surface-card: "#f0f0ed"
  on-primary: "#ffffff"
  accent: "#c8422d"
  accent-dark: "#9e3424"
  sage: "#516259"
  tan: "#a98d6d"
  tint-green: "#eaf3e7"
  border: "#cac9c7"
typography:
  display-xl: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "48px", fontWeight: 500, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.1, letterSpacing: "0px"}
  title-md: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "11px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Averta, 'Helvetica Neue', Arial, sans-serif", fontSize: "13px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.3px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.tint-green}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  certification-callout:
    backgroundColor: "{colors.tint-green}"
    textColor: "{colors.primary-dark}"
    borderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the inferred brand green (#38761d) as a solid fill with white text, intended for primary calls to action such as "Add to Cart." A proposed hover/active state would deepen to `primary-dark` (#254d13), mirroring the darker green observed elsewhere in the palette; this hover behavior is proposed, not observed.

**button-secondary** is an outline treatment using the same green on a transparent background, for lower-emphasis actions like "View Details." Focus and disabled states are not confirmed by the evidence and are proposed as reduced-opacity variants.

**text-input** follows a plain bordered field pattern common to commerce forms, using the neutral border color and body typography. Focus-ring color and validation states (error/success) were not captured in the extracted rules and are proposed only.

**nav-bar** is modeled as a white bar with ink text and a hairline bottom border, consistent with the light, neutral canvas confirmed in the base stylesheet. Sticky behavior, mega-menu structure, and active-link styling are unmeasured and proposed.

**product-card** sits on a slightly warm off-white surface with rounded corners, appropriate for apparel imagery and price/label text. Hover elevation or image-swap interactions are proposed conventions, not verified.

**hero** proposes a large display headline on the soft surface tone, reflecting the confirmed heading weight (500) and tight line-height (1.1) from the h1–h6 rule, scaled up for a landing banner. Exact hero copy, imagery, and breakpoint sizing are not observed.

**footer** uses the darker sage green as a grounding band with white text, an inferred choice to differentiate the footer from the primary white page background while staying within the eco-toned palette. Column structure and link groupings are proposed.

**badge** and **certification-callout** both draw on the light green tint (#eaf3e7) with the darker green text, intended for sustainability messaging (e.g., "Organic Cotton," "Fair Trade Certified") that is typical of an eco-positioned apparel brand. This pairing is an inferred use of the palette's green family for trust/impact signaling, not a confirmed component from the site.

**search** proposes a pill-shaped, muted-tone input for header search, using rounded-full geometry and the muted gray text color; no search UI markup was present in the supplied evidence.

## Responsive Behavior

The following breakpoints are a proposed convention only; no responsive CSS or viewport behavior was present in the supplied evidence.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| xs        | <480px      | Single-column stacking, nav collapses to menu icon |
| sm        | 480–767px   | Product grid at 2 columns |
| md        | 768–1023px  | Product grid at 3 columns, nav partially expands |
| lg        | 1024–1279px | Full horizontal nav, 4-column grid |
| xl        | ≥1280px     | Max-width content container, generous section padding |

Touch targets should be a minimum of 44×44px for buttons and nav items (proposed, not measured). Below the `md` breakpoint, the nav-bar is recommended to collapse into a hamburger/drawer pattern, and product-card grids should reduce column count progressively. All responsive guidance here is a recommendation for implementation, not an observation of the live site's actual mobile behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS text and a color/font-family list, not from rendered pages, DOM inspection, or interaction testing. Several limitations apply: (1) A large portion of the supplied color palette originates from generic third-party libraries (Bootstrap-style alert classes, jQuery UI Smoothness theme, an Amazon-style button yellow) rather than confirmed Pact brand styling; only white canvas, ink text, and the green/terracotta/tan family were treated as plausible brand colors, and this mapping is inferred. (2) Additional font families in the evidence (Juana, GTEesti, Durer, Storyboo, Thistails-Regular) appear in the site's font list but no CSS rule in the supplied evidence assigns them a selector or role, so they are excluded from the typography tokens above. (3) All font sizes above 14px (the one confirmed body size) and all letter-spacing values are proposed, not measured. (4) No hover, focus, active, error, or disabled states were observed in the evidence; all such states in the components section are labeled proposed. (5) No responsive/mobile markup or breakpoint CSS was present; the responsive table is a generic recommendation. (6) Licensing and web-availability of the Averta typeface were not verified from the supplied evidence and would need confirmation before implementation.
