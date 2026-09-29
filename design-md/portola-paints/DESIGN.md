---
version: alpha
name: "Portola Paints"
source_url: "https://portolapaints.com"
captured_at: "2026-09-28T09:19:10.694653+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Portola Paints & Finishes sells specialty decorative coatings (Roman Clay, Lime Wash, Traditional Finish) through a Shopify storefront whose extracted CSS exposes a neutral, utilitarian UI palette layered over a small set of warmer accent tones. The root theme variables define an off-white canvas (#ffffff), a dark neutral foreground near-black used for text and badges, and a mid-gray button surface (#e1e1e1 region), none of which read as an intentional "brand" palette so much as a stock Shopify theme scaffold. The one clearly branded color signal is a teal-blue pair (#1990c6 / #136f99) used for the accelerated-checkout button and its hover state; this is treated here as the inferred primary action color, since paint retailers commonly reserve a saturated accent for calls to action against neutral chrome. Warmer swatch-like tones (#f1d6a8 sand, #d2e4c4 sage, #cfe3e6 pale teal) and an isolated pink (#e91e63/#eb7a8e) appear in the raw palette and are mapped as decorative accent/highlight colors suited to color-chip and gallery contexts, though their actual site usage was not confirmed. Typography combines a serif (Cardo) with a proprietary grotesque (Söhne) atop a system-font fallback stack; Cardo is proposed for display headings to suit an artisanal-finish brand, Söhne/system-ui for UI and body copy, both flagged below as unverified for licensing/availability. Layout, spacing, and radii are proposed conventions, not measured.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#e0e0e0"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sand: "#f1d6a8"
  accent-sage: "#d2e4c4"
  accent-teal-tint: "#cfe3e6"
  accent-highlight: "#e91e63"
typography:
  display-xl: {fontFamily: "Cardo, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Cardo, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Söhne, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Söhne, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Söhne, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Söhne, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.05em}
  button-md: {fontFamily: "Söhne, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.1em}
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
    backgroundColor: "transparent"
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
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.accent-teal-tint}"
    textColor: "{colors.ink}"
    overlayColor: "#00000080"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    swatchColors: ["{colors.accent-sand}", "{colors.accent-sage}", "{colors.accent-teal-tint}", "{colors.accent-highlight}"]
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xs}"

## Components

**button-primary** uses the inferred teal action color (#1990c6, darkening to #136f99 on hover, per the accelerated-checkout CSS) against white text, uppercase micro-caption type at wide tracking — proposed as the primary "Add to Cart" / "Shop Now" treatment.

**button-secondary** is a ghost/outline variant in ink-on-transparent, matching the observed `.buttonGroup .button--secondary:hover` pattern where border and text both resolve to white/ink depending on context; here mapped to ink for light backgrounds. Proposed default (non-hover) state.

**text-input** is a minimal bordered field using the light hairline gray and body copy color; no observed input CSS was present, so padding and radius are proposed conventions typical of Shopify themes.

**nav-bar** assumes a white sticky header (root variables confirm `--use-sticky-header: 1` and a non-transparent header), with ink text and a hairline bottom rule. Actual nav markup/interaction was not observed.

**product-card** proposes a bordered, white-surface card for paint/finish SKUs, pairing a title in the serif title style with sans body pricing — consistent with an artisanal product catalog but not confirmed from captured CSS.

**hero** proposes a banner using the pale teal tint (#cfe3e6) as a calm background suited to a paint brand, with a dark overlay option (`#00000080`, present in the raw palette) for text legibility over imagery; large serif display type per the Cardo mapping.

**footer** is a soft-gray, muted-text block reflecting the `#f5f5f5`/`#757575` pairing found in the general Shopify theme grays; store hours/contact text observed in the page excerpt would plausibly live here.

**badge** is a pill using the same ink color the theme assigns to `--color-badge-foreground`/`--color-badge-border`, on a white background — this directly mirrors the observed root CSS variables rather than being purely inferred.

**search** proposes a soft-gray search field, unobserved directly but consistent with the surface-soft token and general theme conventions.

**color-swatch-selector** is a category-appropriate proposed component for browsing paint colors ("Shop by Color" was observed in nav text), using the sand/sage/teal/highlight accents pulled from the raw palette as representative swatch chips; no actual swatch markup or color values from real Portola products were captured.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column stacking, nav collapses to a drawer/hamburger, hero padding reduces to `{spacing.xl}` |
| tablet | 600–959px | 2-column product grids, nav remains collapsed or condenses to icon row |
| desktop | 960–1279px | Full horizontal nav, 3–4 column product grids |
| wide | ≥1280px | Max-width content container, generous `{spacing.section}` vertical rhythm |

Touch targets should be at least 44×44px for buttons and swatch chips; the observed `#submitBtn` height of 50px meets this. Nav collapse thresholds and drawer behavior are proposed and were not verified via live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text extraction, not a rendered or interactive audit of the live site. The mapping of `#1990c6`/`#136f99` to a "primary brand" role is inferred from a single Shopify payment-button rule, not from confirmed brand guidelines. Root theme RGB variables (e.g., `--color-foreground: 43,46,52`) did not exactly match a provided hex, so the nearest observed hex values (`#212121`, `#333333`) were substituted for ink/body roles. Accent colors (sand, sage, teal-tint, highlight pink) were present in the raw palette but their actual on-page usage/context is unconfirmed. Cardo and Söhne were present in the font-family evidence but their actual application to headings vs. body, and their licensing/self-hosting status (Söhne is a commercial typeface), were not verified. All spacing, radius, breakpoint, and component-state (hover/focus/disabled) values beyond the few directly cited CSS rules are proposed conventions, not observed measurements. No mobile layout, animation, or real interaction states were captured.
