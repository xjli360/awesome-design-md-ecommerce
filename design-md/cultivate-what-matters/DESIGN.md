---
version: alpha
name: "Cultivate What Matters"
source_url: "https://cultivatewhatmatters.com"
captured_at: "2026-09-29T04:03:39.569460+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation reads Cultivate What Matters as a warm, editorial goal-planning brand built on
  a bright magenta-pink identity (#e62e89, reinforced by the Judge.me review-widget variables using
  the same hex for stars, buttons, and reviewer names) layered over a neutral black/white ecommerce
  chrome and a secondary warm-cream/terracotta palette (#fef9f6 through #362217) that likely supports
  product photography, swatches, and seasonal "Final Collection" merchandising.
  Headings are inferred to use the "Reckless" serif family (Bold/Light/Regular/Semibold variants are
  present in the font list) for an editorial, handwritten-adjacent feel appropriate to a planner brand,
  while "Inter" and "Assistant" are treated as the workhorse UI/body sans-serif, matching the many
  Inter weight variants supplied. The root CSS exposes an explicit heading/button type scale
  (--lh-h1 through --lh-h5, --lh-btn-*) which this spec treats as the closest evidence of real
  typographic intent and maps directly into the display and button tokens below.
  Numerous additional families (Baskerville, Alegreya, Roboto Slab, Beach Bound Script, brandon,
  bookmania, caslon, sweet-sans-pro, lindsey-signature) are assumed to be decorative or
  product/packaging-specific fonts baked into imagery or third-party apps rather than core site
  chrome, and are excluded from the token set as unverified for UI use.

colors:
  primary: "#e62e89"
  accent: "#ee4888"
  sale: "#d82727"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#343434"
  muted: "#707070"
  hairline: "#e5e5e5"
  surface-soft: "#f7ebe4"
  surface-card: "#fef9f6"
  on-primary: "#ffffff"
  border-dark: "#333333"
  earth-deep: "#6e4d3a"
typography:
  display-xl: {fontFamily: "Reckless, Baskerville, serif", fontSize: "44px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0.6px"}
  display-md: {fontFamily: "Reckless, Baskerville, serif", fontSize: "34px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  title-md: {fontFamily: "Reckless Semibold, Baskerville, serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, Assistant, Helvetica Neue, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.3px"}
  body-sm: {fontFamily: "Inter, Assistant, Helvetica Neue, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.2px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.8px"}
  button-md: {fontFamily: "Inter Semibold, sans-serif", fontSize: "15px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.5px"}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.earth-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  bundle-builder:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    itemTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"

## Components

**button-primary** — Solid magenta call-to-action (e.g. "SHOP POWERSHEETS NOW!") using the observed `--jdgm-primary-color`/`--jdgm-write-review-bg-color` value of `#e62e89` as background with white text, sized against the observed `--lh-btn-height: 45px` and `--lh-btn-padding: 30px` variables. Hover/active states are proposed, not observed.

**button-secondary** — An outline variant for secondary actions ("LEARN MORE", "VIEW ALL") using an ink border and transparent fill, sharing the same button typography scale. State is proposed.

**text-input** — Newsletter/email capture and account fields, using a light cream card background, a subtle hairline border, and body typography; focus-ring styling is not observed and is proposed.

**nav-bar** — Top utility bar (announcement strip for shipping/sale messaging) plus a primary nav row ("PLANNERS / ACCESSORIES / DESK & OFFICE / FAITH"). White background with a hairline bottom rule is inferred from the neutral palette; sticky behavior on scroll is not observed.

**product-card** — Repeating grid item for PowerSheets SKUs, pairing a cream card surface with title typography for the product name and a smaller price row that must support strikethrough "Regular price" alongside a "Sale price," matching the observed sale copy pattern.

**hero** — The homepage banner announcing "The Final Collection," set on the warm cream surface tone with the largest display type token; imagery/layout composition is inferred, not measured.

**footer** — A deep warm-brown block (drawn from the earthy secondary palette) carrying help/company link columns and social icons, using inverse (white) text for contrast; exact column layout is proposed.

**badge** — Small "Sale," "Low Stock," and "New" pills using the observed red (`#d82727`) or pink accent on a fully-rounded chip, matching the transactional tone of the sale copy in the evidence.

**search** — A lightweight input+icon pattern styled like text-input but compact, for the account/cart header area; not directly observed in the supplied CSS, proposed by ecommerce convention.

**bundle-builder** — A category-specific component modeled on the supplied `.qbk-offer__body` / `.qbk-bundle__list-item` bundle-kit CSS, used for "Build Your Own 3-Pack" and "PowerSheets | Full Set of 5" selection UI: a soft cream container with checkbox-style offer rows and a pink accent for the selected/added state, consistent with the plugin's own `--qbk-highlight-color` behavior.

## Responsive Behavior
Recommended, not measured from live rendering:

| Breakpoint | Width      | Behavior (proposed) |
|-----------|-----------|----------------------|
| mobile    | <600px    | Single-column stack, nav collapses to hamburger, product-card grid becomes 1–2 columns |
| tablet    | 600–1024px| Product-card grid 2–3 columns, nav shows condensed top-level items |
| desktop   | 1024–1440px | Full nav row visible, product-card grid 3–4 columns, hero at full display-xl scale |
| wide      | >1440px   | Max-width content container, additional whitespace, no new columns |

Touch targets should be at least 44px tall, matching the observed `--lh-btn-height: 45px`. Announcement-bar and promo-strip content should truncate or scroll on narrow viewports. None of this responsive behavior was directly observed; it is a conventional recommendation only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted from static CSS/text; no rendered layout, breakpoints, hover/focus states, or JS-driven interactions (cart drawer, mega-menu, bundle-kit widget behavior) were observed.
- The mapping of "Reckless" to headings and "Inter/Assistant" to body copy is inferred from font-family name lists only; no selector-level `font-family` assignment tying these families to h1/body was supplied.
- Numerous additional font families (Baskerville, Alegreya, Roboto Slab, Beach Bound Script, brandon variants, bookmania, caslon, sweet-sans-pro, lindsey-signature) appear in the evidence but their actual usage (decorative product imagery, third-party apps, or unused legacy assets) could not be confirmed, so they are excluded from tokens.
- The `body` selector's `font-size: 1.5rem` with a `--font-body-scale` divisor suggests a fluid/relative type system; the 16px `body-md` value here is a practical, reader-friendly approximation, not a literal pixel reading.
- `#0000ee` (default browser link blue) appears in the palette but is treated as an unstyled/default value, not an intentional brand color, and was excluded from tokens.
- Color-to-role assignments (e.g., which warm-neutral tone is "surface-soft" vs. "surface-card") are inferred from typical light/cream ecommerce patterns, not confirmed against a specific rendered section.
- Custom font licensing, self-hosting, and actual availability (e.g., whether "Reckless" is a licensed webfont in production) were not verified.
- Sale/badge and bundle-builder colors are drawn from generally observed reds/pinks in the palette; their exact production usage on those specific UI elements was not confirmed pixel-by-pixel.
