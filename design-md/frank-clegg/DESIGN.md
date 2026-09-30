---
version: alpha
name: "Frank Clegg"
source_url: "https://frankcleggleatherworks.com"
captured_at: "2026-09-28T09:29:25.814683+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Frank Clegg Leatherworks presents itself as a heritage American leather goods
  maker (est. 1970, Massachusetts workshop), and the extracted CSS reflects a
  restrained, utilitarian Magento theme layered under that story. The working
  UI palette is neutral: white canvas, near-black and mid-gray text (#333333,
  #111111), light gray hairlines and surfaces (#cccccc, #dddddd, #f6f6f6), and
  a single recurring brand accent, deep oxblood #9e1b2b, used for section
  headings, gallery titles, hover states on CTAs, and the "me-q-header" label.
  A soft gold (#c99947) and cream (#fdf0d5) pairing appears in the palette and
  is interpreted here as an inferred "luxury accent" surface for premium
  callouts (e.g. "Give a Little Luxury"), though its exact application was not
  directly observed in the supplied rules. Body copy uses Lato with Helvetica
  Neue/Helvetica/Arial/sans-serif fallbacks, matching the observed `body` and
  `button` rules. Georgia/serif appears in the site's font stack list; it is
  applied here only to display headings as an inferred editorial contrast to
  the sans-serif UI, consistent with the brand's "since 1970" heritage
  positioning. All interaction states (hover/focus button grays) are drawn
  directly from observed CSS.

colors:
  primary: "#9e1b2b"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7d7d7d"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-gold: "#c99947"
  surface-cream: "#fdf0d5"
  link: "#1979c3"
  badge-red: "#e02b27"
  border-default: "#cccccc"
typography:
  display-xl: {fontFamily: "Georgia, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Georgia, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4286, letterSpacing: 0px}
  body-sm: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.6, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.border-default}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-default}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  craftsmanship-badge:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-gold}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** models the oxblood-on-white hover treatment observed on `.fc-welcome-button a:hover` (background `#9e1b2b`, white text), proposed as the default filled CTA style for "Shop Now" and add-to-bag actions.

**button-secondary** is a proposed low-emphasis alternative, drawn from the observed neutral `button` rule (`background:#eee; border:1px solid #ccc; color:#333`) used for wishlist/compare actions, suitable for secondary duffel-bag filters like "Compare" or "Save."

**text-input** is a proposed field style using the observed neutral border/gray token set; no dedicated `input` rule was supplied, so padding and radius are inferred from surrounding button metrics.

**nav-bar** reflects the observed uppercase, white-on-dark account-link styling (`text-transform:uppercase; font-size:13px`) paired with the oxblood accent seen in `.me-q-header`; exact header background was not directly captured and is treated as canvas-on-white, proposed.

**product-card** is a proposed container for duffel/briefcase grid tiles, using the observed `.product-item-name>a { color:#333 }` link color and hairline borders consistent with the theme's light gray palette.

**hero** models the homepage's "Handcrafted Leather Bags" banner copy; background and headline scale are proposed, since no hero-specific selector was supplied, but text/accent colors are grounded in observed tokens.

**footer** is proposed as a dark, high-contrast band using `{colors.ink}` and white text, consistent with typical Magento theme footers; no footer-specific CSS was supplied, so this is an inferred pattern.

**badge** captures the "Free Shipping" and sale-flag styling implied by the observed `#e02b27` red in the palette, proposed for promotional or stock-status labels.

**search-overlay** reflects the observed `.inner-close.header-search-toggle { color:#999 }` icon treatment, extended into a full proposed overlay pattern for the site's search toggle.

**craftsmanship-badge** is a category-appropriate addition for a duffel-bag/leather-goods brand, surfacing "LWG certified," "guaranteed for life," and "since 1970" trust markers using the inferred gold/cream luxury accent pairing.

## Responsive Behavior
Recommended, not measured from live site behavior:

| Breakpoint | Range | Layout notes |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed nav behind menu toggle, sticky free-shipping bar reduced to one line |
| tablet | 600–1024px | 2-column product grid, nav-bar condenses to icon-only search/account/cart |
| desktop | 1024–1440px | 3–4 column product grid, full horizontal nav-bar |
| wide | >1440px | Max-width content container, larger hero imagery |

Touch targets should be at least 44×44px for cart/account/search icons; the mobile nav is expected to collapse into a hamburger menu (`x` toggle text was observed in nav markup, suggesting an existing show/hide pattern) but its exact animation and breakpoints were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from static CSS/text extraction only; no live rendering, computed styles, or DOM interaction were captured. Font-family roles for Georgia/serif are inferred from the site's stated font stack list, not from a confirmed heading selector, and their licensing/availability as web fonts is unverified. Several palette colors (e.g. `#46949a`, `#ff5501`, `#c07600`) appear in the supplied palette but had no associated selector context, so they are omitted from role assignment rather than guessed. Component states (hover/focus/disabled) beyond the explicitly supplied button rules are proposed, not observed. Breakpoints, mobile menu behavior, and hero/footer layouts are inferred conventions for a Magento-based storefront and should be validated against the live site before implementation.
