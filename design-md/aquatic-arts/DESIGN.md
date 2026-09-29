---
version: alpha
name: "Aquatic Arts"
source_url: "https://aquaticarts.com"
captured_at: "2026-09-28T04:18:21.701453+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Aquatic Arts presents as a Shopify-themed livestock storefront built on a light,
  high-key palette. The CSS custom-property block exposes a clear brand system:
  a soft yellow-green primary action color ("#def4a9") paired with pure black
  text ("#000000"), a near-black "alt" surface ("#111111") with white text, and
  a light blue announcement band ("#66bed7") used for banner-style messaging.
  Body surfaces step through white ("#ffffff"), "#fafafa", and "#f2f2f2" dim
  tiers, suggesting a layered light-mode card system rather than deep shadows.
  A teal "cart dot" accent ("#0f7662") and a Shopify-wallet blue
  ("#1990c6" / hover "#136f99") round out functional colors for cart and
  checkout affordances. A red ("#d02e2e") appears available for
  errors/sale flags; role is inferred, not confirmed live.
  Typography is split into a serif display face, Arvo, at a documented 37px/700
  weight for headers, and a sans body face, Assistant, set unusually heavy at
  weight 800 with wide 0.05em tracking — likely a deliberate bold, friendly
  brand voice suited to a specialty pet/aquarium retailer. Button radius is
  documented at 3px, approximated here to the nearest scale step. Payment-brand
  swatches (Visa/Mastercard/PayPal reds-blues) were excluded from the brand
  palette as they are third-party assets, not site identity.

colors:
  primary: "#def4a9"
  on-primary: "#000000"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#fafafa"
  surface-card: "#f2f2f2"
  accent-info: "#66bed7"
  accent-dim: "#d5f192"
  link: "#1990c6"
  link-hover: "#136f99"
  success: "#0f7662"
  danger: "#d02e2e"
  border: "#cccccc"
typography:
  display-xl: {fontFamily: "Arvo, serif", fontSize: "37px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.025em"}
  display-md: {fontFamily: "Arvo, serif", fontSize: "28px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.025em"}
  title-md: {fontFamily: "Arvo, serif", fontSize: "22px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0.02em"}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: "16px", fontWeight: 800, lineHeight: 1.5, letterSpacing: "0.05em"}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.5, letterSpacing: "0.03em"}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: "12px", fontWeight: 700, lineHeight: 1.4, letterSpacing: "0.05em"}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: "14px", fontWeight: 800, lineHeight: 1, letterSpacing: "0.05em"}
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
    border: "1px solid {colors.border}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-dim}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  guarantee-banner:
    backgroundColor: "{colors.accent-info}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the documented "#def4a9" action color with black text and the observed 3px-adjacent radius; this is the storefront's dominant add-to-cart / CTA surface. **button-secondary** is a proposed outline treatment for lower-priority actions (e.g., "view details"), using canvas background and a hairline border for restraint against the busy livestock imagery. **text-input** follows Shopify-theme conventions with a subtle hairline border and generous internal padding for touch accuracy; focus/error states were not observed and are proposed. **nav-bar** is inferred as a white header bar with hairline separation, sized for a horizontal category/search layout typical of specialty-pet Shopify themes. **product-card** groups livestock imagery, a serif title, and a bold price line on a soft off-white surface, echoing the theme's tiered dim-background system. **hero** is proposed on the dark "alt" surface with white hero text, matching the exposed "--colorHeroText" variable, for full-bleed banner sections. **footer** mirrors the dark ink surface for brand consistency and legal/informational density. **badge** leverages the "drawers-dim" green as a small pill, suitable for "In Stock," "New," or category tags common on livestock listings; exact usage not confirmed. **search** is a compact overlay/input pattern on the dim surface tier. **guarantee-banner** is a category-specific, livestock-retail pattern using the observed announcement blue to carry shipping/live-arrival guarantee messaging — a common but unverified pattern for aquatic/fish e-commerce.

## Responsive Behavior

Recommended, not measured: mobile <480px single-column stacking with 44px minimum touch targets; tablet 481–1024px two-column product grids; desktop >1024px multi-column grids with persistent nav. Nav should collapse to a hamburger/drawer below ~1024px, consistent with the "--colorDrawers" tokens present in the CSS. Buttons and inputs should maintain at least 40–44px hit height regardless of breakpoint.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties and cascade rules only; no live page was rendered, screenshotted, or interacted with. Semantic role assignments (e.g., which hex serves "danger," "success," or "badge") are inferred from naming/usage context, not confirmed via rendered UI. Payment-brand colors (Visa/Mastercard/PayPal-style hexes) were deliberately excluded as third-party, non-brand assets. Font sizes beyond the two documented variables (37px header, 16px base) are proposed defaults. Actual mobile menu behavior, hover/focus states, and breakpoint values were not observed and are provided as conventional recommendations only. Licensing and hosting of Arvo and Assistant were not verified.
