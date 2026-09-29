---
version: alpha
name: "Caterpillar"
source_url: "https://catfootwear.com"
captured_at: "2026-09-28T09:19:57.354656+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Cat Footwear's storefront CSS exposes an explicit black-and-white brand
  system through root custom properties: `--color-primary:#000`,
  `--color-secondary:#fff`, `--color-tertiary:#ffcd00`, and
  `--color-quaternary:#dadada`. The tertiary yellow (#ffcd00, with a close
  hover variant #ffcc00) reads as the Caterpillar equipment-yellow accent
  and is confirmed in interactive states (email-signup button hover, CTA
  hover backgrounds). Supporting neutrals (#f5f5f5, #f2f1ee, #cccccc,
  #999999, #333333) come from search-result panels, borders, and disabled
  states, and are repurposed here as surface, hairline, and muted-text
  roles — this mapping is inferred, not asserted by the source rules.
  #dc4405 and #e5b020 appear only in the raw palette without a bound CSS
  rule; they are treated as optional, low-confidence safety/highlight
  accents suited to a workwear category, not confirmed brand colors.
  Typography is anchored by three declared custom properties —
  "Mier-B-Bold" (primary), "Mier-A-Black" (secondary, heavier display),
  and "Mier-B" (tertiary/body) — each falling back through Arial,
  Helvetica, sans-serif. Buttons observed in CSS use uppercase text and
  fully-rounded (99em) or small-radius (5px) shapes; both are represented
  in the rounded scale below. Sizes, spacing, and breakpoints not directly
  measured are proposed and flagged as such throughout.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#f2f1ee"
  on-primary: "#ffffff"
  accent: "#ffcd00"
  accent-hover: "#ffcc00"
  highlight: "#e5b020"
  safety-accent: "#dc4405"
typography:
  display-xl: {fontFamily: '"Mier-A-Black", Arial, Helvetica, sans-serif', fontSize: 56px, fontWeight: 900, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: '"Mier-B-Bold", Arial, Helvetica, sans-serif', fontSize: 36px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: '"Mier-B-Bold", Arial, Helvetica, sans-serif', fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: '"Mier-B", Arial, "Helvetica Neue", Helvetica, sans-serif', fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: '"Mier-B", Arial, "Helvetica Neue", Helvetica, sans-serif', fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: '"Mier-B", Arial, "Helvetica Neue", Helvetica, sans-serif', fontSize: 10px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: '"Mier-B-Bold", Arial, Helvetica, sans-serif', fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.03em}
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
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayAccent: "{colors.accent}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    resultHeadingBackground: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    highlightColor: "{colors.highlight}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-pill:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderColor: "currentColor"
    rounded: "{rounded.full}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.lg}"

## Components
**button-primary** reflects the black-fill, white-text CTA confirmed by the email-signup button rule (`background-color:#000; color:#fff`), with an uppercase button typography style and a small corner radius consistent with the Apple Pay button's 5px radius. A hover state swapping to the accent yellow (#ffcc00) is observed on the signup button and can be proposed for other primary actions.

**button-secondary** is a proposed outline variant using the same ink color for border and text on a transparent fill, giving a lighter-weight action for secondary flows (e.g., "View Details") not directly observed but consistent with the primary button's shape language.

**text-input** is proposed for form fields (search box, email signup, checkout) using the neutral hairline border and canvas background; no explicit input CSS was supplied, so padding and radius are inferred from surrounding button/search patterns.

**nav-bar** represents the mega-menu header structure implied by the extensive Men/Work/Women/Sale navigation text, styled on a white canvas with black text and thin hairline dividers; exact height, sticky behavior, and dropdown animation are not observed.

**product-card** is a proposed pattern for PLP/PDP grids (not directly present in supplied CSS) using the soft off-white surface-card color and a moderate radius, intended to house product imagery, title, and price using the title-md and body-md type styles.

**hero** is modeled on the observed `#home-banner-247` promotional banner block, using a dark/ink background with white text and yellow accent overlay elements; the tooltip/CTA hover states (white background swap) are confirmed, but full hero copy layout is not observed.

**footer** is proposed as a black-background, white-text region echoing the primary/on-primary pairing used elsewhere on the page; link and hairline treatments are inferred from general site conventions, not measured footer CSS.

**badge** captures promotional flagging (e.g., "NEW ARRIVALS", "Site Exclusives", sale codes like FALLHAUL/60SALE referenced in page text) using the accent yellow fill with caption-scale uppercase type, proposed since no badge-specific CSS was supplied.

**search** reflects the confirmed `.site-search-results` styling: `#f5f5f5` result-heading background, `#cccccc` bottom border, and `#e5b020` highlighted match text, directly observed in the supplied selectors.

**category-pill** is drawn from `#home-main-shop-by-category .products .product .link-liner`, a fully-rounded (`border-radius:99em`) outlined button using `currentColor` for its border — mapped here to the full rounded token and reused for category/shop-by-type navigation entries.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | <480px | Single-column nav collapses to hamburger/drawer; category pills stack full-width. |
| tablet | 480–1024px | Two-column product grids; mega-menu likely condenses to accordion. |
| desktop | 1024–1440px | Full mega-nav with Men/Women/Sale columns as enumerated in page text. |
| wide | >1440px | Root `font-size-primary: 1.563vw` suggests fluid-scaling display type at large viewports. |

Touch targets for buttons and category pills should maintain a minimum 44px hit area; the pill component's observed `height:3.10895312em` supports this at typical base font sizes. This table is a design recommendation only — no responsive/mobile layout was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived solely from static CSS/text extraction of a single desktop-rendered page (`/US/en/home`); no JavaScript-driven states, mobile viewport rendering, or interaction sequences (hover/focus/active beyond the few rules supplied) were observed. Several palette entries (e.g., #dc4405, #e5b020, #8e8a7c, #2f547d) appear only in the raw color list without an associated selector, so their brand role is uncertain and treated as optional/inferred accents rather than confirmed system colors. All spacing, radius (beyond the 5px, 99em, and 50% values explicitly seen), breakpoint, and typographic size values not tied to a `--font-size-*` custom property or explicit CSS declaration are proposed estimates, not measurements. Font availability and licensing for the proprietary families referenced in `font_families` (Mier-A/B, Druk, NoeDisplay, PilatExtended) were not verified; generic sans-serif fallbacks are assumed to render in most environments. Component definitions for product-card, hero, footer, text-input, and button-secondary are extrapolated from adjacent evidence and general e-commerce convention, not directly confirmed by supplied selectors.
