---
version: alpha
name: "Dango Products"
source_url: "https://dangoproducts.com"
captured_at: "2026-09-28T10:23:24.487268+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dango Products is a US-made everyday-carry brand selling wallets, watches, and
  rugged accessories. The observed palette is neutral-forward: white, warm
  off-white surfaces (#fff8f0, #fbf7ee, #f5f5ec), and a near-black warm ink
  (#16120c) paired with a saturated orange (#fa6400), a secondary burnt-orange
  (#ed702d) used for the star-rating icon, and deeper tone variants (#e05a00,
  #c75000). These oranges are treated here as the primary accent family, with
  #fa6400 assigned as the dominant CTA color; this role assignment is inferred
  from its saturation and prominence rather than a confirmed brand-token source.
  Material-inspired tones (leather brown #742d1e, olive #7e7f50, navy #1f284d,
  tan #a8916c) appear repeatedly and likely support product-swatch or badge
  contexts given the leather/metal finishes referenced in product names
  (Rawhide, Jet Black, Satin Silver).

  Typography uses a slab display face (cholla-slab) confirmed in CSS as
  --font-display for buttons, rendered bold, uppercase, with squared
  (border-radius: 0) primary/secondary buttons and fully circular icon
  buttons — a rugged, machined aesthetic consistent with the "engineered"
  copy. Body font (helvetica-neue-lt-pro) is inferred for running text since
  it appears in the observed font stack but no body-text CSS rule was
  supplied.

colors:
  primary: "#fa6400"
  primary-deep: "#c75000"
  accent-rating: "#ed702d"
  ink: "#16120c"
  canvas: "#ffffff"
  body: "#3d3d3d"
  muted: "#666666"
  hairline: "#d3d3d3"
  surface-soft: "#fff8f0"
  surface-card: "#f5f5ec"
  on-primary: "#ffffff"
  leather: "#742d1e"
  navy: "#1f284d"
  olive: "#7e7f50"
  tan: "#a8916c"
typography:
  display-xl: {fontFamily: "cholla-slab, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "cholla-slab, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "cholla-slab, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "helvetica-neue-lt-pro, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "helvetica-neue-lt-pro, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "helvetica-neue-lt-pro, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "cholla-slab, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    size: "44px"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    itemShape: "{rounded.full}"
    itemSize: "24px"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    labelTypography: "{typography.caption}"

## Components

**button-primary** is the orange filled CTA (`.btn--primary`), squared per observed `border-radius:0`, uppercase bold slab-display text confirmed in CSS; used for "Shop Now," "Add to Cart."

**button-secondary** mirrors the primary's size/shape (`.btn--secondary` shares `--button-min-height:3.8125rem`) but is outline-style on a light surface; color mapping to `{colors.primary}` for border/text is inferred from limited variable names (`--text-button-secondary`, `--border-button`) without resolved hex values.

**button-icon** covers the circular icon buttons (`.btn--icon-primary/secondary/tertiary`), all `border-radius:50%` at a consistent ~44px box — a comfortably touch-sized control, proposed for cart, account, and search triggers.

**text-input** is a proposed pattern for newsletter/account/search fields; no direct input CSS rules were supplied, so border, radius, and padding are inferred from the general hairline and spacing scale.

**nav-bar** reflects the mega-menu structure implied by the text excerpt (Wallets, Watches, Accessories, Bundles, Sale) sitting atop a "Free Shipping $75+" utility bar; visual treatment (background, border) is proposed, not measured.

**product-card** is proposed for grid listings (e.g., "M4 Maverick™ Rail Wallet," "A10 Adapt™ Wallet") showing title, star rating, price, and color swatches, consistent with the repeated rating/price/"Additional colors" pattern in the evidence.

**hero** models the homepage banner ("MADE FOR EVERYDAY / Designed For Today. Made To Last") as a dark, full-bleed section with a primary CTA; dark background is inferred from brand tone, not a captured hero background-color rule.

**color-swatch-selector** is the category-appropriate component for wallets/watches: circular swatches cycling through finishes like Rawhide, Jet Black, Satin Silver, and Whiskey Brown, matching the repeated "Additional colors" / "Selected value is" interaction pattern in the page text; selected/hover states are proposed.

## Responsive Behavior
| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column product grid, nav collapses to menu toggle (evidenced by "Toggle search" and "Menu" labels), touch targets ≥44px |
| Tablet | 768–1024px | 2-column product grid, mega-menu may remain collapsed |
| Desktop | >1024px | Multi-column mega-nav shown expanded, 3–4 column product grid |

This table is a recommendation based on typical ecommerce patterns and the presence of toggle/menu affordances in the evidence; no actual responsive CSS or viewport behavior was captured. Interactive states (hover, focus, active swatch selection) beyond the `.btn--tab` animated underline rule are likewise proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text only; no rendered layout, computed styles, or DOM screenshots were available, so all component compositions above are proposed interpretations.
- Several CSS custom properties (`--surface-button`, `--text-button`, `--border-button`, `--font-static-xxl`) are referenced but their resolved hex/px values were not supplied, so color and size mappings to these roles are inferred, not confirmed.
- `cholla-slab` is treated as a licensed/hosted webfont (commonly distributed via Adobe/Extensis); availability, licensing, and exact weight/width axes were not verified.
- Body copy font (`helvetica-neue-lt-pro`) role is inferred from the font stack; no body-text CSS rule with this family was directly supplied.
- Breakpoints, spacing scale, and rounded scale beyond the observed `0` (buttons) and `50%` (icon buttons) are proposed defaults, not measured values.
- Mobile/tablet layout behavior, cart drawer, and quick-view modal interactions were not observed and are described only as proposed patterns based on text-excerpt affordances ("Quick View," "Close Modal").
