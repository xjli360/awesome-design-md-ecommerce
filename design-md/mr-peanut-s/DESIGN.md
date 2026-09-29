---
version: alpha
name: "Mr. Peanut's"
source_url: "https://mrpeanutspetcarriers.com"
captured_at: "2026-09-28T09:36:45.869668+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Mr. Peanut's is a pet-carrier and travel-gear storefront built on a deep teal
  and warm neutral palette. The observed CSS root variables name a deep teal
  (#103a3a, restated as #134943/#124944 in card and button contexts) as the
  brand accent, paired with a rust/terracotta secondary (#c25b41) and a soft
  sage tint (#f3f8f1) used for supporting surfaces. Neutral ink tones range
  from near-black (#151515, #1c1d20) to mid greys (#616161, #6d6d6d), sitting
  on a white canvas with off-white panel backgrounds (#fafafa, #f6f6f6,
  #f3f3f3). A muted gold/brass (#b58b3a) appears as a card border accent,
  suggesting a premium trim color for badges or dividers.

  Typography is clearly split by observed rules: headings (h1–h6, logo text)
  use Rubik at weight 700, while body copy and product titles use Raleway at
  weight 500. Buttons and section-header controls use Figtree at 500 weight
  with a wide 0.2em letter-spacing, indicating an uppercase, spaced button
  treatment. Sizes beyond the two confirmed instances (14px controls, 26px
  section headers) are proposed and scaled from the theme's declared 1.05
  body-scale and 1.0 heading-scale variables. All rounding and spacing values
  are proposed conventions, not measured from the source, since no
  border-radius or spacing tokens were present in the supplied evidence.

colors:
  primary: "#103a3a"
  ink: "#1c1d20"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#616161"
  hairline: "#eeeeee"
  surface-soft: "#fafafa"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  teal-deep: "#134943"
  accent-rust: "#c25b41"
  accent-sage: "#f3f8f1"
  accent-gold: "#b58b3a"
  cream: "#f6f6f0"
  success: "#29845a"
  error: "#e93636"
  link: "#005bd3"
typography:
  display-xl: {fontFamily: "Rubik, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Rubik, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Rubik, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Raleway, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Raleway, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Raleway, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.0, letterSpacing: 0.2em}
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
    backgroundColor: "{colors.teal-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  compliance-badge:
    backgroundColor: "{colors.teal-deep}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.accent-gold}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** — Modeled on the observed `.button`-style rule that sets a `#134943` background with white text and a `#b58b3a` border; proposed as the default add-to-cart / checkout CTA using the Figtree button typography with its wide 0.2em tracking.

**button-secondary** — An outline variant inferred for lower-priority actions (e.g., "View Details"), reusing the primary teal as text/border color on a white field. Hover, focus and disabled states are proposed, not observed.

**text-input** — Inferred from the site's form-border variable (`--color-form-border: #dedede`, approximated here to the closer-matching `#eeeeee` hairline token) since no explicit input CSS was supplied; used for search fields, newsletter signup and checkout forms.

**nav-bar** — Proposed structure for the header/utility bar visible in the page text (country/currency selector, category mega-menu). Background and border are inferred defaults; actual sticky/collapse behavior was not observed.

**product-card** — Built from the `.featured-collection product-card` image rule (square 100% aspect ratio) plus the general body/heading font pairing; card chrome (border, radius, padding) is a proposed convention for the pet-carrier and stroller grid listings referenced in the nav taxonomy.

**hero** — Proposed banner treatment using the dark teal accent as a full-bleed background, appropriate for promotional messaging like the observed "Save Up To 25%... Spend > $100" bar. Copy hierarchy and imagery placement are not confirmed from static CSS.

**footer** — Uses the observed `--bg-color-side-panel-footer: #fafafa` token directly; link and label styling default to the muted grey and body-sm typography as a proposed pattern for multi-column footer navigation.

**badge** — General-purpose pill for tags such as "New" or "Sale," using the sage tint (`#f3f8f1`) noted in root variables as `--color-accent3`; color pairing is inferred, not tied to a specific observed badge rule.

**search** — Proposed pill-shaped search field for the header, since the site's large multi-brand/category taxonomy implies a search affordance; no dedicated search CSS was present in evidence.

**compliance-badge** — A category-specific component proposed for this brand's core value proposition (airline-compliant sizing). Combines the teal-deep background with the gold border color observed on a bordered card rule, signaling a "verified/certified" visual cue for under-seat carrier compliance callouts.

## Responsive Behavior

The theme settings string `small=0em&medium=48em&large=66.75em&xlarge=75em` was present in the supplied font/breakpoint evidence, suggesting the following approximate breakpoint scale (converted from em, browser default 16px):

| Token  | Width   | Notes |
|--------|---------|-------|
| small  | 0px     | Base/mobile |
| medium | 768px   | Tablet |
| large  | 1068px  | Small desktop |
| xlarge | 1200px  | Full desktop |

This is a **recommendation**, not measured site behavior. Suggested guidance: stack nav and hero content below `medium`; collapse the multi-column footer to an accordion below `medium`; switch product grids from 2-column to 3–4 column at `large`. Touch targets for buttons and nav items should maintain a minimum 44×44px hit area on mobile, consistent with the padding scale defined above, though this was not verified against live markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text evidence supplied for the homepage; no rendered layout, interaction states (hover/focus/active), or mobile breakpoints were directly observed. Font sizes beyond the two confirmed values (14px button/control text, 26px section header) are proposed extrapolations from the theme's declared scale variables, not measured. The semantic mapping of `ink`, `body`, and `muted` to specific greys is inferred from typical usage patterns since no explicit `color: ` rule for default body text was present in the evidence. Border-radius and spacing tokens are proposed conventions only, as no `border-radius` or margin/padding scale was present in the supplied CSS. Availability, licensing, and self-hosting terms for Rubik, Raleway, and Figtree were not verified — Google Fonts availability is assumed based on family names but not confirmed from source. Component states (disabled, error, loading) and exact grid/column counts for product listings are proposed patterns appropriate to the category, not confirmed observations of this specific site.
