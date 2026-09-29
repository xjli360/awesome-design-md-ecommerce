---
version: alpha
name: "Porter Road"
source_url: "https://porterroad.com"
captured_at: "2026-09-28T09:47:29.471154+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Porter Road's site evidence points to a butcher-shop-modern aesthetic: a stark white
  canvas, near-black ink, and a single high-signal signal color (#ff3600, seen as
  `.button--orange` background) used for primary calls to action like "Add to cart"
  and "Try Now." Headlines use a bold condensed display face (CentralAvenue-Bold) set
  in uppercase with tight tracking, confirmed by the `.h1` rule (50px/45px,
  letter-spacing -1.5px). Body copy and buttons rely on Bau-Pro/Bau-Bold with
  Helvetica/Arial/sans-serif fallbacks, matching a DTC food-brand voice that is direct
  and utilitarian rather than decorative.
  Secondary palette entries (#777569, #3f3a36, #e7e7e7, #f9f8f4) are not tied to
  specific selectors in the supplied evidence, so they are interpreted here as muted
  text, hairline borders, and warm off-white section backgrounds — an inferred
  mapping consistent with the cream/kraft-paper cues implied by #fef9f2 and #fde8cd.
  A bright yellow (#fbfb2f/#fff12d) and reds beyond the primary orange (#d82c0d,
  #d02e2e) appear in the raw palette without confirmed selectors; they are proposed
  here as accent/promo and sale-badge colors respectively, to be validated against
  live markup. Buttons are low-radius (1px per `.btn`), all-caps, and letter-spaced,
  which this spec generalizes into a squared, high-contrast component language
  suited to a butcher/meat-delivery storefront.

colors:
  primary: "#ff3600"
  ink: "#252525"
  canvas: "#ffffff"
  body: "#3f3a36"
  muted: "#777569"
  hairline: "#e7e7e7"
  surface-soft: "#f9f8f4"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent: "#fff12d"
  success: "#66bb6a"
  error: "#d02e2e"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "CentralAvenue-Bold, Helvetica, Arial, sans-serif", fontSize: 50px, fontWeight: 700, lineHeight: 0.9, letterSpacing: -1.5px}
  display-md: {fontFamily: "Bau-Bold, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  title-md: {fontFamily: "Bau-Bold, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
  body-md: {fontFamily: "Bau-Pro, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Bau-Pro, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Bau-Pro, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Bau-Bold, Helvetica, Arial, sans-serif", fontSize: 10px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 2px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    position: "fixed-top"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.overlay}"
    panelBackgroundColor: "{colors.canvas}"
    inputComponent: "text-input"
    resultTypography: "{typography.body-sm}"
  price-per-lb-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.xxs}"

## Components
**button-primary** maps directly to the observed `.button--orange` rule (white text on `#ff3600`, 1px radius, uppercase, letter-spaced) and is proposed as the standard "Add to cart"/"Try Now" action.

**button-secondary** generalizes `.button--hollow`/`.button--black:hover` behavior (black border/text on transparent or white) into an outlined alternative for secondary actions like "See Details." Hover-state inversion is proposed, not confirmed live.

**text-input** is not directly styled in the supplied CSS beyond a generic reset (`button,input,optgroup,select,textarea{font-family:sans-serif}`); the hairline border, radius, and padding here are proposed defaults consistent with the button radius scale.

**nav-bar** reflects the confirmed `.header{position:fixed;background-color:#fff}` and active-link color `#252525`; drawer/mobile behavior is not observed and is proposed.

**product-card** is inferred from page-text evidence (product names, "$170 ~ $21/LB," "Add to cart," subscription framing) rather than a captured card selector; layout, border, and radius are proposed to match the button radius language.

**hero** is inferred from the homepage copy pattern (large uppercase claim + CTA) and uses the confirmed `.h1` display typography with a proposed soft-cream background for visual warmth.

**footer** is inferred from the link/payment-icon list in the page text; no footer background color was captured, so canvas white with a hairline divider is proposed rather than a dark footer.

**badge** is proposed for merchandising flags such as "Dry Aged," "Subscribe & Save," or "Bone-In," using the unconfirmed accent yellow from the raw palette; selector-level confirmation is not available.

**search** reflects the presence of a full-site search overlay ("Enter your search query… Type and press enter to search") in the page text; the scrim, panel, and result styling are proposed.

**price-per-lb-tag** is a category-specific component proposed for the "$21/LB" style secondary pricing seen in the excerpt, styled small and muted to sit beneath a primary price.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | single-column product grid, nav collapses to a hamburger + cart icon, hero stacks headline/CTA vertically |
| tablet | 600–959px | 2-column product grid, sticky header retained |
| desktop | ≥960px | 3–4 column product grid, full horizontal nav |

Touch targets should be at least 44×44px; the observed `.btn` padding (`20px`, `min-width:190px`) already satisfies this at desktop scale and should be preserved at mobile scale. Nav collapse and drawer/search-overlay interaction patterns are proposed and were not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were observed. Several palette entries (#fbfb2f, #fff12d, #d82c0d, #d02e2e, #81c784, #66bb6a, #1990c6, #136f99, #0099ff) had no associated selector in the supplied evidence, so their assigned roles (accent, error, success) are inferred and should be verified against live markup. Body text color (`{colors.body}`) is inferred from the raw palette (#3f3a36) rather than a confirmed body-text selector. Font availability and licensing for Bau-Bold, Bau-Pro, and CentralAvenue-Bold (proprietary/custom names) were not verified; fallback stacks (Helvetica, Arial, sans-serif) are used per the observed CSS. All typography sizes outside the confirmed `.h1` and `.btn` rules are proposed, not measured. Card, footer, badge, and search visual details are inferred from page text and generic Shopify theme conventions, not from captured selectors. Mobile layout, hover/focus states, and drawer/overlay animation were not observed and are marked proposed throughout.
