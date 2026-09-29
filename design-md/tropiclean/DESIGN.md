---
version: alpha
name: "TropiClean"
source_url: "https://tropiclean.com"
captured_at: "2026-09-28T10:34:04.084210+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  TropiClean's storefront CSS exposes a Shopify-based theme built on IBM as the shared heading and body font family, with generic sans-serif fallbacks and no confirmed proprietary webfont license. The observed palette centers on a deep forest green (#154c38 and near-variants like #005430, #184c3b) paired with a high-contrast lime-green accent (#bcec7a and siblings such as #b5ea6c, #afe85e), which is inferred here as the brand's primary/accent pairing given their repetition and separation from the extensive neutral gray scale (#f4f4f4 through #202223) used for surfaces, hairlines, and body text. A cluster of coral/orange tones (#ec523e, #fe8b58, #ff8a4e) is treated as a secondary "warm" accent for promotional or trending badges, consistent with the page's "Trending on TikTok" and bundle-callout content. Payment-network colors (Mastercard reds/oranges, PayPal/Amex blues) were excluded from brand roles as they are third-party iconography, not brand tokens. Button styling evidence shows an explicit CSS reset zeroing border-radius on raw `button` elements, suggesting a squared, no-radius default for primary actions; a rounded scale is still provided for cards and inputs as a proposed, unverified convention. Overall the interpretation favors a clean, high-trust, ingredient-forward grooming brand: dark green authority, lime-green energy, and generous neutral whitespace.

colors:
  primary: "#154c38"
  accent: "#bcec7a"
  warm-accent: "#ec523e"
  ink: "#202223"
  canvas: "#ffffff"
  body: "#515251"
  muted: "#757575"
  hairline: "#e0e0e0"
  surface-soft: "#f4f4f4"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "ibm, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "ibm, sans-serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "ibm, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "ibm, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "ibm, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "ibm, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "ibm, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
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
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.warm-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  trust-stat-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    statTypography: "{typography.display-md}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"

## Components

**button-primary**: Maps to the observed `.btn--primary` rule, which defines a diagonal two-tone hover background via `linear-gradient` between `--btn-bg-color` and `--btn-bg-hover-color`. Here it is rendered as the deep-green primary with white text; the CSS reset on raw `button` elements (`border-radius: 0`) is the basis for assigning `rounded.none`, though the actual computed theme value for `--btn-*` variables was not resolvable from static evidence, so exact hover colors are proposed.

**button-secondary**: Based on `.btn--secondary`, observed to use a transparent background (`--btn-alt-bg-alpha: 0`) with a border and text color both tied to `--btn-alt-text-color`. Interpreted as an outlined primary-green button on white surfaces; hover/focus fill behavior is proposed, not confirmed.

**text-input**: No direct input CSS was supplied beyond shared `--input-bg-color`/`--input-text-color` custom properties inheriting from `--bg-color`/`--text-color`. Styling (border, radius, padding) is therefore a proposed convention consistent with the neutral hairline palette.

**nav-bar**: Evidence includes menu-related text content ("Shop", "About us", "Bark Blog", "Account", "Cart") but no captured layout CSS. A light canvas bar with dark text and a bottom hairline is proposed as a conventional Shopify header pattern; actual sticky/collapse behavior is unobserved.

**product-card**: Inferred from the dense list of named SKUs ("TropiClean Papaya + Coconut Pet Shampoo...") displayed in grid-like merchandising sections ("Best Sellers," "Trending on TikTok"). Card surface, radius, and internal type scale are proposed since no card component CSS was in the evidence set.

**hero**: The page text references a rotating top banner ("Previous Slide / Next Slide," "Loved by Millions... Since 1980," "FREE Standard Shipping") suggesting a carousel-style hero or announcement bar. A dark-green full-bleed treatment with white heading type is proposed; actual banner styling was not in the supplied CSS.

**footer**: No footer-specific selectors were supplied. A dark ink background with white body text is proposed for contrast and brand consistency with the deep-green/near-black tones present in the palette, not confirmed from captured rules.

**badge**: Repeated "Trending on TikTok," "#1 Bestseller," and stat callouts (e.g., "45 yrs," "150K+ Positive Brand Reviews") suggest a pill-shaped label pattern. The warm coral accent is proposed for these labels to visually separate promotional flags from primary brand green; exact badge markup/CSS was not observed.

**search**: No search-bar CSS was captured; a soft-gray field consistent with `--input-bg-color` inheritance is proposed for discoverability of the "Shop" mega-menu categories (By Problem, By Category) referenced in the text.

**trust-stat-bar**: Category-appropriate component reflecting the page's numeric trust markers ("45 yrs," "150 K+ Positive Brand Reviews," "4 sec... One Bottle Sold Every 4 Seconds," "over 25,000 five star reviews"). Rendered on a soft neutral surface with large green stat numerals and small caption labels; layout (grid vs. row) is proposed.

## Responsive Behavior
Recommended, not measured — the source CSS included fluid-typography custom properties (`--fluid-vw`, `--fluid-max-vw: 1536`) implying a fluid scaling approach up to a ~1536px viewport, but no explicit breakpoint values were present in the supplied rules.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column stacks; nav collapses to hamburger + slide-out menu; hero text reduces to `display-md`. |
| Tablet | 768–1023px | 2-column product grids; mega-menu categories condense. |
| Desktop | 1024–1535px | Full mega-menu, 3–4 column product grids, fluid type scaling active per `--fluid-calc`. |
| Wide | ≥1536px | Fluid scaling caps per `--fluid-max-vw: 1536`; layout width likely constrained by a max container. |

Touch targets should be at least 44px in height for buttons and nav items on mobile; the mega-menu's "By Problem"/"By Category" submenu structure implies an accordion or drawer collapse pattern on small screens, which is proposed and not confirmed by captured interaction CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, JavaScript-driven interactions, or actual breakpoint values were observed. Semantic color-role assignments (primary vs. accent vs. warm-accent) are inferred from repetition and contrast within the supplied hex list, not from confirmed CSS variable resolution (e.g., `--btn-bg-color` values were referenced but never resolved to a literal hex in the evidence). Payment-icon colors (Mastercard/PayPal/Amex-like hexes) were deliberately excluded from brand roles. All pixel sizes in the typography scale, all `rounded` values besides the button reset, and all spacing values are proposed defaults, not measured from the site. The "Montserrat" font appears in the raw font-family evidence but its actual application (vs. IBM) could not be confirmed and was excluded from the primary type stack. Mobile menu behavior, carousel/slider mechanics, and card grid structure are described only as plausible Shopify-theme conventions. No custom font licensing or hosting was verified.
