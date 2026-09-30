---
version: alpha
name: "Briggs & Riley"
source_url: "https://briggs-riley.com"
captured_at: "2026-09-28T09:30:29.694765+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Shopify theme variables and inline component
  styles for a premium American luggage and business-bag brand. The observed
  palette is a restrained neutral system — a dark slate-grey (#4a4e54) carries
  body text, links, and primary buttons, paired with near-black nav text
  (#000000/#1c1d1d), soft off-white surfaces (#f2f2f2, #fafafa, #f7f7f7), and a
  cool hairline grey (#d9d9d6) for borders. A single warm burnt-orange
  (#ee5600, with a lighter #ff6b0e used for cart/sale accents) is the only
  saturated color, reserved for CTAs, the announcement bar, and sale
  indicators — this dominant-accent role is directly observed in theme
  variables and hero button rules.

  Typography pairs Montserrat (sans-serif, weights 400/500/600/700) as the
  workhorse for navigation, body copy, and buttons, with ivypresto-display
  (serif) reserved as an accent face — inferred here for editorial headlines
  and collection titles, consistent with a "engineered travel gear with a
  refined finish" brand tone. "Banks Sans light" appears in the evidence but
  its application is unconfirmed, so it is treated as a possible wordmark/logo
  face only, not a body font.

  Corner radii, spacing scale, and most component states below are proposed
  conventions for a durable-goods e-commerce catalog and are not literal CSS
  measurements from the source, except where noted.

colors:
  primary: "#ee5600"
  ink: "#1c1d1d"
  canvas: "#ffffff"
  body: "#4a4e54"
  muted: "#999999"
  hairline: "#d9d9d6"
  surface-soft: "#f2f2f2"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  secondary: "#4a4e54"
  secondary-hover: "#62676f"
  secondary-dim: "#3e4146"
  footer-bg: "#1c1d1d"
  nav-text: "#000000"
  badge-accent: "#ff6b0e"
  accent-alert: "#d02e2e"
  success: "#56ad6a"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0em"}
  display-md: {fontFamily: "'ivypresto-display', serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.0, letterSpacing: "0em"}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0em"}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em"}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em"}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.05em"}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.1em"}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.secondary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.nav-text}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.hairline}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  warranty-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    accent: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the site's single saturated accent — orange background from `--colorBtnPrimary`-adjacent hero/newsletter rules, white text, used for hero CTAs, newsletter submit, and add-to-cart actions. A disabled state (observed as `#000` background with white text) is a confirmed alternate state.

**button-secondary** uses the dark slate `#4a4e54` button color defined in theme root variables for lower-emphasis actions (e.g., "Learn More," filter toggles). Hover/active states using `#62676f`/`#3e4146` are proposed, mirroring the CSS custom properties `--colorBtnPrimaryLight` and `--colorBtnPrimaryDim` which exist but whose triggering states are not confirmed.

**text-input** covers newsletter, search, and account fields; border color and radius are proposed conventions since no explicit input CSS was supplied, though the neutral hairline and canvas background are grounded in the observed palette.

**nav-bar** reflects `--colorNav:#ffffff` and `--colorNavText:#000000` from theme root variables, with a mega-menu structure inferred from the extensive category list (New Luggage, Carry-On, Garment Bags, Briefcases, Collections). Dropdown/mobile-drawer behavior is not observed.

**product-card** is proposed for catalog/collection grids; background uses a light card surface for contrast against the white canvas, consistent with the light-grey surface tokens observed (`#f2f2f2`, `#fafafa`, `#f7f7f7`).

**hero** is grounded in the `.hero__link .btn` rule showing an orange CTA on a dark/video hero background; the `--colorHeroText:#ffffff` variable confirms white hero text. Video/slideshow behavior ("Pause slideshow / Play slideshow") is referenced in page text but interaction is not verified.

**footer** uses `--colorFooter:#1c1d1d` as background with `--colorFooterText:#4a4e54` for body copy, confirmed via theme root variables.

**badge** represents sale/cart-count indicators, grounded in `--colorSaleTag`/`--colorCartDot:#ff6b0e` variables.

**search** is a proposed pill-style search affordance; no search-input CSS was supplied, so radius and padding are conventions.

**warranty-panel** is a category-specific component proposed for this brand's "Simple as that® lifetime guarantee" messaging, referenced repeatedly in page text as a core trust signal for garment bags and business luggage; visual treatment (soft surface, orange accent rule) is inferred, not observed in CSS.

## Responsive Behavior

Recommended breakpoints (not measured from the live site):

| Breakpoint | Width       | Layout notes (proposed) |
|-----------|-------------|--------------------------|
| Mobile    | < 480px     | Single-column, hamburger nav, stacked hero CTA |
| Tablet    | 480–959px   | 2-column product grid, condensed nav |
| Desktop   | 960–1279px  | 3–4 column grid, full mega-menu |
| Wide      | ≥ 1280px    | 4+ column grid, max-width container |

Touch targets should be at minimum 44×44px for cart, nav, and CTA buttons. Mega-menu categories (New Luggage, Bags, Accessories, Collections) should collapse into an accordion pattern on mobile. This table is a recommendation only; no responsive CSS or mobile DOM was supplied in evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, computed styles, or JavaScript-driven interaction states were observed.
- Semantic color-role mapping (e.g., which greys serve "muted" vs "hairline" vs "surface-card") is inferred from variable naming and usage context, not visually confirmed.
- Font weights/sizes for `display-xl`, `title-md`, `body-sm`, `caption`, and `button-md` beyond the two directly observed root variables (`typeHeaderSize: 32px`, `typeBaseSize: 16px`) are proposed, not measured.
- `ivypresto-display` and `Banks Sans light` availability, licensing, and actual on-page usage are not verified; fallback to serif/sans-serif generics is assumed.
- Mobile navigation, drawer, and cart-flyout interaction patterns are inferred from class names (`.disclosure__button`, cart drawer text) but not observed in a live rendered state.
- Rounded-corner and spacing scales are conventional proposals for an e-commerce catalog, not derived from explicit `border-radius`/spacing CSS values in the supplied evidence.
