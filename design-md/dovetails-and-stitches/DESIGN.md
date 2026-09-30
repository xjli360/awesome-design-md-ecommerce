---
version: alpha
name: "Dovetails and Stitches"
source_url: "https://dovetailsandstitches.com"
captured_at: "2026-09-28T05:06:25.268081+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dovetails and Stitches is a fourth-generation woodworking studio (Shopify storefront) selling
  handcrafted furniture, menorahs, kitchen accessories, and home decor. The observed palette is
  warm and material-led: a linen-paper background (#f4f0e7) and near-white surface (#fbf9f4) pair
  with a near-black ink (#25231f) for text, evoking raw hardwood and workshop paper stock rather
  than a typical white e-commerce canvas. An oxblood/walnut brown (#813f32, close to the observed
  link color #7a4229) reads as the brand's primary accent, reinforced by a muted brass (#a5824f)
  used for review stars and hover states in footer CSS — both are inferred as the studio's warm
  metal-and-wood accent pair. A saturated blue (#1990c6/#136f99) appears only in Shopify's native
  accelerated-checkout button and is treated as a system/utility color, not a brand color.
  Typography is dual: body copy is set in Source Sans 3/Source Sans Pro (confirmed via explicit
  footer CSS), a clean grotesque suited to product and care-instruction copy; headings use the
  theme's `--font-heading-family` variable, which resolves to Newsergider/Georgia-class serif
  fallbacks present in the evidence, so a serif (Newsreader, Georgia fallback) is proposed for
  display and title roles to match the "heirloom," letterpress-adjacent tone of the copy. Border
  radii observed on Shopify system buttons default to 0px, suggesting a squared, workshop-plain
  visual language; the token scale below keeps that flat baseline while allowing small radii for
  inputs and cards as a proposed, not measured, convention.

colors:
  primary: "#813f32"
  ink: "#25231f"
  canvas: "#f4f0e7"
  body: "#25231f"
  muted: "#7b7b7b"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#fbf9f4"
  on-primary: "#fbf9f4"
  brass: "#a5824f"
  oxblood: "#813f32"
  link: "#7a4229"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  gold-badge: "#fdcc0d"
  ink-deep: "#121212"
typography:
  display-xl: {fontFamily: "Newsreader, Georgia, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Newsreader, Georgia, serif", fontSize: 34px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Newsreader, Georgia, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Source Sans 3', 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.6px}
  body-sm: {fontFamily: "'Source Sans 3', 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "'Source Sans 3', 'Source Sans Pro', sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.8px}
  button-md: {fontFamily: "'Source Sans 3', 'Source Sans Pro', sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.8px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.link}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    accent: "{colors.brass}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    hairline: "rgba(165,130,79,.45)"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  material-swatch:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    accent: "{colors.brass}"
    typography: "{typography.caption}"
    padding: "{spacing.xs}"

## Components

**button-primary** renders as a near-black, squared call-to-action (matching the theme's `--color-button: 37,35,31` variable), used for "Check out," "Shop the Studio," and similar primary actions. Hover/focus states are proposed, not observed.

**button-secondary** uses the paper canvas background with the oxblood/link brown as border and text, intended for "Continue shopping," "Read the Blog," or outline CTAs alongside a primary button. Exact hover treatment is proposed.

**text-input** covers cart, search, and account fields; it borrows the near-white surface and a light hairline border consistent with the theme's flat, low-radius system defaults (Shopify accelerated-checkout button defaults to `border-radius: 0px`).

**nav-bar** is inferred from the multi-level "Shop / About Us" menu structure in the page text (Custom Furniture, Media Centers, Home Decor, Kitchen Accessories, Menorahs & Judaica). Proposed as a flat canvas-colored bar with a bottom hairline, no elevation/shadow observed.

**product-card** represents catalog tiles (e.g., "Solid Wood Knife Block," "Burl Wood Mirror") using the near-white surface for contrast against the paper page background, with brass used sparingly for star ratings per the Judge.me review widget variables (`--jdgm-star-color`, `--stars-color: #A5824F`).

**hero** models the homepage banner ("Fourth-generation furniture makers / Handcrafted wood furniture & home decor") as a large canvas-background block with serif display type; exact hero height/image treatment is not measured from static CSS.

**footer** is grounded directly in observed CSS: a dark ink background (`--dsf-ink`) with paper-colored text and a brass-tinted hairline (`rgba(165,130,79,.45)`), including a newsletter form button that inverts to brass on hover.

**badge** covers "Sold out" and "Sale" labels seen in the product excerpt, styled as an outlined ink-on-canvas tag consistent with the theme's `--color-badge-*` variables (border and foreground both use the ink color).

**material-swatch** is a category-appropriate, proposed component for wood-species or finish selection (e.g., Cherry, Quarter-Sawn White Oak, Mappa Burl mentioned in product titles), using brass as an accent to signal premium/selected material — not an observed UI pattern, purely inferred from product naming conventions.

## Responsive Behavior

This is a recommendation, not measured site behavior; no breakpoints or mobile layout were observed in the supplied static CSS.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <749px | Single-column product grid, collapsed hamburger nav, stacked hero text |
| Tablet | 750–989px | 2-column product grid, condensed nav labels |
| Desktop | 990–1279px | Full nav bar with dropdown mega-menu for "Shop"/"About Us" |
| Wide | ≥1280px | Max-width content container, 3–4 column product grid |

Touch targets should be a minimum 44×44px for cart, search, and nav icons. Primary nav should collapse to a drawer or accordion below tablet width, consistent with the multi-tier "Shop / Custom Furniture / Media Centers / Home Decor / Kitchen Accessories" menu structure implied by the page text.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction does not reveal actual rendered layout, grid structure, image aspect ratios, or spacing rhythm; all spacing and breakpoint values above are proposed conventions, not measured.
- `--font-heading-family` and `--font-body-family` are CSS custom properties whose resolved values were not directly captured; Newsreader/Georgia and Source Sans 3/Source Sans Pro are inferred from the available font-family list and one explicit footer declaration.
- JudgemeStar is a third-party review-widget font/icon set, not a brand typeface, and is excluded from brand typography roles.
- Border radius defaults (0px) are confirmed only for Shopify's native accelerated-checkout button and Judge.me widget variables; product card and input radii are proposed, not confirmed sitewide.
- No hover, focus, active, disabled, or error states were observed for buttons or inputs beyond the two explicit footer button rules; all other interaction states are proposed.
- Mobile menu, cart drawer, and search overlay behavior were not observed and are described only as conventional patterns.
- Custom/self-hosted font licensing and availability (Newsreader, Source Sans 3) were not verified against the live site's font-loading strategy.
