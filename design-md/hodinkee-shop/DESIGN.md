---
version: alpha
name: "Hodinkee Shop"
source_url: "https://shop.hodinkee.com"
captured_at: "2026-09-28T04:45:23.197772+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Hodinkee Shop's observed CSS shows a restrained editorial system built around near-black neutrals
  (#1a1b1b, #292a2a, #000000) against white and soft off-white surfaces (#ffffff, #f5f7f7, #eaecec),
  consistent with a premium watch-collector storefront that pairs product photography with quiet UI
  chrome. Buttons use uppercase, letter-spaced Brown at small sizes (.btn, .btn-primary), with
  Hodinkee Social used for looser-set functional labels (.btn-functional). Editorial serif families
  (Ivar Headline, Ivar Text, Portrait) appear in the font list and are inferred here as headline/hero
  typefaces, evoking the magazine-like tone of Hodinkee's editorial roots, while Proxima Nova and
  Helvetica Neue are inferred as long-form body fallbacks. A narrow accent palette of brass
  (#a37d49), red (#d02e2e), and green (#56ad6a) is present in the raw swatches but its functional
  role (alerts, status, or decorative accents) is not confirmed by the supplied CSS, so it is mapped
  conservatively to status/badge use. Hairlines (#d8dada, #cccccc) and layered near-black overlays
  (#0000001a, #00000080) suggest a design that relies on subtle borders and shadow-based elevation
  rather than saturated color. All layout proportions and interaction states beyond the supplied
  .btn rules are proposed, not observed.

colors:
  primary: "#292a2a"
  ink: "#1a1b1b"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#767a7a"
  hairline: "#d8dada"
  surface-soft: "#f5f7f7"
  surface-card: "#eaecec"
  on-primary: "#ffffff"
  border-subtle: "#cccccc"
  overlay-dark: "#00000080"
  accent-brass: "#a37d49"
  accent-red: "#d02e2e"
  success: "#56ad6a"
  danger: "#bd4545"
  danger-bg: "#f7d7d6"
typography:
  display-xl: {fontFamily: "Ivar Headline, Georgia, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Portrait, Georgia, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Brown Pro, Brown, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Proxima Nova, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Proxima Nova, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Hodinkee Social Mono, Consolas, monospace", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.0125rem}
  button-md: {fontFamily: "Brown, sans-serif", fontSize: 0.6875rem, fontWeight: 700, lineHeight: 1rem, letterSpacing: 1px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  authenticity-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    accentColor: "{colors.accent-brass}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed `.btn-primary` dark-neutral background with white text, uppercase letter-spaced Brown typography, and a small 2px radius; hover/active/disabled darkening states are directly observed in the supplied CSS (`.btn-primary:hover`, `:active`, `:disabled`).

**button-secondary** mirrors `.btn-secondary`: transparent background, hairline border, dark text, with a lighter hover border color as observed. Proposed for secondary actions like "Continue to Shop" beside a primary CTA.

**text-input** is a proposed pattern for search or account forms; no explicit input CSS was supplied, so border, padding, and radius are inferred to match the button system's restrained aesthetic.

**nav-bar** is proposed as a white, hairline-bordered header consistent with the editorial tone implied by the brand's "Skip to Main Content" markup and icon set (search, journal-spacer icons); exact height and sticky behavior are not observed.

**product-card** is proposed for watch/strap listings, combining a bordered white surface, Brown Pro title typography, and body-md pricing; card imagery treatment is not confirmed by the supplied evidence.

**hero** reflects the observed `--why-buy-hero` and `--insurance-bg` background-image custom properties, using a dark overlay and large serif headline typography inferred from Ivar Headline's presence in the font list.

**footer** is proposed using the soft off-white surface and hairline dividers seen elsewhere, housing the observed link groups (Our Story, Support, Follow Us) referenced in the page text.

**badge** is a proposed pill component for status labels such as "Authorized Retailer" or stock/condition tags, using the neutral surface-card background; color-coded variants (success/danger) may reuse `{colors.success}` or `{colors.danger}` but no such badge markup was directly observed.

**search** is proposed for the search icon referenced in the icon list, styled as a soft-surface input field consistent with the site's low-contrast UI chrome.

**authenticity-panel** is a category-appropriate component proposed for watch-collector trust signals (e.g., "Authorized retailer," warranty, or provenance details mentioned in the page text), using a brass accent to imply heritage/craft without contradicting the observed neutral-dominant palette.

## Responsive Behavior

Proposed breakpoints (not measured from live site behavior):

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | 0–599px | Single-column product grid; nav collapses to a hamburger/menu icon; buttons expand to full width. |
| Tablet | 600–1023px | Two-column product grid; nav-bar shows condensed horizontal links. |
| Desktop | 1024px+ | Multi-column grid; full horizontal nav; hero uses full-bleed background image per `--why-buy-hero`. |

Touch targets are recommended at a minimum 44×44px for buttons and nav items. Below tablet width, secondary navigation and filter panels are recommended to collapse into an off-canvas drawer. This section is a design recommendation only; no actual responsive or mobile layout was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived entirely from static CSS custom properties, a limited set of button-class declarations, a page-text excerpt, and a raw color/font list — no full page layout, grid system, or component markup was supplied. Semantic role assignments for many hex values (e.g., which greens/reds are truly "success"/"error" versus decorative) are inferred from typical patterns, not confirmed usage. Typography sizes for display-xl, display-md, title-md, body-md, body-sm, and caption are proposed defaults, since only `.btn` and `.btn-functional` font-size/line-height values were directly observed. No interaction states (focus, hover) beyond `.btn-primary`/`.btn-secondary` were supplied, and no mobile/responsive behavior was observed at all. Availability, licensing, and correct loading of proprietary fonts (Brown, Brown Pro, Hodinkee Social, Ivar Headline, Ivar Text, Portrait) have not been verified and should be confirmed against Hodinkee's actual font-hosting/licensing agreements before implementation.
