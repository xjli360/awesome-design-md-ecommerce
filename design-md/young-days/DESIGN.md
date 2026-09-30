---
version: alpha
name: "Young Days"
source_url: "https://youngdays.com"
captured_at: "2026-09-29T04:17:04.446423+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Young Days is a direct-to-consumer organic baby and toddler clothing brand
  built around a warm, neutral-first palette accented with playful color.
  The observed CSS exposes a warm cream family (#f7efe5, #faf0e8, #dbba8e)
  alongside near-black text tokens (#121212, #070707) and a coral accent
  (#dd534a) that reads as the brand's primary call-to-action color given its
  saturation relative to the otherwise muted, "neutral colors and patterns"
  positioning stated in the page copy. Secondary tints — a soft green
  (#6cc04a/#9acc7d), a pale sky blue (#cdf3fc), a pale yellow-green
  (#eeffab/#f5ffcd), and an unexpected lilac (#7b61ff) — are inferred as
  collection/seasonal accent colors (e.g. "Cucumber Lemonade," "Fruit Salad")
  rather than core UI colors, since no selector ties them to persistent chrome.
  Two blue values (#1990c6, #136f99) are treated as an inferred link-hover
  pair. Typography pairs a rounded, single-weight display face (Darumadrop
  One) — fitting a playful kids brand — with a utilitarian sans (ABC Diatype)
  for body copy; Hrot Premium's role is unconfirmed and is provisionally
  assigned to mid-weight titles. All sizing, spacing, and radius values below
  are proposed design-system defaults, not measured from the live site.

colors:
  primary: "#dd534a"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#605c58"
  hairline: "#dedede"
  surface-soft: "#f7efe5"
  surface-card: "#faf0e8"
  on-primary: "#ffffff"
  border-strong: "#d9d9d9"
  state-inactive: "#beb9b5"
  overlay: "#0000007f"
  accent-tan: "#dbba8e"
  accent-green: "#6cc04a"
  accent-green-soft: "#9acc7d"
  accent-lilac: "#7b61ff"
  tint-blue: "#cdf3fc"
  tint-yellow: "#f5ffcd"
  link-hover: "#1990c6"
  link-hover-dark: "#136f99"
typography:
  display-xl: {fontFamily: "'Darumadrop One', cursive", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Darumadrop One', cursive", fontSize: "32px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Hrot Premium', 'ABC Diatype', sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0"}
  body-md: {fontFamily: "'ABC Diatype', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0"}
  body-sm: {fontFamily: "'ABC Diatype', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.01em"}
  caption: {fontFamily: "'ABC Diatype', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "'ABC Diatype', sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1.4, letterSpacing: "0.01em"}
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
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary**: The coral (#dd534a) fill is proposed as the primary conversion color for "Add To Cart," "Shop Now," and promo CTAs, based on its higher saturation relative to the brand's otherwise neutral, cream-forward palette. Hover/active states are not observed and are proposed as a modest darken or the shared `--color-link-text-hover-primary` token.

**button-secondary**: An outline treatment in ink is proposed for lower-emphasis actions (e.g. "Quick View," size guide links), reusing the accordion-heading border-radius language observed in `.product__accordion-heading`.

**text-input**: Search and account fields are proposed with a light hairline border and white background, matching the largely white/cream canvas implied by `body` and `.product__benefits` styling; focus state is unobserved.

**nav-bar**: A white sticky header with mega-menu categories ("Baby," "Kids," "Shop by Size") is inferred from the page-text structure; no header CSS selectors were supplied, so background and elevation are proposed defaults.

**product-card**: Cards use white backgrounds with a hairline border and rounded corners consistent with the 10px radius observed on `.product__benefits`; price and title typography reuse body tokens since no dedicated product-card CSS was captured.

**hero**: The homepage banner ("Get Spooky," "New Fall Collection") is proposed against the soft cream surface (#f7efe5) with the display font for headline treatment; actual hero markup/CSS was not in evidence.

**footer**: A warm cream card background is proposed to visually close the page below a white body, using muted text for secondary links; not confirmed by supplied selectors.

**badge**: Small pill badges (e.g. "NEW," "Organic," collection tags like "Fruit Salad") are proposed using the soft green accent, reflecting the brand's organic/eco messaging in body copy; exact badge markup was not observed.

**search**: Modeled identically to text-input with an icon slot; the `swiper-icons` font family present in evidence suggests an icon-font dependency site-wide, though search-specific icon usage is unconfirmed.

**size-selector**: A category-specific component for the observed age/size taxonomy (0–3M through 6T). Selected-state styling (inverted ink fill) is proposed to communicate in-stock/selected sizing, echoing the page copy's "Never shop out-of-stock items again" messaging; actual selected/disabled visuals were not in the supplied CSS.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed nav to hamburger + mega-menu drawer |
| tablet | 640–1023px | 2-column product grid, condensed nav |
| desktop | ≥1024px | 3–4 column grid, full mega-menu on hover |

Touch targets should be a minimum 44×44px for size-selector chips and add-to-cart buttons. Mobile category/size filters are proposed to collapse into an accordion or bottom-sheet pattern rather than the desktop mega-menu, given the deep category/size nesting seen in the page text (Baby/Kids × category × size). No mobile layout, hover, or breakpoint values were observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static snapshot of selectors, computed CSS custom-property names, page text, and a raw color/font list — not a rendered or interactive audit. Several `var(--color-*)` tokens (e.g. `--color-heading-primary`, `--color-link-text-hover-primary`, `--color-accent-tertiary`, `--color-benefits-bg`, `--color-state-inactive`) reference CSS custom properties whose resolved hex values were not supplied; mappings to specific palette entries above are inferred by plausibility, not confirmed. The role of "Hrot Premium" versus "ABC Diatype" versus "Darumadrop One" in actual heading/body usage is unverified — assignments here are a reasonable interpretation based on typical display/body pairing, not extracted font-family CSS. All font licensing and web-font availability are unverified. No spacing, breakpoint, hover, focus, disabled, or mobile-menu behavior was directly observed; all such values are proposed defaults for internal consistency only. Component definitions (hero, footer, nav-bar, search, product-card) are structurally inferred from page copy and generic e-commerce conventions, not from captured layout CSS.
