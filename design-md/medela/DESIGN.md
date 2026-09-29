---
version: alpha
name: "Medela"
source_url: "https://medela.us"
captured_at: "2026-09-28T09:39:30.041101+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Medela's US feeding site evidence shows a neutral-first UI built on Tailwind-style utility tokens (gray scale from #f3f4f6 through #111827, hairline #e5e7eb) layered with a small set of brand accent hues: a saturated yellow (#ffcd00/#ffc709), a deep teal (#007a8c/#016372), and a warm orange (#ff8200/#e47501). Status colors (green #22c55e, red #ef4444, amber #eab308, blue #2563eb) appear to be system/form states rather than brand identity. Three custom families are present in the CSS: OggText (a serif referenced in the h1 headline variable chain, rendering at an observed 35px/35px/400 mobile scale), Centra No2 (a mid-weight sans used generically for heading levels, which share a font-weight:500 rule), and KumbhSans (a geometric sans appearing as a heading fallback and inferred here as the workhorse UI/body face). No desktop type sizes, real letter-spacing values, or breakpoints were present in the supplied CSS, so all non-h1 sizes and every breakpoint are proposed, not measured.

  This interpretation treats yellow as the primary call-to-action color against dark ink text (contrast-safe pairing consistent with a light-canvas, gray-typography storefront), teal and orange as secondary/category accents, and the gray ramp as structural chrome. Rounded corners and spacing are proposed conventions for a clinical-but-approachable feeding/medical-device retailer, not values extracted from layout.

colors:
  primary: "#ffcd00"
  ink: "#3f3f48"
  canvas: "#ffffff"
  body: "#52525e"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  on-primary: "#3f3f48"
  accent-teal: "#007a8c"
  accent-teal-dark: "#016372"
  accent-orange: "#ff8200"
  accent-orange-dark: "#e47501"
  border-strong: "#9ca3af"
  link: "#2563eb"
  success: "#22c55e"
  error: "#ef4444"
  error-dark: "#b91c1c"
  warning: "#eab308"
  warning-dark: "#a16207"
  overlay: "#0000001a"
  black: "#000000"
typography:
  display-xl: {fontFamily: "OggText, serif", fontSize: 35px, fontWeight: 400, lineHeight: 1.0, letterSpacing: 0px}
  display-md: {fontFamily: "OggText, serif", fontSize: 28px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Centra No2, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "KumbhSans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "KumbhSans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "KumbhSans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "KumbhSans, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  part-finder-panel:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-orange}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the observed yellow (#ffcd00) as a high-visibility CTA fill, paired with dark ink text for contrast; hover/disabled state tokens exist in the CSS custom-property chain but their resolved values were not supplied, so hover/disabled treatments are proposed.

**button-secondary** is an outline pattern inferred from the `.a-button-link--secondary` variable structure (border + bg + text tokens exist), rendered here as a white-fill, gray-bordered button since no resolved secondary palette values were present in evidence.

**text-input** follows a conventional light-canvas, hairline-border field; padding and rounding are proposed defaults since no form-field CSS was supplied.

**nav-bar** is inferred from the site's mega-menu content (Products/Solutions/Articles/Services/Shop categories) rather than observed layout CSS; a white bar with gray body-sm labels is proposed as a conservative baseline.

**product-card** reflects the catalog structure implied by repeated "View all" / product-name / short-description text patterns (e.g., Symphony, Pump In Style Pro+); card chrome, border, and radius are proposed.

**hero** models the homepage's large introductory pump-product callouts (e.g., "Pump In Style Pro+... Power meets portability"), using the display-xl serif headline on a soft neutral background; exact hero sizing/imagery was not observed.

**footer** is proposed as a muted, low-emphasis region consistent with the gray/muted token set; no footer-specific CSS was supplied.

**badge** uses the teal accent to flag categorical or status labels (e.g., "No 1 Hospital Pump"); pill shape and color are inferred, not confirmed against a real badge selector.

**search** is proposed as a pill-shaped input consistent with the rounded/full token, since no search-bar CSS was present in evidence.

**part-finder-panel** is a category-specific proposed component addressing the site's "Extra Pump Parts" content (Connectors, Membranes, Tubing, Shields, Power units), using the orange accent to differentiate accessory/compatibility flows from primary pump purchases.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| xs | <480px | Single-column stack; nav collapses to a mobile menu trigger |
| sm | 480–767px | Two-column product grids begin |
| md | 768–1023px | Nav-bar expands to inline top-level links |
| lg | 1024–1279px | Three/four-column product grids, full mega-menu |
| xl | ≥1280px | Max-width content container, generous section spacing |

Touch targets are recommended at a minimum 44×44px for buttons and nav items; the mobile menu label present in evidence ("openMenuMobileLabel") confirms a collapsible mobile navigation exists, but its visual behavior, animation, and exact breakpoint thresholds were not observed and are recommendations only, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed styles, or JavaScript-driven states were observed. Desktop typography sizes, letter-spacing, hover/disabled color values (referenced only as unresolved CSS custom properties like `--a-button-link-primary-bg-hover`), and all breakpoint pixel values are proposed, not measured. The semantic mapping of yellow to "primary," teal/orange to "secondary accents," and gray tokens to ink/muted/hairline roles is inferred from likely usage patterns, not confirmed against rendered components. Font family availability, licensing, and correct weight/style loading for OggText, Centra No2, and KumbhSans were not verified — these are asserted only as names present in the supplied evidence. Mobile menu, search, cart-drawer, and product-card interaction/layout behavior were not observed and are proposed conventions for this product category.
