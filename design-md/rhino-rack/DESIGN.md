---
version: alpha
name: "Rhino-Rack"
source_url: "https://rhinorack.com"
captured_at: "2026-09-28T04:58:42.238530+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in two coexisting token systems found in Rhino-Rack's stylesheet: a Bootstrap-derived utility palette (blues, grays, semantic reds/greens) and a custom brand palette exposed as CSS variables (--earth-v2, --blue-v2, --cream-v2, --black-v2, --sand-v2, --forest-v2, --rock-v2). The observed .btn-primary rules confirm #b65b00 (earth/orange) as the working call-to-action color, with #834200 as its hover state, and a secondary blue variant (#005cb9 hover #004386) for alternate actions. These are treated as primary and secondary respectively. Body copy uses a system sans-serif stack (Segoe UI/Roboto/Helvetica/Arial), while custom "trim-*" weights and "din-2014" appear as declared font-family values, suggesting a display/heading typeface distinct from body text; their exact usage in headings versus buttons is inferred rather than confirmed beyond the single observed .btn rule using trim-regular. Neutral surfaces (#ffffff, #f6f6f6, #f8f8f8) and hairlines (#dee2e6, #cccccc) support a rugged, utilitarian outdoor-gear aesthetic consistent with roof racks, awnings, and load-securing hardware. Component definitions below are proposed patterns for an e-commerce/fitment-driven storefront, not verified DOM observations.

colors:
  primary: "#b65b00"
  primary-hover: "#834200"
  secondary: "#005cb9"
  secondary-hover: "#004386"
  ink: "#10181f"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f6f6f6"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-sand: "#f4c44c"
  accent-forest: "#1f721f"
  accent-rock: "#4c1a0f"
  danger: "#dc3545"
  success: "#28a745"
  focus-ring: "#007bff"
typography:
  display-xl: {fontFamily: "din-2014, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "din-2014, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "trim-semibold, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "trim-regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.5px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
    hoverBackgroundColor: "{colors.primary-hover}"
    hoverBorderColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.secondary}"
    border: "1px solid {colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
    hoverBackgroundColor: "{colors.secondary}"
    hoverTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.focus-ring}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    height: "72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "{components.button-primary}"
    paddingY: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
  badge:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  fit-finder-widget:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    fieldTypography: "{typography.body-sm}"
    ctaComponent: "{components.button-primary}"

## Components

**button-primary** reflects the observed `.btn-primary` rule set directly: earth-orange (#b65b00) fill, white text, uppercase button typography, and a darker hover fill (#834200). This is the confirmed primary CTA treatment for actions like "Shop Now" and "Find a Dealer."

**button-secondary** is a proposed outline variant using the secondary blue (#005cb9), mirroring the `.btn-primary.btn-blue` hover/before rules observed in the CSS, intended for lower-emphasis actions alongside a primary CTA.

**text-input** is a proposed pattern for search fields, dealer-locator zip inputs, and account forms. Border and radius values are inferred from the neutral hairline palette; no live input styling was captured in the supplied evidence.

**nav-bar** represents the persistent header implied by the extensive top-level menu text (Shop By Activity, Vehicles & Fits, Support, About). Background and text colors are inferred from the light canvas and dark ink tokens; exact height and sticky behavior are not observed.

**product-card** is proposed for category/listing grids (Cargo Boxes, Bike Racks, Roof Top Tents, etc.), using the soft card surface and hairline border with the primary orange reserved for price emphasis, consistent with its use as the site's action color.

**hero** models the homepage banner pattern suggested by phrases like "THE FASTEST WAY TO SLOW DOWN" and "Raise The Bar," using the dark ink background and white text with a large display headline and primary CTA button.

**footer** is inferred from the long link list (Warranty, Returns Policy, Privacy Policy, Site Map) and uses the dark ink background for visual weight and contrast, a pattern common to multi-column utility footers, though the actual footer background color was not directly measured.

**badge** is a proposed small-format label (e.g., "New," "In Stock") using the forest-green brand accent, useful for merchandising flags on product cards; no badge markup was present in the supplied CSS.

**search** and **fit-finder-widget** are category-appropriate additions: the latter directly reflects the site's prominent "Fit My Vehicle" / "Cap/Topper Fit" navigation, proposing a bordered panel with fields and a primary CTA to look up vehicle-specific rack compatibility — a core purchase-path pattern for exterior vehicle accessories.

## Responsive Behavior

Breakpoint values below are taken directly from the `:root` custom properties (`--breakpoint-sm/md/lg/xl`) present in the CSS, though their applied media-query behavior on the live site was not observed.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| xs | 0 | Single-column stack, nav collapses to a hamburger menu |
| sm | 576px | Two-column product grids begin |
| md | 768px | Fit-finder widget moves inline with hero content |
| lg | 992px | Full horizontal nav-bar with mega-menu categories |
| xl | 1200px | Max content width; four-column product grids |

Touch targets for buttons and nav items should maintain a minimum 44px height, consistent with the `.btn` padding pattern (`12px 30px 10px`) observed in the CSS. Mobile nav collapse and mega-menu interaction states are recommendations, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed layout, or JavaScript-driven interaction was observed. The mapping of `trim-*` and `din-2014` font families to specific heading/button roles is inferred from a single `.btn` rule and general naming convention, not confirmed across headings. Border-radius values, card shadows, nav-bar height, and footer background color are proposed conventions, not measured from the live DOM. Hover/focus/active states beyond the explicitly supplied `.btn-primary` and `.btn-primary.btn-blue` rules are speculative. Mobile menu behavior, breakpoint-triggered layout shifts, and touch interactions were not observed. Licensing and self-hosting/foundry availability of the `trim-*` and `din-2014` typefaces were not verified and should be confirmed before implementation.
