---
version: alpha
name: "ADAM Audio"
source_url: "https://www.adam-audio.com"
captured_at: "2026-09-28T04:08:54.979849+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from ADAM Audio's WordPress-based markup and a
  legacy Bootstrap-derived stylesheet (main.css) serving the public site. The
  evidence shows a neutral, high-contrast system: near-white canvas (#ffffff,
  #f8f8f8), dark charcoal ink (#333333, #1d1d1d), and a near-black button
  color (#32373c) used consistently for primary actions and file-download
  buttons, with full-pill border-radius (9999px). A muted gray (#777777) marks
  secondary/small text, and thin hairlines (#dddddd, #e4e4e4) separate content
  blocks. A gold tone (#c89e0e) appears in the palette and is treated here as
  an inferred brand accent, evoking ADAM Audio's signature ribbon-tweeter
  hardware, though its exact site usage was not confirmed in the supplied
  rules. Typography is explicitly "Helvetica Neue", Helvetica, Arial,
  sans-serif at the body level (14px/1.43), while DINPro and DINEngschriftStd
  appear as available font-family declarations and are proposed here for
  display/heading roles pending verification. The resulting system favors a
  precise, engineering-driven, monochrome aesthetic with restrained accent
  color, appropriate for a professional audio-hardware brand.

colors:
  primary: "#32373c"
  ink: "#1d1d1d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f8f8f8"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-gold: "#c89e0e"
  dark-surface: "#313131"
  border-strong: "#cccccc"
  danger: "#dc3232"
  info-blue: "#007cba"
typography:
  display-xl: {fontFamily: "DINPro, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "DINPro, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.428571429, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.1, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripeColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** reflects the observed `.wp-block-button__link` / `.wp-element-button` rule set: dark charcoal fill (#32373c), white text, no border, and a full pill radius (9999px) with generous horizontal padding (`calc(1.333em + 2px)`), approximated here with the spacing scale. This is the confirmed primary call-to-action pattern.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn more," "Compare"), using the same pill radius and typography as the primary button but with a transparent fill and hairline border, inverting on hover — hover/focus states are proposed, not observed.

**text-input** is inferred from the shared `font: inherit` reset on form elements; no explicit border or focus styling was present in the supplied rules, so hairline borders and a small radius are proposed defaults consistent with the neutral palette.

**nav-bar** is a proposed structural component representing the top-level product/category navigation implied by a studio-monitor catalog site; background and hairline divider are drawn from the observed near-white/gray surfaces, but actual header layout, logo placement, and sticky behavior were not present in the evidence.

**product-card** is proposed for monitor/product listing grids, using the light gray surface (#eeeeee, matching `.has-very-light-gray-background-color`) as a card background against the white canvas, with a hairline border for separation. Card imagery, price, and CTA placement are not observed and remain proposed.

**hero** uses the dark surface color (#313131, from `.has-very-dark-gray-background-color`) as a full-bleed background for landing/product intro sections, paired with the large display type. Actual hero imagery, video, or copy treatment on adam-audio.com was not captured in this evidence and is proposed only.

**footer** is proposed using the darkest ink tone with muted gray text (#777777, matching the observed `small`/`.h6 small` color), consistent with a utilitarian, link-dense footer common to manufacturer sites; column structure is not observed.

**badge** applies the gold accent (#c89e0e) as a small pill label — proposed for flagging "New," "Award-Winning," or series tags on product tiles; no badge markup was present in the supplied CSS, so this is an inferred pattern reusing an existing palette color.

**search** is a proposed pill-shaped input reusing the soft surface and full-radius tokens, intended for a product/support search field; no search component markup was observed.

**spec-table** is a category-appropriate proposed component for technical specification comparisons (frequency response, driver size, wattage) common to studio-monitor product pages, reusing the confirmed `.table-striped > tbody > tr:nth-of-type(odd)` zebra-stripe color (#f9f9f9, mapped to `{colors.surface-soft}`) with hairline row dividers.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not measured site behavior, since no media queries were present in the supplied evidence:

| Breakpoint | Width      | Notes (proposed)                          |
|------------|-----------|---------------------------------------------|
| xs         | <576px    | Single-column stack, nav collapses to menu icon |
| sm         | 576–767px | Two-column product grids                   |
| md         | 768–991px | Nav-bar expands inline; 2–3 column cards   |
| lg         | 992–1199px| Full horizontal nav; 3–4 column cards      |
| xl         | ≥1200px   | Max-width content container; 4+ column grids |

Touch targets should be a minimum of 44×44px for buttons and nav items, per common accessibility guidance (proposed, not sourced from the site). Below `md`, the nav-bar and search components should collapse into an overlay/drawer pattern; this collapse behavior was not observed and is a UX-standard recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically from CSS/HTML sources; no rendered layout, imagery, spacing measurements, or interaction states (hover, focus, active, disabled) were observed.
- The role of `#c89e0e` as a brand accent is inferred from its presence in the palette and thematic association with the brand's ribbon-tweeter hardware; its actual usage location on the site is unconfirmed.
- Heading typography (DINPro, DINEngschriftStd, MinionPro) is listed among observed font-family declarations but the CSS rule for `h1–h6` explicitly sets `font-family: inherit`, so it is uncertain whether these custom fonts are actually applied to visible headings or reserved for other assets (e.g., PDFs, print, or legacy pages).
- Custom font licensing and web-font availability (DINPro, DINEngschriftStd, MinionPro) were not verified; fallback to system sans-serif is assumed for safety.
- All pixel sizes in the typography scale beyond the confirmed `14px`/`16px`/`42px` values are proposed estimates, not measured from rendered pages.
- Component patterns for nav-bar, hero, product-card, footer, badge, search, and spec-table are proposed structural interpretations based on category norms for a studio-monitor manufacturer site, not confirmed DOM structures.
- Mobile/tablet layout, collapse breakpoints, and touch-target sizing are UX recommendations, not measured from adam-audio.com.
