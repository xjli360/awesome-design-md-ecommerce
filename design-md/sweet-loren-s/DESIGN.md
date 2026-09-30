---
version: alpha
name: "Sweet Loren's"
source_url: "https://sweetlorens.com"
captured_at: "2026-09-28T05:02:58.602441+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sweet Loren's presents itself as a playful, better-for-you baking brand: gluten-free,
  vegan, nut-free cookie dough and refrigerated doughs sold in bold case-pack SKUs.
  The observed palette centers on a saturated magenta/pink (#e21b77, reinforced by
  darker #ac0b56 and pale #ffd7e9/#e793b7 tints) against warm off-white canvases
  (#fffcf6, #faf6e7, #f1ebe0) rather than clinical white, giving a bakery-warm,
  confection-forward feel. A deep indigo-navy (#251b57) and near-navy (#13293c)
  appear alongside near-black body copy (#3a3a3a), suggesting a two-tier text
  system: punchy pink for brand/CTA moments, navy/charcoal for readable body copy.
  Scattered brights (#00b9c4 teal, #f5ea61 yellow, #40b18f green) are treated here
  as flavor/category accent colors rather than core brand colors, since role is
  not confirmed by layout evidence.

  Typography exposes a sans body stack (Proxima Nova family, Avenir, Helvetica
  Neue fallbacks) and several unusual display names (Playfair Display, Halant,
  Caveat, The Vibes, Stash, Turbinado Dry) — consistent with a custom, whimsical
  wordmark plus a serif for editorial headings; exact weight/usage is inferred,
  not measured. The interpretation below proposes a warm-canvas, pink-forward
  system with generous rounded buttons suited to a DTC food storefront.

colors:
  primary: "#e21b77"
  primary-dark: "#ac0b56"
  primary-tint: "#ffd7e9"
  secondary-accent: "#e793b7"
  ink: "#251b57"
  ink-alt: "#13293c"
  body: "#3a3a3a"
  muted: "#737373"
  hairline: "#dedede"
  canvas: "#fffcf6"
  surface-soft: "#faf6e7"
  surface-card: "#ffffff"
  surface-cream: "#f1ebe0"
  on-primary: "#ffffff"
  accent-teal: "#00b9c4"
  accent-yellow: "#f5ea61"
  accent-green: "#40b18f"
  error: "#c31818"
typography:
  display-xl: {fontFamily: "Playfair Display, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Playfair Display, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Proxima Nova, Avenir, Helvetica Neue, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Proxima Nova, Avenir, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Proxima Nova, Avenir, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Proxima Nova, Avenir, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Proxima Nova, Avenir, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
  logo-mark: {fontFamily: "The Vibes, Caveat, cursive", fontSize: 28px, fontWeight: 400, lineHeight: 1, letterSpacing: 0px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink-alt}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-teal}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  diet-claim-badge:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink-alt}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** is the pink, fully-rounded call-to-action used for "Find in Stores," "Shop Now," and add-to-cart actions, echoing the `#e21b77` values seen repeatedly across the swatch set; hover/active states are proposed, not observed.

**button-secondary** offers an outlined variant for lower-priority actions (e.g., "Learn More") using the same primary hue as text/border on a transparent field, consistent with the site's `.btn--secondary` class present in CSS though its exact color mapping was not resolvable from static rules.

**text-input** covers newsletter/search/account fields with a plain card background, hairline border, and modest corner radius; focus-ring behavior (`outline-color:var(--color-text-link)` was observed) is proposed to use the primary pink.

**nav-bar** represents the sticky header containing the logo, mega-menu ("Shop," "Learn," "Our Story"), and cart icon; background is proposed as the warm canvas tone rather than pure white, since `--color-background-header` is a CSS variable without a resolved static value.

**product-card** models the case-pack product tiles seen in carousels (e.g., "Chocolate Chunk Cookie Dough – Case of 6"), with title, price, and swatch region (`--swatch-size:48px` was observed) for flavor variant selection.

**hero** models the homepage banner ("BAKE HAPPY. LIVE FULLY.") using the soft cream surface with large serif display type and a supporting sans-serif subhead; exact hero layout and imagery were not directly inspectable.

**footer** is proposed as a dark navy band (using `#13293c`) for contrast, hosting utility links (Shipping & Returns, FAQ) in the teal accent for link color; this pairing is inferred rather than confirmed by extracted rules.

**badge** and **diet-claim-badge** are two related but distinct patterns: `badge` is a general pill (e.g., "New!" flagged on Scones/Sticks/Oatmeal Bars in the nav), while `diet-claim-badge` is a category-specific pattern for free-from claims (gluten-free, vegan, non-GMO, nut-free) that are central to this brand's positioning per the page copy; visual treatment for both is proposed, not measured.

**search** models the site search/predictive results drawer ("View all results" was present in extracted text), styled consistently with text-input.

## Responsive Behavior

This is a recommended, unmeasured breakpoint scheme — no responsive CSS or viewport behavior was captured from the source.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <768px | Single-column product grid, hamburger/drawer nav (a "Drawer menu" was referenced in extracted text, supporting a slide-out mobile nav pattern), carousels swipeable |
| tablet | 768–1023px | 2-column product grid, mega-menu collapses to accordion |
| desktop | 1024–1439px | Full mega-nav with flyout submenus, 3–4 column grids |
| wide | ≥1440px | Content max-width constrained (`.product` used `max-width:calc(1280px + 6.6vw)` in observed CSS), extra gutter |

Touch targets should be ≥44px height; `--button-height:50px` and `--button-height-small:40px` were observed as CSS custom properties, supporting a 40–50px tappable button range. Carousel controls (scroll buttons, swiper pagination) should collapse to swipe-only gestures below tablet width.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions (e.g., mega-menu flyouts, cart drawer, carousel swipe behavior) were observed.
- Many CSS values reference custom properties (`var(--color-background-header)`, `var(--font-logo)`, `var(--font-body)`) whose resolved values were not present in the supplied evidence; color and font role assignments above are inferred from the broader palette/font list, not confirmed bindings.
- Font role split (display serif vs. script logo vs. body sans) is inferred from font-family names present in the stylesheet; actual usage, weights, and whether these are licensed/self-hosted or third-party webfonts was not verified.
- All typography sizes, line-heights, and letter-spacing values are proposed defaults for a food DTC storefront, not measured pixel values, except where explicit `--button-height*` or `--swatch-size` variables were present.
- Rounded and spacing scales are proposed conventions, not extracted from the site's actual radius/spacing tokens.
- Mobile drawer menu, search overlay, and cart drawer visual treatments are proposed patterns based on textual references ("Drawer menu," "Your cart is empty") rather than observed markup/styles.
