---
version: alpha
name: "Wyndham Collection"
source_url: "https://wyndhamcollection.com"
captured_at: "2026-09-28T09:56:50.754482+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wyndham Collection is a bathroom-fixtures storefront (vanities, bathtubs, storage, countertops, mirrors) built on a Shopify theme with CSS custom properties for color, spacing, and interaction states. The observed palette centers on a near-black foreground/button token (rgb(18,18,18)) against a white background, paired with a family of deep navy-slate tones (#102b44, #455c77, #365977, #222d3a, #303940) used in the header wordmark, image-with-text buttons, and footer. Two very light warm-neutral tints (#f7f2f7, #f8f1f6) appear alongside a cool neutral gray (#f3f3f3), suggesting soft section and card backgrounds. A single saturated blue (#334fb4) and a muted mauve-gray (#9e9499) are also present but their exact UI role is not confirmed from the evidence and is treated as inferred.
  Typography evidence shows body copy set at 1.5rem with 0.06rem letter-spacing via a CSS variable font stack; the site references Assistant, Cabin, Poppins, and Roboto as available families, but which family maps to headings versus body is not proven by the supplied rules and is labeled inferred. A confirmed 2px button corner radius and 44px minimum touch target come directly from an observed slideshow button rule and inform the interaction primitives below. The interpretation favors a restrained, trade-pro-oriented UI: dark neutral actions, navy brand accents, and soft neutral surfaces for product cards.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#9e9499"
  hairline: "#cccccc"
  surface-soft: "#f3f3f3"
  surface-card: "#f7f2f7"
  on-primary: "#ffffff"
  accent-navy: "#102b44"
  footer-bg: "#455c77"
  footer-btn-bg: "#222d3a"
  button-alt-bg: "#303940"
  accent-blue: "#334fb4"
  overlay-strong: "#00000080"
  overlay-soft: "#0000000d"
  border-strong: "#211f21"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Cabin, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.96px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-navy}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    skuTypography: "{typography.caption}"
    skuColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.canvas}"
    overlay: "{colors.overlay-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-primary}"
    buttonBackground: "{colors.footer-btn-bg}"
    buttonText: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
    typography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    triggerBackground: "{colors.primary}"
    iconColor: "{colors.on-primary}"
    panelBackground: "{colors.canvas}"
    panelTextColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    size: "{spacing.xl}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.accent-navy}"
    gap: "{spacing.sm}"

## Components

**button-primary** reflects the observed `--color-button`/`--color-button-text` pair (near-black on white) and the confirmed 2px radius from the slideshow button rule; it is the default add-to-cart and primary CTA style.

**button-secondary** inverts the primary treatment using the observed `--color-secondary-button` tokens (white fill, dark text/border), intended for lower-emphasis actions like "Continue shopping." Hover/active states are proposed, not observed.

**text-input** is a proposed pattern for search and account fields; no explicit input CSS was supplied, so border, radius, and padding are inferred from the general neutral/hairline palette.

**nav-bar** uses the observed header span color (#102b44) for the wordmark/label text against a white background, with a hairline border as a proposed separator. Actual header height, sticky behavior, and mobile menu are not observed.

**product-card** groups vanity/bathtub/storage listings seen in the page text (title, SKU, price). Background uses one of the soft warm-neutral tints from the palette as an inferred card surface; the corner radius maps to a theme variable (`--product-card-corner-radius`) whose resolved value was not supplied, so `sm` is a placeholder.

**hero** models the homepage slideshow referenced in the evidence ("FEATURED BY HGTV," Rebecca bathtub). Overlay and CTA styling reuse the observed slide-button pattern; exact hero imagery treatment is not observed.

**footer** is directly grounded in observed `--footer-bg`, `--footer-text`, and `--footer-btn-bg` variables, giving a navy-slate footer with white text and a darker slate button.

**badge** is a proposed component for stock/trade or "Best Value" style labels, built from the observed `--color-badge-*` variables (white background, near-black foreground and border at low opacity).

**search** reflects the observed white icon color inside `.search__button .icon` on a presumed dark trigger; panel styling and results layout are proposed.

**finish-swatch** is a category-specific proposed component addressing the many trim/finish variants in the product data (e.g., Brushed Gold, Matte Black, Brushed Nickel), using circular swatches with a navy selected-state border.

## Responsive Behavior

Recommended breakpoints (not measured from live site): mobile < 768px, tablet 768–1023px, desktop ≥ 1024px. Navigation is expected to collapse to a hamburger/drawer pattern below tablet width. Touch targets should meet the 44px minimum height confirmed in the `.wc-slide__button` rule. Product-card grids are recommended at 2 columns on mobile, 3 on tablet, 4–5 on desktop. This section is a design recommendation only; actual responsive markup and behavior were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, hover/focus states, or JavaScript-driven interactions were observed. Font-to-selector mapping (Assistant/Cabin/Poppins/Roboto) is inferred from a generic list of declared families, not from confirmed heading/body CSS bindings. Several color roles (muted, surface-card, accent-blue) are inferred from palette proximity rather than confirmed component usage. Sizing for display-xl, display-md, title-md, body-sm, and caption is proposed per standard UI scale, not measured. The `product-card` corner radius references an unresolved Shopify theme variable. Mobile menu, cart drawer, and checkout flow visuals were not observed. Custom font licensing/self-hosting status for Assistant, Cabin, Poppins, and Roboto was not verified from the supplied evidence.
