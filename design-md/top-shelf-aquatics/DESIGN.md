---
version: alpha
name: "Top Shelf Aquatics"
source_url: "https://topshelfaquatics.com"
captured_at: "2026-09-28T09:04:13.618792+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Top Shelf Aquatics is a saltwater-reef ecommerce storefront (corals, fish, inverts,
  equipment) built on a Shopify theme with a deep-navy brand identity. The observed
  palette centers on a near-black navy (#001935 and its alpha/deep variants like
  #0b2347, #061a3a) used for the sticky header, body text, and glass-style border
  effects, paired with a cool white/pale-blue canvas (#ffffff, #f2f6fc, #e6ecf5) for
  content areas. A saturated blue (#1a66d2, with lighter reef tones #5aa9ff, #4f9cff,
  #3b82f6) appears in the announcement-bar gradient and is inferred here as the
  interactive/link accent, evoking reef water. Warm oranges (#ff721a, #e85f0a,
  #c24d00) and a gold (#ffc63b) recur across the sale-percentage swatches and are
  inferred as promotional/badge accents, while a deep red family (#a81a26, #760d16,
  #8a131e) is inferred as a clearance/urgent-sale accent distinct from the general
  orange promo tone. Typography is limited to the observed Barlow and Barlow Semi
  Condensed families; this spec assigns the semi-condensed cut to display/nav/button
  text (a common pairing for dense retail category menus) and standard Barlow to
  body copy, both with generic sans-serif fallback. Radii, spacing, and most sizes
  are proposed conventions, not measured values, since no live rendering was
  captured.

colors:
  primary: "#001935"
  ink: "#001935"
  canvas: "#ffffff"
  body: "#001935"
  muted: "#0b2347"
  hairline: "#00193514"
  surface-soft: "#f2f6fc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1a66d2"
  accent-blue-light: "#5aa9ff"
  accent-orange: "#ff721a"
  accent-orange-deep: "#c24d00"
  accent-gold: "#ffc63b"
  accent-red: "#a81a26"
  accent-red-deep: "#760d16"
  surface-alt: "#e6ecf5"
  border-soft: "#eeeeee"
  overlay-navy: "#0019352e"
typography:
  display-xl: {fontFamily: "Barlow Semi Condensed, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow Semi Condensed, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow Semi Condensed, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Barlow Semi Condensed, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.overlay-navy}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  wysiwyg-tag:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary**: Solid navy fill with white text, used for primary calls to action such as "Add to Cart" or "Shop Coral." Rounded corners are proposed at a small radius; hover/active states (lift or scale) are proposed but not confirmed, though the CSS does define generic `--hover-lift-amount` and `--hover-scale-amount` custom properties suggesting some hover motion exists site-wide.

**button-secondary**: An outlined variant using the same navy on a white ground, intended for lower-emphasis actions like "View All" links seen adjacent to sale sections. Border and text share the primary navy; fill stays transparent/white.

**text-input**: A bordered field using a hairline navy-alpha border and white card background, proposed for search, email capture, and account forms. No live focus-state styling was observed, so focus ring treatment is left undefined.

**nav-bar**: Represents the sticky, glass-effect header confirmed in evidence (`position: sticky/fixed`, navy background `#001935`, layered inset/outset box-shadows referencing reef-light and glass-highlight custom properties). Given the deep multi-level category list (Live Sale, Aquarium Supplies, Live Corals, Saltwater Fish, Inverts, More), the nav is treated as a mega-menu trigger bar; the disclosed backdrop-blur drawer surface (`--kith-menu-drawer-surface`, `backdrop-filter: blur(40px)`) is proposed as the dropdown panel style.

**product-card**: A white card with a light hairline border, used for coral/fish/equipment listings. It carries a title in the condensed display face and a price row; the sale content (e.g., "70% OFF," strikethrough regular price) implies a two-line price block, which is proposed since exact markup wasn't inspected.

**hero**: A full-width navy band with large condensed display type, proposed for homepage banner copy such as the "one stop shop for everything Saltwater Reef tank related" messaging. Text color is inverted to white for contrast against the dark fill.

**footer**: Matches the navy header tone for brand consistency, set in smaller body type, proposed to house newsletter signup, category shortcuts, and legal links; no footer-specific selectors were supplied so structure is inferred from typical ecommerce footers.

**badge**: A pill-shaped label in the deep red accent, proposed for clearance/sale percentage markers ("70% OFF," "64% OFF") distinct from the orange promotional gradient tones also present in the palette; red is chosen for higher urgency signaling.

**search**: A rounded, soft-background field proposed for the header search affordance; not explicitly present in supplied CSS but standard for a 1500+ SKU catalog site with this navigation depth.

**wysiwyg-tag**: A category-specific accent label in the announcement-bar blue, proposed to flag "WYSIWYG Corals" and "WYSIWYG Fish" listings — a livestock-industry convention meaning the photographed specimen is the exact item shipped, distinct from stock-photo listings.

## Responsive Behavior

| Breakpoint | Width        | Layout intent (proposed)                          |
|------------|--------------|----------------------------------------------------|
| sm         | 0–599px      | Single-column product grid, collapsed hamburger nav |
| md         | 600–899px    | 2-column product grid, condensed nav labels         |
| lg         | 900–1199px   | 3–4 column product grid, full mega-menu on hover    |
| xl         | 1200px+      | 4–5 column grid, persistent sticky header confirmed |

Touch targets are recommended at a minimum 44×44px for cart, account, and menu-toggle icons, consistent with the confirmed sticky header's icon-centered flex buttons (`.account-button`). The multi-level category structure (Live Corals → SPS/LPS/Zoanthids/etc.) should collapse into an accordion drawer below `md`; the observed `--kith-drawer-top`, `--kith-drawer-content-padding-*` variables confirm a slide-in drawer pattern exists, but its exact mobile breakpoint trigger was not measured. This table is a recommendation only, not observed responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This is a static CSS/text extraction; no live browser rendering, computed layout, or JavaScript-driven interaction was observed, so actual hover/focus/active states are proposed, not verified.
- Semantic role assignments (e.g., which navy variant is "muted" vs. "ink," which orange/red is "sale" vs. "clearance") are inferred from repetition patterns in the palette, not from confirmed component-to-color mappings.
- All font sizes, weights, letter-spacing, and line-heights are proposed conventions; only the two font-family names (Barlow, Barlow Semi Condensed) were directly observed in evidence.
- Border-radius and spacing scales are conventional proposals, not extracted from measured CSS box-model values.
- Mobile menu/drawer visuals (blur, gradient surface) are confirmed by CSS variables but their triggering breakpoint and final rendered appearance were not observed.
- Licensing and self-hosting/availability of the Barlow font family were not verified in this evidence set.
