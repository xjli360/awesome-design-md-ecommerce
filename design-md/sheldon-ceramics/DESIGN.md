---
version: alpha
name: "Sheldon Ceramics"
source_url: "https://sheldonceramics.com"
captured_at: "2026-09-29T04:18:44.270913+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sheldon Ceramics is a Shopify-built storefront for handmade pottery, dinnerware,
  and home decor, organized around named collections (Farmhouse, Silverlake,
  Vermont, Terra Cotta, Indigo, Stoneware). The observed CSS custom properties
  set headings and body copy in "Crimson Text" (a serif), with Montserrat
  reserved as the accent/sans family for labels and interface chrome. Body copy
  renders at 14px with 1.5 line-height; section headings sit at 24px with
  normal-weight (400) serif letterforms and slight positive letter-spacing,
  suggesting a quiet, editorial tone appropriate to a craft/tabletop brand.
  The supplied palette is dominated by neutral grays and near-blacks (#232323,
  #4a4a4a, #717171, #dddddd) against white and warm off-white surfaces
  (#f6f5f4, #f7f7f7), consistent with a product-photography-forward layout.
  A cluster of blues (#51a7ca, #56b8d6, #2e629d) appears only in wishlist/
  registry hover states, so this interpretation treats the lighter blue
  (#51a7ca) as the primary interactive accent; this mapping is inferred, not
  confirmed as the brand's primary color elsewhere on the site. A muted
  terracotta (#9e6863) from the palette is proposed as a secondary accent to
  echo the "Terra Cotta Collection" naming. Rounded corners and spacing scales
  below are proposed conventions, not measured from layout.

colors:
  primary: "#51a7ca"
  ink: "#232323"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#717171"
  hairline: "#dddddd"
  surface-soft: "#f6f5f4"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent-terracotta: "#9e6863"
  accent-indigo: "#2c4762"
  error: "#cb1f2b"
  warning: "#f1d031"
typography:
  display-xl: {fontFamily: "'Crimson Text', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Crimson Text', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Crimson Text', serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0.025em}
  body-md: {fontFamily: "'Crimson Text', serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  body-sm: {fontFamily: "'Crimson Text', serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.08em}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.05em}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    overlayColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    ctaTypography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"

## Components

**button-primary** — The default call-to-action ("Shop now" links on the homepage collection banners). Uses the inferred primary blue as fill with white text set in the Montserrat accent family; square corners are proposed to match the zero-radius default seen in the Shopify accelerated-checkout button CSS. Hover/active states are not observed and are proposed as a modest darken.

**button-secondary** — An outlined variant for lower-emphasis actions (e.g., "Continue Shopping" in cart drawer). Transparent background, primary-colored border and text; proposed fill-on-hover state not confirmed from evidence.

**text-input** — Search and cart-note fields. Thin hairline border, white background, body serif typography at 14px matching the observed `--font--paragraph--size`. Focus ring color is proposed, not observed.

**nav-bar** — Top navigation housing Shop, About, Studio, FAQ, Contact, Journal, Registry, Account, and Cart entries per the page text. Rendered in the accent (Montserrat) family for menu labels, white background, bottom hairline separator; sticky/collapse behavior is proposed, not measured.

**product-card** — Grid tile for items under Vases, Bowls, Plates, Cups & Mugs, Kitchen & Serving, and Dinner Sets. Off-white card surface, serif product title, smaller serif price line; a thin hairline can separate card from grid background. Hover image-swap is a common pattern for this platform but is not confirmed here.

**hero** — Full-width banner used for "New from the Studio," "A Contemporary Classic," and similar homepage collection intros. Warm off-white background, large serif display headline, serif supporting copy, and a button-primary CTA. Copy hierarchy is inferred from the page-text excerpt order, not from measured layout.

**footer** — Dark ink-colored band carrying copyright ("© 2026 Sheldon Ceramics"), Studio/Search/Gift Card/Journal/FAQ links, and a newsletter subscribe confirmation. Muted-gray link color on dark ink background is proposed for sufficient contrast; exact link states not observed.

**badge** — Small pill label proposed for tagging "New Arrivals" or collection names (e.g., Terra Cotta) on product cards or tiles, using the terracotta accent pulled from the observed palette to echo that collection's naming.

**collection-tile** — Category-appropriate component for the "By Collection" set (Farmhouse, Silverlake, Vermont, Terra Cotta, Indigo, Stoneware). Image-backed tile with a serif title overlay and Montserrat CTA label; overlay scrim color is proposed using ink at reduced opacity, not directly observed in the supplied rules.

## Responsive Behavior

This is a proposed responsive recommendation, not a measured observation of the live site's mobile/tablet layout.

| Breakpoint | Width       | Nav                          | Grid                     |
|-----------|-------------|-------------------------------|---------------------------|
| mobile    | <600px      | Collapsed hamburger menu      | 1-column product grid     |
| tablet    | 600–1024px  | Condensed inline menu         | 2-column product grid     |
| desktop   | >1024px     | Full horizontal nav w/ dropdowns | 3–4 column product grid |

Touch targets should be at least 44×44px for cart, search, and nav-toggle controls. The mega-menu structure implied by the repeated "Shop / By Type / By Collection" text blocks suggests a slide-in mobile drawer with back navigation, consistent with the "Back" labels present in the page text, but the actual interaction mechanics were not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS custom properties, a handful of component rules, and a page-text excerpt; no rendered screenshots or DOM layout were available.
- The mapping of blue hover colors (#51a7ca, #56b8d6, #2e629d) to a single "primary" brand color is inferred from wishlist/registry hover rules only; the true primary brand accent may differ.
- Font stack includes several fallback/system fonts (Arial, Helvetica, Lucida Grande, monospace) and named commercial fonts (minion-pro-display, proxima-nova, blockshop-icons) present in the raw font list but not confirmed as in-use body/heading fonts; only "Crimson Text" and "Montserrat" are tied to active `--font--*` variables and are used here.
- All spacing and corner-radius scales are proposed conventions for a craft/e-commerce interface, not measured from the site's actual CSS box model.
- Hover, focus, active, disabled, and error states for buttons, inputs, and cards are proposed patterns; only wishlist/registry hover colors and Shopify's generic accelerated-checkout button hover were present in evidence.
- Mobile menu, search overlay, and cart-drawer interaction behavior were not observed and are described only as conventional proposals.
- Font licensing/availability for "Crimson Text" and "Montserrat" was not verified beyond their declaration in CSS custom properties.
