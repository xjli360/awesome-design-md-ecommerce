---
version: alpha
name: "Wolfgang Man & Beast"
source_url: "https://wolfgangusa.com"
captured_at: "2026-09-29T03:53:12.902218+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wolfgang's storefront CSS exposes a compact, high-contrast system built around a near-black ink
  (#212322) paired with a signature aqua-teal accent (#7eddd3) used as the primary button and
  Judge.me star color. Body surfaces run on off-white (#fafafa) with a slightly dimmer gray
  (#ededed) for secondary sections, while the footer inverts to the same dark ink with white
  text. Two typefaces are declared in root variables: Fjalla One (condensed, uppercase-leaning
  display sans) for headers, and Barlow for all body, button, and form text — both observed
  directly in :root custom properties. Additional families (Nunito Sans, Source Sans 3,
  Baskerville, DIN Condensed Bold) appear in the broader font list but their exact application is
  not confirmed from the supplied rules, so they are treated here as supplementary/inferred rather
  than primary. Buttons are flat with zero corner radius and heavy uppercase tracking
  (letter-spacing ~0.3em), reflecting an outdoor-gear, utilitarian brand voice rather than a soft
  lifestyle aesthetic. Sale/urgency messaging uses a saturated red (#b30000/#990000), reserved
  strictly for pricing and stock-related callouts. This interpretation extends the confirmed
  tokens into a full component set for a collars/leashes/harnesses catalog, explicitly labeling
  unobserved spacing, radii, and layout as inferred/proposed.

colors:
  primary: "#7eddd3"
  primary-dim: "#6ad8cc"
  primary-light: "#a6e8e1"
  ink: "#212322"
  canvas: "#fafafa"
  body: "#212322"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#212322"
  footer-bg: "#212322"
  footer-text: "#ffffff"
  sale: "#990000"
  savings: "#b30000"
  disabled-bg: "#f6f6f6"
  disabled-text: "#b6b6b6"
typography:
  display-xl: {fontFamily: "'Fjalla One', sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  display-md: {fontFamily: "'Fjalla One', sans-serif", fontSize: 45px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  title-md: {fontFamily: "'Fjalla One', sans-serif", fontSize: 23px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.025em}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.025em}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.025em}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.42, letterSpacing: 0.3em}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.footer-text}"
    overlayColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.footer-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  variant-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "32px"

## Components

**button-primary** — Maps directly to the observed `.btn` rule: teal fill, dark ink text, zero
radius, bold uppercase label with wide tracking. Used for add-to-cart, subscribe, and checkout
actions; hover state (also observed) keeps the same colors, so no separate hover token is
proposed.

**button-secondary** — Not directly observed; proposed as an outlined variant using the same ink
border/text color seen for links and body copy, for lower-emphasis actions like "View all" or
filter toggles.

**text-input** — Inferred from general form defaults (`body,button,input,select,textarea` share
the Barlow base font rule). Border and radius are proposed since no explicit input border-radius
or color was captured.

**nav-bar** — Backed by `--colorNav:#ffffff` and `--colorNavText:#212322`. Structure (mega-menu
categories: Collars, Leashes, Harnesses, Martingales) is inferred from page text, not from
measured layout CSS.

**product-card** — Grid/gutter values (`--grid-gutter:22px`) confirm a card-grid listing pattern;
internal card padding, border, and title/price pairing are proposed to match the Best Sellers
listing referenced in page text.

**hero** — Uses observed `--colorHeroText:#ffffff` over a dark background and the Fjalla One
display type; flickity slider controls (`.hero .flickity-button`) confirm an image-carousel hero,
though exact slide count/timing is not observed.

**footer** — Directly grounded in `--colorFooter:#212322` / `--colorFooterText:#ffffff`; link
list content (About, Terms, Returns, Warranty) is taken from page text.

**badge** — Sale/discount tag colors (`--colorSaleTag:#990000`, `--colorSaleTagText:#ffffff`) are
observed; badge shape/padding are proposed for a small pill/rectangle used on discounted
products.

**search** — Predictive search drawer is referenced in page text ("Search Site navigation");
visual treatment (soft gray field) is proposed, not confirmed by supplied selectors.

**variant-swatch** — Category-appropriate addition for a collar/leash/harness catalog: a
circular color or print swatch selector, styled with the same hairline border and a teal
selected-state ring drawn from the primary accent. This pattern is proposed to support the
site's many print-based collections (Florals, Mountain, Patriotic) and is not confirmed by any
supplied selector.

## Responsive Behavior

Proposed breakpoint table (not measured from live responsive CSS):

| Breakpoint | Width      | Nav behavior                  | Grid columns |
|-----------|------------|--------------------------------|--------------|
| Mobile    | <600px     | Collapsed hamburger + drawer   | 1–2          |
| Tablet    | 600–999px  | Condensed horizontal nav       | 2–3          |
| Desktop   | ≥1000px    | Full mega-menu nav             | 3–4          |

Touch targets for buttons and swatches should maintain a minimum 44×44px hit area; the cart
drawer referenced in page text ("Close cart") implies an off-canvas panel pattern on mobile.
This table is a recommendation only — no media queries or breakpoint values were present in the
supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/text; no rendered layout, hover/focus states, or actual
  responsive breakpoints were observed.
- Semantic role mapping for grays (`muted`, `hairline`) is inferred from a broad palette list
  without confirmed selector usage for those specific roles.
- All spacing scale values beyond the observed `--grid-gutter:22px` and `--drawer-gutter:30px`
  are proposed approximations, not measured.
- Secondary fonts (Nunito Sans, Source Sans 3, Baskerville, DIN Condensed Bold, Consolas) appear
  in the raw font list but their selector-level usage was not confirmed, so they are excluded
  from primary typography tokens.
- Font licensing/availability (e.g., Fjalla One via Google Fonts, Barlow via Google Fonts) is
  assumed based on common distribution but was not independently verified in this evidence set.
- Component states such as focus rings, error states, and disabled-input styling are proposed
  patterns, not sourced from supplied declarations.
