---
version: alpha
name: "Craft and Lore"
source_url: "https://craftandlore.com"
captured_at: "2026-09-28T09:50:53.863724+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Craft and Lore presents itself as a small-batch North Idaho leather workshop,
  and the observed CSS supports a heritage-workshop tone: warm neutrals,
  saddle-orange accents, and dark charcoal surfaces rather than a bright
  retail palette. The clearest evidence is the AI product-feature block,
  which pairs a near-black brown background (#282520) with warm tan text
  (#dbd1be, #cfbb99) and a burnt-orange call-to-action (#e68819, hover
  #d67a15) with a 4px border-radius. Dynamic collection buttons reuse a
  darker rust (#b1660d) and a neutral charcoal (#494949) as alternate
  backgrounds, suggesting a small rotating accent set rather than a single
  fixed brand color. Header overlay logic (#222222 transparent-to-solid)
  indicates a dark, image-forward hero pattern typical of Shopify craft
  brands. Fonts mix a condensed display face (Francois One) with a plainer
  sans (Funnel Sans) and a condensed utility face (Open Sans Condensed) for
  labels/buttons; Crimson Text and Futura also appear but their roles are
  unconfirmed. This interpretation assigns semantic roles (ink, canvas,
  muted, hairline) to plausible but inferred neutrals from the palette,
  since no layout screenshot was supplied. All colors are reused from the
  observed set; no new hues were introduced.

colors:
  primary: "#e68819"
  primary-hover: "#d67a15"
  accent-warm: "#b1660d"
  secondary: "#494949"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  surface-dark: "#282520"
  text-on-dark: "#dbd1be"
  text-on-dark-muted: "#cfbb99"
  success: "#28a745"
  danger: "#dc3545"
typography:
  display-xl: {fontFamily: "Francois One, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Francois One, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Funnel Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Funnel Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Funnel Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans Condensed, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Open Sans Condensed, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    hoverBackgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.accent-warm}"
    borderColor: "{colors.accent-warm}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.text-on-dark}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.lg}"
    hairlineColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.accent-warm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.text-on-dark}"
    overlayColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.text-on-dark-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairlineColor: "#2f2d27"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  announcement-bar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.text-on-dark}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** — Maps directly to the observed `.ai-product-features__button` rule: orange fill (#e68819), white text, 4px radius, and a darker hover state (#d67a15). Proposed as the main add-to-cart / shop CTA.

**button-secondary** — Not directly observed; inferred as an outline variant using the rust accent (#b1660d) seen on collection link buttons, for lower-emphasis actions like "View all" or "Learn More +."

**text-input** — No form CSS was supplied; padding, radius, and border are proposed defaults consistent with the hairline and canvas tokens, intended for newsletter signup and search fields referenced in the page text.

**nav-bar** — Based on the `--header-overlay-background-color: #222222` variable and force-hover rule that solidifies the header on scroll/interaction. Proposed as a dark, transparent-to-solid bar over hero imagery.

**product-card** — Combines the observed light placeholder background (#f4f4f4/#f8f8f8), title font-size 20px, and price color (#cfbb99 on dark, remapped to accent-warm on light cards) drawn from the product-features block styling.

**hero** — Proposed pattern for the "SHOP WALLETS / WATCH STRAPS" promotional sections, using the dark surface (#282520) and tan text seen in the feature block as a stand-in for a full-bleed image hero; not confirmed as the literal homepage hero styling.

**footer** — Inferred dark, near-black footer (#111111/#0c0b09 family) with muted tan body text, consistent with the site's heritage/workshop tone; exact footer CSS was not supplied.

**badge** — Proposed pill component for labels like "NEW," "Sale," or "Limited Run" seen in the product text, using the accent-warm fill and full rounding.

**search** — Proposed light overlay panel triggered by the "Search" nav item; styling inferred from the general light surface tokens since no search-modal CSS was captured.

**announcement-bar** — Directly motivated by the "Don't miss today's offers!" and "Free shipping on USA domestic orders over $150" strings in the page text; styled with the secondary charcoal (#494949) and tan text for a persistent top banner.

## Responsive Behavior

This is a recommendation, not measured site behavior — no viewport-specific CSS was supplied.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed nav behind a hamburger menu, announcement bar truncates to one line. |
| Tablet | 600–1024px | Two-column product grid, nav condenses to icon + label. |
| Desktop | >1024px | Full horizontal nav with mega-menu-style category flyouts (Wallets, Belts, Accessories, Watch Straps, Shell Cordovan). |

Touch targets should be at least 44×44px for cart/menu icons. Nav collapse and mega-menu disclosure are proposed patterns consistent with the listed category structure, not confirmed interaction states.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static CSS/text only; no rendered screenshots, so actual layout, grid structure, and spacing between sections are inferred, not observed.
- Font role assignments (Francois One as display, Funnel Sans as body, Open Sans Condensed as caption/button) are inferred from naming convention and available evidence; Crimson Text and Futura appear in the font list but their usage context is unconfirmed.
- Several color roles (ink, body, hairline, surface-card) are inferred neutrals selected from the observed palette rather than confirmed via a labeled CSS rule.
- Spacing values for hero/section padding are approximated to the proposed scale; the one directly observed padding (`40px 20px`) does not map exactly to a single spacing token.
- No confirmed hover/focus/active states beyond the single documented button hover rule; all other interactive states are proposed.
- Mobile menu, search modal, and cart drawer behavior are not present in the supplied CSS and are marked proposed throughout.
- Custom font licensing/self-hosting was not verified; fallbacks (sans-serif, serif, monospace) should be retained in implementation.
