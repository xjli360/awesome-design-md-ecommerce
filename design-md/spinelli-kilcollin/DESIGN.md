---
version: alpha
name: "Spinelli Kilcollin"
source_url: "https://www.spinellikilcollin.com"
captured_at: "2026-09-29T03:59:41.769858+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in a near-monochrome palette observed across computed
  button, body, and heading styles: pure black (#000000) and near-black graphite (#222222)
  for ink and primary actions, soft off-whites (#f9fafa, #f5f3f4) for canvas and card
  surfaces, a deeper charcoal (#444443) for muted text, and semi-transparent white/black
  overlays (#ffffffcc, #ffffff66, #000000cc) used for scrims, focus states, and lightbox
  chrome (evidenced in the .yarl__button gallery styles). The single observed typeface
  stack, inferi with an "inferi Fallback" and Georgia/serif fallback, is a custom brand
  serif; its pairing with Georgia suggests an editorial, fine-jewelry tone, so this spec
  treats inferi as the display/body serif and reserves a generic sans only as an inferred
  UI fallback for form controls.

  The proposed design language is restrained luxury: a black-and-ivory field, thin
  hairlines instead of heavy borders, low-contrast surface tiers (#f9fafa over #ffffff),
  and black-on-off-white or off-white-on-black buttons mirroring the sampled button
  colors (rgb(34,34,34), rgb(249,250,250), and solid-black backgrounds). Layout details
  such as spacing scale, radii, and breakpoints are not present in the evidence and are
  therefore proposed defaults consistent with a minimal jewelry storefront, not
  measurements of the live site.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#444443"
  hairline: "#f5f3f4"
  surface-soft: "#f9fafa"
  surface-card: "#ffffff"
  on-primary: "#f9fafa"
  overlay-scrim: "#000000cc"
  overlay-light: "#ffffffcc"
  overlay-faint: "#ffffff66"
typography:
  display-xl: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.25px}
  display-md: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 34px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.2px}
  title-md: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "inferi, 'inferi Fallback', Georgia, serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.8px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    caption: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  appointment-cta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.xl}"
    border: "1px solid {colors.hairline}"

## Components

**button-primary** renders the solid-black, off-white-text button pattern evidenced by the sample button (background rgb(0,0,0), text rgb(249,250,250)); used for "SIGN UP," "ACCEPT," and primary checkout/add-to-cart actions. Hover/active states are proposed, not observed.

**button-secondary** is an outlined, ink-on-white variant for lower-emphasis actions such as "MODIFY," "VIRTUAL APPOINTMENT," or "REQUEST A SIZER," using the rgb(34,34,34) text color repeatedly sampled across button instances.

**text-input** covers newsletter/SMS signup and search fields implied by "Join Our Circle" and the country-selector list; a soft off-white fill with a thin hairline border keeps forms visually quiet against the mostly black-and-white palette.

**nav-bar** is a proposed persistent header holding utility links (Visit Us, Request a Sizer, Virtual Appointment, Cart) seen in the page text; a white background with a single hairline rule keeps focus on product imagery below.

**product-card** represents the repeated collection tiles (Halley, Solarium, Acacia, Tigris, etc.) implied by the best-sellers list; a plain white card with a thin border and small caption typography suits dense jewelry grids without competing with metal/gem photography.

**hero** models the "Welcome to Wren" / "The Wren Collection" banner: full-bleed imagery with a black or scrim-darkened background and large serif display type in off-white, matching the sampled h1 color rgb(249,250,250).

**footer** consolidates the observed link groups (Contact, Careers, FAQ, Stockists, Journal, Shipping + Returns, legal links) into a light footer with muted body-sm text and a top hairline, keeping legal/utility content visually subordinate.

**badge** is a proposed small pill (e.g., "New," "One of a Kind") for marquise/limited pieces referenced in the text ("one of a kind marquise collection"); no badge styling was directly observed, so color and shape are inferred from the muted graphite tone.

**appointment-cta** is a category-appropriate module for "Make An Appointment / For a personalized experience in-store or virtually," styled as a bordered off-white panel with title-md serif type, reflecting the brand's showroom-driven, appointment-based retail model for fine jewelry.

## Responsive Behavior

Proposed breakpoints (not measured from the live site):

| Breakpoint | Width | Layout intent |
|---|---|---|
| mobile | <480px | Single-column hero, stacked nav behind a menu icon, 1-up product cards |
| tablet | 480–1024px | 2-up product grid, condensed nav bar, collapsible country/region selector |
| desktop | 1024–1440px | 3–4 up product grid, full horizontal nav, side-by-side hero copy/image |
| wide | >1440px | Wider section padding ({spacing.section}), 4+ up grids for collection pages |

Touch targets should maintain a minimum 44px height for buttons and nav links; the long country-selector list should collapse into a searchable dropdown on small viewports. All breakpoint values and collapse behaviors are recommendations only, not observed responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/computed-style snapshots and page text only; no live rendering, DOM interaction, or JavaScript-driven states were observed. Font sizes, weights, letter-spacing, spacing scale, and border-radius values are proposed defaults, not measured from the site. The mapping of specific hex values to semantic roles (e.g., which off-white is "surface-soft" vs. "on-primary") is inferred from limited computed-style samples and may not match every real component. Hover, focus, active, disabled, and error states beyond the `.yarl__button` lightbox examples were not observed. Mobile menu behavior, cart drawer layout, and country-selector interaction are not observed. The custom "inferi" font's availability, loading strategy, and licensing were not verified; Georgia/serif is assumed as the safe fallback per the supplied font stack.
