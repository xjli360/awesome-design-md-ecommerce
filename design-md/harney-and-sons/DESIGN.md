---
version: alpha
name: "Harney & Sons"
source_url: "https://harney.com"
captured_at: "2026-09-28T09:45:39.026256+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in Harney & Sons' Shopify-rendered storefront CSS, where a warm antique-gold (#c6a95a) drives primary buttons, paired with near-black text (#111111) for contrast — an inferred "old-world tea merchant" palette rather than a confirmed brand guideline. Cream and off-white tones (#fffcf5, #fafafa, #f5f5f5) suggest a soft, paper-like canvas appropriate to a heritage tea purveyor, while a muted olive-gold hover state (#b0913d) and a deeper bronze (#8a722f) provide secondary emphasis. A thin neutral hairline (#d9dbdc) matches the observed sticky-header border token. Typography is anchored by Cardo, a serif observed directly in the CSS, used here for display and heading roles to evoke tradition and craft; sans-serif is reserved for body copy and UI labels since a specific sans family was not named in evidence, only the generic fallback. Heading scale (12–56px+) is taken from the site's own custom-property tokens across breakpoints. Buttons, forms, and spacing follow the measured --button-height (52px) and --form-input-field-height (52px) tokens. Rounded corners, several spacing values, and some component states (hover, focus, mobile nav collapse) are proposed conventions, not confirmed from the supplied evidence, and are labeled accordingly throughout.

colors:
  primary: "#c6a95a"
  primary-hover: "#b0913d"
  ink: "#111111"
  canvas: "#fffcf5"
  body: "#333333"
  muted: "#8a722f"
  hairline: "#d9dbdc"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#111111"
  accent-olive: "#8fa53c"
  accent-green: "#2f7361"
  accent-terracotta: "#95340c"
  accent-gold-light: "#f8de7e"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Cardo, serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Cardo, serif", fontSize: 38px, fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Cardo, serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.75px"}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
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
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  tea-type-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** reflects the directly observed `.dsgn-pck__button-primary` rule (background `#c6a95a`, text `#111111`, hover `#b0913d`) and is scaled to the measured `--button-height: 52px` token; used for "Shop Now," "Take the Quiz," and cart actions.

**button-secondary** is a proposed outline variant sharing the same gold border and hover behavior as the primary button but with a transparent fill, intended for lower-emphasis actions like "View Collection."

**text-input** uses the observed `--form-input-field-height: 52px` for sizing; background, border, and radius are proposed conventions since no explicit input styling was supplied.

**nav-bar** is grounded in the observed sticky header tokens (`--header-background: 255,255,255`, `--header-border-color: 217,217,217`, `--enable-sticky-header: 1`), rendered here as a white bar with a light hairline bottom border; dropdown/mega-menu visuals are proposed, not confirmed.

**product-card** is inferred for the extensive tea-type and collection grids (White, Green, Matcha, etc.) referenced in navigation; card chrome, border, and radius are proposed since no card-specific CSS was supplied.

**hero** models the homepage's "Make Tea Your Everyday Luxury" banner area, using the largest observed heading token (`--heading-large-font-size: 64px` desktop) for display text; background and padding are proposed.

**footer** is inferred from the site's dense link/legal footer content (Service, About, Contact) with a dark ink background and gold link accents; exact footer colors were not directly supplied and are proposed.

**badge** is a proposed pattern for promotional flags like "Sale" or "New Arrivals," using the terracotta accent (`#95340c`) observed in the broader palette for warmth and contrast against gold.

**search** is inferred for the header's "View all results" search affordance; pill shape and soft background are proposed, not measured.

**tea-type-filter-pill** is a category-specific proposed component for the extensive Tea Type filter list (Matcha, White, Green, Oolong, Black, etc.), using the caption typography token and full rounding to suggest a scannable filter row.

## Responsive Behavior
Recommended breakpoints (not measured from live site): mobile <640px, tablet 640–1024px, desktop >1024px. The `:root` token sets (52px→64px large heading; 64px→90px vertical breather) suggest at least two responsive tiers already exist in the source CSS, likely tablet and desktop. Proposed guidance: collapse the mega-menu navigation into a slide-out drawer below 1024px; stack hero text above imagery below 640px; maintain a minimum 44px touch target for nav links and filter pills; product grids should reflow from multi-column to 2-column (tablet) to single-column (mobile). These are recommendations for implementation, not observed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, a limited rule sample, and page text — no live rendering, computed styles, or JavaScript-driven states were observed. Component states such as hover, focus, active, and disabled are proposed except where explicitly present in evidence (button-primary hover). Mobile navigation, menu collapse behavior, and touch interactions were not observed and are inferred conventions only. Body font family is not explicitly named in evidence beyond the generic "sans-serif" fallback; Cardo's availability, licensing, and hosting method were not verified. Several color-to-role mappings (footer background, badge, search) are inferred from general palette availability rather than confirmed selectors. Spacing scale beyond the measured 52px control heights and 64–90px vertical breathers is proposed for consistency, not extracted from source.
