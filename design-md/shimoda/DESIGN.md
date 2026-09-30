---
version: alpha
name: "Shimoda"
source_url: "https://shimodadesigns.com"
captured_at: "2026-09-28T04:36:27.905941+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evidence points to a restrained, high-contrast neutral system built around
  a near-black call-to-action color (#191d1d) against a white canvas (#ffffff),
  with body copy set in #333333 and headings in #444444. Structural chrome —
  panel dividers, form borders, disabled states — draws from a tight gray
  scale (#e5e5e5, #999999, #cccccc), consistent with a utilitarian,
  gear-focused product site rather than a decorative consumer brand. The
  BigCommerce theme layer confirms "Satoshi" as the primary typeface, falling
  back to Arial/Helvetica/sans-serif, with a small positive letter-spacing
  (0.25px) on all headings and a 1.5 body line-height. Other family names
  present in the raw evidence (Montserrat, Mulish, Overpass, PlacardNext-Bold,
  Baskerville, Times) are not attached to any supplied selector and most
  likely originate from an embedded third-party catalog viewer (zmags); they
  are flagged as unverified rather than adopted as brand type. A muted olive
  green (#485b3d) appears in the palette and is treated here as an inferred
  accent — plausible for an outdoor/adventure-photography brand — but its
  role is not confirmed by any rule. The resulting interpretation favors
  flat 4px-radius controls, generous panel padding, and a monochrome-first
  UI with color reserved for status and accent moments.

colors:
  primary: "#191d1d"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#e5e5e5"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  heading: "#444444"
  border: "#999999"
  disabled: "#cccccc"
  accent: "#485b3d"
typography:
  display-xl: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.25px}
  display-md: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0.25px}
  title-md: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  body-sm: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Satoshi, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: normal, letterSpacing: normal}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  capacity-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the near-black `#191d1d` fill observed directly on `.button--primary`, with white text and the 4px corner radius shared across the theme's controls. This is the primary add-to-bag / checkout action.

**button-secondary** mirrors the observed outline `.button` base (transparent background, `#191d1d` border/text). The supplied CSS shows a hover rule that darkens the border to `#333` and flips text to white while leaving the background transparent — an unusual but directly observed quirk, reproduced here as a proposed secondary state rather than a designed intent.

**text-input** is proposed from the generic `button,input,optgroup,select,textarea{font:inherit;margin:0}` reset plus the `.form-body` border color (`#999999`); no dedicated input-field skin was supplied, so padding and radius are proposed.

**nav-bar** is inferred; no header/nav selectors were present in the evidence. It assumes a white canvas bar with hairline division, consistent with the theme's overall light surface.

**product-card** is proposed for camera-bag listings, using the neutral card/hairline pairing seen in `.form-body`/`.panel-header` (white surface, `#e5e5e5`-family divider) rather than any product-tile rule, which was not supplied.

**hero** is proposed as a full-bleed dark section using the same `#191d1d` tone as the primary button, appropriate for adventure-photography imagery with light overlay text; no hero markup or imagery rules were in evidence.

**footer** reuses the primary dark tone for a grounded, technical-gear footer band; no footer-specific selectors were supplied, so this is an inferred extension of the primary color role.

**badge** is proposed using the olive-green accent (`#485b3d`) pulled from the palette for status labels (e.g., "New," "Limited"), acknowledging this color's role is not confirmed by any rule.

**search** is proposed, styled like `text-input`, for a product/PDP search affordance appropriate to an ecommerce gear catalog.

**capacity-spec-table** is a category-appropriate proposed component for comparing bag capacity/weight/dimensions across the Shimoda lineup, using the soft gray surface (`#f3f3f3`) and hairline borders seen elsewhere in the theme for tabular/panel content.

## Responsive Behavior

The supplied evidence contains literal media-query breakpoint fragments (551px, 801px, 1261px, 1681px) from an embedded stylesheet; these are reproduced below as reference points, not confirmed as Shimoda's own site-wide breakpoints, since the associated selector context was not supplied.

| Token | Range | Notes (proposed) |
|---|---|---|
| xs | ≤551px | single-column stack, nav collapses to a toggle/menu |
| sm | 552–801px | two-column card grids begin |
| md | 802–1261px | primary tablet/small-desktop layout |
| lg | 1262–1681px | full desktop grid |
| xl | ≥1682px | max-width content with expanded margins |

Touch targets should be at least 44×44px (proposed, not measured). Below `sm`, primary navigation and filter panels are recommended to collapse into an off-canvas or accordion pattern. This table is a recommendation for implementation planning, not a measurement of Shimoda's live responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no live rendering, screenshots, or DOM interaction were observed. Color-to-role mapping (`accent`, `badge`, `hero`, `footer`) is inferred from generic palette presence, not from selectors confirming those uses — treat these as design proposals. Font family beyond Satoshi/Arial/Helvetica/sans-serif is uncertain: Montserrat, Mulish, Overpass, PlacardNext-Bold, Baskerville, and Times appear in the raw evidence without selector attribution and likely belong to a third-party embedded catalog/PDF viewer rather than the primary Shimoda site chrome. Font sizes across the typography scale are proposed except where the source CSS gave explicit values (button font-size 1rem/16px, heading letter-spacing 0.25px, body line-height 1.5). Breakpoint values are drawn from literal media-query strings in the evidence but their applicability to Shimoda's own responsive design is unverified. Interactive/hover/focus states are only directly evidenced for `.button` and `.button--primary`; all other component states are proposed. Licensing and availability of "Satoshi" as a web font were not verified.
