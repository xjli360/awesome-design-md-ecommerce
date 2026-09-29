---
version: alpha
name: "GT's Kombucha"
source_url: "https://gtslivingfoods.com"
captured_at: "2026-09-29T04:13:14.152127+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation draws from GT's Living Foods' observed Shopify theme evidence: a warm,
  editorial palette (#3f3a33 ink, #f9f8f0 and #f2f2f2 soft neutrals, #dedede hairlines) paired
  with saturated organic accents (#4b868f teal, #3e2952 plum, #f06e69 coral, #f9d0a3/#f3deb0
  tan-golds, #e4ccdb blush, #d6edf5 sky) that evoke fermentation, botanicals, and ritual wellness.
  Typography pairs serif display faces (Atrament, Usherwood, Baskerville No 2, MrsEaves) for
  editorial/brand moments with Montserrat and Museo Sans for UI and body copy, matching the
  theme's --text-h0..h6 scale (observed as rem custom properties with distinct mobile/desktop
  values).
  The system's primary interactive color is inferred from the only concretely observed
  UI-state color pair: the accelerated-checkout button's #1990c6 fill and #136f99 hover, applied
  here as {colors.primary}/{colors.primary-hover} for all primary buttons, since no other button
  background was directly evidenced. Card and section surfaces are inferred from the neutral
  palette (#f9f8f0, #f2f2f2, #e2d5c5) rather than measured. Radius and spacing scales are largely
  proposed conventions layered onto the single confirmed 0px checkout-button radius. No live
  layout, breakpoint behavior, or hover/focus states beyond the checkout button were observed.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#3f3a33"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#9ca3af"
  hairline: "#dedede"
  surface-soft: "#f9f8f0"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-teal: "#4b868f"
  accent-plum: "#3e2952"
  accent-coral: "#f06e69"
  accent-tan: "#f9d0a3"
  accent-cream: "#f3deb0"
  accent-blush: "#e4ccdb"
  accent-sky: "#d6edf5"
  accent-sand: "#e2d5c5"
typography:
  display-xl: {fontFamily: "Atrament, 'Baskerville No 2', serif", fontSize: 80px, fontWeight: 400, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Usherwood, 'Baskerville No 2', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 17px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
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
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-swatch:
    backgroundColor: "{colors.accent-tan}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
    selectedBorderColor: "{colors.primary}"

## Components

**button-primary** carries the only concretely observed interactive color pairing on the site — the accelerated-checkout button's `#1990c6` fill with `#136f99` hover — extended here as the system's general call-to-action treatment (e.g. "Add to Cart," "Subscribe"). Hover/disabled/focus visuals beyond the checkout element are proposed, not measured.

**button-secondary** is an outlined, ink-colored variant proposed for lower-emphasis actions (e.g. "Find a Retailer," "Learn More" links styled as buttons). No secondary button styling was directly observed; border and fill behavior are inferred from typical Shopify-theme conventions paired with the observed `--button-background-opacity: .85` hover rule.

**text-input** uses a plain bordered field on white, sized for the newsletter signup ("Stay Connected") and search. Border color and radius are proposed; only the general hairline gray (`#dedede`) and canvas white were present in evidence to justify this pairing.

**nav-bar** reflects the observed sticky header (`position: sticky; top: 0; z-index: 10`) and the three-column grid template (`logo / main-nav / secondary-nav`). Background is proposed as white/canvas since the homepage state uses a white-text-over-transparent-hero header (`.header:not(.is-filled) ... color:#fff`) that likely switches to a solid, dark-on-light state on scroll — this switch is inferred, not observed in a live capture.

**product-card** is proposed for the brand grid ("Synergy," "Alive," "Agua de Kefir," "COCOYO," "Immortal," "Classic Kombucha") shown in the homepage carousel copy. Card surface, radius, and spacing are proposed conventions layered onto the confirmed soft-cream and light-gray neutrals.

**hero** models the homepage's "We Begin Within" full-bleed section, using the deep plum accent as a background candidate consistent with the brand's apothecary/ritual tone; actual hero background imagery and color were not directly measurable from the supplied CSS.

**footer** groups the observed footer links (Terms, Privacy, Contact, copyright) on a dark ink background for contrast, consistent with typical dark-footer patterns; exact footer background color was not confirmed in evidence.

**badge** is proposed for merchandising labels such as "New," "Best Seller," or probiotic/CFU callouts common to functional-beverage PDPs, using the coral accent for visual pop against the neutral palette.

**flavor-swatch** is a category-specific component proposed for kombucha/kefir flavor selection on PDPs, using the observed tan/gold accent as a default fill and the primary blue as a selected-state ring; no PDP flavor-selector markup was present in evidence.

## Responsive Behavior

Recommended, not measured breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–639px | Single-column stacks; header logo ~55×69px per observed default token |
| tablet | 640–1023px | Two-column product grids; header padding increases per observed `--spacing-8-5` step |
| desktop | 1024–1439px | Header switches to `logo / main-nav / secondary-nav` grid per observed rule; type scale steps up (e.g. `--text-h0` 4rem→5rem) |
| wide | 1440px+ | Max-width containers; largest observed spacing tokens (`--spacing-20`/`--spacing-24`) apply to section padding |

Touch targets should be a minimum 44px tall, consistent with the observed accelerated-checkout button's `clamp(25px, 44px, 55px)` height rule. Navigation should collapse to a hamburger/menu pattern below tablet width; this collapse behavior was not directly observed and is a standard proposal for the header's stated "Open navigation menu" control.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived entirely from static CSS custom properties, a text excerpt, and a partial color/font inventory — no rendered page, computed styles, or interaction states were observed beyond the accelerated-checkout button's fill/hover colors. Semantic color-role mapping (ink, canvas, muted, surface-soft/card) is inferred from generic neutral values in the palette and may not match the brand's actual design intent. Font weights, exact pairing of the eight listed families to display/body roles, and licensing/availability of the custom faces (Atrament, Usherwood, MrsEaves, Museo Sans, Baskerville No 2) were not verified. Border-radius values beyond the single observed `0px` checkout-button default are proposed conventions. Mobile navigation collapse, hover/focus/active states for cards and secondary buttons, hero imagery, and true breakpoint pixel values were not present in the supplied evidence and should be confirmed against a live, rendered capture before implementation.
