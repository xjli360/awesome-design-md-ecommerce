---
version: alpha
name: "Kotn"
source_url: "https://kotn.com"
captured_at: "2026-09-28T04:45:27.072384+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Kotn's storefront CSS shows a neutral, paper-toned palette anchored by near-black text (#000000, #191919), warm off-white canvases (#fcfbef, #f4f1dd), and soft grays (#737373, #7e7e7e, #e8e8e8) that read as restrained, sustainable-basics styling. A small set of saturated accents appear in the palette — a deep green (#14a166, #006642) and a warm gold (#ffd500) — which this interpretation assigns to primary/eco-accent roles, since Kotn's copy emphasizes cotton, ethics, and school-funding impact; this mapping is inferred, not confirmed as brand-official.
  Two font families are directly observed in the CSS: "Kotn Sohne" (used for headers, buttons, and body copy via var(--font-sans)) and "Reckless," which appears only in the supplied font-family list without a captured usage rule — it is treated here as a serif display candidate for large editorial headlines, consistent with Kotn's "timeless design" positioning, but its actual applied selector was not present in evidence. A monospace stack appears once, scoped to a quantity stepper control.
  Layout patterns are inferred from component class names (ProductCard_*, button_*, recommendations_*): a tall 2:3 product-image ratio, white card backgrounds, thin hairline dividers, and a two-tier button system (dark-filled primary, outline secondary) with 2px corner rounding. Spacing and type scale values beyond the CSS variables shown are proposed, not measured.

colors:
  primary: "#14a166"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#737373"
  hairline: "#e5e7eb"
  surface-soft: "#f4f1dd"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  canvas-alt: "#fcfbef"
  accent-gold: "#ffd500"
  deep-green: "#006642"
  text-alt: "#7e7e7e"
  border-dark: "#191919"
  success-bg: "#d1fae5"
  success-text: "#065f46"
  error-bg: "#fee2e2"
  error-text: "#991b1b"
  warning: "#bd4800"
typography:
  display-xl: {fontFamily: "Reckless, serif", fontSize: 56px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Reckless, serif", fontSize: 36px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Kotn Sohne, system-ui, -apple-system, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Kotn Sohne, system-ui, -apple-system, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Kotn Sohne, system-ui, -apple-system, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Consolas, Menlo, Monaco, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Kotn Sohne, system-ui, -apple-system, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.02em}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspect: "2:3"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas-alt}"
    textColor: "{colors.text-alt}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  sustainability-callout:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.deep-green}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"

## Components
**button-primary** renders as a solid dark (near-black) fill with white text, matching the observed `.button_primary__Rr1tZ` rule using dark background/palette-text tokens; hover/active states are proposed, not captured in evidence.
**button-secondary** mirrors the observed `.button_secondary__LgZOe` class: white background, hairline border, 2px radius, disabled state shown with muted text — a real observed disabled style.
**text-input** is proposed by category convention (no input CSS was supplied); border and radius follow the button system for visual consistency.
**nav-bar** is inferred from page-text structure (language selector, Stores/Women/Men/Accessories/Home links, search/bag icons) rather than measured header CSS.
**product-card** is grounded in observed `ProductCard_*` classes: white background, 150%-padding (2:3) image box, single-line clamped title, and a fade-in animation on load — confirmed in CSS, though visual spacing/typography values are estimated.
**hero** is proposed from homepage copy ("A world of timeless designs…") using the warm off-white surface tone and the candidate serif display face.
**footer** is inferred from page-text link list (About Us, Stores, Beit Kotn, Careers, Size Guide, Returns, Gift Cards, Legal) with muted-gray text on a warm canvas.
**badge** (e.g., "Just Launched" or eco-certification tags) is proposed using the green success palette pairing observed elsewhere in the token set, not tied to a captured badge selector.
**search** is proposed styling consistent with the input pattern; no dedicated search-bar CSS was in evidence.
**sustainability-callout** is a category-specific proposed component for messaging like "Every purchase funds new schools," using the deep-green accent to reinforce the eco/ethics narrative.

## Responsive Behavior
Recommendation only — no responsive CSS or breakpoints were present in evidence.
| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column product grid, collapsed hamburger nav, sticky bag icon |
| Tablet | 640–1024px | 2-column product grid, inline search reveal |
| Desktop | >1024px | 3–4 column grid, persistent top nav, hover-reveal color swatches |
Touch targets should be ≥44px (buttons observed at 3.5rem/56px height satisfy this). Nav collapse and swatch/hover interactions are proposed, not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, JavaScript-driven state, or responsive breakpoints were observed. The "Reckless" font's actual selector/usage was not present in the supplied CSS rules — its display role here is inferred solely from its presence in the font-family list and Kotn's editorial tone; licensing and self-hosting details are unverified. Color role assignments (e.g., green/gold as "eco" accents) are interpretive, not confirmed via brand guidelines. All spacing scale values and most typography sizes beyond `--text-copy`/`--text-heading` variables are proposed placeholders. Mobile menu behavior, hover states, form validation styling, and animation timing beyond the two documented `fadeIn` keyframes are not observed.
