---
version: alpha
name: "Yale"
source_url: "https://yalehome.com"
captured_at: "2026-09-28T09:56:14.058958+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from CSS evidence for the Yale Home smart-lock and
  door-hardware storefront, a Shopify-hosted site built on a global theme bundle.
  The observed palette centers on a near-black ink (#1a1a1a, #000000) against a
  white canvas, with a slate-blue neutral (#73859f) recurring across opacity
  variants, suggesting its use as a muted/secondary text and border tone. A single
  saturated magenta-pink (#ff1d5e) stands out as the only strongly chromatic,
  non-neutral color in the evidence and is inferred as the primary brand/CTA
  accent, consistent with sale and highlight usage common in this theme family.
  Supporting tones (#f64747, #ffcc66, #569ff7, #66a8cc) are inferred as
  status/utility colors (error, warning, info-link) rather than core brand colors,
  since none recur with the frequency or emphasis of the pink or the neutrals.
  Typography is anchored by a proprietary display family, YaleSolis (Bold/Light/
  Regular weights), paired with Open Sans for body copy and an Arial/Helvetica
  fallback stack — a hierarchy typical of a security-hardware retailer wanting a
  distinctive display voice with a legible, neutral workhorse text face. Rounded
  and spacing scales below are proposed conventions, not measured from layout.

colors:
  primary: "#ff1d5e"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#393939"
  muted: "#73859f"
  hairline: "#e6e6e6"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  slate-deep: "#2b333f"
  slate-muted-2: "#959ea9"
  border-subtle: "#c9c9c9"
  error: "#f64747"
  warning: "#ffcc66"
  info-link: "#569ff7"
  accent-blue-soft: "#66a8cc"
  overlay-scrim: "#000000cc"
typography:
  display-xl: {fontFamily: "YaleSolis-Bold, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "YaleSolis-Bold, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "YaleSolis-Regular, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "YaleSolis-Bold, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
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
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.slate-muted-2}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
    labelTypography: "{typography.caption}"

## Components
**button-primary** uses the inferred brand accent (#ff1d5e) as a solid fill, appropriate for primary calls to action like "Shop Now" and "Buy Now" seen repeatedly in the source text; hover/pressed states are proposed, not observed.

**button-secondary** is an outlined variant using ink-on-canvas for lower-emphasis actions (e.g., "Learn More"), keeping the same button typography for consistency; its border-only treatment is a proposed convention.

**text-input** models a generic form field (search, checkout, sign-up) with a hairline border and soft rounding; no focus-ring color was directly observed, so focus states are not specified here.

**nav-bar** represents the top-level site header implied by the region/locale switchers ("US ▾ CA-EN ▾ CA-FR ▾") and category links ("Shop by Space," "Accessories," "Door Hardware"); its compact vertical padding is proposed for a dense utility navigation.

**product-card** is inferred from repeated product-listing text patterns (title, configuration string, price range, e.g., "Yale Assure Lock 2 Touch… Buy Now $299.99 – $299.99"), using a card surface with modest rounding for a merchandising grid.

**hero** reflects the large promotional banners referenced in the text ("Your End of Summer Plans Just Got Smarter," "A Brighter Way to Welcome Home"), using the dark slate tone as a scrim-friendly background for overlaid white display type; exact hero imagery and layout were not observed.

**footer** is proposed as a dark-toned closing band consistent with the slate-deep color's reuse in the video-player chrome, offering muted secondary links against a dark field; actual footer content/structure is not confirmed by the evidence.

**badge** covers "Sale" and "New Arrival" labels referenced in the text, using the error-red tone for urgency; pill shape is a proposed convention rather than a measured radius.

**search** is a rounded utility input, proposed for the site's product search entry point; no dedicated search-field CSS was present in the evidence.

**finish-swatch-selector** is a category-specific component reflecting the repeated finish options ("Black Suede," "Oil Rubbed Bronze," "Satin Nickel," "Lifetime Brass") shown per product; modeled as small circular swatches with a primary-colored selected-state ring, a common pattern for hardware/finish selection though not directly observed in markup.

## Responsive Behavior
This is a recommendation, not measured site behavior, since no media-query breakpoints were present in the supplied CSS evidence.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column product grid; nav collapses to a menu icon; hero text stacks above imagery. |
| Tablet | 600–1023px | Two-column product grid; nav may show primary categories with overflow menu. |
| Desktop | 1024px+ | Multi-column grid (3–4 cards); full horizontal nav with locale switcher visible. |

Touch targets should be at least 44×44px (per the Swiper navigation-size default of 44px present in vendor CSS), particularly for finish swatches, carousel arrows, and locale/nav dropdown toggles. Navigation and filter panels are recommended to collapse into an off-canvas or accordion pattern below the tablet breakpoint; no such collapse behavior was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is generated from static CSS/text extraction only; no live rendering, computed layout, or DOM interaction was performed. Color-to-role mapping (e.g., primary vs. accent vs. status colors) is inferred from frequency and contrast plausibility, not from confirmed component usage — in particular, #ff1d5e's role as "primary" brand color is an inference, as is treatment of #007aff as a third-party Swiper default rather than a Yale brand color. Font sizes, weights, letter-spacing, and the full typographic scale are proposed conventions built around the observed family names (YaleSolis-Bold/Light/Regular, Open Sans, Arial/Helvetica); no explicit font-size or weight declarations were present in the supplied CSS rules. All spacing and rounded-corner tokens are proposed defaults, not extracted values. Responsive breakpoints, mobile navigation collapse, hover/focus/active interaction states, and swatch-selection behavior are not observed and are presented only as reasonable, labeled proposals. Availability, licensing, and web-font-loading configuration for the proprietary YaleSolis family were not verified.
