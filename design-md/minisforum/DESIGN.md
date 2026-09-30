---
version: alpha
name: "Minisforum"
source_url: "https://store.minisforum.com"
captured_at: "2026-09-29T04:08:42.703834+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Minisforum's storefront evidence shows a cool, technical e-commerce palette built on near-black text (#000000, #1a1a1a, #1d1d1f) over white and off-white canvases (#ffffff, #fafafa, #f5f5f5), with a saturated blue (#133ee3) driving the review-widget accent, links, and likely primary actions. Secondary reds (#d7002a, #ff4d4f) mark discount tags and "save" pricing, while a muted gray family (#333333, #6e6e73, #999999, #cccccc) carries body copy, captions, and disabled states. Thin hairlines (#e6e6e6, #e7e9ed) separate cards and panels typical of a dense specs-driven catalog (Mini PCs, Workstations, NAS, Motherboards).

  Font evidence is mixed: a large "Cartx…" font stack originates from a third-party review/widget script and is not treated as brand typography. More plausible interface fonts observed are Inter, Poppins, Roboto, PingFang SC, and MiSans, consistent with a China-headquartered hardware brand serving Latin and CJK audiences; system fallbacks (-apple-system, Helvetica Neue, Arial) round out the stack. This interpretation proposes Inter as the primary Latin display/body face with PingFang SC/MiSans as CJK fallbacks, sized against the few concrete CSS values observed (11–18px) and extrapolated upward for headings, which are labeled proposed rather than measured.

colors:
  primary: "#133ee3"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6e6e73"
  hairline: "#e6e6e6"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  ink-strong: "#000000"
  ink-alt: "#1d1d1f"
  border-subtle: "#e7e9ed"
  muted-soft: "#999999"
  muted-line: "#cccccc"
  danger: "#d7002a"
  save-accent: "#ff4d4f"
  link-alt: "#465fff"
  info-blue: "#3b99fc"
  success-green: "#7ac142"
  surface-canvas-alt: "#fafafa"
  surface-tint: "#f2f2f2"
  scrim-dark: "#00000099"
  overlay-light: "#ffffffcc"
typography:
  display-xl: {fontFamily: "Inter, -apple-system, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, -apple-system, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, -apple-system, Helvetica Neue, Arial, sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, PingFang SC, MiSans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, PingFang SC, MiSans, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Inter, PingFang SC, MiSans, sans-serif", fontSize: 11px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  button-md: {fontFamily: "Inter, PingFang SC, MiSans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    height: "80px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    compareTextColor: "{colors.muted-soft}"
  discount-badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  hero:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-canvas-alt}"
    textColor: "{colors.body}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-comparison-row:
    backgroundColor: "{colors.surface-card}"
    borderBottom: "1px solid {colors.border-subtle}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — proposed for primary CTAs ("Shop Now," "Buy Now," "Add To Cart"). Uses the observed accent blue (#133ee3), which appears in the CSS as the review-widget's primary color and is inferred to extend to storefront CTAs given its saturation and prominence in the palette.

**button-secondary** — proposed outline variant for lower-emphasis actions ("Learn More," "Explore More," "View All"), using the same primary blue as border/text on a transparent fill to preserve hierarchy without adding new colors.

**text-input** — proposed styling for newsletter/search fields (e.g. the footer "Email" capture), using hairline borders and body-md typography; no focus or validation states were observed, so those remain unspecified.

**nav-bar** — inferred from the `.header__columns` grid rule (min-height: 80px, three-column grid), giving a left/center/right layout for logo, primary nav ("Products," "Shop By," "Deals," "Explore & Support"), and cart/account icons.

**product-card** — grounded in the `.vidhash_likeProduct` rules, which show an aspect-ratio:1 image box, 8px radius, 12–14px title text, and a strikethrough compare-price in muted gray (#999999). Extended here to the main catalog grid (e.g. MS-A2, UM890 Pro listings) as a proposed generalization.

**discount-badge** — based on the observed `.vidhash_likeProduct_discountTag` style (red background #b20500-adjacent, white text, 4px radius); mapped to the closest supplied palette red (#d7002a) since the exact widget red was not in the top-level palette list.

**hero** — proposed full-bleed banner pattern for rotating promos (MS-S1 MAX-P495, S5 NAS, M2 PRO) referenced in the page text; dark background is inferred from the presence of near-black tokens (#000000, #0a1119) suitable for high-contrast product photography overlays.

**footer** — proposed structure covering the observed link groups (Products, Support, Program, Explore) and newsletter capture, set on the lighter off-white surface (#fafafa) to visually separate from the white body canvas.

**badge** — proposed pill component for merchandising labels seen in text ("New," "Hot," "Best Seller," "Save $XXX"), using a neutral tinted background so it can recolor per context without introducing new hues.

**search** — proposed header search affordance; no dedicated search CSS was supplied, so styling is extrapolated from the input and surface-soft tokens.

**spec-comparison-row** — category-appropriate addition for a PC/workstation storefront, proposed for tabular spec sheets (CPU/GPU/RAM rows seen throughout product blurbs like "AMD Ryzen™ AI Max+ 395 | Radeon 8060S | Up to 200TB"), using hairline dividers and caption-weight labels.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <480px | Single-column product grid, collapsed hamburger nav, sticky bottom cart bar (pattern hinted by `.vidhash_footerDiv` fixed-bottom styling in the review widget) |
| Tablet | 480–960px | 2-column product grid, condensed header |
| Desktop | 960–1280px | 3–4 column grid, full nav-bar grid areas active |
| Wide | >1280px | Up to 6-column grid for featured-product carousels |

Touch targets should be at least 44px; the 80px header height observed suggests generous top-nav spacing already accommodates this. Mobile nav collapse and drawer behavior are proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All layout beyond the single `.header__columns` grid rule and the `.vidhash_*` widget snippets is inferred; no broader stylesheet was supplied.
- Font attribution is uncertain: the large "Cartx…" list is a third-party review-widget font catalog, not confirmed brand typography; Inter/PingFang SC/MiSans were selected as the most plausible interface fonts from the remaining evidence but are not verified as licensed or actually rendered.
- Heading sizes (display-xl/md, title-md) are proposed extrapolations; only 11–18px values were directly observed in CSS.
- Hover, focus, active, and error states for buttons/inputs were not present in the supplied CSS and are unspecified.
- Mobile/responsive behavior, breakpoints, and interaction patterns were not observed and are recommendations only.
- Some palette colors (e.g. #7ac142, #3b99fc, #465fff) have no clear role in the supplied CSS rules; they are included in the token set for completeness but their semantic use is unconfirmed.
