---
version: alpha
name: "Crowd Cow"
source_url: "https://crowdcow.com"
captured_at: "2026-09-28T05:01:58.839740+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Crowd Cow's supplied CSS evidence points to a warm, editorial palette built on deep neutrals and a
  butcher-shop burgundy. The near-black #131313 and soft off-white #f4f3ef/#efece8 tones form the
  primary canvas and text pairing, while #450002, #581a1b and #6a3335 read as a layered maroon family
  likely reserved for primary actions, farm badges, and accent typography — a fitting nod to the
  "craft meat" positioning. #ef7857 appears as a warmer coral accent, plausibly used for promotional
  callouts ("Free favorites," "Claim My Offer") given its contrast against the neutral surfaces.
  Sage/olive tones (#303b1e, #59624b, #bbcb9f) are inferred as category or farm-tag accents based on
  their earthy, agricultural association, though no selector evidence confirms this role.
  Typography is class-driven rather than font-declared: `.text-header-*` classes reference a
  `--font-family-display` token at bold weights (700) with tight, near-1.1 line-heights, while
  `.text-body-*` classes reference `--font-family-body` at regular weight with slightly looser
  tracking. The observed font stack (Archivo Narrow, Oswald, Roboto Condensed, Noto Sans, Helvetica
  Neue, Arial) suggests a condensed display face paired with a humanist sans body face; the exact
  assignment is inferred, not confirmed by a font-family declaration in the supplied rules. Buttons
  show explicit `border-radius: 0`, suggesting a squared, no-radius button language rather than
  pill-shaped CTAs.

colors:
  primary: "#450002"
  primary-deep: "#581a1b"
  primary-muted: "#6a3335"
  accent: "#ef7857"
  category-sage: "#59624b"
  category-sage-light: "#bbcb9f"
  ink: "#131313"
  canvas: "#ffffff"
  body: "#424242"
  muted: "#717171"
  muted-light: "#a1a1a1"
  hairline: "#e4e0d8"
  surface-soft: "#f4f3ef"
  surface-card: "#efece8"
  surface-alt: "#e9e6e0"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 0.9, letterSpacing: 0em}
  display-md: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.0075em}
  title-md: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.0075em}
  title-sm: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.02em}
  body-lg: {fontFamily: "Noto Sans, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.01em}
  body-md: {fontFamily: "Noto Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.0075em}
  body-sm: {fontFamily: "Noto Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.0075em}
  caption: {fontFamily: "Noto Sans, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.01em}
  button-md: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.02em}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    height: "proposed 64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-lg}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.category-sage-light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  farm-provenance-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary-muted}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders CTAs like "Claim My Offer" and "Start" using the deep burgundy fill against white text, matching the `.btn-primary` class's bold, tightly-tracked display type and squared corners (observed `border-radius: 0` on form controls, extended here as a proposed default).

**button-secondary** proposes an outlined variant of the same burgundy for lower-emphasis actions (e.g. "Shop All," "View All Farms"), reusing the primary hue on a transparent background rather than introducing a new color.

**text-input** covers search and account fields; no explicit input styling was observed beyond the reset (`font: inherit; border-radius: 0`), so border, radius, and padding values here are proposed defaults consistent with the button system's squared aesthetic.

**nav-bar** is inferred from the presence of `--z-navbar` and category-heavy navigation text ("Shop," "Cooking," "About"); background/text colors follow the canvas/ink pairing, though exact height and sticky behavior are not confirmed by the evidence.

**product-card** supports listings such as Wagyu cuts, seafood, and limited drops, using the muted card surface (`#efece8`) to separate product tiles from the page canvas, with condensed display type for cut names and body type for pricing — proposed structure, not directly observed markup.

**hero** models the homepage banner ("Your Table Just Got an Upgrade") on the soft neutral surface with large display type and a primary CTA; copy and CTA text are drawn from the supplied excerpt, but exact hero sizing/layout is inferred.

**footer** is proposed as a dark, ink-colored band (inverting the light canvas) to house the long link list (Terms, Privacy, Sitemap, Moolah! Rewards) visible in the evidence; this color inversion is a design proposal, not a confirmed observation.

**badge** supports small labels like "Limited Drops" or category tags, using the lighter sage tone as a soft, food-adjacent accent color, pill-shaped per typical badge conventions — inferred styling.

**search** models the header "Search..." field using the soft surface tone and hairline border for a low-contrast, unobtrusive treatment consistent with the neutral palette.

**farm-provenance-card** is a category-appropriate component for Crowd Cow's farm-sourcing narrative ("Little Belt," "Home Place Pastures," "Margaret River Wagyu"), pairing a muted maroon accent with card surface and condensed titles to echo the site's repeated farm-storytelling content blocks.

## Responsive Behavior
Proposed breakpoints (not measured from live layout): mobile ≤640px (single-column product grids, stacked nav collapsing behind a menu icon, `--container-inline-padding-mobile: 20px` per observed token), tablet 641–1024px (2–3 column grids, `--container-inline-padding-desktop: 40px` engaging near the upper end), desktop ≥1025px (full multi-column grids, persistent nav). Touch targets should target a minimum 44px hit area for buttons and nav items; primary CTA buttons should collapse to full-width on mobile. This section is a recommendation based on the two observed padding tokens, not an observed responsive implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction did not expose actual `font-family` values behind `--font-family-display` / `--font-family-body`; the Archivo Narrow/Noto Sans pairing is inferred from the supplied font list and typographic character (condensed bold headers vs. regular body), not confirmed.
- Semantic color roles (primary vs. accent vs. category-tag) are inferred from hue grouping and brand context (premium meat/farm sourcing), not from selector-level evidence tying specific hex values to specific UI roles.
- Spacing scale and rounded scale beyond the two observed container-padding tokens (`20px`/`40px`) and the observed `border-radius: 0` on form controls are proposed conventions, not measured from the site's actual component CSS.
- No interaction states (hover, focus, active, disabled), mobile menu behavior, or responsive grid breakpoints were present in the supplied evidence; all such behavior above is proposed, not observed.
- Custom font licensing/availability (e.g., whether Archivo Narrow/Oswald/Noto Sans are self-hosted, Google Fonts, or system-substituted) was not verified from the supplied evidence.
