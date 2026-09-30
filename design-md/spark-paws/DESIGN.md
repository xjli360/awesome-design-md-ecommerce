---
version: alpha
name: "Spark Paws"
source_url: "https://sparkpaws.com"
captured_at: "2026-09-28T09:03:48.625409+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Spark Paws is a Shopify-built DTC pet-apparel storefront selling dog hoodies,
  raincoats, harnesses, shoes, and matching human/dog outfits. The extracted CSS
  shows a restrained, utilitarian palette: a dark navy (#344d79) used as the
  primary call-to-action fill on product collection buttons, near-black grays
  (#1c1b1b, #363636, #383a3d) for headings and body copy, and light neutrals
  (#f1f1f1, #f9f9f9, #e7e7e7) for card and section surfaces. A single warm gold
  (#EBBF20) is confirmed as the star-rating icon color and is treated here as
  the brand's accent for badges and highlights. Two blues (#1990c6 / #136f99)
  come from Shopify's accelerated-checkout button default/hover states rather
  than brand-authored CSS, so they are mapped conservatively as a secondary
  "link" role. Several bright reds/oranges/blues in the raw palette (e.g.
  #eb001b, #ff5f00, #1532cb, #00aced) are payment/social-network brand marks,
  not Spark Paws design tokens, and are intentionally excluded.
  Typography is system-first: an explicit stack led by "system_ui" with
  standard OS fallbacks is confirmed for section headings (20px) and
  sub-headings (14px). "Jost" appears in the site's font-family evidence but
  no selector confirming its applied role was captured, so its use in the
  display scale below is inferred, not verified. Layout components (nav,
  product cards, collection tiles) are proposed interpretations consistent
  with the catalog/collection copy, not measured DOM structure.

colors:
  primary: "#344d79"
  on-primary: "#ffffff"
  ink: "#1c1b1b"
  ink-secondary: "#363636"
  body: "#383a3d"
  muted: "#5c5c5c"
  hairline: "#e7e7e7"
  surface-soft: "#f9f9f9"
  surface-card: "#f1f1f1"
  canvas: "#ffffff"
  accent-gold: "#ebbf20"
  link-blue: "#1990c6"
  link-blue-hover: "#136f99"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "'Jost', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Jost', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "system_ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    textColor: "{colors.ink-secondary}"
    borderColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    sticky: true
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    badgeColor: "{colors.accent-gold}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    ctaComponent: "button-secondary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    linkColor: "{colors.link-blue}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    overlayTextColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    ctaColor: "{colors.primary}"
    ctaTypography: "{typography.button-md}"

## Components

**button-primary** renders the dark-navy fill confirmed on `.ProductCollectionListItem__Link.Button` (background `#344d79`, white text, ~12px label). It is the primary "Shop Collection" / add-to-cart action across the catalog grid.

**button-secondary** mirrors the confirmed `.Button` / `.Button::before` pair (white fill, dark-gray `#363636` text, white border), likely used as an inverted CTA over hero imagery. Hover/active states were not captured and are proposed.

**text-input** is a proposed pattern for the newsletter/search fields; no direct border or focus-state CSS was present in the evidence, so styling follows the observed hairline gray and canvas white.

**nav-bar** reflects the confirmed sticky-header custom properties (`--use-sticky-header: 1`) with a white background and dark body-gray text; exact height, logo placement, and mobile menu markup were not observed.

**product-card** is inferred from the repeated product-grid text (title, strikethrough price, "new" label) seen throughout the page excerpt. Hairline border and light padding are proposed to separate cards on a white canvas.

**hero** is a proposed full-bleed banner pattern (e.g., "Customer Faves," "Fall Wear New") using a dark overlay with the white inverted `button-secondary` as its CTA, consistent with the light-on-dark button rule found in the CSS.

**footer** uses the light `surface-card` gray and the confirmed checkout-blue as a link color for the long list of support/info links ("FAQ," "Wholesale," "Track Orders") visible in the page text.

**badge** applies the one fully confirmed accent, `#EBBF20` (the `--lxs-rating-icon-color` token), to small pill labels; its use for "New" product tags beyond star ratings is inferred, not verified.

**collection-tile** is the category-appropriate component for the "Shop By Collection" section (Dog Apparel, Collar & Harness, Summer Cooling, Matching Sets, etc.), proposed as a soft-surface card with a primary-colored text CTA.

## Responsive Behavior

Recommended breakpoints (not measured from the live site):

| Breakpoint | Width      | Notes                                  |
|-----------|------------|-----------------------------------------|
| mobile    | 0–599px    | Single-column product grid, collapsed nav |
| tablet    | 600–959px  | 2-column product grid                   |
| desktop   | 960–1279px | 3–4 column product grid                 |
| wide      | 1280px+    | 4+ column grid, max-width container     |

Touch targets should be at least 44×44px for buttons and nav items. The nav bar is expected to collapse into a hamburger/drawer pattern below tablet width, consistent with the sticky-header flag observed but not with any captured mobile markup. This table is a design recommendation, not an observation of actual responsive CSS or breakpoints on sparkpaws.com.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically from rendered CSS/text; no DOM screenshots, computed layout, or interaction states (hover, focus, open menu, cart drawer) were observed.
- `#1990c6` / `#136f99` originate from Shopify's default accelerated-checkout button styling, not brand-authored CSS, and are mapped as a secondary "link" role with low confidence.
- Several palette entries (`#eb001b`, `#f79e1b`, `#ff5f00`, `#1532cb`, `#142fbd`, `#00aced`, `#0071ce`, `#005fcc`, `#66b3ff`) match known payment-network and social-icon brand colors and were excluded from semantic tokens as not representative of Spark Paws' own design system.
- "Jost" is present in the font-family evidence but no rule tying it to a specific selector/role was captured; its use in `display-xl`/`display-md` is inferred and its license/availability is unverified.
- Component padding, radii, and grid structure (product-card, hero, nav-bar, search) are proposed defaults grounded in typical Shopify theme patterns, not measured from this site's stylesheet.
- Mobile navigation, filtering UI, and size/color selector interactions referenced in the page text (e.g., matching dog/owner sizes) were not present in the supplied CSS and are not specified here.
