---
version: alpha
name: "XGIMI"
source_url: "https://www.xgimi.com"
captured_at: "2026-09-29T04:17:27.363265+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from XGIMI's official Chinese storefront (极米科技官方网站), a mainland-hosted mall presenting the brand's projector and laser-TV catalog (X50 Ultra Max, RS 20, T10, Play 6, AURA2, Sunlight). The observed CSS shows a neutral, product-photography-led foundation: white canvas, dark-gray body text (#333 at 14px/1.5 with .7px letter-spacing), a light gray page background, and thin hairline grays used for cards and dividers. No single CSS rule labels a "brand color," so the orange (#ec6c00) is treated as an inferred primary accent, selected because warm oranges recur across the palette (#ff6700, #ff5644, #f89429) consistent with promotional badges ("新品", "热销") seen in the page text. A teal (#19caa6) and blue (#2566e8) are reused as secondary/tag accents rather than invented. Typography is inferred from the explicit Roboto/Helvetica/Arial stack plus commonly bundled CJK families (PingFang SC, Microsoft Yahei) for headings, since the source is Chinese-language. Layout patterns (hero carousel, grid product cards, dark footer) are proposed conventions for a projector/TV e-commerce catalog, not measured page geometry, and are flagged accordingly throughout.

colors:
  primary: "#ec6c00"
  ink: "#1f1f1f"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#e5e5e5"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#19caa6"
  accent-red: "#ff5644"
  accent-blue: "#2566e8"
  surface-dark: "#191919"
typography:
  display-xl: {fontFamily: "PingFang SC, Microsoft Yahei, Roboto, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "PingFang SC, Microsoft Yahei, Roboto, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.3px}
  title-md: {fontFamily: "PingFang SC, Microsoft Yahei, Roboto, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.7px}
  body-sm: {fontFamily: "Roboto, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.5px}
  caption: {fontFamily: "Roboto, Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Roboto, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.none} {spacing.xl}"
    hairline: "{colors.hairline}"
  hero-carousel:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  spec-compare-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** is proposed for primary calls to action such as "了解详情" (learn more) or add-to-cart. It uses the inferred orange accent against white text, matching the promotional-tag warmth seen across the palette; hover/active states are not observed and are proposed as a slight opacity or darken shift.

**button-secondary** covers outline actions (e.g. filter toggles, secondary nav links), using a white fill with a hairline border and ink text, mirroring the `XuiButton-outlined` white-background rule found in the CSS evidence.

**text-input** represents search or form fields. The light gray fill (`surface-soft`) and hairline border are proposed conventions consistent with the site's generally muted gray palette; no explicit input styling was captured beyond the body font rule.

**nav-bar** models the observed `.official_header__29cf1` rule: a white, full-width bar with a soft drop shadow, containing category links (家用娱乐, 激光电视, 便携娱乐, etc.). Height and exact spacing are not measured and are treated as proposed defaults.

**hero-carousel** reflects the Swiper-based rotating banner evidenced by `.swiper-button-next/prev` and related theme-color variables, used here for the rotating "X50 Ultra Max / RS 20 / T10 / Play 6" hero promotions. Dark overlay background and large display type are proposed for legibility over product photography, not confirmed from layout CSS.

**product-card** supports catalog and "爆款推荐" grid tiles: white surface, rounded corners, hairline border, and a title-weight product name. Image aspect ratio and hover elevation are proposed, not observed.

**badge** covers the small status labels seen in the page text ("新品", "热销", "下单赠"). A red fill is chosen from the palette as an attention color; teal or orange variants are equally plausible substitutes for different badge semantics (new vs. bestseller), left as an implementation choice.

**footer** models the dark, multi-column link footer implied by the extensive footer text block (关于极米, 服务支持, 联系我们). A dark surface color is inferred since no footer background was directly captured in the CSS sample; this is a stylistic proposal for contrast against the white body.

**spec-compare-table** is a category-appropriate addition for projector/TV product pages, where brightness, resolution, and DMD-size comparisons are typical. Styling reuses the muted surface and hairline tokens; no table markup was present in the supplied CSS.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Range | Target | Notes |
|---|---|---|
| ≥1280px | Desktop | Multi-column nav, grid product cards (4–5 per row) |
| 768–1279px | Tablet | Condensed nav, 2–3 column grids |
| <768px | Mobile | Collapsed hamburger nav, single-column stacked cards, carousel becomes swipeable full-width |

Touch targets for buttons and badges should be at minimum 40–44px in height on mobile. Navigation should collapse into a drawer/menu below the tablet breakpoint. These recommendations are standard e-commerce practice applied to the observed component set; no actual responsive CSS or media queries were present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot only; no rendered layout, hover/focus states, animation, or actual mobile behavior was observed. The primary accent color (#ec6c00) and several semantic role assignments (ink, muted, hairline, surface-dark) are inferred from palette frequency and general e-commerce convention, not from explicit component-level CSS captured in the evidence. Font sizing beyond the body rule (14px/1.5/.7px) is proposed, as no heading or button font-size rules were supplied. CJK font families (PingFang SC, Microsoft Yahei, MiSans) are known to be bundled/system fonts on the page but their exact application to specific text roles was not confirmed. Licensing/availability of any custom or proprietary fonts was not verified. Breakpoints, spacing scale, and rounded-corner values are proposed defaults, not measured from the source.
