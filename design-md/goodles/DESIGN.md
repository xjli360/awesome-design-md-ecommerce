---
version: alpha
name: "Goodles"
source_url: "https://goodles.com"
captured_at: "2026-09-28T09:46:29.732021+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Goodles presents as a playful, color-saturated CPG brand built around a mac-and-cheese product line. The observed palette is unusually large and vivid, spanning reds, pinks, cyans, purples, greens and multiple yellows, consistent with per-flavor theming (theme-ui-colors variables show distinct primary/secondary/tertiary sets per product). For this interpretation, {colors.primary} is drawn from the observed ctaColor token (#FF2815), paired with the observed ctaTextColor (#FFDD00) as on-primary for high-contrast CTAs. Ink and muted text roles use dark, saturated tones already present in the palette (#273376 navy, #4F3B97 purple) rather than an unobserved black, since no neutral gray or true black hex was supplied. Canvas and card surfaces use the observed white (#FFFFFF); a soft pink (#FFC8D0), also used as an override accent/bowl-outline color in the CSS, becomes surface-soft for gentle section backgrounds. Hairline uses a light observed blue (#A4DEFB) for subtle separators, an inferred role since no dedicated border color was captured. Typography draws on the observed Sofia Pro family for display and UI text, Helvetica LT Std as a body fallback, and Overpass Mono for small mono-styled accents (e.g., prices, tags), all layered onto system-ui/sans-serif fallbacks. All sizes, weights and component patterns below are proposed conventions for a playful, high-energy snack/pasta storefront, not measured layout values.

colors:
  primary: "#FF2815"
  ink: "#273376"
  canvas: "#FFFFFF"
  body: "#273376"
  muted: "#4F3B97"
  hairline: "#A4DEFB"
  surface-soft: "#FFC8D0"
  surface-card: "#FFFFFF"
  on-primary: "#FFDD00"
  secondary: "#00754A"
  tertiary: "#FF5400"
  accent: "#73E5E1"
  highlight: "#F652AC"
typography:
  display-xl: {fontFamily: "'Sofia Pro', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Sofia Pro', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Sofia Pro', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica LT Std', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica LT Std', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Overpass Mono', monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Sofia Pro', sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  flavor-swatch:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.md}"
    typography: "{typography.button-md}"

## Components
button-primary is the main add-to-cart/shop CTA, using the observed ctaColor/ctaTextColor pairing for strong contrast against the light canvas. button-secondary is a proposed outline variant for lower-emphasis actions like "Learn" or "Where To Buy" links. text-input is an inferred pattern for account/search/email-capture fields, using the light hairline blue for a soft border. nav-bar is a proposed sticky/top navigation bar in white with ink text, hairline-separated from content, sized for the observed multi-item menu (Shop, Build-a-Box, Where To Buy, Learn, Account). product-card is the flavor/SKU tile pattern implied by the many named products (Cheddy Mac, Shella Good, Twirly Mac variants), with rounded corners and a compact caption-styled price row. hero is a full-bleed intro section using the soft pink surface tint for the "A New Spin on Mac" campaign banner, pairing a large display headline with supporting body copy. footer uses the observed secondary green as a grounding color block with light text, a proposed contrast pairing not directly measured. badge is a small pill for flags like "GF" (gluten-free) or "New," using the cyan accent tone seen in the default theme variables. search is a rounded input pattern for the account/FAQ search experience implied by the FAQs/Contact links. flavor-swatch is a category-specific component proposed for selecting among the many colorful flavor variants (Cheddar Weather, Alfredo Heights, Hotshot Jackpot), using the vivid highlight pink to echo the brand's flavor-differentiated theming.

## Responsive Behavior
Recommended, not measured: mobile <480px single-column stacked hero and product grid; tablet 480–959px two-column product grid with condensed nav; desktop ≥960px multi-column grid with full horizontal nav. Touch targets should be at least 44px tall for buttons and nav items; the nav is proposed to collapse into a hamburger/drawer pattern below 960px given the number of listed menu items (Cheesy Macs, Protein Pasta, Build-a-Box, Trial Pack, Where To Buy, Learn, Account). Slick-carousel classes observed in the CSS suggest a horizontally-swiped testimonial/product slider on smaller viewports, but exact breakpoints were not present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This is a static CSS/text extraction; no live rendering, computed layout, JavaScript-driven interaction, or actual mobile viewport was observed. Color-to-role mapping (ink, muted, hairline, surface-soft) is inferred from the closest suitable hues in the supplied palette since no neutral gray or black was present in evidence; an unobserved #000000 was explicitly avoided per prior correction. Typography sizes, weights, and line-heights are proposed conventions, not measured from rendered pages; only the font-family names (Sofia Pro, Helvetica LT Std, Overpass Mono, Pitch, system-ui) are observed. Per-flavor theme-ui color sets (e.g., F652AC/ffdd04 for one product theme, 73E5E1/FF2815 for the default) indicate the live site likely swaps palettes per SKU, which this single interpretation does not fully capture. Custom font licensing, self-hosting, and availability (Sofia Pro, Pitch) were not verified. Component states such as hover, focus, disabled, and error styling are proposed patterns only, not confirmed via observed CSS pseudo-classes beyond the limited slick-dots and modal examples supplied.
