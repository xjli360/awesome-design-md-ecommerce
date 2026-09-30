---
version: alpha
name: "Brookline Booksmith"
source_url: "https://www.brooklinebooksmith.com"
captured_at: "2026-09-29T04:22:19.224160+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Brookline Booksmith's stylesheet exposes a compact palette anchored by a deep marine blue
  (--color-primary: #005a8c) and an even darker navy secondary (--color-secondary: #002f49),
  both declared as CSS custom properties at the root level — the clearest evidence of an
  intentional brand color system on the site. Surrounding these are conventional Drupal-theme
  neutrals (#ffffff, #fafafa, #333333, #dddddd, #5c5c5c) used for text, backgrounds, and
  hairlines, plus a wider incidental palette (greens, yellows, pinks) that appears tied to
  third-party widgets (cookie consent, calendar/event styling) rather than confirmed brand
  identity. This interpretation treats the navy pair as the bookstore's primary brand color
  and its darker hover/ink variant, reuses the neutral grays for body text and dividers, and
  proposes a soft off-white and light-gray pair for card and section surfaces. A muted green
  (#1a936f) is inferred as an accent for in-stock/staff-pick signaling, and a pale yellow
  (#fffa90) is inferred as a highlight for sale or event badges — both are educated proposals,
  not confirmed brand colors. Typography is built on the declared `sofia-pro` family for
  display and heading roles, falling back to the Arial/Helvetica/sans-serif stack observed on
  form widgets for body and UI text. Layout, spacing, and rounding values are proposed to suit
  an independent bookstore's dense, editorial, event-driven storefront.

colors:
  primary: "#005a8c"
  secondary: "#002f49"
  ink: "#232323"
  body: "#333333"
  muted: "#5c5c5c"
  hairline: "#dddddd"
  surface-soft: "#fafafa"
  surface-card: "#f6f6f6"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  accent: "#1a936f"
  highlight: "#fffa90"
  soft-alert: "#fddfdf"
  link: "#2581c4"
typography:
  display-xl: {fontFamily: "sofia-pro, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "sofia-pro, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "sofia-pro, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "sofia-pro, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.125rem, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
    metaTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  event-card:
    backgroundColor: "{colors.surface-soft}"
    accentBar: "{colors.accent}"
    dateTypography: "{typography.caption}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** uses the observed root `--color-primary` (#005a8c) as its fill with white
text, intended for primary calls to action such as "Add to Cart" or "RSVP." State transitions
(hover/active/disabled) are proposed, not observed in the supplied CSS.

**button-secondary** is an outlined variant reusing the same primary blue for border and text
on a transparent background, proposed for lower-emphasis actions like "See all items" links
seen throughout the event and staff-picks listings.

**text-input** is a plain bordered field using the neutral hairline gray and canvas white,
inferred from generic `.ui-widget input` Arial/Helvetica styling present in the CSS; no
site-specific input styling was supplied.

**nav-bar** is proposed as a white bar with a bottom hairline, holding the "Shop / Events /
About" mega-menu structure implied by the page text's navigation labels; no nav layout CSS was
observed, so structure is inferred from content only.

**product-card** represents the staff-picks and book-listing tiles referenced in the page text
(title, author, price, short blurb). Card surface, radius, and type scale are proposed;
observed CSS did not include book-grid-specific selectors.

**hero** is proposed as a dark navy band (secondary color) with large display type, suited to
a homepage banner image rotation implied by the repeated "Image Image Image" markers in the
page text; no hero CSS was directly observed.

**event-card** supports the dense events calendar (dates, times, venues, RSVP/Tickets links)
visible in the page text. The green accent bar is inferred, not confirmed, as a way to
distinguish in-store vs. off-site events.

**footer** reuses the darker secondary navy for a grounding footer band containing newsletter,
gift card, and "Work with Us" links; color pairing is proposed for contrast, not measured.

**badge** models small labels like "SOLD OUT" or "20% Off," using the pale yellow highlight
color found in the supplied palette; its association with sale/status badges is inferred, not
confirmed from observed component markup.

**search** reflects the site's visible "Search type: Books / Local Books / Merchandise"
control, styled as a simple bordered field consistent with the generic form-widget CSS
supplied.

## Responsive Behavior

Recommended, not measured, breakpoint table:

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | 0–599px   | Single-column stacks; nav collapses to hamburger/menu drawer |
| tablet    | 600–959px | Two-column product/event grids; nav may remain collapsed |
| desktop   | 960–1279px| Multi-column grids; full horizontal nav with dropdown sub-nav |
| wide      | 1280px+   | Max-width content container; additional whitespace, not new columns |

Touch targets should be at least 44×44px for buttons and nav items; the mega-menu structure
implied by "Shop sub-navigation / Events sub-navigation / About sub-navigation" suggests
collapsible accordion behavior on mobile. This table is a design recommendation only — no
actual responsive CSS or JavaScript breakpoints were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS and text extraction only; no rendered layout,
computed styles, or interaction states (hover, focus, active, disabled) were observed. The
`sofia-pro` font is asserted via a CSS custom property but its actual loading, weights, and
licensing (e.g., Adobe Fonts/Typekit) were not verified. Most non-primary/secondary colors in
the supplied palette (greens, yellows, pinks, extra blues) could not be confidently traced to
specific branded UI elements and may belong to third-party widgets (cookie consent, calendar
plugin) rather than the bookstore's own design system — their component assignments above are
explicitly inferred. All spacing, radius, breakpoint, and component-state values are proposed
defaults for an independent bookstore storefront and are not measurements taken from the live
site. Mobile menu behavior, cart/wishlist interactions, and search results layout were
referenced only in page text, not in supplied CSS, so their visual treatment is speculative.
