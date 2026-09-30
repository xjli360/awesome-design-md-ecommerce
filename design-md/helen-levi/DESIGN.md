---
version: alpha
name: "Helen Levi"
source_url: "https://helenlevi.com"
captured_at: "2026-09-29T04:10:20.973774+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Helen Levi Ceramics presents a spare, ink-on-paper aesthetic built around two typefaces: HL-T, a custom uppercase display face used sparingly for page titles and section headers, and Everson Mono, a bold monospace that carries body copy, navigation, form controls, and product metadata. The observed palette is tight and print-like: a deep indigo-blue (#2F3490) serves as both the primary brand color and default body-text color, paired against a warm off-white cream (#F5F2E3) that functions as the dominant background/canvas. Near-black (#121212/#000000) and white (#ffffff) appear as secondary ink and surface values, while soft grays (#dedee2/#dedede) and alpha-blended blacks (#00000033, #0000004d, #0000001a) suggest hairlines, overlays, and disabled or inactive states. Two cyan-blue accents (#1990c6, #136f99) are inferred as link/interactive-hover colors distinct from the primary indigo. Inputs and buttons observed in CSS use cream backgrounds with a 1px cream-tint border and 2px border-radius, giving a boxy, stamped-label feel appropriate to handmade pottery. Layout spacing is generous and grid-based (12-column, 48-96px page margins, 64px vertical rhythm), reinforcing a gallery-like, uncluttered presentation of ceramic objects. All semantic role assignments below (ink vs. muted vs. hairline) are inferred from usage context, not explicitly labeled in source CSS.

colors:
  primary: "#2f3490"
  ink: "#121212"
  canvas: "#f5f2e3"
  body: "#2f3490"
  muted: "#2f349099"
  hairline: "#dedee2"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#f5f2e3"
  link: "#1990c6"
  link-hover: "#136f99"
  overlay: "#0000004d"
  border-subtle: "#00000033"
  border-faint: "#0000001a"
  true-black: "#000000"
typography:
  display-xl: {fontFamily: "HL-T, sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "0.08em"}
  display-md: {fontFamily: "HL-T, sans-serif", fontSize: "24px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0.08em"}
  title-md: {fontFamily: "Everson Mono, monospace", fontSize: "16px", fontWeight: 700, lineHeight: 1.28, letterSpacing: "0.08em"}
  body-md: {fontFamily: "Everson Mono, monospace", fontSize: "22px", fontWeight: 700, lineHeight: 1.28, letterSpacing: "normal"}
  body-sm: {fontFamily: "Everson Mono, monospace", fontSize: "16px", fontWeight: 700, lineHeight: 1.28, letterSpacing: "normal"}
  caption: {fontFamily: "Everson Mono, monospace", fontSize: "13px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0.04em"}
  button-md: {fontFamily: "Everson Mono, monospace", fontSize: "17px", fontWeight: 700, lineHeight: 1.28, letterSpacing: "normal"}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-subtle}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.xxl}"
    gap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    thumbnailBorderActive: "{colors.muted}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    border: "1px solid {colors.border-subtle}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    placeholderColor: "{colors.muted}"
  shape-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
    activeBorder: "{colors.muted}"

## Components

**button-primary** is proposed for primary calls to action (Add to Cart, Continue Shopping) using the indigo brand color with cream text, matching the CSS `body` color relationship inverted for emphasis; exact button background was not directly observed on a submit element, so the mapping is inferred from the header-menu's blue/cream pairing.

**button-secondary** covers lower-emphasis actions (e.g., "Continue shopping" link-style buttons) using cream fill with indigo text and a soft border, mirroring the observed `input,button` cream background but without full-weight emphasis; hover/focus states are proposed, not observed.

**text-input** reflects the directly observed `input,button,select,textarea` rule: cream background, 1px cream-tint border, 2px radius, monospace bold type. This is one of the few components with strong CSS evidence.

**nav-bar** represents the `.header__menu` pattern: a full indigo-blue background with cream text and monospace links, used for the slide-out/overlay navigation observed in the stylesheet (`display:none` by default, column layout with 40px gaps). Horizontal top-bar arrangement is inferred, not confirmed.

**product-card** is proposed for shop-grid tiles (mugs, plates, lamps), combining the HL-T uppercase title style seen on `.product-info h1` with an inferred white card surface and the observed active-thumbnail border color (`#2f349099`).

**hero** is a proposed landing/homepage banner pattern using the larger inferred display-xl size on cream canvas; no hero-specific CSS was supplied, so scale and padding are estimates consistent with the page's generous margin variables (48–96px).

**footer** uses the small caption typography scale and cream background seen sitewide, with copyright and policy links (as referenced in page text: "Shop Policies," "Mailing List"); exact footer layout was not present in the CSS evidence.

**badge** is proposed to represent the site's "Less Than Perfect" seconds-sale labeling and pattern tags (Artist Stamped, Marbled) — a small outlined cream chip with indigo text, inferred from the general button/border treatment rather than a dedicated badge rule.

**shape-filter-chip** is a category-appropriate component addressing the "Shop by Shape" / "Shop by Pattern" navigation (Mugs & Cups, Plates & Bowls, Lamps) referenced in page text, styled as a pill using title-md typography; no pill-specific CSS was observed, so this is fully proposed.

## Responsive Behavior

| Breakpoint | Approx. width | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Page margin/gutter drop to 20px (observed CSS var override); nav collapses to full-screen indigo overlay menu (`.header__menu`, `display:none` default toggled open) |
| Tablet | 600–1024px | Grid likely reduces from 12 columns; margins scale via clamp(48px,4.5vw,96px) |
| Desktop | ≥1024px | Full 12-column grid, 48–96px page margins, 64px section rhythm as defined in `:root` |

Touch targets should be at least 44px in the mobile overlay nav given the 40px `gap` already specified between menu items. Collapse behavior (hamburger toggle, cart drawer) is referenced by class names (`.menu--open`, `.header__cart`) but actual interaction/animation was not observed in static CSS. This table is a recommendation based on variable naming, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived solely from static CSS custom properties, selector rules, and page-text excerpts; no rendered layout, computed styles, animation timing, or JavaScript-driven interaction (cart drawer, menu toggle, search overlay) was directly observed. Semantic color roles (ink, muted, hairline, overlay) are inferred from selector context (e.g., alpha-blended blacks used on borders) rather than explicit design-token names in source. Typography sizes for display-xl, caption, and shape-filter-chip are proposed extrapolations beyond the two confirmed sizes (24px HL-T headings, 16–22px Everson Mono body/UI). The `rounded` scale beyond `xs` (2px, the only radius value found in evidence) is a conventional proposed scale, not confirmed elsewhere on the site. Mobile menu, product gallery, and cart-drawer layouts were not visually observed — only inferred from class names and the mobile `:root` override (20px margins, 144px page-start). Availability, licensing, and web-font-loading behavior for the custom "HL-T" typeface were not verified; a generic sans-serif fallback is assumed acceptable. Additional palette values (e.g., `#00000040`, transparent `#00000000`) were not confidently mapped to a role and are omitted from the semantic token set.
