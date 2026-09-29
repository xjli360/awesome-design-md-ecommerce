---
version: alpha
name: "Tea Forte"
source_url: "https://teaforte.com"
captured_at: "2026-09-28T09:10:27.137867+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation draws from Tea Forté's observed CSS custom properties and color palette, which centers on desaturated slate-blue neutrals (#46555e, #455560, #7f8c95) paired with a warm brass/gold accent (#ae8e4b, #b09040) that reads as premium and botanical, consistent with a gourmet tea retailer. True black (#000000, #0c1418, #18191e) and white (#ffffff) anchor contrast, while soft off-whites (#fafafa, #f5f5f5, #f4f3ee) suggest card and section backgrounds. A red family (#e42127, #b8070c) appears in discount-related selectors and is mapped here to sale/badge accents; a green (#25b900) is mapped to success/in-stock states — both roles are inferred from selector naming, not confirmed visual observation. Typography is built on the observed 'Gotham SSm A'/'Gotham SSm B' stack (with Work Sans, Roboto, Helvetica Neue, Arial, and system fallbacks present in the CSS), which this spec treats as the primary brand typeface family for headings and body copy. Spacing tokens mirror the site's own --hh-space-* scale (5–120px). Rounding, exact type sizes beyond the one observed 16px/24px body rule, and most component states are proposed conventions for a premium e-commerce tea brand, not measured layout facts, and are labeled accordingly throughout.

colors:
  primary: "#ae8e4b"
  ink: "#0c1418"
  canvas: "#ffffff"
  body: "#46555e"
  muted: "#7f8c95"
  hairline: "#e0e0e0"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-brass-deep: "#826b2f"
  accent-blue-teal: "#467c99"
  accent-sale: "#e42127"
  accent-sale-deep: "#b8070c"
  accent-success: "#25b900"
  surface-alt: "#f4f3ee"
  border-strong: "#999999"
  overlay-transparent: "#00000000"
typography:
  display-xl: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', -apple-system, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', -apple-system, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceColor: "{colors.ink}"
    saleColor: "{colors.accent-sale}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  tea-collection-tile:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    descriptionTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"

## Components
**button-primary** uses the brass/gold (#ae8e4b) as the primary call-to-action color against white text, reflecting the luxury-gourmet positioning implied by the palette; hover/active states are proposed, not observed. **button-secondary** inverts this to an outlined white button with brass text and border, intended for lower-emphasis actions like "View collection." **text-input** proposes a soft off-white background (#fafafa) with a light hairline border for login/search fields, matching the site's visible sign-in form context. **nav-bar** assumes a white top bar with slate-gray body text, sized for the observed multi-level category menu (Pyramid, Loose, Iced Tea, Subscription, etc.); collapse behavior is proposed only. **product-card** pairs a white card surface with a hairline border and reserves the red accent (#e42127) for sale/discount pricing, inferred from the `--discount-text-color`-style selector naming rather than a confirmed rendered swatch. **hero** proposes a warm off-white section background (#f4f3ee) to host large promotional messaging such as the "Warming Joy Collection" banner referenced in the page text. **footer** is proposed as a near-black (#0c1418) band with white text, a common pattern for premium food/beverage sites, though not confirmed from supplied CSS. **badge** is a small pill using the sale-red accent, intended for "NEW," "Free Gift," or discount flags seen in the banner copy. **search** proposes a pill-shaped light input consistent with the "hit enter or Search" prompt in the page text. **tea-collection-tile** is a category-appropriate component for the many tea-type and box-style listings (Black Tea, Herbal Tea, Presentation Box, etc.), using a white card with brass accent detailing to differentiate collection entries from standard product cards.

## Responsive Behavior
| Breakpoint | Width | Layout guidance (proposed) |
|---|---|---|
| Mobile | <600px | Single-column stacking, collapsed hamburger nav, full-width buttons, touch targets ≥44px |
| Tablet | 600–1024px | 2-column product grids, condensed nav with visible search icon |
| Desktop | 1024–1440px | Multi-column category grids (3–4 across), full horizontal nav |
| Wide | >1440px | Max-width content container (~1280–1440px), generous section padding using {spacing.section} |

This table is a recommendation based on common e-commerce conventions and the spacing scale present in the CSS custom properties; it is not derived from measured site behavior at any breakpoint. Touch targets should maintain a minimum 44×44px hit area on mobile, and any multi-level navigation (visible in the observed category list) should collapse into an accordion or drawer pattern below tablet width.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is generated from static CSS extraction and a text excerpt only; no live rendering, computed layout, or interaction states were observed. Color-to-role mapping (e.g., treating #ae8e4b as primary brand accent, #e42127/#b8070c as sale/discount colors, #25b900 as success) is inferred from selector names and general e-commerce convention, not from visual confirmation. Typography sizes beyond the single observed 16px/24px body rule are proposed, not measured. The Gotham SSm A/B font family's licensing and actual availability/loading on the live site were not verified. No mobile menu, cart drawer, hover, focus, or form-validation states were observed; all such behaviors above are proposed conventions. Rounding and spacing values for individual components are estimated using the site's own spacing scale but were not confirmed against rendered elements.
