---
version: alpha
name: "Gathre"
source_url: "https://gathre.com"
captured_at: "2026-09-28T04:54:52.152334+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Gathre's storefront evidence shows a restrained, neutral palette anchored by near-black text (#262626) on white (#ffffff), with a warm taupe/gold accent (#a7845b) used for the favorite-button active state — inferred here as the brand accent for interactive highlights. Borders and dividers use a light gray (#e2e2e2), and soft surface fills (#f4f4f4, #f8f8f9) appear repeatedly behind product imagery and subdued UI states. A secondary warm neutral (#d5c1aa) appears in a hover-state background and is reused as a soft accent surface. The Shopify theme root variable sets border-radius to 0px, suggesting a largely square, minimal-ornament UI; a 3px radius appears only on a third-party password-page button and is not treated as brand-representative.

  Font evidence lists Arial, Arimo, Gotham, Gothic720 BT (and its Light/Roman variants), and Egyptian, alongside sans-serif fallbacks. Because no CSS explicitly ties a family to a specific role, this spec infers Gotham for display/heading use (a common premium sans common to DTC kids brands) and Gothic720 BT for body copy, both falling back to system sans-serif. All sizes, spacing, and rounding values beyond the observed 0px root radius are proposed, not measured, and are labeled accordingly throughout.

colors:
  primary: "#262626"
  ink: "#262626"
  canvas: "#ffffff"
  body: "#262626"
  muted: "#646e7f"
  hairline: "#e2e2e2"
  surface-soft: "#f8f8f9"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent: "#a7845b"
  accent-soft: "#d5c1aa"
  border-strong: "#cccccc"
  danger: "#dc2626"
  ink-secondary: "#58595b"
typography:
  display-xl: {fontFamily: "Gotham, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gotham, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gotham, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Gothic720 BT', Arimo, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Gothic720 BT', Arimo, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Gothic720 Lt BT Light', Arimo, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Gotham, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focus:
      border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-card}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    hover:
      borderColor: "{colors.border-strong}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    ctaVariant: "button-secondary"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkColor: "{colors.accent-soft}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    size: "{spacing.lg}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.accent}"
    gap: "{spacing.xs}"

## Components

**button-primary** uses the dominant near-black ink tone (#262626) as background with white text, reflecting the `--rivo-aw-primary-color` variable observed in the theme's root scope; sharp corners follow the root `--rivo-aw-border-radius: 0px` signal.

**button-secondary** is inferred from the slideshow `.btn--secondary` rule, which explicitly defines a white background with dark text that inverts to dark-background/white-text on hover — one of the few directly observed interaction states in the evidence.

**text-input** is a proposed pattern; no form-field CSS was supplied, so border color, padding, and focus state are inferred conventions using the observed hairline gray and primary ink.

**nav-bar** is proposed based on typical Shopify header structure combined with the observed hairline border color (#e2e2e2) used elsewhere for `--rivo-aw-border-color`; no header-specific selectors were present in evidence.

**product-card** draws directly from the `.ai-split-screen-product-*` rules, which specify a light gray image background (#f4f4f4), 13–14px title/price text in ink color, and no visible border-radius — treated here as representative of the storefront's product-grid presentation.

**hero** is proposed; no hero-section CSS was supplied beyond a slideshow secondary button, so background and spacing values are inferred defaults using the soft surface tone.

**footer** is proposed as a dark-ink footer with light text and an accent-soft link color, a common DTC pattern; no footer-specific selectors were present in the evidence.

**badge** models the "on sale" and "Top Rated" labels referenced in page text using the one clearly non-neutral, high-saturation color in the palette (#dc2626), though its exact application to sale badges is inferred rather than confirmed by a matching selector.

**color-swatch-selector** is a category-appropriate proposed component reflecting the extensive per-product color/fabric option lists (e.g., Ivory, Camel, Stone Stripe) seen in the page text, using a circular swatch pattern with an accent-colored selected state.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column product grid; `--container-pad-x: 16px` observed in theme root |
| Tablet | 480–1024px | 2-column product grid; nav collapses to menu icon (proposed) |
| Desktop | > 1024px | Multi-column grid; `--container-pad-x: 30px` observed in theme root at desktop gutter |

Touch targets should be at least 44px in height for buttons and swatch selectors (proposed, not verified). Navigation collapse into a hamburger/drawer pattern below tablet width is a standard assumption, not an observed interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/text; no rendered screenshots, computed layout, or DOM structure were available, so actual visual hierarchy and spacing are not confirmed.
- Font-to-role mapping (Gotham for display, Gothic720 BT for body) is inferred from font-family names alone; no selector explicitly ties either family to headings or body text.
- Font licensing/availability (e.g., whether Gotham is self-hosted, licensed, or a fallback stack) was not verified.
- The accent color (#a7845b) is drawn from a single favorite-button CSS variable and its broader use across the brand (e.g., links, highlights) is inferred, not confirmed.
- Border-radius values beyond the observed `0px` root variable and the unrelated 3px password-page button are proposed defaults.
- Interaction states (hover, focus, active) beyond the two explicitly observed slideshow button rules are proposed, not verified.
- Mobile/responsive layout behavior was not observed directly; the breakpoint table is a standard recommendation only.
- Badge and sale-label styling is inferred from page-text mentions of "on sale" and "Top Rated" combined with the one saturated red hex in the palette; no matching selector was supplied.
