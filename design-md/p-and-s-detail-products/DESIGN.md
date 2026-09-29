---
version: alpha
name: "P&S Detail Products"
source_url: "https://psdetailproducts.com"
captured_at: "2026-09-28T10:18:55.227422+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  P&S Detail Products is a Shopify-powered storefront for professional and DIY
  automotive detailing chemicals. The supplied evidence yields a neutral
  Shopify-theme palette: white (#ffffff) and near-black ink (#202223) for
  layout, mid-grey text and border tones (#6d7175, #dedede, #6c6c6c) for
  secondary content, and a small set of accent reds (#eb0a27, #c4293d) that
  are treated here as the inferred primary brand accent, since no explicit
  brand-color declaration was present in the CSS. A slate tone (#454564) is
  proposed as a secondary accent for contrast against the reds. Status colors
  (#108043/#f2faf0 green, #dd9a1a/#fcf1cd amber) appear to originate from
  Shopify's default inventory/notice styling and are mapped to success and
  warning roles. A link-blue (#337ab7) is retained for inline text links. Note:
  a themeColor value (#574cd5) surfaced in the page's embedded chat-widget
  JSON is a third-party script configuration, not part of the site's own CSS
  palette, and has been excluded from this specification. Typography uses the
  observed Arial/Helvetica/Montserrat/sans-serif stack, split by inference
  into a utilitarian body face and a heavier Montserrat-led display face for
  headings, matching the theme's separate --base-font-family and
  --heading-font-family variables. Component patterns follow the visible
  .btn/.btn--secondary/.btn--tertiary button system and a commerce-catalog
  layout implied by the product-grid and quick-buy text in the evidence.

colors:
  primary: "#eb0a27"
  accent-secondary: "#454564"
  ink: "#202223"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6d7175"
  hairline: "#dedede"
  surface-soft: "#f6f6f6"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  link: "#337ab7"
  success: "#108043"
  success-bg: "#f2faf0"
  warning: "#dd9a1a"
  warning-bg: "#fcf1cd"
  border-strong: "#9f9f9f"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1em, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  quick-buy-modal:
    backgroundColor: "{colors.canvas}"
    overlayColor: "#00000040"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#ffffffb3"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge-freeshipping:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  variant-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** is proposed for primary calls to action such as "Shop All," "Add to Cart," and "Subscribe." It uses the inferred red accent on a solid fill with white text; hover/active states were not observed and are proposed as a slight darkening consistent with the `.btn:hover`/`.btn:active` rule seen in the CSS.

**button-secondary** covers outline-style actions (e.g., "View All," filter toggles) using a transparent/white fill with hairline border and ink text, mirroring the `.btn--secondary` variable structure in the evidence, though its resolved colors were not directly captured.

**text-input** represents newsletter and search fields; a thin hairline border and generous internal padding are proposed defaults, as no explicit input styling was present in the extracted CSS.

**nav-bar** models the top utility/announcement bar and main navigation implied by the "Free Shipping on Orders $200+," search, account, and cart text in the evidence. A white background with a light hairline separator is proposed; actual sticky/scroll behavior is unobserved.

**product-card** is the core catalog unit for items like "Brake Buster Total Wheel Cleaner" and "Xpress Interior Cleaner," pairing a title, price ("From $X.XX"), and quick-buy affordance on a soft card surface with a subtle border.

**quick-buy-modal** is proposed for the "Quick buy" interaction referenced repeatedly in the page text (variant title, size dropdown, quantity, Add to cart), rendered as a centered overlay dialog; its open/close animation was not observed.

**hero** reflects the homepage slide content ("Bugs Be Gone," "The Perfect Duo," "No More Headaches") shown against a dark ink-colored section with large display type and a single CTA button.

**footer** consolidates the Company/Distributors/Support link columns and payment-method icons noted in the text, set on the same dark ink background as the hero for visual bookending; the many payment-brand hex values in the raw palette (e.g., Visa/Mastercard blues and reds) are treated strictly as third-party logo colors, not site theme colors, and are excluded from this spec's role assignments.

**badge-freeshipping** and **badge-sale** are small pill/rect labels for merchandising callouts such as the free-shipping threshold banner and sale pricing, using the Shopify-style success-green and primary-red pairs respectively.

**search-bar** and **variant-selector** support the header search control and the product page's size options (Pint/Quart/Gallon/5 Gallon), both proposed with rounded, low-emphasis styling consistent with a utilitarian commerce theme.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–479px | Single-column product grid, collapsed hamburger nav, `--container-pad-x: 16px` per evidence. |
| tablet | 480–989px | Two-column product grid, condensed nav, `--container-pad-x: 30px`. |
| desktop | 990–1279px | Full horizontal nav, three/four-column grid, `--container-pad-x: 50px`. |
| large | 1280px+ | Wider gutters, `--container-pad-x: 60px`, larger hero imagery. |

Touch targets for buttons and variant selectors should be at least 44×44px. The main navigation is expected to collapse into a slide-out or accordion menu below the tablet breakpoint; this collapse behavior and any sticky-header transition were not directly observed in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were observed. Role assignments for `primary`, `accent-secondary`, `success`, and `warning` are inferred from Shopify-theme conventions and color proximity in the supplied palette, not from explicit CSS variable resolution (custom property values such as `--btn-bg-color` were referenced but not resolved to hex in the evidence). The heading/body font split (Montserrat vs. Arial/Helvetica) is inferred from the presence of separate `--heading-font-family` and `--base-font-family` variables plus the observed font list, not a confirmed pairing. All typography sizes beyond generic body defaults are proposed, not measured. Numerous hex values in the raw palette correspond to third-party payment-network logos (Visa, Mastercard, Amex, Apple Pay, Google Pay, Discover) and a chat-widget script configuration; these were identified and excluded from brand role mapping. Mobile navigation collapse, hover/focus states, and modal transitions are proposed patterns, not verified interactions. Custom font licensing and self-hosting status for Montserrat were not verified from the evidence.
