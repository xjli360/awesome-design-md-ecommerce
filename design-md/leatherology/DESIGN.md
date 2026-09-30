---
version: alpha
name: "Leatherology"
source_url: "https://leatherology.com"
captured_at: "2026-09-28T09:49:45.919362+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Leatherology's storefront markup exposes a restrained neutral system built on Shopify Dawn-style CSS custom properties: a near-black foreground (rgb 18,18,18 / #121212) paired with a pure white background, used consistently for text, buttons, and badge borders. Supporting grays (#333333, #7f7f7f, #cccccc, #f7f7f7) appear across body copy, muted labels, and soft surface fills, while a distinct cool-gray/indigo set (#676986, #272d45, #dbdde4, #e5e5eb, #f4f4f6) comes from the third-party Okendo reviews widget rather than core brand chrome; it is retained here as a secondary system for review UI only. A warm sand tone (#cdc5b5), drawn from the "Natural Canvas" leather-color swatch data, is proposed as an inferred decorative accent evoking the brand's cowhide palette, not a confirmed interface color. A red (#d62027) present in the palette is labeled as an inferred sale/alert color, typical for ecommerce promotions, since no explicit UI role was captured. Typography draws on the observed family stack — FreightDispPro (light/medium) for display serif-leaning headlines, and ProximaNova/Assistant/Open Sans for UI and body sans-serif text — reflecting a quiet-luxury leather-goods aesthetic suited to passport holders and RFID travel accessories. All sizes beyond the single captured body rule (1.5rem) are proposed.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7f7f7f"
  hairline: "#dbdde4"
  surface-soft: "#f7f7f7"
  surface-card: "#f4f4f6"
  on-primary: "#ffffff"
  border-strong: "#cccccc"
  link: "#121212"
  accent-leather: "#cdc5b5"
  error-sale: "#d62027"
  review-accent: "#676986"
typography:
  display-xl: {fontFamily: "FreightDispProMedium, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "FreightDispProLight, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "ProximaNova, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "ProximaNova, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  personalization-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-leather}"
    labelTypography: "{typography.body-sm}"
    optionTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components
**button-primary** renders the site's near-black background with white text, matching the captured `--color-button`/`--color-button-text` pair; used for "Shop Now," add-to-cart, and RFID passport-holder purchase actions.

**button-secondary** is a proposed inverse treatment (white fill, dark border/text) for secondary actions such as "Continue shopping" or "View All," inferred from the presence of `--color-secondary-button` variables even though no visual instance was captured.

**text-input** covers search and account fields; border and radius are proposed defaults since no explicit input CSS was supplied, styled to sit quietly against the neutral palette.

**nav-bar** represents the mega-menu header structure implied by the extensive category text (Women, Men, Home & Office, Travel, Gifts); background and hairline are proposed, typography reuses observed body-sm sizing.

**product-card** is proposed for passport-holder and travel-wallet grid listings; title/price colors of `#000000`-equivalent (`{colors.ink}`) were directly observed in `.trending__product .product-item__title-text` and `.product-item__price` rules.

**hero** models the homepage banner pattern ("Travel — Considered Travel — Shop Now") using a soft neutral background and the largest display type; imagery and exact spacing are not observed.

**footer** is a proposed structural block for legal/account/newsletter content implied by the "Sign Up To Receive 10% Off" copy; visual styling not directly measured.

**badge** supports pill labels like "New," "Sale," or free-shipping callouts referenced in the page text; colors reuse the observed badge-foreground/background/border trio directly from `:root`.

**search** models the repeated "Search Search Search" UI control referenced in the extracted text; styling is proposed using surface-card and hairline tokens.

**personalization-selector** is a category-appropriate proposed component for monogram/hand-paint/logo personalization flows explicitly listed in the site's navigation (Trapunto, Hand Paint, Script, Logo), relevant to RFID passport-holder customization; the sand accent color is inferred from the observed "Natural Canvas" leather swatch data, not a confirmed UI color.

## Responsive Behavior
Proposed, not measured from live rendering:
| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <768px | Single-column nav collapses to hamburger/drawer; product grid 1–2 columns; touch targets ≥44px. |
| tablet | 768–1023px | 2–3 column product grid; mega-menu likely condenses to accordion. |
| desktop | ≥1024px | Full mega-menu with multi-column dropdowns (matches nav complexity in page text); 3–4 column product grid. |

Touch targets for buttons and nav items should maintain a minimum 44×44px hit area; mega-menu items should collapse into an accordion pattern below tablet width. This table is a recommendation only, not derived from observed responsive CSS or rendered breakpoints.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were directly observed beyond the Okendo review-widget button states, which are third-party and may not reflect core site components. Several colors (e.g., #676986, #272d45, #dbdde4) originate from the Okendo reviews plugin and are mapped separately as `review-accent`/hairline reuse rather than assumed brand chrome. The accent-leather (#cdc5b5) and error-sale (#d62027) roles are inferred assumptions, not confirmed UI usages. Root font-size context (rem base) was not captured, so absolute body/heading pixel sizes are approximate/proposed. Mobile menu, cart drawer, and personalization-tool interaction behavior were not observed. Custom font availability, licensing, and actual weight/style variants for FreightDispPro, AvenirLTStd, and ProximaNova were not verified and should be confirmed against Leatherology's licensed webfont files before implementation.
