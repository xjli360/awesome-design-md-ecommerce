---
version: alpha
name: "Banwood"
source_url: "https://banwood.com"
captured_at: "2026-09-28T09:58:35.633203+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Banwood's markup shows a Shopify-based storefront for Scandinavian-styled kids' balance
  bikes, trikes, scooters and helmets. The observed palette is dominated by near-black
  ink (#1c1c1c, #232323, #121212) against white and off-white surfaces (#ffffff, #fefefe,
  #e8e9eb, #dedede), with a small set of warm neutral browns (#5a4e46, #8f887c) likely
  tied to vegan-leather product accents rather than UI chrome. Sale/error red (#df3b3b,
  #dc3545) and a soft green (#41d38b, #74c587) appear in status/badge custom properties
  and are mapped here to sale and success roles. Payment-network colors (Mastercard,
  Amex, PayPal blues) and the Shopify accelerated-checkout blue (#1990c6) are excluded
  from brand semantics as third-party UI, not brand identity.

  Typography evidence lists Figtree and Nunito alongside system sans fallbacks; this
  spec assigns Figtree to headings/buttons for a clean geometric voice and Nunito to
  body copy for a rounder, friendlier read suited to a children's brand. Observed
  --text-* custom properties (12–20px) anchor the smaller type steps; larger display
  sizes are proposed. The accelerated-checkout button's default 0px border-radius and
  the black button--outline fill support a squared, high-contrast, minimal aesthetic
  used throughout this interpretation. Layout, breakpoints and hover/focus states are
  not observed and are marked as proposed.

colors:
  primary: "#1c1c1c"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#686767"
  hairline: "#dedede"
  surface-soft: "#e8e9eb"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  accent-clay: "#8f887c"
  accent-earth: "#5a4e46"
  success: "#41d38b"
  success-soft: "#74c587"
  error: "#dc3545"
  sale: "#df3b3b"
typography:
  display-xl: {fontFamily: "Figtree, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Figtree, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0.3px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    saleBackground: "{colors.sale}"
    saleText: "{colors.on-primary}"
    soldOutBackground: "{colors.surface-soft}"
    soldOutText: "{colors.muted}"
    customBackground: "{colors.primary}"
    customText: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
  age-fit-guide:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-earth}"
    successColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the site's dominant call-to-action (e.g. "SHOP NOW", "SUBSCRIBE NOW") as a solid near-black fill with white text, matching the observed `.button--outline` rule that forces `background-color: black !important; color: white; font-weight: bold`. Square corners (`rounded.none`) reflect the accelerated-checkout button's observed default `border-radius: 0px`.

**button-secondary** is proposed as an inverse/outline treatment for use on white backgrounds (e.g. filter toggles, secondary navigation actions), reusing the same ink border and typography for consistency; no distinct outline-on-light variant was directly observed.

**text-input** covers search and account/newsletter fields. Border and radius are proposed conservative defaults consistent with the site's flat, minimal button styling; no input-specific CSS was supplied.

**nav-bar** reflects the observed sticky header (`--header-is-sticky: 1`) and its two-row grid (`primary-nav / logo / secondary-nav`) with a 15%-opacity ink hairline (`--header-separation-border-color: 28 28 28 / 0.15`) mapped to `hairline`. Logo width tokens (100px/195px) were observed but exact breakpoint triggers were not.

**product-card** is proposed for the basket/pin and bike listing grids seen in the page text (e.g. "BANWOOD PIN & RIDE BASKET"), using the near-white `surface-card` tone and a light hairline border; card elevation/shadow was not observed and is omitted.

**hero** models the homepage slideshow/video block ("Unmute video... The perfect size for every child"), using the ink background and a 40%-opacity overlay derived from the observed `--page-overlay: 0 0 0 / 0.4` token; the transparent-fill `.button--outline` variant used inside the slideshow is treated as `button-secondary` on dark ground.

**footer** groups the observed footer link clusters (Shop, Support, Information, About Us) plus payment-method and legal text, using a soft neutral background and muted text; exact column widths are proposed, not measured.

**badge** encodes the sale, sold-out, and custom badge custom properties found in `:root` (`--on-sale-badge-background`, `--sold-out-badge-background`, `--custom-badge-background`), giving concrete, evidence-based colors for promotional and inventory states.

**search** is a proposed lightweight input/icon pairing for the observed "Open search" control; no distinct search-panel styling was supplied.

**age-fit-guide** is a category-appropriate, fully proposed component for helping caregivers match balance bikes/trikes to a child's age or height — a natural pairing with the "perfect size for every child" copy and the age-tiered navigation (Vintage/Icon Balance Bikes, Maxi/3-Wheel Scooters). It borrows the earthy accent and success-green tokens to signal a confirmed fit.

## Responsive Behavior

Recommendation only; no live breakpoints were measured.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, sticky header per `--header-is-sticky`, container gutter tightens toward `--container-gutter: 2rem`. |
| Tablet | 600–1024px | Two-column product grid; header grid shifts from stacked (`. logo secondary-nav` / `primary-nav primary-nav primary-nav`) toward the single-row `primary-nav logo secondary-nav` layout observed in custom properties. |
| Desktop | >1024px | Three+ column product grid; full-width gutter (`--container-gutter: 3rem`); logo width step to 195px as observed. |

Touch targets should be a minimum 44px height, consistent with the accelerated-checkout button's `clamp(25px, 44px, 55px)` sizing observed in Shopify's portable-wallet CSS. Primary nav should collapse to a drawer/menu below tablet width; this interaction was not observed and is a standard proposed pattern.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This spec is derived from static CSS custom properties, a page-text excerpt, and a color/font list — no rendered screenshots, computed layout, or interaction states were available. Semantic role assignments (e.g. `primary` = near-black, `muted` = mid-gray) are inferred from usage context (badge/button rules) rather than directly labeled brand tokens. Display-size typography (`display-xl`, `display-md`) and all `rounded` values beyond the checkout button's observed `0px` default are proposed, not measured. Spacing scale values are a standard proposed system; only the `--container-gutter`, `--section-vertical-spacing`, and `--section-stack-gap` rem values were directly observed and are not one-to-one with the fixed scale used here. Hover, focus, active, and error-input states were not observed. Mobile menu, drawer, and cart-panel layouts were not observed. Figtree and Nunito are used based on their presence in the supplied font list; their licensing, exact weights, and whether they are self-hosted or third-party loaded were not verified.
