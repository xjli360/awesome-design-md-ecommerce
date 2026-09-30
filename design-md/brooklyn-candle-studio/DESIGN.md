---
version: alpha
name: "Brooklyn Candle Studio"
source_url: "https://brooklyncandlestudio.com"
captured_at: "2026-09-28T05:06:40.704366+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Brooklyn Candle Studio's storefront evidence points to a warm, editorial luxury-goods aesthetic built on a near-black/white core (#000000, #1c1c1c, #ffffff) paired with soft warm neutrals (#f9f8f4, #efe3dc, #f3e8e4, #e8d6cc) that read as candle-wax cream, kraft, and blush tones. A muted grayscale system (#303030, #767474, #d9d9d9, #e5e5e5) supports body copy, dividers, and disabled states, while #c9a24e (gold) and #c4443b (terracotta) are treated here as inferred accent colors for seasonal badges, ratings, or promotional callouts, since the CSS shows them present but does not confirm their exact UI role. #c70000 appears tied to sale/promo messaging given the "WAREHOUSE SALE" and "on-sale" token names, so it is mapped to a sale/alert role. Typography is anchored by Miller Display (a serif family with Roman, Light, SemiBold, Bold and Italic cuts) for headline moments, contrasted with Helvetica/Helvetica Neue and Montserrat for UI chrome, navigation, and body text — matching the brand's stated positioning as a "luxury" handcrafted candle and home-fragrance line. Root-level tokens (--text-xs through --text-xl, container-gutter, section-vertical-spacing) confirm a compact, mobile-first type scale and generous section spacing, which this document extends into a full interpreted system. All layout proportions, hover/focus states, and breakpoints below are proposed conventions, not measured observations.

colors:
  primary: "#000000"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#767474"
  hairline: "#d9d9d9"
  surface-soft: "#f9f8f4"
  surface-card: "#efe3dc"
  on-primary: "#ffffff"
  accent-gold: "#c9a24e"
  accent-blush: "#f3e8e4"
  accent-terracotta: "#c4443b"
  sale: "#c70000"
  success: "#5cb85c"
  badge-neutral: "#e5e5e5"
typography:
  display-xl: {fontFamily: "Miller Display, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Miller Display, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 21px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "Helvetica, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 1px}
  button-md: {fontFamily: "AkzidenzGrotesk, Helvetica, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 1px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    overlayColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  scent-family-filter:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components
- **button-primary**: Solid black call-to-action (e.g. "SHOP NOW", "SUBSCRIBE NOW") matching the `--jdgm-write-review-bg-color: #000000` token; proposed hover state would darken toward `{colors.ink}` but is not confirmed by evidence.
- **button-secondary**: Outlined variant for lower-emphasis actions (e.g. "MANAGE SUBSCRIPTION"), inferred from the site's restrained black/white palette rather than directly observed.
- **text-input**: Used for search, newsletter, and account forms; hairline border and rounded-xs corners are proposed defaults consistent with the small `--jdgm-border-radius: 10` hint from review widget styling.
- **nav-bar**: Sticky header (confirmed via `--header-is-sticky: 1`) with a three-column grid (`primary-nav logo secondary-nav`) observed in the header CSS; logo width tokens (175px/210px) suggest a responsive logo scale-up on larger viewports.
- **product-card**: Warm beige card surface for candle/diffuser listings, using Montserrat title type and Helvetica price type; card structure (image, title, price, badge) is a proposed pattern for this product category, not directly observed in markup.
- **hero**: Full-width promotional banner matching the observed rotating announcement copy ("WAREHOUSE SALE", "CABIN COLLECTION", "GHOST PUMPKIN"); uses the warm off-white surface and large serif display type to convey seasonal, editorial merchandising.
- **footer**: Dark, high-contrast footer inferred from the ink/canvas pairing; content structure (links, newsletter, social) is proposed, not confirmed by supplied CSS.
- **badge / badge-sale**: On-sale and custom badges are explicitly tokenized (`--on-sale-badge-background`, `--custom-badge-background`, `--sold-out-badge-background`), so these two variants are grounded in evidence; colors map on-sale to black and sale-specific messaging to `{colors.sale}` as a proposed extension.
- **search**: Site search/predictive search surface, styled with soft warm background to match the overall product-discovery UI; proposed only.
- **scent-family-filter**: A pill-style filter control proposed for the "SHOP BY SCENT FAMILY" navigation (Aquatic, Citrus, Floral, etc.) seen in the nav text; no direct filter markup was supplied, so this is an inferred category-specific component.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column product grid; header collapses to hamburger + centered logo, matching the sidebar-nav CSS block observed. |
| Tablet | 640–1024px | 2-column product grid; nav-bar retains 3-column grid with reduced gutter. |
| Desktop | 1024–1440px | 3–4 column product grid; full primary/secondary nav visible, container-gutter at the observed 3rem (48px). |
| Wide | >1440px | Max-width content container centered; hero and section-vertical-spacing (3rem/48px observed) scale up to `{spacing.section}`. |

Touch targets are recommended at a minimum 44×44px for buttons and nav links. The mobile sidebar menu (`header-sidebar__linklist`) should collapse nested scent/collection menus into accordion panels, consistent with the "back-button" pattern seen in the CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is limited to static CSS rules and page text; no rendered layout, hover states, animations, or actual breakpoint values were observed.
- Font weight/style availability for Miller Display (Bold, SemiBold, Light, Italic variants) is inferred from class/family names only; licensing and actual font-file delivery were not verified.
- Several palette colors (e.g. `#1773b0`, `#1990c6`, `#20124d`, `#5cb85c`) may belong to third-party widgets (reviews, chat) rather than core brand styling; roles assigned here (e.g. success) are best-effort inferences.
- Spacing and rounded-corner scales beyond the explicitly observed tokens (`--text-xs`–`--text-xl`, `--container-gutter`, `--jdgm-border-radius: 10`) are proposed conventions for a cohesive system, not extracted measurements.
- Component structures (product-card, hero, footer, scent-family-filter) are category-appropriate proposals based on nav/text content, not confirmed DOM/CSS observations.
- Mobile interaction patterns (accordion behavior, drawer transitions) are described based on class naming conventions only, not verified interactive testing.
