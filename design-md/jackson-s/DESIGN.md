---
version: alpha
name: "Jackson's"
source_url: "https://jacksonschips.com"
captured_at: "2026-09-29T03:55:22.714548+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Jackson's is a CPG snack brand (avocado-oil kettle chips, sweet potato chips,
  veggie straws) selling direct-to-consumer via Shopify. The supplied CSS
  confirms a warm, appetite-driven palette: white (#ffffff) as the primary
  canvas, a saturated red (#b1202b) explicitly wired to heading color and
  input borders in the theme's color-scheme variables, a lime-green accent
  (#cde53e) used as a full background scheme (likely for promo bands or
  badges), and a soft neutral gray (#f2f2f2) used as a secondary background
  scheme. A deep brown (#592e2c) appears in the palette and is inferred as a
  secondary brand/footer tone given the rustic, kitchen-made brand story.
  Additional palette entries (greens, orange, blue, dark red) are inferred as
  supporting semantic colors for nutrition badges, allergen callouts, and
  informational links, since CPG snack sites commonly use small accent chips
  for "Non-GMO," "Vegan," "Gluten-Free" claims echoed in the page copy.
  Typography mixes structured sans-serifs (Montserrat, Poppins) for
  headings/UI with a handwritten script (Caveat) for playful accents, and a
  body font (Liter) for running copy; a fifth family ("Sink") is unverified
  and treated cautiously. Layout, spacing scale, and component states below
  are proposed conventions for a snack e-commerce site, not measured DOM
  observations.

colors:
  primary: "#b1202b"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#00000066"
  hairline: "#e6e6e6"
  surface-soft: "#f2f2f2"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-lime: "#cde53e"
  accent-brown: "#592e2c"
  accent-orange: "#ee9441"
  success: "#3ed660"
  success-deep: "#006400"
  error: "#8b0000"
  link: "#1990c6"
  link-deep: "#136f99"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Liter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Liter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Caveat, cursive", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-brown}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-lime}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    accentColor: "{colors.accent-lime}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the confirmed red (#b1202b) as a solid fill with white text, matching the CSS-confirmed heading/border role of that color; padding is proposed, loosely informed by the observed `--button-padding-inline: 2.5rem` token. **button-secondary** is an outlined variant reusing the same red for border and label, proposed for lower-emphasis actions like "Learn More." **text-input** and **search** both reuse the red border token, directly grounded in the observed `--color-scheme-1-input-border: rgb(177 32 43)` declaration; hover/focus states are proposed, not observed. **nav-bar** is proposed as a white bar with hairline underline, consistent with a mega-menu structure implied by the `MegaMenuList` selectors in the CSS, though exact layout is unmeasured. **product-card** proposes a near-white card surface with a soft hairline border to separate snack SKUs (Kettle Chips, Sweet Potato Chips, Super Veggie Straws) in a grid; imagery treatment is unobserved. **hero** proposes the light-gray scheme-4 background (#f2f2f2) as a section band, consistent with its confirmed use as a background variable, paired with a bold display headline. **footer** is proposed using the brown palette entry as a grounding dark band with lime-green links for contrast, since the footer content list (About, Support, Ways to Save) is extensive per the page text. **badge** models the "Top 9 Allergen Free / Vegan / Kosher / Gluten-Free" claim chips visible in the copy, using the confirmed lime-green scheme-3 background as a pill. **subscription-card** is a category-appropriate proposed component for the "Subscribe & Save 10%" feature described in the text, using red framing and lime accent to visually match the brand's promotional tone; none of these interior states (hover, active, disabled) were observed in the static CSS.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <480px | Single-column stacks, nav collapses to hamburger |
| tablet | 480–1024px | 2-column product grid; mega-menu at 4 columns (matches observed `--menu-columns-tablet: 4`) |
| desktop | >1024px | Mega-menu at 6 columns (matches observed `--menu-columns-desktop: 6`); multi-column product/badge grids |

Touch targets should meet at least a 36–44px minimum, loosely consistent with the observed `--button-size-md: 36px` token. Mega-menu collapse behavior on mobile is proposed and was not observed in interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variable dumps and page text only; no rendered layout, hover/focus states, animation, or actual responsive breakpoints were observed. Semantic color roles (muted, surface-card, accent-orange, success, error, link) are inferred from generic CPG/e-commerce conventions and the presence of relevant-sounding hex values in the palette, not from confirmed selector usage. Typography sizes are proposed except where a specific pixel/weight value appeared in the CSS (e.g., font-weight 600 on text-block decorations). The font family "Sink" could not be verified as a real, licensed typeface and is excluded from component definitions; "inherit!important" was excluded as a non-font value. Spacing and radius scales are conventional proposals loosely cross-checked against the one observed button padding token (`2.5rem`) and one observed radius token (`--menu-image-border-radius: 0px`), but are not a full measured system. Mobile navigation, cart drawer, and subscription-flow interactions described in the page text were not available as CSS/DOM evidence.
