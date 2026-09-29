---
version: alpha
name: "Nakamichi"
source_url: "https://nakamichi-usa.com"
captured_at: "2026-09-28T04:27:30.091621+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Nakamichi's evidence points to a dark, high-contrast home-theater aesthetic layered over a warm burnt-orange primary (#c85000) accent, with pure black and near-black surfaces (#000000, #161616, #1c1b1c, #272626) dominating the observed palette. Supporting neutrals span from white (#ffffff) through mid-grays (#797676, #adaaaa, #c9c6c5) to soft off-whites (#fafafa, #f0f0f0), suggesting a UI that alternates between deep cinematic backgrounds and lighter content panels. A secondary red (#ed1c24) and a muted green (#12753a) appear in the palette and are treated here as inferred status/accent colors (e.g., alerts, ratings, promotional badges) rather than primary brand colors. A gold/amber tone (#ffc338) is mapped as an inferred rating-star or highlight color, consistent with the "#1 Rated" review-driven positioning in the page title.

  Typography is grounded in two observed families: "Red Hat Text" for body and UI copy (confirmed via CSS custom properties and fallback declarations), and "Basement Grotesque" for display headings (referenced as var(--font-display)). Fallback stacks use only generic sans-serif per platform convention; no specific fallback family names are asserted as brand-approved. Sizing scale (body-large 22px, body-medium/regular 17px, body-small 14px) is directly observed; display and title sizes are proposed extrapolations consistent with a bold, product-hero-driven e-commerce layout. Rounded and spacing scales are inferred conventions for a modern audio/electronics storefront, not measured from source.

colors:
  primary: "#c85000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#161616"
  muted: "#797676"
  hairline: "#adaaaa"
  surface-soft: "#fafafa"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  ink-secondary: "#1c1b1c"
  panel-dark: "#272626"
  panel-darker: "#313030"
  border-subtle: "#c9c6c5"
  text-faint: "#e5e1e1"
  accent-amber: "#ffc338"
  accent-red: "#ed1c24"
  accent-green: "#12753a"
  overlay-scrim: "#000000cc"
typography:
  display-xl: {fontFamily: "Basement Grotesque, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Basement Grotesque, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Red Hat Text, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Red Hat Text, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Red Hat Text, sans-serif", fontSize: 14px, fontWeight: 900, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Red Hat Text, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.1px}
  button-md: {fontFamily: "Red Hat Text, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.border-subtle}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
    hairline: "{colors.panel-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    overlay: "{colors.overlay-scrim}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-secondary}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    hairline: "{colors.panel-dark}"
  badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.border-subtle}"
    padding: "{spacing.sm} {spacing.base}"
  review-rating:
    backgroundColor: "transparent"
    textColor: "{colors.accent-amber}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components
**button-primary** is the core call-to-action element (e.g. "Shop Now," "Add to Cart"), using the observed `--primary` orange against white text; proposed hover/active/disabled states are not confirmed from static CSS. **button-secondary** provides an outlined alternative for lower-emphasis actions, inferred from the neutral hairline/border tokens present in the palette. **text-input** and **search** share a light-surface pattern suited to a dark-themed storefront, using soft-white backgrounds so form fields remain legible against black page chrome; focus-ring styling is proposed, not observed. **nav-bar** is modeled as a dark header bar consistent with the near-black tones dominating the palette, carrying small bold body text for menu items. **product-card** uses the lighter surface-card token to visually separate product tiles from a darker page background, a common pattern for electronics retail though not directly confirmed via layout evidence. **hero** represents the top-of-page banner area, pairing display typography with a dark background and scrim overlay (using observed `#000000cc`) to support text legibility over product photography — this composition is inferred from the page title's marketing framing, not from measured DOM structure. **footer** reuses the darker panel tone with muted-gray body text, typical of e-commerce footers listing links and legal copy. **badge** and **review-rating** are inferred from the "#1 Rated" title copy and the presence of an amber tone in the palette, proposed as a ratings/promo indicator rather than a confirmed UI element.

## Responsive Behavior
Recommended (not measured) breakpoints: mobile up to 640px, tablet 641–1024px, desktop 1025px+. Touch targets should maintain a minimum 44px height for buttons and nav items on mobile. Navigation is proposed to collapse into a hamburger/drawer pattern below the tablet breakpoint, with product-card grids stepping from a single column (mobile) to 2–3 columns (tablet) to 4+ columns (desktop). All breakpoint values and collapse behavior are proposed conventions, not observed from the live site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/token extraction only; no rendered page, JavaScript-driven interaction, or mobile viewport was observed. Semantic color roles (e.g., which grays serve as body vs. muted vs. hairline) are inferred from typical usage patterns in the supplied hex list, not confirmed via applied selectors. Sizing for display-xl, display-md, title-md, caption, and button-md typography is proposed and extrapolated from the confirmed body-large/medium/small scale; only those three body sizes and their weights are directly evidenced in the CSS rules. Rounded and spacing scales are conventional proposals, not extracted from source. Availability, licensing, and web-font loading of "Basement Grotesque" and "Red Hat Text" were not verified beyond their appearance as CSS variable references. No hover, focus, active, or error states were observed; all interactive states beyond base styling are proposed placeholders for future validation against live markup.
