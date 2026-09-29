---
version: alpha
name: "Dang Foods"
source_url: "https://dangfoods.com"
captured_at: "2026-09-28T10:03:53.124320+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dang Foods presents itself as a playful, ingredient-forward snack brand rooted in Thai-American
  family recipes. The observed CSS root variables define a restrained brand-neutral base: white
  canvas (#ffffff), dark navy-black body text (#161d25), a muted blue-gray border (#849bb6), and
  a pale blue-gray accent (#c4cdd5). Layered on top of this base, per-section utility classes
  reveal three distinct category accent colors used for outlined buttons and headings: green
  (#289848) for "Story," magenta (#f51374) for "Why Keto," and gold (#ffb500) for "DangFinder."
  These three are treated here as brand accent roles rather than a single primary, since the site
  itself rotates them by content section. The remaining palette entries (orange #e35205, dark
  orange #dd4504, teal #aadddd, lime #b5d05d, pink-light #e793b7, yellow #ffff00, silver #c0c0c0,
  light gray #eeeeee, black #000000) are inferred as supporting flavor/badge accents typical of a
  multi-SKU snack line, since no selectors tie them to specific roles. Typography is drawn from
  the supplied webfont family names (Knockout condensed display weights, brandonGrotesque body
  weights); CSS also defines a Helvetica/Arial system fallback stack, noted here descriptively but
  not used as a typography token value since it is not among the enumerated observed families.

colors:
  primary: "#ffb500"
  secondary-green: "#289848"
  secondary-pink: "#f51374"
  ink: "#161d25"
  canvas: "#ffffff"
  body: "#161d25"
  muted: "#c0c0c0"
  hairline: "#849bb6"
  surface-soft: "#eeeeee"
  surface-card: "#c4cdd5"
  on-primary: "#ffffff"
  accent-orange: "#e35205"
  accent-orange-dark: "#dd4504"
  accent-teal: "#aadddd"
  accent-lime: "#b5d05d"
  accent-pink-light: "#e793b7"
  accent-yellow: "#ffff00"
  ink-strong: "#000000"
typography:
  display-xl: {fontFamily: "Knockout 29, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Knockout 27, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "brandonGrotesque-bold, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "brandonGrotesque-regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "brandonGrotesque-regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "brandonGrotesque-light, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "brandonGrotesque-medium, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.secondary-green}"
    borderColor: "{colors.secondary-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.accent-teal}"
    selectedBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** uses the gold accent (#ffb500) observed on the DangFinder section as a fill
color with white text, proposed as the site's primary call-to-action treatment (e.g. "Shop Now").
Hover/focus states are not measured but are proposed to darken or invert per the observed
outline-button hover pattern.

**button-secondary** is modeled directly on the observed `.btn-outline-primary` pattern: a
transparent fill with colored border and text that inverts to a solid fill with white text on
hover/focus, as literally shown in the Story-section CSS rules. Green is used here as the default
secondary accent; pink and gold variants are proposed for other sections.

**text-input** is a proposed pattern for account/newsletter forms (the site references sign-in and
account creation), using the observed border and ink colors since no input-specific CSS was
supplied.

**nav-bar** is proposed as a light, white-background bar reflecting the `--color-main-background`
and `--color-body-text` variables, since header markup/CSS was not directly captured in evidence.

**product-card** represents the repeated "flavor" tiles referenced in page text (Original Recipe,
Sriracha Spice, Caramel Sea Salt, etc.), using the pale blue-gray accent as a card surface tint and
the observed border color, both proposed layout choices not measured from live card markup.

**hero** is proposed for the homepage banner area implied by the rotating "Story / Why Keto /
DangFinder" content, using a soft neutral background with large display type.

**footer** is proposed dark-on-light-inverted using black (#000000) from the palette, reflecting
common footer treatments; the extensive footer link list (About, Blog, Careers, Policies) is
confirmed in page text but its visual styling is not.

**badge** is proposed for callouts like the "15% off" promo code shown in page text ("MAGIC"),
using the bright yellow palette entry as an attention accent, unobserved as an actual badge
component.

**search** and **flavor-selector** are proposed, category-appropriate patterns: search for a
generic site-search affordance, and flavor-selector for choosing among the many named product
variants (Thai Rice Chips, Coconut Chips flavors) referenced repeatedly in page text, using the
teal accent as an unselected-state border and gold as the selected-state indicator.

## Responsive Behavior

Recommendation only, not measured from live responsive behavior:

| Breakpoint | Width      | Layout notes (proposed) |
|------------|-----------|--------------------------|
| mobile     | <480px    | single-column, stacked nav collapses to menu icon |
| tablet     | 480–1024px| 2-column product grid, nav may remain inline or collapse |
| desktop    | >1024px   | 3–4 column product grid, full inline nav |

Touch targets are proposed at a minimum 44px height for buttons and nav items. Navigation
collapse behavior (hamburger menu) is standard practice for this category but was not observed in
supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is based solely on static CSS custom properties, a limited set of scoped
button/heading rules, and page text extraction — no live layout, computed styles, or DOM structure
were observed. Font family assignments use only the exact family name strings present in the
supplied evidence (Knockout weights, brandonGrotesque weights); the CSS-declared fallback stack of
`Helvetica, Arial, sans-serif` is noted descriptively but not encoded as a typography token since
those individual family names were not present in the enumerated font list. Actual rendering,
font-loading success, and licensing of Knockout/brandonGrotesque webfonts are not verified. Most
color-to-role assignments beyond the three explicitly scoped section accents (green/pink/gold) are
inferred from general palette availability, not confirmed selector usage. All spacing, rounding,
and typographic sizes beyond the root variables are proposed defaults, not measured values.
Component states (hover, focus, active, error, disabled) are proposed conventions except where
explicitly shown in the Story-section outline-button CSS. Mobile/responsive behavior is a
recommendation only.
