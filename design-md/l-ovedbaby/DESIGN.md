---
version: alpha
name: "L'ovedbaby"
source_url: "https://lovedbaby.com"
captured_at: "2026-09-28T09:07:09.943313+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  L'ovedbaby is a Shopify-based storefront (Prestige-family theme, evidenced by
  --colorBtnPrimary custom properties, flickity carousels, and hotspot modules)
  selling GOTS-certified organic baby and toddler clothing. The observed palette
  centers on a deep maroon/brick red (#831d27) used for header navigation
  accents, paired with a dusty rose (#a66464) for bold nav labels and a muted
  mauve (#a8777a) for star ratings — together these read as a warm, natural,
  slightly vintage accent family appropriate to an organic-cotton nursery brand.
  Neutrals dominate the rest of the system: near-black inks (#212427, #1c1d1d,
  #333333) for text, and a wide range of off-white/gray surfaces (#f8f5f5,
  #f6f6f6, #fafafa, #e7e5e4, #dddddd) for cards, testimonial blocks, and
  section backgrounds. A GOTS-green accent (#009639) appears on a specific nav
  item, inferred here as an "eco/organic" signal color. Payment-network icon
  colors (Visa blue, Mastercard red/orange, PayPal blue) were present in the
  raw palette but are excluded from brand roles as they belong to third-party
  checkout badges, not brand identity.

  Typography is inferred from two observed families: Lora (serif) is proposed
  for display/heading roles, and Source Sans Pro (sans-serif) for body and UI
  text, consistent with a soft-but-legible nursery-brand pairing. No font
  sizes, weights, or breakpoints were present in the supplied CSS beyond a
  22px grid gutter and 30px drawer gutter; all typographic scale, radii usage,
  and spacing values below are proposed defaults, not measured observations.

colors:
  primary: "#831d27"
  ink: "#212427"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f8f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-rose: "#a66464"
  accent-mauve: "#a8777a"
  accent-green: "#009639"
  accent-sale: "#d02e2e"
  border-strong: "#b6b6b6"
  text-secondary: "#505050"
  overlay-scrim: "#0000004d"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Lora, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Lora, serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Source Sans Pro, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Source Sans Pro, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Source Sans Pro, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Source Sans Pro, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentText: "{colors.primary}"
    boldAccentText: "{colors.accent-rose}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    controlBackground: "{colors.canvas}"
    controlShadow: "0 5px 5px #0000001a"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-mauve}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    iconColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  certification-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-green}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** maps to the theme's `--colorBtnPrimary` custom property, observed driving both the flickity carousel arrows and the "new" product tag badge; the maroon `{colors.primary}` fill is a proposed brand assignment for this role, inferred from its repeated use in header navigation accents.

**button-secondary** is proposed as an outlined counterpart, using the observed `.btn--secondary { text-decoration-color: #222222 }` rule as partial evidence of a secondary/underline treatment; fill and border values are inferred defaults, not directly observed.

**text-input** is a proposed pattern for search and form fields; no input-specific CSS was supplied, so colors and radius are inferred from the neutral hairline/canvas palette rather than measured.

**nav-bar** reflects observed multi-level site navigation with per-item color overrides (`#831d27` for one dropdown summary, `#a66464` bold for toolbar links, `#009639` for a specific nav item, inferred as an eco/organic-themed category). Dropdown and mobile-drawer states are proposed, not confirmed interactive.

**product-card** is inferred from `.grid-product__tag` evidence (a "new" badge using the primary button color); overall card surface, border, and padding are proposed defaults typical of Shopify grid-product templates, not directly measured.

**hero** is grounded in `.hero .flickity-button` rules showing a light control background (`--colorBody`) with a soft `0 5px 5px #0000001a` shadow over the hero image/slider; hero copy scale and padding are proposed.

**footer** composition (dark background, light text, accent links) is proposed; no footer-specific selectors were supplied, so this pattern is inferred from the observed dark neutrals and social/utility link list in the page text (Rewards, App, Registry, Blog, Support).

**badge** generalizes the observed `.grid-product__tag--new` treatment (primary-colored background, on-primary text) into a reusable sale/new/limited badge component.

**search** is a proposed overlay pattern inferred from the presence of "icon-search" in navigation markup; no search-panel CSS was supplied.

**certification-badge** is a category-appropriate, proposed component reflecting the repeated marquee copy "GOTS-CERTIFIED ORGANIC COTTON / NO BAMBOO OR SEMI-SYNTHETICS," using the observed green (`#009639`) as a trust/certification signal color against a soft neutral background.

## Responsive Behavior

Recommended breakpoints (not measured from the site): mobile up to 749px, tablet 750–999px, desktop 1000px+. Below 750px, the multi-level `.site-nav` is expected to collapse into the observed `#NavDrawer .mobile-nav` drawer pattern (evidenced by matching mobile-nav selectors mirroring desktop nav color rules), with the hamburger and cart icons remaining in a fixed top bar. Touch targets for nav items, buttons, and badges should be at least 44×44px. Hero carousel controls (`.flickity-button`) should scale down and remain thumb-reachable near the image edges on mobile. This section is a recommendation based on theme conventions, not observed responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, computed breakpoints, hover/focus/active states, or real interaction behavior were observed. Color-to-role mapping (e.g., which maroon is "primary" vs. incidental) is inferred from selector context, not confirmed brand guidelines. Payment-network icon colors present in the raw palette (Visa blue #0071ce, Mastercard red/orange #eb001b/#f79e1b, PayPal blues #142fbd/#1532cb) were deliberately excluded from brand roles. Two border-radius values (10px, 20px) appear only on a third-party "appbrew" app-download widget and are not folded into the core `rounded` scale. All typography sizes, weights, and letter-spacing are proposed, as only font-family names (Lora, Source Sans Pro) were present in evidence — no font-size or weight declarations were supplied. Licensing/self-hosting status of Lora and Source Sans Pro was not verified from the evidence provided. Spacing scale beyond the observed 22px grid-gutter and 30px drawer-gutter is proposed convention, not measured.
