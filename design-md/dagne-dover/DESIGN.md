---
version: alpha
name: "Dagne Dover"
source_url: "https://dagnedover.com"
captured_at: "2026-09-28T05:03:57.713978+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dagne Dover's public CSS shows a restrained, editorial e-commerce palette built on
  white canvas (#ffffff), near-black text and button ink (#333333), and a muted grey
  body copy tone (#666666) set in nimbus-sans with Trebuchet MS and sans-serif
  fallbacks. Observed button rules define a pill-shaped, uppercase, letter-spaced
  (2px) 14px/14px bold label with a white-fill/dark-border default state and an
  inverted dark-fill hover state — this pattern is treated as the canonical button
  language. A small accent set appears in the palette (a pale lime #f4ff9c on
  .btn-accent, a terracotta #ba7361, a utility link blue #0051c1) but their exact
  UI roles are not confirmed by markup context, so they are mapped here as
  inferred secondary/accent tokens rather than primary brand color. Greys
  (#f7f7f7, #f5f5f5, #eeeeee, #cccccc) are inferred as surface and hairline tones
  for cards, section backgrounds, and dividers, consistent with a light,
  neutral, product-photography-forward layout typical of a structured bag/
  backpack catalog. No serif or display headline family was directly observed
  in rule declarations, so heading treatments below reuse the observed
  nimbus-sans stack and are marked as proposed, not measured.

colors:
  primary: "#333333"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#cccccc"
  surface-soft: "#f7f7f7"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-lime: "#f4ff9c"
  accent-terracotta: "#ba7361"
  link: "#0051c1"
  success: "#40954a"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "nimbus-sans, 'Trebuchet MS', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "nimbus-sans, 'Trebuchet MS', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "nimbus-sans-condensed, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
  body-md: {fontFamily: "nimbus-sans, 'Trebuchet MS', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "nimbus-sans, 'Trebuchet MS', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "nimbus-sans, 'Trebuchet MS', sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "nimbus-sans, 'Trebuchet MS', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    surface: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.overlay}"
    textColor: "{colors.on-primary}"
    ctaButton: "button-secondary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** reflects the directly observed `.btn` rule: white-on-dark contrast is inverted (dark fill, white text) for the highest-emphasis call to action such as "Shop Now" or add-to-bag actions, using the pill radius and uppercase letter-spaced label observed in the CSS.

**button-secondary** mirrors the observed default `.btn` state (white background, dark border and text) used for lower-emphasis actions like "Shop All" links; hover-state inversion to dark fill is proposed to stay consistent with the observed `.btn:hover` rule.

**text-input** is a proposed pattern for search and newsletter fields; no explicit input CSS was supplied, so border and radius values are inferred from the site's general hairline-grey and low-radius conventions.

**nav-bar** is inferred as a light, white-background top navigation consistent with body background rules and the flat, minimal button styling; underlying category flyout structure (Backpacks, Totes, Crossbody, etc.) is assumed from page text but its visual styling is not confirmed.

**product-card** is proposed for grid listings of items like the Dakota Backpack or Andre Backpack, using soft surface tones and title/price typography scaled from observed body copy; card shadow/border treatment is not evidenced and is omitted rather than invented.

**hero** models the homepage hero block, for which `#html-hero` rules were observed directly: transparent/outline buttons over imagery with a white-outline default and white-fill hover, here generalized with an overlay token for text legibility.

**footer** is inferred from the long footer link list in the page text (Customer Service, About, Social); background and link-blue color are drawn from the observed palette's `#0051c1` link swatch and neutral surface tones.

**badge** proposes use of the observed accent-lime `.btn-accent` color as a small promotional or "New" flag treatment, since no dedicated badge component was present in the supplied CSS.

**search** is a proposed pill-shaped search affordance matching the "SHOP WITH AI" / trending-search UI implied by the page text, styled with the same hairline border and full radius language as buttons.

**size-selector** is category-appropriate for backpacks sold in named sizes ("Large"); an active/inactive toggle state is proposed using the primary/on-primary inversion pattern already evidenced by the button hover rules, though no size-selector markup was supplied.

## Responsive Behavior

A compact, proposed breakpoint table (not measured from live site behavior):

| Breakpoint | Width | Nav | Product grid |
|---|---|---|---|
| Mobile | <600px | Collapsed/hamburger | 1–2 columns |
| Tablet | 600–1024px | Condensed horizontal | 2–3 columns |
| Desktop | >1024px | Full horizontal with flyouts | 3–4 columns |

Touch targets for buttons and size-selector chips should maintain a minimum 44px hit area, following the observed 42px button height on the hero signup control. Navigation collapse to a hamburger/drawer pattern below tablet width is a recommendation based on standard e-commerce conventions, not an observed interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed styles, or DOM interactions were observed. Semantic color roles (e.g., which grey is a true hairline vs. a surface fill) are inferred from usage context in class names, not confirmed via visual inspection. Heading typography sizes, weights, and the display font family are proposed defaults reusing the observed nimbus-sans stack, since no heading-specific CSS rule was supplied. Component states beyond the explicitly captured `.btn`, `.btn-dark`, `.btn-secondary`, `.btn-accent`, and `.btn-clear` rules (including nav-bar, product-card, footer, search, and size-selector) are proposed patterns only. Mobile/responsive layout, breakpoints, and touch behavior were not observed and are marked as recommendations. Availability and licensing of "nimbus-sans," "nimbus-sans-condensed," and "nimbus-sans-extended" as custom/licensed fonts were not verified beyond their appearance in the supplied font-family list.
