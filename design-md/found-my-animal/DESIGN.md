---
version: alpha
name: "Found My Animal"
source_url: "https://foundmyanimal.com"
captured_at: "2026-09-28T09:03:56.589830+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Found My Animal presents as a warm, editorial pet-lifestyle storefront layered onto a
  Shopify theme (evidenced by app.css scaffolding, side-panel and chat-widget variables).
  The observed palette centers on a warm off-white canvas (#f6f3ed, darkening to #f1ece3)
  paired with a near-black ink (#151515/#1c1c1c) for body copy and headings, bordered by
  soft neutrals (#e2e2e2, #dedede, #7b7b7b, #8a8a8a). A cluster of saturated accents
  (#ff6d2d, #e93636, #ff1876, #279a4b) appears in promo/sale banner context ("Treat
  Special," "BOGO50," sale badges) and is interpreted here as highlight/alert roles
  rather than a single fixed brand hue, since CSS variables define --color-accent as
  equal to --color-body (i.e., accent = ink, not a color). A star-rating orange
  (#fd9a52) is explicitly named in the source. Several blue/red/teal tones map to
  third-party payment-method iconography and are excluded from brand roles.
  Typography evidence is split: one rule set assigns "Archivo Narrow" to all
  headings/body text; a separate, more specific rule applies 'Brandon Grotesque
  Black'/'Brandon Grotesque' with !important to select elements; the base theme
  fallback is a system font stack. This design treats Archivo Narrow as the
  primary observed family and flags Brandon Grotesque as an unverified override.
  All sizes, spacing, and radii below are proposed conventions, not measured layout.

colors:
  primary: "#151515"
  ink: "#151515"
  canvas: "#ffffff"
  body: "#1c1c1c"
  muted: "#8a8a8a"
  hairline: "#e2e2e2"
  surface-soft: "#f6f3ed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-highlight: "#ff6d2d"
  accent-alert: "#e93636"
  star-rating: "#fd9a52"
  form-border: "#dedede"
  surface-darken: "#f1ece3"
typography:
  display-xl: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "0em"}
  title-md: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0em"}
  body-md: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0em"}
  body-sm: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em"}
  caption: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "12px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "0.1em"}
  button-md: {fontFamily: "'Archivo Narrow', sans-serif", fontSize: "13px", fontWeight: 600, lineHeight: 1.0, letterSpacing: "0.02em"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.form-border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.form-border}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
  product-variant-swatch:
    size: "32px"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.primary}"

## Components
**button-primary** is the ink-on-white-inverse call-to-action (Add to Cart, Shop Now), using the dark `primary` fill sourced from `--color-accent`/`--color-body`, which the CSS defines as identical values — proposed as the storefront's default button treatment.

**button-secondary** is an outline variant for lower-priority actions (e.g., "Shop All," filter toggles), keeping the same button typography but on a light canvas with a hairline border; state changes (hover/active) are proposed, not observed.

**text-input** reflects the theme's `--color-form-border` (#dedede/#e2e2e2 across two root definitions) as the resting border color, used for newsletter, search, and account forms; focus/error states are proposed.

**nav-bar** models the mega-menu structure implied by the page text (Dog Leashes, Essentials, Apparel, Wellness, Get Involved, Collaborations) as a light bar with hairline underline; dropdown/mega-menu open state is proposed since no interaction was captured.

**product-card** is inferred for leash/collar/harness listings, combining a card border, sm radius, and title/price typography split; hover elevation and quick-add affordances are proposed, not observed.

**hero** uses the warm off-white `surface-soft` background (`--bg-body: #f6f3ed`) observed as the page/body background, paired with large display type for homepage banners referencing sale and collection callouts.

**footer** is proposed as an ink-background block (inverting the light theme) for site-wide links (Mission, Our Factory, Adopt Us, Gift Cards) seen in the navigation text; this inversion is a stylistic proposal, not a captured footer screenshot.

**badge** covers sale/promo tags such as "BOGO50," "SALE," and "New," using `accent-highlight` (#ff6d2d) as a plausible attention color drawn from the observed non-neutral palette; exact badge usage per tag is inferred.

**search** is a pill-shaped input drawing on the `rounded.full` token and `form-border` color; no live search UI was captured, so layout is proposed.

**announcement-bar** directly reflects the observed top-of-page promotional strip content ("Free Shipping Over $50," "BOGO50," "Buy One Get One Free!") using the dark ink background for contrast against the light body.

**product-variant-swatch** is the category-appropriate component for collar/leash color or size selection, proposed as a circular swatch with a bordered selected state using `primary`; no swatch markup or colors were present in the supplied evidence.

## Responsive Behavior
A CSS custom-property fragment in the source (`small=0em&medium=48em&large=66.75em&xlarge=75em`) suggests approximate breakpoint intents rather than confirmed responsive rules:

| Token   | ~em   | ~px (16px base) | Proposed use |
|---------|-------|------------------|--------------|
| small   | 0em   | 0px              | base/mobile styles |
| medium  | 48em  | 768px            | tablet, nav collapses to hamburger (proposed) |
| large   | 66.75em | 1068px         | desktop nav/mega-menu (proposed) |
| xlarge  | 75em  | 1200px           | max content width (proposed) |

Touch targets are recommended at a minimum 44×44px for buttons and swatches; the side-panel tab buttons observed in CSS (`height:50px`) support a comparable minimum. Mobile nav collapse, mega-menu behavior, and cart drawer interactions are not observed and should be validated against the live site before implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, hover/focus states, or mobile viewport behavior was observed. Color roles are inferred from CSS custom-property names (e.g., `--color-accent` equaling `--color-body`) and promotional banner context, not from confirmed brand guidelines. Font usage is contradictory in the source: "Archivo Narrow" is asserted as both heading and body font in one rule block, a system font stack is the theme's underlying default, and 'Brandon Grotesque'/'Brandon Grotesque Black' appear in a separate !important override of uncertain scope — availability and licensing of Brandon Grotesque were not verified and it may be a paid/proprietary font. All pixel sizes in `typography`, all `rounded` and `spacing` scale values, and component padding/border details are proposed design conventions, not measurements. Payment-icon colors present in the raw palette (blues, reds, teals tied to card networks) were deliberately excluded from brand color roles.
