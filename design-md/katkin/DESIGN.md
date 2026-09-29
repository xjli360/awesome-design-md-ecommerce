---
version: alpha
name: "KatKin"
source_url: "https://katkin.com"
captured_at: "2026-09-28T09:35:22.668689+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  KatKin's observed CSS exposes a compact, high-contrast palette built around near-black ink (#231F20), a saturated yellow-green brand accent (#D5E709), and warm off-white surfaces (#EEEFE4, #FFFFFF). Supporting hues (orange, green, blue, pink) appear as small tokenized accents (--color-orange, --color-green, --color-blue, --color-pink) likely used for iconography or category tagging rather than primary UI chrome. Two custom font families are declared, "GreedBold" and "Scto" (Bold/Regular), paired with system sans-serif fallbacks; these read as a bold display face for headlines and a neutral grotesk for body copy, consistent with a direct-to-consumer, editorial-leaning pet-food brand.

  This interpretation treats the black button (.bg-component-button-default) as the primary CTA color, with the brand yellow-green reserved for secondary/tertiary emphasis and section headers (per .bg-component-headed-section-header-fresh). Card and soft-surface tones are inferred from the light-grey and near-white tokens already present. Type scale, radius, and spacing values are extended from the site's own CSS custom properties (--text-new-*, --radius) where available, and proposed where not measured. No layout, breakpoint, or interaction behavior was directly observed; all such guidance below is a design recommendation only.

colors:
  primary: "#231f20"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#4b4748"
  muted: "#888888"
  hairline: "#ededed"
  surface-soft: "#eeefe4"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent-brand: "#d5e709"
  accent-brand-tint: "#d5e7091a"
  accent-blue: "#45afe2"
  accent-green: "#3eb16a"
  accent-green-dark: "#256c41"
  accent-orange: "#ff8902"
  accent-pink: "#ea8bed"
  danger: "#ff0000"
  grey-400: "#a3a1a1"
typography:
  display-xl: {fontFamily: "GreedBold, sans-serif", fontSize: 80px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -1px}
  display-md: {fontFamily: "GreedBold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  title-md: {fontFamily: "SctoBold, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "SctoRegular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "SctoRegular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "SctoRegular, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "SctoBold, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.accent-brand}"
    textColor: "{colors.ink}"
    borderColor: "{colors.accent-brand}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-brand}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  meal-plan-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.accent-brand}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-green-dark}"

## Components

**button-primary** — Proposed default call-to-action, modeled on the observed `.bg-component-button-default` (black background). Used for high-commitment actions like "Start my trial." Hover/focus states not observed; assume a slight opacity or darken treatment as proposed.

**button-secondary** — Modeled on `.bg-component-button-secondary`, which uses the brand yellow-green as both border and fill. Suited to lower-commitment actions ("Learn more") or promotional callouts. Text color kept dark for contrast against the light accent.

**text-input** — No form-field CSS was directly observed; styling is proposed using the site's hairline and canvas tokens to stay consistent with the neutral card surfaces seen elsewhere (e.g., email signup, account login).

**nav-bar** — Inferred from header height tokens (`--header-height-mobile:50px`, `--header-height-desktop:88px`) and the white/black header theme classes. Assumes a persistent top bar with logo, primary nav links, and a login/CTA cluster; exact link styling not measured.

**product-card** — Represents the "Fresh Food," "Litter," and comparison-table tiles referenced in page copy. Uses the light card surface and hairline border to separate content blocks; padding and radius are proposed defaults.

**hero** — Reflects the large headline treatment implied by the `--text-new-5xl`/`--text-new-6xl` custom properties and the "Born to eat meat" hero copy. Background uses the soft light-grey surface token seen in `body:has([data-page-theme=secondary])`.

**footer** — Inferred as a dark, ink-colored band given the footer-shadow token and the dense link list in the page text (Help, FAQs, social links, legal). Contrast pairing (ink background, white text) is proposed, not confirmed.

**badge** — Small pill-shaped accent, e.g., for "Rated 4.6/5" Trustpilot mention or "100% Fresh" claims. Uses brand yellow-green fill with dark text; fully rounded per `full` token.

**search** — No dedicated search UI was found in the evidence; this is a speculative component provided for completeness, styled to match the card/hairline system rather than any observed search bar.

**meal-plan-card** — Category-specific component representing the personalized "Tell us about your cat" plan-builder step described in the page copy. Uses a brand-accent border to visually distinguish the core conversion flow from generic content cards; internal accent color draws on the dark-green token for nutrition-related emphasis.

## Responsive Behavior

This is a recommendation, not measured site behavior — no live breakpoint or resize testing was performed.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 640px | Single-column stacking; header collapses to `--header-height-mobile` (50px) with a hamburger/menu toggle. |
| Tablet | 640–1024px | Two-column card grids; nav links may partially collapse. |
| Desktop | > 1024px | Full nav bar at `--header-height-desktop` (88px); multi-column hero and card grids. |

Touch targets should be at least 44×44px for buttons and nav items. Primary/secondary buttons should retain `{spacing.md} {spacing.lg}` padding across breakpoints to preserve tap area. Mobile navigation collapse pattern (drawer vs. dropdown) is not observed and left to implementation discretion.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered page, computed styles, or DOM interaction states were observed.
- "primary" vs. "secondary" button role assignment is inferred from class naming (`button-default` vs `button-secondary`) and may not match actual visual hierarchy or usage frequency on the live site.
- Font files for "GreedBold," "SctoBold," and "SctoRegular" were referenced by name only; their availability, licensing, and exact rendered weights/metrics are unverified.
- All font sizes above the root `--text-new-*` scale are mapped from that scale but their real-world application (which element uses which size) was not confirmed.
- Hover, focus, active, disabled, and error states for all components are proposed defaults, not observed.
- Mobile menu structure, footer column layout, and card grid column counts are inferred from copy density and standard e-commerce conventions, not measured.
- Border radius and spacing scales beyond `--radius:0.5rem` are proposed conventions layered onto the one confirmed token.
