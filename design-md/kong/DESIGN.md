---
version: alpha
name: "Kong"
source_url: "https://kongcompany.com"
captured_at: "2026-09-28T04:47:03.033032+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  KONG's storefront runs on a stock BigCommerce Stencil theme, so the extracted CSS shows a neutral, utilitarian foundation (white canvas, near-black type, gray hairlines) carrying one clear brand accent: a saturated red (#d61b37) used for primary buttons and cart-caption overlays, deepening to #961024 on hover/active. Typography pairs Jost for body copy with Oswald for headings and buttons — both are observed via explicit font-family declarations, with Arial/Helvetica/sans-serif as measured fallbacks. Other family names in the raw evidence (Comic Relief, Montserrat, Mulish) appear in the CSS bundle but are not tied to any selector in the supplied rules, so they are omitted from the typography system as unverified.
  The broader palette (golds, oranges, blues, greens) reflects seasonal/category badges (Halloween, 50th-anniversary gold) and BigCommerce form-state colors (success/info/warning tints) rather than core brand identity; this spec treats the red/black/white/gray set as primary and reuses the remaining hues sparingly for promotional and status accents, with those role assignments marked inferred. Radii and spacing follow the single observed 4px button/pagination radius, extended into a proposed scale. Layout, responsive behavior, and hover/focus states beyond the two documented button rules are proposed patterns for a chew-toy/pet-product storefront, not confirmed observations.

colors:
  primary: "#d61b37"
  primary-hover: "#961024"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#e5e5e5"
  surface-soft: "#f2f2f2"
  surface-alt: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border: "#8f8f8f"
  border-strong: "#474747"
  disabled: "#cccccc"
  text-muted-btn: "#666666"
  gold-accent: "#e6a700"
typography:
  display-xl: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0.25px}
  display-md: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.25px}
  title-md: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "Jost, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Jost, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Jost, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "Oswald, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: normal, letterSpacing: 0px}
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
    border: "1px solid {colors.primary}"
    hover: {backgroundColor: "{colors.primary-hover}", borderColor: "{colors.primary-hover}"}
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.text-muted-btn}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border}"
    hover: {borderColor: "{colors.border-strong}", textColor: "{colors.body}"}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border}"
    padding: "{spacing.sm} {spacing.md}"
    focus: {borderColor: "{colors.primary}"}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.body}"
    linkTypography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** is the confirmed, evidence-backed pattern: red fill (#d61b37), white text, 4px radius, deepening to #961024 on hover/active per the `.button--primary` rules — used for "Add to Cart," "Shop Now," and checkout actions.

**button-secondary** is a proposed outline treatment inferred from the neutral `.button` base class (gray border #8f8f8f, gray text #666, darkening border/text on hover) — likely used for filters, "Read More," or "Select an Option" controls.

**text-input** is proposed for search fields, coupon-code entry, and account forms; the border color and subtle box-shadow pattern is inferred from `.form-body`'s observed border/shadow treatment, extended to individual inputs.

**nav-bar** is proposed for the sticky header holding the hamburger menu, logo, cart icon, and category flyout (Dog Toys, Cat Toys, Collections) referenced in the page text; no header-specific selectors were supplied, so spacing and color are inferred from body/canvas defaults.

**product-card** is proposed for the recurring toy/treat tiles (e.g., "Halloween Stuff-A-Ball," "KONG Extreme Tires") seen throughout the excerpt; caption color (#757575) is directly observed via `.card-figcaption-body .card-text`.

**hero** is proposed for the homepage banner ("Classic now golden," "Trick or Treat Halloween") — a full-width soft-gray section with large Oswald display type and a primary CTA button; exact imagery and layout are not observed.

**footer** is proposed for the multi-column link list (Quick Links, Legal, social icons, payment badges) named in the page text; background and hairline are inferred defaults, not measured.

**badge** is a proposed small label for "New," "Limited-Edition," or "Halloween" tags on product cards, using the gold accent (#e6a700) tied loosely to the site's "Gold KONG" 50th-anniversary messaging — this color-to-role pairing is inferred, not measured on an actual badge element.

**search** and **promo-banner** are proposed supporting components: an overlay search panel (referenced as "Search Search View All Results") and a top free-shipping announcement bar ("Get free standard shipping... over $29!"), styled from the same primary/neutral palette with no direct CSS evidence for these specific elements.

## Responsive Behavior
Proposed, not measured from live rendering — inferred only from the presence of BigCommerce Stencil media-query breakpoints in the CSS bundle (≤551px, 551–1024px, 1024–1280px, 1280–1681px, ≥1681px):
| Range | Layout intent |
|---|---|
| ≤551px | Single-column stack; nav collapses to hamburger + slide-in cart drawer; product grid becomes 1–2 columns. |
| 551–1024px | 2–3 column product grid; condensed nav with icon-only search/account. |
| 1024–1280px | Full desktop nav; 3–4 column product grid. |
| ≥1280px | Max-width contained layout; 4+ column grid; expanded footer columns. |

Touch targets should be at least 44px for cart/nav icons; the mobile menu and cart drawer are assumed to use overlay/slide patterns typical of Stencil themes, but no interaction behavior was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered page, computed layout, or DOM screenshots were available. Font sizes, letter-spacing beyond the two observed heading/button rules, and all component paddings/breakpoints are proposed estimates, not measurements. Color-to-role mapping for non-button colors (gold, orange, blue, green tints) is inferred from general palette presence and BigCommerce form-state conventions, not confirmed selectors. Jost and Oswald are used as observed font-family declarations; their licensing, hosting, and actual availability were not verified. Additional font names present in the raw CSS bundle (Comic Relief, Montserrat, Mulish) had no associated selector evidence and were excluded. No hover/focus/active states, mobile menu behavior, or cart-drawer interactions were directly observed — all are proposed conventions for BigCommerce Stencil storefronts.
