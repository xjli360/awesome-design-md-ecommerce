---
version: alpha
name: "Illoura the Label"
source_url: "https://illourathelabel.com"
captured_at: "2026-09-29T04:08:25.796908+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Illoura the Label's storefront CSS exposes a warm, paper-toned palette built
  around a cream background (#f5f1e9), a deep bark-brown ink (#2e2317), and
  white (#ffffff) surfaces, with a soft dusty-pink neutral (#dccfc7) and a
  light hairline grey (#dedede) rounding out the neutral set. Two
  Shopify-hosted custom web fonts are declared by internal identifiers,
  "Font-1675291683463" for h1–h4 headings and "Font-1675291779036" implied
  for body copy via the theme's font-body/font-heading variables; their
  actual family names, weights and licensing are not disclosed in the CSS and
  are treated here as unverified. Accent blue values (#1990c6, hover
  #136f99) appear on unbranded accelerated-checkout buttons, and are
  reused here as the primary interactive color. Sale/error red (#d72c0d)
  and a success green (#008060) are present as Shopify system tokens and are
  mapped to badge/status roles rather than primary brand actions, since no
  evidence ties them to core navigation or CTAs. Layout, spacing and
  component geometry are not observable from static CSS alone, so this
  document proposes a restrained, editorial system: generous whitespace,
  soft sharp-to-rounded corners, and letter-spaced small-caps-style
  navigation echoing the observed 10px, 0.06rem-tracked nav/button tokens.
  All sizing beyond the explicit 10px and 1.5rem body values is inferred and
  labeled as proposed.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#2e2317"
  canvas: "#f5f1e9"
  body: "#2e2317"
  muted: "#dccfc7"
  hairline: "#dedede"
  surface-soft: "#f5f1e9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark: "#121212"
  danger: "#d72c0d"
  success: "#008060"
typography:
  display-xl: {fontFamily: "\"Font-1675291683463\", sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"Font-1675291683463\", sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "\"Font-1675291683463\", sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "\"Font-1675291779036\", sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "\"Font-1675291779036\", sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  caption: {fontFamily: "\"Font-1675291779036\", sans-serif", fontSize: 10px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.06rem}
  button-md: {fontFamily: "\"Font-1675291779036\", sans-serif", fontSize: 10px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.06rem}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  size-guide-tag:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** carries the accelerated-checkout blue (#1990c6) with a
darker hover state (#136f99) drawn directly from Shopify's payment-button
CSS; here it is generalized to the main "Add to Cart" and "Shop Now"
actions. Square corners are proposed to match the brand's clean, editorial
feel; hover/focus/disabled states are proposed, not observed.

**button-secondary** is an outline variant using the ink color for text and
border on a white card surface, mirroring the theme's `.button--secondary`
rule which swaps background/border/text roles; exact border width is not
measured and is proposed at 1px.

**text-input** and **search** share a white surface with a light hairline
border (#dedede), sized for the small 10px navigation typography scale seen
in the CSS variables. Focus rings and validation states are proposed, not
observed in the supplied evidence.

**nav-bar** reuses the cream header background and dark ink foreground
explicitly set in `#shopify-section-header` (`--color-header-background`,
`--color-header-foreground`), rendered at the observed 10px navigation font
size with the observed 0.06rem letter-spacing from `body`.

**product-card** is a white surface for listing children's and women's
apparel (tees, skorts, crochet vests seen in page text), with modest
padding and a subtle corner radius; no card shadow or border was observed,
so none is asserted.

**hero** uses the soft cream surface for large campaign moments like "New
Arrivals" and "Live Like Flowers," set in the large display type driven by
the heading font variable; exact hero sizing/copy layout is not observed
and is proposed.

**footer** is proposed in the near-black (#121212) tone present in the
palette, paired with cream text, to visually anchor sign-up, i=Change
donation messaging, and Traditional Owners acknowledgment seen in the page
text; this dark-footer choice is an inferred stylistic pairing, not a
measured observation.

**badge** applies the Shopify system red (#d72c0d) for sale/sold-out
indicators referenced in the product text ("Sold out," "Sale price"); shape
and exact usage are proposed.

**size-guide-tag** is a small inferred component for the "Size Guide" link
found in customer-care navigation, using the muted dusty-pink tone as a
low-emphasis chip; this pattern is proposed, not observed as a
styled element.

## Responsive Behavior

Recommended breakpoints (not measured from the live site):

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | 0–599px    | Single-column product grid, collapsed hamburger nav |
| tablet    | 600–999px  | 2-column product grid, condensed nav |
| desktop   | 1000–1439px| Full horizontal nav, 3–4 column grid |
| wide      | 1440px+    | Max-width container, 4+ column grid |

Touch targets should be at least 44×44px per common accessibility
guidance; the observed 10px button/nav font size implies generous padding
is needed to reach that target, which is reflected in the proposed
`button-md` padding above. Header/nav collapse behavior, cart-drawer
interaction, and country/currency selector layout are not observed and are
proposed based on common Shopify theme conventions.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a handful of
selector rules, and page text; no live rendering, computed layout, or
interaction testing was performed. The two custom font identifiers
("Font-1675291683463," "Font-1675291779036") are Shopify-generated
placeholder names for uploaded web fonts — their true family names,
weights, and font licensing are unverified and could not be confirmed from
the evidence. Fallback stacks (Helvetica, Arial) appear in the raw CSS
variables but are omitted from the typography tokens above since only the
custom font identifiers are treated as confirmed observed families here.
All pixel sizes in `typography` other than the explicit 10px
navigation/button size and the 1.5rem body base are proposed estimates for
an editorial kidswear aesthetic, not measured values. Color-role mapping
(e.g., treating #1990c6 as the primary brand action color) is inferred from
its use on Shopify's generic accelerated-checkout button, not from a
brand-specific button rule. Mobile menu behavior, product grid density,
hover/focus states, and cart-drawer design were not present in the
supplied evidence and are therefore proposed rather than observed.
