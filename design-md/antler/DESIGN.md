---
version: alpha
name: "Antler"
source_url: "https://antler.co.uk"
captured_at: "2026-09-29T04:13:34.051377+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Antler's UK storefront presents a neutral, editorial luggage catalogue built around a light canvas, near-black ink text, and a single saturated coral accent reserved for tertiary buttons and brand highlights (--color-antler-coral maps to the observed #ff4713). Body and heading typography both resolve to CSS custom properties (--font-body-family, --font-heading-family); only one concrete family, CircularStd, is present in the supplied evidence, so heading/body differentiation is inferred rather than confirmed as distinct typefaces. The broader palette includes muted heritage tones — forest green, navy, burgundy, and tan — which align with the site's "Shop by Colour" suitcase filters (black, pink, green, blue, white, red) and are treated here as secondary/category accent colors rather than core UI colors, since their exact application (swatch vs. imagery vs. seasonal collection) is not verifiable from static CSS alone. Card and button theming uses CSS variables layered over RGB channel strings (e.g., --color-base-text), so hex-to-role mapping below is a best-effort reconstruction. Surfaces use warm off-white/cream tones (#e8e4da, #ded7c8) suggesting a premium, tactile "British heritage" aesthetic rather than a stark white e-commerce look. All spacing, radius, and most typographic sizes are proposed conventions layered onto the observed variable structure, not measured pixel values.

colors:
  primary: "#ff4713"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#727563"
  hairline: "#e3e3e3"
  surface-soft: "#e8e4da"
  surface-card: "#ded7c8"
  on-primary: "#ffffff"
  accent-forest: "#294634"
  accent-navy: "#003b4a"
  accent-burgundy: "#551c25"
  accent-tan: "#864b2b"
  overlay-scrim: "#00000052"
typography:
  display-xl: {fontFamily: "CircularStd, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "CircularStd, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "CircularStd, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.2px"}
  body-md: {fontFamily: "CircularStd, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.2px"}
  body-sm: {fontFamily: "CircularStd, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.3px"}
  caption: {fontFamily: "CircularStd, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.4px"}
  button-md: {fontFamily: "CircularStd, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.6px"}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-tertiary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  color-swatch:
    backgroundColor: "{colors.accent-navy}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.none}"

## Components

**button-primary** uses the near-black ink fill (`--color-base-text`) with white label text, matching the site's default `.button--primary` variable chain; hover state (inverting to white background/ink text) is documented in CSS but its exact motion/easing is only partially confirmed (0.15s ease-in-out on secondary buttons) and is treated as proposed for primary.

**button-secondary** is an outline pattern (ink border, white fill) inferred from `.button--secondary` variable swaps; a documented hover state inverts to a solid ink background, which is directly evidenced in the CSS rather than proposed.

**button-tertiary** carries the distinctive coral accent (`--color-antler-coral`), likely reserved for promotional or "shop now" CTAs distinct from transactional buttons; its exact usage context is inferred from naming only.

**text-input** is a proposed pattern for search and form fields, using the light hairline border and canvas background; no explicit input CSS was supplied, so radius and padding are proposed conventions.

**nav-bar** reflects the mega-menu structure implied by the extensive "Shop by" category text (Hand Luggage, Suitcases, Luggage Sets, etc.); visual styling (background, spacing) is proposed since no header CSS block was supplied.

**product-card** uses `--product-card-background-color` (rgb 242,242,242, approximated here to the nearest observed hex `#e8e4da`) with configurable radius/border/shadow variables confirmed in CSS, though their resolved values were not supplied.

**hero** is a proposed full-width banner pattern using a warm surface tone, suited to seasonal collection imagery (e.g., "Discovery Collection," "Heritage Collection") referenced in page text; layout was not observed.

**footer** is proposed using the deep forest green as an inferred brand-heritage color block; no footer-specific CSS was supplied, so this is a stylistic extrapolation from the swatch palette.

**badge** supports promotional messaging such as "Save 20%" or "Free Delivery," using pill shape and outline styling consistent with `--color-badge-border` variables in the CSS.

**color-swatch** is a category-appropriate proposed component for the "Shop by Colour" suitcase filters (black, pink, green, blue, white, red), rendered as small circular swatches using accent colors from the observed palette.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile ≤599px, tablet 600–989px, desktop ≥990px, matching common Shopify theme conventions implied by the vendor-neutral CSS variable structure. Touch targets should be ≥44px height for primary/secondary buttons and swatches. Mega-menu navigation should collapse into an accordion drawer below tablet width; product grids should reduce from 4 to 2 columns at tablet and 1 column at mobile. This section is a design recommendation, not observed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS variable declarations and page text only; no rendered layout, computed styles, or interaction states were observed. Color role assignments (primary, muted, surface-card, etc.) are inferred from variable naming patterns and educated placement within a 59-color palette that mixes UI, product-swatch, and seasonal-campaign colors — several palette entries could not be confidently assigned a UI role and were omitted. Typography sizes, weights, and letter-spacing are proposed values layered onto confirmed CSS variable names (--text-size-base, --tracking-wide, etc.) whose actual computed pixel/weight values were not supplied. Only one font family, CircularStd, appears in evidence; its licensing, availability as a web font, and whether heading/body truly differ are unverified. Hover, focus, active, and disabled states beyond the two documented secondary-button hover rules are not observed. Mobile menu behavior, breakpoint values, and grid column counts are proposed conventions, not measured. Spacing and radius scales are standard proposed conventions, not derived from supplied CSS.
