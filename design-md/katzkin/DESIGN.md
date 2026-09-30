---
version: alpha
name: "Katzkin"
source_url: "https://katzkin.com"
captured_at: "2026-09-28T09:42:44.102349+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Katzkin's homepage CSS exposes a compact, utilitarian palette dominated by
  near-black warm charcoal ("#332e2b"), white, and mid-grays ("#575757",
  "#777777"), with a single confirmed accent blue ("#066aab") used on form
  submit buttons and a confirmed error red ("#d63637") from the WPForms
  validation variables. Most other hexes in the raw palette are generic
  WordPress/Gutenberg default swatches (e.g. "#ff6900", "#cf2e2e", "#9b51e0")
  with no CSS rule tying them to a real component, so they are treated here
  as decorative/unused rather than brand signal.
  The interpretation leans on the charcoal-and-white system that repeats
  across every observed call-to-action (design tool submit, install-booking
  button, review CTA), treating "#332e2b" as the primary action color and
  white as the on-primary text, which is directly confirmed in the CSS.
  Typography pairs a display serif-adjacent sans, Clash Display, for uppercase
  section headings (32px/600/uppercase, directly observed) with Figtree as the
  workhorse body/button font and Inter reserved for smaller supporting text.
  Roundedness is treated as a spectrum from sharp form inputs (3px, observed)
  to fully pill CTAs (9999px, observed), which is inferred to reflect a
  premium-automotive, craftsmanship-forward tone appropriate to custom leather
  upholstery.

colors:
  primary: "#332e2b"
  accent: "#066aab"
  highlight: "#f47a21"
  danger: "#d63637"
  ink: "#332e2b"
  ink-alt: "#32373c"
  canvas: "#ffffff"
  body: "#575757"
  muted: "#777777"
  hairline: "#dbdbdb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Clash Display', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0.4px}
  display-md: {fontFamily: "'Clash Display', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0.6px}
  title-md: {fontFamily: "'Figtree', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "'Figtree', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Figtree', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Inter', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Figtree', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
rounded:
  none: 0px
  xs: 2px
  sm: 3px
  md: 8px
  lg: 12px
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
    rounded: "{rounded.lg}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.ink-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  vehicle-selector:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

**button-primary** models the repeated dark charcoal CTA (`#332e2b`, white text, 12px radius, 12–20px padding) that appears identically across the review-CTA button, the YMMT "Submit" control, and the post-review CTA section — this is the most consistently observed interactive pattern on the page.

**button-secondary** is proposed around the confirmed accent blue (`#066aab`) sourced from the WPForms button-background CSS variable. It is treated as a secondary/form-submission action rather than the primary storefront CTA, since no homepage marketing button uses this color directly.

**text-input** reflects the WPForms root variables: white background, a semi-transparent black border (mapped to the closest observed hairline gray), and a small 3px radius. Focus/error states are not observed and are proposed only, aside from the confirmed error-red variable.

**nav-bar** is inferred from `.wp-block-navigation a` inheriting text color and the overall white body background; no header layout, sticky behavior, or breakpoint collapse was directly observed in the supplied CSS.

**hero** is proposed as a large dark panel using the ink-alt tone (`#32373c`, seen on default WP button backgrounds) with large uppercase Clash Display type, consistent with the "Custom Automotive Leather Upholstery" hero copy in the page text, though exact hero styling was not present in the CSS excerpt.

**vehicle-selector** is a category-specific component modeling the Year/Make/Model/Trim ("YMMT") widget referenced in the CSS (`#homepage-ymmt-widget`), using the light surface tone and the same dark primary accent as its "Next" button.

**product-card** is proposed for the Popular-Vehicles-by-Make and materials/color-swatch grids described in the page copy; no explicit card CSS was supplied, so border, radius, and spacing are inferred defaults.

**badge** models small labels such as "OEM AUTHORIZED" using the one clearly brand-flavored, automotive-adjacent orange (`#f47a21`) present in the palette; this color-to-role mapping is inferred, not confirmed by a matching CSS rule.

**footer** is proposed using the dark ink tone for contrast with the white page body, consistent with the button-darkness pattern elsewhere, but no footer-specific selectors were present in the supplied evidence.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Notes                                      |
|------------|-----------|---------------------------------------------|
| sm         | ≤480px    | Single-column stacking, full-width CTAs     |
| md         | 481–768px | Two-column card grids, condensed nav        |
| lg         | 769–1180px| Matches observed `--width-1: 1180px` var    |
| xl         | ≥1440px   | Matches observed `--page-width: 1440px` var |

Touch targets on primary buttons should stay at or above the observed 48px min-height used on `.post-review-cta-button`. Navigation is recommended to collapse to a hamburger/off-canvas pattern below `md`, though this collapse behavior was not observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text only; no rendered layout, JavaScript-driven interactions, hover/focus states, or real breakpoint behavior were observed.
- Most palette hexes beyond `#332e2b`, `#575757`, `#066aab`, and `#d63637` come from generic WordPress/Gutenberg default color swatches and are not confirmed to be intentional Katzkin brand colors; `highlight` (`#f47a21`) is an inferred, unconfirmed role assignment.
- `display-xl` size (48px) and most spacing-scale values are proposed defaults, not measured from the supplied CSS.
- `rounded.lg` (12px) and `rounded.md` (8px) are directly observed; `rounded.full` and `rounded.sm` are also observed, but their application to every component above is inferred by analogy.
- Font availability, licensing, and self-hosted vs. third-party delivery of "Clash Display," "Figtree," and "Inter" were not verified.
- No footer, nav, or product-card CSS selectors were present in the supplied evidence; those components are proposed patterns only.
