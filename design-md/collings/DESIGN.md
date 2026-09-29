---
version: alpha
name: "Collings"
source_url: "https://www.collingsguitars.com"
captured_at: "2026-09-28T04:06:07.725048+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Collings' public markup exposes a restrained, high-contrast system: a near-black
  header (#020202) with white text and a hover state stepping to #141414, sitting
  above an off-white canvas (#f8f8f8) and black body copy. The one componentized
  color rule observed — .wp-block-button__link — uses a dark slate (#32373c) fill
  with white text and a fully pill-shaped 9999px radius, which we adopt as the
  primary action color given it is the only button treatment with explicit
  declarations in the evidence. Body copy runs in Montserrat at a loose
  1.89 line-height; Oswald appears in the observed font-family list but no rule
  ties it to a specific element, so its use for display type here is inferred,
  not confirmed. The broader supplied palette includes many values consistent
  with the WordPress/Gutenberg default editor palette (e.g. #cf2e2e, #fcb900,
  #9b51e0) rather than site-authored brand color; these are treated as
  incidental, not brand signals. A warm red-orange (#c02b0a) is present in the
  palette without an attached selector — we surface it only as a tentative
  accent candidate. The interpretation favors a quiet, editorial, photography-
  forward layout with a dark chrome header, generous whitespace, and sparing use
  of color, appropriate to a handmade-instrument brand where imagery of the
  guitars themselves should carry visual weight.

colors:
  primary: "#32373c"
  ink: "#000000"
  canvas: "#f8f8f8"
  body: "#000000"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  header: "#020202"
  header-hover: "#141414"
  accent: "#c02b0a"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.8888888889, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.3px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.header}"
    textColor: "{colors.on-primary}"
    hoverBackground: "{colors.header-hover}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.header}"
    overlayColor: "{colors.header}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.header}"
    textColor: "{colors.on-primary}"
    dividerColor: "{colors.header-hover}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  gallery-lightbox:
    backgroundColor: "{colors.header}"
    controlColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
---

## Components

**button-primary** reuses the one explicitly declared button treatment in the
evidence (`.wp-block-button__link`): a dark-slate fill, white text, and a fully
pill-shaped radius. Sizing follows the observed `1.125em` font-size and generous
horizontal padding.

**button-secondary** is a proposed outline variant for lower-emphasis actions
(e.g. "Learn More" links beside a primary CTA), inverting the fill to
transparent while keeping the same pill radius and type scale for visual
consistency. Not directly observed.

**text-input** is a proposed baseline form field style using the neutral
hairline border and card-white background seen elsewhere in the surface
palette; no explicit input styling was present in the supplied CSS beyond
reset rules (`background-color: transparent; color: inherit;`).

**nav-bar** reflects the observed `.main-header` (near-black background,
white text) and the observed hover/focus rule that shifts background to
`#141414` on secondary navigation items — this hover state is directly
evidenced. The mobile hamburger uses white 2px bars per `nav.header-nav
.menu-icon div`.

**hero** is inferred from the rule making `.main-header` transparent and
absolutely positioned on template-default and shoptour pages, implying a
full-bleed hero image sits behind a see-through header on landing-style
pages. Exact hero imagery, copy layout, and overlay opacity are not observed.

**footer** is a proposed pattern only, reusing the header's dark chrome for
visual bookending; no footer selector appeared in the supplied evidence.

**product-card** is a category-appropriate, proposed component for guitar
model listings (image, model name, short spec line), styled with the card
surface and hairline border tokens since no `.product-card`-equivalent
selector was supplied.

**badge** is a proposed small pill label (e.g. "Custom Shop," "New") using
the tentative accent color; its brand role is unconfirmed since no selector
ties `#c02b0a` to any component in the evidence.

**search** is a proposed rounded search field for a site-search affordance;
no search-specific selector was present in the supplied CSS.

**gallery-lightbox** is grounded in the observed `dialog[open]
.dialog-controls button` rule (white, absolutely centered control icon over
a dark surface), extended into a full lightbox pattern for guitar detail
photography — a reasonable fit for an instrument catalog, though the
surrounding dialog layout itself was not observed.

## Responsive Behavior

*Recommendation only — no responsive breakpoints, container queries, or
mobile layout were present in the supplied CSS evidence.*

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| sm        | 0–599px    | Single column; `nav-bar` collapses to hamburger menu (`#header-menus` toggled) |
| md        | 600–959px  | Two-column `product-card` grid |
| lg        | 960–1279px | Three-column grid; expanded nav visible |
| xl        | 1280px+    | Max-width content container; hero at full scale |

Touch targets for `button-primary`/`button-secondary` should maintain a
minimum 44px tap height given the pill padding tokens. The hamburger-to-menu
collapse pattern is inferred from `nav.header-nav .menu-icon` and
`#header-menus` selectors but the actual breakpoint at which this triggers
was not present in the evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS extraction only; no live
  rendering, computed layout, or DOM screenshots were available.
- Many palette entries (e.g. `#cf2e2e`, `#fcb900`, `#0693e3`, `#9b51e0`,
  `#8dff1c`) match default WordPress/Gutenberg editor swatches and are
  unlikely to be intentional brand colors; they are excluded from the
  semantic token set.
- The role of `#c02b0a` as an accent is unconfirmed — it appears in the
  supplied palette without an attached selector.
- Oswald's use for display typography is inferred from the observed
  `font_families` list; no rule in the evidence assigns it to a specific
  element.
- All pixel sizes in the typography, rounded, and spacing scales beyond the
  one observed `font: 400 1rem/1.8888888889 "Montserrat"...` and `1.125em`
  button size are proposed defaults, not measured values.
- Hero, footer, product-card, badge, and search components are proposed
  patterns inferred from partial or absent selectors; actual page structure,
  mobile navigation behavior, and interaction states (focus rings, disabled
  states, form validation) were not observed.
- Font licensing/availability for Montserrat and Oswald was not verified
  beyond their appearance in the site's declared font stack.
