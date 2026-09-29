---
version: alpha
name: "Remarkable"
source_url: "https://remarkable.com"
captured_at: "2026-09-28T04:27:25.795061+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  reMarkable's marketing site pairs a paper-like neutral canvas (#fcfbf8, #f8f7f6) with near-black ink (#211e1c) for a restrained, editorial reading feel appropriate to a paper-tablet brand. A single saturated blue family (#003bb2, #1142d4, #2559f4, #99c3ff, #e9f2ff) supplies the primary interactive accent — CSS exposes a --color-pen-blue token feeding light-theme pictograms, so blue is treated here as the confirmed brand accent for links, CTAs, and focus states. A red (#da0810) and a muted sage-green family (#5f6d5f, #e6eae6) also appear in the palette and align with the site's data-theme=light-green/light-red/dark-* attributes; these are interpreted as inferred accent themes for alternating content sections rather than universal brand colors. Warm neutral grays (#6e635e, #37322f, #d2cabc) round out body text and borders. Typography uses a custom reMarkableSans for UI and reMarkableSerif for editorial emphasis, both falling back to system sans/serif (Arial, Helvetica, Georgia, Book Antiqua) — availability and licensing of the custom faces are unverified. Rounding is treated as minimal/sharp, since the only observed radius rule resets inputs to 0.

colors:
  primary: "#003bb2"
  ink: "#211e1c"
  canvas: "#fcfbf8"
  body: "#37322f"
  muted: "#6e635e"
  hairline: "#211e1c1a"
  surface-soft: "#f8f7f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue-bright: "#2559f4"
  accent-blue-mid: "#1142d4"
  accent-blue-light: "#99c3ff"
  accent-blue-tint: "#e9f2ff"
  accent-blue-tint-strong: "#cce1ff"
  accent-red: "#da0810"
  accent-red-tint: "#f7979b"
  accent-green: "#5f6d5f"
  accent-green-tint: "#e6eae6"
  divider-strong: "#211e1c33"
  overlay-scrim: "#211e1cbf"
typography:
  display-xl: {fontFamily: "reMarkableSerif, Georgia, serif", fontSize: 56px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "reMarkableSerif, Georgia, serif", fontSize: 36px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "reMarkableSans, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "reMarkableSans, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "reMarkableSans, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "reMarkableSans, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "reMarkableSans, Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.1px}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: "52px"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.accent-blue-light}"
    padding: "{spacing.xxl} {spacing.xl}"
    typography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.accent-blue-tint}"
    textColor: "{colors.accent-blue-mid}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  paper-theme-panel:
    backgroundColor: "{colors.accent-green-tint}"
    textColor: "{colors.accent-green}"
    accentBorder: "{colors.accent-red-tint}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    typography: "{typography.body-md}"

## Components

**button-primary** is the core call-to-action (e.g. "Shop", "Buy now") using the confirmed pen-blue accent as a solid fill; hover/pressed/disabled states are proposed, not observed. **button-secondary** offers an outlined variant on light backgrounds for lower-priority actions like "Learn more," reusing the same blue for border and label to keep hierarchy consistent without adding new hues.

**text-input** follows the site's own reset (border-radius: 0, transparent background) as evidence that form fields favor a flat, minimal treatment over pill or rounded styling; focus-ring color is proposed as the primary blue.

**nav-bar** sits on the paper-toned canvas with a hairline bottom border; the 52px height is drawn directly from an observed `--ark-navbar-height` token, while a 67px variant appears at a presumably wider viewport — both are cited from CSS, not visually confirmed layout.

**product-card** represents device/tile listings (tablets, marker accessories) with a plain white surface separated from the cream page background, a subtle border, and generous internal padding suited to product photography; hover elevation is proposed.

**hero** anchors landing/product pages with large serif-styled display type over the paper canvas, echoing the brand's "digital paper" positioning; exact hero copy and imagery placement are not observed and are treated as conventional e-commerce hero structure.

**footer** inverts to the near-black ink color with light text and blue links, mirroring common dark-footer patterns; column layout and link groupings are inferred, not extracted from markup.

**badge** is a small pill for labels such as "New" or feature tags, using the light blue tint background with the mid-blue text color pulled from the accent scale; this pairing is proposed for accessibility contrast, not measured.

**search** proposes a flat, low-emphasis input styled like text-input but on the soft off-white surface, for a header search affordance; presence and exact placement of a search feature on the live site were not confirmed in the supplied evidence.

**paper-theme-panel** is a category-specific, evidence-grounded component: the CSS defines `data-theme` variants (`light-green`, `light-red`, `light-neutral`, and dark counterparts), strongly suggesting the site supports color-themed content blocks (e.g. device color options or seasonal sections). This panel pattern uses the green-tinted surface with a soft red accent border as one plausible theme combination; other theme permutations (red-on-neutral, dark variants) are proposed extensions of the same token system.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Compact | < 640px | Single-column stacks, nav collapses to a menu icon, `--ark-navbar-height` ~52px |
| Medium | 640–1024px | Two-column product grids, nav-bar may expand toward 67px |
| Wide | > 1024px | Multi-column hero/footer grids, side margins approaching the observed 12.5% margin-width token |

Touch targets should be at least 44×44px for buttons and nav items. Collapse product-card grids from 3–4 columns down to 1 column below the compact breakpoint. All spacing should scale using the `{spacing.*}` tokens rather than fixed pixel overrides.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/color/font extraction only; no live page was rendered or interacted with, so component states (hover, focus, active, disabled), animations, and mobile navigation behavior are proposed, not observed. Semantic role assignments — which exact hex maps to "primary CTA" versus "link" versus "themed accent" — are inferred from token naming patterns (e.g. `--color-pen-blue`) and typical usage conventions, not from rendered screenshots. Type sizes, line-heights, and letter-spacing in the scale are proposed engineering defaults; only the font-family names (`reMarkableSans`, `reMarkableSerif`, and their fallbacks) are directly observed in CSS. The reMarkableSans/Serif custom fonts' licensing and public availability are unverified. Border-radius values are inferred from a single input-reset rule (`border-radius:0`) and general minimal-UI convention, not a full corner-radius audit. The green/red/neutral theme system is confirmed to exist via `data-theme` selectors, but which content sections actually apply each theme was not observed.
