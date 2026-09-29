---
version: alpha
name: "Fix & Fogg"
source_url: "https://fixandfogg.com"
captured_at: "2026-09-28T09:28:04.908916+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Fix & Fogg presents as an adventurous, B-Corp-certified New Zealand food brand whose
  supplied CSS evidence centers on a cream/off-white canvas (#fefdf4, #fffffb) paired with
  deep navy ink tones (#091535, #002c5e, #202a44) and two explicitly named brand accents:
  --highlight-one (#f8cc46, a warm yellow) and --highlight-two (#d31641, a bold crimson).
  A small swatch palette (grey-marl #abacae, violet #dfcbcb, forest-green #5f8374, baby-blue
  #cbd7f0) appears to map to flavor or product-variant selectors. Typography is anchored by
  an observed h1 rule using 'Futura Bold' at 5.6rem/6.2rem, weight 700, uppercase — treated
  here as the brand's display voice. Work Sans is the only other named family and is inferred
  as the body/UI typeface, since no body-text CSS was supplied directly. A 'paralucent' family
  also appears in the font list but its application is unconfirmed, so it is not assigned a role.
  Checkout components reveal a utilitarian blue (#1990c6 / hover #136f99) tied to Shopify's
  accelerated-checkout widget rather than the primary brand palette, so it is scoped narrowly
  to payment UI. A space-themed override (body.space-theme) with a near-black navy background
  (#030329) and white text suggests a seasonal/campaign skin layered atop the core theme;
  this interpretation treats it as an alternate surface, not the default brand system. All
  semantic role assignments (primary, ink, surface, etc.) below are inferred from token names
  and usage context, not confirmed via rendered screenshots.

colors:
  primary: "#f8cc46"
  ink: "#091535"
  canvas: "#fefdf4"
  body: "#202a44"
  muted: "#8890a0"
  hairline: "#e6e6e6"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#091535"
  accent-crimson: "#d31641"
  accent-navy-deep: "#002c5e"
  accent-space-navy: "#030329"
  swatch-grey-marl: "#abacae"
  swatch-violet: "#dfcbcb"
  swatch-forest-green: "#5f8374"
  swatch-baby-blue: "#cbd7f0"
  checkout-blue: "#1990c6"
  checkout-blue-hover: "#136f99"
  border-strong: "#bbbbbb"
typography:
  display-xl: {fontFamily: "'Futura Bold', sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.11, letterSpacing: 0px}
  display-md: {fontFamily: "'Futura Bold', sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "'Futura Bold', sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Work Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Work Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Work Sans', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "'Futura Bold', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.accent-navy-deep}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    typography: "{typography.body-sm}"
  flavor-swatch:
    optionColors: ["{colors.swatch-grey-marl}", "{colors.swatch-violet}", "{colors.swatch-forest-green}", "{colors.swatch-baby-blue}"]
    shape: "{rounded.full}"
    size: "{spacing.lg}"
    selectedBorder: "2px solid {colors.ink}"

## Components
**button-primary** uses the observed highlight-one yellow as a fill with dark navy text for contrast, reflecting the brand's playful, high-visibility CTA style; hover/active states are proposed and unobserved. **button-secondary** proposes an outlined navy-on-cream treatment for lower-emphasis actions such as "Learn More" links seen in the page text. **text-input** is a standard bordered field using the neutral hairline color; no form-field CSS was directly supplied, so padding and radius are inferred defaults. **nav-bar** assumes a light cream header consistent with the canvas tone, since no header-specific rule was captured in evidence. **product-card** is proposed for the nut-butter product grid, pairing a white surface with a hairline border to separate items on the cream page background; card interaction states (hover elevation) are not observed. **hero** maps to the large-headline sections referenced by the h1 rule, using the deep navy accent as background with cream text for a bold, space-adventure tone matching the NASA/astronaut copy. **footer** is inferred as a dark navy band with light text, a common pattern for the multi-link footer structure implied by the site-map text (Shop NZ, Store Locator, B Corp, etc.). **badge** repurposes the crimson highlight-two color for status labels such as "B Corp Certified" or "Award Winning," styled as a pill per the observed 400px border-radius pattern on swiper controls. **search**, if present, is proposed as a pill-shaped soft-grey field consistent with the neutral surface tones. **flavor-swatch** is a category-appropriate addition for nut-butter variant selection, directly using the four named swatch CSS variables (grey-marl, violet, forest-green, baby-blue) as circular option indicators — a plausible use given their explicit swatch naming, though the actual rendered selector UI was not observed.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column layout; h1 mobile font-size drops to 4.6rem per observed `--font-size-mobile`. |
| Tablet | 600–1023px | Two-column product grids; nav collapses to a hamburger menu (unobserved). |
| Desktop | 1024px+ | Full multi-column grid; carousel arrows (swiper-button) visible at edges. |

Touch targets should be at least 44px in height, consistent with the Shopify accelerated-checkout button's clamp(25px, …, 55px) sizing. Navigation collapse behavior, mobile menu treatment, and swiper carousel gesture behavior are recommendations only and were not measured from live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and text extraction only; no rendered screenshots, computed styles, or interaction states were captured. Semantic color roles (primary, ink, muted, etc.) are inferred from CSS variable names and contextual usage, not confirmed brand guidelines. Several typography sizes (display-md, title-md, body-md/sm, caption, button-md) are proposed defaults, not observed CSS values, since only the h1 rule was directly supplied. The `--theme-navy` variable referenced in component CSS has no resolved hex in the supplied evidence, so navy roles were approximated using the closest observed hex values (#002c5e, #091535). Availability, licensing, and web-font loading behavior for 'Futura', 'Futura Bold', 'Work Sans', and 'paralucent' were not verified. Mobile menu behavior, hover/focus states, and the space-theme campaign skin's full interaction model are not observed and are marked as proposed throughout.
