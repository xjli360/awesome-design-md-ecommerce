---
version: alpha
name: "Lowepro"
source_url: "https://lowepro.com"
captured_at: "2026-09-28T05:05:18.939324+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lowepro's stylesheet exposes a Bootstrap-derived variable system layered with a
  custom brand palette. The primary accent is a saturated safety orange
  (#f8971d), paired with a near-black body ink (#252525) and a secondary
  charcoal (#3a3a3a) used for dark-mode text and Bootstrap's "dark" role. Body
  copy sits on a pure white canvas (#fff) with a soft off-white (#fafafa) used
  for Bootstrap's "light" surfaces — inferred here as card and section
  backgrounds since no dedicated surface token was observed. Status colors
  (success #009688 teal-green, danger #dc3545 red, warning #ffc107 amber, info
  #17a2b8 cyan) follow standard Bootstrap semantics and are retained for
  form/alert states. A distinct sustainability green (#38923a) appears as a
  bespoke utility class, suggesting an eco/product-responsibility badge use,
  which is inferred rather than confirmed by layout.

  Typography is anchored on "Gilroy" as the declared sans-serif stack, falling
  back through system UI fonts (-apple-system, Segoe UI, Roboto, Helvetica
  Neue, Arial). Base body text is 16px/1.5 at weight 400; headings inherit
  color and use weight 500 with tight 1.2 line-height — both confirmed CSS
  rules. Additional families (Open Sans, Karla-Bold, verveine, luma-icons) were
  detected in the font list but their applied selectors were not evidenced, so
  their usage here (secondary UI text, icon glyphs) is proposed and marked
  inferred. Rounding, spacing, and component states below extend the observed
  tokens into a coherent, camera-bag-retail-appropriate system.

colors:
  primary: "#f8971d"
  primary-hover: "#db7d07"
  ink: "#252525"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#6e6e6e"
  hairline: "#e0e0e0"
  surface-soft: "#fafafa"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  secondary: "#6e6e6e"
  secondary-hover: "#555454"
  success: "#009688"
  danger: "#dc3545"
  warning: "#ffc107"
  info: "#17a2b8"
  dark: "#3a3a3a"
  sustainability: "#38923a"
  border-light: "#d1d1d1"
  text-faint: "#999999"
typography:
  display-xl: {fontFamily: "Gilroy, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gilroy, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gilroy, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Gilroy, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Gilroy, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Gilroy, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Gilroy, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.secondary}"
    borderColor: "{colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.secondary-hover}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottomColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.text-faint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sustainability}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  region-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary** uses the confirmed `--primary` orange with a documented hover shift to `#db7d07` (an observed `:hover/:focus` rule), giving the CTA a clear pressed state. Text color and rounding are proposed, matching general Bootstrap button conventions implied by the variable set.

**button-secondary** is a proposed outline treatment using the observed `--secondary` gray and its hover value `#555454`, intended for lower-priority actions like "Compare" or "Add to Wishlist" on product pages.

**text-input** takes its neutral border (`#d1d1d1`, inferred from the palette's light grays) and focuses to the primary orange, a common accessible-focus pattern; exact border-radius and padding are proposed, not measured.

**nav-bar** is proposed as a white bar with a light hairline divider (`#e0e0e0`), sized for the site's stated navigation categories (bags, backpacks, cases); no live header layout was captured in evidence.

**product-card** anticipates the grid used for "Shop for Lowepro camera bags..." listings; background uses a light card gray (`#f1f1f1`) distinguished from pure white canvas, with hairline borders — this hierarchy is inferred, not observed in markup.

**hero** is proposed for the homepage banner referenced by the page's marketing copy ("Shop now and receive free shipping"), using the dark charcoal background for contrast against orange CTA buttons.

**footer** mirrors the dark surface convention and uses faint gray text links (`#999999`) against `--dark`, matching typical Bootstrap dark-footer patterns; not confirmed from footer-specific CSS.

**badge** repurposes the bespoke `--sustainability` green class, likely for eco-material product callouts (e.g., recycled fabric labeling), a reasonable but unverified interpretation of that unique token's presence.

**search** and **region-selector** are proposed utility components: the region-selector directly reflects the page-text evidence of a country/language chooser ("Choose your language... United States Canada... Japan China"), styled with neutral borders and small body typography.

## Responsive Behavior

Recommended breakpoints (not measured, proposed only), loosely aligned with the `--breakpoint-*` custom properties found in the stylesheet:

| Token | Width  | Notes (proposed) |
|-------|--------|-------------------|
| xs    | 0      | Single-column stacking, full-width buttons |
| sm    | 576px  | Two-column product grids begin |
| md    | 768px  | Nav collapses to horizontal bar, filters inline |
| lg    | 992px  | Three/four-column product grids |
| xlg   | 1024px | Site-specific breakpoint per `--breakpoint-xlg`; likely tablet-to-desktop nav switch |
| xl    | 1200px | Max-width content container |
| xxl   | 1980px | Wide-desktop gutters increase |

Touch targets should be at least 44×44px for primary buttons and nav items on mobile. The nav-bar and region-selector should collapse into a hamburger/menu drawer below `md`, per common e-commerce convention — not a confirmed behavior of this site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All values are derived from static CSS extraction of one stylesheet plus page text; no rendered layout, DOM structure, or interaction states (hover/focus/active beyond documented `:hover` rules) were observed.
- Semantic role assignments (e.g., which gray is "muted" vs. "hairline," which light gray is "surface-card") are inferred from Bootstrap variable naming conventions, not confirmed visual hierarchy.
- Component definitions (hero, product-card, footer, nav-bar, search, region-selector) are proposed patterns appropriate to a camera-bag e-commerce site; their existence, exact markup, and precise measurements were not verified against live page renders.
- Typography sizes beyond the confirmed 16px/1.5/400 body rule and 0.5rem heading margin are proposed estimates, not measured values.
- "Gilroy" is a commercial font; its licensing and actual delivery (webfont vs. fallback rendering) were not verified. "Karla-Bold," "verveine," and "luma-icons" appeared in the font list but no selector evidence for their application was supplied, so their roles are unconfirmed and excluded from the typography scale except as a noted possibility.
- Spacing and rounding scales are proposed conventions, not extracted from measured box models.
