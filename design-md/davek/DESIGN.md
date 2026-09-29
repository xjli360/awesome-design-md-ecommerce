---
version: alpha
name: "Davek"
source_url: "https://davekny.com"
captured_at: "2026-09-28T05:06:15.243886+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Davek's storefront evidence points to a restrained, technical-outdoor aesthetic built around a single dark navy anchor color, #1a2431, which appears explicitly as the Judge.me review-widget primary/star/reviewer color and is the strongest brand-color signal in the supplied CSS. Neutral grayscale values (#ffffff, #f5f5f5, #eeeeee, #dddddd, #333333, #000000) dominate the remaining palette, consistent with a product-photography-forward umbrella catalog rather than a saturated lifestyle brand. A small set of saturated colors (#eb001b, #00730b, #fbcd0a) surface in the raw palette dump without confirmed selectors; these are treated as inferred utility colors (sale/clearance, success/in-stock, highlight) rather than core brand colors, since their roles are not evidenced by the supplied rules.
  Typography is more clearly evidenced: heading elements (h1–h6) explicitly load a custom family, "neuzeits," at font-weight 100, giving headlines an intentionally light, editorial feel — this is an unusual and specific observed choice, not a default. Body typography references a CSS variable (--font-body) whose resolved value was not captured in evidence; Karla is used here as the most plausible sans candidate from the observed font list, alongside Montserrat, Nunito Sans, and Instrument Sans, and this assignment is explicitly inferred, not confirmed. Layout tokens use a --spacing-unit of 4px, which anchors the spacing scale below.

colors:
  primary: "#1a2431"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent-sale: "#eb001b"
  accent-success: "#00730b"
  accent-highlight: "#fbcd0a"
typography:
  display-xl: {fontFamily: "neuzeits, sans-serif", fontSize: 48px, fontWeight: 100, lineHeight: 1.25, letterSpacing: -0.5px}
  display-md: {fontFamily: "neuzeits, sans-serif", fontSize: 32px, fontWeight: 100, lineHeight: 1.3, letterSpacing: -0.25px}
  title-md: {fontFamily: "neuzeits, sans-serif", fontSize: 24px, fontWeight: 100, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Karla, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.71, letterSpacing: 0px}
  body-sm: {fontFamily: "Karla, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Karla, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Karla, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  wind-rating-indicator:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary** — The dark navy `{colors.primary}` fill with white text is proposed for main calls to action ("Shop now," "Check them out"), following the strongest observed brand color signal. Hover/focus states are not observed and are proposed as a slight opacity or darken shift.

**button-secondary** — An outlined variant using the same navy for border and text on a transparent field, proposed for lower-emphasis actions like "Compare Umbrellas" or "View All Umbrellas."

**text-input** — A white field with a light hairline border, matching the neutral gray tones seen throughout the palette (#dddddd, #cccccc). Focus-ring styling is not observed and is proposed only.

**nav-bar** — A white header with dark text is the default proposed state. The evidence does confirm a distinct `.header--transparent` variant that overrides text/icon colors to white with a low-opacity light border (`rgba(177,177,177,0.2)`), implying a transparent-over-hero header treatment on entry; the underlying non-transparent nav-bar styling itself is inferred by contrast.

**product-card** — A soft off-white card surface for umbrella listings (Solo, Commuter, Duet, etc.), using `{typography.title-md}` for model names and `{typography.body-md}` for pricing, consistent with the flagship/best-seller product grid described in page text.

**hero** — A full-bleed navy section with large, light-weight (100) display type in the custom `neuzeits` font, matching the "UMBRELLAS BUILT TO ENDURE." homepage messaging pattern. Exact hero dimensions are not observed.

**footer** — Proposed as a navy band echoing the header/hero treatment, given the extensive footer navigation (Corporate, About Us, Accessories) implied by repeated menu text in the evidence; actual footer background is not directly confirmed.

**badge** — A small red-accent label for sale/clearance flags, using `#eb001b` from the raw palette; role is inferred since no selector tied this color explicitly to a badge component.

**wind-rating-indicator** — A category-specific component proposed for this brand's core differentiator (wind resistance, "Max Wind Resistance" use-case category): a small neutral chip with navy accent, suitable for surfacing wind-rating or "Forever Guarantee" callouts on product pages. This pattern is proposed, not observed.

## Responsive Behavior

This is a recommended breakpoint strategy, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger, single-column product grid | 1 column |
| Tablet | 600–1024px | Collapsed or condensed nav, 2-column grid | 2 columns |
| Desktop | >1024px | Full horizontal nav with mega-menu (implied by extensive category list), 3–4 column grid | 3–4 columns |

Touch targets are proposed at a minimum 44×44px for buttons and nav icons. Mega-menu collapse into an accordion drawer below 1024px is a reasonable inference given the deep BY MODEL / BY TYPE / BY USE menu structure, but no mobile-menu markup or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered screenshots, computed styles, or interaction states (hover, focus, active, disabled) were observed.
- The `--font-body` CSS variable's resolved font value was not present in evidence; Karla was selected as the most plausible body font from the observed family list, but this mapping is inferred, not confirmed.
- The custom heading font "neuzeits" availability, licensing, and full character set are unverified; it is used here only because it appears explicitly in the theme CSS for h1–h6.
- Several palette colors (#eb001b, #00730b, #fbcd0a, and others) appear in the raw color list without a confirmed selector or role; their assignment to sale/success/highlight roles here is inferred for plausibility, not evidenced.
- Border-radius values are proposed defaults; only the Judge.me review widget's `--jdgm-border-radius: 0` was directly observed, and it is not confirmed to represent site-wide radius conventions.
- Spacing scale beyond the observed `--spacing-unit: 4px` (and its multiples) is a proposed convenience scale for component authoring, not a full extraction of the theme's spacing system.
- Mobile navigation, cart drawer, and search overlay layouts were not observed and are described only as proposed patterns.
