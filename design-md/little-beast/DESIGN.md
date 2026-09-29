---
version: alpha
name: "Little Beast"
source_url: "https://littlebeast.co"
captured_at: "2026-09-28T04:46:25.068258+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Little Beast's storefront evidence shows a navy-and-cream palette built around a deep indigo-navy (#152868, with a closely related #16256a and #0e296c), paired with warm off-white/cream surfaces (#fdf9f0, #fcf9f1, #f7efdc, #f3f3ef) and a burnt-orange accent (#d2782c) used for hover states. Neutral grays (#666666, #cccccc, #ebebeb, #f8f8f8) support body copy and dividers. Typography draws on a mix of named webfont files: 'Lexend-Regular' and 'Lexend-SemiBold' for navigation, buttons, and product subtitles (often uppercase, sometimes italic on headers); 'AnonymousPro-Bold' and 'Anonymous Pro' (monospace) for product-title styling; and 'Lora' variants (Bold/Regular/Italic/SemiBold) present in the type stack, inferred here for longer-form editorial copy such as the About/brand story. This interpretation treats navy as the primary brand color and on-primary text as the pale cream #f3f3ef seen on filled navy buttons, with orange reserved for hover/interactive emphasis, matching the two observed button-hover rules. Card and section surfaces reuse the cream/gray tones already present rather than introducing new colors. Component patterns (product card, quick-add, hero, footer) are proposed based on the commerce vocabulary in the page text (Quick Add, swatches, sizes, sale badges) and are explicitly not confirmed layout observations.

colors:
  primary: "#152868"
  ink: "#152868"
  canvas: "#fdf9f0"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f7efdc"
  surface-card: "#ffffff"
  on-primary: "#f3f3ef"
  accent: "#d2782c"
  accent-alt: "#0e296c"
  sale: "#d2782c"
  disabled: "#cccccc"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "'Lexend-SemiBold', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Lexend-SemiBold', sans-serif", fontSize: 30px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Lexend-Regular', sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Lora-Regular', serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Lora-Regular', serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'AnonymousPro-Bold', monospace", fontSize: 12px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Lexend-Regular', sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
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
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.caption}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  size-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** reflects the two observed CTA rules (`.teaser__button`, `.about-section-2__button`): navy fill, cream text, Lexend-Regular label, with an orange hover swap — the only interaction state actually present in the evidence.

**button-secondary** is proposed for lower-emphasis actions (e.g., "No, thank you" on the signup banner); it mirrors the primary's shape and type but as an outlined navy-on-transparent treatment, not confirmed by CSS.

**text-input** is inferred for the email-capture and search fields referenced in the page text; padding and border follow the neutral hairline/gray tones already in the palette.

**nav-bar** generalizes the `.about-menu__anchor` styling (uppercase Lexend-Regular, navy text on cream) into a full header bar; the mega-menu list (Shop, Sale, Gift Card, etc.) implies a dropdown but exact behavior is not measured.

**product-card** draws on the AnonymousPro-Bold uppercase title rule and the $-price pattern seen repeatedly in the text excerpt (e.g., "Stripe Onesie $48.00"); swatch and size rows ("xxs–xxl") are proposed sub-elements.

**hero** is proposed from the homepage copy ("shop now," large title, CTA) using the cream surface and navy display type; exact hero dimensions are not observed.

**footer** assumes the deep-navy variant (#0e296c) as a footer band holding the listed legal/informational links (Privacy Policy, FAQ, Returns, Terms); this color-role assignment is inferred, not confirmed by a footer-specific CSS rule.

**badge** models the "-15%"/"-50%" sale markers visible in the text excerpt, using the orange accent already confirmed as a hover/CTA color, repurposed here for sale emphasis.

**search** and **size-swatch-selector** are proposed utility components matching the "Search" and per-product size-picker (xxs–xxl) UI implied by the text content; no dedicated CSS was supplied for either.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤480px, tablet 481–1024px, desktop ≥1025px. Recommend collapsing the multi-column mega-menu (Shop All / Coming Soon / category list) into an accordion below 1024px, per the `about-menu-mobile__*` class names in evidence, which suggest a distinct mobile menu pattern already exists in the site's own CSS. Touch targets for buttons and size swatches should be at minimum 44×44px. This section is a design recommendation only, not a report of measured responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or runtime interaction (hover, focus, menu open/close, cart drawer) was directly observed. Color-to-role mapping (e.g., footer background, canvas vs. surface-soft) is inferred from limited selector context and may not match actual usage elsewhere on the site. Typography sizes for body/caption/display-md are proposed estimates informed by the few explicit `font-size` values in evidence (16px, 18px, 20px, 30px); other sizes are not confirmed. Spacing and rounded-corner scales are conventional proposals, not extracted values. Availability, licensing, and web-font loading of the named families ('Lexend-*', 'Lora-*', 'AnonymousPro-Bold') were not verified beyond their appearance as font-family declarations. Mobile-specific visual layout and breakpoint thresholds are not observed and are offered only as recommendations.
