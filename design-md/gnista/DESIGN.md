---
version: alpha
name: "Gnista"
source_url: "https://gnistaspirits.com"
captured_at: "2026-09-28T10:21:31.851146+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gnista's evidence set is a Shopify (Dawn-derivative) theme with a warm,
  editorial palette anchored by a single burnt-orange accent (#bf570a,
  paired with a deeper amber #92400e) against near-black ink (#111827) and
  a warm off-white canvas (#fdfdfa). Supporting neutrals (#f7f7f7, #dedede,
  #c8c8c8, #6b7280, #374151) form a restrained gray scale used for
  surfaces, hairlines, and muted copy; these role assignments are inferred
  from typical Shopify utility patterns, not confirmed computed styles.
  Semantic red/green tokens (#b91c1c/#fef2f2, #166534/#ecfdf3) appear to be
  stock form-validation colors rather than brand choices. Card-network
  colors (Visa blue, Mastercard red/orange, PayPal blues) found in the raw
  palette are payment-badge artifacts and are explicitly excluded from the
  brand system below.
  Typography mixes two apparent custom serif families (AdelonSerial,
  RomieTrial) with Playfair Display and Arya, suggesting a serif-led,
  premium-spirits editorial voice for headlines and a plainer sans for
  body/UI text. The interpretation below proposes a quiet, amber-accented,
  editorial e-commerce layout suited to a small-batch non-alcoholic
  spirits and alt-wine brand, with layout, radii, and spacing largely
  proposed rather than measured.

colors:
  primary: "#bf570a"
  primary-dark: "#92400e"
  ink: "#111827"
  canvas: "#fdfdfa"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#dedede"
  border-strong: "#c8c8c8"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  danger: "#b91c1c"
  danger-bg: "#fef2f2"
  danger-border: "#fecaca"
  success: "#166534"
  success-bg: "#ecfdf3"
typography:
  display-xl: {fontFamily: "RomieTrial, serif", fontSize: 56px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Playfair Display, serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "AdelonSerial, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arya, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Arya, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arya, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arya, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1em, letterSpacing: 0.5px}
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
    border: "1.5px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1.5px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "transparent"
    backgroundStateNote: "Proposed scroll state: {colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "linear-gradient(to bottom, rgba(0,0,0,0.25), transparent)"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  testimonial-marquee:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.base}"
    rounded: "{rounded.none}"

## Components

**button-primary** carries the single confirmed accent (#bf570a) as a solid fill, used for primary CTAs like "Buy Now"; the hover/active darkening to `{colors.primary-dark}` is proposed, mirroring the theme's `--btn-bg-hover-color` pattern without a resolved value.

**button-secondary** is an outline treatment on the card surface, appropriate for secondary actions (e.g., "Learn More") alongside a filled primary button; border and text share the accent color, consistent with the `.btn--secondary` variable-swap pattern observed in CSS.

**text-input** uses a light hairline border and card-white background, matching the generic `.buttoned-input` border/background variables seen in the CSS; focus-ring color is not observed and is proposed as a subtle primary-tinted outline.

**nav-bar** is inferred as transparent-over-hero (per `--transparent-header-bg-gradient`) transitioning to a solid ink or canvas bar on scroll; this scroll-state behavior is proposed, not measured, since only the gradient variable was observed.

**product-card** groups a product image, serif title (`title-md`), and sans price line on a white surface with a soft hairline border, standard for a Shopify collection grid; hover elevation/shadow is proposed and unobserved.

**hero** applies the dark radial/linear overlay gradient found in `.section-header` over a full-bleed image, with large serif display type in white — this directly reflects the observed gradient variables layered for text legibility.

**footer** is proposed as a dark ink band echoing the header's dark-text-on-image treatment, holding newsletter signup, social, and legal links in small sans type; no footer-specific selectors were present in evidence.

**badge** is proposed for award/press callouts ("Michelin-starred," "Award-winning") using the darker amber tone as a small pill, since the page text emphasizes accolades but no badge component CSS was captured.

**search** follows the same bordered-input convention as text-input, scaled for a header search affordance; interaction states (open/closed, results dropdown) are not observed.

**testimonial-marquee** is a category-appropriate component reflecting the repeating press-quote block visible in the page text (Forbes, Vinepair, Alton Brown, etc.); rendered on a soft neutral surface with a continuous or paginated quote strip — motion behavior is proposed, not confirmed.

## Responsive Behavior
Recommendation only, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <768px | single-column stack, `--container-pad-x: 16px`, nav collapses to menu icon |
| tablet | 768–1023px | `--container-pad-x: 30px`, 2-column product grid |
| desktop | 1024–1439px | `--container-pad-x: 50px`, 3–4 column grid, persistent nav |
| large | ≥1440px | `--container-pad-x: 60px`, max-width container, wider gutters |

Touch targets should be ≥44px (matching the observed `--buttoned-input-size: 44px`). Mobile nav is assumed to collapse into a hamburger/drawer pattern typical of this Shopify theme family; this is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction provides variable names (e.g., `--btn-border-radius`, `--btn-bg-hover-color`) without resolved computed values, so radii, hover colors, and transform/case rules are inferred defaults, not confirmed.
- Semantic color-role assignments (ink, muted, hairline, surface-soft/card) are inferred from conventional gray-scale usage, not from confirmed selector-to-role mapping.
- Payment-network colors (Visa/Mastercard/PayPal blues, reds, oranges) present in the raw palette were intentionally excluded as third-party badge artifacts, not brand colors.
- No layout, hover, focus, or mobile-menu interaction was directly observed; all interaction and responsive behavior above is proposed.
- Custom font names (AdelonSerial, RomieTrial) could not be verified for licensing, hosting, or actual on-page rendering; fallback stacks are assumed generic per the supplied `sans-serif`/`serif` values.
- Typography sizes are proposed scale values loosely anchored to a serif-display + sans-body pairing; no explicit `font-size` px values were present in the supplied CSS rules.
