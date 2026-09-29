---
version: alpha
name: "Snap-on"
source_url: "https://snapon.com"
captured_at: "2026-09-28T04:19:42.677573+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Snap-on's public CSS surfaces a utilitarian, high-contrast palette built around a
  single saturated red (#ff0000), declared in :root as --color-brand-primary, paired
  with a darker red hover state (#990000/#900) and a near-black body ink (#282828) set
  on white canvas — a construction consistent with a trade-tool brand favoring
  conviction over ornament. Neutrals dominate structural chrome: light greys
  (#f2f2f2, #eeeeee, #dddddd, #cccccc) serve hairlines, panels, and disabled states,
  with #d3d3d3 explicitly used on a disabled submit button. Typography is pragmatic:
  Roboto and system Arial/Helvetica sans-serif stacks handle form fields and body
  copy, while several custom family names (MemphisBold, MemphisExtraBold,
  MemphisMedium, MemphisMediumItalic) appear in the stylesheet and are treated here
  as an inferred display typeface for headings — their availability and licensing
  are unverified. FontAwesome is present strictly as an icon font. Buttons show an
  observed, distinctive pattern: 1px border-radius, 10.5px uppercase label text,
  1px letter-spacing, and 500 weight — a compact, mechanical button language carried
  here into secondary variants. A rarely-seen navy (#203263) is included as an
  inferred accent for secondary wayfinding, since no confirmed CSS role exists for
  it. Layout, spacing, and breakpoints below are proposed conventions, not measured
  observations.

colors:
  primary: "#ff0000"
  primary-hover: "#990000"
  ink: "#282828"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#cccccc"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border: "#dddddd"
  disabled: "#d3d3d3"
  warning: "#ff9900"
  dark: "#1b1b1b"
  accent-navy: "#203263"
typography:
  display-xl: {fontFamily: "MemphisExtraBold, Arial, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "MemphisBold, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "MemphisMedium, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, Arial, Helvetica, sans-serif", fontSize: 10.5px, fontWeight: 500, lineHeight: 1, letterSpacing: 1px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    accent: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-sheet-table:
    backgroundColor: "{colors.surface-card}"
    hairline: "{colors.hairline}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.body-sm}"
    cellTypography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** reflects the observed CSS pattern directly: red fill, white text, a near-square 1px radius approximated here as `{rounded.xs}`, uppercase 10.5px letterspaced label, and 500 weight. Hover/active states are proposed to shift to `{colors.primary-hover}` since the stylesheet defines a brand-primary-hover token without showing the exact selector transition.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "view spec sheet"), inverting the primary's fill to keep the red as an accent stroke rather than a solid block, useful where multiple actions compete for attention on a product page.

**text-input** is proposed from generic form-field conventions; the CSS confirms Roboto/Arial usage on `.FAQ input`/`.SearchBox input` but not border color or padding, so hairline borders and compact padding are inferred defaults appropriate to a dense industrial-catalog interface.

**nav-bar** is proposed as a white bar with dark ink links and a red active/current-state indicator, consistent with the observed `#leftNav a.current { color:#000 }` and general `.titanBody a { color:#f00 }` link treatment, though exact top-nav structure is not confirmed from the supplied evidence.

**product-card** is a proposed pattern for a tool catalog: white surface, light border, and a title/body pairing using the inferred Memphis display family for names and Roboto for descriptions — no card markup was present in the supplied CSS, so dimensions and shadow are unstated.

**hero** is proposed as a dark, high-contrast banner using `{colors.dark}` (#1b1b1b) with the red accent reserved for a single call-to-action, appropriate to a heavy-equipment brand; no hero selectors were present in the evidence.

**footer** is proposed as a dark closing band echoing the hero's tone, keeping legal/utility links muted and only brightening on hover — a reasonable convention for reducing footer visual weight below primary content, not confirmed by evidence.

**badge** repurposes the observed `#ff9900` warning-orange swatch for status flags (e.g., "new," "clearance"), a role inferred from its presence in the palette rather than any confirmed badge selector.

**search** is proposed as a soft-grey input using `{colors.surface-soft}` (#f2f2f2), matching the general treatment of muted background panels seen across `.titanBody` variants, though no dedicated search-bar CSS was supplied.

**spec-sheet-table** is a category-appropriate proposed component for hand-tool specification listings (torque values, sizes, part numbers), using alternating soft-grey headers and hairline row dividers consistent with the observed `hr` and disabled-state grey tokens.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| compact | <600px | Single-column stacks; nav collapses to a toggled menu (proposed) |
| medium | 600–1024px | Two-column product grids; condensed nav (proposed) |
| wide | 1024–1440px | Full multi-column catalog layout (proposed) |
| max | >1440px | Content capped, generous margins (proposed) |

Touch targets should be at least 44px for buttons and nav items; the observed button padding (`9px 19px`) is likely desktop-sized and should be enlarged on touch surfaces. Navigation collapse and mobile menu interaction were not observed in the supplied CSS and are proposed only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/color/font extraction only; no live page rendering, computed layout, or interaction states were observed. Component structures (hero, product-card, nav-bar, footer, search, spec-sheet-table) are proposed conventions inferred from a category-appropriate hand-tools retail site, not confirmed markup. The role of `#203263` (accent-navy) is unconfirmed — it appears in the palette without a clearly associated selector. The Memphis-family fonts (MemphisBold, MemphisExtraBold, MemphisMedium, MemphisMediumItalic) are treated as an inferred display typeface; their actual usage, availability, and licensing on the live site are unverified. Font sizes and spacing values beyond the directly observed button typography (10.5px/500/1px letter-spacing) and root color variables are proposed placeholders for a coherent scale, not measurements. Mobile/responsive breakpoints and touch behavior are recommendations only.
