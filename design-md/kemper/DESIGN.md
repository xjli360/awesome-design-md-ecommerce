---
version: alpha
name: "Kemper"
source_url: "https://www.kemper-amps.com"
captured_at: "2026-09-28T04:07:16.281581+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kemper's public site renders as a dark-themed interface: the observed
  body rule sets a near-black canvas (#1a1a1a) with white body copy (#ffffff)
  set in 'Lato', a humanist sans-serif, at 14px/1.43 line-height. Heading
  elements inherit the body family at a medium 500 weight with a tight 1.1
  line-height, consistent with a compact, technical-product tone suited to
  an amp/cabinet modeling brand. A muted grey (#919191) is confirmed for
  small/secondary text. Beyond these confirmed rules, the supplied palette
  contains a cluster of muted greens (#33715b, #8baea2, #aec7bd, #475b57)
  and a warm coral (#f17e6f) that recur alongside greys (#232830, #3a3a3a,
  #333333, #cccccc, #dddddd); these are treated here as the inferred brand
  accent and neutral-surface system, since no explicit selector ties them to
  a specific brand role. A large set of recognizable third-party brand hues
  (Facebook blue, Instagram magenta, Twitter/X blue, Pinterest red, Spotify
  green, etc.) also appears in the evidence; these are social-share icon
  colors, not Kemper brand colors, and are excluded from the palette below.
  Bootstrap-style alert colors (success/warning/danger/info) are present
  verbatim and are carried through as semantic status colors only. The
  interpretation below proposes a dark, restrained, music-gear-appropriate
  system built from these confirmed and inferred tokens; sizing, radii, and
  spacing are proposed unless otherwise noted.

colors:
  primary: "#33715b"
  ink: "#ffffff"
  canvas: "#1a1a1a"
  body: "#dddddd"
  muted: "#919191"
  hairline: "#333333"
  surface-soft: "#232830"
  surface-card: "#3a3a3a"
  on-primary: "#ffffff"
  accent: "#f17e6f"
  sage: "#aec7bd"
  sage-deep: "#8baea2"
  forest: "#475b57"
  border-light: "#cccccc"
  success: "#3c763d"
  success-bg: "#dff0d8"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  danger: "#a94442"
  danger-bg: "#f2dede"
  info: "#31708f"
  info-bg: "#d9edf7"
typography:
  display-xl: {fontFamily: "'Lato', sans-serif", fontSize: "48px", fontWeight: 500, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Lato', sans-serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.1, letterSpacing: "0px"}
  title-md: {fontFamily: "'Lato', sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'Lato', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.42857143, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Lato', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "'Lato', sans-serif", fontSize: "11px", fontWeight: 400, lineHeight: 1, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Lato', sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.3px"}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sage-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rowStripeColor: "#f9f9f9"
    rowHoverColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary** uses the inferred brand green as its fill with white text, reflecting the dark canvas needing a clearly legible, higher-contrast call-to-action; hover/active states (e.g., a darkened or `forest` fill) are proposed, not observed.

**button-secondary** is an outline treatment against the dark background, using the hairline grey for its border so it reads as a lower-emphasis action beside the primary green button; this pairing is proposed.

**text-input** sits on the darker card surface rather than pure black, borrowing the confirmed neutral grey (#3a3a3a) so form fields remain distinguishable on the dark canvas; focus-ring styling is proposed and unobserved.

**nav-bar** is modeled as a persistent dark header matching body canvas color, with body-toned link text and a hairline division from page content; sticky/scroll behavior is not confirmed from static CSS.

**product-card** (for amp/cabinet/profile listings) uses the soft dark surface tone with generous padding, reserving the coral accent for a small highlight (e.g., "new" or featured tag); card elevation/shadow is proposed only.

**hero** reuses canvas and ink tokens at large display scale, with the primary green available as an accent underline or button anchor; no hero copy or imagery was present in the supplied evidence, so exact composition is inferred from typical product-marketing conventions.

**footer** uses the surface-soft background with muted-grey (#919191, confirmed small-text color) body copy and hairline rules between columns, consistent with the site's confirmed small-text styling rule.

**badge** applies the secondary sage-deep green at full pill radius for compact status labels (e.g., firmware version, "beta"), an inferred pattern not tied to a specific observed selector.

**search** mirrors the text-input styling but is called out separately for a persistent product/profile search affordance; no search-specific selector was present in the evidence, so this is a proposed component.

**spec-table** directly reflects the observed Bootstrap table rules: odd-row striping at #f9f9f9, hover state at #f5f5f5/#e8e8e8, and semantic success/warning/danger/info row backgrounds taken verbatim from the supplied CSS — useful for amp/cabinet spec comparisons or firmware-version tables.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| xs | <576px | Single-column stack; nav collapses to a toggled menu; touch targets ≥44px |
| sm | 576–768px | Two-column product grids begin; spec-table becomes horizontally scrollable |
| md | 768–992px | Nav-bar expands inline; hero copy and media sit side-by-side |
| lg | 992–1200px | Full multi-column product/cabinet grids; footer becomes multi-column |
| xl | ≥1200px | Max-width content container; additional whitespace via `{spacing.section}` |

Touch targets should maintain a minimum 44×44px hit area on interactive elements (buttons, nav items, table row actions). Collapse patterns (hamburger nav, accordioned spec tables) are proposed conventions for a dark, information-dense product site and were not verified from the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/color/font extraction only; no rendered page, DOM structure, or interaction states were observed. Layout composition (grid structure, hero content, nav markup) is inferred from general product-site conventions, not from captured HTML. Border-radius and spacing values are proposed defaults, as no radius or margin/padding rules were present in the supplied evidence. The role of several palette colors (e.g., #33715b, #f17e6f, #8baea2, #aec7bd) as "brand" vs. incidental is an inferred mapping based on recurrence and plausibility, not a confirmed selector-to-role binding. Numerous supplied hex values (Facebook, Instagram, Twitter/X, Pinterest, Spotify, Google-brand blues/reds) were identified as third-party social-icon colors and deliberately excluded from the brand token set. Font availability and licensing for 'Lato' (and any secondary faces like 'proxima-nova' seen in the raw font list but not confirmed by a body/heading rule) were not verified and should be confirmed before production use. Mobile/touch interaction patterns, hover/focus states, and animation are entirely proposed and unobserved.
