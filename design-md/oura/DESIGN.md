---
version: alpha
name: "Oura"
source_url: "https://ouraring.com"
captured_at: "2026-09-28T04:26:31.063630+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Oura's extracted palette centers on warm, low-contrast neutrals — a family of cream
  and putty tones (#f7f1e8, #ede9e4, #e7e0d9) that likely serve as canvas and section
  backgrounds — paired with a near-black ink (#1c1c1c/#19191c) used for text and
  primary actions. This restrained neutral base is punctuated by a small set of
  saturated accents (teal #00aca4, green #08833d, blue #1f72cd, plum #3e2242, deep
  navy #0b051d, red #d22c15, and softer rose/tan tones #e7a7c6/#c0865d). Given Oura's
  product line of health-score dashboards and ring finish options, these accents are
  inferred to encode health-metric states (readiness, sleep, activity) and/or ring
  color-swatch imagery rather than core UI chrome; no live component usage was
  observed.

  Typography draws on two declared families: AkkuratLL as the primary sans-serif for
  UI and body copy, and Editorial New as a serif reserved for display/editorial
  headlines — a pairing consistent with a premium wellness-tech brand voice. Sizes,
  weights, and the serif/sans split for specific headline levels are proposed
  interpretations, not measured layout. Rounded corners and spacing follow a compact,
  minimal-radius system suited to a clinical-but-warm aesthetic.

colors:
  primary: "#1c1c1c"
  ink: "#1c1c1c"
  body: "#19191c"
  canvas: "#ffffff"
  muted: "#6f6e6d"
  hairline: "#dedddb"
  surface-soft: "#f7f1e8"
  surface-card: "#ede9e4"
  on-primary: "#ffffff"
  accent-teal: "#00aca4"
  accent-plum: "#3e2242"
  accent-navy: "#0b051d"
  success: "#08833d"
  alert: "#d22c15"
  link: "#1f72cd"
  swatch-tan: "#e1ba8b"
  swatch-rose: "#e7a7c6"
typography:
  display-xl: {fontFamily: "Editorial New, serif", fontSize: "56px", fontWeight: 500, lineHeight: 1.05, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Editorial New, serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "AkkuratLL, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "AkkuratLL, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "AkkuratLL, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "AkkuratLL, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "AkkuratLL, sans-serif", fontSize: "15px", fontWeight: 600, lineHeight: 1.0, letterSpacing: "0.2px"}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  score-ring:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.title-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md}"

## Components
`button-primary` uses the near-black ink as fill with white text, matching the dark, low-key CTA style implied by the site's neutral-forward palette; hover/active states are proposed and not observed. `button-secondary` is an outlined variant on a hairline border for secondary actions like "Learn more" links. `text-input` sits on the slightly darker cream card surface with a thin hairline border, proposed for forms such as email capture. `nav-bar` is inferred from the `--menubar-height` custom property observed in CSS, indicating a fixed-height header; background and border treatment are proposed to match the light canvas. `hero` pairs the serif display type with a soft cream background, reflecting the editorial tone suggested by the "Editorial New" font token; exact hero layout was not observed. `product-card` uses a deeper cream surface with generous rounding, suited to ring/product imagery on an e-commerce PLP. `footer` is proposed as a dark navy block (from the observed `#0b051d`) with white text, a common pattern for premium DTC sites, though this contrast was not directly confirmed. `badge` and `score-ring` are category-appropriate components inferred from Oura's health-tracking product: small teal-filled chips or ring shapes likely represent readiness/sleep/activity scores, using the accent teal as a plausible metric-status color; other accents (green, red, blue) may represent additional score states but their exact application is unconfirmed.

## Responsive Behavior
This is a proposed recommendation, not measured site behavior, since no breakpoint or viewport CSS was captured beyond the fluid `--menubar-height` calc values.

| Breakpoint | Width       | Notes                                  |
|-----------|-------------|-----------------------------------------|
| xs        | <480px      | Single-column, stacked nav, full-width CTAs |
| sm        | 480–767px   | Two-column product grids begin          |
| md        | 768–1023px  | Nav collapses to hamburger; menubar height per observed calc |
| lg        | 1024–1439px | Full horizontal nav, multi-column hero  |
| xl        | ≥1440px     | Max-width content container, generous section padding |

Touch targets should be at least 44px in height for buttons and nav items; the observed `--menubar-height` fluid calc (`.0107 * 100vw + 50.48px`) suggests the header height scales slightly with viewport width, collapsing to a fixed 55–72px range at extremes — treat this as a hint, not a confirmed layout rule.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS custom properties, selector fragments, and a raw color/font list; no rendered page, computed layout, or DOM structure was observed. Role assignments (primary, muted, hairline, surface-soft/card) are inferred from typical usage patterns of neutral/cream and near-black tones in DTC e-commerce and are not confirmed against actual applied styles. The teal/green/blue/plum/red/rose accent colors' semantic purpose (health-score states vs. ring-color swatches vs. payment-icon branding) is speculative. Typography sizes, weights, and line-heights are proposed defaults, not extracted values, since no font-size or weight declarations were present in the supplied CSS rules beyond the family names. Interaction states (hover, focus, active, disabled) and any mobile-specific layout were not observed. Availability and licensing of "AkkuratLL" and "Editorial New" as web fonts have not been verified.
