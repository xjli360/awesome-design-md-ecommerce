---
version: alpha
name: "Rivian Gear Shop"
source_url: "https://rivian.com/gear-shop"
captured_at: "2026-09-28T10:02:39.240899+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is grounded in CSS custom properties and inline styles captured from gearshop.rivian.com, a Shopify-based storefront for Rivian's adventure gear, apparel, charging equipment, wheels/tires, and parts. The observed system is high-contrast and neutral-first: pure black (#000000) foreground and button color against a white (#ffffff) canvas, with light gray (#f2f2f2) used as a secondary background and mid-gray (#606060) as a secondary foreground/muted tone. A narrow set of accent blues appears in interactive/utility contexts — #0066ff and #007aff as link/theme colors, and #1990c6/#136f99 as a checkout-button default and its hover state — which this spec treats as an inferred "accent" role suited to charging/electrical iconography. Warm and cool near-white tones (#f2e7db, #d9ecf2) also appear in the raw palette and are mapped here as soft surface variants for imagery-heavy product tiles, though their exact usage context was not confirmed. Font stacks reference custom families named "Adventure" and "Adventure Mono" with sans-serif/system-ui fallbacks; no weights or exact sizes beyond a 1.2rem/19.2px body base were confirmed, so the full type scale is proposed. Corner radii are taken directly from root tokens (12px input, 20px product/block, 50px pill button) and generalized into a compact rounded scale.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#343435"
  muted: "#606060"
  hairline: "#dedede"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#0066ff"
  accent-info: "#1990c6"
  accent-info-hover: "#136f99"
  surface-warm: "#f2e7db"
  surface-cool: "#d9ecf2"
typography:
  display-xl: {fontFamily: "Adventure, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Adventure, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Adventure, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Adventure Mono, system-ui, sans-serif", fontSize: 19.2px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Adventure Mono, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Adventure Mono, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Adventure, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
rounded:
  none: 0px
  xs: 4px
  sm: 12px
  md: 20px
  lg: 24px
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderColor: "{colors.hairline}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fit-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.body-sm}"
    fieldTypography: "{typography.body-md}"
    actionButton: "button-primary"

## Components

**button-primary** reflects the root `--color-button: 0,0,0` / `--color-button-text: 255,255,255` pair and the site's `--border-radius-button: 50px` token, rendered here as a fully-rounded pill. Hover state (`--color-button-hover: 51,51,51`) is observed in the CSS variables and proposed for interactive feedback.

**button-secondary** uses the observed `--color-button-secondary` (#f2f2f2) and its hover (#e5e5e5, approximated to hairline/surface-soft in this palette) for lower-emphasis actions such as "View all" or filter toggles seen in the page text.

**text-input** is grounded in `--border-radius-input: 12px` and `--color-border-input`. States for focus/error are not observed in the supplied CSS and are proposed only.

**nav-bar** is sized from the confirmed `--header-height: 64px` token and uses the header-menu font-family variable family, distinct from body copy, matching the site's separation of `--font-header-menu-family` from `--font-body-family`.

**product-card** generalizes the repeated PDP tile pattern evident in the product-list text (title, price, "Regular price / Sale price" pairs) using the observed `--border-radius-product: 20px`. Image treatment and hover zoom are not observed and are proposed.

**hero** is an inferred full-bleed section pattern based on the "Gear up for fall / Explore gear built to keep you on the road" banner copy; exact background image, overlay, and copy alignment are not confirmed in CSS and are proposed.

**footer** is inferred from the presence of navigation groupings (Adventure Gear, Charging, Wheels and Tires, Parts, Apparel, Accessories, Culinary, Pets) but no footer-specific selectors were supplied; layout and column structure are proposed.

**badge** is proposed for merchandising labels (e.g., sale/new/fit-your-vehicle confirmation) using the accent-info blue drawn from the Shopify accelerated-checkout button color, repurposed here since no dedicated badge color was observed.

**vehicle-fit-selector** is a category-appropriate component derived directly from the "Fit your vehicle" / "Model and year" / "VIN" / model list (R1T, R1S, R2) and year list found in the page text — a compatibility-lookup pattern that is highly relevant to a charging-accessories and parts storefront where product fitment varies by vehicle and model year. Its visual treatment (card surface, hairline border, product-radius) is proposed by analogy to the product-card and input tokens, since no dedicated selector CSS was supplied.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid, nav collapses to a drawer menu (menu-drawer classes are referenced in the CSS but layout not observed). |
| Tablet | 600–1024px | 2-column product grid; vehicle-fit-selector likely becomes a modal/sheet. |
| Desktop | 1024–1440px | 3–4 column product grid; persistent top nav. |
| Wide | >1440px | Max-width content container with increased section padding (`{spacing.section}`). |

Touch targets are recommended at a minimum 44px height for buttons and inputs, consistent with the Shopify-supplied `--shopify-accelerated-checkout-button-block-size` default of 44px observed in the checkout CSS. Menu-drawer collapse behavior is inferred from class names only (`menu-drawer__utility-account-body`, etc.); actual collapse thresholds were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS/text extraction only; no rendered layout, interaction states (hover/focus/active), or JavaScript-driven behavior (e.g., drawer/menu open states, VIN lookup flow) was observed.
- `--font-body-family` and `--font-header-menu-family` are CSS variables whose resolved font names were not present in the supplied evidence beyond the generic `font_families` list; "Adventure" and "Adventure Mono" are assumed as the intended custom families based on that list, but exact weights, availability, and licensing are unverified.
- Several palette colors (e.g., #c181ff, #444635, #e7e0de, #12171d) appear in the raw evidence but were not confidently mapped to a role and are omitted from the token set; they may represent seasonal campaign or imagery-specific colors not part of the core UI system.
- Rounded-scale `full` (9999px) generalizes an observed 50px pill button radius rather than reproducing the literal value; treat as an approximation.
- Spacing scale values are proposed conventions; the only directly observed spacing tokens were `--spaced-section` (5rem/16rem depending on context) and grid gaps (`--row_gap: 4rem`, `--column_gap: 1.6rem`), which are larger than this document's `section` token and are not reconciled here.
- Hero, footer, and vehicle-fit-selector visual details (backgrounds, imagery, exact copy placement) are inferred from page text and generic patterns, not from confirmed layout CSS.
- Mobile/tablet rendering, breakpoint pixel values, and drawer/collapse thresholds are proposed recommendations only and were not present in the supplied evidence.
