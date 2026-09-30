---
version: alpha
name: "La Colombe"
source_url: "https://lacolombe.com"
captured_at: "2026-09-29T04:05:06.063000+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  La Colombe's storefront CSS shows a warm cream canvas (#fef9f4) paired with a deep
  navy ink (#0f223e) used for both running body copy and the primary button fill, per
  the .button and body selectors in bundle.theme.css. Grandway is the only font-family
  explicitly assigned to live UI text (body, buttons), so it anchors body-md, body-sm,
  caption, and button-md. Tiempos Text appears in the site's shipped font list without
  a confirmed selector; it is used here for display-xl/display-md as an inferred serif
  display pairing, not a verified heading style. The review-widget (Okendo) variables
  surface a secondary muted slate (#676986) and light border/surface tones (#dbdde4,
  #f7f7f8, #e5e5eb) that inform hairline, muted-text, and soft-surface roles across
  cards and inputs. A cluster of saturated palette values — deep red (#b02028),
  ochre-gold (#c4a84c), and bright yellow (#ffcf2a) — is proposed for seasonal badges,
  ratings, and promotional accents (e.g. "Pumpkin Spice", "Bundle & Save"), since the
  excerpt shows frequent promo callouts but no confirmed swatch-to-role binding.
  Radii and spacing follow a restrained scale: the observed .button has 0 radius while
  the Okendo button token uses 4px, so both are retained as distinct rounded roles
  rather than merged.

colors:
  primary: "#0f223e"
  ink: "#0f223e"
  canvas: "#fef9f4"
  body: "#0f223e"
  muted: "#676986"
  hairline: "#dbdde4"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#fef9f4"
  accent: "#b02028"
  accent-gold: "#c4a84c"
  accent-yellow: "#ffcf2a"
  surface-alt: "#f8f5f3"
  border-soft: "#e5e5eb"
typography:
  display-xl: {fontFamily: "Tiempos Text, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Tiempos Text, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Grandway, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.01em}
  body-md: {fontFamily: "Grandway, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.3, letterSpacing: -0.01em}
  body-sm: {fontFamily: "Grandway, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: -0.01em}
  caption: {fontFamily: "Grandway, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0}
  button-md: {fontFamily: "Grandway, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.3, letterSpacing: -0.01em}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  bundle-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.accent-gold}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    discountTypography: "{typography.body-sm}"
    discountColor: "{colors.accent}"

## Components

**button-primary** renders the site's confirmed `.button` style: navy fill, cream text, zero radius, Grandway type at 16px/400. This is the most directly observed component in the evidence.

**button-secondary** is a proposed outline variant sharing the same navy/cream pairing inverted, for lower-emphasis actions like "Shop All →" links; hover/active states are not observed and are proposed only.

**text-input** infers a light card surface with a thin hairline border, drawn from the Okendo review-widget border token (`#dbdde4`/`#e5e5eb`); no first-party form-field CSS was supplied.

**nav-bar** assumes the cream canvas continues into the header, using the `--header-height` custom properties observed in `:root` (111–135px across breakpoints) as evidence that a fixed-height header exists, though its visual styling is not confirmed.

**product-card** is inferred from repeated "Roast / Rating / Price" text patterns in the excerpt (e.g. "Fall Blend… 4.7… $21"); layout, elevation, and card chrome are proposed, not measured.

**hero** reflects the promotional banner text ("Pumpkin Spice", "Bundle & Save up to 20% OFF") using the display serif pairing as an inferred editorial treatment; no hero-specific selectors were in evidence.

**footer** reuses the primary navy as an inverted-contrast band; this is a proposed convention for coffee DTC sites and is not confirmed by supplied CSS.

**badge** uses the bright yellow accent for seasonal/limited callouts ("PSL is back"); color-to-role binding is proposed since no badge selector was supplied.

**search** and **bundle-card** are category-appropriate additions: search reuses the Okendo soft-surface token, and bundle-card supports the "Build your bundle" flow referenced in the page text, using the gold accent as a border cue for savings framing.

## Responsive Behavior

Recommended breakpoints (not measured):

| Breakpoint | Width | Notes |
|---|---|---|
| sm | 0–639px | Single-column product grid, collapsed nav to hamburger |
| md | 640–1023px | 2-column product grid |
| lg | 1024–1279px | 3–4 column grid, full nav visible |
| xl | 1280px+ | Max-width container, 4+ column grid |

Touch targets should be at least 44px tall for buttons and nav items. The header height custom properties (111px–135px) observed in `:root` suggest the live site adjusts header height across breakpoints/announcement-bar states, but exact collapse behavior, sticky logic, and mobile menu treatment were not observed and are recommendations only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered layout, hover/focus states, animation, or JavaScript-driven interaction was observed. Font-role mapping is uncertain: Grandway is confirmed on `body`/`.button`, but Tiempos Text, Carrosserie-Medium, TAY Birdie, BNPelicanScript, and the `draftlattesans` family appear only in the shipped font list without selector confirmation, so heading and product-labeling typography here is inferred, not verified. All pixel sizes in the typography scale beyond the confirmed 1rem/14px tokens are proposed, not measured. Color-to-role assignments beyond the `.button` and Okendo `:root` tokens (e.g. accent-yellow, accent-gold, accent for badges) are plausible inferences from promotional page-text context, not confirmed swatches. Custom font licensing/availability (Grandway, Tiempos Text, Carrosserie, TAY Birdie, BNPelicanScript, draftlattesans) was not verified and should be checked before implementation. Mobile menu structure, cart drawer, and subscription/membership flows mentioned in page text were not present in supplied CSS and are therefore undesigned here.
