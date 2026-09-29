---
version: alpha
name: "RJ Julia Booksellers"
source_url: "https://www.rjjulia.com"
captured_at: "2026-09-29T04:06:22.935940+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from a limited static CSS extraction of rjjulia.com, an
  independent bookstore's Drupal-based (Bookworm theme) storefront. The only concretely
  observed font stack in the supplied CSS is "Arial, Helvetica, sans-serif," used on form
  widgets; a `--font-family: var(--font-serif)` custom property is referenced site-wide but
  its resolved value was not present in the evidence, so no serif family is claimed here —
  all typography below uses the observed Arial/Helvetica/sans-serif stack. The color
  evidence mixes true brand tokens (`--color-primary: #080808` near-black, `--color-secondary:
  #d8282f` a warm red) with third-party Klaro cookie-consent variables (#fafafa, #a0a0a0,
  #5c5c5c, #1a936f) and CMS/admin utility colors (Gin toolbar blues, form focus rings). This
  spec treats #080808 and #d8282f as the brand ink/accent pair, reuses the light grays for
  canvas and card surfaces, and infers hairline and muted roles from the mid-gray consent-UI
  palette since no dedicated border tokens were observed. Layout, spacing, radii, and
  component states are proposed conventions suited to a books/independent-retail storefront
  (staff picks grids, event listings, book-club services), not measurements taken from a
  live rendered page. All semantic role assignments below are labeled inferred where the
  source CSS did not name the role explicitly.

colors:
  primary: "#080808"
  accent: "#d8282f"
  ink: "#080808"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#5c5c5c"
  hairline: "#dddddd"
  surface-soft: "#fafafa"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  border-strong: "#a0a0a0"
  disabled: "#c8c8c8"
typography:
  display-xl: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.125, letterSpacing: 0.2px}
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
    borderColor: "{colors.primary}"
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
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceColor: "{colors.accent}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  staff-pick-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** uses the near-black `--color-primary` token observed in `:root` as its
fill, with white text for contrast; proposed for primary calls-to-action like "Add to Cart."
**button-secondary** is an outlined variant reusing the same ink color for text and border,
proposed for lower-emphasis actions such as "Add to Wishlist," with hover/focus states not
observed and left to implementation.

**text-input** is inferred from generic Arial/Helvetica form-widget CSS found in the Drupal
theme (`.ui-widget input`), giving a plain bordered field with a light hairline border;
focus-ring color was not clearly attributable to brand styling and is left unspecified.

**nav-bar** is a proposed pattern for the observed multi-level menu structure (Books, Kids,
Events, Services) described in the page text; no header layout CSS was supplied, so spacing
and sticky behavior are conventions, not measurements.

**product-card** models the "Staff Pick" book tiles referenced in the content (title, author,
price, blurb), using the accent red for price emphasis and a soft card background; card
shadows and hover elevation are proposed, not observed.

**hero** is a proposed full-width introductory band using the soft light background
(`#fafafa`) and largest display type, intended for the homepage banner imagery mentioned in
evidence ("Home Page Image"); no hero CSS rules were present in the source.

**footer** inverts to the primary near-black fill with white text, a common independent-retail
pattern; actual footer markup/CSS was not present in the supplied evidence.

**badge** and **staff-pick-tag** both draw on the accent red and soft-background tokens to
flag promotional or editorial content ("Staff Pick," "New & Noteworthy"); shapes (pill vs.
rectangle) are proposed conventions.

**search** reflects the "Search Search" utility control mentioned in the page text; a
mid-gray border (`#a0a0a0`, sourced from Klaro consent CSS) is reused here as the closest
observed neutral border tone, since no dedicated search-input CSS was supplied.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Layout notes (proposed)                         |
|-----------:|-----------:|--------------------------------------------------|
| mobile     | 0–599px    | Single-column nav collapses to hamburger; stacked product cards |
| tablet     | 600–959px  | 2-column product grid; nav may remain collapsed  |
| desktop    | 960–1279px | 3–4 column product grid; full horizontal nav      |
| wide       | 1280px+    | Max-width content container; extra gutter padding |

Touch targets should be at least 44×44px for nav links, cart, and wishlist icons. Navigation
sub-menus (Books, Kids, Events, Services) are recommended to collapse into accordion-style
disclosure on mobile widths. No JavaScript-driven interaction or actual mobile rendering was
observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a partial static CSS/text extraction and carries several
limitations. No page layout, computed hero imagery, or responsive breakpoints were directly
observed; all spacing, radii, and breakpoint values are proposed conventions appropriate to
an independent bookstore's e-commerce site. The brand's intended display typeface is
referenced only as an unresolved CSS variable (`--font-serif`), so this spec uses the sole
concretely observed stack, Arial/Helvetica/sans-serif, throughout; no proprietary or licensed
webfont was verified. A meaningful share of the supplied color palette originates from
third-party Klaro cookie-consent styling and Drupal/Gin admin-toolbar CSS rather than
customer-facing brand styling; colors judged most likely to be genuine brand tokens
(`#080808`, `#d8282f`) were prioritized for primary/accent roles, but this mapping is
inferred, not confirmed. No interactive states (hover, focus, active, disabled) were observed
in the evidence and are marked proposed. Component existence (product-card, hero, search) is
inferred from page-text content rather than directly observed markup or CSS selectors for
those elements.
