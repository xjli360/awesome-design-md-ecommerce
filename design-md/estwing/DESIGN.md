---
version: alpha
name: "Estwing"
source_url: "https://estwing.com"
captured_at: "2026-09-29T04:14:28.168211+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Estwing's public site uses a utilitarian, industrial-blue palette consistent
  with its identity as a 100-year-old American forged-steel tool maker. Two
  blues recur across button and heading rules: a deep navy (#003556) used for
  entry-title headings, and a mid-tone blue (#0067b1, also #2467b2) used for
  primary call-to-action buttons. Buttons observed in the source CSS are
  explicitly flat (border-radius: 0 !important), uppercase, bold, and set in
  'Open Sans' with Helvetica/Arial/Lucida/sans-serif fallbacks — this is the
  only font family with direct CSS evidence tied to typographic roles; all
  other listed families (Roboto, Segoe UI, system fonts, Font Awesome sets)
  appear only as icon or system fallbacks and are not used for brand type.
  Neutral slate tones (#334155, #64748b, #e2e8f0, #f1f5f9, #f8fafc) are
  inferred as body text, muted text, hairlines, and surface tints, since no
  body-copy color was directly captured. Warning/red tones (#dc2626, #cf2e2e)
  are treated as inferred error/alert accents rather than confirmed states.
  This interpretation favors squared corners, high-contrast navy-on-white
  headers, and bold uppercase CTAs, matching a rugged, made-in-USA tool brand
  rather than a soft consumer-retail aesthetic.

colors:
  primary: "#0067b1"
  secondary: "#2467b2"
  ink: "#003556"
  canvas: "#ffffff"
  body: "#334155"
  muted: "#64748b"
  hairline: "#e2e8f0"
  surface-soft: "#f1f5f9"
  surface-card: "#f8fafc"
  on-primary: "#ffffff"
  border-strong: "#cbd5e1"
  danger: "#dc2626"
typography:
  display-xl: {fontFamily: "'Open Sans', Helvetica, Arial, Lucida, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Open Sans', Helvetica, Arial, Lucida, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Open Sans', Helvetica, Arial, Lucida, sans-serif", fontSize: 26px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "'Open Sans', Helvetica, Arial, Lucida, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Helvetica, Arial, Lucida, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Open Sans', Helvetica, Arial, Lucida, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.5px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
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
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.border-strong}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  made-in-usa-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** renders the site's dominant CTA pattern (e.g. "Shop Now", "Learn More") using the observed flat, uppercase, bold button style with squared corners, matching the `border-radius: 0` and `text-transform: uppercase` rules found in source CSS.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Read More" story links), reusing the primary blue as border/text color on a transparent background; not directly observed but consistent with the bordered-button pattern already present.

**text-input** is inferred for search and form fields (e.g. the "promagnifier" search box), using neutral hairline borders and canvas background since no distinct input styling was captured in the evidence.

**nav-bar** represents the top navigation containing "Products," "Company," and "Resources" menus; canvas background and ink-colored text are inferred defaults, as no direct nav background/text color was captured.

**product-card** is proposed for hammer/tool category tiles (Hammers, Outdoor, Farrier Tools, etc.), using a soft card surface and hairline border to separate items on white canvas; card styling itself is not directly observed.

**hero** models the homepage banner ("Who's Behind Your Swing?", "New Titanium") on a dark ink background with large display type, an inferred treatment since only text content, not hero background color, was captured.

**footer** covers the multi-column footer (Quick Links, Follow Us, legal links) on the dark ink background, a proposed but plausible pairing given the brand's navy heading color.

**badge** and **made-in-usa-badge** are proposed small-label components for tags like "Officially Licensed" or the site's "Made in the USA" manufacturing claim, using pill and outline treatments respectively; neither badge styling was directly observed in CSS.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width      | Behavior (proposed)                              |
|-----------|------------|---------------------------------------------------|
| mobile    | <640px     | Single-column stack, nav collapses to menu icon   |
| tablet    | 640–1024px | Two-column product grids, nav remains collapsed   |
| desktop   | >1024px    | Multi-column grids, full horizontal nav visible   |

Touch targets should be at least 44px tall for buttons and nav items. The primary navigation is expected to collapse into a hamburger/off-canvas menu below tablet width, following common WordPress/Elementor conventions implied by the underlying block-editor CSS variables observed (`--wp--style--global--wide-size: 1200px`). This is a recommendation only; no actual responsive layout, breakpoint, or collapse behavior was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed styles, or DOM layout was observed. Semantic color roles (body, muted, hairline, surface tiers) are inferred from generic Tailwind-like slate values present in the palette, not confirmed against actual text or background usage. Typography sizes for display-xl, body-md, body-sm, and caption beyond the two directly observed heading rules (36px/600 and 26px/700) are proposed estimates, not measured. Component states (hover, focus, active, disabled) are proposed and unverified. Mobile/tablet layout and interaction behavior were not observed. The 'Open Sans' font's exact loading source, licensing, and availability were not verified from the supplied evidence, only its presence in font-family declarations.
