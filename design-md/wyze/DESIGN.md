---
version: alpha
name: "Wyze"
source_url: "https://wyze.com"
captured_at: "2026-09-28T09:19:44.214348+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Wyze's storefront CSS defines a single observed custom typeface, Gilroy, applied to body and heading elements with a generic sans-serif fallback stack (Futura, system UI fonts, Roboto, Helvetica, Arial). Only "Gilroy" is treated as brand-authored; all other named fallbacks are system substitutes, not confirmed brand fonts, so typography below uses "Gilroy, sans-serif" only.
  The palette centers on a bright mint/teal accent (#1df0bb, used as --color-accent and --color-button) against a white canvas (#ffffff) and near-black foreground text (#1f1f1f). Supporting neutrals (#f5f5f5, #fafafa, #e3e3e3, #cccccc, #969696, #757575) suggest card surfaces, hairlines, and muted text, inferred from common Shopify Dawn-theme variable naming rather than directly observed layout. Secondary brand colors (#334fb4 blue, #4e2fd2 violet, #ff8f5e coral) appear in the extended palette and are inferred as accent/badge colors for category tagging. Border radius and shadow values are theme CSS custom-property placeholders (e.g. --product-card-corner-radius) without resolved pixel values, so rounded/spacing scales below are proposed, informed by typical Shopify card conventions. This interpretation favors a clean, high-contrast, tech-retail aesthetic: white surfaces, mint CTAs, and dark ink text, appropriate for a smart-home security brand emphasizing affordability and trust.

colors:
  primary: "#1df0bb"
  ink: "#1f1f1f"
  canvas: "#ffffff"
  body: "#1f1f1f"
  muted: "#757575"
  hairline: "#e3e3e3"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#1f1f1f"
  accent-blue: "#334fb4"
  accent-violet: "#4e2fd2"
  accent-coral: "#ff8f5e"
  accent-deep-teal: "#055446"
  danger: "#bc3131"
  warning-bg: "#fff8df"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Gilroy, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gilroy, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Gilroy, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Gilroy, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.53, letterSpacing: 0.6px}
  body-sm: {fontFamily: "Gilroy, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "Gilroy, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Gilroy, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.6px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  device-quiz-stepper:
    backgroundColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    trackColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"

## Components

**button-primary** uses the theme's observed `--color-button: 29,240,187` (mint) with dark foreground text, matching the CSS `.button` background/text variable pairing directly evidenced in the stylesheet.

**button-secondary** mirrors `.button--secondary`'s variable swap to `--color-secondary-button: 255,255,255`, rendering as a white button with dark ink border/text; the hover border-glow effect referenced in `.button:hover::after` is proposed as a subtle outline state, not confirmed visually.

**text-input** is inferred; no explicit input CSS was supplied, so padding, rounding, and border color follow the surrounding hairline/neutral palette as a reasonable proposal for search and account forms.

**nav-bar** is proposed based on typical Shopify Dawn header patterns referenced by class names like `.header`, using canvas background and ink text; exact height and sticky behavior were not observed.

**product-card** draws on the `.contains-card--product` and `.product-card-wrapper .card` rules, which reference CSS custom properties for corner radius, border, and shadow (e.g., `--product-card-corner-radius`) without resolved values; rounded/padding values here are therefore proposed defaults consistent with the variable names.

**hero** is inferred from page-text evidence describing large promotional banners ("Indoor Cam Pan," "Introducing our Wyze VIPs"); no hero-specific CSS was supplied, so background, spacing, and typography scale are proposed.

**footer** is proposed; no footer-specific selectors were included in evidence, so a dark-ink-on-canvas-reverse treatment is suggested for contrast, not confirmed.

**badge** reflects the observed `--color-badge-background: 255,255,255`, `--color-badge-border: 31,31,31`, and `--alpha-badge-border: 0.1`, suggesting an outlined pill badge (e.g., for "NEW" or "DEAL" labels seen in page text) rendered in canvas/ink.

**search** is inferred from the "Search" and "Ask Wyze Assistant" text present in page copy; no dedicated search-input CSS was supplied, so this component's visual treatment is proposed.

**device-quiz-stepper** is a category-appropriate proposed component reflecting the multi-step "What type of property are you protecting?" quiz flow found in page text, using the primary mint accent for progress indication; no stepper CSS was supplied.

## Responsive Behavior

Proposed breakpoint table (not measured from live site):

| Breakpoint | Width | Layout notes |
|---|---|---|
| mobile | <750px | Single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet | 750–989px | 2-column product grid, condensed nav labels |
| desktop | 990–1439px | 3–4 column product grid, full horizontal nav |
| wide | ≥1440px | Max-width content container, generous section spacing |

Touch targets should be at least 44×44px for buttons and nav items on mobile. Primary nav is expected to collapse into a drawer or accordion below tablet width. This table is a recommendation based on common Shopify theme conventions, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived from static CSS custom properties, a partial selector list, and page text only; no rendered screenshots or DOM layout were observed. Many spacing, radius, and shadow values in the source CSS reference unresolved custom properties (e.g., `--product-card-corner-radius`, `--buttons-radius-outset`) whose computed pixel values are unknown, so all rounded/spacing scale numbers here are proposed, not measured. Component states (hover, focus, disabled) beyond the single `.button:hover::after` glow rule are inferred from convention, not confirmed. Mobile/responsive layout, breakpoint pixel values, and interaction behavior were not observed and are proposed recommendations only. The Gilroy typeface's licensing and actual web-font availability/loading were not verified; fallback fonts (Futura, system UI, Roboto, Helvetica, Arial) are system substitutes noted in CSS but excluded from the typography tokens above per brand-font-only policy. Secondary palette colors (blues, violets, corals, reds) were present in the supplied swatch list but their exact UI role (category tags, alerts, gradients) is inferred, not confirmed by selector evidence.
