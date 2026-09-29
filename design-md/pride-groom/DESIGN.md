---
version: alpha
name: "Pride+Groom"
source_url: "https://prideandgroom.com"
captured_at: "2026-09-28T04:47:17.734867+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pride+Groom's storefront (a Shopify-built site) presents a clean, editorial grooming-brand aesthetic anchored by a single deep maroon accent, #972525, which the source CSS assigns explicitly to --color-cta-bg and --color-highlight — this is treated as the confirmed primary brand color. Surrounding it is a neutral system: white canvas (#ffffff), near-black text (#1a1a1a) for headings, and a mid-gray (#333333) for body copy, consistent with a minimal, ingredient-forward apparel-adjacent pet-care brand rather than a saturated e-commerce look. Observed header-border and skeleton-loader tones (#d1d5db, #c9cac9, #f7f7f7, #f4f6f8) inform the hairline and soft-surface roles used for card separation and section banding — these role assignments are inferred, since the CSS only proves their presence in header/loading contexts, not general layout. A secondary blue pair (#1773b0 / #136f99) appears solely on Shopify's accelerated-checkout button and is carried forward here as an "accent" token for links/secondary CTAs, an inferred reuse rather than a documented brand color. Typography uses Figtree with Helvetica Neue/Arial/sans-serif fallbacks, per the theme's font-family variables; the body's small uppercase, wide-tracked CTA label (0.07em letter-spacing, weight 600) is the one directly observed type treatment and is used to define button-md.

colors:
  primary: "#972525"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#c9cac9"
  hairline: "#d1d5db"
  surface-soft: "#f7f7f7"
  surface-card: "#f4f6f8"
  on-primary: "#ffffff"
  accent: "#1773b0"
  accent-hover: "#136f99"
typography:
  display-xl: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06em"}
  body-sm: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: "0.04em"}
  caption: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.05em"}
  button-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 12.5px, fontWeight: 600, lineHeight: 1, letterSpacing: "0.07em"}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  coat-finder-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
button-primary: Used for the site's high-emphasis calls to action (e.g., "SHOP NOW"), directly modeled on the observed `.header__cta` rule — maroon fill, white text, 4px radius, uppercase 600-weight label. Hover state (swap to white background/maroon text/border) is explicitly present in CSS and treated as observed.

button-secondary: An outline variant for lower-emphasis actions (e.g., "Learn More"), inferred from the theme's `--color-button-border`/`--color-base-outline-button-labels` variables, which prove an outline-button pattern exists but not its exact resolved color; ink is used as a safe proposed value.

text-input: Applies to newsletter and search fields; border and radius are proposed extensions of the sm rounded token and hairline color, since no dedicated input CSS was supplied.

nav-bar: Represents the persistent header containing logo, navigation links, and CTA badge, grounded in the `#shopify-section...__header` variables (white background, dark foreground, light border). Sticky/scroll behavior is not confirmed and is proposed only.

product-card: Represents shampoo/conditioner and tool listings implied by "SHOP BY NEED" categories; card surface and radius are inferred design defaults, as no explicit `.product-card` selector was in evidence.

hero: Models the top promotional band ("Pearly Wipes" launch, Oprah-favorite callout) using the soft surface tone as a plausible section background; exact hero styling was not present in the supplied CSS.

footer: Reflects the multi-column footer (Shop/Help/Learn/newsletter) visible in page text; dark-on-light vs. light-on-dark treatment is proposed, since footer color declarations were not in the evidence.

badge: Represents small labels like "4X OPRAH FAVORITE" and "FREE SHIPPING" ribbons; pill shape and primary-color fill are proposed, matching brand accent usage seen on the CTA button.

search: Covers the "Search our site" overlay field referenced in page text; styling is proposed, using the light surface and hairline tokens for consistency with the header.

coat-finder-tile: A category-specific component for the "What's Your Dog Dealing With?" grid (Shedder / Non-Shedder / Sensitive One / Balm), a distinctive grooming-brand navigation pattern; card treatment is proposed but the content structure is grounded in the observed page copy.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤599px, tablet 600–999px, desktop ≥1000px. Nav-bar should collapse to a hamburger/logo/cart layout below tablet width, with the CTA badge either hidden or moved into a mobile menu. Product-card and coat-finder-tile grids are recommended to run 2 columns on mobile, 3–4 on tablet/desktop. All interactive targets (buttons, tiles, search field) should maintain a minimum 44×44px touch area regardless of the smaller visual padding observed on the desktop `.header__cta`. This section is a design recommendation only; no responsive CSS or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered layout, computed styles, or JavaScript-driven states were observed. Color roles beyond `--color-cta-bg`/`--color-highlight` (primary) are inferred by proximity and plausibility, not confirmed usage. Typography sizes (other than the button's letter-spacing/weight) are proposed design values, since root font-size context was ambiguous in the evidence. Hover/focus/active states beyond the documented `.header__cta:hover` and payment-button hover are not observed and are marked proposed. Mobile menu behavior, sticky header behavior, and actual grid/column counts were not present in the evidence and are recommendations only. Figtree's licensing/self-hosting status and full weight availability were not verified from the supplied data.
