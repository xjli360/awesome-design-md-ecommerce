---
version: alpha
name: "Lyre's"
source_url: "https://lyres.com"
captured_at: "2026-09-28T09:10:56.565478+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lyre's presents as a premium, editorial non-alcoholic spirits storefront built on a
  restrained navy-and-ivory palette. The confirmed root tokens set deep navy (#0c2340)
  as the heading and primary button color, pure white (#ffffff) as the base canvas, and
  a warm off-white (#f8f5ef, with a near-identical #f8f5f0 variant) as an alternating
  section background. A champagne-gold (#c3a767, with a deeper #be9546 variant) is used
  for link color and button hover states, giving the brand a refined, bar-forward
  accent against the navy. Body copy is set in pure black (#000000); a pale blue
  (#eaf1fb) token is declared as the general border/hairline color. Sharp geometry is
  explicit in the CSS: card, form, and block radii are all 0px while buttons carry a
  subtle 3px radius, together producing a crisp, label-like aesthetic. Oswald is the
  only font-family explicitly confirmed in the evidence, used uppercase on pricing
  text — its condensed, all-caps character is extended here (inferred) to headings and
  buttons. A serif fallback stack (Source Serif Pro / Iowan Old Style / Apple
  Garamond / Baskerville family) also appears in the evidence and is proposed
  (inferred) for longer-form editorial or recipe body copy, contrasting the
  condensed sans used for commerce UI. Status-like hues (#45a35d, #ff5454, #ffbd00)
  are treated as inferred availability/state colors rather than confirmed brand marks.

colors:
  primary: "#0c2340"
  primary-deep: "#102f55"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#252324"
  muted: "#808080"
  hairline: "#eaf1fb"
  surface-soft: "#f8f5ef"
  surface-card: "#f8f5f0"
  on-primary: "#ffffff"
  accent-gold: "#c3a767"
  accent-gold-deep: "#be9546"
  accent-navy-mid: "#1c5296"
  success: "#45a35d"
  error: "#ff5454"
  warning: "#ffbd00"
typography:
  display-xl: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: "70px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: "55px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: "30px", fontWeight: 500, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Source Serif Pro, Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, Times, serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "Source Serif Pro, Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, Times, serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.55, letterSpacing: "0px"}
  caption: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 3, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    hoverColor: "{colors.accent-gold}"
    height: "72px"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.caption}"
    priceColor: "{colors.primary}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  spirit-filter-tabs:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** — Navy-filled call-to-action ("Add to cart", "Shop All") using the confirmed `--button-background:#0c2340`; hover state (proposed, per `--button-background-hover:#c3a767`) shifts to gold. Radius reflects the confirmed 3px button token, rounded here to the nearest scale step.

**button-secondary** — An outline variant for lower-emphasis actions (e.g., "Select quantity" controls, secondary nav CTAs). Not directly observed as a distinct style; proposed as the inverse treatment of button-primary for consistency.

**text-input** — Form fields use the confirmed `--form-background:#f8f5ef` and `--form-border` tokens with a 0px radius, matching the declared `--form-radius:0px`. Placeholder/focus states are proposed, not observed.

**nav-bar** — The header exposes logo-width tokens (200px desktop, 150px at a narrower breakpoint) and a 14px menu font size, consistent with a slim, uppercase Oswald navigation bar. Currency/locale selector and account/cart icons are present in the evidence text but their exact visual treatment is inferred.

**product-card** — Bestseller grid items (e.g., "Classico Sparkling $22.99") pair a title with an uppercase 12px price label styled in Oswald and navy, matching the confirmed `.product-pricing .product-actual-price` rule. Card corners are sharp (0px radius confirmed).

**hero** — A full-bleed navy section proposed for top-of-page storytelling ("mindful drinking", award-winning range), using the largest confirmed heading scale (`--h1: 70px`) reduced for smaller breakpoints per the multiple `:root` overrides observed.

**footer** — Navy background with gold link accents, housing the extensive shop/recipe/about link architecture evident in the page text (About, FAQs, Frequent Sipper Club, social icons). Column layout is proposed, not measured.

**badge** — A pill-shaped accent label, proposed for merchandising callouts such as "Bestseller" or "Free shipping over $60"; a distinct `soldout` badge class exists in the CSS with its own background/color custom properties, though the resolved hex values were not present in the evidence.

**search** — Lightweight overlay/input matching the text-input treatment, proposed for the site search entry point implied by standard Shopify header patterns; no dedicated search CSS was present in the evidence.

**spirit-filter-tabs** — A category-appropriate pattern for the "Shop By Spirit" navigation (Gin, Rum, Bourbon, Tequila, etc.) and "By Occasion" recipe filters, styled as pill tabs using the gold/navy accent pairing; interaction states are proposed.

## Responsive Behavior

This is a recommendation derived from token hints (dual `--header-logo-width` values, a `--mobile-menu-font-size:24px` override, and stepped `--h1`/`--h2` scales), not measured site behavior.

| Breakpoint | Approx. width | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Header logo ~150px; mobile menu type scales to 24px; nav collapses to a full-screen drawer. |
| Tablet | 480–959px | Intermediate heading scale (`--h1` 40–50px tier observed in cascading `:root` overrides). |
| Desktop | 960–1279px | Header logo ~200px; `--h1` 60px tier. |
| Large desktop | ≥ 1280px | Largest heading tier (`--h1` 70px, `--h2` 55px). |

Touch targets on mobile should be at least 44px in the block dimension (aligned with the Shopify accelerated-checkout button's own `clamp(25px, 44px, 55px)` sizing observed in vendor CSS). Primary nav and filter tabs should collapse into a scrollable or drawer pattern below the tablet breakpoint; this is a proposed pattern, not confirmed by layout evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a limited set of selector-level rules, and page text — not a rendered or interactive audit. Specific limitations:

- No layout, grid, or component screenshots were available; hero, footer, product-card, and nav-bar structures are inferred from token names and page-text content, not visual observation.
- Font-family declarations were confirmed only for the product price element (Oswald) and a generic serif fallback chain surfaced elsewhere in the stylesheet; extension of Oswald to headings/buttons and the serif stack to body copy is inferred, not confirmed.
- Several hex values in the supplied palette (e.g., payment-network colors such as `#eb001b`, `#f79e1b`, `#1990c6`) originate from third-party Shopify checkout/wallet CSS and were deliberately excluded from brand role mapping.
- Exact `soldout` badge colors reference undefined custom properties (`--soldout-badge-bg/color`) whose resolved hex values were not present in the evidence.
- No hover, focus, active, error, or loading states were directly observed for buttons, inputs, or cards; all such states above are proposed.
- Responsive breakpoint pixel values are inferred from the presence of multiple cascading `:root` overrides, not from confirmed media-query widths.
- Font licensing/availability (e.g., whether Oswald is self-hosted or loaded via a web font service) was not verified.
