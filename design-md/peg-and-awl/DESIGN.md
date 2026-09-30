---
version: alpha
name: "Peg and Awl"
source_url: "https://pegandawl.com"
captured_at: "2026-09-29T04:12:53.571047+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Peg and Awl's supplied stylesheet evidence points to a warm, paper-toned
  studio aesthetic rather than a stark e-commerce look. The dominant surface
  is a soft off-white (#f9f6ef body background, #fcfbf7 secondary surface)
  paired with near-black ink (#1a1818, with pure #000 reserved for h1
  elements) and a muted gray (#707070) used for de-emphasized button text.
  A single mustard-gold (#ddba21) recurs across primary buttons and the
  third-party review widget's interactive states, functioning as the sole
  strong accent in the extracted evidence — inferred here as the brand's
  primary action color. Headline type is set in ITC Cheltenham Std at a
  light weight (300), giving a handcrafted, editorial tone consistent with
  the "treasures built from abandoned materials" positioning; body and
  button copy lean on ITC Franklin Gothic Std with wide uppercase tracking
  (3.2px), a workshop-label feel fitting for a leather-goods maker. A
  terracotta (#ae4f42) and a warm red (#bc676c) appear in the palette and
  are proposed here as secondary/sale accents, not confirmed from layout.
  Hairlines and card borders are modeled on the widget's #e5e5eb border
  token. This document treats font pairings and component shapes as
  interpretive proposals grounded in, but not screenshots of, the live site.

colors:
  primary: "#ddba21"
  ink: "#1a1818"
  ink-strong: "#000000"
  canvas: "#f9f6ef"
  body: "#1a1818"
  muted: "#707070"
  hairline: "#e5e5eb"
  surface-soft: "#fcfbf7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#ae4f42"
  accent-warm-red: "#bc676c"
  tan: "#e1d5c6"
  border-alt: "#dddddd"
  info: "#136f99"
typography:
  display-xl: {fontFamily: "ITC Cheltenham Std, serif", fontSize: 48px, fontWeight: 300, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "ITC Cheltenham Std, serif", fontSize: 40px, fontWeight: 300, lineHeight: 1.1, letterSpacing: normal}
  title-md: {fontFamily: "ITC Cheltenham Std, serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.25, letterSpacing: normal}
  body-md: {fontFamily: "ITC Cheltenham Std, serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: normal}
  body-sm: {fontFamily: "ITC Cheltenham Std, serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "ITC Franklin Gothic Std, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "ITC Franklin Gothic Std, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 3.2px}
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
    border: "1px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-strong}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  material-tag:
    backgroundColor: "{colors.tan}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** reflects the extracted `.btn--primary` rule directly: mustard-gold fill, white text, uppercase wide-tracked label. Its hover state (background transparent, text turns muted gray) is observed and should be preserved; the pill-like `rounded.full` mapping approximates the site's 19–25px radius relative to typical button height, since the fixed token scale has no exact match.

**button-secondary** mirrors the observed `.btn--secondary`, which shares the primary's border/radius/letterspacing but sits on a translucent off-white fill with muted-gray text — proposed here as the "quiet" action pattern for secondary CTAs like "Explore Our Jewelry."

**text-input** is inferred; no form-field CSS was supplied, so border, radius, and padding follow the widget's `--oke-border-color` hairline and general body spacing rhythm as a reasonable default.

**nav-bar** is proposed as a simple canvas-toned bar using the button typography for links (uppercase, tracked), consistent with the site's small link-navigation text ("SHOP / ABOUT / BLOG / LOGIN") though exact nav styling was not in the CSS evidence.

**product-card** is proposed for listing items like "The Hunter Satchel" or "Sendak Nutshell Artist Roll." White card surface with hairline border keeps focus on product photography; title uses the light-weight Cheltenham display style, price/description in body-sm.

**hero** models the homepage's large introductory statement ("Welcome to Peg and Awl!") using display-xl on the canvas background; actual hero image treatment and overlay were not present in the supplied CSS and are not claimed here.

**footer** groups the observed footer link categories (About, Customer Service, Wholesale, Newsletter) on the soft-surface tone with muted body-sm text and a top hairline, matching the site's dense multi-column footer text.

**badge** is proposed for callouts such as "Of a Kind" limited-collection labels or sale flags, using the terracotta accent as a warm, non-gold secondary signal distinct from primary CTAs.

**search** is inferred as a pill-shaped input consistent with the button radius language, since no search-bar CSS was supplied.

**material-tag** is a category-specific proposed component for leather/waxed-canvas material callouts (e.g. "Waxed Canvas," "Full-Grain Leather") using the tan neutral as a fabric-swatch-like background, appropriate to a leather-goods maker's product detail pages.

## Responsive Behavior

Recommended (not measured) breakpoints:

| Breakpoint | Width      | Layout guidance                                  |
|-----------|------------|---------------------------------------------------|
| mobile    | < 480px    | single column, nav collapses to menu icon (proposed) |
| tablet    | 480–1024px | 2-column product grid, hero text stacks above image |
| desktop   | > 1024px   | 3–4 column product grid, persistent top nav          |

Touch targets should be at least 44×44px for buttons using `{spacing.md} {spacing.xl}` padding, which comfortably meets this at the specified font sizes. Navigation is expected to collapse into a hamburger/menu pattern below tablet width; this is a UX-pattern recommendation, not an observed behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/text (including a secondary `pegandawlbuilt.com` theme asset and a third-party review-widget stylesheet), not from rendered/live layout, so component arrangement, spacing rhythm, and hero imagery are proposed, not observed.
- The body font declaration (`ITC Cheltenham Std` at line-height `.8`) appears to be a low-level reset value; actual running body copy may use `PT Serif` or `Baskerville`, both present in the font list but not tied to a specific selector in the supplied CSS — this mapping is uncertain.
- `Margaux Regular` / `Margaux All Caps` appear in the font list (likely a licensed/custom display or script font for the wordmark) but no selector or rendering evidence was supplied, so it is omitted from the typography scale rather than guessed at.
- Rounded-token mapping for buttons is an approximation: the true observed radii (19px, 25px) don't align exactly to the fixed `rounded` scale in this schema.
- Several palette hexes (near-transparent variants, e.g. `#f47b5f1a`, `#9ad82e2e`) were excluded as they read as overlay/shadow utilities rather than brand surface or text colors.
- No verified hover/focus/active states exist beyond the two documented in `.btn--primary:hover` / `.btn--secondary:hover`; all other interaction states above are proposed.
- Mobile menu behavior, product-grid column counts, and card imagery aspect ratios were not present in the supplied CSS and are marked as recommendations only.
- Font licensing/availability for `ITC Cheltenham Std` and `ITC Franklin Gothic Std` was not verified; these are proprietary ITC families and would require licensed webfont files in production.
