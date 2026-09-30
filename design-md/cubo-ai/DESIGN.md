---
version: alpha
name: "Cubo Ai"
source_url: "https://getcubo.com"
captured_at: "2026-09-28T09:58:38.065660+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  CuboAi's storefront (getcubo.com / us.getcubo.com) presents a Shopify-based baby-monitor product site organized around AI safety and sleep features. The CSS custom properties expose a clear brand palette: a teal primary (#24ceb9) with tonal steps (#5be3d3, #b7f1ea, #dcebe9, #e9f4f3), a coral secondary (#ff8784) used for cart badges, a sky blue accent (#4cc3e5) tied to "Health" features, and an amber warning color (#ffb516) tied to "Memories" and a floating action button. Feature-toggle buttons (Safety/Sleep/Health/Memories) map directly to these four hues, an observed and unusually explicit color-to-content mapping worth preserving. Typography relies on 'museo-sans-rounded' for headings with Corbel Bold/sans-serif fallback, and a plain sans-serif/Corbel stack for body copy — no evidence of licensed webfont hosting was found, so fallback behavior should be assumed. Neutral text tones (#6d6d6d nav/body, #9a9a9a muted, #121212 ink) and light surface tones (#e9f4f3, #f4f5f6) are inferred as a soft, clinical-but-friendly UI supporting the "peace of mind" positioning. Rounded pill shapes (50px/50% radii) recur in real buttons and controls, informing an interpretation favoring soft, rounded, approachable components over sharp corners.

colors:
  primary: "#24ceb9"
  primary-pale: "#bbefe9"
  primary-soft: "#b7f1ea"
  secondary: "#ff8784"
  secondary-soft: "#f4e8e8"
  blue: "#4cc3e5"
  blue-soft: "#ebf5fa"
  warning: "#ffb516"
  cta: "#1990c6"
  cta-hover: "#136f99"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#6d6d6d"
  muted: "#9a9a9a"
  hairline: "#dedede"
  surface-soft: "#e9f4f3"
  surface-card: "#f4f5f6"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'museo-sans-rounded', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'museo-sans-rounded', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'museo-sans-rounded', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "sans-serif, 'Corbel'", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "sans-serif, 'Corbel'", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "sans-serif, 'Corbel'", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "'museo-sans-rounded', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    height: "64px"
    hairline: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  feature-tab:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-md}"
    activeVariants:
      safety: "{colors.secondary}"
      sleep: "{colors.primary}"
      health: "{colors.blue}"
      memories: "{colors.warning}"
  floating-action-button:
    backgroundColor: "{colors.warning}"
    rounded: "{rounded.full}"
    size: "48px"
    position: "fixed bottom-right"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the observed core teal (`--primary-color`) as a solid fill with white text, formatted as a pill (`rounded.full`) consistent with the rounded, high-contrast checkout and CTA buttons implied by the Shopify accelerated-checkout CSS. Hover/active darkening is proposed, not observed.

**button-secondary** is an outlined variant proposed for lower-emphasis actions (e.g., "Learn more" links seen repeatedly in the page text), using primary-colored text and border on a transparent background to avoid introducing unobserved fill colors.

**text-input** is a proposed pattern for forms such as the mailing-list signup ("Sign up to receive a $10 off coupon"); no explicit input CSS was supplied, so border, radius, and padding are inferred from the site's generally soft, low-radius aesthetic.

**nav-bar** reflects real evidence: a sticky, white (`#ffffff`) header with a fixed 64px row height and `#6d6d6d` link/text color, matching `.header-sticky .nav` rules directly from the CSS.

**product-card** is proposed for shop-grid items (Smart Baby Monitor, Sleep Safety Bundle, Add-ons) using the light neutral `surface-card` tone and moderate radius; no explicit card CSS was in evidence, so shadow and border are unspecified/proposed.

**hero** is proposed for the homepage's stated monitor headline and imagery, using the soft mint tint (`surface-soft`, equal to `--tertiary-color`) as a background wash consistent with the light, clinical brand feel, paired with a primary CTA button.

**feature-tab** is directly grounded in evidence: `.badge__button--safety/--health/--sleep/--memories.active` rules explicitly set background colors to secondary, blue, primary, and warning respectively. This is the strongest, most literal color-to-semantic mapping in the source CSS and should anchor any feature-navigation UI.

**floating-action-button** mirrors the observed `.global-popup .popup-button`: a fixed, bottom-right, amber (`#ffb516`) circular button at 48px, likely a chat or support launcher, rendered with `rounded.full`.

**footer** and **search** are proposed compositions filling structural gaps not present in the supplied CSS excerpt; footer uses the darkest observed neutral (`#121212`) for contrast, and search reuses the text-input pattern.

## Responsive Behavior
This is a recommended, non-measured breakpoint scheme; no responsive CSS or mobile layout was present in the supplied evidence.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| Mobile    | <480px      | Single-column stacks, nav collapses to hamburger, feature-tabs become horizontally scrollable |
| Tablet    | 480–1024px  | Two-column product/feature grids, sticky nav retained |
| Desktop   | >1024px     | Multi-column hero/grid layouts, full nav links visible |

Touch targets should be at least 44px for buttons and the floating action button (already 48px per evidence). Nav collapse and swiper-control behavior on small screens are proposed, not confirmed from static CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, isolated selector/declaration snippets, and page text — not a rendered or interactively tested site. Component structures (product-card, hero, footer, text-input, search) beyond nav-bar, feature-tab, and floating-action-button are proposed compositions, not directly observed markup/CSS. Font availability for 'museo-sans-rounded' and Corbel variants (licensing, hosting, actual render fallback) was not verified; generic sans-serif fallback should be assumed in implementation. Type sizes, weights, and letter-spacing in the typography scale are proposed conventions, not measured computed styles, aside from the font-family stacks themselves. No hover, focus, error, or disabled states were observed beyond the swiper-button and Shopify checkout-button hover rules; all other interaction states are proposed. Mobile/responsive layout, breakpoints, and touch behavior were not present in evidence and are recommendations only.
