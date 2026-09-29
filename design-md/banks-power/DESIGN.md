---
version: alpha
name: "Banks Power"
source_url: "https://bankspower.com"
captured_at: "2026-09-29T04:22:02.169174+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Banks Power's site evidence shows a utilitarian, high-contrast industrial palette built around a near-black body ink (#2c2d2e) on white and light-grey (#f5f5f5) canvases, with a saturated red (#c50008, reinforced by #c60007/#a10007/#c62a32 variants) reserved for brand accents, CTAs, and alerts. Headings use 'Roboto' at 700 weight per the observed CSS rule targeting h1-h6 and heading-font classes; body copy uses 'acumin-variable' with system sans-serif fallbacks, at a base size near 17px (1.0625rem) and 1.6 line-height. Muted text (#8a8a8a) and hairline greys (#dadce0, #e6e6e6, #cacaca) support secondary labels, dividers, and disabled states — these tonal roles are inferred from selector context (.subheader, small) rather than directly labeled as such by the source. A dark surface (#272727) appears in a scrolling-text badge, suggesting a secondary dark-UI accent for callouts or overlays.

  The proposed interpretation leans into this automotive-performance aesthetic: bold condensed-feeling headings in red or near-black, dense utilitarian navigation reflecting the large vehicle-fitment product catalog, and a vehicle-selector widget as a first-class component given the "Shop Parts for your Vehicle" flow repeated in the evidence. Rounded corners stay minimal (sm/md) to match an engineering-tool tone rather than a soft consumer-retail one.

colors:
  primary: "#c50008"
  primary-strong: "#a10007"
  ink: "#2c2d2e"
  canvas: "#ffffff"
  body: "#2c2d2e"
  muted: "#8a8a8a"
  hairline: "#dadce0"
  border: "#e6e6e6"
  disabled: "#cacaca"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#272727"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
typography:
  display-xl: {fontFamily: "'Roboto', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Roboto', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Roboto', sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: "normal"}
  body-md: {fontFamily: "'acumin-variable', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "normal"}
  body-sm: {fontFamily: "'acumin-variable', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  caption: {fontFamily: "'acumin-variable', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'acumin-variable', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.15, letterSpacing: "0.3px"}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed brand red (#c50008) as a solid fill with white text, intended for primary calls to action such as "FIND PARTS" or "ADD TO CART." The weight and letter-spacing are proposed to match a compact, utilitarian button style consistent with the site's dense navigation.

**button-secondary** is a bordered, transparent-background variant for lower-emphasis actions (e.g., "CHANGE VEHICLE"), using the ink color for text and a light hairline border. This pairing is proposed, not confirmed by a captured button screenshot.

**text-input** models form fields (vehicle year/make/model selectors, search) with a white background, light border, and body typography. Padding and border-radius are proposed defaults appropriate to a functional, non-decorative form aesthetic.

**nav-bar** reflects the large mega-menu structure evident in the page text (Products, About Banks, Support, multi-level category lists). A light canvas background with a hairline bottom border is proposed; the source CSS confirms a `.header` component with a transparent-over-hero state but not its resting-state colors, so this mapping is inferred.

**product-card** is proposed for the "Shop By Category" grid (Cold Air Intakes, Exhaust Systems, etc.), using a white surface, subtle border, and title/body type pairing drawn from the confirmed heading/body font rules.

**hero** uses the dark surface (#272727) as a background for large banner sections (e.g., "OVER 68 YEARS OF INNOVATION"), with white text and the display-xl heading style. This dark-hero treatment is inferred from the one confirmed dark-surface use case (`.scrolling-text`) generalized to a larger hero block.

**footer** reuses the dark surface for a full-width footer housing the extensive sitemap-style link list observed in the page text (Power Bundles, Turbo Systems, Contact Us, etc.), with white link text at body-sm size.

**badge** models the small pill-shaped label confirmed in CSS (`.scrolling-text`, border-radius 48px, dark background, white text), used here generically for status or promotional badges like "PAYMENT PLANS AVAILABLE AT CHECKOUT."

**search** is a proposed lightweight input styled with the soft surface grey, matching the header's search icon/action referenced in the page text.

**vehicle-selector** is a category-appropriate component built for Banks' recurring "Shop Parts for your Vehicle" year/make/model/engine widget, using the soft surface background with red accent highlights for the primary "FIND PARTS" action — a pattern central to a performance-parts fitment-driven storefront.

## Responsive Behavior

Proposed breakpoints (not measured from live site behavior):

| Breakpoint | Width      | Notes                                  |
|-----------|------------|-----------------------------------------|
| small     | 0–48em     | Single-column, collapsed nav to drawer  |
| medium    | 48–66.75em | Two-column product grids                |
| large     | 66.75–75em | Full mega-menu, three/four-column grids |
| xlarge    | 75em+      | Max-width container, wide hero          |

These bucket labels (`small`, `medium`, `large`, `xlarge`) are drawn from a font-metrics string found in the evidence (`small=0em&medium=48em&large=66.75em&xlarge=75em`), which appears to be a breakpoint-definition artifact rather than confirmed rendered CSS; treat widths as directionally correct only. Touch targets for buttons and nav items should be at least 44px tall. The multi-level Products mega-menu should collapse into an accordion-style mobile menu below the `medium` threshold. This section is a recommendation for implementation, not a measurement of the live site's actual responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered screenshots, computed layout, or interaction states (hover, focus, active, error) were observed. Color-to-role mapping (e.g., which reds serve default vs. hover vs. destructive states) is inferred from selector naming and frequency, not confirmed visually. Font availability and licensing for 'acumin-variable' were not verified — it is an Adobe/commercial font and may require a subscription or self-hosted license; fallbacks are specified accordingly. Typography sizes beyond the confirmed base body size (1.0625rem/17px) are proposed, not measured. Mobile menu behavior, cart/drawer interactions, and vehicle-selector dropdown mechanics were not observed and are inferred from page text only. No CSS custom-property values for header/hero backgrounds in their default (non-transparent) state were present in the supplied evidence, so hero/footer dark-surface use is an extrapolation from a single confirmed dark-badge rule.
