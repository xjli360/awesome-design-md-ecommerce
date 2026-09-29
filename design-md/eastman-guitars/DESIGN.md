---
version: alpha
name: "Eastman Guitars"
source_url: "https://www.eastmanguitars.com"
captured_at: "2026-09-28T10:24:27.961445+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from a NationBuilder-hosted Bootstrap theme rather
  than bespoke brand CSS, so the palette is dominated by neutral grays (#ffffff,
  #333333, #777777, #dddddd, #eeeeee) and standard Bootstrap alert colors
  (success/warning/danger/info). The one clearly non-utilitarian, saturated hue in
  the supplied evidence is #dd1144, which is treated here as the brand accent for
  primary actions; this is an inferred role, not a confirmed brand-guideline color.
  Typography is directly observed: body copy uses "neue-haas-unica" sans-serif at
  16px/1.7 with slight letter-spacing, while headings use "TTCommons-VarRoman"
  sans-serif at line-height 1.1 — a clean, editorial pairing suited to a
  craftsmanship-focused instrument maker. Given the product category (handcrafted
  acoustic guitars), the design system favors generous whitespace, restrained
  chrome, and photography-led layouts (hero banners for new models, dealer/warranty
  utility pages) rather than dense commerce grids. Card and surface tones reuse the
  observed light grays (#f5f5f5, #eeeeee) to separate content blocks without
  introducing new colors. All component patterns below are proposed conventions
  built from Bootstrap-era CSS evidence, not measured live-page observations.

colors:
  primary: "#dd1144"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  border: "#cccccc"
  accent-success: "#3c763d"
  accent-danger: "#a94442"
  accent-info: "#31708f"
  accent-warning: "#8a6d3b"
typography:
  display-xl: {fontFamily: "TTCommons-VarRoman, sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "TTCommons-VarRoman, sans-serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0"}
  title-md: {fontFamily: "TTCommons-VarRoman, sans-serif", fontSize: "22px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0"}
  body-md: {fontFamily: "neue-haas-unica, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.7, letterSpacing: "0.02em"}
  body-sm: {fontFamily: "neue-haas-unica, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.02em"}
  caption: {fontFamily: "neue-haas-unica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.02em"}
  button-md: {fontFamily: "neue-haas-unica, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.04em"}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — The dominant call-to-action treatment (e.g. "Learn More", "Shop Now", "Register") uses the accent color `#dd1144` as fill with white text. Hover/active states (darkening, underline) are proposed conventions, not observed in the supplied CSS.

**button-secondary** — An outlined variant for lower-priority actions ("View Specs", "Find a Dealer"), using a hairline border and ink-colored text on transparent background. Proposed for pairing with button-primary in hero sections.

**text-input** — Form fields such as those in the "Register Your Instrument" warranty form (First Name, Email, Postal Code, Country). Border and padding are proposed conventions consistent with the Bootstrap-derived theme; focus-state ring color is not confirmed in evidence.

**nav-bar** — A top-level navigation housing category links (Acoustic, Electric, Mandolin, Our Artists, Dealers, Store) and utility links (Vision, Care & Cleaning, FAQ). Background and text values are drawn from the observed body defaults; sticky/collapse behavior is proposed, not measured.

**product-card** — Used for instrument model tiles (e.g. archtop, dreadnought, parlor icons referenced in the evidence). A soft gray surface (`#eeeeee`) distinguishes cards from the white canvas without introducing new palette colors; rounded corners are proposed for a modern catalog feel.

**hero** — Full-bleed promotional banners for featured releases (Fullertone Offset, Lady Moon Signature, SB55 Olive Drab, T64-T Ice Blue Metallic) pairing large display type over a dark ink background for contrast; imagery and exact treatment are not confirmed from static CSS alone.

**footer** — A muted, low-contrast utility zone for social links (Facebook, Twitter, Instagram) and legal/dealer information, using the light surface-soft background and muted gray text observed in the theme's small/secondary text styling.

**badge** — Small status or "New" labels (e.g. "NOW AVAILABLE") using the observed info-blue (`#31708f`) as a pill-shaped indicator; this reuses Bootstrap's alert-info hue rather than a bespoke brand tag color.

**search** — A basic text-input variant for dealer or site search, styled identically to text-input; no distinct search-specific styling was present in the supplied CSS.

**spec-table** — Category-appropriate component for presenting acoustic guitar specifications (tonewoods, body shape, scale length) in a simple bordered row layout using hairline dividers and small body type, consistent with the site's documentation-style FAQ/Care & Cleaning content.

## Responsive Behavior
A proposed, non-measured breakpoint scheme suitable for a catalog/marketing site:

| Breakpoint | Width       | Behavior (proposed)                              |
|-----------|-------------|---------------------------------------------------|
| xs        | <576px      | Single-column stack, nav collapses to menu icon   |
| sm        | 576–767px   | Two-column product cards, hero text stacks        |
| md        | 768–991px   | Three-column product grid, inline nav emerges     |
| lg        | 992–1199px  | Full nav bar, four-column grids where applicable  |
| xl        | ≥1200px     | Max-width container, generous section padding     |

Touch targets should be at least 44px in the effective tap area for buttons and nav links. Navigation collapse to a hamburger/off-canvas pattern below `md` is a recommendation based on common Bootstrap-era conventions, not a confirmed behavior of this site. No live responsive layout, breakpoint values, or JavaScript interaction was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed layout, or DOM interaction was observed. The selection of `#dd1144` as the primary brand accent is an inference — its actual usage context (link, tag, or incidental UI element) is not confirmed in the supplied rules. Heading and body font sizes for `display-xl`, `display-md`, `title-md`, `body-sm`, `caption`, and `button-md` are proposed values, not measured from live typography scales. Spacing and rounded-corner tokens are proposed system defaults, not extracted from layout CSS. Custom font availability and licensing for "neue-haas-unica" and "TTCommons-VarRoman" were not verified and may require licensing confirmation before implementation. Component states (hover, focus, disabled, error) are proposed conventions only. Mobile/responsive behavior and interaction patterns were not observed and are recommendations based on common practice for catalog-style sites.
