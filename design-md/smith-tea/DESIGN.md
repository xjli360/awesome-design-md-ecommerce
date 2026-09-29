---
version: alpha
name: "Smith Tea"
source_url: "https://smithtea.com"
captured_at: "2026-09-28T04:31:45.828257+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Steven Smith Teamaker's storefront evidence points to a warm, tea-shop
  palette built on muted browns and neutral sand tones, with a dark ink for
  text and small pops of botanical and accent color. Body copy is set in
  Janson, a serif referenced directly in base.css for body and heading
  elements, giving the brand an editorial, craft-goods feel; a secondary
  sans-serif (Figtree, present in the observed font stack) is inferred for
  UI chrome such as buttons, form fields, and navigation, since Shopify
  theme variables reference an unconfirmed "avenir" token that could not be
  verified in the supplied evidence. Primary actions use a brown
  (`--color-brown-700`-style) fill with white text and uppercase, tracked
  button type, matching the `.button` rule's letter-spacing and weight.
  Sand/cream surfaces (`#f5f3ee`, `#ebe7dc`, `#faf9f6`) suggest a light,
  paper-like canvas, while a brick red and sage green appear positioned as
  secondary accent colors, plausibly for sale badges or botanical callouts,
  though this semantic role is inferred rather than confirmed. A blue pair
  (`#1990c6`/`#136f99`) is only verified for Shopify's accelerated-checkout
  button, not for general brand use. Radii, spacing, and most type sizes
  below are proposed conventions layered onto this evidence, not measured
  site values.

colors:
  primary: "#72654e"
  ink: "#212121"
  canvas: "#f5f3ee"
  body: "#3e3d38"
  muted: "#787f82"
  hairline: "#e0e0df"
  surface-soft: "#ebe7dc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#a23434"
  sage: "#616f53"
  gold: "#f4a735"
  interactive: "#1990c6"
  interactive-hover: "#136f99"
  border-strong: "#000000"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Janson, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Janson, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Janson, serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 1px}
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
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  variant-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBorderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** reflects the observed `.button,.button--primary,.btn`
rule: brown fill, white text, uppercase tracked type, and a hairline
border. This is a confirmed structural pattern; the exact brown hex used by
`--color-brown-700` was not directly resolvable, so `{colors.primary}` is
an evidence-informed approximation from the supplied palette.

**button-secondary** is proposed for lower-emphasis actions (e.g. "Learn
more"), using a transparent fill with a dark hairline border, mirroring
the black border/text seen on the generic `#button` selector fallback.

**text-input** is a proposed pattern for newsletter, search, and account
forms; no dedicated input CSS was supplied, so padding, radius, and border
color are inferred from general theme neutrals.

**nav-bar** is proposed as a light sand bar with dark ink text and a thin
hairline division, consistent with the sand-neutral canvas variables
referenced in `body`, though no nav-specific selectors were supplied.

**product-card** is proposed for tea listing grids, pairing a serif title
(matching the observed `h1,h2` Janson rule) with a smaller sans price
line; card chrome (border, radius, padding) is inferred, not measured.

**hero** is proposed as a full-width introductory band using the softer
cream surface tone, large serif display type, and generous section
spacing; no hero-specific CSS was in evidence.

**footer** is proposed with an inverted brown background and white text,
reusing the primary/on-primary pair for brand consistency at the page
end; this inversion is a design choice, not an observed rule.

**badge** is proposed for "new," "limited," or origin labels, using the
gold accent color pulled from the palette with a pill radius; no badge CSS
was supplied.

**search** is proposed as a bordered field with a muted icon color,
reusing text-input conventions; unconfirmed by direct selectors.

**variant-selector** is a category-appropriate proposed component for tea
size/flavor pickers, using the soft surface tone at rest and the primary
brown as a selected-state border; no such selector was present in the
supplied CSS.

## Responsive Behavior

The following breakpoints are a recommendation for implementation, not a
measured observation of smithtea.com's actual responsive behavior:

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| xs        | 0–479px    | Single-column, stacked nav, full-width buttons |
| sm        | 480–767px  | Two-column product grid |
| md        | 768–1023px | Three-column product grid, inline nav begins |
| lg        | 1024–1279px| Four-column grid, full nav bar |
| xl        | 1280px+    | Max-width content container, generous section padding |

Touch targets should be at least 44px in the block dimension, consistent
with the `min-height:clamp(25px, …, 55px)` pattern observed on Shopify's
accelerated checkout button. Navigation and filter panels are assumed to
collapse into a drawer or accordion below `md`, but this collapse behavior
was not observed and is a conventional e-commerce recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/asset evidence, not a rendered or
interactive audit of smithtea.com. Specific gaps include: (1) the resolved
hex values behind theme variables such as `--color-brown-700`,
`--color-sand-100`, and `--color-sand-500` were not directly present in
the supplied evidence, so color role assignments (primary, canvas, body)
are best-fit inferences from the observed palette; (2) the `--font-family-
avenir` variable referenced for buttons could not be matched to a
confirmed font name in the supplied `font_families` list, so Figtree is
used as a plausible sans-serif substitute, and its licensing/availability
as a webfont is unverified; (3) all sizing, spacing, radius, and
breakpoint values are proposed conventions rather than measured layout
data; (4) no interaction states (hover, focus, active, disabled), mobile
navigation patterns, or actual page layouts were observed; (5) some
palette entries (e.g. blues from the Shopify accelerated-checkout widget,
a purple from a third-party compliance script) are third-party UI colors,
not confirmed brand colors, and were excluded from primary role
assignments where possible.
