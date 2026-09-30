---
version: alpha
name: "Dandelion Chocolate"
source_url: "https://dandelionchocolate.com"
captured_at: "2026-09-28T10:20:16.143712+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dandelion Chocolate's evidence shows a warm, artisanal palette built around a muted
  bronze-brown (#826d40) used as both --color-accent and --color-body, paired with a
  near-black ink (#151515/#333333) for headings and body copy. Backgrounds lean toward
  soft off-whites (#ffffff, #f9f7f2, #f5f1db) that evoke unbleached paper and cocoa
  packaging rather than a stark e-commerce white. A small set of secondary hues
  (gold #d3a741, terracotta #9b5a1d, green #279a4b) appear in the raw palette and are
  interpreted here as inferred accent/badge colors for origin tags and ethical-sourcing
  callouts, since no selector evidence ties them to a specific UI role.

  Typography is anchored by an observed serif display face, OPTICaslonBold-Cond, used
  at 34px/500 weight with wide letter-spacing on product titles -- a distinctive,
  editorial choice suited to a single-origin, "winemaker's approach" brand story.
  Garamond Premiere Pro appears in the font stack and is proposed here for secondary
  serif headings, while sans-serif system fonts (avenir, Open Sans, helvetica neue)
  are proposed for body and UI text, since no selector evidence pins body-copy fonts
  precisely. Buttons use a small 3px corner radius and 0.02em letter-spacing, observed
  directly from Shopify payment-button CSS, informing the button and input components
  below. Overall the interpretation favors restraint: warm neutrals, a single accent
  brown, and generous whitespace implied by the factory/café retail context.

colors:
  primary: "#826d40"
  ink: "#151515"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e9e9e9"
  surface-soft: "#f9f7f2"
  surface-card: "#f5f1db"
  on-primary: "#ffffff"
  border-form: "#dedede"
  accent-gold: "#d3a741"
  accent-terracotta: "#9b5a1d"
  accent-green: "#279a4b"
  bg-darken: "#f7f7f7"
typography:
  display-xl: {fontFamily: "'OPTICaslonBold-Cond', 'Garamond Premiere Pro', Garamond, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: 0.04em}
  display-md: {fontFamily: "'OPTICaslonBold-Cond', Garamond, serif", fontSize: 34px, fontWeight: 500, lineHeight: 1.0, letterSpacing: 0.04em}
  title-md: {fontFamily: "'Garamond Premiere Pro', Garamond, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.0em}
  body-md: {fontFamily: "avenir, 'Open Sans', 'helvetica neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.0em}
  body-sm: {fontFamily: "avenir, 'Open Sans', 'helvetica neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.15em}
  caption: {fontFamily: "avenir, 'Open Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "avenir, 'Open Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0.02em}
rounded:
  none: 0px
  xs: 2px
  sm: 3px
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
    padding: "{spacing.sm} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-form}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayTextColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaBorderColor: "{colors.on-primary}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-terracotta}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  origin-swatch:
    size: "48px"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    selectedRingColor: "{colors.primary}"

## Components

**button-primary** is modeled on the Shopify payment-button CSS, which directly shows a 48px-tall control with 3px radius, `#826d40`-derived accent background, and white label text; this is the highest-confidence component in the set.

**button-secondary** is a proposed outline variant inferred from the hero CTA rule that sets `color:#fff !important; border-color:#fff !important` on a dark background -- the neutral (non-hero) outline state on light backgrounds is not directly observed and is proposed for consistency.

**text-input** uses the observed `--color-form-border: #dedede` token; padding and radius are proposed, as no explicit input CSS was supplied.

**nav-bar** reflects the observed `.header { background-color:#f9f7f2; border-color:#ccccce }` rule; the soft off-white header on a hairline border is a real captured value, while spacing and mobile collapse behavior are proposed.

**product-card** draws its title typography directly from `.thb-product-detail .product-title` (OPTICaslonBold-Cond, 34px, letter-spacing .04em, color #333) and its price styling from `.product-price-container .price` (14px, letter-spacing .15em, color #666). Card background, border, and padding are proposed layout conventions for a grid of chocolate bar listings.

**hero** is proposed as a full-bleed dark section matching the image-with-text-overlay button rule (`color:#fff; border-color:#fff`), appropriate for the observed single-origin/factory imagery messaging; exact hero background color is not confirmed and `{colors.ink}` is used as a reasonable dark-overlay stand-in.

**footer** infers a soft-canvas footer (`#f9f7f2` or `#f7f7f7` darken token) with hairline dividers; the Klaviyo email-signup button rules confirm a `.footer` selector exists but reveal no visual footer styling beyond a transparent icon button, so layout is proposed.

**badge** is proposed to carry the "ETHICALLY SOURCED / BEAN-TO-BAR / DIRECT TRADE / KOSHER / SOY FREE / VEGAN" marquee text seen repeated in the page content, using a warm card background and terracotta text; no badge CSS was supplied, so styling is fully proposed.

**search** is a proposed minimal input matching the general input/border tokens; the site confirms a Search entry point in navigation but no search-field CSS was captured.

**origin-swatch** is the most concretely observed product-variant control: `.product-form__input--color input[type=radio]+label` is exactly 48x48px with an inset box-shadow border and a circular (`border-radius:50%`) color swatch inset 14px on each side -- interpreted here as an origin/flavor selector consistent with single-origin bar variants.

## Responsive Behavior

Recommended breakpoints (a proposed table informed by an observed CSS custom-property string `small=0em&medium=48em&large=66.75em&xlarge=75em` found in the evidence, suggesting the theme's own scale):

| Token  | Width    | Notes (proposed) |
|--------|----------|-------------------|
| small  | 0em      | Base mobile layout |
| medium | 48em (768px) | Nav collapses to hamburger; single-column product grid to 2-column |
| large  | 66.75em (~1068px) | 3–4 column product grid; full horizontal nav |
| xlarge | 75em (1200px) | Max content width, generous section padding |

Touch targets should be at least 44–48px, matching the one directly observed control size (the 48x48px color-swatch radio label). Navigation collapse, sticky header behavior, and mobile menu treatment are proposed conventions, not measured from the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text evidence and a title/meta excerpt; no rendered layout, computed styles, or interaction states were observed. Semantic color role assignments (e.g., which neutral is "ink" vs. "body", which of the gold/green/terracotta hues map to badges or alerts) are inferred from likely usage patterns, not confirmed by selector-to-role evidence. Font stacks for body copy (avenir/Open Sans/helvetica) are asserted from the raw font-family list but not tied to specific body-text selectors. OPTICaslonBold-Cond and SAF appear to be custom/licensed fonts whose availability, licensing, and web-font delivery were not verified. Breakpoint values are taken from a single ambiguous CSS custom-property string, not confirmed via media-query rules. All spacing, rounded-corner (outside the observed 3px button radius), hero, footer, badge, and search styling are proposed placeholders pending direct visual or DOM inspection. Mobile menu, hover/focus, and disabled-state interactions are not observed and should be validated against the live site before implementation.
