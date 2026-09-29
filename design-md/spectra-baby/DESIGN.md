---
version: alpha
name: "Spectra Baby"
source_url: "https://spectrababyusa.com"
captured_at: "2026-09-28T10:16:32.738353+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Spectra Baby USA's storefront reads as a clinical-meets-nurturing feeding
  brand built around breast pump technology. The observed CSS exposes a vivid
  magenta accent (#e00065, closely paired with #e60067) used for primary CTA
  buttons and highlight icons, set against a near-black ink (#1a1a1a) and
  neutral grays (#696969, #333333) for header and body copy. A soft pink tint
  (#fef8f9) and light hairline grays (#e5e5e5, #dddddd) suggest a clean,
  clinical-light canvas typical of medical-adjacent consumer products.
  Success/warning/error tokens (green #1a7b3c on #f0fdf4, red #d72c0d) point
  to an inferred semantic feedback system for cart, stock, and form states.
  Typography relies on Libre Franklin and Open Sans as the two observed
  sans-serif families, with a documented small-type scale
  (--text-xs through --text-lg) driving UI copy; larger display sizes are
  inferred to support hero and product headings, since no explicit heading
  font-size tokens were captured. A tertiary blue (#1990c6) appears only on
  Shopify's accelerated-checkout button and is treated as a payment-provider
  color, not a brand token. The overall interpretation favors a light,
  high-contrast, trust-forward retail layout: generous section spacing,
  wide product-grid gutters, and one dominant pink CTA color reused across
  buttons, badges, and interactive accents.

colors:
  primary: "#e00065"
  primary-alt: "#e60067"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#696969"
  hairline: "#e5e5e5"
  surface-soft: "#fef8f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  success: "#1a7b3c"
  success-bg: "#f0fdf4"
  error: "#d72c0d"
  badge-soft-pink: "#ffe7ec"
typography:
  display-xl: {fontFamily: "Libre Franklin, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Libre Franklin, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Libre Franklin, sans-serif", fontSize: 21px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Fustat, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    logoWidth: "140px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    badge: "{components.badge}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    onSaleBackground: "{colors.error}"
    onSaleText: "{colors.on-primary}"
    soldOutBackground: "{colors.ink}"
    soldOutText: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  pump-bundle-card:
    backgroundColor: "{colors.badge-soft-pink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    savingsTextColor: "{colors.primary}"
    ctaButton: "{components.button-primary}"

## Components

**button-primary** is the dominant CTA pattern, using the observed magenta (#e00065/#e60067) at full opacity with white text, matching the "Shop S1 Plus" and announcement-bar CTAs seen in evidence. **button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g. "Continue shopping") using the same pink as border/text on a white fill; its existence is inferred, not directly observed in the CSS excerpt. **text-input** is proposed for search, account, and checkout fields, using the observed --input-padding-block (0.75rem) and generic hairline borders since no explicit input styling was captured. **nav-bar** reflects the header grid tokens (logo/primary-nav/secondary-nav areas, 140px logo width, transparent vs non-transparent text-color variables), rendered here in its non-transparent state with muted gray (#696969) link text. **product-card** is a proposed pattern for the featured-products carousel (S1 Plus, S2 Plus, Synergy Gold, etc.), combining a white surface, hairline border, and the badge component for sale/sold-out states drawn from the --on-sale-badge and --sold-out-badge custom properties. **hero** models the "GENTLE, YET POWERFUL" banner using the soft pink surface and display-xl heading, with spacing derived from the observed --section-vertical-spacing (3.5rem/4.5rem) tokens. **footer** is proposed as a dark, ink-colored close of page given the brand's strong pink/dark contrast pattern elsewhere, though its actual footer styling was not present in evidence. **badge** directly reflects the observed CSS custom properties for on-sale (red) and sold-out (near-black) states. **search** is proposed as a pill-shaped overlay input consistent with the site's "Search for..." placeholder text and modal search pattern noted in the page copy. **pump-bundle-card** is a category-specific proposed component for the bundle listings (e.g. "S1 Plus, Bag & Cooler Kit Bundle"), using the soft pink badge tint to visually group multi-item feeding kits distinctly from single-pump product cards.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column nav collapses to hamburger; --container-gutter reduces toward 2rem; product grid single column. |
| Tablet | 480–960px | Two-column product-list grid; --product-list-column-gap (3rem) and --product-list-row-gap (4rem) apply at reduced scale. |
| Desktop | 960–1440px | Header grid resolves to logo/primary-nav/secondary-nav three-column layout; container-gutter expands to 3rem. |
| Wide | > 1440px | Max-width content container centers; section-vertical-spacing reaches 4.5rem. |

Touch targets should meet a minimum 44px tap height (consistent with the observed accelerated-checkout button's clamp(25px, 44px, 55px) sizing). Primary nav and mega-menu collapse behavior at mobile widths is proposed, not observed, given the multi-level category structure evident in the page text (Shop All, Breast Pumps, Accessories, etc.).

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This DESIGN.md is derived from static CSS custom properties and a single page-text excerpt; no rendered layout, hover/focus states, animation, or actual responsive breakpoints were observed. Color-role assignments (ink, body, muted, surface-soft) are inferred from likely usage patterns (header text-color variables, badge backgrounds) rather than confirmed against rendered elements. Display-size typography (48px/32px headings) is proposed, since only small-scale text tokens (--text-xs through --text-lg, 14–21px) were present in evidence. Font weights and letter-spacing for headings and buttons are estimated conventions, not extracted values. Custom font availability and licensing for Libre Franklin, Open Sans, and Fustat were not verified beyond their appearance in the font-family evidence list. Rounded-corner values follow a generic proposed scale, as the only observed radius token (Shopify's accelerated-checkout button) defaulted to 0px. Component states such as disabled, error, and loading were not captured and are treated as proposed extensions of the observed success/warning/error CSS variables.
