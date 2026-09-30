---
version: alpha
name: "Warren London"
source_url: "https://warrenlondon.com"
captured_at: "2026-09-29T04:01:58.917671+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Warren London's storefront CSS centers on a warm, spa-like cream canvas
  (#f6eee3) paired with pure black (#000000) for text, links, and primary
  buttons, and white (#ffffff) for button text and card surfaces. This
  high-contrast, minimal palette suits a "premium pet spa" positioning:
  clean, editorial, and product-forward rather than playful or saturated.
  Root theme variables confirm the button, badge, and link colors are all
  literal black/cream/white, with translucent black (#00000080 and related
  alpha values) available for secondary text or overlays. A secondary
  warm-gold swatch cluster (#eed9b9, #cfa354, #d4a95c) appears in the
  palette; its exact UI role is not confirmed by the supplied selectors,
  so it is treated here as an inferred accent for premium badges or
  spa-menu callouts rather than a core brand color. Payment-network hex
  values (blue/red/orange/yellow tones) present in the raw palette are
  excluded from brand roles as they most likely belong to third-party
  checkout icons, not Warren London's own design system.
  Typography uses "Instrument Sans" with a system-ui fallback, observed
  at the document body level with a 1.5rem base size and 0.06rem letter
  spacing — an unusually roomy, confident body-text rhythm reused across
  the proposed type scale below. Layout patterns (hero slider, mega
  navigation, footer) are inferred from page text/structure, not from
  measured DOM screenshots.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#f6eee3"
  body: "#000000"
  muted: "#00000080"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#eed9b9"
  accent-gold: "#cfa354"
  surface-dark: "#242833"
typography:
  display-xl: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.96px}
  body-sm: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.32px}
  caption: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Instrument Sans, system-ui, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayTextColor: "{colors.surface-soft}"
    headingTypography: "{typography.display-xl}"
    ctaBackground: "{colors.surface-card}"
    ctaTextColor: "{colors.ink}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  solution-tile:
    backgroundColor: "{colors.surface-soft}"
    accentBorder: "1px solid {colors.accent-gold}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders the site's dominant call-to-action pattern (e.g. "Shop Now"), using the black button background and white text confirmed by the `--color-button` / `--color-button-text` root variables. Hover-state color inversion (white bg / black text) is observed in the `.btn_first_*` and `.btn_sec_*` hero-slider rules and is treated as a confirmed interaction pattern for slider CTAs specifically; its use on non-hero buttons is proposed by extension.

**button-secondary** uses the cream canvas background with black text and a black hairline border, mirroring the `--color-secondary-button` / `--color-secondary-button-text` variables. Proposed for lower-emphasis actions like "Continue shopping" or filter toggles.

**text-input** is a proposed pattern for search boxes, newsletter fields, and account forms; no explicit input CSS was supplied, so the card surface, hairline border, and body-sm typography are inferred from the neutral, high-contrast theme.

**nav-bar** represents the mega-navigation implied by the page text (Products, By Type, Solutions, Business Customers, plus country/currency selector). Styling is inferred to match the canvas/ink palette; dropdown behavior, sticky states, and mobile collapse are not observed in the supplied CSS.

**product-card** is the base grid unit for listings like "All Products," "Dog Shampoos," and "Creative Color." White surface, hairline border, and title/price typography are proposed conventions consistent with the observed neutral palette; no `.product-card` selector was present in evidence.

**hero** models the homepage slider referenced by `.color-slider-1/2/3` classes, with white/off-white (#f3f3f3) heading text over a presumed dark or photographic background, and overlaid black/white button pairs — this pairing is directly observed in the supplied slider button rules.

**footer** is proposed using the dark slate tone (#242833) present in the palette but not tied to a specific selector in evidence; it is a plausible role for site-wide social icon links (Facebook, Instagram, YouTube, TikTok, Pinterest) noted in the page text. Actual footer background is unconfirmed.

**badge** reflects the explicit `--color-badge-background`, `--color-badge-foreground`, and `--color-badge-border` variables (cream bg, black text/border), suited to labels like "New," "Sample," or wholesale-only tags.

**search** is a proposed component for the "Search" link referenced in navigation text; no dedicated search-input CSS was supplied.

**solution-tile** is a category-specific component proposed for the "Solutions" taxonomy (Skin and Coat, Nail and Paw, Itchy Skin, Odor, Ear and Face, After Bath Sprays) listed in the page text. It uses the soft neutral surface with a gold accent border to visually differentiate grooming "solution" categories from standard product cards; this accent-gold usage is inferred, not confirmed against a specific selector.

## Responsive Behavior

Proposed breakpoint table (not measured from live rendering):

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | 0–599px | Single-column product grid, nav collapses to a hamburger/off-canvas menu, hero heading drops to `display-md` scale |
| tablet | 600–989px | 2-column product grid, mega-nav dropdowns may remain hidden behind a toggle |
| desktop | 990–1279px | 3–4 column product grid, full horizontal nav with dropdown mega-menus |
| wide | 1280px+ | Max-width content container, hero imagery at full bleed |

Touch targets for buttons and nav links should maintain a minimum 44×44px hit area, using `{spacing.md}`–`{spacing.lg}` padding as defined above. Mega-menu columns (Products / By Type / Solutions / Business Customers) should collapse into stacked accordions on mobile. This entire section is a UX recommendation only; no responsive/mobile CSS or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variable declarations, a limited set of component-class rules (hero slider buttons, `:root` color tokens), and page text — not from rendered screenshots, computed styles, or interaction testing. Specific gaps:

- **Unconfirmed accent usage**: The gold/tan swatch cluster (#eed9b9, #cfa354, #b8914f, #e6c27a, #d4a95c, #f0d28c) and dark slate tones (#242833, #222831, #121212) appear in the raw palette without a selector confirming their functional role; they are used here as inferred accents only.
- **Excluded payment colors**: Hex values matching common card-network branding (blue, red, orange, yellow) were excluded from all role assignments as likely third-party checkout icon colors, not brand tokens.
- **No measured typography scale**: Only the body font-size (1.5rem) and letter-spacing (0.06rem) were directly observed; all heading, caption, and button sizes are proposed.
- **No spacing/radius CSS observed**: The spacing and rounded-corner scales are proposed defaults, not extracted values.
- **Layout and interaction unobserved**: Navigation dropdown behavior, mobile menu collapse, card grid columns, hover/focus states beyond the two documented button rules, and footer structure are inferred from page text and general e-commerce convention, not measured.
- **Font licensing unverified**: "Instrument Sans" availability, license, and self-hosting vs. third-party delivery were not verified from the supplied evidence.
