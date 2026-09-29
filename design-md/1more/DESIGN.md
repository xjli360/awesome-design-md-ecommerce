---
version: alpha
name: "1MORE"
source_url: "https://usa.1more.com"
captured_at: "2026-09-28T10:17:27.077165+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  1MORE's storefront CSS exposes a neutral, technical palette built around a near-black
  foreground (#121212), a soft blue-gray canvas (#f0f3f6), and white product-card
  surfaces. A family of red-orange accents (#f93822, #f83a1f, #fd3b1e, #ff3c1f, #eb0e0e)
  recurs across promotional badges and call-to-action blocks tied to specific custom
  section components, so a single representative red is treated here as the brand
  accent while the others are noted as tonal variants used per-campaign. A distinct
  green (#319335) appears only on a cart upsell button and is mapped as a proposed
  success/add-to-cart state rather than a core brand color. Body copy uses "gotham-book"
  with an observed -1px letter-spacing, while heading weights ("gotham-bold",
  "gotham-medium", "gotham-light") are present as font-family declarations without
  directly observed heading sizes; type scale sizes below are therefore proposed,
  not measured. Border-radius values of 10px (announcement countdown) and 16px (chat
  widget) are the only observed rounding; the broader rounded scale is inferred to
  keep components consistent. Numerous payment-network colors (Visa, Mastercard,
  PayPal, Amex) were excluded from the semantic palette as third-party badge colors,
  not brand tokens. The resulting interpretation favors a clean, dark-on-light
  audio-tech aesthetic with red used sparingly for urgency (sale badges, primary CTAs).

colors:
  primary: "#f93822"
  ink: "#121212"
  canvas: "#f0f3f6"
  body: "#333333"
  muted: "#7e7e7e"
  hairline: "#eeeeee"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#f3f3f3"
  success: "#319335"
  border-strong: "#c0c0c0"
  accent-alt: "#f83a1f"
typography:
  display-xl: {fontFamily: "gotham-bold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "gotham-bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  title-md: {fontFamily: "gotham-medium, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  body-md: {fontFamily: "gotham-book, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: -1px}
  body-sm: {fontFamily: "gotham-book, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: -0.5px}
  caption: {fontFamily: "gotham-light, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "gotham-medium, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border-strong}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    mutedText: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px rgba(18,18,18,0.08)"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaBackground: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  feature-callout:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the core commerce action (Add to Cart, Buy Now), mapped from the observed `--color-button: 18,18,18` and multiple `.button1` red backgrounds seen in promo sections; here it is generalized to the accent red for consistency, a proposed unification rather than a single observed rule.

**button-secondary** uses the canvas tone as a low-emphasis alternative for actions like "View all" or "Continue shopping," inferred from the `--color-secondary-button` variables since no distinct secondary button CSS block was captured.

**text-input** is proposed for account/login and newsletter forms; no input-specific CSS was supplied, so border, radius, and padding are inferred defaults consistent with the card and hairline tokens.

**nav-bar** represents the persistent header (logo, category menu, cart, country selector) implied by the text excerpt's navigation structure; exact height, sticky behavior, and mobile menu treatment were not observed in the CSS.

**product-card** models the repeated product-grid tiles (e.g., S30, SonoFlow HQ31) referenced heavily in the page text; background, radius, and shadow are proposed since no card-specific selector was present in the evidence.

**hero** is a proposed full-bleed banner pattern for homepage storytelling ("tuned by a 4-time Grammy Award-winning sound engineer"), using the dark ink background with light text for contrast; no hero selector was directly supplied.

**footer** is inferred from the long link list (About Us, FAQ, Shipping, Warranty, social icons) in the text excerpt; dark background with light text follows the site's general dark/light contrast pattern but was not confirmed via footer-specific CSS.

**badge** covers the frequent "NEW," "Save %," and sale labels seen throughout the category listings; pill shape and red fill are proposed, generalizing from the sparse but consistent use of red accents across promotional elements.

**search** is a proposed lightweight search field using the soft surface tone; no dedicated search-bar CSS was captured in the supplied rules.

**feature-callout** is a category-appropriate component for audio spec highlights (driver type, Grammy-tuning claim, noise cancellation) using the canvas background and title typography to separate marketing copy from product-grid content; entirely proposed, not tied to a specific selector.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column product grid, collapsed hamburger nav, sticky cart icon |
| Tablet | 600–959px | Two-column product grid, nav links may wrap or collapse |
| Desktop | 960–1439px | Multi-column grid (3–4 cards), full horizontal nav |
| Wide | 1440px+ | Max-width content container, additional whitespace |

Touch targets are recommended at a minimum 44×44px for cart, nav, and badge-adjacent controls. Mobile navigation is assumed to collapse into a slide-out or hamburger menu given the multi-level category structure (All Products, Open-Ear, Over-Ear, True Wireless, Wired) implied by the text excerpt. This table is a recommendation based on typical Shopify-theme conventions; no viewport-specific CSS or media queries were included in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS custom properties, a limited set of selector/declaration pairs, and page text — no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed. The red accent family (#f93822, #f83a1f, #fd3b1e, #ff3c1f, #eb0e0e, #f12929, #dd3a3f) appears across different custom-section instances; treating one value as "primary" is an interpretive simplification, not a confirmed single brand red. The green (#319335) is attributed to a cart-recommendation button only and its broader use as a "success" color is inferred, not confirmed. Heading font sizes, weights-to-family mapping (which weight corresponds to which visual heading level), and letter-spacing beyond the observed body -1px are proposed. Border-radius values beyond the two observed instances (10px, 16px) are inferred to complete a usable scale. Mobile menu behavior, cart drawer interaction, and product-card hover states were not present in the supplied evidence. Availability, licensing, and web-font loading configuration for the "gotham-*" family were not verified and must be confirmed against 1MORE's actual font license before implementation. Payment-network badge colors (Visa, Mastercard, PayPal, Amex) were deliberately excluded from the semantic palette as non-brand third-party colors.
