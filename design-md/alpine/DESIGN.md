---
version: alpha
name: "Alpine"
source_url: "https://alpine-usa.com"
captured_at: "2026-09-28T04:59:10.992717+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Alpine's public site presents a technical, performance-oriented car-audio catalog built on a
  cool institutional blue (#00549a) paired with near-black ink (#212121) and a white canvas.
  Supporting neutrals (#f0f0f0, #fafafa, #d9d9d5, #777777) suggest a restrained light-mode UI with
  soft card and hairline treatments, inferred from repeated near-white and light-gray values in the
  palette. A saturated red (#d93025) and a green (#32be3f) appear in the extracted palette and are
  interpreted as promotional/alert and success/in-stock accents respectively; these roles are
  inferred, not confirmed by observed component usage. Typography is bifurcated: condensed heavy
  display faces (Dharma Gothic E Bold, HN Bold Extended, HN Heavy Extended) drive buttons and
  large headings, matching the one directly observed CSS rule for `.globalButton__arrow`
  (Dharma Gothic E Bold, 18px, weight 700, letter-spacing .02em), while rounder humanist families
  (Circular Book/Bold/Black, Nunito Sans, Open Sans) are inferred for body and secondary copy.
  This spec proposes a spacing/radius scale and component set consistent with an automotive
  parts-and-electronics storefront (fitment lookup, product cards, promo badges) without claiming
  unobserved layout or interaction behavior.

colors:
  primary: "#00549a"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#777777"
  hairline: "#d9d9d5"
  surface-soft: "#f0f0f0"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-alert: "#d93025"
  success: "#32be3f"
  ink-deep: "#003b6b"
  surface-dark: "#354558"
typography:
  display-xl: {fontFamily: "Dharma Gothic E Bold, Arial Black, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "HN Bold Extended, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Circular Bold, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Circular Book, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Circular Book, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Dharma Gothic E Bold, Arial Black, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.125, letterSpacing: 0.02em}
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
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
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
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fit-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"

## Components

**button-primary** — The solid blue CTA (`{colors.primary}` on `{colors.on-primary}`) mirrors the one
directly observed `.globalButton__arrow` rule, including its condensed 18px display typography and
angular arrow accent. Hover-state color swap to ink is documented in CSS but treated here as a
proposed default rather than a fully verified interaction across all button contexts.

**button-secondary** — An outlined inverse of the primary button, using primary blue for border and
text on a white fill. This variant is inferred from the "white" and "black" arrow-button modifier
classes present in the CSS, which imply a small family of button color variants beyond the blue
default.

**text-input** — A minimal bordered field using the hairline gray for its outline and body copy
typography. No native input styling was present in the supplied CSS; this pattern is proposed based
on conventional storefront search/lookup needs.

**nav-bar** — A white top bar with dark ink text and a light hairline underline, sized to hold
category links such as those listed in the page text (Car Audio, Marine, Off-Road, Alpine Vehicles).
Structure and behavior are proposed; no header layout rules were present in the extracted CSS.

**product-card** — A soft off-white card (`{colors.surface-card}`) with a light hairline border,
housing a bold title and smaller body copy for spec/price text. Card elevation, image aspect ratio,
and hover treatment are not present in the supplied evidence and are proposed conventions for a
parts catalog grid.

**hero** — A deep-blue banner (`{colors.ink-deep}`) intended for promotional messaging such as the
"Back to Cool Sale" banner referenced in the page text, using the largest display type for headline
impact. Exact hero imagery, overlay, and content width are not observed.

**footer** — A dark slate band (`{colors.surface-dark}`) carrying the multi-column link groups implied
by the page text (Company, Support, Store Locator, legal links). Column layout and link styling are
proposed, not measured.

**badge** — A small pill using the alert red for sale/promo labels (e.g., "25% OFF," "Up to $700 OFF")
referenced repeatedly in the page text. Color role is inferred from the presence of a saturated red
in the palette; no badge component markup was directly observed.

**search / vehicle-fit-selector** — A light, bordered lookup module intended for the "See products
that fit your vehicle" fitment tool mentioned in the page copy, distinct from a general text search.
Its layout, field count, and validation states are proposed and not confirmed by any supplied
selector.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | 0–599px     | Single-column stacks; nav collapses to a hamburger/drawer pattern |
| tablet    | 600–959px   | Two-column product grids; hero retains full-width banner |
| desktop   | 960–1279px  | Three/four-column product grids; full horizontal nav |
| wide      | 1280px+     | Max-width container with generous side padding (`{spacing.xxl}`) |

Touch targets should be at minimum 44px tall, consistent with the button padding proposed above.
Navigation and fitment-selector collapse into modal or accordion patterns on mobile — this is a
proposed pattern only; no mobile DOM or media-query behavior was present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was drawn from a single static CSS/text extraction; no rendered screenshots, computed
  styles, or DOM structure were available, so layout, spacing rhythm, and component composition are
  largely inferred rather than observed.
- Several near-duplicate blues (e.g., #003b6b, #0e55a0, #09529e, #02529b) appear in the raw palette;
  only `#00549a` was tied to an observed selector, so remaining blues were consolidated or omitted
  rather than assigned speculative roles.
- Green (#32be3f) and additional reds (#f44236, #cf422b) exist in the palette but no selector
  confirms their functional use; success/alert roles assigned here are inferred guesses.
- Font availability and licensing for Dharma Gothic E Bold, HN Bold/Heavy Extended, Circular
  Black/Bold/Book/Light, and brother-1816 were not verified; fallbacks to generic sans-serif are
  specified per family.
- No hover, focus, active, or disabled states were observed beyond the single documented button
  hover swap; all other interaction states in this spec are proposed defaults.
- Mobile/tablet layout, navigation collapse behavior, and touch interactions were not observed and
  are presented only as recommendations.
